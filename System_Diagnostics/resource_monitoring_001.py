import threading
import psutil
import time
from datetime import datetime
# from .es_helpers import BulkSimpleIterator
import logging


# log when ever there is change in +/- 5% or every minute...or any trigger...
class ResourceLogger(threading.Thread):
    """description of class"""

    def __init__(self, index_id, doc_type, es, logger):
        self.index_id = index_id
        self.doc_type = doc_type
        self.process_id_list = {}
        threading.Thread.__init__(self)
        self.threadLock = threading.Lock()
        self.keep_running = True
        self.force_read = False
        self.delay = 10
        self.es = es
        self.logger = logger

        self.process_dict = {}

    def force_read(self):
        with self.threadLock:
            self.force_read = True

    # add combination of both.
    def add_new_process_id(self, process_id, func_name):
        with self.threadLock:
            pfunc = psutil.Process(process_id)
            self.process_id_list[process_id] = (func_name, pfunc)
            aaa = 1

    def remove_process_id(self, process_id):
        with self.threadLock:
            self.process_id_list.pop(process_id, None)

    def stop(self):
        self.keep_running = False

    def run(self):

        start_time = datetime.now()

        for id, (fun_name, pfunc) in self.process_id_list.items():
            self.process_dict[id] = []



        # self.logger.info('logger started')
        info = lambda total_mem, total_cpu, process_mem, process_cpu, total_python_process, child_process_info, timestamp, \
                      no_process: {'total_mem_usage': total_mem,
                                   'total_cpu_usage': total_cpu,
                                   'process_mem_usage': process_mem,
                                   'process_cpu_usage': process_cpu,
                                   "total_python_process": total_python_process,
                                   'child_process_info': child_process_info,
                                   "timestamp": timestamp,
                                   'no_process_running': no_process
                                   }
        data_list = []
        start_idx = 0
        end_idx = 0
        batch_size = 5
        while self.keep_running:
            # if self.force_read :
            #    self.force_read=False
            print('going to log data')
            total_cpu_used = psutil.cpu_percent()
            total_mem_used = psutil.virtual_memory().percent
            timestamp = datetime.utcnow().isoformat()
            process_total_cpu = 0
            process_total_mem = 0
            total_python_process = sum(
                [i.memory_percent() for i in psutil.process_iter() if str(i.name()).startswith("python")])
            child_info_list = []
            with self.threadLock:
                for id, (fun_name, pfunc) in self.process_id_list.items():
                    try:
                        process_cpu = pfunc.cpu_percent()
                        process_cpu_time = pfunc.cpu_times()
                        process_user = process_cpu_time.user
                        process_kernel = process_cpu_time.system
                        process_total = process_user + process_kernel

                        process_mem = pfunc.memory_percent()
                        process_total_cpu += process_cpu
                        process_total_mem += process_mem

                        current_time = datetime.now()

                        current_str = current_time.strftime("%m/%d/%Y, %H:%M:%S")
                        elapsed_time = (current_time - start_time).total_seconds()
                        #elapsed_str = elapsed_time.strftime("%m/%d/%Y, %H:%M:%S")

                        self.process_dict[id] = [process_total, process_cpu, current_time]

                        child_info_list.append(
                            {'current_time':current_str, 'elapsed_time':elapsed_time, 'fun_name': fun_name, 'cpu_usage': process_cpu, 'process_id': id, 'mem_usage': process_mem,
                             'cpu_time': process_cpu_time, 'process_cpu_total':process_total})
                    except:
                        # del self.process_id_list[id]
                        continue
            # data=info(total_mem_used,total_cpu_used,process_total_mem,process_total_cpu,total_python_process,child_info_list,timestamp,len(self.process_id_list.items()))

            data = (child_info_list)

            import json


            combined_cpu_time = 0
            combined_cpu_usage = 0
            current_time = None


            for item in self.process_dict.items():

                combined_cpu_time += item[1][0]
                combined_cpu_usage += item[1][1]
                current_time = item[1][2]



            print('TOTAL', current_time, combined_cpu_time, combined_cpu_usage)

            #print(json.dumps(data))
            data_list.append(data)
            bbb = 2

            '''
            if len(data_list)>batch_size:


                start_idx=end_idx
                end_idx=start_idx+len(data_list)
                index_iterator=list(range(start_idx,end_idx))
                data_iterator = data_list
                bulk_iter = BulkSimpleIterator(data_iterator, index_iterator, "monitoring_"+self.index_id, self.doc_type)
                print("pushing to elasticsearch")
                self.es.bulk(bulk_iter, refresh=True)
                data_list=[]
            '''
            time.sleep(self.delay)

        '''
        #push all the left data
        start_idx=end_idx
        end_idx=start_idx+len(data_list)
        index_iterator=list(range(start_idx,end_idx))
        data_iterator = data_list
        bulk_iter = BulkSimpleIterator(data_iterator, index_iterator, "monitoring_"+self.index_id, self.doc_type)
        self.es.bulk(bulk_iter, refresh=True)
        print('resource logger going to exit')
        '''


def find_process_id_by_name(process_name):
    '''
    Get a list of all the PIDs of a all the running process whose name contains
    the given string processName
    '''

    list_of_process_objects = []

    # Iterate over the all the running process
    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=['pid', 'name', 'create_time'])
            # Check if process name contains the given name string.
            if process_name.lower() in pinfo['name'].lower():
                list_of_process_objects.append(proc)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    return list_of_process_objects;




if __name__ == '__main__':
    rl = ResourceLogger(None, None, None, None)

    # Get CA daemon process.
    pid = 0
    proc = None
    processes = find_process_id_by_name('python')
    for process in processes:
        arguments = process.cmdline()
        for argument in arguments:
            if 'app_daemon.py' in argument:
                pid = process.pid
                proc = process

    rl.add_new_process_id(pid, 'parent_' + str(pid))


    # Get child processes
    child_processes = proc.children()
    for child_process in child_processes:
        pid = child_process.pid
        rl.add_new_process_id(child_process.pid, 'child_' + str(pid))







    #rl.add_new_process_id(10856, 'custom_name_jq')
    rl.run()
    a = 1
