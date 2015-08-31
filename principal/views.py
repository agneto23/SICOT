# -*- coding: utf-8 -*-
from io import BytesIO
from django.core import serializers
from django.http import HttpResponse
from django.views.generic import ListView
from reportlab.platypus import SimpleDocTemplate, Paragraph, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import Table

from .models import Producto

from django.shortcuts import render

# Create your views here.

#from principal.models import Receta, Bebida
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.contrib.auth.models import User
from django import forms
from django.template import RequestContext
from django.http import HttpResponse
from django.template import loader, context
from django.views.generic import UpdateView,CreateView,DeleteView,DetailView
from django.views.generic import FormView, ListView
from pywin.mfc.docview import EditView
from principal.models import Categoria
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

from .forms import *
from .models import *



def index_view(request):
    return render_to_response('inicio.html',context=RequestContext(request))


def login_view(request):
    return  render_to_response('login.html',context=RequestContext(request))




#Principal

@login_required(login_url='/')
def orden(request):
    return render_to_response('orden.html',context=RequestContext(request))

@login_required(login_url='/')
def v_inventario(request):
    return render_to_response('inventario.html',context=RequestContext(request))

@login_required(login_url='/')
def reporte(request):
    return render_to_response('reporte.html',context=RequestContext(request))

@login_required(login_url='/')
def usuario(request):
    return render_to_response('usuario.html',context=RequestContext(request))

#Gestionar

@login_required(login_url='/')
def gestionarproducto(request):
    return render_to_response('gestionarproducto.html',context=RequestContext(request))

@login_required(login_url='/')
def gestionarproveedor(request):
    return render_to_response('gestionarproveedor.html',context=RequestContext(request))

@login_required(login_url='/')
def gestionarcategoria(request):
    return render_to_response('gestionarcategoria.html',context=RequestContext(request))

@login_required(login_url='/')
def gestionarorden(request):
    return render_to_response('gestionarorden.html',context=RequestContext(request))

@login_required(login_url='/')
def gestionarcliente(request):
    return render_to_response('gestionarcliente.html',context=RequestContext(request))



#GESTIONARUSUARIO


@login_required(login_url='/')
def ingresarusuario(request):
    if request.method=='POST':
        usu=Usuario(usu_cedula=request.POST["txtCedula"],
                    usu_nombre=request.POST["txtNombre"],
                    usu_apellido=request.POST["txtApellido"],
                    usu_contrasena=request.POST["txtContra"],




                    )
        usu.save()

        return redirect('ingresarusuario')

    return render_to_response('ingresarusuario.html',"",context_instance=RequestContext(request))

@login_required(login_url='/')
class modificarusuario(UpdateView):
    model = Usuario
    fields = ('usu_cedula','usu_nombre','usu_apellido','usu_contrasena','usu_estado')
    template_name = 'modificarusuario.html'
    success_url = '/usuario/buscarusuario/'

@login_required(login_url='/')
def buscarusuario(request):
    if request.method=='POST':
        usu=Usuario.objects.filter(usu_cedula__contains=request.POST["txtBuscar"]).values()

        return render_to_response('buscarusuario.html',{'usu':usu},context_instance=RequestContext(request))

    usu=Usuario.object.filter(usu_estado = "a")
    return render_to_response('buscarusuario.html',{'usu':usu},context_instance=RequestContext(request))





def delUser_view(request,pk):
    obj = get_object_or_404(Usuario, pk=pk)
    obj.usu_est=False
    obj.save()
    return redirect("/usuario/Administrar/")

class newUser_view(FormView):
    form_class = UserForm
    template_name = 'ingresarusuario.html'
    success_url = '/usuario/Administrar/'

    def form_valid(self,form):
        form.save()
        return super(newUser_view,self).form_valid(form)

class editUser_view(UpdateView):
    model = Usuario
    fields = ('usu_cedula','usu_nombre','usu_apellido','usu_correo','usu_estado','password')
    template_name = 'modificarusuario.html'
    success_url = '/usuario/buscarusuario/'


