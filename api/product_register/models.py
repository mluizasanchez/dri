import logging

from django.db import models
from django.conf import settings
from current_user import get_current_user

class Export(models.Model):
 
    exp_username = models.CharField(max_length=128)
    exp_date = models.DateTimeField()
    exp_external_process = models.PositiveIntegerField()

class Site(models.Model):

    sti = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE, default=get_current_user, verbose_name='User Name')

    sti_name = models.CharField(max_length=128, verbose_name='Site')
    sti_url = models.URLField(verbose_name='Url', null=True, blank=True)

class ExternalProcess(models.Model):
    epr_name = models.CharField(max_length=128, verbose_name='Internal Name')
    epr_username = models.CharField(max_length=128, verbose_name='User Name')
    epr_site = models.ForeignKey(
        Site, on_delete=models.CASCADE, verbose_name='Site',
        help_text='origin of the process. instance from which it was imported.', default=None)
    epr_original_id = models.PositiveIntegerField(verbose_name='Original Id',
        help_text='original process id on your instances of origin.')
    epr_start_date = models.DateTimeField(verbose_name='Start Date')
    epr_end_date = models.DateTimeField(verbose_name='End Date')
    epr_readme = models.CharField(max_length=128, verbose_name='Readme')
    epr_comment = models.CharField(max_length=128, verbose_name='Comment', help_text='Process submission comment.')


    def __str__(self):
        return str(self.epr_original_id)
