from django.urls import path
from Farmer import views

app_name="farmer"

urlpatterns = [
    path('farmerhomepage/', views.Farmerhomepage,name="farmhome"),
    path('Myprofile/', views.Myprofile,name="myprofile"),
    path('Editprofile/', views.Editprofile,name="editprofile"),
    path('Changepassword/', views.Changepassword,name="changepassword"),

    path('Ajaxplace/', views.ajaxplace,name="Ajax-place"),
    path('Searchmarket/', views.Searchmarket,name="searchmarket"),
    path('Ajaxmarket/', views.ajaxmarket,name="Ajax-Market"),

    path('ptype/', views.producttype,name="PType"),
    path('delptype/<int:did>',views.Delptype,name="delptype"),
    path('editptype/<int:eid>',views.Editptype,name="editptype"),

    path('Product/', views.product,name="product"),
    path('delproduct/<int:did>',views.Delproduct,name="delproduct"),
    path('Stock/', views.stock,name="stock"),
    path('delstock/<int:did>',views.Delstock,name="delstock"),

    path('UserRequest/', views.Userrequest,name="requestuser"),
    path('FarmerRequest/<int:aid>', views.FarmerRequest,name="farmerrequest"),
    path('delrequest/<int:did>',views.Delrequest,name="delrequest"),

    path('Useraccept/', views.Useraccept,name="useraccept"),
    path('Userreject/', views.Userreject,name="userreject"),
    path('au/<int:aid>', views.accept,name="acceptuser"),
    path('ru/<int:rid>', views.reject,name="rejectuser"),

    path('Farmerfeedback/', views.Farmerfeedback,name="farmerfeedback"),
    path('delffeedback/<int:fid>',views.Feedback_delete,name="delffeedback"),

    path('Farmercomplaint/', views.Farmercomplaint,name="farmercomplaint"),
    path('delfcomplaint/<int:fid>',views.Complaint_delete,name="delfcomplaint"),

    path('searchpdt/',views.search_pdt,name="Search_Pdt"), 
  
    path('getproduct/',views.get_product,name="GetProduct"),
    path('request/<int:pid>',views.request_pdt,name="Request"),
    path('myreqsts/',views.myreqsts,name="MyRequests"),
    path('paynow/<int:pid>',views.paynow,name="PayNow"),
    path('processingpayment/', views.processingpayment,name="processingpayment"),
    path('paymentsuccessful/', views.paysuccess,name="paysuccess"),

    path('viewevents/',views.viewevents,name="ViewEvents"),   
    path('slotbooking/<int:rid>',views.slotbooking,name="BookSlot"),  

    path('viewallocatedslots/',views.viewallocatedslots,name="viewallocatedslots"),
    path('Billing/',views.Billing,name="Billing"),
 
]



