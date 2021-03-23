from datetime import datetime
from Analytics.addbadge import add_badge
from Analytics.badgescore import  add_badge_score
from Analytics.delayscores import create_delay_scores
from Analytics.growthscore import add_growth
from Analytics.balancedscore import add_balanced
from Analytics.preparedict import unpack
from Analytics.retentionscore import add_retention
from Analytics.scaledelay import delay_diff
from Analytics.scaler import min_max_scaler

#import time

def datetime_now():
    return datetime.utcnow()

def add_score(all_rows, cut_off_data, time_now):
    top_fan_cutoff = cut_off_data[0] + 2*cut_off_data[1]
    #top_fan_cutoff = 2
    #####min, max values for scaling####

    all_comments = [unpack(row) for row in all_rows]

    maxs = {}
    mins = {}

    for col in ['timestamp', 'total_comments', 'total_replies', 'responses', 'sec_comment']:
        try:
            maxs[col] = max([comment[col] for comment in all_comments if comment[col] is not None])
            mins[col] = min([comment[col] for comment in all_comments if comment[col] is not None])
        except (ValueError):
            maxs[col] = None
            mins[col] = None

    delay_max = create_delay_scores(maxs['timestamp'], maxs['sec_comment'], time_now)
    delay_min = create_delay_scores(mins['timestamp'], mins['sec_comment'], time_now)

    replies = {}
    proccessed_comments = []
    for comment in all_comments:

        if comment is None:
            continue

        parent_comment = comment['parent_youtube_comment_id']

        if parent_comment is None:

            delays_unscaled = create_delay_scores(comment['timestamp'], comment['sec_comment'], time_now)

            comment['badge'] = add_badge(comment['total_comments'], top_fan_cutoff, delays_unscaled)

            delays_scaled = [min_max_scaler(delays_unscaled[i], delay_min[i], delay_max[i])
                            if delay_min[i] and delays_unscaled[i] else None
                            for i in range(3)]


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