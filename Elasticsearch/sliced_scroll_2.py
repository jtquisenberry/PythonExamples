# Demonstrates multiprocessing with a sliced scroll.

from multiprocessing import Pool, TimeoutError, Manager
import multiprocessing
import time
import os
from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search
from elasticsearch_dsl.query import MatchAll, Q
import datetime


ES_SERVER_NAME = 'http://127.0.0.1:9200'
DOCUMENT_COUNT = 9500

def get_document_text_slice(self, slice_count=0, slice_size=1000, slice_id=0):

    s = Search(using=self.es, index=self.index, doc_type='items').query(Q({"match_all": {}})).params(
        scroll='5m', size=slice_size)
    # s = s.extra(slice={"id": work, "max": 1})
    s = s.extra(slice={'id': slice_id, 'max': slice_count})

    response = s.execute()

    # print("MIN ID:", min(map(int, ([h['_id'] for h in response.hits.hits]))))
    # print("MAX ID:", max(map(int, ([h['_id'] for h in response.hits.hits]))))
    # print("ID COUNT:", len([h['_id'] for h in response.hits.hits]))

    for document in response:
        if 'itemText' in document:
            yield document.meta.id, document['itemText']
        else:
            yield document.meta.id, ''


def scan_parallel(slice_parameters):

    slice_id = slice_parameters[0]
    slice_count = slice_parameters[1]
    slice_size = slice_parameters[2]

    # Parallelism data
    print('')
    print('Begin SCANNING. PID: {0}'.format(os.getpid()))

    # Create a new Elasticsearch client because the ES client does not handle fork well.
    # https://elasticsearch-py.readthedocs.io/en/master/
    client = Elasticsearch(ES_SERVER_NAME)
    client.query = {"query": {"match_all":{}}}

    # The features of each document in the chunk
    features = []

    for document_id, text in client.get_document_text_slice(slice_count=slice_count,
                                                            slice_size=slice_size, slice_id=slice_id):

        # TODO: Do Work
        pass


if __name__ == '__main__':

    start_time = datetime.datetime.now()

    # CPU core count
    print("CPU Count", multiprocessing.cpu_count())

    # Get document count
    client = Elasticsearch(ES_SERVER_NAME)
    query = {"query": {"match_all": {}}}

    document_count = DOCUMENT_COUNT
    chunk_size = 1000
    chunk_count = document_count // 1000 if document_count % chunk_size == 0 else (document_count // 1000) + 1
    chunk_list = range(0, chunk_count)

    #iterable of [slice ID, slice count, slice size]
    chunk_list = [[i, chunk_count, chunk_size] for i in chunk_list]

    # start 4 worker processes
    with Pool(processes=3) as pool:

        # Use a manager with the pool.
        with Manager() as manager:
            # list attached to the manager.
            managed_list = manager.list(range(0, chunk_count))

            # list of results
            # map applies function f to each element in chunk_list
            print(pool.map(func=scan_parallel, iterable=chunk_list))

    end_time = datetime.datetime.now()
    elapsed_time = end_time - start_time

    print("Multiprocessing pool is closed")
    print("DONE")
    print(elapsed_time.total_seconds())
    a = 1

