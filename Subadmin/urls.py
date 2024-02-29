from django.urls import path
from Subadmin import views
app_name="subadmin"

urlpatterns = [
    
    path('Subadminhomepage/',views.Subadminhomepage,name="subadminhomepage"),
    path('Subadminprofile/', views.Subadminprofile,name="subadminprofile"),
    path('Editprofile/', views.Editprofile,name="editprofile"),
    path('Changepassword/', views.Changepassword,name="changepassword"),
    path('Newmarket/', views.Newmarket,name="newmarket"),
    path('Marketaccept/', views.Marketaccept,name="marketaccept"),
    path('Marketreject/', views.Marketreject,name="marketreject"),
    path('am/<int:aid>', views.accept,name="acceptmarket"),
    path('rm/<int:rid>', views.reject,name="rejectmarket"),

    path('Products/',views.Prod,name="Products"),
    path('delproduct/<int:did>', views.DelProd,name="delproduct"),
    path('prodstock/<int:pid>', views.ProdStock,name="prodstock"),
    path('delprodstock/<int:pid>',views.ProdStock_delete,name="delprodstock"),
    path('prodgallery/<int:pid>', views.Prodgallery,name="prodgallery"),
    path('delfeed/<int:fid>',views.DelViewgallery,name="delfeed"),

    path('FarmerVerification/',views.Farlist,name="FarmerVerification"),
    path('acceptfarmer/<int:acid>', views.acceptfrmr,name="acceptfarmer"),
    path('rejectfarmer/<int:rjid>', views.rejectfrmr,name="rejectfarmer"),

    path('FarmerAccepted/',views.acceptflist,name="FarmerAccepted"),
    path('FarmerRejected/',views.rejectflist,name="FarmerRejected"),


    path('viewreqs/',views.view_req,name="ViewRequests"),
    path('acceptreq/<int:arid>',views.accept_req,name="Accept_req"),
    path('rejectreq/<int:rrid>',views.reject_req,name="Reject_req"),
    path('acceptedreqs/',views.accepted_req,name="AcceptedRequests"),
    path('rejectedreqs/',views.rejected_req,name="RejectedRequests"),


   
]