from django.contrib import admin

from inven.models import Attribute
from inven.models import ConsumerAttribute
from inven.models import Entity
from inven.models import ProviderAttribute
from inven.models import ProviderDataset


@admin.register(ProviderDataset)
class ProviderDatasetAdmin(admin.ModelAdmin):
    pass


@admin.register(ProviderAttribute)
class ProviderAttributeAdmin(admin.ModelAdmin):
    pass


@admin.register(ConsumerAttribute)
class ConsumerAttributeAdmin(admin.ModelAdmin):
    pass


@admin.register(Attribute)
class AttributeAdmin(admin.ModelAdmin):
    pass


@admin.register(Entity)
class EntityAdmin(admin.ModelAdmin):
    pass
