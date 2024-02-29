
from django.urls import path
from Admin import views
app_name="wadmin"
urlpatterns = [
    path('District/', views.district,name="dis"),
    path('deldis/<int:did>',views.Deldistrict,name="deldistrict"),
    path('editdis/<int:eid>',views.Editdistrict,name="editdistrict"),
    path('adminhome/', views.Homepageadmin,name="adminhome"),


    path('Place/', views.place,name="place"),
    path('delPlace/<int:did>',views.Delplace,name="delplace"),

   
    path('Subadmin/', views.subadmin,name="subadmin"),
    path('delsubadmin/<int:did>',views.Delsubadmin,name="delsubadmin"),

    path('Feedback/', views.Viewfeedback,name="viewfeedback"),
    path('complaint/', views.Viewcomplaintinsert,name="complaint"),
    path('Reply/<int:cid>', views.ReplyInsert,name="reply"),
    

     path('ProductType/', views.ProdType,name="ProductType"),
     path('delproducttype/<int:did>', views.DelProdType,name="delproducttype"),

    path('userreport/', views.UserReport,name="userreport"),
    path('farmerreport/', views.FarmerReport,name="farmerreport"),
    path('marketreport/', views.MarketReport,name="marketreport"),

]