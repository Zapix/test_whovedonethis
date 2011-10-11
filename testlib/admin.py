from django.contrib import admin

from whovedonethis import admin as who_admin

from testlib import models 

class TestCreatedModelAdmin(who_admin.CreatedByAdminModel):
    list_display = ('value', 'created_by')

class TestUpdatedModelAdmin(who_admin.UpdatedByAdminModel):
    list_display = ('value', 'updated_by')

class TestCreatedUpdatedModelAdmin(who_admin.CreatedUpdatedByAdminModel):
    list_display = ('value', 'updated_by', 'created_by')

class TestAnotherCreatedModelAdmin(admin.ModelAdmin):
    list_display = ('value', 'author')
    exclude = ('author',)

class TestAnotherUpdatedModelAdmin(admin.ModelAdmin):
    list_display = ('value', 'updater')
    exclude = ('updater',)

class TestAnotherCreatedUpdatedModelAdmin(admin.ModelAdmin):
    list_display = ('value', 'corrector', 'author')
    exclude = ('corrector', 'author')


admin.site.register(models.TestCreated, TestCreatedModelAdmin)
admin.site.register(models.TestUpdated, TestUpdatedModelAdmin)
admin.site.register(models.TestCreatedUpdated,
    TestCreatedUpdatedModelAdmin
)
admin.site.register(models.TestAnotherCreated, TestAnotherCreatedModelAdmin)
admin.site.register(models.TestAnotherUpdated, TestAnotherUpdatedModelAdmin)
admin.site.register(models.TestAnotherCreatedUpdated,
    TestAnotherCreatedUpdatedModelAdmin
)



