from django.urls import path
from.import views

urlpatterns = [
    path('',views.index),
    path('dashboard/',views.dashboard),
    path('courses/',views.courses),
    path('addcourses/',views.addcourses),
    path('signup/',views.signup),
    path('sign_up/',views.sign_up),
    path('tables/',views.tables),
    path('viewstudents/',views.viewstudents),
    path('addstudent/',views.add_student),
    path('login/',views.login)
 


    
]
