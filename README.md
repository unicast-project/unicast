# UniCast

The UniCast project brings machine learning (ML) forecasting and ML models to Uniswap v3 and the larger DeFi ecosystem. The project aims to contribute with the tools, building blocks and examples to create, train and serve machine learning predictions off-chain or on-chain. UniCast is available for free as open source. We hope the community finds it useful and it can serve as a starting point in many other ML projects.

### Uniswap v3

Uniswap V3 created a new way to provide liquidity in DeFi. Instead of liquidity providers (LPs) providing liquidity on the entire price range, Uniswap V3 enables concentrated liquidity. LPs can now allocate liquidity on a price range where their liquidity is used, instead of over the total range of prices.

When allocating in a narrow price range your liquidity is highly concentrated, and the position is more capital efficient and generates more fees when the price is in range.

The wider the price range, the fewer fees you’ll accrue. But by providing liquidity in a tighter price range you’re also at a higher risk of impermanent loss.

### Impermanent Loss in Uniswap v3

In a recent paper by the Bancor team there's evidence that the majority of the addresses providing liquidity in Uniswap v3 were not profitable. Although deploying positions in tight ranges can lead to higher returns it is at the expense of a higher risk of incurring more impermanent losses. In the paper, it is concluded that the impermanent losses (-$260.1M) exceed the returns LPs earned from trading fees ($199.3M).

<img src="https://s3.us-west-2.amazonaws.com/secure.notion-static.com/2412fed5-1177-482d-8707-ad48b915a1b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20211203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20211203T115140Z&X-Amz-Expires=86400&X-Amz-Signature=bddbd2a375d9a47a7c275109a03b7332aa833f673448bf7d2ed49c668c47494e&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22&x-id=GetObject" width=60%>
  
Source: https://arxiv.org/pdf/2111.09192.pdf

It seems that using trivial LP strategies or too active strategies will almost guarantee you to underperform. Liquidity provision on Uniswap v3 has become a game for professional LPs and experienced DeFi users that understand market-making.

### Smart LPing

With UniCast we aim to create the foundation for building AI-driven strategies that intelligently adapt to market conditions and offer good returns to LPs on Uniswap v3.

The first release of UniCast focuses on assessing the risk of the price to move completely outside a Uniswap v3 position. There's a live model (with a REST-API) available with with code, tutorial and instructions on the Github project page.

<img src="https://s3.us-west-2.amazonaws.com/secure.notion-static.com/b04cf8e0-ae80-4b2e-906c-3b6393558071/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20211203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20211203T114951Z&X-Amz-Expires=86400&X-Amz-Signature=2470d1b40adbbc9f150b6224e0b76c9e3b898295414bba31476f512054a1fbea&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22&x-id=GetObject" width=60%>
  
Source: https://github.com/unicast-project/unicast/blob/main/demo_python_endpoints.ipynb

Going forward we are focusing on upgrading the hosting and secure long time (free) API access to both models, publish better instructions, tutorials and documentation for both the risk assessment and range optimizer model, and deploying smart contracts that serve predictions on-chain from the models. 

### Test on a hosted endpoint
The Docker image below has been deployed and is available for testing. It will return the expected risk of current price moving out of the position in the set timeframe. The upp er and lower bound are expressed as a fraction of the current price, e.g. upper_bound (in USD terms) / current_price (in USD terms) gives the upper fraction. Any asset id from Coingecko can be used. This endpoint is purely for testing purposes and comes with no accuracy, uptime or performance gurantees.

```python
import pickle
import requests
import json
import numpy as np

def fraction(range_bound, current_price):
    fraction = range_bound/current_price
    return fraction


url = 'http://165.227.232.84:8000/expected_timefraction'

inp = {
    "lower_bound": fraction(2276, 4553), 
    "upper_bound": fraction(9106, 4553),
    "time_horizon": 30,
    "coingecko_kwargs": {'id': 'ethereum', 'vs_currency': 'usd', 'days': '100'}
}

res = requests.post(url, headers = {'Content-type': 'application/json'}, json=inp)
print(res)
f = (json.loads(res.json())['time_fraction'])
print("Expected time fraction: ", np.round(f,3), " (chance of moving out of range in the time horizon: ", np.round(((1-np.round(f,3))*100),3), "%)")
```

### Docker Deployment tutorial
Docker can be used to deploy Unicast and create an endpoint using fast-api.  
In the project folder, build the Docker image with:
`docker build -t <your_username>/unicast .`  
Start the Docker container:
`docker run -p 8000:8000 <your_username>/unicast`
This will generate endpoints that can be called with curl or used in e.g. a python script:  `

```
import requests
import json
```
define an url the the format:  ADRESS:PORT/UNICAST-FUNCTION, here we demonstrate a local deployement
with the default port 8000 and the unicast function best_range
```
url = 'http://0.0.0.0:8000/best_range'
```
Set input values: time_fraction, time_horizon and coingecko_kwargs:
```
inp = {
    "time_fraction": 0.5, 
    "time_horizon": 30,
    "coingecko_kwargs": {'id': 'bitcoin', 'vs_currency': 'usd', 'days': '5000'}
}
```
Call the api:
```
res = json.loads(requests.post(url, headers = {'Content-type': 'application/json'}, json=inp).json())
```
this will return a json with the result value.

### More info & sources

For more project updates and to get in touch with the team, please use Twitter or interact with us directly here on GitHub:
Twitter (https://twitter.com/0xUnicast)
GitHub (https://github.com/unicast-project)
Gitcoin Grant (https://gitcoin.co/grants/3600/unicast)

Sources  
[https://arxiv.org/abs/2111.09192](https://arxiv.org/abs/2111.09192)