class modificarperfil_view(UpdateView):
    model = Usuario
    fields = ('usu_cedula','usu_nombre','usu_apellido','usu_correo','usu_estado','password')
    template_name = 'modificarperfil.html'
    success_url = '/usuario/buscarusuario/'

@login_required(login_url='/')
def perfilusuario(request,id):
     usu=Usuario.object.get(pk=id)
     return render_to_response('perfilusuario.html',{'usu':usu},context_instance=RequestContext(request))








#GESTIONARPRODUCTO



@login_required(login_url='/')
def ingresarproducto(request):
    cat = Categoria.objects.all()
    prov = Proveedor.objects.all()
    data = {}
    data["categorias"]=cat
    data["proveedores"]=prov

    if request.method=='POST':

        prov = Proveedor.objects.get(pk=request.POST["cmbProv"])
        cat = Categoria.objects.get(pk=request.POST["cmbCat"])

        pro=Producto(prov_cedula=prov,
                     cat_id=cat,
                     pro_nombre=request.POST["txtNombre"],
                     pro_modelo=request.POST["txtModelo"],
                     pro_marca=request.POST["txtMarca"],
                     pro_stocka=request.POST["txtStockA"],
                     pro_stockm=request.POST["txtStockM"],
                     pro_precio=request.POST["txtPrecioP"],
                     pro_preciov=request.POST["txtPrecio"],

                     )
        pro.save()

        return redirect('ingresarproducto')

    return render(request,"ingresarproducto.html",data)


@login_required(login_url='/')
def modificarproducto(request,id):
    if request.method=='POST':

        prov = Proveedor.objects.get(pk=request.POST["cmbProv"])
        cat = Categoria.objects.get(pk=request.POST["cmbCat"])
        pro=Producto(prov_cedula=prov,
                     cat_id=cat,
                     pro_id=id,
                     pro_nombre=request.POST["txtNombre"],
                     pro_modelo=request.POST["txtModelo"],
                     pro_marca=request.POST["txtMarca"],
                     pro_stocka=request.POST["txtStockA"],
                     pro_stockm=request.POST["txtStockM"],
                     pro_precio=request.POST["txtPrecioP"],
                     pro_preciov=request.POST["txtPrecio"],

                     )
        pro.save()

        return redirect(buscarproducto)


    pro=Producto.objects.get(pk=id)
    cat=Categoria.objects.get(pk=pro.cat_id_id)
    prov=Proveedor.objects.get(pk=pro.prov_cedula_id)

    cate = Categoria.objects.all()
    prove = Proveedor.objects.all()

    return render_to_response('modificarproducto.html',{'pro':pro,'cat':cat,'prov':prov,'cate':cate,'prove':prove},context_instance=RequestContext(request))


@login_required(login_url='/')
def buscarproducto(request):
    if request.method=='POST':
        pro=Producto.objects.filter(pro_nombre=request.POST["txtBuscar"]).values()


        return render_to_response('buscarproducto.html',{'pro':pro},context_instance=RequestContext(request))

    pro=Producto.objects.all()
    return render_to_response('buscarproducto.html',{'pro':pro},context_instance=RequestContext(request))

@login_required(login_url='/')
def ordenproducto(request):

    if request.method=='POST':
        pro=Producto.objects.filter(cli_nombre=request.POST["txtBuscar"]).values()


        return render_to_response('ordenproducto.html',{'pro':pro},context_instance=RequestContext(request))

    pro=Producto.objects.all()
    return render_to_response('ordenproducto.html',{'pro':pro},context_instance=RequestContext(request))


#GESTIONARCATEGORIA


def ingresarcategoria(request):

    if request.method=='POST':
        categoria=Categoria(cat_nombre=request.POST["txtNombre"],
                            cat_detalle=request.POST["txtDetalle"],

                            )
        categoria.save()

        return redirect('buscarcategoria')

    return render_to_response('ingresarcategoria.html',context_instance=RequestContext(request))

