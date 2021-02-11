from datetime import datetime
import Analytics, Filter, Formating, Query, Sort
from flask import jsonify
import config

def main(request):

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
        return jsonify({'error': 'must include an okta id'}), 404


    perPage = int(requestArgs.get('perPage', 100))
    pageNum = int(requestArgs.get('pageNum', 0))
    limit = requestArgs.get('sample', 5000)
    
    """ Get data from db and backrest """
    raw_data = Query.latest_comments(okta_id, limit)
    cut_off_data = Query.batch_data(okta_id)
    
    """ Add analytics calculations """
    scored_comments, replies = Analytics.add_score(raw_data, cut_off_data)

    if requestArgs.get('resource') == 'fans':
        filtered_comments = Filter.from_list(
              scored_comments, 
              badge=requestArgs.get('badge', 'topFan'))
        sorted_comments = Sort.from_list(
              filtered_comments, 
              param='badge_score')

        final_list = Formating.fans(sorted_comments, pageNum, perPage)


    elif requestArgs.get('resource') == 'comments':
        filtered_comments = Filter.from_list(
              scored_comments, 
              videoId=requestArgs.get('videoId'),
              badge=requestArgs.get('badge'),
              archived=requestArgs.get('archived'),
              comment_class=requestArgs.get('comment_class'))
        sorted_comments = Sort.from_list(
              filtered_comments, 
              param=requestArgs.get('order', 'balanced'))
        final_list = Formating.comments(sorted_comments, replies, pageNum, perPage)
        
    if config.ENV == 'Local':
        return final_list

    ## Set CORS headers for the main request
    headers = {
        'Access-Control-Allow-Origin': '*'
    }

    return (jsonify(final_list), 200, headers)

# if __name__ == '__main__':
#      class Flask_Request:
#           def __init__(self, request_dict):
#                self.args = request_dict 

#      final_list = main(Flask_Request({'okta_id':'00u1mjatc3FRbFhUr4x7', 'resource':'comments', 'comment_class':'Suggestion'}))
#      print(final_list[0:5])