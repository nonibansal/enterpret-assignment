## ENTERPRET ASSIGNMENT

### To Do
1. Add tests

### How to Run

```shell
make install
make model_hoster-run
make model_management-run
make model_executor-run
```

### Adding a pipeline
```shell
curl --location 'http://localhost:8081/v1/pipeline/' \
--header 'Content-Type: application/json' \
--data '{
    "name": "sentiment",
    "tenant": "curefit",
    "version": 1,
    "is_active": true,
    "url": "http://localhost:8080/v1/0"
}'
```

### Adding pipelines for a tenant
```shell
curl --location 'http://localhost:8081/v1/tenant-pipelines/' \
--header 'Content-Type: application/json' \
--data '{
    "tenant": "curefit",
    "pipelines": [0, 0, 0]
}'
```

### Getting prediction against a pipeline
```shell
curl --location 'http://localhost:8080/v1/0' \
--header 'Content-Type: application/json' \
--data '{
    "input": {
        "id": "12324",
        "text": "quality"
    }
}'
```

### Getting insights
```shell
curl --location 'http://localhost:8082/v1/insights' \
--header 'tenant: curefit' \
--header 'Content-Type: application/json' \
--data '{
    "record": {
        "id": "dggdggdg",
        "text": "quality"
    }
}'
```