from django.shortcuts import render




def index(request):
	return render(request, 'index.html')


#@login_required
#@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return HttpResponseRedirect('/')
        else:
            messages.error(request, _('Please correct the error below.'))
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'authent/profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })


def Logout(request):
    logout(request)
    return HttpResponseRedirect('/')
