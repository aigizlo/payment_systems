import hashlib
def generate_free_kassa(order_id, order_amount):
    merchant_id =
    secret_word =
    currency = 'RUB'
    sign = hashlib.md5(f"{merchant_id}:{order_amount}:{secret_word}:{currency}:{order_id}".encode('utf-8')).hexdigest()

    base_url = 'https://pay.freekassa.ru/'
    params = {
        'm': merchant_id,
        'oa': order_amount,
        'o': order_id,
        's': sign,
        'currency': currency,
        'lang': 'ru',
    }

    query_string = '&'.join([f"{key}={value}" for key, value in params.items()])
    payment_url = f"{base_url}?{query_string}"

    return payment_url