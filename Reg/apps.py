from django.apps import AppConfig


class RegConfig(AppConfig):
    name = 'Reg'

    # we are not writing the code of signals.py here,
    # because there will be some side affects.
    def ready(self):
        import Reg.signals