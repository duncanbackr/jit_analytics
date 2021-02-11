import config
import requests

def batch_data(okta_id: str, backrest_url=config.BACKREST_URL):
    """
        Requests the most recent analytics for the creator and returns a list [mean, standard deviation]
        :param okta_id: creator to request
        :param backrest_url: url of backrest
        :return: [mean, standard deviation]
    """
    if config.ENV == 'Local':
        return {'data': [4, 2]}
    
    url = f'{backrest_url}/youtube/creatoranalytics/'

    response = requests.get(url,
                params={'creator__okta_platform_account_id': '00u1qjieo8vM0Ifrz4x7',
                        'limit': 1})

    if response.status_code == 200 and response.json()['results']:
        mean = response.json()['results'][0]['mean']
        std = response.json()['results'][0]['standard_deviation']
        return {'data': [mean, std]}
    
    else:
        return {'error': f'Must run batch analytics for creator {okta_id}'}