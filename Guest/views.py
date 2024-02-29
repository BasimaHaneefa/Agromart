from django.shortcuts import render,redirect

from django.conf import settings
from django.core.mail import send_mail
from django.contrib import messages

from Guest.models import *
from Admin.models import *
import random

# Create your views here.
def login(request):
    if request.method=="POST":
        Farmercount=Farmer.objects.filter(email=request.POST.get('txtemail'),password=request.POST.get('txtpassword')).count()
        Marketcount=Market.objects.filter(email=request.POST.get('txtemail'),password=request.POST.get('txtpassword'),status=1).count()
        Usercount=User.objects.filter(email=request.POST.get('txtemail'),password=request.POST.get('txtpassword')).count()
        Subadmincount=Subadmin.objects.filter(email=request.POST.get('txtemail'),password=request.POST.get('txtpassword')).count()
        Admincount=Admin.objects.filter(email=request.POST.get('txtemail'),password=request.POST.get('txtpassword')).count()


    
        if Farmercount > 0:
            farmer=Farmer.objects.get(email=request.POST.get('txtemail'),password=request.POST.get('txtpassword'))
            request.session['fid']=farmer.id
            return redirect("farmer:farmhome")
        elif Marketcount > 0:
            market=Market.objects.get(email=request.POST.get('txtemail'),password=request.POST.get('txtpassword'),status=1)
            request.session['mid']=market.id
            return redirect("market:markethome")
        elif Usercount > 0:
            user=User.objects.get(email=request.POST.get('txtemail'),password=request.POST.get('txtpassword'))
            request.session['uid']=user.id
            return redirect("user:userhome")
        elif Subadmincount > 0:
            subadmin=Subadmin.objects.get(email=request.POST.get('txtemail'),password=request.POST.get('txtpassword'))
            request.session['sid']=subadmin.id
            return redirect("subadmin:subadminhomepage")
        elif Admincount > 0:
            admin=Admin.objects.get(email=request.POST.get('txtemail'),password=request.POST.get('txtpassword'))
            request.session['aid']=admin.id
            return redirect("wadmin:adminhome")
        else:
            return render(request,"Guest/Login.html")

    else:
        return render(request,"Guest/Login.html")

def ForgotPass(request):
    if request.method=="POST":
        otp=(random.randint(100000,999999))
        request.session["otp"]=otp
        request.session["femail"]=request.POST.get('txt_email')
        send_mail(
            'Respected Sir/Madam '+" ",#subject
            "Your Otp is"+str(otp),#body
            settings.EMAIL_HOST_USER,
            [request.POST.get('txt_email')],
        )
        return redirect('guest:validateotp')
    else:
        return render(request,"Guest/ForgotPassword.html")

def ValidateOtp(request):
    if request.method=="POST":
        otp=request.POST.get("txt_otp")
        ce=str(request.session["otp"])
        if otp==ce:
            return redirect("guest:createpass")
    return render(request,"Guest/ValidateOTP.html")

def CreatePass(request):
    if request.method=="POST":
        if request.POST.get("txt_pass")==request.POST.get("txt_confirm"):
            usercount=User.objects.filter(email=request.session["femail"]).count()
            techniciancount=Farmer.objects.filter(email=request.session["femail"]).count()
            if usercount>0:
                user=User.objects.get(email=request.session["femail"])
                user.password=request.POST.get("txt_pass")
                user.save()
                return redirect("guest:log")
            elif techniciancount>0:
                  technician=Farmer.objects.get(email=request.session["femail"])
                  technician.password=request.POST.get("txt_pass")
                  technician.save()
                  return redirect("guest:log")
        else:
            return render(request,"Guest/CreatePassword.html",{'msg':"Passwords not same"})
    else:
        return render(request,"Guest/CreatePassword.html")




