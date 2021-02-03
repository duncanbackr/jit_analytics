def prepare(all_rows):
    '''take list of list and drop faulty columns'''

    #####gets rid of row if there is no timestamp####
    all_rows_clean1 = [i for i in all_rows if str(i[5]) != 'nan']

    #####gets rid of row if the comment id is a string#####

    return all_rows_clean1 