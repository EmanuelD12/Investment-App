from flask import Flask
from flask_cors import CORS
from api.market_data import market_data_bp

def create_app():
    app = Flask(__name__)
    CORS(app)  # Enable CORS for all routes
    
    # Register blueprints
    app.register_blueprint(market_data_bp, url_prefix='/api/market')
    
    @app.route('/')
    def health_check():
        return {'status': 'healthy', 'message': 'StockSense API running'}
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)