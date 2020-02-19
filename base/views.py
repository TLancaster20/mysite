from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# error_404 and error_500 set up error custom error pages
#def error_404(request, exception):
#	data={}
#	return render(request, '404.html', data)

#def error_500(request):
#	return render(request, '500.html')


def index(request):
    return render(request, 'index.html')
