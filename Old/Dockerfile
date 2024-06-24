FROM python:3.10

USER root

RUN apt-get update && apt-get install -yy nano curl && pip install pytest-playwright && playwright install-deps && playwright install

WORKDIR /test

# CMD [ "python3", "/test/test.py" ]
CMD [ "pytest" ]