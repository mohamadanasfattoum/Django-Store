from celery import shared_task

import time


@shared_task
def send_emails():
    for x in renge (5):
        time.sleep(1)
        print(f'sending emails for user number {x}')