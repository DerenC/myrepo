from elasticsearch import Elasticsearch

es = Elasticsearch(
	"https://localhost:9200",
	basic_auth=("elastic","i3Hr8jp+7f_*RCJDycfp"),
	ca_certs="node-1/config/certs/http_ca.crt"
)
index_name = "cv-transcriptions"

response = es.count(index=index_name)
print(f"There are now {response['count']} documents in the {index_name} index.")

r = es.search(index=index_name, query={"match_all": {}})
print(f"Total hits: {r['hits']['total']['value']}")