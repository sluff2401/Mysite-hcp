from django.shortcuts               import render, get_object_or_404, redirect
#from django.utils                   import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models     import User
from users.models                   import Person
from .models                        import ClubSettings
from .forms                         import UpdateAdvertForm, InsertAdvertForm
from mysite.settings                import IS_CLUB


# functions which do not update the database
'''
@login_required
def siteadmin_detail(request):
  activeuser                              =  User.objects.get(id=request.user.id)
  activeperson                            =  Person.objects.get(username=activeuser.username)
  return render(request, 'mysite/siteadmin_detail.html', { 'activeperson': activeperson, 'IS_CLUB': IS_CLUB})
'''

@login_required
def advert_display(request):
  activeuser                              =  User.objects.get(id=request.user.id)
  activeperson                            =  Person.objects.get(username=activeuser.username)
  return render(request, 'mysite/advert_display.html', { 'activeperson': activeperson, 'IS_CLUB': IS_CLUB})

# functions which update the database in two stages,  using forms
# but don't require a pk as they don't refer to an existing record
@login_required
def advert_insert(request):
  activeuser                            =  User.objects.get(id=request.user.id)    # get details of activeuser
  activeperson                          =  Person.objects.get(username=activeuser.username)
  if activeperson.status                >= 60:
    can_insert                          = True
  else:
    can_insert                          = False
  if request.method                     != "POST": # i.e. method == "GET":
    if can_insert:
      form = InsertAdvertForm()                                               # get a blank InsertPersonForm
      return render(request, 'mysite/advert_new.html', {'form': form})
    else:
      return redirect('events.views.event_list')
  else:                                 # i.e method == 'POST'
    form                                = InsertAdvertForm(request.POST)                     # get a InsertPersonForm filled with details of new user
    if form.is_valid()\
    and activeperson.status             >= 60:
      advert                                = form.save(commit=False)                 # extract details from user for
      advert.save()
      return redirect('events.views.event_list')
    else:
      return render(request, 'users/insert_update.html', {'form': form})

# functions which update the database in two stages,  using forms
# and do require a pk as they refer to a user who is not, generally, the activeuser
@login_required
def siteadmin_detail(request):
  activeuser                            =  User.objects.get(id=request.user.id)    # get details of activeuser
  activeperson                          =  Person.objects.get(username=activeuser.username)
  clubsettings                          =  get_object_or_404(ClubSettings)     # get details of person to be updated/displayed/deleted

  if request.method                     != "POST": # i.e. method == "GET":
    form = UpdateAdvertForm(instance=clubsettings)                                # get a UpdatePersonForm filled with details of Profile to be upd
    return render(request, 'mysite/siteadmin_detail.html', {'form': form, 'clubsettings': clubsettings})                # ask activeuser for details of new/updated user
  else:                                 # i.e method == 'POST'
    form                                = UpdateAdvertForm(request.POST, instance=clubsettings)
    if form.is_valid()\
    and activeperson.status             >= 60:
      clubsettings                            = form.save(commit=False)                 # extract details from user form
      clubsettings.save()                                                                   # update user record with extra details
      return redirect('users.views.member_list')
    else:                                                                        # i.e. form is not valid, ask activeuser to resubmit it
      return render(request, 'mysite/siteadmin_detail.html', {'form': form, 'clubsettings': clubsettings})




