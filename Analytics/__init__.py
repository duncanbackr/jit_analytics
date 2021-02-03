from Analytics.addbadge import add_badge
from Analytics.badgescore import add_fan_score
from Analytics.delayscores import create_delay_scores
from Analytics.growthscore import add_growth_score
from Analytics.preparedict import unpack
from Analytics.retainscore import add_retain_score
from Analytics.scalescores import delay1_score, delay2_score, delay3_score, comment_score, reply_score, response_score

def add_score(all_rows, top_fan_cutoff): 
    replies = {}
    proccessed_comments = []
    for k in range(len(all_rows)):
        comment = unpack(all_rows[k])

        y = comment['parent_youtube_comment_id']

        if (isinstance(y, float)):
            comment['badge'] = add_badge(comment['total_comments'], top_fan_cutoff, 
                                   comment['timestamp'], comment['sec_comment'], comment['max'])

            comment['growth_score'] = add_growth_score(comment['total_comments'], top_fan_cutoff, 
                                                    comment['responses'], comment['timestamp'], 
                                                    comment['sec_comment'], comment['max'], comment['badge'])

            comment['retain_score'] = add_retain_score(comment['total_comments'], top_fan_cutoff, 
                                                    comment['responses'], comment['total_replies'], comment['timestamp'], 
                                                    comment['sec_comment'], comment['max'], comment['badge'])

            comment['badge_score'] = add_fan_score(comment['total_comments'], top_fan_cutoff, 
                                                    comment['responses'], comment['timestamp'], 
                                                    comment['sec_comment'], comment['max'], comment['badge'])

            proccessed_comments.append(comment)

        else:
            if y in replies:
                replies[y].append(comment)
            else:
                replies[y] = [comment]
            
    return  proccessed_comments, replies