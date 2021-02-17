from datetime import datetime
from Analytics.addbadge import add_badge
from Analytics.badgescore import  add_badge_score
from Analytics.delayscores import create_delay_scores_scaled, create_delay_scores_unscaled
from Analytics.growthscore import add_growth
from Analytics.preparedict import unpack
from Analytics.retentionscore import add_retention
from Analytics.scaledelay import max_delay, min_delay
#import time

def datetime_now():
    return datetime.utcnow()

def add_score(all_rows, cut_off_data, time_now):
    top_fan_cutoff = cut_off_data[0] + 2*cut_off_data[1]
    #top_fan_cutoff = 2
    #####min, max values for scaling####
    maxs = {}
    mins = {}

    for name, i in [('date_posted', 5), ('total_comments', 10), ('total_replies', 11), ('total_responses', 12), ('sec_date_posted', 13)]:
         maxs[name] = max([row[i] for row in all_rows if row[i] is not None])

    for name, i in [('date_posted', 5), ('total_comments', 10), ('total_replies', 11), ('total_responses', 12), ('sec_date_posted', 13)]:
         mins[name] = min([row[i] for row in all_rows if row[i] is not None])

    max_delay1 = max_delay(time_now, mins['date_posted'])
    min_delay1 = max_delay(time_now, maxs['date_posted'])

    max_delay3 = max_delay(time_now, mins['sec_date_posted'])
    min_delay3 = max_delay(time_now, maxs['sec_date_posted'])

    delay2_max = (maxs['date_posted'] - mins['sec_date_posted']).days + ((maxs['date_posted'] - mins['sec_date_posted']).seconds)/(3600*24)
    delay2_min = 0

    delay_max = {
                "delay1": max_delay1,
                "delay2": delay2_max,
                "delay3": max_delay3
                }

    delay_min = {
                "delay1": min_delay1,
                "delay2": delay2_min,
                "delay3": min_delay3
                }

    replies = {}
    proccessed_comments = []
    for row in all_rows:
        comment = unpack(row)

        if comment is None:
            continue

        parent_comment = comment['parent_youtube_comment_id']

        if parent_comment is None:

            delays_unscaled = create_delay_scores_unscaled(comment['timestamp'], comment['sec_comment'], time_now)
            delays_scaled = create_delay_scores_scaled(comment['timestamp'], comment['sec_comment'], time_now, delay_max, delay_min)

            comment['badge'] = add_badge(comment['total_comments'], top_fan_cutoff, delays_unscaled)

            comment['growth'] = add_growth(comment['total_comments'], top_fan_cutoff, 
                                                    comment['responses'], comment['badge'], delays_scaled, maxs, mins)

            comment['retention'] = add_retention(comment['total_comments'], top_fan_cutoff, 
                                                     comment['responses'], comment['total_replies'], comment['badge'], delays_scaled, maxs, mins)

            comment['balanced'] = 0.5*(
                                         add_retention(comment['total_comments'], top_fan_cutoff, 
                                                 comment['responses'], comment['total_replies'], comment['badge'], delays_scaled, maxs, mins) 
                                        
                                         + 
                                        
                                        add_growth(comment['total_comments'], top_fan_cutoff,  \
                                                comment['responses'], comment['badge'], delays_scaled, maxs, mins)
                                        
                                        )

            comment['badge_score'] =  add_badge_score(comment['total_comments'], top_fan_cutoff, 
                                                    comment['responses'], comment['badge'], delays_scaled, maxs, mins)

            proccessed_comments.append(comment)

        else:
            if parent_comment in replies:
                replies[parent_comment].append(comment)
            else:
                replies[parent_comment] = [comment]
            
    return  proccessed_comments, replies
    #print(end - start)