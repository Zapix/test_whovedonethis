from django.db.models.signals import pre_save
from django.dispatch import receiver

from whovedonethis import decorator

#from testlib.models import (
    #TestCreated, TestUpdated, TestCreatedUpdated, TestAnotherCreated,
    #TestAnotherUpdated, TestAnotherCreatedUpdated)
from testlib.models import TestCreated, TestUpdated, TestCreatedUpdated,\
    TestAnotherCreated, TestAnotherUpdated, TestAnotherCreatedUpdated

@receiver(pre_save, sender=TestCreated)
@decorator.add_created_user
def pre_save_testcreated_handler(sender, instance, **kwargs):
    pass

@receiver(pre_save, sender=TestUpdated)
@decorator.add_updated_user
def pre_save_testupdated_handler(sender, instance, **kwargs):
    pass

@receiver(pre_save, sender=TestCreatedUpdated)
@decorator.add_created_and_updated_user
def pre_save_testcreatedupdated_handler(sender, instance, **kwargs):
    pass

@receiver(pre_save, sender=TestAnotherCreated)
@decorator.add_created_user
def pre_save_testanothercreated_handler(sender, instance, **kwargs):
    pass

@receiver(pre_save, sender=TestAnotherUpdated)
@decorator.add_updated_user
def pre_save_testanotherupdated_handler(sender, instance, **kwargs):
    pass
    
@receiver(pre_save, sender=TestAnotherCreatedUpdated)
@decorator.add_created_and_updated_user
def pre_save_testanothercreatedupdated_handler(sender, instance, **kwargs):
    pass

