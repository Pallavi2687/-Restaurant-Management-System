from django.shortcuts import render , redirect
from django.http import HttpResponse
from myapp.models import BookTable, AboutUs, Feedback, ItemList, Items
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def HomeView(request):
    items =  Items.objects.all()
    list = ItemList.objects.all()
    review = Feedback.objects.all()
    return render(request, 'home.html',{'items': items, 'list': list, 'review': review})


def AboutView(request):
    data = AboutUs.objects.all()
    return render(request, 'about.html',{'data': data})


def MenuView(request):
    items =  Items.objects.all()
    list = ItemList.objects.all()
    return render(request, 'menu.html', {'items': items, 'list': list})


def BookTableView(request):
    if request.method=='POST':
        name = request.POST.get('user_name')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('user_email')
        total_person = request.POST.get('total_person')
        booking_data = request.POST.get('booking_data')

        if name != '' and len(phone_number) == 10 and email != '' and total_person != 0 and booking_data != '':
            data = BookTable(Name=name, Phone_number=phone_number,
                             Email=email,Total_person=total_person,
                             Booking_date=booking_data)
            data.save()
    return render(request, 'book_table.html')



def FeedbackView(request):
    return render(request, 'feedback.html')
def login_page(request):
     if request.method == "POST":
          username = request.POST.get('username')
          password = request.POST.get('password')

          if not User.objects.filter(username = username).exists():
             messages.info(request , ' Invalid Username')
             return redirect('/login/')
          
          user = authenticate(username = username , password = password)

          if user is None:
             messages.info(request , ' Invalid Password')
             return redirect('/login/')
     
          else:
            login(request ,user)
            return redirect('/receipes/')

     return render(request , 'login.html')
def logout_page(request):
     logout(request)
     return redirect('/login/')


def register(request):
     if request.method == "POST":
          first_name = request.POST.get('first_name')
          last_name = request.POST.get('last_name')
          username = request.POST.get('username')
          password = request.POST.get('password')

          user = User.objects.filter(username = username)

          if user.exists():
               messages.info(request , 'Username already exist')
               return redirect('/register/')

          user = User.objects.create(
             first_name  = first_name ,
             last_name =    last_name ,
             username = username 
          )
          user.set_password(password)
          user.save()
          messages.info(request , 'Account created successfully')
          return redirect('/register/')



     return render(request , 'register.html')