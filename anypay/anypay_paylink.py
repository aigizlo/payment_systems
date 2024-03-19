import urllib.parse
import hashlib


def generate_any_pay_link(pay_id, desc, amount, secret_key):
    project_id = '13544'
    currency = 'RUB'
    success_url = ''
    fail_url = ''
    try:
        params = {
            'merchant_id': project_id,
            'pay_id': pay_id,
            'amount': amount,
            'currency': currency,
            'desc': desc,
            'success_url': success_url,
            'fail_url': fail_url
        }

        arr_sign = [project_id, pay_id, amount, currency, desc, success_url, fail_url, secret_key]

        # подпись
        sign = hashlib.sha256(":".join(arr_sign).encode()).hexdigest()

        # params['sign'] = sign
        encoded_params = urllib.parse.urlencode(params)

        # подпись к параметрам
        encoded_params += f'&sign={sign}'

        # итоговая ссылка
        payment_url = f"https://anypay.io/merchant?{encoded_params}"

        return payment_url

    except Exception as e:
        logger.error(f'ERROR - GENERATE_PAY_LIN Ошибка при генерации ссылки - {pay_id} - {e}')
        return False
