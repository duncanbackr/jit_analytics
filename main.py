from datetime import datetime
import Analytics, Filter, Formating, Query, Sort
from flask import jsonify

def main(request):

     requestArgs = request.args

     if requestArgs.get('okta_id'):
          okta_id = requestArgs.get('okta_id')
     else: 
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
               video_id=requestArgs.get('video_id'),
               badge=requestArgs.get('badge'),
               archived=requestArgs.get('archived'),
               comment_class=requestArgs.get('comment_class'))
          sorted_comments = Sort.from_list(
               filtered_comments, 
               param=requestArgs.get('order', 'balanced'))
          final_list = Formating.comments(sorted_comments, replies, pageNum, perPage)


     return jsonify(final_list), 200

# if __name__ == '__main__':
#      final_list = main(
#           {
#                'okta_id': '00u1h5s6uhNe35ICm4x7',
#                'resource': 'comments',
#                'badge': 'topFan'
#      })
#      print(final_list)