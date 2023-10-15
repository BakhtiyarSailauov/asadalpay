import os
import requests_mock
import pytest
from asadalpay.api import AsadalPayAPI
from asadalpay.models.order import Order


def get_api_key(filename='asadalpay_api_key.txt'):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, filename)
    with open(file_path, 'r') as file:
        return file.read().strip()


@pytest.fixture
def order_api():
    api_key = get_api_key()
    api_instance = AsadalPayAPI(api_key=api_key)
    return Order(api=api_instance)


@requests_mock.Mocker()
def test_create_order(order_api, mock):
    # Мокаем HTTP ответ.
    order_response = {
        "products": [{"name": "test_product", "price": 100}],
        "currency": "KZT",
        "description": "Test Order"
    }
    mock.post("https://api-dev.asadalpay.com/api/orders/create-order", json=order_response)

    # Подготовим данные для заказа.
    products = [{"name": "TestProduct", "price": 100}]
    currency = "KZT"
    description = "Test Order"

    # Создаем заказ и проверяем ответ.
    response = order_api.create(products=products, currency=currency, description=description)
    assert response == order_response


@requests_mock.Mocker()
def test_get_order_by_uuid(order_api, mock):
    # Мокаем HTTP ответ.
    order_uuid = "test_uuid"
    order_response = {
        "uuid": order_uuid,
        "products": [{"name": "test_product", "price": 100}],
        "currency": "KZT",
        "description": "Test Order"
    }
    mock.get(f"https://api-dev.asadalpay.com/api/orders/{order_uuid}", json=order_response)

    # Запрашиваем информацию о заказе и проверяем ответ.
    response = order_api.get_by_uuid(order_uuid=order_uuid)
    assert response == order_response
