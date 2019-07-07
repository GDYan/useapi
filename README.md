#useapi

https://github.com/GDYan/useapi/
 
python3.6.8
django2.0
django-rest-framework

使用curl 测试GET  POST  DELETE请求

#初始所有用户
curl -v 127.0.0.1:8000/users/
#增加用户
curl -l -v -H "Content-type: application/json" -X POST -d {\"name\":\"1387\",\"pwd\":\"test\"} http://127.0.0.1:8000/users/
#所有用户
curl -v 127.0.0.1:8000/users/
#删除刚才添加的人
curl -l -v -H "Content-type: application/json" -X DELETE -d {\"name\":\"1387\"} http://127.0.0.1:8000/users/

