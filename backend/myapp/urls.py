from django.urls import path
from .views import signup, login_user, logout_user, contact_form

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
      path('contact/', contact_form, name='contact_form_submission'),
]
