from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.dashboard, name="dashboard"),
    path('logout/', views.logout_user, name='logout'),
    path('viewuser/<str:pk>/', views.view_user, name="viewuser"),
    path('bill/', views.bill, name="bill"),
    path('plans/', views.plans, name="plans"),
    path('createplan/', views.create_plan, name="createplan"),
    path('deleteplan/<int:pk>/', views.delete_plan, name="deleteplan"),
    path('updateplan/<int:pk>/', views.update_plan, name="updateplan"),
    path('users/', views.users, name="users"),
    path('createuser/', views.create_user, name="createuser"),
    path('deleteuser/<int:pk>/', views.delete_user, name="deleteuser"),
    path('edituser/<str:pk>/', views.edit_user, name="updateuser"),
    path('login/', views.login_page, name="login"),
]
