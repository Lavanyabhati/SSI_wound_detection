from django.urls import path
from .views import *
from Auth import views as authviews

urlpatterns = [
    path('otp/', authviews.otp, name='OTP'),
    path('update/', update_jr_doctor_details, name='update_jr_doctor_details'),
]
