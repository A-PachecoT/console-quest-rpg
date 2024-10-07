FROM python:3.12-slim

# Establecer el directorio de trabajo en /app
WORKDIR /src/app

# Copiar los archivos de requerimientos
COPY requirements.txt .

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt


# Copiar todo el contenido del directorio backend al contenedor
COPY . .

# Set environment variables for testing
ENV MONGO_URL=mongodb://mongodb:27017
ENV MONGO_DB_NAME=testdb

# Ejecutar pytest
RUN python -m pytest tests/

# Comando para correr la aplicación FastAPI
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
