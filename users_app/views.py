from django.shortcuts import render, redirect
from .forms import CustomRegistartionForm
from django.contrib import messages
from buddytask.views import tasklist


# Create your views here.
def registration(request):
    if request.method == "POST":
        registration_form = CustomRegistartionForm(request.POST)
        if registration_form.is_valid():
            registration_form.save()
            messages.success(request,("success. Login to Proceed"))
            return redirect('registration')
        else:
            messages.error(request, "Form submission failed. Please correct errors.")
            return render(request, 'registration.html', {'registration_form': registration_form})
    else:
        registration_form = CustomRegistartionForm()
        return render(request, 'registration.html', {'registration_form':registration_form})