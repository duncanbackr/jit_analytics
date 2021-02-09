from datetime import datetime
import Analytics, Filter, Formating, Query, Sort
import time

def main(request):

     requestArgs = request.args()

     if requestArgs.get('okta_id'):
          okta_id = requestArgs.get('okta_id')
     else: 
          # TODO raise error with frontend (ask Michael)
          return {'error': 'must include an okta id'}


     perPage = int(requestArgs.get('perPage', 100))
     limit = perPage * 50
     
     start =  time.process_time()
     """ Get data from db and backrest """
     raw_data = Query.latest_comments(okta_id, limit)
     cut_off_data = Query.batch_data(okta_id)
     
     end_pull =  time.process_time() - start

     """ Add analytics calculations """
     scored_comments, replies = Analytics.add_score(raw_data, cut_off_data)

     end_analytics =  time.process_time() - end_pull

     if requestArgs.get('resource') == 'fans':
          filtered_comments = Filter.from_list(
               scored_comments, 
               badge=requestArgs.get('badge', 'topFan'))
          end_filter =  time.process_time() - end_analytics
          sorted_comments = Sort.from_list(
               filtered_comments, 
               param='badge_score')
          end_sort =  time.process_time() - end_filter
          final_list = Formating.fans(sorted_comments)
          end_format = time.process_time() - end_sort
          end_all =  time.process_time() - start

     elif requestArgs.get('resource') == 'comments':
          filtered_comments = Filter.from_list(
               scored_comments, 
               video_id=requestArgs.get('video_id'),
               badge=requestArgs.get('badge'),
               archived=requestArgs.get('archived'),
               comment_class=requestArgs.get('comment_class'))
          end_filter =  time.process_time() - end_analytics
          sorted_comments = Sort.from_list(
               filtered_comments, 
               param=requestArgs.get('order', 'balanced'))
          end_sort =  time.process_time() - end_filter
          final_list = Formating.comments(sorted_comments, replies)
          end_format = time.process_time() - end_sort
          end_all =  time.process_time() - start
     
     times = {
          'pull time (s)': end_pull,
          'analytics time (s)': end_analytics,
          'filter time (s)':end_filter,
          'sort time (s)':end_sort,
          'formating time (s)':end_format,
          'full time (s)':end_all
     }
     final_list.insert(0, times)
     
     return final_list

if __name__ == '__main__':
     final_list = main(
          {
               'okta_id': '00u1h5s6uhNe35ICm4x7',
               'resource': 'comments',
               'badge': 'topFan'
     })
     print(final_list[0])