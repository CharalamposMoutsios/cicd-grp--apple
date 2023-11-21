FROM python

WORKDIR /app

COPY . .

RUN pip install Flask apscheduler validators requests

ENTRYPOINT flask run --host=0.0.0.0