def ingresarcategoria1(request):

    if request.method=='POST':
        categoria=Categoria(cat_nombre=request.POST["txtNombre"],
                            cat_detalle=request.POST["txtDetalle"],

                            )
        categoria.save()

        return redirect('ingresarproducto')

    return render_to_response('ingresarcategoria1.html',context_instance=RequestContext(request))




@login_required(login_url='/')
def modificarcategoria(request,id):

    if request.method=='POST':

        if 'guardar' in request.POST:

            cate = Categoria(
                cat_id=id,
                cat_nombre=request.POST["cat_nombre"],
                cat_detalle=request.POST["cat_detalle"])
            cate.save()


    cate=Categoria.objects.get(pk=id)


    return render_to_response('modificarcategoria.html',{'cate':cate},context_instance=RequestContext(request))


@login_required(login_url='/')
def buscarcategoria(request):



    if request.method=='POST':
        categoria=Categoria.objects.filter(cat_nombre=request.POST["txtBuscar"]).values()


        return render_to_response('buscarcategoria.html',{'categoria':categoria},context_instance=RequestContext(request))

    categoria=Categoria.objects.all()
    return render_to_response('buscarcategoria.html',{'categoria':categoria},context_instance=RequestContext(request))



#GESTIONARPROVEEDOR

@login_required(login_url='/')
def ingresarproveedor(request):
    if request.method=='POST':
        prov=Proveedor(prov_cedula=request.POST["txtCedula"],
                       prov_repre=request.POST["txtRepre"],
                       prov_direccion=request.POST["txtDir"],
                       prov_ciudad=request.POST["txtCiu"],
                       prov_telefono=request.POST["txtTel"],
                       prov_nombre=request.POST["txtNombre"],
                       prov_correo=request.POST["txtCorreo"],

                       )
        prov.save()

        return redirect('ingresarproveedor')

    return render_to_response('ingresarproveedor1.html',"",context_instance=RequestContext(request))


def ingresarproveedor1(request):
    if request.method=='POST':
        prov=Proveedor(prov_cedula=request.POST["txtCedula"],
                       prov_repre=request.POST["txtRepre"],
                       prov_direccion=request.POST["txtDir"],
                       prov_ciudad=request.POST["txtCiu"],
                       prov_telefono=request.POST["txtTel"],
                       prov_nombre=request.POST["txtNombre"],
                       prov_correo=request.POST["txtCorreo"],

                       )
        prov.save()

        return redirect('ingresarproducto')

    return render_to_response('ingresarproveedor.html',"",context_instance=RequestContext(request))


@login_required(login_url='/')
def modificarproveedor(request,id):
    if request.method=='POST':


        prov=Proveedor(prov_cedula=id,
                       prov_repre=request.POST["txtRepre"],
                       prov_direccion=request.POST["txtDir"],
                       prov_ciudad=request.POST["txtCiu"],
                       prov_telefono=request.POST["txtTel"],
                       prov_nombre=request.POST["txtNombre"],
                       prov_correo=request.POST["txtCorreo"],

                       )
        prov.save()

        return redirect(buscarproveedor)


    prov=Proveedor.objects.get(pk=id)


    return render_to_response('modificarproveedor.html',{'prov':prov},context_instance=RequestContext(request))

@login_required(login_url='/')
def buscarproveedor(request):
    if request.method=='POST':
        prov=Proveedor.objects.filter(prov_nombre=request.POST["txtBuscar"]).values()


        return render_to_response('buscarproveedor.html',{'prov':prov},context_instance=RequestContext(request))

    prov=Proveedor.objects.all()
    return render_to_response('buscarproveedor.html',{'prov':prov},context_instance=RequestContext(request))



#GESTIONARORDEN



