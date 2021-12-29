from django.shortcuts import render, redirect
from .models import Book
from django.contrib import messages
# Create your views here.
def index(request):
    data = Book.objects.all()
    messages.info(request,'List of books')
    return render(request, 'index.html',{'data':data})
def add(request):
    return render(request, 'add.html')
def create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        price = request.POST.get('price')
        data = Book.objects.create(title=title, author=author, price=price)
        messages.success(request, 'Book added successfully')
    return redirect('/')
def update(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        price = request.POST.get('price')
        data = Book.objects.get(id=request.POST.get('id'))
        data.title = title
        data.author = author
        data.price = price
        data.save()
        messages.success(request, 'Book updated successfully')
    return redirect('/') 
def edit(request, id):
    data = Book.objects.get(id=id)
    return render(request, 'edit.html', {'data':data})
def delete(request, id):
    data = Book.objects.get(id=id)
    data.delete()
    messages.success(request, 'Book deleted successfully')
    return redirect('/')