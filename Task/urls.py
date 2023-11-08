
from django.contrib import admin
from django.urls import path, include
from django.urls import path
from accounts import views
from django.contrib.auth.views import (
    LoginView, LogoutView,
    PasswordChangeView, PasswordChangeDoneView,
    PasswordResetView,PasswordResetDoneView, PasswordResetConfirmView,PasswordResetCompleteView,
)
from accounts.views import MySignUpView
app_name = 'accounts'


urlpatterns = [
    path('home/', views.home, name='home' ),
    path('admin/', admin.site.urls),
    path('sign_up/', MySignUpView.as_view(), name='sign_up'),
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('password_change/', PasswordChangeView.as_view( success_url='accounts/password_change/done/'), name="password_change"),
    path('password_change/accounts/password_change/done/', PasswordChangeDoneView.as_view(), name="password_change_done"),
    path('password_reset/', PasswordResetView.as_view(success_url='done/'), name="password_reset"),
    path('password_reset/done/', PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view( success_url='/accounts/reset/done/'), name="password_reset_confirm"),
    path('reset/done/', PasswordResetCompleteView.as_view(), name="password_reset_complete"),
    path('profile/', views.profile, name='profile'),
    path('blog/', views.blog, name='blog'),
    path('add_blog/', views.add_blog, name='add_blog'),
    path('delete_blog/', views.delete_blog, name='delete_blog'),
    path('delete/<title>', views.delete, name='delete'),
]
