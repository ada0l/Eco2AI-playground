eco2ai-playground
=================

# Usage

1) Copy example.env to .env. And also edit it if you need

```bash
cp example.env .env
```

2) Run project via docker compose
```bash
docker compose up
```

3) You can find documentation of rest in http://locahost:8000/docs

4) Good luck, have fun

# Webhook (http://localhost:8000/ws)

Example of json about notification of new consumption:
```json
{"type":"new_consumption","project_id":"95139a23-3d83-4368-bb48-766aa1c1a7a2","data":{"duration":10.641446113586426,"power":1.9910377834923455e-6,"co2":8.820894692206139e-7}}
```
