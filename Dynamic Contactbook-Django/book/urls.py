from django.urls import path
from . import views

urlpatterns =[

    path('',views.index , name="index"),
    path('add/',views.add , name="add"),
    path('profile/<str:pk>',views.profile,name='profile'),
    path('edit/<str:pk>',views.edit,name="edit"),
    path('delete/<str:pk>',views.delete,name = 'delete')
]
