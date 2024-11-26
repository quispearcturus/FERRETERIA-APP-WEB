from django.core.management.base import BaseCommand
from django.apps import apps

class Command(BaseCommand):
    help = 'List all installed apps'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS(f'Installed Apps'))
        for app_config in apps.get_app_configs():
            
            if app_config.name.startswith('apps.'):
                self.stdout.write(self.style.SQL_COLTYPE(f'├ {app_config.name}'))
                modelos = app_config.get_models()
                for modelo in modelos:
                    self.stdout.write(self.style.SQL_COLTYPE(f'  ├ {modelo.__name__}'))

