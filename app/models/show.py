from tortoise import fields, models


class Show(models.Model):
    id = fields.UUIDField(pk=True)
    title = fields.CharField(max_length=255)
    description = fields.TextField(
        null=True,
        blank=True,
    )
    image = fields.TextField(
        blank=True,
        null=True,
    )

    imdb_rating = fields.FloatField(
        null=True,
        blank=True,
    )
    tmdb_rating = fields.FloatField(
        null=True,
        blank=True,
    )
    kinopoisk_rating = fields.FloatField(
        null=True,
        blank=True,
    )
    bg_image = fields.TextField(
        blank=True,
        null=True,
    )
    release_date = fields.DateField(
        null=True,
        blank=True,
    )

    duration = fields.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    keywords = fields.TextField(null=True, blank=True)

    class Meta:
        table = "content_show"
