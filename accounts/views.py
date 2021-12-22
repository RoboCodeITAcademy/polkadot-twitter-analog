from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserEditForm, ProfileEditForm
from .models import Profile
# Create your views here.
def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            Profile.objects.create(user=user)

            return render(request, "app.html")
    else:
        form = UserRegisterForm()
    return render(request, "account/register.html", {"form":form})

@login_required(login_url="/account/login/")
def profile(request):
    u = request.user
    user = Profile.objects.get(user=u)
    if user:
        return render(request, "account/detail.html", {"user": user})
    else:
        return render(request, "account/detail.html")



def edit(request,user_id):
    if request.method == "POST":
        user_edit_form = UserEditForm(request.POST)
        profile_edit_form = ProfileEditForm(request.POST)
        if user_edit_form.is_valid():
            user_edit_form.save()
            return redirect("/account/profile/")
        if profile_edit_form.is_valid():
            profile_edit_form.save()
            return redirect("/account/profile/")
    else:
        user_edit_form = UserEditForm()
        profile_edit_form = ProfileEditForm()

    context = {
        "user_form":user_edit_form,
        "profile_form":profile_edit_form
    }
    return render(request, "account/edit.html", context)