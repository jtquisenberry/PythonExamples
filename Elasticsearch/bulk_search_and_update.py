from elasticsearch import Elasticsearch
import elasticsearch.helpers as helpers
import elasticsearch


# Make connection
es = Elasticsearch(hosts=[{'host': '10.12.239.136', 'port': 9200, 'timeout':600}])


# Get data
index_name = 'mp__jeb002'
doc_type = 'pii_ent_items'

tag = 'all'

body = ''
if tag == 'all':
    body = {
        "query": {
            "match_all": {}
        }
    }
else:
    body = {
        "_source": [
            "pii"
        ],
        "query": {
            "match_phrase": {
                "pii.major_tag": "{0}".format(tag)
            }
        }
    }

pii_documents = es.search(index=index_name, doc_type=doc_type, size=9999,
                                          _source_include=['pii'], body=body)


print(len(pii_documents['hits']['hits']))

ids = []
for pii_document in pii_documents['hits']['hits']:
    ids.append(pii_document['_id'])
    a = 1


# Update data
# Note the operation of "update". Without it, entire documents would be overwritten and loaded.
k = ({
    "_op_type": "update",
    "_index": "mp__jeb002",
    "_type": "items",
    "_id": idx,
    "doc": {"subset": "20191107"},
} for idx in ids)

helpers.bulk(es, k)

print('Done')
