from datetime import datetime
import Query, Analytics, Sort, Formating

def main(request):

     requestArgs = request.args()

     if requestArgs.get('creator_id'):
          creator_id = int(requestArgs.get('creator_id'))
     else: 
          # TODO raise error with frontend (ask Michael)
          return {'error': 'must include a creator_id'}

     if request.args.get('limit'):
          limit = int(requestArgs.get('limit'))
     else:
          limit = 200
     
     """ Get data from db and backrest """
     raw_data = Query.latest_comments(creator_id, limit)
     cut_off_data = Query.batch_data(creator_id)

     """ Add analytics calculations """
     scored_comments, replies = Analytics.add_score(raw_data, cut_off_data)

     """ Filter Data """
     # TODO call filter
     filtered_comments = scored_comments

     """ Sort Data """
     # TODO call sort
     sorted_comments = filtered_comments

     """ Format Data """
     if requestArgs.get('')
     formated_result = Formating.comments(sorted_comments, replies)
     
     return formated_result
