# JIT_analytics
Just-in-time analytics

## Return formats
```js
comments = [{
    platformAvatar: thumbnail_url (str),
    badge: str **Calculated**,
    fanID: YoutubeFan.id,
    authorDisplayName: YoutubeFan.account_title,
    commentDatePosted: timestamp,
    commentID: YoutubeComment.id,
    textDisplay: YoutubeComment.content,
    likeCount: YoutubeComment.numblikes,
    archive: YoutubeComment.archived,
    up_vote: YoutubeComment.upVote,
    down_vote: YoutubeComment.upVote,
    replies: formattedReplies,
    videoTitle: YoutubeVideo.title,
}]

formattedReplies = [{
    platformAvatar: thumbnail_url (str),
    badge: str,
    fanID: YoutubeFan.id,
    authorDisplayName: YoutubeFan.account_title,
    commentDatePosted: timestamp,
    commentID: YoutubeComment.id,
    textDisplay: YoutubeComment.content,
    likeCount: YoutubeComment.numblikes,
    archive: YoutubeComment.archived,
    up_vote: YoutubeComment.upVote,
    down_vote: YoutubeComment.upVote,
    replies: formattedReplies,
    videoTitle: YoutubeVideo.title,
}]

fans = [{
    fanID: YoutubeFan.id,
    profileImage: thumbnail_url (str),
    displayName: YoutubeFan.account_title,
    note: YoutubeFan.note,
    lastCommentDate: timestamp **Calculated**,
    fanScore: int (0-100) **Calculated**,
    badge: str **Calculated**,
}]
```

connect to db
./cloud_sql_proxy -instances=backr-dev:us-central1:data-main=tcp:5432
