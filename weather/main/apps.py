from django.apps import AppConfig


class MainConfig(AppConfig):
    # This setting specifies the default type for auto-created primary key fields.
    # 'BigAutoField' is a 64-bit integer, which is suitable for large tables.
    default_auto_field = 'django.db.models.BigAutoField'
    # This is the name of the application.
    # It must be unique across all installed applications.
    name = 'main'