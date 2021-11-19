from django.http.response import HttpResponse
from django.shortcuts import redirect

# Create your views here.
def home(request):
    return HttpResponse('''<h1 style="color:green">Working . . .</h2>''')


def get_url(request, uuid1):
    print(uuid1)
    return redirect('get_link', uuid=uuid1)
