from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from educationapp.models import Course,Customer,CartModel,Orders,Payment
from django.shortcuts import render,redirect
from django.http import HttpResponse
from datetime import date
from django.conf import settings
from django.core.mail import send_mail



class SuccessTemplate(TemplateView):
    template_name='educationapp/sucess.html'

class AboutTemplate(TemplateView):
    template_name='educationapp/about.html'

class ContactTemplate(TemplateView):
    template_name='educationapp/contact.html'

class IndexTemplate(TemplateView):
    template_name='educationapp/index.html'

class InstructorTemplate(TemplateView):
    template_name='educationapp/instructorlogin.html'

# class InnerTemplate(TemplateView):
#     template_name='educationapp/course-inner.html'

class BlogTemplate(TemplateView):
    template_name='educationapp/blog.html'

# class StudentRegistrationTemplate(TemplateView):
#     template_name='educationapp/studentregistration.html'



class CourseCreateView(CreateView):
    model=Course
    fields=['name','price','studentsenrolled','updatedon','course_image']
    success_url='/success/'

class CourseListView(ListView):
    model=Course
    context_object_name='courses'
    template_name='educationapp/course.html/'

class EditCourse(DetailView):
    model=Course
    context_object_name='courses'
    template_name='educationapp/updatecourse.html'

def updateCourse(request):
    if request.method=='POST':
        cid=request.POST['id']
        cname=request.POST['name']
        cprice=request.POST['price']
        enrolled=request.POST['studentsenrolled']
        updated=request.POST['updatedon']
        cs=Course.objects.filter(id=cid)
        cs.update(id=cid,name=cname,price=cprice,studentsenrolled=enrolled,updatedon=updated)
        return redirect("/courselist/")
    else:
        return render(request,'updatecourse.html')


def deleteCourse(request,id):
    data=Course.objects.get(id=id)
    data.delete()
    return redirect("/courselist/")

class CompleteTemplate(TemplateView):
    template_name='educationapp/complete.html'

class CustomerCreateView(CreateView):
    model=Customer
    fields=['fname','lname','emailId','password']
    success_url='/login/'

class CustomerListView(ListView):
    model=Customer
    context_object_name='customers'
    template_name='educationapp/customerlist.html'

class Update(UpdateView):
    model=Customer
    fields=['fname','lname','emailId','password']
    success_url='/custlist/'

class Delete(DeleteView):
    model=Customer
    success_url='/custlist/'


class DeleteCart(DeleteView):
    model=CartModel
    success_url='/cartlist/'

def addCartForm(request,id):
    if request.method=='GET':
        data=Course.objects.get(id=id)
        return render(request,'educationapp/addtocart.html',{'course':data})
    else:
        course=Course.objects.get(id=id)
        email=request.POST['emailId']
        cust=Customer.objects.get(emailId=email)
        totalPrice=request.POST['totalPrice']
        # quan=request.POST['quantity']
        cart=CartModel.objects.create(cid=course,emailId=cust,totalPrice=totalPrice)
        cart.save()
        return redirect("/cartlist/")
        
def showCart(request):
    # email= "inzamammukadam@gmail.com"
    email = request.session.get('username')
    print("hello")
    data=CartModel.objects.filter(emailId=email)
    print(len(data))
    return render(request,'educationapp/cartlist.html',{'cart':data})

def showOrderForm(request):
    if request.method=='POST':
        # emailId="inzamammukadam@gmail.com"
        emailId = request.session['username']
        data=CartModel.objects.filter(emailId=emailId)
        totalbill=0
        for i in data:
            totalbill=totalbill+i.totalPrice
        name=request.POST['name']
        add=request.POST['address']
        city=request.POST['city']
        st=request.POST['state']
        pin=request.POST['pincode']
        pno=request.POST['phoneno']
        data=Orders.objects.create(emailId=emailId,name=name,address=add,city=city,state=st,pincode=pin,phoneno=pno)
        data.save()
        dateobj=date.today()
        dateobj=str(dateobj).replace('-','')
        datedata=str(data.orderId)+dateobj
        data.ordernumber=datedata
        data.save()
        data=Orders.objects.get(emailId=emailId,ordernumber=datedata)
        total=data.totalbillamount
        return render(request,'educationapp/paymentpage.html',{'order':data,'total':totalbill})
    else:
        return render(request,'educationapp/order.html')
    

def Login(request):
    if request.method=='POST':
        emailId=request.POST['email']
        # emailId="inzamammukadam@gmail.com"
        custobj=Customer.objects.get(emailId=emailId)
        password=request.POST['password']
        if password==custobj.password:
            request.session['username']=emailId
            # return HttpResponse("<h1>LOGGED IN</h1>")  
            return render(request,'educationapp/index.html')
        else:
            return HttpResponse("<h1>Wrong</h1>")  
    else:
        return render(request,'educationapp/studentlogin.html')
    


def logout(request):
    session_keys=list(request.session.keys())
    for key in session_keys:
        del request.session[key]
    return render(request,'educationapp/index.html')
    

def emailDemo(request):
    subject="Subject here."
    email_body="Here is the message."
    from_email=settings.EMAIL_HOST_USER
    fail_silently=False
    send_mail(subject=subject,message=email_body,from_email=from_email,recipient_list=['trendygayatri.95@gmail.com'])
    return HttpResponse("email Successful")

def paymentsucess(request,tid,orderid):
    emailId=request.session["username"]
    data1=Orders.objects.get(ordernumber=orderid)
    payment=Payment.objects.create(emailId=emailId,amount_paid=data1.totalbillamount,payment_id=tid,status='completed')
    payment.save()
    subject="Thank You For Your Order"
    email_body="email:"+emailId +"tid :"+tid +"id: "+orderid+"message: order get placed"

    from_mail=settings.EMAIL_HOST_USER

    send_mail(subject=subject, message=email_body, from_email=from_mail, recipient_list=['trendygayatri.95@gmail.com'])
    return HttpResponse("<h1>Payment Sucessful</h1>")

