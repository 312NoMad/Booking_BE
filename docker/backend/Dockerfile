FROM python:3.9
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY requirements/base.txt /app/requirements/
COPY requirements/dev.txt /app/requirements/
COPY requirements/prod.txt /app/requirements/
RUN pip install --upgrade pip
RUN pip install -r /app/requirements/prod.txt
RUN pip install psycopg2-binary
ADD ./docker /app/docker
ADD ./ /app/backend
RUN ["chmod", "+x", "/app/docker/backend/wsgi-entrypoint.sh"]
EXPOSE 8000