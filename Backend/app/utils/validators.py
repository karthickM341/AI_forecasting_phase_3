import re

class Validator:

    @staticmethod
    def validate_email(email):

        pattern = r"^[\\w\\.-]+@[\\w\\.-]+\\.\\w+$"

        return re.match(pattern, email)


    @staticmethod
    def validate_password(password):

        return len(password) >= 6


    @staticmethod
    def validate_stock(stock):

        return stock >= 0