from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test 
from .models import *
from .forms import LugarPatrimonialForm

def home(request):
    return render(request, 'Patrimonio/home.html')

@login_required
def catalogo(request):
    categorias = Categoria.objects.all()
    catalogoCompleto = LugarPatrimonial.objects.all()
    return render(request, 'Patrimonio/catalogo.html', {'lugares': catalogoCompleto , 'categorias': categorias})

@login_required
@user_passes_test(lambda u: u.is_staff or u.is_superuser)
def gestion(request):
    catalogoCompleto = LugarPatrimonial.objects.all()
    return render(request, 'Patrimonio/gestion.html', {'lugares': catalogoCompleto})

@login_required
def detalle_lugar(request, id):
    lugar = get_object_or_404(LugarPatrimonial, id=id)
    return render(request, 'Patrimonio/detalle.html', {'lugar': lugar})

@login_required
def catalogoFiltro(request, id):
    categorias = Categoria.objects.all()
    categoria = get_object_or_404(Categoria, id=id)
    lugares_filtrados = LugarPatrimonial.objects.filter(categoria=categoria)
    return render(request, 'Patrimonio/catalogo.html', {'lugares': lugares_filtrados, 'categoria': categoria, 'categorias': categorias})

def login_view(request):
    fallo = False
    if request.method == 'POST':
        user = authenticate(request,username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            fallo = True
            
    return render(request, 'Patrimonio/sesion.html', {'fallo': fallo})

def registro(request):
    form = UserCreationForm(request.POST)

    if request.method == 'POST':

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')


        pass
    return render(request, 'Patrimonio/registro.html', {'form': form })


def cerrar_sesion(request):
    logout(request)
    return redirect('home')

@login_required
@user_passes_test(lambda u: u.is_staff or u.is_superuser)
def eliminar_lugar(request, id):
    lugar = get_object_or_404(LugarPatrimonial, id=id)
    if request.method == 'POST':
        lugar.delete()
        return redirect('gestion') # Redirige al panel o catálogo principal
        
    return redirect('home')

@login_required
@user_passes_test(lambda u: u.is_staff or u.is_superuser)
def gestion_form(request):
    fallo = False
    categorias = Categoria.objects.all()
    if request.method == 'POST':
        form = LugarPatrimonialForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('gestion')
        else: 
            fallo = True
    else:
        form = LugarPatrimonialForm()

    return render(request, 'Patrimonio/gestion_form.html', {'form': form, 'fallo': fallo, 'categorias': categorias})

@login_required
@user_passes_test(lambda u: u.is_staff)
def editar_lugar(request, id):
    lugar = get_object_or_404(LugarPatrimonial, id=id)
    
    if request.method == 'POST':
        form = LugarPatrimonialForm(request.POST, instance=lugar)
        
        if form.is_valid():
            form.save()
            return redirect('gestion')
    else:
        form = LugarPatrimonialForm(instance=lugar)
        
    return render(request, 'Patrimonio/gestion_form.html', {'form': form})