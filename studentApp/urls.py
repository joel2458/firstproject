from.import views
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
  
    path('',views.homepage,name='homepage'),
    path('loginpage',views.loginpage,name='loginpage'),
    path('signuppage',views.signuppage,name='signuppage'),
    path('user_profile',views.user_profile,name='user_profile'),
    path('welcome',views.welcome,name='welcome'),
    path('show_profile',views.show_profile,name='show_profile'),
    path('load_edit_user_page',views.load_edit_user_page,name='load_edit_user_page'),
    path('edit_user_details',views.edit_user_details,name='edit_user_details'),
    


    path('admin_home',views.admin_home,name='admin_home'),
    path('load_add_course',views.load_add_course,name='load_add_course'),
    path('add_course',views.add_course,name='add_course'),
    path('student1',views.student1,name='student1'),
    path('add_student',views.add_student,name='add_student'),
    path('show_student_details',views.show_student_details,name='show_student_details'),
 

    path('user_signup',views.user_signup,name='user_signup'),
    path('user_login',views.user_login,name='user_login'),
    path('logout',views.logout,name='logout'),
    

    path('show_user_details',views.show_user_details,name='show_user_details')

]