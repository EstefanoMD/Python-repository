from django.contrib import admin
from .models import Categoria, Contato

class ContatoAdmin(admin.ModelAdmin):
    list_display = ('id','nome', 'sobrenome' , 'telefone' , 'email' , 'mostrar')
    list_display_links= ('nome' , 'id')
    search_fields = ('nome' , 'sobrenome')
    list_per_page = 5
    list_editable = ('mostrar', 'telefone')

admin.site.register(Contato , ContatoAdmin)
admin.site.register(Categoria)
