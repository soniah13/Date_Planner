from flask import Flask, request, jsonify
from planner.plans import add_plans, list_plans, draw_plan, mark_done, reset_plans

app = Flask(__name__)

@app.get("/")
def root():
    return {"ok": True, "message": "Date Planner API"}

@app.post("/events")
def add_event():
    data = request.json or {}
    title = data.get("title")
    if not title:
        return {"error": "title required"}, 400
    result = add_plans(title)  
    return result, 201

@app.get("/events")
def get_events():
    return jsonify(list_plans())  

@app.post("/events/draw")
def draw():
    result = draw_plan()  
    return result, 200

@app.post("/events/<int:id>/done")
def done(id):
    result = mark_done(id) 
    if "error" in result:
        return result, 400
    return result, 200

@app.post("/events/reset")
def reset():
    result = reset_plans()  
    return result, 200
