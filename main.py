from datetime import datetime
import Analytics, Filter, Formating, Query, Sort
import time
from flask import jsonify

def main(request):

     requestArgs = request.args

     if requestArgs.get('okta_id'):
          okta_id = requestArgs.get('okta_id')
     else: 
          # TODO raise error with frontend (ask Michael)
          return {'error': 'must include an okta id'}


     perPage = int(requestArgs.get('perPage', 100))
     limit = perPage * 500
     
     start =  time.process_time()
     """ Get data from db and backrest """
     raw_data = Query.latest_comments(okta_id, limit)
     cut_off_data = Query.batch_data(okta_id)
     
     end_pull =  time.process_time()

     """ Add analytics calculations """
     scored_comments, replies = Analytics.add_score(raw_data, cut_off_data)

     end_analytics =  time.process_time()

     if requestArgs.get('resource') == 'fans':
          filtered_comments = Filter.from_list(
               scored_comments, 
               badge=requestArgs.get('badge', 'topFan'))
          end_filter =  time.process_time()
          sorted_comments = Sort.from_list(
               filtered_comments, 
               param='badge_score')
          end_sort =  time.process_time()
          final_list = Formating.fans(sorted_comments, perPage)
          end_format = time.process_time()
          end_all =  time.process_time()

     elif requestArgs.get('resource') == 'comments':
          filtered_comments = Filter.from_list(
               scored_comments, 
               video_id=requestArgs.get('video_id'),
               badge=requestArgs.get('badge'),
               archived=requestArgs.get('archived'),
               comment_class=requestArgs.get('comment_class'))
          end_filter =  time.process_time()
          sorted_comments = Sort.from_list(
               filtered_comments, 
               param=requestArgs.get('order', 'balanced'))
          end_sort =  time.process_time()
          final_list = Formating.comments(sorted_comments, replies, perPage)
          end_format = time.process_time()
          end_all =  time.process_time()
     
     times = {
          'pull time (s)': end_pull - start,
          'analytics time (s)': end_analytics - end_pull,
          'filter time (s)':end_filter - end_analytics,
          'sort time (s)':end_sort - end_filter,
          'formating time (s)':end_format - end_sort,
          'full time (s)':end_all - start
     }
     final_list.insert(0, times)

     return jsonify(final_list)

# if __name__ == '__main__':
#      final_list = main(
#           {
#                'okta_id': '00u1h5s6uhNe35ICm4x7',
#                'resource': 'comments',
#                'badge': 'topFan'
#      })
#      print(final_list)