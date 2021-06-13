from django.urls import path
from App import views

urlpatterns = [
    path('index/',views.index,name="index"),
    path('login/',views.login,name="login"),
    path('signup/',views.signup,name="signup"),
    path('users/',views.users,name="users"),
    path('edit/<str:pk>',views.edit,name="edit"),
    path('delete/<int:pk>',views.delete,name='delete'),
    path('update/<str:pk>',views.update,name="update"),
    path('logout/',views.logout,name="logout"),
   
]