from django.urls import path
from . import views

urlpatterns = [

    path('manage_user/', views.manage_user, name="manage-user"),
    path('student/', views.index, name="index"),
    path('<str:ic_no>', views.user_detail, name="user-detail"),
    path('newUser_form/', views.newUser_form, name="newUser-form"),
    path('editUser_form/<ic_no>/', views.editUser_form, name="editUser-form"),
    path('delete_user/<ic_no>/', views.delete_user, name="delete-user"),
]