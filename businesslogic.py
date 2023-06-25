from dataaccess import DataAccess

class ProductLogic:
    def __init__(self):
        self.data_access = DataAccess()

    def insert_product(self, first_name, last_name, product_name):
        self.data_access.insert_product(first_name, last_name, product_name)

    def get_purchases(self):
        purchases = self.data_access.get_purchases()
        purchase_list = []
        for purchase in purchases:
            purchase_list.append({
                'firstName': purchase[0],
                'lastName': purchase[1],
                'productName': purchase[2],
                'productPrice': purchase[3]
            })
        return purchase_list

    def get_purchase_history(self, full_name):
        history = self.data_access.get_purchase_history(full_name)
        return history
