from django.shortcuts import render,redirect
from Admin.models import *
from Guest.models import *
from User.models import *
from Market.models import *
from Farmer.models import *
from Subadmin.models import *
import random
from datetime import datetime


# Create your views here.
def Farmerhomepage(request):
    return render(request,"farmer/Farmerhomepage.html")

def Myprofile(request):
    data=Farmer.objects.get(id=request.session['fid'])
    return render(request,"farmer/Myprofile.html",{'data': data})

def Editprofile(request):
    data=Farmer.objects.get(id=request.session['fid'])
    if request.method=="POST":
        data.name=request.POST.get('txtname')
        data.contact=request.POST.get('txtcontact')
        data.address=request.POST.get('txtaddress')
        data.save()
        return redirect("farmer:myprofile")
    else:
        return render(request,"farmer/Editprofile.html", {'data':data})

def Changepassword(request):
    if request.method=="POST":
        Farmercount=Farmer.objects.filter(password=request.POST.get('currentpassword'),id=request.session["fid"]).count()
        if Farmercount>0:
            farmer=Farmer.objects.get(password=request.POST.get('currentpassword'),id=request.session["fid"])
            if request.POST.get('newpassword')==request.POST.get('confirmpassword'):
                farmer.password=request.POST.get('newpassword')
                farmer.confirmpassword=request.POST.get('confirmpassword')
                farmer.save()
                return redirect("farmer:farmhome")
            else:
                 return render(request,"farmer/Changepassword.html")
        else:
             return render(request,"farmer/Changepassword.html")
    else:
        return render(request,"farmer/Changepassword.html")


def ajaxplace(request):
    dis=District.objects.get(id=request.GET.get('disid'))
    pla=Place.objects.filter(district=dis)
    return render(request,"Farmer/Ajaxplace.html",{'data':pla})
    

def Searchmarket(request):
    districtdata=District.objects.all()
    marketdata=Market.objects.all()
    return render(request,"Farmer/Searchmarket.html",{'dis':districtdata,'data':marketdata})

def ajaxmarket(request):
    if request.GET.get('plid')!="":
        pl=Place.objects.get(id=request.GET.get('plid'))
        data=Market.objects.filter(place=pl)
        return render(request,"Farmer/Ajaxmarket.html",{'data':data})
    else:
        dis=District.objects.get(id=request.GET.get('disd'))
        data=Market.objects.filter(place__district=dis)
        return render(request,"Farmer/Ajaxmarket.html",{'data':data})


def producttype(request):
    ptypedata=ProductType.objects.all()
    if request.method=="POST":
        d=ProductType.objects.filter(product_type__icontains=request.POST.get("ptype"))
        if d:
            return render(request,"Farmer/ProductType.html",{'data':ptypedata,'msg':"Product type already exists"})
        else:
            ProductType.objects.create(product_type=request.POST.get('ptype'))
            return render(request,"Farmer/ProductType.html",{'data':ptypedata})
    else:
        return render(request,"Farmer/ProductType.html",{'data':ptypedata})


def Delptype(request,did):
    ProductType.objects.get(id=did).delete()
    return redirect("farmer:PType")

def Editptype(request,eid):
    pt=ProductType.objects.get(id=eid)
    ptypedata=ProductType.objects.all()
    if request.method=="POST":
        pt.product_type=request.POST.get('ptype')
        pt.save()
        return redirect("farmer:PType")
    else:
        return render(request,"Farmer/ProductType.html",{'data':ptypedata,'ptype':pt})


def product(request):
    ptypedata=ProductType.objects.all()
    fam=Farmer.objects.get(id=request.session["fid"])
    productdata=FarmerProducts.objects.filter(farmer=fam)
    if request.method=="POST":
        d=FarmerProducts.objects.filter(name__icontains=request.POST.get("pname"))
        if d:
            return render(request,"Farmer/Product.html",{'data':productdata,'msg':"Product already exists"})
        else:
            pt=ProductType.objects.get(id=request.POST.get('sel_pytpe'))
            FarmerProducts.objects.create(name=request.POST.get('pname'),details=request.POST.get('pdetails'),photo=request.FILES.get('pphoto'),ptype=pt,rate=request.POST.get('prate'),farmer=fam)
            return render(request,"Farmer/Product.html",{'ptype':ptypedata,'data':productdata})
    else:
        return render(request,"Farmer/Product.html",{'ptype':ptypedata,'data':productdata})

def Delproduct(request,did):
    FarmerProducts.objects.get(id=did).delete()
    return redirect("farmer:product")

def stock(request):
    productdata=FarmerProducts.objects.all()
    stockdata=Stock.objects.all()
    if request.method=="POST":
        pro=FarmerProducts.objects.get(id=request.POST.get('sel_product'))  
        Stock.objects.create(date=request.POST.get('sdate'),quantity=request.POST.get('squantity'),product=pro)
        return redirect("farmer:stock")
    else:
        return render(request,"farmer/Stock.html",{'product':productdata,'stock':stockdata})

def Delstock(request,did):
    Stock.objects.get(id=did).delete()
    return redirect("farmer:stock")

def Userrequest(request):
    fam=Farmer.objects.get(id=request.session["fid"])
    userrequestdata=Sendrequest.objects.filter(farmer=fam,status=0)
    return render(request,"farmer/UserRequest.html",{'udata':userrequestdata})


