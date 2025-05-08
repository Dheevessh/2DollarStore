from app import app
from apscheduler.schedulers.background import BackgroundScheduler
from api.scraper import scrape_aliexpress_products

# Start the scheduler
scheduler = BackgroundScheduler()
scheduler.add_job(scrape_aliexpress_products, 'interval', days=1)
scheduler.start()

if __name__ == "__main__":
    app.run() 