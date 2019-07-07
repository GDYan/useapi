from django.http import JsonResponse, HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser, FormParser
from rest_framework.request import Request
from .serializer import Userserializers
from .models import User,myuser
parser_classes = [JSONParser,FormParser]
class  UserAPI(APIView):

    def get_all_username(self,request):
        # all_names = myuser.objects.all()
        all_names = myuser.objects.values('name')
        #serializer = Userserializers(instance=all_names, many=True)
        #print("allname:", serializer.data)
        print('user', all_names)
        data={}
        data['list'] = list(all_names)
        if all_names:
            return JsonResponse(data, safe=False)
        print('Null')
        return False



    def save_user(self,request):
        # user={}
        # user['username'] = request.POST.get('username')
        # user['password'] = request.POST.get('password')
        user = self.request.data
        print('save_user:', user)
        serializer = Userserializers(data=user)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(None, status=202, safe=False)
        # return  HttpResponse("保存成功")
        else:
            return HttpResponse("保存失败")
