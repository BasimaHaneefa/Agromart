from django.shortcuts import render,redirect
from Admin.models import *
from User.models import *
from Market.models import *
from Farmer.models import *
from Guest.models import *





# Create your views here.

def district(request):
    districtdata=District.objects.all()
    if request.method=="POST":
        d=District.objects.filter(name__icontains=request.POST.get("txtdis"))
        if d:
            return render(request,"Admin/District.html",{'data':districtdata,'msg':"District already exists"})
        else:
            District.objects.create(name=request.POST.get('txtdis'))
            return render(request,"Admin/District.html",{'data':districtdata})
    else:
        return render(request,"Admin/District.html",{'data':districtdata})

def Deldistrict(request,did):
    District.objects.get(id=did).delete()
    return redirect("wadmin:dis")

def Editdistrict(request,eid):
    dis=District.objects.get(id=eid)
    districtdata=District.objects.all()
    if request.method=="POST":
        dis.name=request.POST.get('txtdis')
        dis.save()
        return redirect("wadmin:dis")
    else:
        return render(request,"Admin/District.html",{'data':districtdata,'dis':dis})


def place(request):
    districtdata=District.objects.all()
    placedata=Place.objects.all()
    if request.method=="POST":
        d=Place.objects.filter(name__icontains=request.POST.get("txtplace"))
        if d:
            return render(request,"Admin/Place.html",{'place':placedata,'msg':"Place already exists"})
        else:
            dis=District.objects.get(id=request.POST.get('sel_dis'))
            Place.objects.create(name=request.POST.get('txtplace'), district=dis)
        return render(request,"Admin/Place.html",{'district':districtdata,'place':placedata})
    else:
        return render(request,"Admin/Place.html",{'district':districtdata,'place':placedata})

def Delplace(request,did):
    Place.objects.get(id=did).delete()
    return redirect("wadmin:place")
    




def login(request):
    if request.method=="POST":
        Subadmincount=Subadmin.objects.filter(email=request.POST.get('txtemail'),password=request.POST.get('txtpassword')).count()
        if Subadmincount > 0:
            subadmin=Subadmin.objects.get(email=request.POST.get('txtemail'),password=request.POST.get('txtpassword'))
            request.session['sid']=subadmin.id
            return redirect("subadmin:subadminhome")
    else:
        return render(request,"Guest/Login.html")



def subadmin(request):
    districtdata=District.objects.all()
    subadmindata=Subadmin.objects.all()
    if request.method=="POST":
        d=Subadmin.objects.filter(email__icontains=request.POST.get("txtemail"))
        if d:
            return render(request,"Admin/Newsubadmin.html",{'subadmin':subadmindata,'msg':"Email already exists"})
        else:
            dis=District.objects.get(id=request.POST.get('sel_dis'))
            Subadmin.objects.create(name=request.POST.get('txtname'),contact=request.POST.get('txtco'),email=request.POST.get('txtemail'),
            address=request.POST.get('txtaddress'),gender=request.POST.get('gender'),photo=request.FILES.get('txtphoto'),
            password=request.POST.get('txtpassword'),confirmpassword=request.POST.get('txtconfirmpassword'),district=dis)
            return redirect("wadmin:subadmin")
    else:
        return render(request,"Admin/Newsubadmin.html",{'district':districtdata,'subadmin':subadmindata})

def Delsubadmin(request,did):
    Subadmin.objects.get(id=did).delete()
    return redirect("wadmin:subadmin")

def Viewfeedback(request):
    userdata=User.objects.all()
    farmerdata=Farmer.objects.all()
    marketdata=Market.objects.all()
    userfeedback=Feedback.objects.filter(user__in=userdata)
    farmerfeedback=Feedback.objects.filter(farmer__in=farmerdata)
    marketfeedback=Feedback.objects.filter(market__in=marketdata)
    return render(request,"Admin/ViewFeedback.html",{'userfeedback':userfeedback,'farmerfeedback':farmerfeedback,'marketfeedback':marketfeedback})

def Viewcomplaintinsert(request):
    userdata=User.objects.all()
    farmerdata=Farmer.objects.all()
    marketdata=Market.objects.all()
    usercomplaint=Complaint.objects.filter(user__in=userdata)
    farmercomplaint=Complaint.objects.filter(farmer__in=farmerdata)
    marketcomplaint=Complaint.objects.filter(market__in=marketdata)
    return render(request,"Admin/ViewComplaint.html",{'usercomplaint':usercomplaint,'farmercomplaint':farmercomplaint,'marketcomplaint':marketcomplaint})


def ReplyInsert(request,cid):
    comp=Complaint.objects.get(id=cid)
    if request.method=="POST":
        comp.reply=request.POST.get('comprply')
        comp.status=1
        comp.save()
        return redirect("wadmin:complaint")
    else:
        return render(request,"Admin/Reply.html")


def ProdType(request):
    prodtype=SProductType.objects.all()
    if request.method=="POST":
        d=SProductType.objects.filter(producttype_name__icontains=request.POST.get("txt1"))
        if d:
            return render(request,"Admin/ProductType.html",{'ProdType':prodtype,'msg':"Data already exists"})
        else:
            SProductType.objects.create(producttype_name=request.POST.get('txt1'))
        return render(request,"Admin/ProductType.html",{'ProdType':prodtype})
    else:
        return render(request,"Admin/ProductType.html",{'ProdType':prodtype})

def DelProdType(request,did):
    prodtype=SProductType.objects.get(id=did)
    prodtype.delete()
    return redirect('wadmin:ProductType')

def Homepageadmin(request): 
    admin=Admin.objects.get(id=request.session["aid"]) 
    return render(request,"Admin/AdminHomePage.html",{'data':admin})


def UserReport(request):
    if request.method=="POST":
        frdate=request.POST.get('frdate')
        todate=request.POST.get('todate')
        data=Sendrequest.objects.filter(req_date__gte=frdate,req_date__lte=todate)
        return render(request,"Admin/UserReport.html",{'data':data,'f':frdate,'t':todate}) 
    return render(request,"Admin/UserReport.html")

def FarmerReport(request):
    if request.method=="POST":
        frdate=request.POST.get('frdate')
        todate=request.POST.get('todate')
        data=Request.objects.filter(req_date__gte=frdate,req_date__lte=todate)
        return render(request,"Admin/FarmerReport.html",{'data':data,'f':frdate,'t':todate}) 
    return render(request,"Admin/FarmerReport.html")

def MarketReport(request):
    if request.method=="POST":
        frdate=request.POST.get('frdate')
        todate=request.POST.get('todate')
        data=AuctionSlotBooking.objects.filter(slotbookdate__gte=frdate,slotbookdate__lte=todate)
        return render(request,"Admin/MarketReport.html",{'data':data,'f':frdate,'t':todate}) 
    return render(request,"Admin/MarketReport.html")