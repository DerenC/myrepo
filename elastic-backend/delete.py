from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk, BulkIndexError

es = Elasticsearch("http://localhost:9200")
index_name = "cv-transcriptions"

if es.indices.exists(index=index_name):
	resp = es.indices.delete(index=index_name)

if resp and resp.get("acknowledged"):
	print(f"Index {index_name} deleted.")
else:
	print(f"Index {index_name} not deleted.")