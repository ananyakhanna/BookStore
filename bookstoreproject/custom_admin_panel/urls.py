from django.urls import path
from .import views
from bookstoreapp.views import logout

urlpatterns = [
    path('dashboardAdmin/', views.dashboard, name='dashboard'),
    path('bookAdmin/', views.book, name='bookAdmin'),
    path('bookAdmin/delete/<int:id>', views.delete, name='delete'),
    path('create/', views.create, name='create'),
    path('addUser/', views.AddUser.as_view(), name='addUserAdmin'),
    path('statusAdmin/', views.statusAdmin, name='statusAdmin'),
    path('viewDescription/', views.viewDescription, name='viewDescription'),
    path('editBook/', views.editBook, name='editBook'),
    path('logout/', logout, name='logout')

]