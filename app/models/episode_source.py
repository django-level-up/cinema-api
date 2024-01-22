from tortoise import fields, models


class EpisodeSource(models.Model):


    episode = fields.ForeignKeyField(
        "models.Episode",
        on_delete=fields.CASCADE,
        related_name="episode_sources",
    )

    source = fields.ForeignKeyField(
        "models.Source",
        on_delete=fields.CASCADE,
        related_name="episode_sources",
    )

    download_link = fields.TextField(
        null=True,
        blank=True,
    )

    kinopoisk_link = fields.TextField(
        null=True,
        blank=True,
    )

    imdb_link = fields.TextField(
        null=True,
        blank=True,
    )

    valid_source = fields.BooleanField(default=True)

    def __str__(self) -> str:
        return f"Got {self.episode.title} on {self.source.title}"

    class Meta:
        table = "content_episodesource"
