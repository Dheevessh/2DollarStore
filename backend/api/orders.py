from flask import Blueprint, jsonify, request
from models.order import Order, OrderItem
from models.product import Product
from app import db

orders_bp = Blueprint('orders', __name__)

@orders_bp.route('/', methods=['POST'])
def create_order():
    data = request.get_json()
    
    # Validate required fields
    required_fields = ['email', 'shipping_address', 'items']
    if not all(field in data for field in required_fields):
        return jsonify({'error': 'Missing required fields'}), 400
    
    # Create order
    order = Order(
        email=data['email'],
        shipping_address=data['shipping_address'],
        total_amount=len(data['items']) * 2.00  # $2 per item
    )
    
    # Create order items
    for item in data['items']:
        product = Product.query.get(item['product_id'])
        if not product:
            return jsonify({'error': f'Product {item["product_id"]} not found'}), 404
        
        order_item = OrderItem(
            product_id=product.id,
            quantity=item.get('quantity', 1),
            price=2.00  # Always $2
        )
        order.items.append(order_item)
    
    db.session.add(order)
    db.session.commit()
    
    return jsonify(order.to_dict()), 201

@orders_bp.route('/<int:order_id>', methods=['GET'])
def get_order(order_id):
    order = Order.query.get_or_404(order_id)
    return jsonify(order.to_dict()) 