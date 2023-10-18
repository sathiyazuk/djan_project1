from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Datas


# Create your views here.


# def home(request):
#     msg="<h1>HIIIIIIIIIIIIIIIIIIIIIIIIIIII</h1>"
#     return HttpResponse(msg)

# def index(request):
#     msg1="<p>This is the index page</p>"
#     return HttpResponse(msg1)


# def user(request):


#    return render(request,"home.html",{'name':"vijay"})

# def user(request):


#    return render(request,"home.html")


# def product(request):
#     mobile=int(request.GET["mobile"])
#     keyboard=int(request.GET["keyboard"])
#     monitor=int(request.GET["monitor"])
#     price=mobile+keyboard+monitor
#     return render(request,"result.html",{'Price':price})


def home(request):

    mydata = Datas.objects.all()

    if (mydata != ''):
        return render(request, 'index.html', {'datas': mydata})
    else:
        return render(request, 'index.html')
    # if request.method=="POST":
    #    name=request.POST['name']
    #    age=request.POST['age']
    #    address=request.POST['address']
    #    contact=request.POST['contact']
    #    mail=request.POST['mail']

    #    obj=Datas()
    #    obj.Name=name
    #    obj.Age=age
    #    obj.Address=address
    #    obj.Contact=contact
    #    obj.Mail=mail
    #    obj.save()
    #    mydata=Datas.objects.all()
    #    return render(request,"home.html",{'datas':mydata})

    return render(request, "index.html")


def adddata(request):
    if request.method == "POST":
        name = request.POST['name']
        age = request.POST['age']
        address = request.POST['address']
        contact = request.POST['contact']
        mail = request.POST['mail']

        obj = Datas()
        obj.Name = name
        obj.Age = age
        obj.Address = address
        obj.Contact = contact
        obj.Mail = mail
        obj.save()
        mydata = Datas.objects.all()
        return redirect("home")
    return render(request, "index.html")


def updatedata(request, id):
    mydata = Datas.objects.get(id=id)
    if request.method == "POST":
        name = request.POST['name']
        age = request.POST['age']
        address = request.POST['address']
        contact = request.POST['contact']
        mail = request.POST['mail']

        mydata.Name = name
        mydata.Age = age
        mydata.Address = address
        mydata.Contact = contact
        mydata.Mail = mail
        mydata.save()

        return redirect('home')

    return render(request, 'update/index.html', {'data': mydata})


def deletedata(request, id):
    mydata = Datas.objects.get(id=id)
    mydata.delete()
    return redirect('home')


# def register(request):
#    name=request.POST["name"]
#    password=request.POST["password"]
#    address=request.POST["address"]
#    mail=request.POST["mail"]
#    return render(request,"result.html",{"name":name,'password':password,'address':address,'mail':mail})
