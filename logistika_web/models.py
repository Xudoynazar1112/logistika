from django.contrib.auth.models import User
from django.db import models


class Order(models.Model):
    DELIVER_TYPE = (
        ('морской', 'Морской'),
        ('воздушный', 'Воздушный'),
        ('наземный', 'Наземный'),
        ('экспресс', 'Экспресс'),
        ('группирование', 'Группирование'),
        ('насыпной груз', 'Насыпной груз'),
    )

    user = models.CharField(max_length=50)
    send_from = models.TextField()
    send_to = models.TextField()
    receive_address = models.TextField()
    receive_data = models.DateTimeField()
    deliver_address = models.TextField()
    about_product = models.TextField()
    product_id = models.CharField(max_length=100)
    marking = models.CharField(max_length=100)
    origin_country = models.TextField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    packaging_type = models.CharField(max_length=100)
    size = models.CharField(max_length=100)
    volume = models.CharField(max_length=100)
    seats = models.IntegerField(default=0)
    weight = models.IntegerField(default=0)
    deliver_path = models.CharField(max_length=100, choices=DELIVER_TYPE, default='морской')
    instruction_paperwork = models.TextField()
    product_insurance = models.TextField()
    other_instructions = models.TextField()
    temp_save = models.TextField()
    special_notes = models.TextField()
    tg_nickname = models.CharField(max_length=100, null=True, blank=True)
    phone_number = models.IntegerField(default=941234567)
