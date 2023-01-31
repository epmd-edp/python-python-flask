FROM public.ecr.aws/docker/library/python:3.8.16-slim

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app.py /code

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port", "8080"]
