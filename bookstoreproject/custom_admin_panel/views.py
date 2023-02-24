from django.shortcuts import render, redirect, get_object_or_404
from bookstoreapp.models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.generic import CreateView
from .forms import *
# Create your views here.

def dashboard(request):
    return render(request, 'dashboardAdmin.html')

def book(request):
    book = Book.objects.all()
    context = {
        'book': book,
    }
    return render(request, 'bookAdmin.html', context)

def delete(request, id):
    book = Book.objects.get(id=id)
    book.delete()
    messages.success(request, 'Book - {} has been successfully deleted.'.format(book.name))
    return redirect('bookAdmin')

def create(request):
    context = {}
    if request.method == 'POST':
        name = request.POST['name']
        amount = request.POST['amount']
        description = request.POST['description']

        if 'image' in request.FILES:
            image = request.FILES['image']
        
        newBook = Book(name=name, amount=amount, description=description, image=image)
        newBook.save()
        messages.success(request, 'Book-{} has been created successfully'.format(name))
    return render(request, 'createAdmin.html', context)

class AddUser(CreateView):
    model: User
    form_class = UCF
    template_name = "../templates/addUseradmin.html/"
    context_object_name = 'form'

    def form_valid(self, form):
        form.save()
        # print(form)
        messages.success(self.request, 'The user is registered successfully!')
        return redirect('addUserAdmin')
   

def statusAdmin(request):
    context = {}
    obj = IncidentReport.objects.all()
    context['incident'] = obj

    if request.method == 'POST':
        incident_id = request.POST.get('incident-id')
        
        incident = IncidentReport.objects.get(id=incident_id)
        incident.action = True
        incident.save()
        messages.success(request, 'The incident has been fixed successfully!')
    # incident_id = request.GET.get('incident-id')
    # request.session['incident-id'] = incident_id
    return render(request, 'statusAdmin.html', context)

def viewDescription(request):
    context = {}
    # incident = IncidentReport.objects.all()
    if request.method == 'POST':
        incident_id = request.POST.get('incident-id')
        # print('hiii')
        # print(incident_id)
        incident = IncidentReport.objects.get(id=incident_id)
        context['incident'] = incident

    return render(request, 'viewDescription.html', context)

def editBook(request):
    context = {}
    book_id = request.GET.get("book-id")
    request.session['book-id'] = book_id
    getBook = get_object_or_404(Book, id=book_id)
    context['book'] = getBook

    if request.method == 'POST':
        name = request.POST['name']
        amount = request.POST['amount']
        description = request.POST['description']
            
        if 'image' in request.FILES:
            image = request.FILES['image']
            getBook.image = image

        getBook.name = name
        getBook.amount = amount
        getBook.description = description

        getBook.save()
        messages.success(request, 'Changes saved successfully')
        context["id"] = request.session.get('book-id')

        # print(request.POST)

    return render(request, 'editBookAdmin.html', context) 