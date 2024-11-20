FROM python:3.12.6-alpine

#define o working dir
WORKDIR /app_desafio_final

#instala as dependencias
COPY ./requirements.txt /app_desafio_final
RUN pip install --no-cache-dir --upgrade -r requirements.txt

#copia o resto do script
COPY . /app_desafio_final

ENV PORT=8080

EXPOSE 8080

#roda o servidor
CMD python main.py