@login_required(login_url='/')
def ingresarorden(request):
    if request.method=='POST':

        cli = Cliente.objects.get(pk=request.POST["idcliente"])
        ord=OrdenTrabajo(cli_cedula=cli,
                         ord_numero=request.POST["Numero"],
                         ord_fechar=request.POST["fechaR"],
                         ord_fechae=request.POST["fechaE"],
                         ord_detalle=request.POST["txtDetalle"],
                         ord_servicio=request.POST["txtSer"],
                         ord_tipo=request.POST["cmbTipo"],
                         ord_estado="h",


                         )

        ord.save()

        return redirect('ingresarorden')

    ord=OrdenTrabajo.objects.count()
    return render_to_response('ingresarorden.html',{'ord':ord},context_instance=RequestContext(request))

@login_required(login_url='/')
def modificarorden(request,id):

    if request.method=='POST':

        if 'guardar' in request.POST:

            cli = Cliente.objects.get(pk=request.POST["idcliente"])
            ord=OrdenTrabajo(ord_id=id,
                         cli_cedula=cli,
                         ord_numero=request.POST["Numero"],
                         ord_fechae=request.POST["fechaE"],
                         ord_detalle=request.POST["txtDetalle"],
                         ord_servicio=request.POST["txtSer"],
                         ord_tipo=request.POST["cmbTipo"],
                         ord_estado=request.POST["cmbEst"],
                         ord_precio=request.POST["pretot"],
                         )

            ord.save()

            for i in range(1, int(request.POST["totalproductos"])+1):

                print(request.POST["totalproductos"])


                nombrepro = '%s%s' %("pronom",str(i))
                cantidad = '%s%s' %("",str(i))
                precio = '%s%s' %("pre",str(i))
                nuevostock = '%s%s' %("nuevostock",str(i))



                pro = Producto.objects.get(pk=request.POST[""+nombrepro])
                orden=get_object_or_404(OrdenTrabajo,ord_id=id)

                ordp=OrdenProducto( pro_id=pro,
                                    ord_id=orden,
                                    ordp_cantidad=request.POST[""+cantidad],
                                    ordp_precio=request.POST[""+precio],
                                    )
                ordp.save()

                provee = Proveedor.objects.get(prov_cedula=pro.prov_cedula_id)
                cate = Categoria.objects.get(cat_id=pro.cat_id_id)

                productonuevo=Producto(prov_cedula=provee,
                               cat_id=cate,
                               pro_id=pro.pro_id,
                               pro_nombre=pro.pro_nombre,
                               pro_modelo=pro.pro_modelo,
                               pro_marca=pro.pro_marca,
                               pro_stocka=request.POST[""+nuevostock],
                               pro_stockm=pro.pro_stockm,
                               pro_precio=pro.pro_precio,
                               pro_preciov=pro.pro_preciov,
                       )
                productonuevo.save()

    ord=OrdenTrabajo.objects.get(pk=id)
    listapro = []
    orden1=OrdenProducto.objects.filter(ord_id_id=id)
    produc=Producto.objects.all()
    if OrdenProducto.objects.filter(ord_id_id=id).exists():
        print "yaaaaaaaa"
        orden=OrdenProducto.objects.filter(ord_id_id=id)
        for i in orden:

            idpro = i.pro_id_id
            print idpro
            produc = Producto.objects.get(pro_id=idpro)
            listapro.append(produc)
    cedula = ord.cli_cedula_id
    print cedula
    cli=Cliente.objects.get(cli_cedula=cedula)

    return render_to_response('modificarorden1.html',{'ord':ord,'cli':cli,'orden1':orden1,'listapro':listapro},context_instance=RequestContext(request))

@login_required(login_url='/')
def buscarorden(request):
    if request.method=='POST':

        buscar = request.POST["txtBuscar"]
        print(buscar)
        if (request.POST["txtBuscar"] == ""):
            ord=OrdenTrabajo.objects.filter(ord_estado=request.POST["cmbTipo"]).values()
            return render_to_response('buscarorden.html',{'ord':ord},context_instance=RequestContext(request))
        else:
            ord=OrdenTrabajo.objects.filter(cli_cedula=request.POST["txtBuscar"]).values()
            return render_to_response('buscarorden.html',{'ord':ord},context_instance=RequestContext(request))



    ord=OrdenTrabajo.objects.all()





    return render_to_response('buscarorden.html',{'ord':ord},context_instance=RequestContext(request))




