from datetime import datetime, timezone
import query
import Analytics
import sort

if __name__ == '__main__':
     creator_id = 37 # TODO grab these from the request params
     limit = 5000
     
     """ Get data from db and backrest """
     raw_data = Query.latest_comments(creator_id, limit)
     cut_off_data = Query.batch_data(creator_id)

     """ Add analytics calculations """
     all_comments = Analytics.add_score(raw_data, cut_off_data)
     
     print(all_comments)
