# app/models/user.py
from tortoise import fields, models

class User(models.Model):
    id = fields.UUIDField(pk=True)
    email = fields.CharField(max_length=50)

    class Meta:
        table = "account_user"
