from django.shortcuts import render
from users.models import Friend
from .models import Message
from django.views.generic import DetailView
from django.contrib.auth.models import User
from django.shortcuts import redirect

# Create your views here.
def allMsgs(request):
    # I need to get all of the friends of a user
    friends = Friend.get_friends(request.user)
    context = {
        "friends": friends,
    }
    return render(request, "messaging/msglist.html", context)

def friendMsgs(request, user_id):
    friend = User.objects.get(username=user_id)
    incoming = Message.objects.filter(sender=request.user, receiver=friend)
    outgoing = Message.objects.filter(sender=friend, receiver=request.user)
    # later we can check if a post request is made and actually add messages to the database

    # todo get a request when the user is typing to show the other user that their friend is active


    context = {
        "msgs": incoming.union(outgoing),
        "friend": friend,
    }
    return render(request, "messaging/textFeed.html", context)


def sendMsg(request, user_id):
    if request.method == "POST":
        friend = User.objects.get(username=user_id)
        msg = Message(sender=request.user, receiver=friend, content=request.POST["content"])
        msg.save()
    return redirect("text-feed", user_id=user_id)