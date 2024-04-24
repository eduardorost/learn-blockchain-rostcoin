FROM python:3.10-slim

WORKDIR /app

COPY poetry.lock pyproject.toml /app/

RUN pip install poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-dev

COPY . /app

EXPOSE 5000

ENV FLASK_APP=main.py

CMD ["poetry", "run", "python", "main.py"]
