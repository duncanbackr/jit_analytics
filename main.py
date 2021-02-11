from datetime import datetime
import Analytics, Filter, Formating, Query, Sort
from flask import jsonify
import config

def main(request):

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
     time_now = Analytics.datetime_now()
     """ Add analytics calculations """
     scored_comments, replies = Analytics.add_score(raw_data, cut_off_data, time_now)

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

     return jsonify(final_list), 200

if __name__ == '__main__':
     class Flask_Request:
          def __init__(self, request_dict):
               self.args = request_dict 

     #final_list = main(Flask_Request({'okta_id':'00u1mjatc3FRbFhUr4x7', 'resource':'comments'}))
     raw_data = Query.latest_comments('00u1mjatc3FRbFhUr4x7', 300)
     # max_date = datetime(2018,1,1)
     # for item in raw_data:
     #      date = item[5]
     #      if date > max_date and item[1] is None:
     #           max_date = date
     
     print(raw_data[0:300])