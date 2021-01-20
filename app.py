from flask import Flask, render_template,request
#from flask_jira import FlaskJIRA
from flask_atlassian_connect import AtlassianConnect
from flask_ngrok import run_with_ngrok
import requests
import json
#jira = FlaskJIRA()
app = Flask(__name__)
ac = AtlassianConnect(app)
#jira.init_app(app)
#run_with_ngrok(app)
@ac.webhook('jira:issue_created')
def handle_jira_issue_created(client, event):
    pass

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/',methods=['POST'])
def getvalue():
    name=request.form['name']
    name1=request.form['name1']
    #hrtsum=int(name)+int(name1)
    url1 = "https://harshitsomani98.atlassian.net/rest/assetapi/asset/bulk"
    url2 = "https://testingportal.hexnodemdm.com/api/v1/devices/?order_by=desc"
 
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
        }
    headers1 = {
         "Authorization" :"t1BG7voOhkc6113yjczQ"
         }
    r = requests.get(url2, headers = headers1)                #returns requests.Response object
    k=(json.loads(r.text))                                    #converting to json type
    n=[] 
    putRequests=[]
    for z in k.get('results',None):
        #print(z['id'],end =" ")
        #print(z['serial_number'],end =" ")
        #print(z['device_name'])
        origin={}
        label={}
        putRequests1={}
        origin.update({"appKey":"my-app"})
        origin.update({"originId":z['id']})
        label.update({"value":z['serial_number'].encode('utf-8')})
        putRequests1.update({"origin":origin})
        putRequests1.update({"label":label})
        putRequests.append(putRequests1)
        #print(z['device_name'])
        #print(z['device_name'].encode('utf8'))
    print(putRequests)
    payload = json.dumps( {
    "putRequest": # putRequests
    [{'origin': {'appKey': 'my-app', 'originId': 1216}, 'label': {'value': 'abhinharshit173'}}]
    })  
    response = requests.request(
         "PUT",
         url1,
          data=payload,
          headers=headers,
          auth=('harshit@cloudlds2.com','uUcOe6CoskQd8KoEphWq3F16')
          )
  
    return render_template('pass.html')

if __name__=='__main__':
    app.run()
