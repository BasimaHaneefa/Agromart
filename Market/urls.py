
from django.urls import path

from Market import views

app_name="market"
urlpatterns = [
    path('markethome/', views.Markethomepage,name="markethome"),
    path('Myprofile/', views.Myprofile,name="myprofile"),
    path('Editprofile/', views.Editprofile,name="editprofile"),
    path('Changepassword/', views.Changepassword,name="changepassword"),
    path('FarmerRequest/', views.Farmerrequest,name="requestfarmer"),

   
    path('Farmeraccept/', views.Farmeraccept,name="farmeraccept"),
    path('Farmerreject/', views.Farmerreject,name="farmerreject"),
    path('af/<int:aid>', views.accept,name="acceptfarmer"),
    path('rf/<int:rid>', views.reject,name="rejectfarmer"),

    path('Marketfeedback/', views.Marketfeedback,name="marketfeedback"),
    path('delmfeedback/<int:mid>',views.Feedback_delete,name="delmfeedback"),

    path('Marketcomplaint/', views.Marketcomplaint,name="marketcomplaint"),
    path('delmcomplaint/<int:mid>',views.Complaint_delete,name="delmcomplaint"),

    path('markevent/', views.Markevent,name="markevent"),
    path('delmarkevent/<int:did>', views.DelMarkevent,name="delmarkevent"),   

    path('slotbookingrequest/', views.slotbookingrequest,name="slotbookingrequest"),
    path('Allotslot/<int:sid>', views.Allotslot,name="Allotslot"),
]



