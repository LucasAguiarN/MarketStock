from flask import request, jsonify, make_response
from flask_jwt_extended import jwt_required, get_jwt_identity
from src.Application.Service.report_service import ReportService

class ReportController:
    @staticmethod
    @jwt_required()
    def get_sales_summary():
        seller_id = get_jwt_identity()
        
        period = request.args.get('period', 'month').lower()
        
        valid_periods = ['today', 'week', 'month']
        if period not in valid_periods:
            return make_response(jsonify({"erro": f"Período inválido. Use um de: {', '.join(valid_periods)}"}), 400)

        summary_data = ReportService.get_sales_summary(seller_id, period)

        return make_response(jsonify({
            "report_type": "sales_summary",
            "period": period,
            "data": summary_data
        }), 200)

    @staticmethod
    @jwt_required()
    def get_top_selling_products():
        seller_id = get_jwt_identity()

        try:
            limit = request.args.get('limit', 5, type=int)
            if limit <= 0:
                raise ValueError()
        except (ValueError, TypeError):
            return make_response(jsonify({"erro": "O parâmetro 'limit' deve ser um número inteiro positivo."}), 400)

        products_data = ReportService.get_top_selling_products(seller_id, limit)

        return make_response(jsonify({
            "report_type": "top_selling_products",
            "limit": limit,
            "data": products_data
        }), 200)

    @staticmethod
    @jwt_required()
    def get_low_stock_products():
        seller_id = get_jwt_identity()

        try:
            threshold = request.args.get('threshold', 10, type=int)
            if threshold < 0:
                raise ValueError()
        except (ValueError, TypeError):
            return make_response(jsonify({"erro": "O parâmetro 'threshold' deve ser um número inteiro não-negativo."}), 400)

        products_data = ReportService.get_low_stock_products(seller_id, threshold)

        return make_response(jsonify({
            "report_type": "low_stock_products",
            "threshold": threshold,
            "data": products_data
        }), 200)