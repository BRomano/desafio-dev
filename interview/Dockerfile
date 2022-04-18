FROM python:3.8.5-alpine

ENV HOME=/home/app/
ENV APP_HOME=/home/app/interview/

# Create directory for the app user
RUN mkdir -p $HOME $APP_HOME

# Create the app user
RUN addgroup -S app && adduser -S -G app app

WORKDIR $HOME
COPY Pipfile Pipfile.lock ./

COPY . $APP_HOME

# To make layers and help and make process agile, for production docker image should be '&&'
RUN chown -R app:app $HOME

RUN apk update && apk add --virtual build-deps gcc python3-dev musl-dev && apk add mariadb-dev

RUN pip install --upgrade pip --no-cache-dir
RUN pip install pipenv --no-cache-dir
RUN pipenv install --system

COPY setup.py $HOME
RUN pip install .

RUN apk del build-deps
EXPOSE 5000

#USER app
