# Usar una imagen base
FROM python:3.14-bookworm
# Establecemos la carpeta de trabajo
WORKDIR /app
# Copiando archivos del proyecto al contnedor
COPY . .
# Instalando las dependencias
RUN pip install -r requirements.txt
# Puerto que el contenedor escuchará
EXPOSE 5000
# Comando por defecto para ejecutar el contenedor
CMD ["python", "app.py"]
