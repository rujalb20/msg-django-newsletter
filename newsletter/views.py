from django.shortcuts import render
# Create your views here.
from django.http import HttpResponseRedirect
from .forms import EmailCaptureForm
from newsletter.models import Subscriber
from django.contrib import messages
from django.shortcuts import get_object_or_404
import secrets
def subscribe(request):
    if request.method == "POST":
        form = EmailCaptureForm(request.POST)
        if form.is_valid():
            some_queryset = Subscriber.objects.filter(email=form.cleaned_data["email"])
            if some_queryset.exists():
                messages.info(request,"Already subscribed")
                return HttpResponseRedirect("/subscribe/")

            else:
                s=Subscriber(email=form.cleaned_data["email"],token = secrets.token_urlsafe(16), is_active = True)
                s.save()
                messages.success(request, "Successfully subscribed")
            return render(request,"newsletter/subscribe.html", {
                "form":form,
                "subscriber":s
            })
    else:
        form = EmailCaptureForm()
    return render(request, "newsletter/subscribe.html", {"form": form})
def unsubscribe(request,token):
    obj= get_object_or_404(Subscriber, token=token)
    obj.is_active = False 
    obj.save()
    messages.success(request, "You have successfully unsubscribed from our newsletter")
    return render(request, "newsletter/unsubscribe.html")
