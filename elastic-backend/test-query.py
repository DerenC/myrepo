from elasticsearch import Elasticsearch

es = Elasticsearch(
	"https://localhost:9200",
	basic_auth=("elastic","i3Hr8jp+7f_*RCJDycfp"),
	ca_certs="node-1/config/certs/http_ca.crt"
)
index_name = "cv-transcriptions"

query = {
    "query": {
        "match": {
            # "filename": "cv-valid-dev/sample-000926.mp3"
            "accent": "england"
			# "text": "the"
        }
    }
}
response = es.search(index=index_name, body=query)

docs = list(map(lambda doc : doc["_source"], response["hits"]["hits"]))

print(len(docs))

for d in docs:
	print(d)
