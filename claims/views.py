from django.http.response import Http404
from django.shortcuts import render, redirect
from .models import LeadDetails, User, AgentUser,VechileDetails,ObjectDetails,FeedBack
from django.contrib.auth import login, logout, authenticate
from django.views.generic.list import ListView
from django.views.generic import TemplateView
from django.core.mail import send_mail
from django.conf import settings


def Leadlist(request):
    
    user = request.user
    idl = User.objects.filter(username = user.username).first()
    data = LeadDetails.objects.filter(user = idl)
    context = {
        'data': data,
        "user": idl
    }
    return render(request, 'list.html', context)


def Agentleadslist(request):
    username = request.user.username
    user = User.objects.filter(username = username).first()
    auser = AgentUser.objects.filter(user = user).first()
    data = LeadDetails.objects.filter(agent = auser)
    context = {
    'data' :data
    }
    return render(request,'Agentleads.html',context)



def LandingPage(request):
    user = request.user
    context = {
    "user":user
    }
    return render(request,'claims/Landingpage.html',context)



#def AgentList(request):
#    agent = AgentUser.objects.all()
#    context = {
#    'agents':agent
#    }
 #   return render(request,'claims/agentlist.html',context)

class AgentList(ListView):
    template_name = 'agentlist.html'
    queryset = AgentUser.objects.all()
    context_object_name = 'agents'



def Login(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username,password = password)
        if user is not None:
            login(request,user)
            return redirect('landingpage')
        else:
           return redirect('landingpage')


    return render(request,'login.html')



def CustomerSignUp(request):
    if request.method == "POST":
        first_name = request.POST['fname']
        last_name = request.POST['lname']
        username = request.POST['username']
        password = request.POST['pass1']
        repass = request.POST['pass2']
        pic = request.FILES['pic']
        email = request.POST['email']
        asi = User(first_name = first_name,last_name = last_name,username = username,password = password,socialauth = False,email = email,pic = pic)
        
        if(password != repass):
            return redirect('landingpage')
        asi.set_password(password)
        asi.save()

    return render(request,'signup.html')        




def AgentSignUp(request):
    if request.method == "POST":
        first_name = request.POST['fname']
        last_name = request.POST['lname']
        username = request.POST['username']
        password = request.POST['pass1']
        repass = request.POST['pass2']
        pic = request.FILES['pic']
        email = request.POST['email']
        asi = User(first_name = first_name,last_name = last_name,
            socialauth = False,username = username,password = password,is_agent = True,email = email,pic = pic)
        
        phone = request.POST["phone"]
        if(password != repass):
            redirect('landingpage')
        asi1 = AgentUser(user = asi,phone_number = phone)
        asi.set_password(password)
        asi.save()
        asi1.save()
        return redirect('landingpage')

    return render(request,'signup.html')        


def LeadDelete(request,pk):
    if request.method == "POST":
        print(pk)
        lead = LeadDetails.objects.get(id = pk)
        lead.delete()
        return redirect('claims:list')
    
    return render(request,'claims/delete.html')

def Logout(request):
    logout(request)
    return redirect('landingpage')


def LeadCreate(request):
    loginuser= request.user

    agent = AgentUser.objects.all()
    context = {
    'user':loginuser,
    'agents':agent
    }
    if request.method == "POST":
        first_name = request.POST['first-name']
        last_name = request.POST['last-name']
        age = request.POST['age']
        email = request.POST['email']
        phone_number = request.POST['phone']
        address = request.POST['address']
        occupation = request.POST['occ']
        auser = request.POST['agent']
        user = User.objects.filter(username = auser).first()
        luser = User.objects.filter(username = loginuser.username).first()
        agent = AgentUser.objects.filter(user = user).first()
        image = request.FILES['upload']
        describtion = request.POST['desc']
        
        typ = request.POST['type']
        if typ == 'Vechile':
            obj = LeadDetails(user=luser,first_name = first_name,last_name = last_name,age = age,email = email,
            address = address,phone = phone_number,occupation = occupation,agent = agent,image = image,describtion = describtion)
            obj.save()
            return redirect('claims:vechile',obj.id)
        else:
            obj = LeadDetails(user=luser,first_name = first_name,last_name = last_name,age = age,email = email,
            address = address,phone = phone_number,occupation = occupation,agent = agent,is_v = False,image = image,describtion = describtion)
            obj.save()
            return redirect('claims:object',obj.id)

    return render(request,"create.html",context)

def Vechile(request,pk):
    if request.method == 'POST':
        lead = LeadDetails.objects.filter(id = pk).first()
        license = request.POST['license']
        licencepic = request.FILES['lpic']
        Rigestration_Number = request.POST['rc']
        Rcpic = request.FILES['rcpic']
        licenseuser = request.POST['luser']
        phone = request.POST['phone']
        vo = VechileDetails(lead = lead,license = license,licencepic = licencepic,Rigestration_Number = Rigestration_Number
            ,Rcpic = Rcpic,licenseuser = licenseuser,phone = phone)
        vo.save()
        return redirect('claims:list')
    return render(request,'claims/vechile.html')

