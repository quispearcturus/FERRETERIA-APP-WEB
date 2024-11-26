from django.core.management.base import BaseCommand
from django.core.management import call_command

import os
from django.conf import settings
from django.apps import apps

class Command(BaseCommand):
    help = 'Crea migraciones para la aplicación poll'
    project_name = os.path.basename(settings.BASE_DIR)

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS(f"Running makemigrations for { self.project_name.capitalize() } project applications"))
        for app_config in apps.get_app_configs():
            if app_config.name.startswith('apps.'):
                name_app = (app_config.name).split('.')[-1]
                self.stdout.write(self.style.SQL_COLTYPE(f'├ { name_app }'))
                call_command('makemigrations', name_app)
        self.stdout.write(self.style.SUCCESS("Performing migrate complete"))
        call_command('migrate')
