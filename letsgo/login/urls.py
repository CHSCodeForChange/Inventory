from django.conf.urls import url
from . import views
from django.contrib.auth.views import LoginView

urlpatterns = [
url(r'login',LoginView.as_view(template_name='login/logininfo.html'), name = 'login'),
url(r'home',views.index, name = "index" ),
url(r'^signup/$', views.signup, name='signup')
]
