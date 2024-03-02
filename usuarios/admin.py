from django.contrib import admin

from usuarios.models import Usuario, Beneficiario, Acudiente, Padrino, Referencia

# Register your models here.
admin.site.register(Usuario)
admin.site.register(Beneficiario)
admin.site.register(Acudiente)
admin.site.register(Padrino)
admin.site.register(Referencia)