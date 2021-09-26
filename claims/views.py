from django.http.response import Http404
from django.shortcuts import render,redirect
from .models import LeadDetails,User,AgentUser,CustomerUser
from django.contrib.auth import login,logout,authenticate

def Leadlist(request):
    data = LeadDetails.objects.all()
    context = {
        'data':data
    }
    return render(request,'claims/list.html',context)
   

def LeadCreate(request):
	LeadDetails()
	if request.method == "POST":
		first_name = request.POST["first-name"]
		last_name = request.POST["last-name"]
		age = request.POST["age"]
		phone = request.POST["phone"]
		address = request.POST["address"]
		email = request.POST["email-address"]
		occupation = request.POST["occ"]
		images = request.FILES["upload"]

		describtion = request.POST["desc"]
		fd = LeadDetails(first_name = first_name,last_name = last_name,age = age,
		phone = phone,address = address,email = email,occupation = occupation,
		image = images,describtion = describtion)
		fd.save()
	
	return render(request, "claims/create.html")

def LandingPage(request):
    return render(request,'base.html',context = {
        'user':request.user
    })

def Login(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username,password = password)
        if user is not None:
            login(request,user)
            redirect('landingpage')
        else:
            redirect('landingpage')


    return render(request,'signup.html')

def AgentSignUp(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['pass1']
        repass = request.POST['pass2']
        asi = User(username = username,password = password,is_agent = True)
        
        email = request.POST['email']
        pic = request.FILES['pic']

        if(password != repass):
            redirect('landingpage')
        asi1 = AgentUser(user = asi,email = email,pic = pic)
        asi.set_password(password)
        asi.save()
        asi1.save()

    return render(request,'agentsn.html')        

def CustomerSignUp(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['pass1']
        repass = request.POST['pass2']

        asi = User(username = username,password = password,is_customer = True)

        
        email = request.POST['email']
        pic = request.FILES['pic']

        if(password != repass):
            redirect('landingpage')
        asi1 = CustomerUser(user = asi,email = email,pic = pic)
        asi.set_password(password)
        asi.save()
        asi1.save()

    return render(request,'agentsn.html')


def Logout(request):
    logout(request)
    return redirect('landingpage')