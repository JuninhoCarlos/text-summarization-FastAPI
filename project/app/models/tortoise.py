from tortoise import fields, models


class TextSummary(models.Model):
    url = fields.TextField()
    sumary = fields.TextField()
    created_at = fields.DatetimeField(auto_now=True)

    def __str__(self):
        return self.url
