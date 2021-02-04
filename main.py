from datetime import datetime, timezone
import Query
import Analytics
import Sort

all_rows = Query.query_db()

##(mean, sd)##
cut_off_data = [4, 2]
top_fan_cutoff = cut_off_data[0] + 2*cut_off_data[1]


if __name__ == '__main__':
     proccessed_comments = Analytics.add_score(all_rows, top_fan_cutoff)[0]
     x = Sort.backr_sort(proccessed_comments, 'timestamp')
     print(x)

