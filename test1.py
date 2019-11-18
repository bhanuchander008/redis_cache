from config import *


class Getcreateredis(Resource):

    def get(self):

        json_obj = request.get_json()
        vals = r.lrange("obj12", 0, -1)
        for x in vals:
            z=x.decode()
            str = z.replace("\'", "\"")
            res = json.loads(str)
            v="s"
            for key ,value in res.items():
                if (key == "player" or key=="name" or key=="basket"):
                    print("<<<<<<<<<<<<<<<",type(value))
                    if value.startswith(v):
                        dict={key:value}
                        print(dict)
                    if value.endswith(v):
                        dict={key:value}
                        print(dict)
                    #print("<<<<<<<<<<<<<<<",type(value))

    def post(self):
           # try:

               json_obj = request.get_json()
               if json_obj:
                   for key, values in json_obj.items():
                       for x in values:
                           #print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>",x)
                           obj = r.rpush(key, x)
                           expire=r.expire(key,200000)
                   return ({"success":True, "message": "data posted successfully"})
               else:
                    return ({"success":False, "message": "data not posted successfully"})


    def put (self):
        delete_obj=r.delete("obj13")
        if delete_obj:
             return ({"success":True, "message": "data deleted successfully"})
        else:
            return ({"success":False, "message": "data not deleted successfully"})

        json_obj = request.get_json()
        if json_obj:
            for key, values in json_obj.items():
                 for x in values:
                     obj = r.rpush(key, x)
                     expire=r.expire(key,60)
            return ({"success":True, "message": "data updated successfully on same key"})
        else:
            return ({"success":False, "message": "data not updated successfully"})



    def delete(self):
        obj=r.flushall()
        if obj:
              return ({"success":True, "message": "data deleted successfully"})
        else:
              return ({"success":False, "message": "data not deleted successfully"})







api.add_resource(Getcreateredis, '/api/postredis')


if __name__ == '__main__':
   app.run(port=5001,debug=True)
