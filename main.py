from datetime import datetime, timezone
import Query
import Analytics
import Sort
import Filter

if __name__ == '__main__':
     creator_id = 37 # TODO grab these from the request params
     limit = 5000
     
     """ Get data from db and backrest """
     raw_data = Query.db.latest_comments(creator_id, limit)
     cut_off_data = Query.backrest.batch_data(creator_id)

     """ Add analytics calculations """
     proccessed_comments = Analytics.add_score(raw_data, cut_off_data)
     
     print(proccessed_comments)
