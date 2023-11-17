from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from collegeapp.models import Teacher,Course,Student
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout
import os

# Create your views here.

def home(request):
    return render(request,'home.html')

@login_required(login_url='home') 
def teacherhome(request):
    return render(request,'teacherhome.html')

@login_required(login_url='home')
def adminhome(request):
    return render(request,'adminhome.html')

def signup(request):
    c = Course.objects.all()
    return render(request,'teacher.html',{'c':c})

def loginn(request):
    if request.method == 'POST':
        uname = request.POST['username']
        pas = request.POST['password']
        usr = auth.authenticate(username=uname,password=pas) 
        if usr is not None:
            if usr.is_superuser:
                login(request,usr)
                messages.info(request,f'Welcome Admin : {uname}')
                return redirect('adminhome')
            else:
                login(request,usr)
                messages.info(request,f'Welcome  {uname}')
                return redirect('teacherhome')

def signupaction(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        uname = request.POST['uname']
        pas = request.POST['pass']
        cpas = request.POST['cpass']
        email = request.POST['email']
        addrss = request.POST['address']
        age = request.POST['age']
        date = request.POST['date']
        gender = request.POST['gender']
        contact = request.POST['contact']
        photo = request.FILES['image']
        course = request.POST['course'] 

        if pas == cpas :
            if User.objects.filter(username = uname).exists():
                messages.info(request,'username exists')
                return redirect('signup')
            else:
                usr = User.objects.create_user(first_name = fname, last_name = lname, password = pas,email=email,username=uname)
                usr.save()
                b = Teacher(user=usr,course_id=course,address = addrss,age=age,contactnumber=contact,joindate=date,gender=gender,image=photo)
                b.save()
                return redirect('home')
        else:
            messages.info(request,'password doesnt match')
            return redirect('signup') 
        
@login_required(login_url='home')
def logoutt(request):
    logout(request)
    return redirect('home')

@login_required(login_url='home')
def add(request):
    if request.method == 'POST':
        name = request.POST['coursename']
        fee = request.POST['fee']
        c = Course(coursename=name,coursefee=fee)
        c.save()
        messages.info(request,f'{name} successfully added !') 
        return redirect('add_course') 
    
@login_required(login_url='home')    
def add_course(request):
    return render(request,'add_course.html')

@login_required(login_url='home')
def show_teacher(request):
    t = Teacher.objects.all()
    return render(request,'show_teacher.html',{'shw':t})

@login_required(login_url='home')
def student(request):
    s = Course.objects.all()
    return render(request,'student.html',{'cours':s})

@login_required(login_url='home')
def addstudent(request):
    if request.method == 'POST':
        name = request.POST['name']
        age = request.POST['age']
        email = request.POST['email']
        date = request.POST['date']
        qual = request.POST['qualification']
        gender = request.POST['gender']
        course = request.POST['course']
        ad = Student(name=name,age=age,email=email,joindate=date,qualification=qual,gender=gender,course_id=course)
        ad.save()
        messages.info(request,'successfully added')
        return redirect('student')

@login_required(login_url='home')   
def show_student(request):
    v = Student.objects.all()
    return render(request,'show_student.html',{'view':v})

@login_required(login_url='home')
def seeprofile(request):
    profile = Teacher.objects.get(user=request.user)
    # profile1 = Course.objects.get(user=request.user)
    img=profile.image
    nam = request.user.first_name
    nam2=request.user.last_name
    uname=request.user.username
    age = profile.age
    gen = profile.gender
    date = profile.joindate
    email = request.user.email
    qul = profile.contactnumber 
    
    cor = profile.course.coursename 
    add = profile.address
    context = {
        'name':nam,'age':age,'gender':gen,'date':date,'mail':email,'qual':qul,'address':add,'i':profile,'img':img,'nam2':nam2, 'uname':uname, 'cor':cor
    }
    return render(request,'seeprofile.html',context)

@login_required(login_url='home')
def edit(request):
    profile = Teacher.objects.get(user=request.user)
    pro1 = Course.objects.get(id=profile.course_id)
    nam = request.user.first_name
    lname = request.user.last_name
    username = request.user.username
    age = profile.age
    gen = profile.gender
    date = profile.joindate
    email = request.user.email
    qul = profile.contactnumber
    cor = pro1.coursename
    co = profile.course_id
    fee = pro1.coursefee
    add = profile.address
    course = Course.objects.all()
    photo = profile.image
    context = {
        'photo':photo,'fee':fee,'co':co ,'course':course, 'cor':cor ,'name':nam,'age':age,'gender':gen,'date':date,'mail':email,'qual':qul,'address':add,'lname':lname,'username':username
    }
    return render(request,'editprofile.html',context)


@login_required(login_url='home')
def  delete(request,pk):
    profile = User.objects.get(id=pk)
    teache = Teacher.objects.get(user_id=pk)
    profile.delete()
    teache.delete()
    return redirect('show_teacher') 

@login_required(login_url='home')
def update(request):
    if request.method == 'POST':
        usr = User.objects.get(id=request.user.id)
        tec = Teacher.objects.get(user_id=request.user.id)
        usr.first_name = request.POST['fname']
        usr.last_name = request.POST['lname']
        usr.username = request.POST['uname']
        usr.email = request.POST['email']
        tec.address = request.POST['address']
        tec.age = request.POST['age']
        tec.joindate = request.POST['date']
        tec.gender = request.POST['gender']
        tec.contactnumber = request.POST['contact']
        if len(request.FILES)!=0:
            if len(tec.image)>0: 
                os.remove(tec.image.path)
            else:
                tec.image = request.FILES['image']
            tec.image=request.FILES['image'] 
        tec.course_id = request.POST['cours']
        usr.save()
        tec.save()
        return redirect('seeprofile')

@login_required(login_url='home')   
def deletestud(request,pk):
    s=Student.objects.get(id=pk)
    s.delete()
    return redirect('show_student')

@login_required(login_url='home')
def upd(request,pk):
    if request.method == 'POST':
        u = Student.objects.get(id=pk)
        u.name = request.POST['name']
        u.age = request.POST['age']
        u.email = request.POST['email']
        u.joindate = request.POST['date']
        u.qualification = request.POST['qualification']
        u.gender = request.POST['gender']
        u.course_id = request.POST['course']
        u.save()
        messages.info(request,'successfully updated')
        return redirect('show_student')

@login_required(login_url='home')    
def edt(request,pk):
        s = Student.objects.get(id=pk)
        c = Course.objects.all()
        return render(request,'edit_stud.html',{'s':s,'c':c})