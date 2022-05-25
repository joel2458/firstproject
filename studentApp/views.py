from ast import Pass
from multiprocessing import context
import os
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from studentApp.models import course, student, user_Member
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def homepage(request):
    return render(request,'homepage.html')

def loginpage(request):
    return render(request,'loginpage.html')

def signuppage(request):
    return render(request,'signuppage.html')


def user_profile(request):
    if 'uid' in request.session:
        return render(request,'user_profile.html')
    return redirect('loginpage')
 
@login_required(login_url='loginpage')
def welcome(request):
    #if 'uid' in request.session:
    return render(request,'welcome.html')
    #return redirect('loginpage')


def admin_home(request):
    if not request.user.is_staff: 
        return redirect('loginpage')  
    return render(request,'admin_home.html')

def load_edit_user_page(request):
    return render(request,'edit_user_details.html')

@login_required(login_url='login')
def load_add_course(request):
    uid = User.objects.get(id=request.session["uid"])
    return render(request,'courses.html',{'uid':uid})

@login_required(login_url='login')
def student1(request):
    courses=course.objects.all()
    context={'courses':courses}
    return render(request,'student.html',context) 

      

    



def user_signup(request):
    if request.method == 'POST':
        fname=request.POST['fname']
        lname=request.POST['lname']
        uname=request.POST['uname']
        email=request.POST['email']
        cemail=request.POST['cemail']
        password=request.POST['password']
        cpass=request.POST['cpass']
        add=request.POST['add']
        gender=request.POST['gender']
        if request.FILES.get('file') is not None:
            image=request.FILES['file']
        else:
            image="/static/image/defaultimg.png"
        print("hii")
        if password == cpass:
            if email == cemail:
                if User.objects.filter(username=uname).exists():
                    messages.info(request,"Username is allready exist")
                    return redirect('signuppage')
                else:
                    user=User.objects.create_user(
                        first_name=fname,
                        last_name=lname,
                        username=uname,
                        email=email,
                        password=password
                    )
                    user.save()
                    
                    print("save")
                    u=User.objects.get(id=user.id)
                    member=user_Member(user_address=add,user_gender=gender,user_image=image,user=u)
                    member.save()
                    messages.info(request,"successfully Registered")
                    return redirect('loginpage')
            else:
                messages.info(request,"Email id not matching!!")
                return redirect('signuppage')
        else:
            messages.info(request,"password is not matching!!")
            return redirect('signuppage')
           
    else:
        return render(request,'signuppage.html')



def user_login(request): 
    try:
        if request.method == 'POST':
            try:
                username = request.POST['username']
                password = request.POST['password']
              
                user = auth.authenticate(username=username, password=password)
                request.session["uid"] = user.id
                if user is not None:
                    if user.is_staff:
                        auth.login(request,user)
                        return redirect('admin_home') 
                    else:                     
                        auth.login(request, user)
                        messages.info(request, f'Welcome {username}')
                        return redirect('welcome')
                else:
                    messages.info(request, "invalid details")
                    return redirect('loginpage')
            except:
                messages.info(request, "invalid details1")
                return render('loginpage.html')
        else:
            messages.info(request, "invalid details2")
            return render('loginpage.html')
    except:
        messages.info(request, 'Invalid username or password')
        return render(request, 'loginpage.html')


def show_profile(request):
    user=user_Member.objects.filter(user=request.user)
    context={'user':user}
    return render(request,'user_profile.html',context)

@login_required(login_url='login')
def edit_user_details(request):
    if request.method == 'POST':
        umember=user_Member.objects.get(user=request.user)
        umember.user.first_name = request.POST.get('fname')
        umember.user.last_name = request.POST.get('lname')
        umember.user.username = request.POST.get('uname')
        umember.user.email = request.POST.get('email')
        umember.user_address = request.POST.get('add')
        umember.user_gender = request.POST.get('gender')
        if request.FILES.get('file') is not None:
            if not umember.user_image == "/static/image/defaultimg.png":
                os.remove(umember.user_image.path)
                umember.user_image = request.FILES['file']
            else:
                umember.user_image = request.FILES['file']
        else:
            os.remove(umember.user_image.path)
            umember.user_image = "/static/image/defaultimg.png"
        umember.save()
        umember.user.save()
        return redirect('show_profile')
    umember=user_Member.objects.filter(user=request.user)
    context={'umember':umember} 
    return render(request,'edit_user_details',context)



@login_required(login_url='login')
def show_user_details(request):
    user=user_Member.objects.all()
    context={'user':user}
    return render(request,'show_user_details.html',context)

def logout(request):
    request.session["uid"] = ""
    auth.logout(request)
    return redirect('homepage')



@login_required(login_url='login')
def add_course(request):
    if request.method=='POST':
        cors=request.POST['course']
        cfee=request.POST['cfee']
        print(cors)
        crs=course()
        crs.course_name=cors
        crs.fee=cfee
        crs.save()
        print("hii")
        return redirect('admin_home')

@login_required(login_url='login')
def add_student(request):
    if request.method=='POST':
        # adno=request.POST['adno']
        sname=request.POST['sname']
        address=request.POST['address']
        age=request.POST['age']
        jdate=request.POST['jdate']
        sel1 = request.POST['sel']
        course1=course.objects.get(id=sel1)
        std=student(std_name=sname,
                    std_address=address,
                    std_age=age,
                    Join_date=jdate,
                    course=course1)
        std.save()
        print("hii")
        return redirect('admin_home')


@login_required(login_url='login')
def show_student_details(request):
    std=student.objects.all()
    return render(request,'show_students.html',{'std':std})









