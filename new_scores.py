from datetime import datetime
import Analytics
from mock_data import raw_sql_data

items = raw_sql_data

cut_off_data = [4,2]
time_now = datetime(2021, 2, 18, 18, 32, 34)

if __name__ == "__main__":
    df = Analytics.add_score(items, cut_off_data, time_now)

    for i in range(0,10):
        print(df[0][i]['badge'])
        print(df[0][i]['balanced'])