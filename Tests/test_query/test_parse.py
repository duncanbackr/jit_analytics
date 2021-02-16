import Query

def test_video_id_parser():
    video_string = Query.parse.create_string('12z13z14z')
    assert video_string == ' AND video_id in (12, 13, 14)'

    video_string = Query.parse.create_string('12z')
    assert video_string == ' AND video_id in (12)'