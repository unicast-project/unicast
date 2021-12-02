from pydantic import BaseModel
from typing import Optional


class PredType_best_range(BaseModel):

    time_horizon: Optional[int] = 30
    time_fraction: float
    coingecko_kwargs: Optional[dict] = {'id': 'ethereum', 'vs_currency': 'usd', 'days': '5000'}


class PredType_expected_timefraction(BaseModel):

    time_horizon: Optional[int] = 30
    lower_bound: float
    upper_bound: float
    coingecko_kwargs: Optional[dict] = {'id': 'ethereum', 'vs_currency': 'usd', 'days': '5000'}
