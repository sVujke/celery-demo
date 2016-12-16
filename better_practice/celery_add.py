from celery_config import app
import random

@app.task
def add(a, b):
    return a + b

def add_listed(listn):
	for i in listn:
		add.delay(i, random.randint(0,10)

if __name__ == "__main__":
    add_listed([5,6,7,8])