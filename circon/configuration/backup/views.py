from django.views.generic import TemplateView


class Backup(TemplateView):
    template_name = 'configuration/backup/backup.html'
