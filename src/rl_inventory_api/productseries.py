from sqlite3 import connect


class ProductSeries:
    def __init__(self, product_series: list):
        self.product_series = product_series

    @staticmethod
    def from_database():
        connection = connect('product_series..sqlite3')
        connection.execute('select * from product_series')
        return ProductSeries()

    @staticmethod
    def generate_product_series():
        from rl_insider_api import RlInsider
        connection = connect('product_series.sqlite3')
        cursor = connection.cursor()
        connection.execute('CREATE TABLE IF NOT EXISTS product_series (product_series smallint);')
        connection.execute('SELECT * FROM product_series;')
        connection.commit()
        rl_insider = RlInsider.connect_pc()


    def auto_connection(self):
        pass
