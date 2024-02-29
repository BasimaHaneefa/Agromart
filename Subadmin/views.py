from django.shortcuts import render,redirect
from Admin.models import *
from Market.models import *
from Farmer.models import *
from Guest.models import *
from Subadmin.models import *

def Subadminhomepage(request):
    return render(request,"subadmin/SadminHome.html")

def Subadminprofile(request):
    data=Subadmin.objects.get(id=request.session["sid"])
    return render(request,"subadmin/Subadminprofile.html",{'data':data})

def Editprofile(request):
    data=Subadmin.objects.get(id=request.session['sid'])
    if request.method=="POST":
        data.name=request.POST.get('txtname')
        data.contact=request.POST.get('txtcontact')
        data.address=request.POST.get('txtaddress')
        data.save()
        return redirect("subadmin:subadminprofile")
    else:
        return render(request,"subadmin/Editprofile.html", {'data':data})

def Changepassword(request):
    if request.method=="POST":
        Subadmincount=Subadmin.objects.filter(password=request.POST.get('currentpassword'),id=request.session["sid"]).count()
        if Subadmincount>0:
            subadmin=Subadmin.objects.get(password=request.POST.get('currentpassword'),id=request.session["sid"])
            if request.POST.get('newpassword')==request.POST.get('confirmpassword'):
                subadmin.password=request.POST.get('newpassword')
                subadmin.confirmpassword=request.POST.get('confirmpassword')
                subadmin.save()
                return redirect("subadmin:subadminhomepage")
            else:
                 return render(request,"subadmin/Changepassword.html")
        else:
             return render(request,"subadmin/Changepassword.html")
    else:
        return render(request,"subadmin/Changepassword.html")



def Newmarket(request):
    data=Market.objects.filter(status=0)
    return render(request,"subadmin/Newmarketlist.html",{'data':data})

def Marketaccept(request):
    data=Market.objects.filter(status=1)
    return render(request,"subadmin/Marketaccept.html",{'data':data})

def Marketreject(request):
    data=Market.objects.filter(status=2)
    return render(request,"subadmin/Marketreject.html",{'data':data})

def accept(request,aid):
    mark=Market.objects.get(id=aid)
    mark.status=1
    mark.save()
    return redirect("subadmin:newmarket")

def reject(request,rid):
    mark=Market.objects.get(id=rid)
    mark.status=2
    mark.save()
    return redirect("subadmin:newmarket")


def Prod(request): 
    ProdType=SProductType.objects.all() 
    Pro=Products.objects.all()
    if request.method=="POST" and request.FILES:
        d=Products.objects.filter(product_name__icontains=request.POST.get("txtname"))
        if d:
            return render(request,"Subadmin/Products.html",{'pro':Pro,'msg':"Product already exists"})
        else:
            prodtype=SProductType.objects.get(id=request.POST.get('sel_Producttype'))
            sub=Subadmin.objects.get(id=request.session["sid"]) 
            Products.objects.create(product_name=request.POST.get("txtname"),product_description=request.POST.get("txtname1"),
            product_rate=request.POST.get("txtname2"),product_image=request.FILES.get("image"),producttype=prodtype,subadmin=sub)
            return render(request,"Subadmin/Products.html",{'ProdType':ProdType,'pro':Pro}) 
    else: 
        return render(request,"Subadmin/Products.html",{'ProdType':ProdType,'pro':Pro}) 


def DelProd(request,did):
    prod=Products.objects.get(id=did)
    prod.delete()
    return redirect('subadmin:Products')


def ProdStock(request,pid):
    prod=Products.objects.get(id=pid)
    ProdType=ProductType.objects.all() 
    Pro=Products.objects.all()
    Prodstock=ProductStock.objects.all() 
    if request.method=="POST":
        ProductStock.objects.create(product_stock=request.POST.get("txt1"),product=prod)
        return redirect("subadmin:Products") 
    else: 
        return render(request,"Subadmin/ProductStock.html",{'Prodstock':Prodstock})

def ProdStock_delete(request,pid):
    ProductStock.objects.get(id=pid).delete()
    return redirect("subadmin:Products")

def Prodgallery(request,pid):
    prod=Products.objects.get(id=pid)
    prodimg=ProductGallery.objects.filter(product=prod)
    if request.method=="POST" and request.FILES:
        ProductGallery.objects.create(productgallery_image=request.FILES.get("photo"),product=prod)
        return redirect("subadmin:Products") 
    else: 
        return render(request,"Subadmin/AddGallery.html",{'data':prodimg})

def DelViewgallery(request,fid):
     feedb=ProductGallery.objects.get(id=fid)  
     feedb.delete()
     return redirect('subadmin:Viewgall')

def Farlist(request):
    newfar=Farmer.objects.filter(farmer_sts=0)
    return render(request,"Subadmin/FarmerVerification.html",{'data':newfar})

def acceptfrmr(request,acid):
    acceptf=Farmer.objects.get(id=acid)
    acceptf.farmer_sts=1
    acceptf.save()
    return redirect('subadmin:FarmerAccepted')

def rejectfrmr(request,rjid):
    rejectf=Farmer.objects.get(id=rjid)
    rejectf.farmer_sts=2
    rejectf.save()
    return redirect('subadmin:FarmerRejected')


def acceptflist(request):
    accorg=Farmer.objects.filter(farmer_sts=1)
    return render(request,"Subadmin/AcceptedList.html",{'data':accorg})    

def rejectflist(request):
    rejorg=Farmer.objects.filter(farmer_sts=2)
    return render(request,"Subadmin/RejectedList.html",{'data':rejorg})



# ----------------------- #


def view_req(request):
    vw=Request.objects.filter(product__subadmin=request.session['sid'],req_sts=0)
    return render(request,"Subadmin/ViewRequests.html",{'VR':vw})

def accept_req(request,arid):
    ar=Request.objects.get(id=arid)
    a=ar.product.id
    c=int(ar.quantity)
    ar.req_sts=1
    ar.save()
    stck=ProductStock.objects.get(product=a)
    b=int(stck.product_stock)
    newstock=b-c 
    stck.product_stock=newstock
    stck.save()
    return redirect('subadmin:ViewRequests')

def reject_req(request,rrid):
    rr=Request.objects.get(id=rrid)
    rr.req_sts=2
    rr.save()
    return redirect('subadmin:ViewRequests')

def accepted_req(request):
    accptdreq=Request.objects.filter(product__subadmin=request.session['sid'],req_sts=1)
    return render(request,"Subadmin/AcceptedRequests.html",{'AR':accptdreq})


def rejected_req(request):
    rjctdreq=Request.objects.filter(product__subadmin=request.session['sid'],req_sts=2)
    return render(request,"Subadmin/RejectedRequests.html",{'RR':rjctdreq})