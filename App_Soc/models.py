from django.db import models
from datetime import datetime, timedelta
from django.utils import timezone

# Create your models here.
class User(models.Model):
    timestamp = models.DateTimeField(auto_now=True)
    ic_no = models.CharField(primary_key=True, max_length=12, verbose_name='IC No.')
    name = models.CharField(max_length=100, verbose_name='Name', blank=False)
    phone_no = models.CharField(max_length=100, verbose_name='Phone Number', blank=False)

    def was_published_recently(self):
        return self.timestamp >= timezone.now() - datetime.timedelta(days=1)

    def calculate_age(self):
        birthday = self.ic_no[:6]
        date_time_obj = datetime.strptime(birthday, '%y%m%d')
        if date_time_obj > datetime.now():
            date_time_obj -= timedelta(weeks=5124, days=2)
        age = datetime.now() - date_time_obj
        ageYears = int(age.days / 365)
        return ageYears
