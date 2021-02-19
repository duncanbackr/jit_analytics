import config
import requests

def batch_data(okta_id: str, backrest_url=config.BACKREST_URL):
    """
        Requests the most recent analytics for the creator and returns a list [mean, standard deviation]
        :param okta_id: creator to request
        :param backrest_url: url of backrest
        :return: {data: [mean, standard deviation], creator: {creator object}}
    """
    if config.ENV == 'Local':
        return {'data': [4, 2], 'creator': {'thumbnail': 'sample_creator_thumbnail', 'channel_name': 'sample crator name'}}

    url = f'{backrest_url.geturl()}youtube/creatoranalytics/'
    
    metadata_server_token_url = 'http://metadata/computeMetadata/v1/instance/service-accounts/default/identity?audience='

    token_request_url = metadata_server_token_url + backrest_url.geturl()
    token_request_headers = {'Metadata-Flavor': 'Google'}

    # Fetch the token
    token_response = requests.get(token_request_url, headers=token_request_headers)
    jwt = token_response.content.decode("utf-8")

    #Provide the token in the request to the receiving service
    backrest_headers = {'Authorization': f'bearer {jwt}'}

    response = requests.get(url,
                params={'creator__okta_platform_account_id': okta_id,
                        'limit': 1},
                headers=backrest_headers)

    if response.status_code == 200 and response.json()['results']:
        mean = response.json()['results'][0]['mean']
        std = response.json()['results'][0]['standard_deviation']
        creator_url = response.json()['results'][0]['creator']

        creator = requests.get(creator_url,
                    headers=backrest_headers)

        return {'data': [mean, std], 'creator': creator.json()}
    
    else:
        return {'error': f'Must run batch analytics for creator {okta_id}'}
