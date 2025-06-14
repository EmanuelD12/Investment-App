from flask import Blueprint, jsonify, request
from utils.data_fetcher import get_stock_data

market_data_bp = Blueprint('market_data', __name__)

@market_data_bp.route('/quote/<symbol>', methods=['GET'])
def get_quote(symbol):
    try:
        data = get_stock_data(symbol, function='GLOBAL_QUOTE')
        return jsonify(data)
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@market_data_bp.route('/historical/<symbol>', methods=['GET'])
def get_historical(symbol):
    try:
        outputsize = request.args.get('outputsize', 'compact')
        data = get_stock_data(symbol, function='TIME_SERIES_DAILY', outputsize=outputsize)
        return jsonify(data)
    except Exception as e:
        return jsonify({'error': str(e)}), 400
