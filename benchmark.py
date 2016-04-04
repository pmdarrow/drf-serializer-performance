import requests
import time

base_url = 'http://localhost:8000'

# people = [requests.post(base_url + '/people/', json={
#     'first_name': 'Test',
#     'last_name': 'User'
# }).json() for i in range(500)]
people = requests.get(base_url + '/people/').json()[:500]

sub_contracts = [{
    'name': 'Sub contract',
    'type': 'j',
    'date': '2016-01-01T12:00',
    'authors': [
        p['url']
    ],
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
} for p in people]

contract = {
    'name': 'Master contract',
    'sub_contracts': sub_contracts,
}

portfolio = {
    'name': 'Main portfolio',
    'contracts': [contract],
}

start = time.time()
r = requests.post('http://localhost:8000/portfolios/', json=portfolio)
elapsed = time.time() - start

print('Total time to POST portfolio: {:.2f}s'.format(elapsed))
print('Status code:', r.status_code)
print('Body:', str(r.json())[:1000], '...')
