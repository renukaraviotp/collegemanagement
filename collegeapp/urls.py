from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
   
   path('',views.home,name='home'),
   path('teacherhome',views.teacherhome,name='teacherhome'),
   path('adminhome',views.adminhome,name='adminhome'),
   path('loginn',views.loginn,name='loginn'),
   path('signup',views.signup,name='signup'),
   path('signupaction',views.signupaction,name='signupaction'),
   path('logoutt',views.logoutt,name='logoutt'),
   path('add',views.add,name='add'),
   path('add_course',views.add_course,name='add_course'),
   path('show_teacher',views.show_teacher,name='show_teacher'),
   path('student',views.student,name='student'),
   path('addstudent',views.addstudent,name='addstudent'),
   path('show_student',views.show_student,name='show_student'),
   path('seeprofile',views.seeprofile,name='seeprofile'),
   path('edit',views.edit,name='edit'),
   path('delete/<int:pk>',views.delete,name='delete'),
   path('update',views.update,name='update'),
   path('deletestud/<int:pk>',views.deletestud,name='deletestud'),
   path('upd/<int:pk>',views.upd,name='upd'),
   path('edt/<int:pk>',views.edt,name='edt')
  


]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)