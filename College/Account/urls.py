from django.conf.urls import url
from django.urls import include, path
from django.urls import path
from django.contrib.auth import views as auth_views
from College import settings
from django.conf.urls.static import static


from . import views
app_name="Account"
urlpatterns=[
url("^$",(views.signup_view) ,name="registration"),
url('login',views.signin_view,name='login'),
url('PytmResponse/',views.PytmResponse,name='payment_response'),
url('payment/',views.payment,name='payment'),


url('logout',views.logout_view,name='logout'),
url('home',views.home,name='home'),


url('', include('django.contrib.auth.urls')),
url('image',views.profile,name='upload')
]

'''
or we can add complete url and views
from django.contrib.auth import views as auth_views


urlpatterns = [
	...
	url(r'^password_reset/$', auth_views.password_reset, name='password_reset'),
	url(r'^password_reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
	url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
		auth_views.password_reset_confirm, name='password_reset_confirm'),
	url(r'^reset/done/$', auth_views.password_reset_complete, name='password_reset_complete'),
]'''
#40019420007599