
from django.urls import path
from Guest import views
app_name="guest"
urlpatterns = [
    path('Login/', views.login,name="log"),
    path('forgotpass/', views.ForgotPass,name="forgotpass"),
    path('validateotp/', views.ValidateOtp,name="validateotp"),
    path('createpass/', views.CreatePass,name="createpass"),
    path('Market/', views.market,name="mark"),
    path('Ajaxplace/', views.ajaxplace,name="Ajax-place"),
    path('Farmer/', views.farmer,name="farm"),
    path('User/', views.user,name="user"),

    path('', views.home,name="Home"),
    path('Guest/', views.about,name="About"),
    path('Guest/', views.service,name="service"),

    
]