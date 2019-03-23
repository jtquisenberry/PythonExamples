from elasticsearch import Elasticsearch
import elasticsearch.helpers as helpers
import elasticsearch

# https://stackoverflow.com/questions/35182403/bulk-update-with-pythons-elasticsearch

# https://elasticsearch-py.readthedocs.io/en/master/helpers.html#bulk-helpers

# https://stackoverflow.com/questions/20288770/how-to-use-bulk-api-to-store-the-keywords-in-es-by-using-python

es = Elasticsearch(hosts=[{'host': 'localhost', 'port': 9200}])

# NOTE the (...) round brackets. This is for a generator.
k = ({
    "_index": "nginx",
    "_type": "logs",
    "_id": idx,
    "_source": es_nginx_d,
} for idx, es_nginx_d in [(0,0)(1,1)])

helpers.bulk(es, k)