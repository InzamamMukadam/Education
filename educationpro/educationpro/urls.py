"""
URL configuration for educationpro project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from educationapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/',views.AboutTemplate.as_view(),name='about'),
    path('contact/',views.ContactTemplate.as_view(),name='contact'),
    path('index/',views.IndexTemplate.as_view(),name='index'),
    path('instructor/',views.InstructorTemplate.as_view(),name='instructor'),
    path('course/',views.CourseListView.as_view(),name='course'),
    path('blog/',views.BlogTemplate.as_view(),name='blog'),
    # path('student/',views.StudentTemplate.as_view()),
    # path('course-inner/',views.InnerTemplate.as_view(),name='course-inner'),
    path('course/addcart/<int:id>',views.addCartForm,name='addcart'),
    path('success/',views.SuccessTemplate.as_view(),name='success'),
    path('coursecreate/',views.CourseCreateView.as_view(),name='coursecreate'),
    # path('innercreate/',views.InnerCreateView.as_view(),name='innercreate'),
    path('courselist/edit/<int:pk>',views.EditCourse.as_view(),name='edit'),
    path('courselist/edit/update',views.updateCourse),
    path('courselist/delete/<int:id>',views.deleteCourse),
    path('thanks/',views.CompleteTemplate.as_view(),name='thanks'),
    path('custcreate/',views.CustomerCreateView.as_view(),name='custcreate'),
    path('custlist/',views.CustomerListView.as_view(),name='custlist'),
    path('custlist/edit/<str:pk>',views.Update.as_view(),name='edit'),
    path('custlist/delete/<str:pk>',views.Delete.as_view(),name='delete'),
    path('course/addcart/<int:id>',views.addCartForm,name='addcart'),
    # path('addcart/',views.addCartForm,name='addcart'),
    path('cartlist/placeorder',views.showOrderForm,name='placeorder'),
    path('login/',views.Login,name='login'),
    # path('sregistration/',views.StudentRegistrationTemplate.as_view(),name='sregistration'),
    path('ilogin/',views.Login,name='ilogin'),
    path('paymentsucess/<str:tid>/<str:orderid>/',views.paymentsucess,name="paymentsucess"),
    path('logout/',views.logout,name='logout'),
    path('cartlist/',views.showCart,name='cartlist'),
    path('cartlist/delete/<int:cid>/',views.DeleteCart.as_view(),name='delete'),




] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


