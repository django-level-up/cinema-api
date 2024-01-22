from tortoise import fields, models

class MovieSource(models.Model):
    id = fields.UUIDField(pk=True)
    movie = fields.ForeignKeyField("models.Movie")
    source = fields.ForeignKeyField("models.Source")
    download_link = fields.TextField(null=True, blank=True)
    kinopoisk_link = fields.TextField(null=True, blank=True)
    imdb_link = fields.TextField(null=True, blank=True)
    tmdb_link = fields.TextField(null=True, blank=True)
    watch_link = fields.TextField(null=True, blank=True)
    valid_source = fields.BooleanField(default=False)

    class Meta:
        table = "content_moviesource"
