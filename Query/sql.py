def full_query(okta_id, video_string, limit=5000):
    query = f'''
            WITH 
            -- FIRST CTE
            all_comments (
                comment_id, 
                parent_youtube_comment_id,
                youtube_fan_id,
                by_creator,
                content,
                archived,
                timestamp,
                up_vote,
                down_vote,
                video_title,
                video_id
                )
            AS (
                SELECT 
                    comments.id as comment_id,
                    comments.parent_youtube_comment_id as parent_youtube_comment_id,
                    comments.youtube_fan_id as youtube_fan_id,
                    comments.by_creator as by_creator,
                    comments.content as content,
                    comments.archived as archived,
                    comments.timestamp as timestamp,
                    comments.up_vote as up_vote,
                    comments.down_vote as down_vote,
                    video.video_title as video_title,
                    video.video_id as video_id
                FROM
                    (   
                        SELECT 
                            id as video_id,
                            video_title
                        FROM
                            (
                                SELECT
                                    id as creator_id
                                FROM
                                    creators
                                WHERE
                                    okta_platform_account_id = '{okta_id}'
                            )
                            creator
                        JOIN
                            youtube_videos
                        ON youtube_videos.creator_id = creator.creator_id
                    )
                    video
                JOIN 
                    youtube_comments comments
                ON video.video_id = comments.youtube_video_id
            ),

            -- SECOND CTE 
            top_comments (
                comment_id, 
                parent_youtube_comment_id,
                youtube_fan_id,
                by_creator,
                content,
                archived,
                timestamp,
                up_vote,
                down_vote,
                video_title,
                video_id
                )
            AS 
            (    
                SELECT
                    *
                FROM 
                    all_comments
                WHERE 
                    parent_youtube_comment_id is NULL{video_string}
                AND
                    by_creator is false
                ORDER BY timestamp desc
                LIMIT {limit}

            ),

            -- THIRD CTE
            top_fan_comments (
                comment_id, 
                parent_youtube_comment_id,
                youtube_fan_id,
                timestamp
                )
            AS (
                SELECT
                    all_comments.comment_id as comment_id, 
                    all_comments.parent_youtube_comment_id as parent_youtube_comment_id,
                    all_comments.youtube_fan_id as youtube_fan_id,
                    all_comments.timestamp as timestamp
                FROM 
                    (
                        SELECT
                            DISTINCT youtube_fan_id as id
                        FROM top_comments
                    )
                    top_fans
                JOIN all_comments
                ON top_fans.id = all_comments.youtube_fan_id
            ),

            -- FOURTH CTE
            top_comments_with_replies (
                comment_id, 
                parent_youtube_comment_id,
                youtube_fan_id,
                by_creator,
                content,
                archived,
                timestamp,
                up_vote,
                down_vote,
                video_title,
                video_id
                )
            AS (
                SELECT
                    *
                FROM
                    top_comments 
                UNION
                SELECT
                    replies.comment_id as comment_id,
                    parent_youtube_comment_id,
                    youtube_fan_id,
                    by_creator,
                    content,
                    archived,
                    timestamp,
                    up_vote,
                    down_vote,
                    video_title,
                    video_id
                FROM
                (
                    SELECT
                        comment_id
                    FROM
                        top_comments
                ) roots
                JOIN
                    all_comments replies
                ON roots.comment_id = replies.parent_youtube_comment_id
            )

            -- MAIN QUERY
            SELECT
                top_comments_with_replies.comment_id,
                top_comments_with_replies.parent_youtube_comment_id,
                top_comments_with_replies.youtube_fan_id,
                top_comments_with_replies.content,
                top_comments_with_replies.archived,
                top_comments_with_replies.timestamp,
                top_comments_with_replies.up_vote,
                top_comments_with_replies.down_vote,
                top_comments_with_replies.video_title,
                top_comments_with_replies.video_id,
                fan_aggregations.total_comments,
                fan_aggregations.total_replies,
                fan_aggregations.responses,
                fan_aggregations.sec_comment,
                youtube_fans.account_title,
                youtube_fans.thumbnail_url,
                youtube_fans.note,
                engagement_analytics.engagement_class_id
            FROM
                top_comments_with_replies
            LEFT JOIN
            (   -- AGGREGATION
                SELECT 
                    top_fan_comments.youtube_fan_id as youtube_fan_id, 
                    COUNT(top_fan_comments.comment_id) as total_comments, 
                    COUNT(top_fan_comments.parent_youtube_comment_id) as total_replies, 
                    COUNT(responses.creator_response) as responses, 
                    MAX(second_comment.sec_timestamp) as sec_comment
                FROM 
                    top_fan_comments
                JOIN -- Second Comment timestamp
                    (
                        SELECT 
                            comment_id,
                            youtube_fan_id, 
                            nth_value(timestamp,2) OVER (PARTITION BY youtube_fan_id
                            ORDER BY timestamp DESC) AS sec_timestamp
                        FROM top_fan_comments
                    )
                    second_comment
                ON top_fan_comments.comment_id = second_comment.comment_id
                LEFT JOIN -- Creator Responses
                    (
                        SELECT
                            distinct parent_youtube_comment_id as creator_response
                        FROM all_comments
                        WHERE by_creator = TRUE
                    )
                    responses
                ON top_fan_comments.comment_id = responses.creator_response
                GROUP BY top_fan_comments.youtube_fan_id
            )
            fan_aggregations
            ON top_comments_with_replies.youtube_fan_id = fan_aggregations.youtube_fan_id

            LEFT JOIN
            (
                SELECT
                    id,
                    account_title,
                    thumbnail_url,
                    note
                FROM
                    youtube_fans
            )
            youtube_fans
            ON top_comments_with_replies.youtube_fan_id = youtube_fans.id

            LEFT JOIN
            (
                SELECT
                    engagement_class_id,
                    youtube_comment_id
                FROM
                    engagement_analytics
            )
            engagement_analytics
            ON top_comments_with_replies.comment_id = engagement_analytics.youtube_comment_id
        '''
    return query