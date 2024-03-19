import requests


def create_order(product_id, pay_id):
    # URL API для инициализации заказа
    api_url = 'https://api.softpaymoney.com/api/v1/order'
    from config import api_key
    custom_data = {
        "pay_id": pay_id,
    }

    # Заголовки запроса, возможно, включая аутентификационный токен
    headers = {
        "Authorization": f"{api_key}"  # Замените YOUR_API_KEY на ваш действительный API ключ
    }

    # Данные заказа
    order_data = {
        "product": product_id,
        "customData": custom_data
    }

    # Отправляем POST-запрос для создания заказа
    response = requests.post(api_url, headers=headers, json=order_data)
    # Проверяем ответ от API
    data = response.json().get('data')
    order = data.get("order")
    status = order.get('status')

    url = data.get("url")

    if response.status_code == 201:
        if status == 'CREATED':
            return url
        else:
            return False
    return False