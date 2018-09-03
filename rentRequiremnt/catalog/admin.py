from django.contrib import admin

# Register your models here.

from catalog.models import Memory, RAM, Processor, Category,Product,ProductInstance,Brand

admin.site.register(Memory)
admin.site.register(RAM)
admin.site.register(Processor)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(ProductInstance)
admin.site.register(Brand)