def Objectd(request,pk):
    if request.method == 'POST':
        lead = LeadDetails.objects.filter(id = pk).first()
        item_name = request.POST['item']
        UID = request.POST['uid']
        pdate = request.POST['date']
        ob = ObjectDetails(lead = lead,item_name = item_name,UID = UID,Pdate = pdate)
        ob.save()
        return redirect('claims:list')
    return render(request,'claims/object.html')

def Leadproperties(request,pk):
    data = LeadDetails.objects.filter(id = pk).first()
    user = request.user
    if user.is_agent:

        auser = User.objects.filter(username = user).first()
        agent = AgentUser.objects.filter(user = auser).first()

    if data.is_v:
        vech = VechileDetails.objects.filter(lead = data).first()
        context = {
        'data':data,
        'vech':vech,
        'user':user,
        'pk':pk
        }
    else:
        obje = ObjectDetails.objects.filter(lead = data).first()
        context = {
        'data':data,
        'obj':obje,
        'user':user,
        'pk':pk
        }
    if request.method == "POST":
        message = 'Further details contact the agent. \n'+'Agent Name:'+ agent.user.username   + '\n Mail:' + agent.user.email  

        
        send_mail(
            "Your claim has been selected by agent" + data.agent.user.username,
            message,
            'khajababa.md2002@gmail.com',
            [data.email]

            )
        data.is_selected = True
        agent.is_available = False
        agent.save()
        data.save()
        return redirect('claims:agentleads')

    return render(request,"Details.html",context)

def Agentdetail(request,user):

    auser = User.objects.filter(username = user).first()
    details = AgentUser.objects.filter(user = auser).first()
    context = {
    'details':details
    }
    return render(request,'claims/adetails.html',context)


def Accountdetails(request):
    user = request.user
    
    auser = User.objects.filter(username = user).first()
    if auser.is_agent:
        agent = AgentUser.objects.filter(user = auser).first()
        context = {
        'agent':agent,
        'user':user
        }
    else:
        context={
        'auser':auser,
        }
    if request.method == "POST":
        value = request.POST['avai']
        agent = AgentUser.objects.filter(user = auser).first()
        if value == 'A':
            agent.is_available = True
            agent.save()
        else:
            agent.is_available = False
            agent.save()

        return redirect('claims:agentleads')
    return render(request,'accountdetails.html',context)


def ContactUs(request):
    if request.method == "POST":
        message = request.POST['message']
        email = request.POST['email']
        fd = FeedBack(message = message,email = email)
        fd.save()
        return redirect('landingpage')


    return render(request,'Contact.html')


def UpdateLead(request,pk):
   
    if request.method == "POST":
        first_name = request.POST['fname']
        last_name = request.POST['lname']
        age = request.POST['age']
        email = request.POST['email']
        phone_number = request.POST['phone']
        address = request.POST['address']
        occupation = request.POST['occ']
        auser = request.POST['agent']
        user = User.objects.filter(username = auser).first()
        luser = User.objects.filter(username = loginuser.username).first()
        agent = AgentUser.objects.filter(user = user).first()
        image = request.FILES['upload']
        describtion = request.POST['desc']
        obj = LeadDetails(user=luser,first_name = first_name,last_name = last_name,age = age,email = email,
            address = address,phone = phone_number,occupation = occupation,agent = agent,image = image,describtion = describtion)
        obj.update()
        
        
        if obj.is_v:
            lead = obj
            license = request.POST['license']
            licencepic = request.FILES['lpic']
            Rigestration_Number = request.POST['rc']
            Rcpic = request.FILES['rcpic']
            licenseuser = request.POST['luser']
            phone = request.POST['phone']
            vo = VechileDetails(lead = lead,license = license,licencepic = licencepic,Rigestration_Number = Rigestration_Number
                ,Rcpic = Rcpic,licenseuser = licenseuser,phone = phone)
            vo.update()
            return redirect('claims:list')
        else:
            lead = LeadDetails.objects.filter(id = pk).first()
            item_name = request.POST['item']
            UID = request.POST['uid']
            pdate = request.POST['date']
            ob = ObjectDetails(lead = lead,item_name = item_name,UID = UID,Pdate = pdate)
            ob.update()
        
            return redirect('claims:list') 

    data = LeadDetails.objects.filter(id = pk).first()
    agent = AgentUser.objects.all()       
    if data.is_v:
        vdta = VechileDetails.objects.filter(lead = data).first()
        context = {
        'data':data,
        'vdta':vdta,
        'agent':agent
        }
    else:
        edta = ObjectDetails.objects.filter(lead = data).first()
        context = {
        'data':data,
        'edta':edta,
        'agent':agent
        }


    return render(request,'claims/update.html',context)

def AboutUs(request):
    return render(request,'About.html')