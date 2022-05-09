FROM python:3.8-alpine
WORKDIR /api
ADD . /api
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
CMD ["python3","api.py"]
