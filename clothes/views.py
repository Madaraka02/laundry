from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from .models import *
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# Create your views here.

def home(request):
    clothes = Client.objects.all().order_by('-id')

    form = ClientForm()
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {
        'form':form,
        'clothes':clothes
    }  
    return render(request, 'home.html', context)      

def clients(request):
    # clothes = Client.objects.all().order_by('-id')
    clients_list = Client.objects.all().order_by('-id')
    page = request.GET.get('page', 1)
    paginator = Paginator(clients_list, 10)

    try:
        clothes = paginator.page(page)
    except PageNotAnInteger:
        clothes = paginator.page(1)
    except EmptyPage:
        clothes = paginator.page(paginator.num_pages)

    context = {
        'clothes':clothes
    }
    return render(request, 'clienst.html', context)      

def editClient(request, id):
    client = get_object_or_404(Client, id=id)

    form = ClientUpdateForm(instance=client)
    if request.method == 'POST':
        form = ClientUpdateForm(request.POST,instance=client)
        if form.is_valid():
            form.save()
            return redirect('clients')

    context = {
        'form':form,
        'client':client

    }       

    return render(request, 'update.html', context)      

def clientDelete(request, id):
    client = get_object_or_404(Client, id=id)
    client.delete()
    return redirect('clients')


                