from tortoise import fields, models

class Source(models.Model):
    id = fields.UUIDField(pk=True)
    title = fields.CharField(max_length=255)
    slug = fields.CharField(max_length=255)

    class Meta:
        table = "content_source"
