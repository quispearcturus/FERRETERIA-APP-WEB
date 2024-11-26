# ZeroPaul
from django.urls import path, include
from apps.auths.views.login import LoginView,LogoutView, ChangePasswordView
# from django.contrib.auth.views import LogoutView

app_name = 'auths'

urlpatterns = [
    # path('example/', ExampleView.as_view(), name='example'),
    path('login/', LoginView.as_view(), name='login'),
    # path('logout/', LogoutView.as_view(), name='logout'),
    path('logout/', LogoutView.as_view(), name='logout'),
     path('change-password/', ChangePasswordView.as_view(), name='change_password'),
]