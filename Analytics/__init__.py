from datetime import datetime
from Analytics.addbadge import add_badge
from Analytics.badgescore import  add_badge_score
from Analytics.delayscores import create_delay_scores
from Analytics.growthscore import add_growth
from Analytics.preparedict import unpack
from Analytics.retentionscore import add_retention
from Analytics.scale import delay1_dict, delay2_dict, delay3_dict, comments_dict, \
    reply_dict, response_dict, bin_scale
  
def datetime_now():
    return datetime.utcnow()

def add_score(all_rows, cut_off_data, time_now):
    top_fan_cutoff = cut_off_data[0] + 2*cut_off_data[1]
    #top_fan_cutoff = 2
    #####min, max values for scaling####
    maxs = []
    mins = []

    for i in (5,10,11,12, 13):
        maxs.append(max([row[i] for row in all_rows if row[i] is not None]))

    for i in (5,10,11,12, 13):
        mins.append(min([row[i] for row in all_rows if row[i] is not None]))

    replies = {}
    proccessed_comments = []
    for row in all_rows:
        comment = unpack(row)

        if comment is None:
            continue

        parent_comment = comment['parent_youtube_comment_id']

        if parent_comment is None:

            delays = create_delay_scores(comment['timestamp'], comment['sec_comment'], time_now)

            comment['badge'] = add_badge(comment['total_comments'], top_fan_cutoff, delays)

            comment['growth'] = add_growth(comment['total_comments'], top_fan_cutoff, 
                                                    comment['responses'], comment['badge'], delays, maxs, mins)

            # comment['retention'] = add_retention(comment['total_comments'], 2, 
            #                                         comment['responses'], comment['total_replies'], comment['badge'], delays, maxs, mins)

            comment['balanced'] = 0.5*(
            #                             add_retention(comment['total_comments'], top_fan_cutoff, 
            #                                     comment['responses'], comment['total_replies'], comment['badge'], delays, maxs, mins) 
                                        
            #                             + 
                                        
                                        add_growth(comment['total_comments'], top_fan_cutoff, 
                                                comment['responses'], comment['badge'], delays, maxs, mins)
                                        
                                        )

            # comment['badge_score'] =  add_badge_score(comment['total_comments'], top_fan_cutoff, 
            #                                         comment['responses'], comment['badge'], delays, maxs, mins)

            proccessed_comments.append(comment)

        else:
            if parent_comment in replies:
                replies[parent_comment].append(comment)
            else:
                replies[parent_comment] = [comment]
            
    return  proccessed_comments, replies