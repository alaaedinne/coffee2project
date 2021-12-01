from django.shortcuts import redirect, render
from django.contrib import messages , auth
from django.contrib.auth.models import User
from .models import UserProfile
import re 

# Create your views here.

def signin(request):
    if request.method == 'POST' and 'btnsignup' in request.POST:
    
        name = None
        email = None
        phone = None
        address = None
        password = None
        username = None
        termes = None
        is_added = None
        # Get value from the forme :
        if 'name' in request.POST  :
            name = request.POST['name']
        else: messages.error(request,"error in name field")
        if 'email' in request.POST: 
            email = request.POST['email']
        else: messages.error(request , 'error in email field')
        if 'phone' in request.POST:
            phone = request.POST['phone']
        else: messages.error(request , 'error in phone number field')
        if 'address' in request.POST:
            address = request.POST['address']
        else: messages.error(request , 'error in address field')
        if 'username' in request.POST:
            username = request.POST['username']
        else: messages.error(request , 'error in username field')
        if 'pass' in request.POST:
            password = request.POST['pass']
        else: messages.error(request , 'error in password field')
        
        if 'termes' in request.POST:
            termes = request.POST['termes']

        ## Check the empty value :
        if name and email and phone and address and username and password :
            if termes == 'on':
                ## Check if username is taken :
                if User.objects.filter(username=username).exists():
                    messages.error(request , 'This username alredy exist')
                else:
                    ## Check if email is used :
                    if User.objects.filter(email=email).exists():
                        messages.error(request , 'This email is taken')
                    else:
                        patt = "^\w+([-+.']\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$"
                        if re.match(patt , email):
                            #Add user :
                            user = User.objects.create_user(first_name = name , last_name = name , email = email , username= username, password=password)
                            user.save()
                            ## Add more info in table: userprofile ::
                            userprofile = UserProfile(user=user , address =address , phone=phone)
                            userprofile.save()

                            #### Clear fields For new registration :
                            name = ''
                            email= ''
                            phone= ''
                            address = ''
                            username = ''
                            password = ''
                            termes = None
                            ### Success Message :
                            messages.success(request, 'Your account is created succefuly')
                            is_added = True
                            return redirect('signup')
                        else:
                            messages.error(request, 'Enter a valid email')
            else:
                messages.error(request , 'You must agree to the termes')
        else: 
            messages.error(request , "Check the empty fields")
        return render(request , 'account/signin.html' , {
            'name': name,
            'email':email,
            'phone':phone,
            'address':address,
            'username':username,
            'password':password,
            'is_added' : is_added
        })
    else:
        return render(request , 'account/signin.html')



def signup(request):
    if request.method == 'POST' and 'btnlogin' in request.POST:
        username = None
        password = None
        if 'user' in request.POST and 'pass' in request.POST:
            username = request.POST['user']
            password = request.POST['pass']
            user = auth.authenticate(username=username , password=password)
                ##Cheek if user exist :
            if user is not None:
                if 'rememberme' not in request.POST : 
                    request.session.set_expiry(0)
                auth.login(request,user)
            else : messages.error(request , 'username or password invalid')
        else: messages.error(request, 'Check empty field')
        return render(request , 'pages/index.html')
    else: return render(request , 'account/signup.html')

def logout(request):
    if request.method == 'POST' and 'btnlogout' in request.POST:
        if request.user.is_authenticated:
            auth.logout(request)
            return redirect('index')
    else:
        return render(request, 'account/logout.html') 