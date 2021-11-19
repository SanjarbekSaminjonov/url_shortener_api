from django.conf.urls import url
from django.shortcuts import redirect
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Url
from .serializers import UrlSerializer
from .isValidURL import isValidURL

# Create your views here.


def get_long_url(request, uuid="ooooo"):
    link_orign = Url.objects.filter(uuid=uuid).first()
    url = link_orign.get_link()
    return redirect(url)


@api_view(['POST'])
def create(request):
    myKey = 'link'

    newData = request.data
    print(newData)

    if myKey in newData.keys():
        newLink = newData[myKey]

        if not newLink.startswith("http"):
            newLink = 'http://' + newLink
        
        if isValidURL(newLink):        
            shortUrl = Url.objects.create(link=newLink)
            shortUrl.add_uuid()
            shortUrl.save()
            serializer = UrlSerializer(shortUrl, many=False)
            return Response(serializer.data)
        else:
            return Response("Url is not Valid!!!")

    return Response("Necessary data was not sent!!!")
