from django.contrib import admin
from django.urls import path, include

from birthday_invitation.invitation.views import HomePageView, InvitationView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('invitation', InvitationView.as_view(), name='invitation'),
]