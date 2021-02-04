import math
from Analytics.constants import sql_columns

def unpack(row):
    '''converts row to dictionary'''

    comment = {sql_columns[i]['name']: row[i] 
              for i in range(len(sql_columns))
              if type(row[i]) is sql_columns[i]['type']}

    return comment
