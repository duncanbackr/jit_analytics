from Analytics.addbadge import add_badge
from Analytics.badgescore import add_fan_score
from Analytics.delayscores import create_delay_scores
from Analytics.growthscore import add_growth_score
from Analytics.preparedict import unpack
from Analytics.retainscore import add_retain_score
from Analytics.scalescores import delay1_score, delay2_score, delay3_score, comment_score, reply_score, response_score
import math

def add_score(all_rows, cut_off_data):
    top_fan_cutoff = cut_off_data[0] + 2*cut_off_data[1]
    replies = {}
    proccessed_comments = []
    for k in range(len(all_rows)):
        comment = unpack(all_rows[k])

        y = comment['parent_youtube_comment_id']

        if str(y) =='None':
            comment['badge'] = add_badge(comment['total_comments'], top_fan_cutoff, 
                                   comment['timestamp'], comment['sec_comment'])

            comment['growth_score'] = add_growth_score(comment['total_comments'], top_fan_cutoff, 
                                                    comment['responses'], comment['timestamp'], 
                                                    comment['sec_comment'], comment['badge'])

            comment['retain_score'] = add_retain_score(comment['total_comments'], top_fan_cutoff, 
                                                    comment['responses'], comment['total_replies'], comment['timestamp'], 
                                                    comment['sec_comment'], comment['badge'])

            comment['balanced_score'] = 0.5*(add_retain_score(comment['total_comments'], top_fan_cutoff, 
                                                    comment['responses'], comment['total_replies'], comment['timestamp'], 
                                                    comment['sec_comment'], comment['badge']) + 
                                                    add_growth_score(comment['total_comments'], top_fan_cutoff, 
                                                    comment['responses'], comment['timestamp'], 
                                                    comment['sec_comment'], comment['badge']))

            comment['badge_score'] = add_fan_score(comment['total_comments'], top_fan_cutoff, 
                                                    comment['responses'], comment['timestamp'], 
                                                    comment['sec_comment'], comment['badge'])

            proccessed_comments.append(comment)

        else:
            if y in replies:
                replies[y].append(comment)
            else:
                replies[y] = [comment]
            
    return  (proccessed_comments, replies)