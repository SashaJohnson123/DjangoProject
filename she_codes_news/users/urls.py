from django.urls import path
from .views import CreateAccountView, UserProfileView

app_name = 'users'

urlpatterns = [
    path('create-account/', CreateAccountView.as_view(), name='createAccount'),
    path('user-profile/'), UserProfileViewView.as_view(), name= 'UserProfile'),
]
