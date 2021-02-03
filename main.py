from datetime import datetime, timezone
from Query.query_sql import query_data
import Analytics

all_rows_unclean = query_data()
all_rows = prepare(all_rows_unclean)
#today = datetime.now()

##(mean, sd)##
cut_off_data = [4, 2]
top_fan_cutoff = cut_off_data[0] + 2*cut_off_data[1]


if __name__ == '__main__':
     proccessed_comments = Analytics.add_score(all_rows, top_fan_cutoff)
     print(proccessed_comments)

