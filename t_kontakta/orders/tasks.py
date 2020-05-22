"""from celery import task
from django.core.mail import send_mail as django_send_mail
from .models import Order


@task
def order_created(order_id):
    order = Order.objects.get(id=order_id)
    subject = f'Номер заказа {order_id}'
    message = 'Dear {},\n\nYou have successfully placed an order.\
                Your order id is {}.'.format(order.first_name,
                                             order.id)
    mail_sent = django_send_mail(subject,
                          message,
                          'admin@myshop.com',
                          [order.email])
    return mail_sent"""


from django.core.mail import send_mail
from .models import Order

def my_send_mail(order_id):
    order = Order.objects.get(id=order_id)
    subject = f'Номер заказа {order_id}'
    message = f'Уважаемый {order.first_name}! Номер вашего заказа {order.id}. В ближайшее время с Вами свяжется наш сотрудник'
    mail_sent = send_mail(subject,
              message,
              'from@example.com',
              [order.email],
              fail_silently=False,)
    return mail_sent