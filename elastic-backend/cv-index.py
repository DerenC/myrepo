from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk, BulkIndexError

import csv

fieldTypes = {
	"filename": "text",
	"text": "text",
	"up_votes": "integer",
	"down_votes": "integer",
	"age": "text",
	"gender": "text",
	"accent": "text",
	"duration": "float",
	"generated_text": "text",
}

mappings = {
	"properties": {
		field: {"type": fieldType}
		for field, fieldType in fieldTypes.items()
	}
}

csv_filepath = "../asr/cv-valid-dev.csv"
es = Elasticsearch(
	"https://localhost:9200",
)

index_name = "cv-transcriptions"

if es.indices.exists(index=index_name):
	resp = es.indices.delete(index=index_name)

es.indices.create(index=index_name, mappings=mappings, ignore=400)
print(f"\nIndex {index_name} created.")

with open(csv_filepath, mode='r', encoding='utf-8') as csv_file:
	csv_reader = csv.DictReader(csv_file)

	documents = [
		{
			"_index": index_name,
			"_source": {
				field: row[field] for field in fieldTypes
			}
		}
		for row in csv_reader
	]

try:
	success, _ = bulk(es, documents)
	print(f"Successfully bulk indexed {success} documents.")
except BulkIndexError as e:
	print("Bulk indexing failed.")
	for error in e.errors[:2]:
		print(error)

