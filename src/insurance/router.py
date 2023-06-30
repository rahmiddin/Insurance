import json
from datetime import date as date_type
from json import JSONDecodeError

from fastapi import APIRouter, File, UploadFile

from src.insurance.dao import InsuranceDAO
from src.insurance.schemas import InputData

router = APIRouter(
    prefix="/insurance",
    tags=["Insurance"],
)


@router.post('/add')
async def add_rate(data_date: InputData):
    rate = await InsuranceDAO.add(data_date.dict())
    return rate


@router.post('/add/by_file')
async def add_rate_by_file(file: UploadFile = File(None)):
    try:
        file_json = json.load(file.file)
    except JSONDecodeError:
        return {'Status': 'False', 'Detail': "Incorrect file"}

    await InsuranceDAO.add(file_json)

    return {'Status': 'Complete'}


@router.post('/calculate_insurance')
async def calculate_insurance(price: int, date: date_type, cargo_type: str):
    rate = await InsuranceDAO.find(date=date, cargo_type=cargo_type)
    if not rate:
        return {'Status': 'По заданным значениям ничего не найдено'}
    return int(price * rate['rate'])
