from tortoise import fields
from tortoise.models import Model


class Rate(Model):
    id = fields.IntField(pk=True)
    date = fields.DateField()
    cargo_type = fields.TextField()
    rate = fields.FloatField()

    def __str__(self):
        return f'{self.date} -> {self.rate}'
