from django.core.management.base import BaseCommand
from bugs.models import User

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@mail.ru', 'Admin1234!', role='admin')
            self.stdout.write('admin created')
        if not User.objects.filter(username='tester').exists():
            User.objects.create_user('tester', 'tester@mail.ru', 'Tester1234!', role='tester')
            self.stdout.write('tester created')
        if not User.objects.filter(username='developer').exists():
            User.objects.create_user('developer', 'dev@mail.ru', 'Developer1234!', role='developer')
            self.stdout.write('developer created')