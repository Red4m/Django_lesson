from home import views
from user_profile import views

from django.urls import path

urlpatterns = [
    path('<username>/', views.profile, name="profile"),
    path('<username>/edit/', views.edit_profile, name='edit_profile'),
    path('<username>/delete/', views.delete_profile, name='delete_profile')
]
