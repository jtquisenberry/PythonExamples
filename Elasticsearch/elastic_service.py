
ES_HOSTS = ['127.0.0.1']

from elasticsearch import Elasticsearch


def connect(timeout=60):
    return Elasticsearch(hosts=ES_HOSTS, timeout=timeout, max_retries=3, retry_on_timeout=True)