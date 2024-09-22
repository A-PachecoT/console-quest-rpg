FROM python:3.12-slim

# Establecer el directorio de trabajo en /app
WORKDIR /app

# Copiar los archivos de requerimientos
COPY requirements.txt .

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar todo el contenido del directorio backend al contenedor
COPY . .

# Comando para correr la aplicación FastAPI
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
