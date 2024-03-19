from flask import Flask, request, jsonify, abort


@app.route('/soft_pay_corbots', methods=['POST'])
def notify_payment_soft_pay():
    from config import secret_key_webhook

    # Получаем данные и токен из запроса
    data = request.get_data(as_text=True)
    data_dict = json.loads(data)

    amount = data_dict['amount']
    paidAmount = data_dict['paidAmount']
    paidAt = data_dict['paidAt']
    payer = data_dict['payer']
    payerEmail = data_dict['payerEmail']
    payerPhone = data_dict['payerPhone']
    productLink = data_dict["productLink"]
    promocodeName = data_dict['promocodeName']
    promocodeType = data_dict['promocodeType']
    recurrent = data_dict['recurrent']

    secret = secret_key_webhook
    status = data_dict['status']
    types = data_dict['type']

    concatenated_string = (
            str(amount) +
            str(paidAmount) +
            str(paidAt) +
            str(payer) +
            str(payerEmail) +
            str(payerPhone) +
            str(productLink) +
            str(promocodeName) +
            str(promocodeType) +
            str(recurrent).lower() +
            str(secret) +
            str(status) +
            str(types)
    )

    pay_id = data_dict['data']['pay_id']

    token = data_dict['token']

    # Проверяем подлинность вебхука
    if not verify_webhook(concatenated_string, token):
        error_message = {'error': 'Invalid token'}
        return jsonify(error_message), 401

    try:

        if status != "CONFIRMED":
            return 401

    except Exception as e:
        logger.error(f"Ошибка платежа - {e}")

    # Возвращаем успешный ответ
    return 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
