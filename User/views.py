from django.shortcuts import render,redirect
from Admin.models import *
from Guest.models import *
from Farmer.models import *
from Market.models import *
from User.models import *
# Create your views here.
def Userhomepage(request):
    return render(request,"user/Userhomepage.html")

def Myprofile(request):
    data=User.objects.get(id=request.session['uid'])
    return render(request,"user/Myprofile.html",{'data':data})

def Editprofile(request):
    data=User.objects.get(id=request.session['uid'])
    if request.method=="POST":
        data.name=request.POST.get('txtname')
        data.contact=request.POST.get('txtcontact')
        data.address=request.POST.get('txtaddress')
        data.save()
        return redirect("user:myprofile")
    else:
        return render(request,"user/Editprofile.html", {'data':data})

def Changepassword(request):
    if request.method=="POST":
        Usercount=User.objects.filter(password=request.POST.get('currentpassword'),id=request.session["uid"]).count()
        if Usercount>0:
            user=User.objects.get(password=request.POST.get('currentpassword'),id=request.session["uid"])
            if request.POST.get('newpassword')==request.POST.get('confirmpassword'):
                user.password=request.POST.get('newpassword')
                user.confirmpassword=request.POST.get('confirmpassword')
                user.save()
                return redirect("user:userhome")
            else:
                 return render(request,"user/Changepassword.html")
        else:
             return render(request,"user/Changepassword.html")
    else:
        return render(request,"user/Changepassword.html")

def ajaxplace(request):
    dis=District.objects.get(id=request.GET.get('disid'))
    pla=Place.objects.filter(district=dis)
    return render(request,"Guest/Ajaxplace.html",{'data':pla})
    

def Searchfarmer(request):
    districtdata=District.objects.all()
    farmerdata=Farmer.objects.all()
    return render(request,"User/Searchfarmer.html",{'dis':districtdata,'fdata':farmerdata})


def ajaxfarmer(request):
    if request.GET.get('plid')!="":
        pl=Place.objects.get(id=request.GET.get('plid'))
        data=Farmer.objects.filter(place=pl)
        return render(request,"User/Ajaxfarmer.html",{'data':data})
    else:
        dis=District.objects.get(id=request.GET.get('disd'))
        data=Farmer.objects.filter(place__district=dis)
        return render(request,"User/Ajaxfarmer.html",{'data':data})


def Searchproduct(request,fid):
    ptypedata=ProductType.objects.all()
    fam=Farmer.objects.get(id=fid)
    request.session["farmer"]=fid
    productdata=FarmerProducts.objects.filter(farmer=fam)
    return render(request,"User/Searchproduct.html",{'data':productdata,'ptype':ptypedata})

def ajaxproduct(request):
    fam=Farmer.objects.get(id=request.session["farmer"])
    ptypeid=ProductType.objects.get(id=request.GET.get('disd'))
    productdata=FarmerProducts.objects.filter(farmer=fam,ptype=ptypeid)
    return render(request,"User/Ajaxproduct.html",{'data':productdata})

def ProductRequest(request,pid):
    pro=FarmerProducts.objects.get(id=pid)
    fam=Farmer.objects.get(id=request.session["fid"])
    us=User.objects.get(id=request.session["uid"])
    sendrequestdata=Sendrequest.objects.filter(user=us,farmer=fam)
    if request.method=="POST":
        Sendrequest.objects.create(content=request.POST.get('ucontent'),product=pro,user=us,farmer=fam)
        return render(request,"User/Requestproductuser.html",{'farmerdata':sendrequestdata})
    else:
        return render(request,"User/Requestproductuser.html",{'farmerdata':sendrequestdata})

def Delurequest(request,did):
    Sendrequest.objects.get(id=did).delete()
    return redirect("user:searchfarmer")


def Userfeedback(request):
    us=User.objects.get(id=request.session["uid"])
    userdata=Feedback.objects.filter(user=us)
    if request.method=="POST":
        Feedback.objects.create(feedback=request.POST.get('ufdbk'),user=us)
        return redirect("user:userfeedback")
    else:
        return render(request,"User/UserFeedback.html",{'userfeed':userdata})


def Feedback_delete(request,uid):
    Feedback.objects.get(id=uid).delete()
    return redirect("user:userfeedback")

def Usercomplaint(request):
    us=User.objects.get(id=request.session["uid"])
    userdata=Complaint.objects.filter(user=us)
    if request.method=="POST":
        Complaint.objects.create(complaint=request.POST.get('usercomp'),user=us)
        return redirect("user:usercomplaint")
    else:
        return render(request,"User/Usercomplaint.html",{'usercomp':userdata})


def Complaint_delete(request,uid):
    Complaint.objects.get(id=uid).delete()
    return redirect("user:usercomplaint")



def Viewstock(request):
    stockdata=Stock.objects.all()
    return render(request,"User/Viewstocks.html",{'userstock':stockdata})


def myrequests(request):
    us=User.objects.get(id=request.session["uid"])
    req=Sendrequest.objects.filter(user=us)
    return render(request,"User/MyRequests.html",{'farmerdata':req})



def paynow(request,pid):
    pay=Sendrequest.objects.get(id=pid)
    if request.method=="POST":
        pay.payment_sts=1
        pay.save()
        return redirect('user:processingpayment')
    else:
        return render(request,"User/Payment.html")


def processingpayment(request):
    return render(request,"User/runpayment.html")


def paysuccess(request):
    return render(request,"User/paysucessful.html")






        