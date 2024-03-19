from flask import Flask, request, jsonify, abort
import hashlib


@app.route('/free_kassa_corbots', methods=['POST'])
def notify_payment_fk():
    MERCHANT_SECRET = """"""
    TRUSTED_IPS = ['168.119.157.136', '168.119.60.227', '138.201.88.124', '178.154.197.79']

    def is_request_from_trusted_ip():
        client_ip = request.remote_addr
        if request.headers.get('X-Real-IP'):
            client_ip = request.headers.get('X-Real-IP')
        return client_ip in TRUSTED_IPS

    def calculate_sign(merchant_id, amount, merchant_secret, merchant_order_id):
        sign_str = f"{merchant_id}:{amount}:{merchant_secret}:{merchant_order_id}"
        return hashlib.md5(sign_str.encode('utf-8')).hexdigest()

    if not is_request_from_trusted_ip():
        abort(403, description="hacking attempt!")
    data = request.form

    merchant_id = data['MERCHANT_ID']
    amount = data['AMOUNT']  # Сумма платежа в формате 100.00
    pay_id = data['MERCHANT_ORDER_ID']  # ID платежа в вашей системе
    sign = data['SIGN']
    check_sign = calculate_sign(merchant_id, amount, MERCHANT_SECRET, pay_id)

    if check_sign != sign:
        abort(400, description="wrong sign")

    return 'YES', 200
