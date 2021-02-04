from Analytics.constants import sql_columns

def unpack(row):
    '''converts row to dictionary'''

    comment = {}
    for i in range(len(row)):
        key = sql_columns[i]
        value = row[i]

        if type(value) is key['type']:
            comment[key['name']] = value
        
        elif key['required']:
            return None

        else:
            comment[key['name']] = None

    return comment
