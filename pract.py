import redis
import os
import requests
from flask import Flask
from flask_redis import Redis
from flask import make_response,abort,request
from flask_restful import reqparse, abort, Api, Resource
import os
from flask_restful import Api
import pickle
import json
import yaml
import gzip
from datetime import timedelta

app = Flask(__name__)

api =Api(app)


app.config['REDIS_URL'] = 'redis://:redis123@localhost:6379/0'

r = Redis(app)
#
# r.set("msg:hello", "Hello Redis!!!")
#
# # step 5: Retrieve the hello message from Redis
# msg = r.get("msg:hello")


#uri = r.set("uri","https://devapi.appkeelaa.com/api/processpayments")
# dict_obj = {"name":"bhanu","last":"sheeram"}
# r.set("uri", str(dict_obj))

#
# @app.route('/api/postcall')

class Getcreateredis(Resource):

    def get(self):

        vals = r.lrange("obj13", 0, -1)
        for x in vals:
            z=x.decode()
            str = z.replace("\'", "\"")
            res = json.loads(str)
            v="z"
            for key ,value in res.items():
                if (key == "name"):
                    print("<<<<<<<<<<<<<<<",type(value))
                    if value.startswith(v):
                        dict={key:value}
                        print(dict)
                    if value.endswith(v):
                        dict={key:value}
                        print(dict)

    def post(self):
           # try:
               json_obj = request.get_json()
               for key, values in json_obj.items():
                   for x in values:
                       #print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>",x)
                       obj = r.rpush(key, x)
                       expire=r.expire(key,60)
                       #print(expire)
                       print(obj)

    def put (self):
        delete_obj=r.delete(key)
        json_obj = request.get_json()
        for key, values in json_obj.items():
             for x in values:
                 obj = r.rpush(key, x)
                 expire=r.expire(key,60)
                 print(obj)


    def delete(self,id):
        obj=r.delete(id)
        print(obj)


        # for key,value in r.zscan_iter("obj7",match="name"):
        # #     print(key)
        # p = r.pipeline()
        # # t=p.get("obj10")
        # # print(t)
        # for k,v in r.hscan_iter("obj7","name"):
        #     print(k,v)
        #         vals = r.mget(keys)
        #data=r.lrange("obj7",0,-1)

    # def post(self):
    #        # try:
    #            json_obj = request.get_json()
    #            #p = r.pipeline()
    #            for key, values in json_obj.items():
    #                for x in values:
    #                    #print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>",x)
    #                    obj = r.rpush(key, x)
    #                    expire=r.expire("key",1)
    #                    print(obj)
                       # obj2=r.rpush(obj)
                       # print(obj2)

            # # json_images = json.dumps(json_obj)
            # print(r.set('event',str(json_images)))
            # # unpacked_images = json.loads(r.get('event').decode('utf-8'))
            # #
            # # d=unpacked_images['event']
            # # for x in d:
            # #     for name, age in x.items():
            # #         if age
            # #     print(x)







        # except Exception as e:
        #    return (str(e))
        #


        #  json_obj = request.get_json()
        #  for key, value in json_obj.items()
        #
        #  result_list = [int(v) for lst in qs for k, v in lst.items()]
        #
        # # mydict = pickle.dumps(json_obj)
        #  #library_obj=r.setex("libry_obj", timedelta(minutes=15),value=str(json_obj))
        #  obj=r.hmset("event",json_obj)
        #  print(obj)

         #d=r.expire("nani",200000)
         #r.bgsave()
         # nani)

    # def delete(self):
    #     s=r.delete("uri")
# # #
# class Getall(Resource):
#
#
#     def get(self):
#
#         data={}
#         keys = r.keys()
#         vals = r.mget(keys)
#         kv = zip(keys, vals)
#         print(dict(kv))
#
#
# class Getupdtae(Resource):
#
#     def get(self):
#
#         d=r.hmget("nani","name")
#         print(d)
#
#         val="852"
#         keys = r.keys()
#         #print(">>>>>>>>>>>>>>>>",keys)
#         di=[]
#         for y in keys:
#             a=y.decode()
#             #print("<<<<<<<<<<<<<<<",a)
#             for k,v in r.hscan_iter(a,match="ph*"):
#                 print(k.decode(),v.decode())
#                 if val in str(v.decode()):
#                      #print(k.decode(),v.decode())
#                      dict={k.decode():v.decode()}
#                      dict2={a:dict}
#                      di.append(dict2)

