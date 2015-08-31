
from principal.forms import *

#Metodos necesarios para los Procesos
def ver_logeo(request):
    try:
        nombre = request.user.usu_nombre

    except:
        print 'error proceso'

    return nombre

def listar_categorias():
    try:
        categorias = Categoria.objects.all().order_by('id')

    except:
        print 'error proceso'

    return categorias





########PROCESOS

#Proceso para formulario de login
def proceso1(request):
    context = {
        'formularioLogeo':ver_logeo(),
    }

    return context

#Proceso para listar categorias en el menu
