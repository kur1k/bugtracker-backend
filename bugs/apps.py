from django.apps import AppConfig

class BugsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bugs'

    def ready(self):
        try:
            from bugs.models import User
            if not User.objects.filter(username='admin').exists():
                User.objects.create_superuser('admin', 'admin@mail.ru', 'Admin1234!', role='admin')
            if not User.objects.filter(username='tester').exists():
                User.objects.create_user('tester', 'tester@mail.ru', 'Tester1234!', role='tester')
            if not User.objects.filter(username='developer').exists():
                User.objects.create_user('developer', 'dev@mail.ru', 'Developer1234!', role='developer')
        except Exception:
            pass