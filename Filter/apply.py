# filtered_commments = Filter(
# 	processed_comments,
# 	videoID = '182z184z189z', '183z', None # youtube video id (postgres)
# 	badge = 'All', 'newFan', 'topFan', 'trendingFan', 'reEngageFan', None # str
# 	archived = True, False, None # Bool
# 	commentClass = 'All', None, 'Question', 'Positive', 'Suggestion', 'Negative' # str
# 	)


def from_list(comments, videoId=None, badge=None, archived=None, comment_class=None):

    filter_list = []

    for comment in comments:

        if badge:
            if comment['badge'] != badge:
                continue

        if videoId:
            video_list = [int(video) for video in videoId.split('z') if video]
            if comment['videoId'] not in video_list:
                continue

        # if archived != None:
        #     if comment['archived'] != archived:
        #         continue

        if comment_class:
            if (comment['classification'] is None) or \
                        (comment['classification'].lower() != comment_class.lower()):
                continue

        filter_list.append(comment)

    return filter_list 
