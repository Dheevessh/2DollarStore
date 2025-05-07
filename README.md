# 2DollarStore

A full-stack web application that sells products at a fixed price of $2, sourced from various online marketplaces.

## Features

- Product catalog with items priced at exactly $2
- Shopping cart and checkout functionality
- Automatic product scraping from AliExpress
- Daily product updates
- Responsive React frontend
- Flask REST API backend
- SQLite database (upgradable to PostgreSQL)

## Project Structure

```
2DollarStore/
├── frontend/           # React frontend application
├── backend/           # Flask backend application
│   ├── api/          # REST API endpoints
│   ├── scraper/      # Product scraping scripts
│   └── models/       # Database models
└── docs/             # Documentation
```

## Setup Instructions

### Prerequisites

- Python 3.8+
- Node.js 16+
- npm or yarn

### Backend Setup

1. Navigate to the backend directory:
   ```bash
   cd backend
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

5. Initialize the database:
   ```bash
   flask db upgrade
   ```

6. Run the development server:
   ```bash
   flask run
   ```

### Frontend Setup

1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Set up environment variables:
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

4. Run the development server:
   ```bash
   npm start
   ```

## Development

- Backend API runs on http://localhost:5000
- Frontend development server runs on http://localhost:3000
- API documentation available at http://localhost:5000/api/docs

## Important Notes

- Shipping fees apply to all orders
- Estimated shipping time: 2-4 weeks
- Product prices are automatically adjusted to $2 regardless of source price
- Product catalog is updated daily via automated scraping

## License

MIT