#         #
#         # return di
#
#
# class Create(Resource):
#
#     def post(self):



class Getupdtae(Resource):

    def post(self):

        json_obj = request.get_json()
        for k,v in json_obj.items():
            for values in v:
                obj=r.hmset(k,values)
                expire=r.expire("k",1)
                print(obj)

    def get(self):
         keys = r.keys()
         vals = r.mget(keys)
         print(keys,vals)
        # json_obj = request.get_json()
        # obj=r.mget("set_obj")
        # print(obj)

        # vals = r.lrange("json_obj", 0, -1)
        # for obj in vals:
        #     z=(obj.decode())
        #     print(z)
        #     for x , y in z.items():
        #         print(x,y)
        #
        # for key in r.hscan_iter("json_obj","name"):
        #     print(key)
        # # d=r.hmget("json_obj","name")
        # # print(">>>>>>>>>>>>>",d)
        #
        # val="852"
        # keys = r.keys()
        # #print(">>>>>>>>>>>>>>>>",keys)
        # di=[]
        # for y in keys:
        #     a=y.decode()
        #     #print("<<<<<<<<<<<<<<<",a)
        #     for k,v in r.hscan_iter(a,match="ph*"):
        #         print(k.decode(),v.decode())
        #         if val in str(v.decode()):
        #              #print(k.decode(),v.decode())
        #              dict={k.decode():v.decode()}
        #              dict2={a:dict}
        #              di.append(dict2)

    def put (self,id):
        json_obj = request.get_json()
        library_obj=r.set(id,str(json_obj))
        data=json.dumps(json_obj)
        print(json_obj)

    def delete(self,id):
        obj=r.delete(id)
        print(obj)

#
#
#
#
#
# class Getcreate(Resource):
#
#     def get(self):
#
#         obj= r.hgetall("event")
#         unidict = dict((k.decode('utf8'), v.decode('utf8')) for k, v in obj.items())
#         print(unidict)
#         if unidict["name"]=="bhanu":
#
#




#
#
#
#
#
#
#
#         # for hash in r.hscan_iter('libry_obj2'):
#         #     print(hash)
#
#         # # for keys in r.scan_iter('uri','name'):
#         # #     print(">>>>>>>>>>>",keys)
#         #     vals = r.mget(keys)
#         #     print(vals)
#         #     dict_obj = vals.decode()
#         #     print(dict_obj)
#         #     kv = {keys:vals}
#         #     print((kv))
#
#                 #print(dict(kv))
#             # #print(vals)
#             # d=len(vals)
#             # for y in range(0,d):
#             #     z=vals[y]
#             #     # print(z)
#             #     dict_obj = z.decode()
#             #     dit=dict_obj
#             #     # print(int(dit))
            #     search_key="na*"
            #     #
            #     # #print(res)
            #     for key in dit:
            #         if search_key in key:
            #             print(keys)
            #     # #print(res)

            #     # re.serach("na")

        # for name in r.scan_iter('uri'):
        #     for x in r.scan_iter('na*:'):
        #         print(x)
        # #for key in r.scan_iter("user:*")
        # for user,value in r.scan_iter('*u','n*'):
        #     print(user,value)
        #
        # for hash in r.scan_iter('uri',):
        #    print(hash) #for all child key
        # #msg1 = r.get(id)
        # # data=json.dumps(msg1)
        # # #return data
        #
        # # print(msg1)

    #
    #



api.add_resource(Getcreateredis, '/api/postredis')
# #
# api.add_resource(Getall, '/api/getall')
# # #
api.add_resource(Getupdtae, '/api/getupdate')
#
# api.add_resource(Getcreate, '/api/get')
#


if __name__ == '__main__':
   app.run(port=5001,debug=True)