def FarmerRequest(request,aid):
    productdata=Product.objects.all()
    fam=Farmer.objects.get(id=request.session["fid"])
    mark=Market.objects.get(id=aid)
    farmerrequestdata=farmerRequest.objects.filter(farmer=fam)
    if request.method=="POST":
        pro=FarmerProducts.objects.get(id=request.POST.get('sel_product'))
        farmerRequest.objects.create(content=request.POST.get('fcontent'),farmer=fam,product=pro,market=mark)
        return render(request,"Farmer/Requestproductfarmer.html",{'farmerdata':farmerrequestdata,'data':productdata})
    else:
        return render(request,"Farmer/Requestproductfarmer.html",{'farmerdata':farmerrequestdata,'data':productdata})

def Delrequest(request,did):
    farmerRequest.objects.get(id=did).delete()
    return redirect("farmer:searchmarket")


def Useraccept(request):
    us=User.objects.get(id=request.session["uid"])
    udata=Sendrequest.objects.filter(user=us,status=1)
    return render(request,"farmer/Useraccept.html",{'udata':udata})

def Userreject(request):
    us=User.objects.get(id=request.session["uid"])
    udata=Sendrequest.objects.filter(user=us,status=2)
    return render(request,"farmer/Userreject.html",{'udata':udata})

def accept(request,aid):
    us=Sendrequest.objects.get(id=aid)
    us.status=1
    us.save()
    
    return redirect("farmer:requestuser")

def reject(request,rid):
    us=Sendrequest.objects.get(id=rid)
    us.status=2
    us.save()
    return redirect("farmer:requestuser")





def Farmerfeedback(request):
    fam=Farmer.objects.get(id=request.session["fid"])
    farmerdata=Feedback.objects.filter(farmer=fam)
    if request.method=="POST":
        Feedback.objects.create(feedback=request.POST.get('ffdbk'),farmer=fam)
        return redirect("farmer:farmerfeedback")
    else:
        return render(request,"Farmer/Farmerfeedback.html",{'farmerfeed':farmerdata})


def Feedback_delete(request,fid):
    Feedback.objects.get(id=fid).delete()
    return redirect("farmer:farmerfeedback")

def Farmercomplaint(request):
    fam=Farmer.objects.get(id=request.session["fid"])
    farmerdata=Complaint.objects.filter(farmer=fam)
    if request.method=="POST":
        Complaint.objects.create(complaint=request.POST.get('farmcomp'),farmer=fam)
        return redirect("farmer:farmercomplaint")
    else:
        return render(request,"Farmer/Farmercomplaint.html",{'famcomp':farmerdata})


def Complaint_delete(request,fid):
    Complaint.objects.get(id=fid).delete()
    return redirect("farmer:farmercomplaint")




# ---------------------------#



def search_pdt(request):
    typeob=SProductType.objects.all()
    if request.method=="POST":
        pd=Products.objects.all()
        stock=ProductStock.objects.get(product=pd).count()
    
        return render(request,"Farmer/SearchProduct.html",{'TYP':typeob,'PD':pd})
    else:
        pd=Products.objects.all()
        return render(request,"Farmer/SearchProduct.html",{'TYP':typeob,'PD':pd})





def get_product(request):
    typ=SProductType.objects.get(id=request.GET.get('tid'))
    pd=Products.objects.filter(producttype=typ)
    return render(request,"Farmer/GetProduct.html",{'PD':pd})



def request_pdt(request,pid):
    pd=Products.objects.get(id=pid)
    frid=Farmer.objects.get(id=request.session["fid"])
    if request.method=="POST":
        Request.objects.create(quantity=request.POST.get('qnty'),
                               total_amnt=request.POST.get('total_amnt'),product=pd,farmer=frid)
        return redirect('farmer:MyRequests')
    else:
        return render(request,"Farmer/Request.html",{'P':pd})
    
def myreqsts(request):
    if 'fid' in request.session:
        req=Request.objects.filter(farmer=request.session['fid'])
        return render(request,"Farmer/MyRequests.html",{'RQ':req})
    
    
def paynow(request,pid):
    pay=Request.objects.get(id=pid)
    if request.method=="POST":
        pay.p_sts=1
        pay.save()
        return redirect('farmer:processingpayment')
    else:
        return render(request,"Farmer/Payment.html")
    


def processingpayment(request):
    return render(request,"Farmer/runpayment.html")


def paysuccess(request):
    return render(request,"Farmer/paysucessful.html")



def viewevents(request):
    events=Marketevent.objects.all()
    return render(request,"Farmer/ViewEvents.html",{'Events':events})



def slotbooking(request,rid):
    events=Marketevent.objects.get(id=rid)
    fam=Farmer.objects.get(id=request.session["fid"])
    AuctionSlotBooking.objects.create(marketevent=events,farmer=fam,slot_status=1)
    return redirect('farmer:ViewEvents')


def viewallocatedslots(request):
    frid=Farmer.objects.get(id=request.session["fid"])
    slots=SlotReply.objects.filter(slotbook__farmer=frid)
    return render(request,"Farmer/ViewAllocatedSlots.html",{'Slots':slots})
    



def Billing(request):
    if 'fid' in request.session:
        billno=random.randint(10000,99999)
   
        today = datetime.now()
        today=today.strftime("%d-%m-%Y")
   
        farm=Farmer.objects.get(id=request.session["fid"])
        uobj=Request.objects.filter(farmer=farm).last()
        return render(request,"Farmer/Bill.html",{'billno':billno,'today':today,'userdata':farm,'data':uobj})
    else:
        return redirect("guest:log")












