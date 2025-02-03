# myrepo

### Info on deployment url

I did not have any deployment url as I have finished using my free tier resources on Azure and AWS.
Thus, I am still waiting for my newly opened AWS and Azure account to be validated.

### asr-api

To run the asr api locally:

```
flask --app asr_api run --port=8001 --debug --reload
```

To run the asr api in production as a server:

```
waitress-serve --host localhost --port 8001 asr_api:app
```


To run the script that decodes the mp3 files:

```
python asr\cv-decode.py
```

### Command to add a new node to the existing elastic search cluster

bin\elasticsearch --enrollment-token eyJ2ZXIiOiI4LjE0LjAiLCJhZHIiOlsiMTcyLjIyLjExMi4xOjkyMDAiXSwiZmdyIjoiMjQ1ZGVkZThjZTlhMjQ0MjM1ZWIwYzM1NWY1MzhmNWQzOTFkZDMzYjRhOTEzODM5OWEwNTdlZGZmMjUyNjk4MSIsImtleSI6IlFPcmF1NVFCRDhZZWtkY2FNR2FlOkpaWmpnanNSUkN5OWhXek82aWhIeUEifQ==

### Command to run the 2 elastic search nodes and the SearchUI frontend

Run first node:

1. Navigate to the directory, elastic-backend/node-1/bin
2. Run elasticsearch by typing in the command, `elasticsearch`.
3. Use one of the URLs in the next section to check the status of the elastic search cluster. 

Run second node (open a separate terminal):

1. Navigate to the directory, elastic-backend/node-2/bin
2. Run elasticsearch by typing in the command, `elasticsearch`.
3. Use one of the URLs in the next section to check the status of the elastic search cluster.

Run SearchUI frontend (open a separate terminal):

1. Navigate to the directory, search-ui.
2. Run `npm run start`.
3. Once it starts running, use your browser to go to [localhost:3000](http://localhost:3000) to see the web app.

### URLs to test status of the elastic search service:

[To check status of nodes](http://localhost:9200/_cat/nodes?v)
[To check status of cluster](http://localhost:9200/_cluster/health?pretty)
[To check status of "cv-transcriptions" index](http://localhost:9200/cv-transcriptions)
[To check the information about the documents stored in the "cv-transcriptions" index](http://localhost:9200/cv-transcriptions/_search)

### Elastic search backend service credential

username: elastic
password: i3Hr8jp+7f_*RCJDycfp
