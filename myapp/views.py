from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from myapp.models import AuthSignUpCompany, AuthSignUpStudent, Contact_Us
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

# Create your views here.

def index(r):
    return render(r,'index.html')

def serv(r):
    return render(r,'services.html')

def career(r):
    return render(r,'career.html')

def all_type(r):
    return render(r,'all_type.html')

def comp_it(r):
    return render(r,'comp_it.html')

def digit_mrkt(r):
    return render(r,'digit_mrkt.html')

def desigin(r):
    return render(r,'desigin.html')

def accessories(r):
    return render(r,'accessories.html')

def about_us(r):
    return render(r,'about_us.html')

def about_us(r):
    return render(r,'about_us.html')

def srch_rslt(r):
    return render(r,'srch_rslt.html')

def privacy_policy(r):
    return render(r,'privacy_policy.html')

def services(r):
    return render(r,'services.html')

def reg(r):
    return render(r,'registration.html')

def cont_us(r):
    # print("Data=",r.POST)
    all_data = Contact_Us.objects.all().order_by("id")
    # print(data)
    if 'Submit' in r.POST:
        # return HttpResponse("Data=",r.POST)
        name = r.POST["name"]
        con = r.POST["Contact"]
        sub = r.POST["subject"]
    # return HttpResponse("<h1>"+name+con+sub+"</h1>")
        data = Contact_Us(name=name, contact_number=con, subject=sub)
        data.save()
        res = "Dear {} Thanks for your feedback".format(name)
        return render(r, "contact_us.html", {"status": res, "messages": all_data})
        # return render(r,"contact_us.html".{"status":res})
        return HttpResponse("<h1>Dear {} Data save successfully!</h1>".format(name))
    return render(r, 'contact_us.html', {"messages": all_data})
    return render(r,'contact_us.html')

def login(r):
    if 'signin' in r.POST:
        email = r.POST['email']
        password = r.POST['password']
        user = authenticate(username=email , password=password)
        if(user):
            login(r,user)
            resp=HttpResponseRedirect('index')
            resp.set_cookies('user_id',user.id)
            resp.set_cookies('user_email',user.email)
            messages.add_message(r,messages.INFO,'login successfully')
        else: 
            messages.add_message(r,messages.INFO,'login unsuccessfully')
    return render(r,'login.html')

def reg_company(r):
    if 'signup' in r.POST:
        fN = r.POST['first_name']
        lN = r.POST['last_name']
        ph = r.POST['phone']
        em = r.POST['email']
        ps = r.POST['password']
        add = r.POST['address']
        ct = r.POST['city']
        st = r.POST['state']
        zi = r.POST['zipcode']
        userdata = User.objects.create_user(em,em,ps)
        userdata.first_name = fN
        userdata.last_name =  lN
        data = AuthSignUpCompany(user = userdata , first_name = fN , last_name = lN ,  phone=ph , email = em , address = add , city = ct , state = st , zipcode = zi)
        data.save()
        messages.add_message(r,messages.INFO,'Auth Registration done successfully')
    return render(r,'registration_company.html') 
    # return HttpResponseRedirect('index.html') 

def reg_student(r):
    if 'signup' in r.POST:
        fN = r.POST['first_name']
        lN = r.POST['last_name']
        ph = r.POST['phone']
        em = r.POST['email']
        ps = r.POST['password']
        userdata = User.objects.create_user(em,em,ps)
        userdata.first_name = fN
        userdata.last_name =  lN
        data = AuthSignUpStudent(user = userdata , first_name = fN , last_name = lN ,  phone=ph , email = em)
        data.save()
        messages.add_message(r,messages.INFO,'Auth Registration done successfully')
    # return render(r,'registration_student.html') 
    return render(r,'registration_student.html') 

def reset_password(r):
    uname = r.user.username
    message = {}
    if r.method == 'POST':
        email = r.POST['email']
        new_password = r.POST['new_password']
        retype_new_password = r.POST['re_new_password']
        user = authenticate(username=uname, password=email)
        if user is not None:
            if new_password == retype_new_password and new_password != '':
                u = user.objects.get(username=uname)
                u.set_password(new_password)
                u.save()
                message = 'Successfully Changed the Password.'
            else:
                message = 'Invalid Passwords!'
        else:
            message = 'Invalid Password!'

    return render(r,'reset_password.html')
    # return HttpResponseRedirect(r,'index.html')
    return HttpResponse(json.dumps(message), content_type='application/json')
