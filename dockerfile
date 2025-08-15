FROM python:3.13.1

WORKDIR /app

COPY . /app/

RUN rm -rf /app/.venv

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "fast_app:app", "--host", "0.0.0.0", "--port", "8000"]
