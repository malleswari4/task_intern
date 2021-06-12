from django.urls import path
from App import views
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('index/',views.index,name="index"),
    path('login/',views.login,name="login"),
    path('signup/',views.signup,name="signup"),
    path('users/',views.users,name="users"),
    path('edit/<str:pk>',views.edit,name="edit"),
    path('delete/<int:pk>',views.delete,name='delete'),
    path('update/<str:pk>',views.update,name="update"),
    path('logout/',views.logout,name="logout"),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]