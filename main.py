from datetime import datetime
import Analytics, Filter, Formating, Query, Sort
from flask import jsonify
import math
import config
#import time

def main(request):
    #total_start = time.time()

    ## Set CORS headers for the preflight request
    if request.method == 'OPTIONS':
        ## Allows GET requests from any origin with the Content-Type
        headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Max-Age': '3600'
        }

        return ('', 204, headers)

    requestArgs = request.args

    if requestArgs.get('okta_id'):
        okta_id = requestArgs.get('okta_id')
    else:
        if config.ENV == 'Local':
              return {'error': 'must include an okta id'}
        return (jsonify({'error': 'must include an okta id'}), 400)

    page = int(requestArgs.get('page', 0))
    perPage = int(requestArgs.get('perPage', 100))
    limit = requestArgs.get('sample', 5000)
    
    """ Create video filter string """
    if requestArgs.get('videoId'):
        video_string = Query.parse.create_string(requestArgs.get('videoId'))
    else:
        video_string = ""
    
    """ Get data from db and backrest """
    raw_data = Query.latest_comments(okta_id, video_string, limit)
    backrest_response = Query.batch_data(okta_id)
    if backrest_response.get('error'):
        return (jsonify(backrest_response), 500)
    else:
        cut_off_data = backrest_response['data']
        creator = backrest_response['creator']

    """ Add analytics calculations """
    scored_comments, replies = Analytics.add_score(raw_data, cut_off_data, Analytics.datetime_now())

    if requestArgs.get('resource') == 'fans':
        filtered_comments = Filter.from_list(
              scored_comments, 
              badge=requestArgs.get('badge', 'topFan'))
        sorted_comments = Sort.from_list(
              filtered_comments, 
              param='badge_score')
        final_list, total_length = Formating.fans(sorted_comments, page, perPage)

    elif requestArgs.get('resource') == 'comments':
        filtered_comments = Filter.from_list(
              scored_comments, 
              videoId=requestArgs.get('videoId'),
              badge=requestArgs.get('badge'),
              comment_class=requestArgs.get('comment_class'))
        sorted_comments = Sort.from_list(
              filtered_comments, 
              param=requestArgs.get('order', 'balanced'))
        archive = requestArgs.get('archive') == 'true'
        final_list, total_length = Formating.comments(sorted_comments, replies, creator, archive, page, perPage)
        
    if config.ENV == 'Local':
        return final_list

    ## Set CORS headers for the main request
    headers = {
        'Access-Control-Allow-Origin': '*'
    }
    # total_end = time.time()
    # final_list.insert(0, {'batch_call:': end-start, 'total_time': total_end-total_start})

    return (jsonify({'success': True,
                    'data': final_list,
                    'page': page,
                    'totalPages': math.ceil(total_length/perPage)
                    }), 200, headers)

if __name__ == '__main__':
    class Flask_Request:
        def __init__(self, request_dict):
            self.args = request_dict
            self.method = 'Not OPTIONS'

    final_list = main(Flask_Request({'okta_id':'00u28tfvep3vxPf3B4x7', 'resource':'comments', 'archive':'true'}))

    print([item.get('replies') for item in final_list])