FROM nikolaik/python-nodejs:python3.8-nodejs12
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
RUN cd /code/front && npm install && npm run build
CMD uwsgi --http 0.0.0.0:8000 --wsgi-file project/wsgi.py --static-map /static=/code/static
