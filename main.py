from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/1001")
def read_root():
    return{"Collegename":"Idhya",
           "studentname":"sundari",
           "duration":"three years",
           "course":"Bcom",
           "Stream":"Arts",
           "cutoff":120
           }
@app.get("/1002")
def read_root():
    return {"Collegename": "Sastra",
            "studentname": "shanvi",
            "duration": "three years",
            "course": "Bsc(cs)",
            "Stream": "Arts",
            "cutoff": 120
            }
@app.get("/1003")
def read_root():
    return {"Collegename": "Govt college for mens",
            "studentname": "kaviraj",
            "duration": "three years",
            "course": "Bca",
            "Stream": "Arts",
            "cutoff": 120
            }
@app.get("/1004")
def read_root():
    return {
        "Collegename": "Govt college for women",
        "studentname": "Renu",
         "duration":"three years",
        "course": "Bsc(IT)",
        "Stream" : "Arts",
        "cutoff":130}

@app.get("/1005")
def read_root():
    return{
        "collegename":"ksk",
        "studentname": "harini",
        "duration":"three years",
        "course":"Bsc(maths)",
        "stream":"Arts",
        "cutoff":120}
@app.get("/1006")
def read_root():
    return{
        "collegename":"prist",
        "studentname":"priya",
        "duration":"three years",
        "course":"BBA",
        "stream":"Arts",
        "cutoff":110}
@app.get("/1007")
def read_root():
    return{
        "collegename":"pmist",
        "studentname":"Abi",
        "duration":"three years",
        "course":"B.com(B.M)",
        "stream":"Arts",
        "cutoff": 100}
@app.get("/1008")
def read_root():
    return{
        "collegename":"sdc",
        "studentname":"saro",
        "duration":"three years",
        "course":"B.com(c.s)",
        "stream":"Arts",
        "cutoff": 150}


@app.get("/check")
def read_root(college_id:str,cutoff:int):
    college={
        "1001":{"Collegename":"Idhya",
           "studentname":"sundari",
           "duration":"three years",
           "course":"Bcom",
           "Stream":"Arts",
           "cutoff":100},

        "1002":{"Collegename": "Sastra",
            "studentname": "shanvi",
            "duration": "three years",
            "course": "Bsc(cs)",
            "Stream": "Arts",
            "cutoff": 150},

        "1003":{"Collegename": "Govt college for mens",
            "studentname": "kaviraj",
            "duration": "three years",
            "course": "Bca",
            "Stream": "Arts",
            "cutoff": 140},
        "1004":{
            "Collegename": "Govt college for women",
            "studentname": "Renu",
            "duration": "three years",
            "course": "Bsc(IT)",
            "Stream": "Arts",
            "cutoff": 130
        },
        "1005":{
            "collegename": "ksk",
            "studentname": "harini",
            "duration": "three years",
            "course": "Bsc(maths)",
            "stream": "Arts",
            "cutoff": 120
        },
        "1006":{
            "collegename": "prist",
            "studentname": "priya",
            "duration": "three years",
            "course": "BBA",
            "stream": "Arts",
            "cutoff": 110
        },
        "1007":{
            "collegename": "pmist",
            "studentname": "Abi",
            "duration": "three years",
            "course": "B.com(B.M)",
            "stream": "Arts",
            "cutoff": 100
        },
        "1008":{
            "collegename": "sdc",
            "studentname": "saro",
            "duration": "three years",
            "course": "B.com(c.s)",
            "stream": "Arts",
            "cutoff": 150
        }
    }
    if college_id in college:
     mark = college[college_id]["cutoff"]
     details = college[college_id]
     if mark<=cutoff:
         return details
     else:
         return "failed"
    else:
     return "not found"




