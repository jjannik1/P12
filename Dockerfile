# Etapa de construcción
FROM python:3.11-slim AS build
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

# Etapa final
FROM python:3.11-slim
WORKDIR /app
COPY --from=build /app /app
EXPOSE 8000
RUN pip install --no-cache-dir -r requirements.txt
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "wsgi:app"]
