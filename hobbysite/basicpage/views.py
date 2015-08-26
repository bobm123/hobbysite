from django.shortcuts import render


def home_page(request):
    return render(request, 'home.html', {'nbar': 'home'})
    
def about_page(request):
    return render(request, 'about.html', {'nbar': 'about'})