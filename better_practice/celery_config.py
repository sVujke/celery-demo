from celery import celery

app = Celery('celery_config', broker='redis://localhost:6379/0', include=['celery_blog'])