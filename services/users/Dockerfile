# base image
FROM python:3.7.2-alpine

# set working directory (in image filesystem)
WORKDIR /usr/src/app

# add requirements and install them
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# add app
COPY . /usr/src/app

# run server on start
CMD python manage.py run -h 0.0.0.0
