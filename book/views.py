from django.shortcuts import render,redirect
from .models import Book
from .forms import BookForm
from django.views import View
from django.views.generic import ListView, DetailView

# Create your views here.

# class BookList(View):
#     nombre_template = 'book/book_list.html'
    
#     def get(self,request):
#         form=BookForm()
#         return render(request, self.nombre_template, {'books': Book.objects.all(),'form':form})
    
#     def post(self,request):
#         form=BookForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('book_list')
#         return render(request, self.nombre_template, {'books': Book.objects.all(),'form':form})

class BookList(ListView):
    model = Book
    

class BookCreate(View):
    nombre_template = 'book/book_create.html'
    
    def get(self,request):
        form=BookForm()
        return render(request, self.nombre_template, {'books': Book.objects.all(),'form':form})
    
    def post(self,request):
        form=BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
        return render(request, self.nombre_template, {'books': Book.objects.all(),'form':form})
    

# class BookInspect(View):
#         nombre_template = 'book/book_inspect.html'
#         def get(self,request,pk):  
#             book = Book.objects.get(id=pk)
#             return render(request, self.nombre_template, {'book': book})

class BookInspect(DetailView):
    model = Book
    template_name = 'book/book_inspect.html'

class BookEdit(View):
    nombre_template = 'book/book_edit.html'

    def get(self,request,pk):
        book=Book.objects.get(id=pk)
        form=BookForm(instance=book)
        return render(request, self.nombre_template, {'book': book,'form':form})
    
    def post(self,request,pk):
        book=Book.objects.get(id=pk)
        form=BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
        return render(request, self.nombre_template, {'book': book,'form':form})
    