def market(request):
    districtdata=District.objects.all()
    if request.method=="POST":
        pla=Place.objects.get(id=request.POST.get('txtplace'))
        Market.objects.create(name=request.POST.get('txtname'),contact=request.POST.get('txtcontact'),email=request.POST.get('txtemail'),address=request.POST.get('txtaddress'),logo=request.FILES.get('txtlogo'),proof=request.FILES.get('txtproof'),password=request.POST.get('txtpassword'),confirmpassword=request.POST.get('txtconfirm'),place=pla)
        
        market=Market.objects.latest('id')
        name=market.name
        email=market.email
        send_mail(
                'Respected sir/madam '+name, #subject
                "\rYour Deal is Successfully Confirmed By  MunicippalOfficer and Proceed To  welcome you to Municipal-E-GOV.your Username  is " + email + ".\n This is from DreamBuild team thank you for signing up to our service. \r\n If you have any questions and if there is anything we can improve please reply to this email. \r\n we were always happy to help!. \r\n \r\n Team DreamBuild.\n Thank you.",#body
                settings.EMAIL_HOST_USER,
                [email],

            )
        return render(request,"Guest/Newmarket.html",{'data':districtdata})
    else:
        return render(request,"Guest/Newmarket.html",{'data':districtdata})

def ajaxplace(request):
    dis=District.objects.get(id=request.GET.get('disd'))
    pla=Place.objects.filter(district=dis)
    return render(request,"Guest/Ajaxplace.html",{'data':pla})

def farmer(request):
    districtdata=District.objects.all()
    if request.method=="POST":
        d=Farmer.objects.filter(email__icontains=request.POST.get("femail"))
        if d:
            return render(request,"Guest/Newfarmer.html",{'data':districtdata,'msg':"Email already exists"})
        else:
            pla=Place.objects.get(id=request.POST.get('txtplace'))
            Farmer.objects.create(name=request.POST.get('fname'),contact=request.POST.get('fcontact'),email=request.POST.get('femail'),address=request.POST.get('faddress'),gender=request.POST.get('gender'),photo=request.FILES.get('fphoto'),password=request.POST.get('fpassword'),confirmpassword=request.POST.get('fconfirm'),place=pla)
            
            farm=Farmer.objects.latest('id')
            name=farm.name
            email=farm.email
            send_mail(
                    'Respected sir/madam '+name, #subject
                    "\rYour havev Successfully Registered as  farmer in AgroAcre's and Proceed To  welcome you to AgroAcre's.your Username  is " + email + ".\n This is from DreamBuild team thank you for signing up to our service. \r\n If you have any questions and if there is anything we can improve please reply to this email. \r\n we were always happy to help!. \r\n \r\n Team DreamBuild.\n Thank you.",#body
                    settings.EMAIL_HOST_USER,
                    [email],

                )

            return render(request,"Guest/Newfarmer.html",{'data':districtdata})
    else:
        return render(request,"Guest/Newfarmer.html",{'data':districtdata})

def user(request):
    districtdata=District.objects.all()
    if request.method=="POST":
        d=User.objects.filter(email__icontains=request.POST.get("txtemail"))
        if d:
            return render(request,"Guest/Newuser.html",{'data':districtdata,'msg':"Email already exists"})
        else:
            pla=Place.objects.get(id=request.POST.get('txtplace'))
            User.objects.create(name=request.POST.get('txtname'),contact=request.POST.get('txtcontact'),email=request.POST.get('txtemail'),address=request.POST.get('txtaddress'),
            gender=request.POST.get('gender'),photo=request.FILES.get('txtphoto'),password=request.POST.get('txtpassword'),confirmpassword=request.POST.get('txtconfirm'),place=pla)
            
            user=User.objects.latest('id')
            name=user.name
            email=user.email
            send_mail(
                    'Respected sir/madam '+name, #subject
                    "\rYour havev Successfully Registered as  user in AgroAcre's and Proceed To  welcome you to AgroAcre's.your Username  is " + email + ".\n This is from DreamBuild team thank you for signing up to our service. \r\n If you have any questions and if there is anything we can improve please reply to this email. \r\n we were always happy to help!. \r\n \r\n Team DreamBuild.\n Thank you.",#body
                    settings.EMAIL_HOST_USER,
                    [email],

                )

            return render(request,"Guest/Newuser.html",{'data':districtdata})
    else:
        return render(request,"Guest/Newuser.html",{'data':districtdata})




def home(request):
    return render(request,"Guest/Home.html")


def about(request):
    return render(request,"Guest/Aboutus.html")

def service(request):
    return render(request,"Guest/Service.html")
