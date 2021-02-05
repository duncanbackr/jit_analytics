# filtered_commments = Filter(
# 	processed_comments,
# 	videoID = '182z184z189z', '183z', None # youtube video id (postgres)
# 	badge = 'All', 'newFan', 'topFan', 'trendingFan', 'reEngageFan', None # str
# 	archived = True, False, None # Bool
# 	commentClass = 'All', None, 'Question', 'Positive', 'Suggestion', 'Negative' # str
# 	)


def from_list(comments, video_id=None, badge=None, archived=None, comment_class=None):

    filter_list = []

    comment_class_dict = {1:'Positive', 2: 'Negative', 3: 'Question', 4: 'Suggestion', 5: 'Other'}

    for comment in comments:

        if badge:
            if comment['badge'] != badge:
                continue

        if video_id:
            video_list = [int(video) for video in video_id.split('z')]
            if comment['video_id'] not in video_list:
                continue

        if archived:
            if comment['archived'] != archived:
                continue

        if comment_class:
            if comment_class_dict[comment['comment_class']] != comment_class:
                continue

        filter_list.append(comment)

    return filter_list 
