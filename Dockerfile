# pull the official base image
FROM python:3.10.9

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
COPY ./requirements.txt .
RUN pip install -r requirements.txt
#

COPY ./bookshop /app

WORKDIR /app
## copy project
#COPY . /usr/src/bookshop
#
#EXPOSE 8000
#
#
#CMD ["python", "manage.py", "migrate"]
#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]