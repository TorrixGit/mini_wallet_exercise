from django.db import models
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

# Create your models here.
class Account(models.Model):
    customer_xid = models.CharField(max_length=50, unique=True)
    User = models.OneToOneField(User, on_delete=models.DO_NOTHING)

class wallet(models.Model):
    customer = models.OneToOneField(Account, on_delete=models.DO_NOTHING)
    balance = models.DecimalField(max_digits=20,decimal_places=3,default=0)
    status = models.BooleanField(default=False)

class transaction(models.Model):
    TRANSACTION_CHOICES = (('Deposit', 'deposit'),('Withdraw', 'withdraw'))
    transaction_type = models.CharField(max_length=50, choices=TRANSACTION_CHOICES)
    transaction_by = models.ForeignKey(Account, on_delete=models.DO_NOTHING)
    amount = models.DecimalField(max_digits=20, decimal_places=3)
    reference_id = models.CharField(max_length=250)