# Клиент AsadalPay API

Простой и интуитивно понятный Python-клиент для взаимодействия с API AsadalPay.

## Содержание

- [Установка](#установка)
- [Использование](#использование)
  - [Инициализация](#инициализация)
  - [Создание заказа](#создание-заказа)
  - [Получение заказа по UUID](#получение-заказа-по-uuid)
- [Тестирование](#тестирование)
- [Участие в проекте](#участие-в-проекте)
- [Лицензия](#лицензия)

## Установка

Для установки пакета `asadalpay` просто используйте `pip`:

```bash
pip install asadalpay
```

Или если вы хотите установить из исходного кода:

```bash
git clone https://github.com/[ваш_никнейм]/asadalpay.git
cd asadalpay
pip install .
```

## Использование

### Инициализация

Чтобы начать использовать клиент AsadalPay API, вы должны инициализировать его с помощью вашего API-ключа:

```python
from asadalpay.api import AsadalPayAPI

api_key = 'ВАШ_API_КЛЮЧ'
api_client = AsadalPayAPI(api_key=api_key)
```

### Создание заказа

Создайте заказ, предоставив детали продукта, валюту и описание:

```python
from asadalpay.models.order import Order

order_api = Order(api=api_client)

products = [{"name": "Товар1", "price": 1000}]
currency = "KZT"
description = "Тестовый заказ"

response = order_api.create(products=products, currency=currency, description=description)
```

### Получение заказа по UUID

Получите детали заказа, используя UUID заказа:

```python
order_uuid = 'пример_order_uuid'
response = order_api.get_by_uuid(order_uuid=order_uuid)
```

Для более детального использования и других функций обратитесь к [документации API](./docs/api.md).

## Тестирование

Чтобы запустить набор тестов, склонируйте репозиторий, а затем запустите `pytest`:

```bash
git clone https://github.com/[ваш_никнейм]/asadalpay.git
cd asadalpay
pytest
```

Убедитесь, что вы установили все зависимости для разработки:

```bash
pip install -r requirements.txt
```

