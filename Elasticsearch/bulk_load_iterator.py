from . import elastic_service

class BulkSimpleIterator(object):
    def __init__(self,dociterator, iditerator, indexname, doctype):
        self.dociter = dociterator
        self.iditer = iditerator
        self.indexname = indexname
        self.doctype = doctype

    def __iter__(self):
        for index, curr_doc in zip(self.iditer, self.dociter):
           index_data = {'index':{  '_index': self.indexname,
                   '_type': self.doctype,
                   '_id': index}}
           yield index_data
           yield curr_doc



all_text = ['alpha bravo', 'charlie delta']
all_ids = [0, 1]
doc_type = 'jq_doc'
index_name = 'jq_bulk_001'



bulk_iter=BulkSimpleIterator(all_text,all_ids,index_name,doc_type)
es=elastic_service.connect(timeout=600)
es.indices.delete(index=index_name,ignore=[400,404])
es.bulk(bulk_iter, refresh=True)