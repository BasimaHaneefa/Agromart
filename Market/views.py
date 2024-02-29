from django.shortcuts import render,redirect
from Admin.models import *
from Guest.models import *
from Farmer.models import *
from Market.models import *
# Create your views here.
def Markethomepage(request):
    data=Market.objects.get(id=request.session['mid'])
    return render(request,"market/Markethomepage.html",{'data': data})

def Myprofile(request):
    data=Market.objects.get(id=request.session['mid'])
    return render(request,"market/Myprofile.html",{'data': data})


def Editprofile(request):
    data=Market.objects.get(id=request.session['mid'])
    if request.method=="POST":
        data.name=request.POST.get('txtname')
        data.contact=request.POST.get('txtcontact')
        data.address=request.POST.get('txtaddress')
        data.save()
        return redirect("market:myprofile")
    else:
        return render(request,"market/Editprofile.html", {'data':data})

def Changepassword(request):
    if request.method=="POST":
        Marketcount=Market.objects.filter(password=request.POST.get('currentpassword'),id=request.session["mid"]).count()
        if Marketcount>0:
            market=Market.objects.get(password=request.POST.get('currentpassword'),id=request.session["mid"])
            if request.POST.get('newpassword')==request.POST.get('confirmpassword'):
                market.password=request.POST.get('newpassword')
                market.confirmpassword=request.POST.get('confirmpassword')
                market.save()
                return redirect("market:markethome")
            else:
                 return render(request,"market/Changepassword.html")
        else:
             return render(request,"market/Changepassword.html")
    else:
        return render(request,"market/Changepassword.html")


def Farmerrequest(request):
    mark=Market.objects.get(id=request.session["mid"])
    farmerrequestdata=farmerRequest.objects.filter(market=mark,status=0)
    return render(request,"market/ViewfarmerRequest.html",{'data':farmerrequestdata})


def Farmeraccept(request):
    mark=Market.objects.get(id=request.session["mid"])
    data=farmerRequest.objects.filter(market=mark,status=1)
    return render(request,"market/Farmeraccept.html",{'data':data})

def Farmerreject(request):
    mark=Market.objects.get(id=request.session["mid"])
    data=farmerRequest.objects.filter(market=mark,status=2)
    return render(request,"market/Farmerreject.html",{'data':data})

def accept(request,aid):
    farm=farmerRequest.objects.get(id=aid)
    farm.status=1
    farm.save()
    return redirect("market:requestfarmer")

def reject(request,rid):
    farm=farmerRequest.objects.get(id=rid)
    farm.status=2
    farm.save()
    return redirect("market:requestfarmer")


def Marketfeedback(request):
    mark=Market.objects.get(id=request.session["mid"])
    marketdata=Feedback.objects.filter(market=mark)
    if request.method=="POST":
        Feedback.objects.create(feedback=request.POST.get('mfdbk'),market=mark)
        return redirect("market:marketfeedback")
    else:
        return render(request,"Market/Marketfeedback.html",{'marketfeed':marketdata})


def Feedback_delete(request,mid):
    Feedback.objects.get(id=mid).delete()
    return redirect("market:marketfeedback")


def Marketcomplaint(request):
    mark=Market.objects.get(id=request.session["mid"])
    marketdata=Complaint.objects.filter(market=mark)
    if request.method=="POST":
        Complaint.objects.create(complaint=request.POST.get('markcomp'),market=mark)
        return redirect("market:marketcomplaint")
    else:
        return render(request,"Market/Marketcomplaint.html",{'markcomp':marketdata})


def Complaint_delete(request,mid):
    Complaint.objects.get(id=mid).delete()
    return redirect("market:marketcomplaint")



def Markevent(request):
    markevent=Marketevent.objects.all()
    m=Market.objects.get(id=request.session['mid'])
    if request.method=="POST":
        Marketevent.objects.create(marketevent_date=request.POST.get("date"),marketevent_starttime=request.POST.get("time"),
        marketevent_description=request.POST.get("txt"),market=m)
        return render(request,"Market/AddEvent.html",{'markevent':markevent})
    else: 
        return render(request,"Market/AddEvent.html",{'markevent':markevent}) 

def DelMarkevent(request,did):
    markevent=Marketevent.objects.get(id=did)
    markevent.delete()
    return redirect('market:markevent')


def slotbookingrequest(request):
    slotbooking=AuctionSlotBooking.objects.all()
    return render(request,"Market/SlotBookingRequest.html",{'SlotBooking':slotbooking})


def Allotslot(request,sid):
    slot=AuctionSlotBooking.objects.get(id=sid)
    if request.method=="POST":
        SlotReply.objects.create(slotbook=slot,slotreply_allocatetime=request.POST.get('txt_time'),slotreply_no=request.POST.get('txt_slotno'))
        return redirect('market:markethome')
    else:
        return render(request,"Market/SlotAllocation.html")


