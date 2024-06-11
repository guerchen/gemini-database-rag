# gemini-database-rag

With this project I aim to build a multi-agent LLM that gives answers grounded to data found in a Postgres Database.

For this project, the data was generated using Google's Gemini and can be found in `gemini_database_app/assets/example.csv`

## How to run

1. Add you Gemini API Key to `docker-compose.yml`
2. Run:

```
docker-compose build --no-cache
```

3. Then run:
```
docker-compose up -d
```