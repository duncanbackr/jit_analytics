from Analytics.constants import sql_columns

def unpack(row):
    '''converts row to dictionary'''

    comment = {}
    for i in range(len(row)):
        key = sql_columns[i]
        value = row[i]
        
        comment[key['name']] = None

        if type(value) is key['type']:
            comment[key['name']] = value
        
        elif key['required']:
            return None

        elif row[1] is None:
            # Check if its a root comment
            if key['root_required']:
                return None
    
    return comment
