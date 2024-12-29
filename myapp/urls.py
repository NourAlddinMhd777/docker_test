from . import views
from django.urls import path

urlpatterns=[
    path(f'view',views.fun_view,name='fun_view'),
]
