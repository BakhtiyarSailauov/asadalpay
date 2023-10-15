class Order:
    def __init__(self, api):
        self.api = api

    def create(self, products, currency="KZT", external_id=None, description=None,
               attempts=10, mcc=None, capture_method="AUTO", back_url=None,
               notify_url=None, receiver=None):
        endpoint = "/api/orders/create-order"
        order_data = {
            "products": products,
            "currency": currency,
            "external_id": external_id,
            "description": description,
            "attempts": attempts,
            "mcc": mcc,
            "capture_method": capture_method,
            "back_url": back_url,
            "notify_url": notify_url,
            "receiver": receiver,
        }
        order_data = {k: v for k, v in order_data.items() if v is not None}
        return self.api._make_request("post", endpoint, data=order_data)

    def get_by_uuid(self, order_uuid):
        endpoint = f"/api/orders/{order_uuid}"
        return self.api._make_request("get", endpoint)
