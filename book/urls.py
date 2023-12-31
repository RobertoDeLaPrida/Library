from django.urls import path

from .views import BookCreate, BookEdit, BookInspect, BookList, BookDelete

urlpatterns = [

path('',BookList.as_view(), name='book_list'),
path('create',BookCreate.as_view(), name='book_create'),
path('inspect/<int:pk>',BookInspect.as_view(),name='book_inspect'),
path('edit/<int:pk>',BookEdit.as_view(),name='book_edit'),
path('book/delete/<int:pk>',BookDelete.as_view(), name='book_delete'),

]