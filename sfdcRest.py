import requests 
import constants

DOMAIN = constants.DOMAIN_FULL

# Generate Access Token
def generate_token():    
    payload = {
        'grant_type': 'password',
        'client_id': constants.CONSUMER_KEY,
        'client_secret': constants.CONSUMER_SECRET,
        'username': constants.USERNAME,
        'password': constants.PASSWORD
    }
    oauth_endpoint = '/services/oauth2/token'
    response = requests.post(DOMAIN + oauth_endpoint, data=payload)
    return response.json()

# Run Tooling API query
def tooling_query(soql_query):
    try:
        access_token = generate_token()['access_token']
        headers = {
            'Authorization': 'Bearer ' + access_token
        }
        #soql_query = "SELECT EntityDefinitionId,DurableId, Max, Remaining from EntityLimit WHERE EntityDefinition.DeveloperName = 'Account'"
        endpoint = '/services/data/v58.0/tooling/query/?q='+soql_query
        records = []
        response = requests.get(DOMAIN + endpoint, headers=headers, params={'q': soql_query})
        records.extend(response.json()['records'])
        total_size = response.json()['totalSize']
        while not response.json()['done']:
            response = requests.get(DOMAIN + endpoint + response.json()['nextRecordsUrl'], headers=headers)
            records.extend(response.json()['records'])
        return {'record_size': total_size, 'records': records}
    except Exception as e:
        print("**Tooling Query Exception***")
        print(e)
        return