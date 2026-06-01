# backend/app/utils/helpers.py

from datetime import datetime


class Helpers:

    @staticmethod
    def current_time():

        return str(datetime.utcnow())

    @staticmethod
    def success(message, data=None):

        return {
            "success": True,
            "message": message,
            "data": data
        }

    @staticmethod
    def error(message):

        return {
            "success": False,
            "message": message
        }

    @staticmethod
    def stock_status(stock):

        if stock <= 0:
            return "Out of Stock"

        if stock < 10:
            return "Low Stock"

        return "In Stock"