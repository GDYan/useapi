from django.http import JsonResponse, HttpResponse
from rest_framework.views import APIView
from .models import myuser
from .serializer import Userserializers
# Create your views here.

class  UserAPI(APIView):
    def get(self):
        all_names = myuser.objects.values('name')
        print('user', all_names)
        data={}
        data['list'] = list(all_names)
        if all_names:
            return JsonResponse(data, safe=False)
        print('Null')
        return False



    def post(self):

        user = self.request.data
        print('save_user:', user)
        serializer = Userserializers(data=user)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(None, status=201, safe=False)
        else:
            return HttpResponse("保存失败")





    def delete(self):
        print("  这是删除方法", self.request.data["name"])
        print("  这是删除方法", myuser.objects.filter(name=self.request.data["name"]))
        if myuser.objects.filter(name=self.request.data["name"]):
           myuser.objects.filter(name=self.request.data["name"]).delete()
           return JsonResponse(None, status=204,safe=False)
        return JsonResponse({'code': 'Notfounduser'}, status=404,safe=False)


