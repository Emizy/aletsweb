from django.shortcuts import render


# Create your views here.
def index(request):
    if request.method == 'GET':
        context = locals()
        templates = 'index.html'
        return render(request, templates, context)


def partner(request):
    if request.method == 'GET':
        context = locals()
        templates = 'partner.html'
        return render(request, templates, context)


def service(request):
    if request.method == 'GET':
        context = locals()
        templates = 'services.html'
        return render(request, templates, context)


def contacts(request):
    if request.method == 'GET':
        context = locals()
        templates = 'contact.html'
        return render(request, templates, context)

def crane(request):
    if request.method == 'GET':
        context = locals()
        templates = 'crane.html'
        return render(request, templates, context)
