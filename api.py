from aiohttp import web
import json
import pymongo
from bson import json_util
 
mongourl = "mongodb://127.0.0.1:27017/" #Database url
 
async def apitest(request):
    result ={"status":"200"}
    return web.Response(text=json.dumps(result), status=200)
 
async def create(request):
    try:
        collection = request.match_info.get('collection', "Anonymous") #Get collection name from params
 
        myclient = pymongo.MongoClient(mongourl)
        mydb = myclient["database"]  # Database Name
        mycol = mydb["collection"]  # Collection name
        j = await request.json()
        x = mycol.insert_one(j)
        
        # emit something is changed notify event through webSocket
        await sio.emit('notify',str(x.inserted_id))
        
        response_obj = {'status': 'success',"_id":str(x.inserted_id)}
        return web.Response(text=json.dumps(response_obj), status=200)
    except Exception as e:
        response_obj = {'status': 'failed', 'reason': str(e)}
        web.Response(text=json.dumps(response_obj), status=500)
 
async def show(request):
    try:
        collection = request.match_info.get('collection', "Anonymous") #Get collection name from params
 
        myclient = pymongo.MongoClient(mongourl)
        mydb = myclient["database"]  # Database Name
        mycol = mydb["collection"]  # Collection name
        mydoc = list(mycol.find())  # add all data in a List
        # convert list into json
        response_obj = json.loads(json_util.dumps(mydoc))
        res = {"Data":response_obj}
        return web.Response(text=json.dumps(res), status=200)
    except Exception as e:
        response_obj = {'status': 'failed', 'reason': str(e)}
        web.Response(text=json.dumps(response_obj), status=500)
 
app = web.Application()
 
#Add Routers
app.router.add_get('/apitest',apitest)
app.router.add_post('/create/{collection}',create)
app.router.add_get('/show/{collection}',show)
 
if __name__ == '__main__':
    web.run_app(app)
