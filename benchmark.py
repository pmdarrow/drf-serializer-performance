import requests
import time


contracts = [{
    'name': 'Test contract',
    'date': '2016-01-01T12:00',
    'premium': {
        'value': 123567.89,
        'currency': 'usd',
    },
    'limit': {
        'value': 123567.89,
        'currency': 'usd',
    },
    'franchise': {
        'value': 123567.89,
        'currency': 'usd',
    },
    'attachment': {
        'value': 123567.89,
        'currency': 'usd',
    }
} for i in range(500)]

portfolio = {'contracts': contracts}

start = time.time()
r = requests.post('http://localhost:8000/portfolios/', json=portfolio)
elapsed = time.time() - start

print('Total time to POST portfolio: {:.2f}s'.format(elapsed))
print('Status code:', r.status_code)
print('Body:', str(r.json())[:500], '...')
