import errno
import io
import shutil
import os
from importlib import import_module
from os import path

import django
from django.conf import settings
from django.template import Context, Engine
from django.core.management.base import CommandError
from django.core.management.utils import handle_extensions
from django.core.management.templates import TemplateCommand

import apps.templifys as general


class Command(TemplateCommand):
    help = (
        "Create a Frontend Module directory structure for the given app name in "
        "the current directory or optionally in the given directory."
    )
    missing_args_message = "You must provide an application name."
    rewrite_template_suffixes = (
        ('.dj-py', '.py'),
    )

    def add_arguments(self, parser):
        super(Command, self).add_arguments(parser)
        parser.set_defaults(extensions=['py', 'html'])

    def handle_template(self, template, subdir):
        """
        Determine where the app or project templates are.
        Use django.__path__[0] as the default because we don't
        know into which directory Django has been installed.
        """
        if template is None:
            return path.join(general.__path__[0], 'conf', subdir)
        return super(Command, self).handle_template(template, subdir)

    def _expand_target_dir(self, app_name, target):
        if target is None:
            top_dir = path.join(os.getcwd(), 'apps', app_name)
            try:
                os.makedirs(top_dir)
            except OSError as e:
                if e.errno == errno.EEXIST:
                    # message = "'%s' already exists app" % top_dir
                    message = f'already exists { app_name } app created in Project'
                else:
                    message = e
                raise CommandError(message)
        else:
            top_dir = os.path.abspath(path.expanduser(target))
            if not os.path.exists(top_dir):
                raise CommandError("Destination directory '%s' does not "
                                   "exist, please create it first." % top_dir)
        return top_dir
    
    def _expand_models_dir(self, app_name, model_name):
        path_model = path.join(os.getcwd(), 'apps', app_name, 'models', model_name)
        if os.path.exists(path_model):
            message = f'already exists { model_name } model created in { app_name} App'
            raise CommandError(message)
        else:
            path_model_create = path.join(os.getcwd(), 'apps', app_name, 'models')
            if os.path.exists(path_model_create):
                return path_model_create
            else:
                message = f'Destination directory {path_model_create} does not exist'
                raise CommandError(message)

    def handle(self, **options):
        self.verbosity = options['verbosity']
        
        # app_name, target = options.pop('name'), options.pop('directory')
        app_name, model = options.pop('name'), options.pop('directory')
        extensions = tuple(handle_extensions(options['extensions']))
        extra_files = []
        for file in options['files']:
            extra_files.extend(map(lambda x: x.strip(), file.split(',')))

    #     self._validate_name(app_name)

        self.paths_to_remove = []
        # top_dir = self._expand_target_dir(app_name, model)
        top_dir = self._expand_models_dir(app_name, model)

        camel_case_model_name = ''.join(x for x in model.title() if x != '_')
        print(top_dir)
        context = Context(dict(options, **{
            'app_name': app_name,
            'camel_case_model_name': camel_case_model_name,
            'base_directory': top_dir,
            'author': '# ZeroPaul'
        }), autoescape=False)

        # Setup a stub settings environment for template rendering
        if not settings.configured:
            settings.configure()
            django.setup()

        template_dir = self.handle_template(options['template'], 'model_template')
        if not path.exists(top_dir + '\\'+ model + '.py'):
        
            with open(template_dir + '\model.dj-py', 'r') as template_file:
                content = template_file.read()

            with open(top_dir + '\\'+ model + '.py', 'w') as new_file:
                
                template = Engine().from_string(content)
                rendered_content = template.render(context)
                new_file.write(rendered_content)

            self.stdout.write(self.style.SUCCESS(f'{ model } model has been created in the { app_name} App'))
        else:
            self.stdout.write(self.style.ERROR(f'already exists { model } model created in { app_name} App'))