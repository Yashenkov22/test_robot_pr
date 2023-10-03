from robots.models import Robot
from customers.models import Customer


def construct_data_for_order(data: dict):
    customer, _ = Customer.objects.get_or_create(email=data['email'])

    dict_for_order = dict(customer=customer,
                          robot_serial=data['robot_serial'])

    if Robot.objects.filter(serial=data['robot_serial']).count() == 0:
        dict_for_order['is_wait'] = True
        response_text = 'К сожалению, выбранного робота нет в наличии.\
                         Мы сообщим Вам на почту, когда он появится.'
    else:
        response_text = 'Заказ оформлен'

    return (
        dict_for_order,
        response_text
    )