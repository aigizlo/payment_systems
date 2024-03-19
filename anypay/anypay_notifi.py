from flask import Flask, request, jsonify, abort
import hashlib


@app.route('/notification_corbots', methods=['POST'])
def payment_notification():
    # Получаем параметры из POST-запроса
    data = request.form.to_dict()

    # Формируем строку для подписи
    signature_data = ':'.join([
        data['currency'],
        data['amount'],
        data['pay_id'],
        data['merchant_id'],
        data['status'],
        # data['test'],

    ])

    # Вычисляем SHA256 подпись
    calculated_signature = hashlib.sha256(signature_data.encode()).hexdigest()


    # Проверяем подпись
    if calculated_signature != data['sign']:
        logger.info("Ошибка в подписи")
        return 'Wrong Sign!', 400
    currency = data['currency']
    amount = data['amount']
    pay_id = data['pay_id']
    merchant_id = data['merchant_id']
    status = data['status']
    test = data['test']

    if status == 'paid':
        return 'OK', 200