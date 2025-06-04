# Usa una imagen base de Python
FROM python:3.10-slim

# Establece el directorio de trabajo
WORKDIR /app

# Copia los archivos del proyecto
COPY . .

# Instala las dependencias
RUN pip3 install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Expone el puerto interno (dentro del contenedor)
EXPOSE 7000

# Comando para ejecutar la app
CMD ["python", "app.py"]
