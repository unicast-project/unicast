from src.models.expected_timefraction_predictions import best_range, expected_timefraction
from src.models import input_type

import uvicorn
from fastapi import FastAPI
import json

app = FastAPI()
PredType_best_range = input_type.PredType_best_range
PredType_expected_timefraction = input_type.PredType_expected_timefraction


@app.get("/")
def read_root():
    return {"UniCast": "Optimize your Uniswap settings"}


@app.post("/best_range")
def best_range_(inp_request: PredType_best_range = None):
    timefraction = inp_request.time_fraction
    time_horizon = inp_request.time_horizon
    coingecko_kwargs = inp_request.coingecko_kwargs
    res = best_range(timefraction, time_horizon, **coingecko_kwargs)

    return json.dumps(res)


@app.post("/expected_timefraction")
def expected_timefraction_(inp_request: PredType_expected_timefraction = None):
    lower_bound = inp_request.lower_bound
    upper_bound = inp_request.upper_bound
    time_horizon = inp_request.time_horizon
    coingecko_kwargs = inp_request.coingecko_kwargs
    print("main coingecko_kwargs: ", coingecko_kwargs)
    res = expected_timefraction(lower_bound, upper_bound, time_horizon, **coingecko_kwargs)
    return json.dumps(res)


if __name__ == '__main__':
    uvicorn.run(app, port=8000, host="0.0.0.0")