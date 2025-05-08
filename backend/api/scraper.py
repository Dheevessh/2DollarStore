from flask import Blueprint, jsonify
from models.product import Product
from extensions import db
import requests
from bs4 import BeautifulSoup
import time
import random
import os
from datetime import datetime

scraper_bp = Blueprint('scraper', __name__)

def scrape_aliexpress_products():
    # This is a simplified version. In production, you'd want to use Selenium
    # or a proper scraping service to handle JavaScript and avoid being blocked
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    # Example search URL (you'll need to adjust this based on AliExpress's current structure)
    search_url = "https://www.aliexpress.com/wholesale?SearchText=cheap+items&minPrice=0.01&maxPrice=1.50"
    
    try:
        response = requests.get(search_url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # This is a placeholder for the actual scraping logic
        # You'll need to inspect AliExpress's HTML structure and adjust accordingly
        products = []
        
        # Example product extraction (adjust selectors based on actual HTML)
        for item in soup.select('.product-item'):  # Adjust selector
            try:
                title = item.select_one('.product-title').text.strip()
                price = float(item.select_one('.product-price').text.strip().replace('$', ''))
                image_url = item.select_one('img')['src']
                source_url = item.select_one('a')['href']
                
                if price <= 1.50:  # Only include items under $1.50
                    products.append({
                        'name': title,
                        'price': 2.00,  # Always $2 in our store
                        'description': f'Imported from AliExpress. Original price: ${price:.2f}',
                        'image_url': image_url,
                        'aliexpress_url': source_url,
                        'is_active': True
                    })
            except (AttributeError, ValueError) as e:
                continue
        
        return products
    except Exception as e:
        print(f"Error scraping AliExpress: {str(e)}")
        return []

@scraper_bp.route('/refresh', methods=['POST'])
def refresh_products():
    # Deactivate all current products
    Product.query.update({'is_active': False})
    
    # Scrape new products
    new_products = scrape_aliexpress_products()
    
    # Add new products to database
    for product_data in new_products:
        product = Product(**product_data)
        db.session.add(product)
    
    db.session.commit()
    
    return jsonify({
        'message': f'Successfully refreshed {len(new_products)} products',
        'timestamp': datetime.utcnow().isoformat()
    })

@scraper_bp.route('/status', methods=['GET'])
def get_scraper_status():
    active_products = Product.query.filter_by(is_active=True).count()
    total_products = Product.query.count()
    
    return jsonify({
        'active_products': active_products,
        'total_products': total_products,
        'last_update': datetime.utcnow().isoformat()
    }) 