from flask import Flask,jsonify,abort,render_template
from flask_restful import Resource,Api,request
app=Flask(__name__)
api=Api(app)
tasks=[]
@app.route("/put/<string:name>",methods=["POST","GET"])
def post(name):
    temp={"data":name}
    tasks.append(temp)
    return {"note":"added"}
@app.route("/post/<string:name>",methods=["GET"])
def get(name):
    if request.method=="GET":
        for x in tasks:
            if x["data"]==name:
                return x
            else:
                return ({"data":"none"})

@app.route("/rest/<string:name>",methods=["GET","POST"])
def delete(name):
    for ind,x in enumerate(tasks):
        if x["data"] == name:
            tasks.pop(ind)
            return ({"NOTE":"deleted"})
@app.route("/draw/<string:name>/<string:surname>",methods=["GET","POST","PUT"])
def update(name,surname):
    for ind,x in enumerate(tasks):
        if x["data"] == name:
            x["data"]=surname
            return tasks
if (__name__)=="__main__":
    app.run(debug=True)