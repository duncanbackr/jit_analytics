def create_video_string(videoId):
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

def create_fan_string(fan_id):
    """
    Function which accepts a fan_id arg and returns sql string

    param:
        fan_id = '1234'
    returns:
        " AND youtube_fan_id = 1234"
    """
    video_string = f" AND youtube_fan_id = {fan_id}"
    return video_string