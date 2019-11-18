import pickle
import redis

r = redis.StrictRedis('localhost')
mydict = {1:2,2:3,3:4}
p_mydict = pickle.dumps(mydict)
r.set('mydict',p_mydict)

read_dict = r.get('mydict')
yourdict = pickle.loads(read_dct)




#update expire  time for key

SETEX myKey ttlvalue newValue
