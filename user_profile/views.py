from django.contrib.auth.models import User
from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, FormView

from home.models import Article
from user_profile.models import Profile

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout


@login_required
def profile(request, username):
    user = get_object_or_404(User, username=username)
    return render(
        request, "profiles.html", {"user": user},
    )


def edit_profile(request, username):
    print(request.POST)
    user = get_object_or_404(User, username=username)
    if request.method == 'POST':
        user.username = request.POST.get('username')
        profile, _ = Profile.objects.get_or_create(user=user)
        profile.phone = request.POST.get('phone')
        profile.country = request.POST.get('country')
        user.save()
        profile.save()
    return render(
        request, "edit_profile.html", {"user": user},
    )


def delete_profile(request, username):
    user = get_object_or_404(User, username=username)
    if request.method == 'POST':
        user.delete()
        return render(
            request, "success_delete.html", {"user": user},
        )
    return render(
        request, "delete_profile.html", {"user": user},
    )


@login_required
def sign_in_view(request):

    if request.user.is_authenticated:
        user = User.objects.all()
        return render(
            request, "sign_in_view.html", {"user": user},
        )
    else:
        return HttpResponse(f"You are not logged in", 404)


class RegisterFormView(FormView):
    form_class = UserCreationForm




