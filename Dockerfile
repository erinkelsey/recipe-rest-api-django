FROM python:3.7-alpine 

ENV PYTHONUNBUFFERED 1 

COPY ./requirements.txt /requirements.txt 
RUN pip install -r /requirements.txt 

RUN mkdir /app 
WORKDIR /app 
COPY ./app /app

# add user to run the program
RUN adduser -D user 
# switch the user to the user created to run program
# therefore, not running as root user
USER user 