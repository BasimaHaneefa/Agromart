
from django.urls import path
from Admin import views
from Guest import views
from Farmer import views
from User import views

app_name="user"
urlpatterns = [
    path('Userhomepage/', views.Userhomepage,name="userhome"),
    path('Myprofile/', views.Myprofile,name="myprofile"),
    path('Editprofile/', views.Editprofile,name="editprofile"),
    path('Changepassword/', views.Changepassword,name="changepassword"),
    path('Ajaxplace/', views.ajaxplace,name="Ajax-place"),
    path('Searchfarmer/', views.Searchfarmer,name="searchfarmer"),
    path('Ajaxfarmer/', views.ajaxfarmer,name="Ajax-Farmer"),
    path('Searchproduct/<int:fid>', views.Searchproduct,name="searchproduct"),
    path('ajax-product/', views.ajaxproduct,name="ajax-product"),
    path('SendRequest/<int:pid>', views.ProductRequest,name="requestproduct"),
    path('delurequest/<int:did>',views.Delurequest,name="delurequest"),
    path('Userfeedback/', views.Userfeedback,name="userfeedback"),
    path('delufeedback/<int:uid>',views.Feedback_delete,name="delufeedback"),

    path('Usercomplaint/', views.Usercomplaint,name="usercomplaint"),
    path('delucomplaint/<int:uid>',views.Complaint_delete,name="delucomplaint"),
    path('Userstock/', views.Viewstock,name="viewstock"),   

    path('myrequests/', views.myrequests,name="myrequests"), 

    path('paynow/<int:pid>', views.paynow,name="paynow"),
    path('processingpayment/', views.processingpayment,name="processingpayment"),
    path('paymentsuccessful/', views.paysuccess,name="paysuccess"),
]
