from django.shortcuts import render , get_object_or_404 
from .models import Contato
from django.core.paginator import Paginator
from django.http import Http404

def index(request):
    contatos = Contato.objects.order_by('-id').filter(
        mostrar = True
    )
    paginator = Paginator(contatos, 3)
    
    page = request.GET.get('p')
    contatos = paginator.get_page(page)
    return render(request, 'contatos/index.html', {
        'contatos' : contatos ,
        'page' : page
    })

def ver_contato(request , contato_id):
    
    '''Utilizei o atalho 'get_object_or_404' para levantar o erro de páginas não encontradas.
    O atalho substítiu essa linha de código >>> "contato = Contato.objects.get(id=contato_id)" '''
    
    contato = get_object_or_404(Contato, id=contato_id  )
    
    if not contato.mostrar:
        raise Http404()
    
    
    return render(request, 'contatos/ver_contato.html', {
        'contato' : contato
    })



