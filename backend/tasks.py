from backend.models import wallet
from mini_wallet.celery import shared_task

def update_wallet_balance(amount, trx_type , wallet_id):
    wallet = wallet.objects.get(id=wallet_id)
    if trx_type == 'deposit':
        wallet.balance = wallet.balance + int(amount)
    else:
        wallet.balance = wallet.balance - int(amount)
    wallet.save()