from datetime import datetime
import Analytics, Filter, Formating, Query, Sort
import time
from flask import jsonify
import config

def main(request):

     requestArgs = request.args

     if requestArgs.get('okta_id'):
          okta_id = requestArgs.get('okta_id')
     else: 
          # TODO raise error with frontend (ask Michael)
          return {'error': 'must include an okta id'}


     perPage = int(requestArgs.get('perPage', 100))
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
          end_filter =  time.process_time()
          sorted_comments = Sort.from_list(
               filtered_comments, 
               param='badge_score')
          final_list = Formating.fans(sorted_comments, perPage)

     elif requestArgs.get('resource') == 'comments':
          filtered_comments = Filter.from_list(
               scored_comments, 
               videoId=requestArgs.get('videoId'),
               badge=requestArgs.get('badge'),
               archived=requestArgs.get('archived'),
               comment_class=requestArgs.get('comment_class'))
          end_filter =  time.process_time()
          sorted_comments = Sort.from_list(
               filtered_comments, 
               param=requestArgs.get('order', 'balanced'))
          final_list = Formating.comments(sorted_comments, replies, perPage)

     if config.ENV == 'Local':
          return final_list

     return jsonify(final_list)

# if __name__ == '__main__':
#      class Flask_Request:
#           def __init__(self, request_dict):
#                self.args = request_dict 

#      final_list = main(Flask_Request({'okta_id':'00u1mjatc3FRbFhUr4x7', 'resource':'comments', 'comment_class':'Suggestion'}))
#      print(final_list[0:5])