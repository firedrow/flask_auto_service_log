FROM python:3.10-slim
WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY ./run.py /code/
COPY ./app /code/app/
COPY ./app/templates /code/app/templates/
COPY ./app/static /code/app/static/
CMD ["python", "/code/run.py"]
