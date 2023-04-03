# urls.py 
from django.urls import path
from . import views as messaging_views

urlpatterns = [
    path("", messaging_views.allMsgs, name="message-list"),
    path("<str:user_id>", messaging_views.friendMsgs, name="text-feed"),
    path("send/<str:user_id>", messaging_views.sendMsg, name="message-create")
]