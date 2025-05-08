# Koristi Python 3.12 kao bazni image
FROM python:3.12-slim

# Postavi radni direktorijum u kontejneru
WORKDIR /app

# Kopiraj requirements.txt i instaliraj zavisnosti
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Kopiraj ostatak aplikacije
COPY . .

# Izloži port 8000
EXPOSE 8000

# Komanda za pokretanje aplikacije
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]