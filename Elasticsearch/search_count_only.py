#https://stackoverflow.com/questions/33830460/python-elasticsearch-how-to-include-search-type-count-in-a-query

import elasticsearch

URI = 'http://127.0.0.1:9200'

client = elasticsearch.Elasticsearch(URI)

#query
q = {'query':{'match_all':{}}}

#res = client.search(index = "indexname*", doc_type = "doc_type", body = q, size=0)
res = client.search(index = "index001", doc_type = "type001", body = q, size=0)

print(res)