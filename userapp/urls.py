from django.urls import path,include
from. import views
urlpatterns=[
    path('user/register/',views.userregview.as_view(),name='user created'),
    path('user/login/', views.userlogin.as_view(), name='user login'),
]