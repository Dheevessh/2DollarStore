from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger
import requests
import os
from datetime import datetime

def refresh_products():
    try:
        response = requests.post('http://localhost:5000/api/scraper/refresh')
        print(f"Products refreshed at {datetime.utcnow()}: {response.json()}")
    except Exception as e:
        print(f"Error refreshing products: {str(e)}")

def start_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(
        refresh_products,
        trigger=IntervalTrigger(hours=24),
        id='refresh_products',
        name='Refresh products daily',
        replace_existing=True
    )
    scheduler.start()
    print("Scheduler started. Products will be refreshed daily.")

if __name__ == '__main__':
    start_scheduler() 