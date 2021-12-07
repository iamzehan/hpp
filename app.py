import pickle

from fastapi import FastAPI,Form, Body
from fastapi.param_functions import Depends

from pydantic import BaseModel
from fastapi.responses import HTMLResponse

class Houses(BaseModel):
#['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude']
    Rooms: int

    Bathroom: float

    Landsize: float

    Lattitude: float

    Longtitude: float

app = FastAPI()


@app.get("/prediction",response_class=HTMLResponse)
async def main():
    content = """
<body>
    <form method="post">
        <input name="Rooms" type="text" placeholder="Rooms">
        <input name="Bathroom" type="text" placeholder="Bathrooms">
        <input name="Landsize" type="text" placeholder="Landsize">
        <input name="Lattitude" type="text" placeholder="Lattitude">
        <input name="Longtitude" type="text" placeholder="Longtitude">
        <input type="submit">
    </form>
</body>
    """
    return HTMLResponse(content=content)

with open("./model/melbourne_model.sav", "rb") as f:

    model = pickle.load(f)



@app.post('/prediction')

def get_house_price(Rooms:int=Form(...), Bathroom: float=Form(...), Landsize: float=Form(...),Lattitude: float=Form(...), Longtitude: float=Form(...)):
#['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude']

    pred_name = model.predict([[Rooms, Bathroom, Landsize, Lattitude, Longtitude]]).tolist()[0]

    return {'prediction': float(pred_name)}

