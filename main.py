from datetime import datetime, timezone
from query.query import query_data
from Analytics.addbadge import add_badge
from Analytics.badgescore import add_fan_score
from Analytics.delayscores import create_delay_scores
from Analytics.growthscore import add_growth_score
from Analytics.preparedict import unpack
from Analytics.retainscore import add_retain_score
from Analytics.scalescores import delay1_score, delay2_score, delay3_score, comment_score, reply_score, response_score
from Analytics.preparerows import prepare

all_rows = query_data()
all_rows = prepare(all_rows)
#today = datetime.now()

##(mean, sd)##
cut_off_data = [4, 2]
top_fan_cutoff = cut_off_data[0] + 2*cut_off_data[1]

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

# if __name__ == '__main__':
#     proccessed_comments = add_score(all_rows, top_fan_cutoff)
#     print(type(proccessed_comments['3464'][0]['parent_youtube_comment_id']))

