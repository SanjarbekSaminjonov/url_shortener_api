import uuid
from django.shortcuts import redirect
from api.models import Url

# Create your views here.


def get_url(request, uuid1):
    print(uuid1)
    return redirect('get_link', uuid=uuid1)
