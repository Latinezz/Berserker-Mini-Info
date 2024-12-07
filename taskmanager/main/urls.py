from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('about', views.about, name='we'),
    path('design', views.design, name='des'),
    path('korzina', views.korzina, name='korzina'),
    path('primary', views.primary, name='primary'),
    path('otryad',views.otryad, name='ot'),
    path('registration', views.registration, name='reg'),
    path('gif',views.gif, name='gif')
]