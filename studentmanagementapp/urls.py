from django.urls import path

from studentmanagementapp import views

urlpatterns = [
    path('reg',views.reg_fun,name='reg'),
    path('regdata',views.regdata_fun),
    path('',views.log_fun,name='log'),
    path('logdata',views.logdata_fun,name='logdata'),
    path('home',views.home_fun,name='home'),
    path('add_students',views.addstudents_fun,name='add'),
    path('readdata',views.reddata_fun),
    path('display',views.display_fun,name='display'),
    path('update/<int:id>',views.update_fun,name='up'),
    path('delete/<int:id>',views.delete_fun,name='del'),
    path('log_out',views.log_out_fun,name='log_out')
]