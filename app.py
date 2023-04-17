from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

app = FastAPI()
templates = Jinja2Templates(directory="templates")


class BMIInput(BaseModel):
    weight: float
    height: float


def calculate_bmi(weight, height):
    """
    計算 BMI 值
    :param weight: 體重，單位：公斤
    :param height: 身高，單位：公分
    :return: BMI 值
    """
    height_in_meters = height / 100.0  # 將身高從公分換算成公尺
    bmi = weight / (height_in_meters ** 2)  # 計算 BMI 值
    return bmi


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/")
async def calculate(input: BMIInput):
    bmi = calculate_bmi(input.weight, input.height)
    return {"bmi": bmi}
