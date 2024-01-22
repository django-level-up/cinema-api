from tortoise import fields, models


class Season(models.Model):
    title = fields.CharField(max_length=255)
    description = fields.TextField()
    show = fields.ForeignKeyField(
        "models.Show",
        related_name="seasons",
        on_delete=fields.CASCADE,
        db_column="show_id",
    )

    duration = fields.CharField(
        max_length=255,
        null=True,
        blank=True,
    )

    class Meta:
        table = "content_season"
