from django.db import models
from django.contrib.auth.models import User

from whovedonethis import models as who_models

class TestCreated(who_models.CreatedByMixin):
    value = models.CharField('Value', max_length=255)

class TestUpdated(who_models.UpdatedByMixin):
    value = models.CharField('Value', max_length=255)

class TestCreatedUpdated(who_models.CreatedUpdatedByMixin):
    value = models.CharField('Value', max_length=255)
    
class TestAnotherCreated(models.Model):
    value = models.CharField('Value', max_length=255)
    author = models.ForeignKey(User, verbose_name='Author')
    
    created_by_field = 'author'
    
class TestAnotherUpdated(models.Model):
    value = models.CharField('Value', max_length=255)
    updater = models.ForeignKey(User, verbose_name='Updater')
    
    updated_by_field = 'updater'

class TestAnotherCreatedUpdated(models.Model):
    value = models.CharField('Value', max_length=255)
    author = models.ForeignKey(User, verbose_name='Author',
        related_name='%(class)s_author'
    )
    corrector = models.ForeignKey(User, verbose_name='Corrector',
        related_name='%(class)s_corrector'
    )
    
    created_by_field = 'author'
    updated_by_field = 'corrector'

from testlib import signals
