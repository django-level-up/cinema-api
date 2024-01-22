from tortoise import Tortoise

TORTOISE_ORM = {
    "connections": {
        "default": "postgres://db_user:db_password@127.0.0.1:5400/db_dev",
    },
    "apps": {
        "models": {
            "models": ["app.models.user", "app.models.movie", "app.models.source", "app.models.movie_source"],

            "default_connection": "default",
        }
    }
}

Tortoise.init(config=TORTOISE_ORM)
