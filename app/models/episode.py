from tortoise import fields, models


class Episode(models.Model):
    id = fields.UUIDField(pk=True)
    title = fields.CharField(max_length=255)
    description = fields.TextField()
    season = fields.ForeignKeyField(
        "models.Season",
        related_name="episodes",
        on_delete=fields.CASCADE,
        db_column="season_id",
    )

    duration = fields.CharField(
        max_length=255,
        null=True,
        blank=True,
    )

    class Meta:
        table = "content_episode"
