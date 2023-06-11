from django.shortcuts import render


# Create your views here.
from .models import *
from .serializers import *
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin

'''
class Audiencelist(GenericAPIView,ListModelMixin):
    queryset = Audience.objects.all()
    serializer_class = AudienceSerializer
    def get(self,request):
        return self.list(request)
    


class Audiencecreate(GenericAPIView,CreateModelMixin):
    queryset= Audience.objects.all()
    serializer_class = AudienceSerializer
    def post(self,request):
        return self.create(request)
        
class Audiencedisplay(GenericAPIView,RetrieveModelMixin):
    queryset = Audience.objects.all()
    serializer_class = AudienceSerializer
    def get(self,request,**kwargs):
        return self.retrieve(request,**kwargs)
    

class Audience_Update(GenericAPIView,UpdateModelMixin):
    queryset = Audience.objects.all()
    serializer_class = AudienceSerializer
    def put(self,request,**kwargs):
        return self.update(request,**kwargs)
    
class Audience_del(GenericAPIView,DestroyModelMixin):
    queryset = Audience.objects.all()
    serializer_class = AudienceSerializer
    def delete(self,request,**kwargs):
        return self.destroy(request,**kwargs)
    

'''

class Audiencelistcreate(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset = Audience.objects.all()
    serializer_class = AudienceSerializer
    def get(self,request):
         return self.list(request)
    def post(self,request):
        return self.create(request)
    


    
    
class Audiencedisplay(GenericAPIView,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
    queryset = Audience.objects.all()
    serializer_class = AudienceSerializer
    def get(self,request,**kwargs):
        return self.retrieve(request,**kwargs)
    def put(self,request,**kwargs):
        return self.update(request,**kwargs)
    def delete(self,request,**kwargs):
        return self.destroy(request,**kwargs)
    


