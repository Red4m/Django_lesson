from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView, CreateView, \
    DetailView, DeleteView, UpdateView, ListView

from home.models import Article
from user_profile.forms import AuthUserForm, \
    RegisterUserForm
from user_profile.models import Profile

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout, authenticate, login


# @login_required
# def profile(request, username):
#     user = get_object_or_404(User, username=username)
#     return render(
#         request, "profiles.html", {"user": user},
#     )


# class ProfileView(TemplateView):
#     template_name = "profiles.html"
#
#     def get_context_data(self, username, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['user'] = get_object_or_404(User, username=username)
#         return context

class ProfileListView(ListView):
    model = User
    template_name = "all_profiles.html"
    ordering = "username"
    context_object_name = "user"


class ProfileDetailView(DetailView):
    model = User
    template_name = "profiles.html"
    # url_kwarg = "username"
    slug_field = "username"
    slug_url_kwarg = "username"
    context_object_name = "user"

    def get_context_data(self, **kwargs):
        context = super(ProfileDetailView, self).get_context_data(**kwargs)
        # context['article'] = ['hell', 'my name is']
        # context['articles'] = Article.objects.filter(author=context['user'])
        context['articles'] = Article.objects.all()
        print(context)
        return context
#
#
# def edit_profile(request, username):
#     print(request.POST)
#     user = get_object_or_404(User, username=username)
#     if request.method == 'POST':
#         user.username = request.POST.get('username')
#         profile, _ = Profile.objects.get_or_create(user=user)
#         profile.phone = request.POST.get('phone')
#         profile.country = request.POST.get('country')
#         user.save()
#         profile.save()
#     return render(
#         request, "edit_profile.html", {"user": user},
#     )


class UserUpdateView(UpdateView):
    model = User
    slug_field = "username"
    slug_url_kwarg = "username"
    template_name = "edit_profile.html"
    success_url = "/articles/"
    context_object_name = "user"
    fields = ['username', 'first_name', 'last_name']




    # class EditProfileView(TemplateView):
    #     template_name = "edit_profile.html"
    #
    #     def get_context_data(self, username, **kwargs):
    #         context = super().get_context_data(**kwargs)
    #         context['user'] = get_object_or_404(User, username=username)
    #         return context


# def delete_profile(request, username):
#     user = get_object_or_404(User, username=username)
#     if request.method == 'POST':
#         user.delete()
#         return render(
#             request, "success_delete.html", {"user": user},
#         )
#     return render(
#         request, "delete_profile.html", {"user": user},
#     )


class UserDeleteView(DeleteView):
    model = User
    slug_field = "username"
    slug_url_kwarg = "username"
    template_name = "delete_profile.html"
    success_url = "success_delete.html"


class MyprojectLoginView(LoginView):
    template_name = 'login.html'
    form_class = AuthUserForm
    # success_url = reverse_lazy('edit_page')
    success_url = "profiles.html"

    # def get_success_url(self):
    #     return self.success_url


class RegisterUserView(CreateView):
    model = User
    template_name = 'registration.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('edit_page')
    success_msg = 'Пользователь успешно создан'

    def form_valid(self,form):
        form_valid = super().form_valid(form)
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password"]
        aut_user = authenticate(username=username,password=password)
        login(self.request, aut_user)
        return form_valid


class MyProjectLogout(LogoutView):
    next_page = reverse_lazy('edit_page')

# @login_required
# def sign_in_view(request):
#
#     if request.user.is_authenticated:
#         user = User.objects.all()
#         return render(
#             request, "sign_in_view.html", {"user": user},
#         )
#     else:
#         return HttpResponse(f"You are not logged in", 404)


# def register(request):
#     user = User.objects.all()
#     if request.method == "POST":
#         user.username = request.POST.get('username')
#         profile, _ = Profile.objects.get_or_create(user=user)
#         profile.phone = request.POST.get('phone')
#         profile.country = request.POST.get('country')
#         user.save()
#         profile.save()
#     else:
#         form = UserOurRegistration()
#     return render(request, 'registration.html', {'form': form})




