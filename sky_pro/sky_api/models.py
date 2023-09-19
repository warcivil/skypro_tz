from django.db import models
from datetime import timedelta

from django.utils import timezone


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255,
                            verbose_name='Название товара')
    category = models.CharField(max_length=255,
                                verbose_name='Категория')
    is_active = models.BooleanField(default=True,
                                    verbose_name='Статус активности')
    price = models.DecimalField(max_digits=10,
                                decimal_places=2, verbose_name='Цена')

    class Meta:
        verbose_name_plural = 'Товары'

    def orders_last_month(self):
        today = timezone.now()
        last_month_start = today.replace(month=today.month-1,
                                         day=1,
                                         hour=0,
                                         second=0,
                                         minute=0)
        last_month_end = today.replace(day=1,
                                       hour=23,
                                       minute=59,
                                       second=59) - timedelta(days=1)
        return self.orders.filter(
            order_date__range=[last_month_start, last_month_end]).count()

    def orders_current_month(self):
        today = timezone.now()
        current_month_start = today.replace(day=1, hour=0, minute=0, second=0)
        return self.orders.filter(order_date__gte=current_month_start).count()


class Order(models.Model):
    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE,
                                verbose_name='Товар',
                                related_name='orders')
    order_date = models.DateTimeField(auto_now_add=True,
                                      verbose_name='Дата заказа')

    class Meta:
        verbose_name_plural = 'Заказы'
