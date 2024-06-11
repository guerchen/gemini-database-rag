FROM python:3.10

WORKDIR /gemini_database_rag

COPY ./requirements.txt /gemini_database_rag/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /gemini_database_rag/requirements.txt

COPY . .

CMD ["uvicorn", "gemini_database_rag.main:app", "--host", "0.0.0.0", "--port", "8000"]