from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    # path('profile/<int:id>',views.profile,name="profile"),
    path('registration/',views.registration,name='registration'),
    path('login/',views.userlogin,name="userlogin"),
    path('logout/',views.userlogout,name='userlogout')
]
