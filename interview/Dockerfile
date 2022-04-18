FROM python:3.8.5-alpine

ENV HOME=/home/app
ENV APP_HOME=/home/app/interview

# Create directory for the app user
RUN mkdir -p $HOME $APP_HOME

# Create the app user
RUN addgroup -S app && adduser -S -G app app

WORKDIR $HOME

COPY Pipfile Pipfile.lock ./

COPY . $APP_HOME

# To make layers and help and make process agile, for production docker image should be '&&'
RUN chown -R app:app $HOME

RUN pip install --upgrade pip --no-cache-dir
RUN pip install pipenv --no-cache-dir
RUN pipenv install

COPY setup.py $HOME
RUN pipenv install .

EXPOSE 5000

USER app

CMD ["pipenv", "run", "gunicorn", "--workers", "8", "--bind", "0.0.0.0:5000", "interview:create_app('DevConfig')", "--max-requests", "10000", "--timeout", "5", "--keep-alive", "5", "--log-level", "info"]
