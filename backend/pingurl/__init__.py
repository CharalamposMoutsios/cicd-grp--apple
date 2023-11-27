import atexit
from flask import Flask
from apscheduler.schedulers.background import BackgroundScheduler
from pingurl import watched_urls

app = Flask(__name__)
scheduler = BackgroundScheduler(daemon=True)
scheduler.start()

# Shut down the scheduler when exiting the app
atexit.register(scheduler.shutdown())