#GESTIONARCLIENTE


@login_required(login_url='/')
def ingresarcliente(request):
    if request.method=='POST':
        cli=Cliente(cli_cedula=request.POST["txtCedula"],
                    cli_nombre=request.POST["txtNombre"],
                    cli_apellido=request.POST["txtApellido"],
                    cli_telefono=request.POST["txtTel"],
                    cli_direccion=request.POST["txtDir"],
                    cli_ciudad=request.POST["txtCiu"],


                    )
        cli.save()

        return redirect('ingresarcliente')

    return render_to_response('ingresarcliente.html',"",context_instance=RequestContext(request))

@login_required(login_url='/')
def nuevocli(request):
    if request.method=='POST':
        cli=Cliente(cli_cedula=request.POST["txtCedula"],
                    cli_nombre=request.POST["txtNombre"],
                    cli_apellido=request.POST["txtApellido"],
                    cli_telefono=request.POST["txtTel"],
                    cli_direccion=request.POST["txtDir"],
                    cli_ciudad=request.POST["txtCiu"],


                    )
        cli.save()

        return redirect('ingresarorden')

    return render_to_response('nuevocli.html',"",context_instance=RequestContext(request))

@login_required(login_url='/')
def modificarcliente(request,id):
    if request.method=='POST':



            cli = Cliente(
                cli_cedula=id,
                cli_nombre=request.POST["txtNombre"],
                cli_apellido=request.POST["txtApellido"],
                cli_telefono=request.POST["txtTel"],
                cli_direccion=request.POST["txtDir"],
                cli_ciudad=request.POST["txtCiu"],)
            cli.save()

            return redirect(buscarcliente)


    cli=Cliente.objects.get(pk=id)


    return render_to_response('modificarcliente.html',{'cli':cli},context_instance=RequestContext(request))

@login_required(login_url='/')
def buscarcliente(request):
    if request.method=='POST':
        cli=Cliente.objects.filter(cli_nombre__contains=request.POST["txtBuscar"]).values()


        return render_to_response('buscarcliente.html',{'cli':cli},context_instance=RequestContext(request))

    cli=Cliente.objects.all()
    return render_to_response('buscarcliente.html',{'cli':cli},context_instance=RequestContext(request))

@login_required(login_url='/')
def ordencliente(request):

    if request.method=='POST':
        cli=Cliente.objects.filter(cli_nombre=request.POST["txtBuscar"]).values()


        return render_to_response('ordencliente.html',{'cli':cli},context_instance=RequestContext(request))

    cli=Cliente.objects.all()
    return render_to_response('ordencliente.html',{'cli':cli},context_instance=RequestContext(request))



#REPORTES


class IndexView(ListView):
    template_name = "reporteproducto.html"
    model = Producto
    context_object_name = "c"


def generar_pdf(request):
    print "Genero el PDF"
    response = HttpResponse(content_type='application/pdf')
    pdf_name = "productos.pdf"  # llamado clientes
    # la linea 26 es por si deseas descargar el pdf a tu computadora
    # response['Content-Disposition'] = 'attachment; filename=%s' % pdf_name
    buff = BytesIO()
    doc = SimpleDocTemplate(buff,
                            pagesize=letter,
                            rightMargin=40,
                            leftMargin=40,
                            topMargin=60,
                            bottomMargin=18,
                            )
    productos = []
    styles = getSampleStyleSheet()
    header = Paragraph("     Listado de Productos", styles['Heading1'])
    productos.append(header)
    headings = ('Proveedor','Categoria','Nombre','Modelo','Marca','Stock A', 'Stock M', 'Precio P', 'Precio V')
    allproductos = [(p.prov_cedula, p.cat_id, p.pro_nombre, p.pro_modelo,p.pro_marca,p.pro_stocka,p.pro_stockm,p.pro_precio,p.pro_preciov) for p in Producto.objects.all()]
    print allproductos

    t = Table([headings] + allproductos)
    t.setStyle(TableStyle(
        [
            ('GRID', (0, 0), (9, -1), 1, colors.springgreen),
            ('LINEBELOW', (0, 0), (-1, 0), 2, colors.springgreen),
            ('BACKGROUND', (0, 0), (-1, 0), colors.springgreen)
        ]
    ))
    productos.append(t)
    doc.build(productos)
    response.write(buff.getvalue())
    buff.close()
    return response


