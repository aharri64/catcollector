from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# import models
from .models import Cat

# access the feeding form
from .forms import FeedingForm, CatForm

# import Django form classes
# these handle CRUD for us


# class CatCreate(CreateView):
#     model = Cat
#     # fields = '__all__'
#     success_url = '/cats'


class CatUpdate(UpdateView):
    model = Cat
    fields = ['name', 'breed', 'description', 'age']

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        return HttpResponseRedirect('/cats/' + str(self.object.pk))


class CatDelete(DeleteView):
    model = Cat
    success_url = '/cats'


# Create your views here.
def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


# CATS
def cats_index(request):
    cats = Cat.objects.all(t)
    return render(request, 'cats/index.html', {'cats': cats})


def cats_show(request, cat_id):
    # we get access to that cat_id variable
    # query for the specific cat clicked
    cat = Cat.objects.get(id=cat_id)
    # lets make a feeding_form
    feeding_form = FeedingForm()
    return render(request, 'cats/show.html', {
        'cat': cat,
        'feeding_form': feeding_form
    })


def cats_new(request):
    # create new instance of cat form filled with submitted values or nothing
    cat_form = CatForm(request.POST or None)
    # if the form was posted and valid
    if request.POST and cat_form.is_valid():
        new_cat = cat_form.save(commit=False)
        new_cat.user = request.user
        new_cat.save()
        # redirect to index
        return redirect('index')
    else:
        # render the page with the new cat form
        return render(request, 'cats/new.html', {'cat_form': cat_form})
# FEEDING


def add_feeding(request, pk):
    form = FeedingForm(request.POST)
    # validate form.is_valid built in
    if form.is_valid():
        new_feeing = form.save(commit=False)
        # don't save yet!!! First let's add our cat_id
        new_feeing.cat_id = pk
        # the cat has been added we can now save
        new_feeing.save()
    return redirect('cats_show', cat_id=pk)


def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)

# Instrcutions
# 1. Update index view function to look similar to the contact view function
# 2. Add a index.html page with the current HTML that is displayed
# 3. Update about view function to look similar to the contact view function
# 4. Add a about.html page with the current HTML that is displayed
# 5. Update your urls.py file (main_app) to look similar to the contact path

# 1. Make a view function
# 2. Make the html page
# 3. Add the view to the urls.py inside of main_app.urls

# In browser
# When I go to localhost:8000/contact
# Django -> urls -> /contact -> vews.contact (runs function) -> templates -> contact.html
