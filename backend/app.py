from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from datetime import datetime
import os
from dotenv import load_dotenv
from apscheduler.schedulers.background import BackgroundScheduler
from api.scraper import scrape_aliexpress_products

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Configure database
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///2dollarstore.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev')

# Initialize database
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Import models
from models.product import Product
from models.order import Order

# Import routes
from api.products import products_bp
from api.orders import orders_bp
from api.scraper import scraper_bp

# Register blueprints
app.register_blueprint(products_bp, url_prefix='/api/products')
app.register_blueprint(orders_bp, url_prefix='/api/orders')
app.register_blueprint(scraper_bp, url_prefix='/api/scraper')

@app.route('/api/health')
def health_check():
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.utcnow().isoformat()
    })

if __name__ == '__main__':
    # Start the scheduler
    scheduler = BackgroundScheduler()
    scheduler.add_job(scrape_aliexpress_products, 'interval', days=1)
    scheduler.start()
    
    # Run the app with host and port configuration
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 5000))) 