from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf


def login(request):
  print(request.GET)
  c = {'hide_login_btn': True}
  c.update({'next': request.GET.get('next', '/')})
  if 'error' in request.GET:
    c.update({'error': True})
  c.update(csrf(request))
  print(c)
  return render_to_response('login.html', c)


def auth_view(request):
  username = request.POST.get('username', '')
  password = request.POST.get('password', '')
  user = auth.authenticate(username=username, password=password)

  if user is not None:
    auth.login(request, user)
    print("Valid User")
    return HttpResponseRedirect(request.POST.get('next', '/')) 
  else:
    return HttpResponseRedirect('/accounts/login/?error=')


#def loggedin(request):
#  return render_to_response('loggedin.html',
#                            {'full_name': request.user.username})

#def invalid_login(request):
#  return render_to_response('invalid_login.html')


def logout(request):
  auth.logout(request)
  return HttpResponseRedirect(request.GET.get('next', '/')) 

