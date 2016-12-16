from celery_config import app
import random

@app.task
def add(a, b):
    return a + b

def add_listed(list):
	for i in list:
		add.delay(i, random.randint(0,10))