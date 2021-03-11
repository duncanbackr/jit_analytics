from datetime import datetime
from Analytics.addbadge import add_badge
from Analytics.badgescore import  add_badge_score
from Analytics.delayscores import create_delay_scores_scaled, create_delay_scores_unscaled
from Analytics.growthscore import add_growth
from Analytics.balancedscore import add_balanced
from Analytics.preparedict import unpack
from Analytics.retentionscore import add_retention
from Analytics.scaledelay import delay_diff
#import time

def datetime_now():
    return datetime.utcnow()

def add_score(all_rows, cut_off_data, time_now):
    top_fan_cutoff = cut_off_data[0] + 2*cut_off_data[1]
    #top_fan_cutoff = 2
    #####min, max values for scaling####
    maxs = {}
    mins = {}

    for name, i in [('date_posted', 5), ('total_comments', 11), ('total_replies', 12), ('total_responses', 13), ('sec_date_posted', 14)]:
         maxs[name] = max([row[i] for row in all_rows if row[i] is not None])

    for name, i in [('date_posted', 5), ('total_comments', 11), ('total_replies', 12), ('total_responses', 13), ('sec_date_posted', 14)]:
         mins[name] = min([row[i] for row in all_rows if row[i] is not None])

    delay_max = {
                "delay1": delay_diff(time_now, mins['date_posted']),
                "delay2": delay_diff(maxs['date_posted'], mins['sec_date_posted']),
                "delay3": delay_diff(time_now, mins['sec_date_posted'])
                }

    delay_min = {
                "delay1": delay_diff(time_now, maxs['date_posted']),
                "delay2": 0,
                "delay3": delay_diff(time_now, maxs['sec_date_posted'])
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

            comment['balanced'] = add_balanced(comment['total_comments'], top_fan_cutoff, 
                                                    comment['responses'], comment['total_replies'], comment['badge'], delays_scaled, maxs, mins,
                                                    comment['retention'], comment['growth'])

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