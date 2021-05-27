from django.urls import path,include
from. import views
from django.views.decorators.csrf import csrf_exempt
urlpatterns=[
    path('admin/advisor/',views.advisorgeneric.as_view(),name='advisor created'),
    path('user/<int:id>/advisor/',views.advisorview.as_view(),name=' show all advisors'),
    path('user/<int:id1>/advisor/<int:id>/',csrf_exempt(views.advisorbooking.as_view()),name='advisor booking time'),
    path('user/<int:id>/advisor/booking/',views.advisorbookingview.as_view(),name='showbooked advisors'),
]