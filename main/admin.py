from django.contrib import admin
from .models import UsersAb, Skins, CasesCategory, Cases, Orders

admin.site.register(Skins)
admin.site.register(UsersAb)
admin.site.register(CasesCategory)
admin.site.register(Cases)
admin.site.register(Orders)