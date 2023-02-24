from . import views
from django.urls import path

urlpatterns = [
    # path('', views.index, name= 'index'),
    path('', views.login_homepage, name='login_homepage'),
    path('login_authenticate/', views.login, name='login'),
    path('landingPageUser/', views.landingPageUser, name='landingPageUser'),
    path('shop/', views.shopBooks, name='shopBooks'),
    path('logout/', views.logout, name='logout'),
    path('cart/', views.cart, name='cart'),
    path('change_quantity/', views.change_quantity, name='change_quan'),
    path('cart/remove/<int:id>', views.remove, name='remove'),
    path('checkout/', views.checkout, name='checkout'),
    path('order', views.order, name='order'),
    path('reportUser/', views.reportUser, name='reportUser'),
    path('statusUser/', views.statusUser, name='statusUser'),
    path('viewDescriptionUser/', views.viewDescriptionUser, name='viewDescriptionUser'),
    path('contactUs/', views.contactUs, name='contactUs'),
    path('userProfile/', views.userProfile, name='userProfile'),
    path('orderConfirmed/', views.order, name='order'),
    path('orderStatus/', views.orderStatus, name='orderStatusUser'),
    # path('increase_quantity/', views.increase_cart_data, name='increase_cart_data'),
    # path('decrease_quantity/', views.decrease_cart_data, name='decrease_cart_data'),    

]
