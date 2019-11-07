from elasticsearch import Elasticsearch
import elasticsearch.helpers as helpers
import elasticsearch

# https://stackoverflow.com/questions/35182403/bulk-update-with-pythons-elasticsearch

# https://elasticsearch-py.readthedocs.io/en/master/helpers.html#bulk-helpers

# https://stackoverflow.com/questions/20288770/how-to-use-bulk-api-to-store-the-keywords-in-es-by-using-python

es = Elasticsearch(hosts=[{'host': 'localhost', 'port': 9200}])

ids = [598939, 598940, 598941]

# NOTE the (...) round brackets. This is for a generator.
k = ({
    "_op_type": "update",
    "_index": "mp__jeb001",
    "_type": "items",
    "_id": idx,
    "doc": {"cows4": "a"},
} for idx in ids)

helpers.bulk(es, k)
