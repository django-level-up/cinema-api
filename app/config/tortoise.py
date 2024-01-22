TORTOISE_ORM = {
    "connections": {
        "default": "postgres://db_user:db_password@localhost:5400/db_dev",
    },
    "apps": {
        "models": {
            "models": [
                "models",
                # "app.models",
            ],
            "default_connection": "default",
        }
    },
}
