from home import views
from user_profile import views

from django.urls import path

urlpatterns = [
    path('<username>/', views.ProfileDetailView.as_view(), name="profile"),
    path('<username>/edit/', views.UserUpdateView.as_view(), name='edit_profile'),
    path('<username>/delete/', views.UserDeleteView.as_view(), name='delete_profile'),
    # path('login/', views.MyprojectLoginView.as_view(), name='login_page'),
    # path('register/', views.RegisterUserView.as_view(), name='register_page'),
    # path('logout/', views.MyProjectLogout.as_view(), name='logout_page'),

]