class Index(ListView):
    template_name = "reporteorden.html"
    model = OrdenTrabajo
    context_object_name = "c"


def generar_pdforden(request):
    print "Genero el PDF"
    response = HttpResponse(content_type='application/pdf')
    pdf_name = "ordenes.pdf"  # llamado clientes
    # la linea 26 es por si deseas descargar el pdf a tu computadora
    # response['Content-Disposition'] = 'attachment; filename=%s' % pdf_name
    buff = BytesIO()
    doc = SimpleDocTemplate(buff,
                            pagesize=letter,
                            rightMargin=40,
                            leftMargin=40,
                            topMargin=60,
                            bottomMargin=18,
                            )
    productos = []
    styles = getSampleStyleSheet()
    header = Paragraph("     Listado de Ordenes de Trabajo", styles['Heading1'])
    productos.append(header)
    headings = ('Cliente','Numero','Fecha Recepcion','Fecha Entrega','Tipo','Precio', 'Estado')
    allproductos = [(p.cli_cedula, p.ord_numero, p.ord_fechar, p.ord_fechae,p.ord_tipo,p.ord_precio,p.ord_estado) for p in OrdenTrabajo.objects.all()]
    print allproductos

    t = Table([headings] + allproductos)
    t.setStyle(TableStyle(
        [
            ('GRID', (0, 0), (9, -1), 1, colors.springgreen),
            ('LINEBELOW', (0, 0), (-1, 0), 2, colors.springgreen),
            ('BACKGROUND', (0, 0), (-1, 0), colors.springgreen)
        ]
    ))
    productos.append(t)
    doc.build(productos)
    response.write(buff.getvalue())
    buff.close()
    return response


def imprimirorden(request,id):
    ord=OrdenTrabajo.objects.get(pk=id)
    listapro = []
    orden1=OrdenProducto.objects.filter(ord_id_id=id)
    produc=Producto.objects.all()
    if OrdenProducto.objects.filter(ord_id_id=id).exists():
        print "yaaaaaaaa"
        orden=OrdenProducto.objects.filter(ord_id_id=id)
        for i in orden:

            idpro = i.pro_id_id
            print idpro
            produc = Producto.objects.get(pro_id=idpro)
            listapro.append(produc)
    cedula = ord.cli_cedula_id
    print cedula
    cli=Cliente.objects.get(cli_cedula=cedula)

    return render_to_response('imprimirorden.html',{'ord':ord,'cli':cli,'orden1':orden1,'listapro':listapro},context_instance=RequestContext(request))


def imprimirordeninicial(request,id):
    ord=OrdenTrabajo.objects.get(pk=id)
    listapro = []
    orden1=OrdenProducto.objects.filter(ord_id_id=id)
    produc=Producto.objects.all()
    cedula = ord.cli_cedula_id
    print cedula
    cli=Cliente.objects.get(cli_cedula=cedula)

    return render_to_response('imprimirordeninicial.html',{'ord':ord,'cli':cli,'orden1':orden1,'listapro':listapro},context_instance=RequestContext(request))

def notificaciones(request):
    print "aquiiiiiiiiiiiiiiii"
    Productos=Producto.objects.all()
    listaNotificaciones=[]
    for produc in Productos:
        print "2323232"
        if int(produc.pro_stocka)<=int(produc.pro_stockm):
            print "444444"
            listaNotificaciones.append(produc)
    data=serializers.serialize('json',listaNotificaciones,
                               fields={'pro_nombre','pro_id','pro_stocka','pro_stockm','pro_modelo','pro_marca',})

    return HttpResponse(data,content_type='application/json')