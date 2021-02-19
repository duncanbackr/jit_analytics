def create_string(videoId):
    """
    Function which accepts a videoId arg and returns sql string

    param:
        videoId = '342z248z'
    returns:
        " AND video_id in (342, 248)"
    """
    video_list = videoId.split('z')
    video_string = " AND video_id in ("
    for video_id in video_list:
        video_string = video_string + str(video_id) + ', '
    return video_string[:-4] + ')'