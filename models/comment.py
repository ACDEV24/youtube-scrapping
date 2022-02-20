# This code parses date/times, so please
#
#     pip install python-dateutil
#
# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = comment_from_dict(json.loads(json_string))

from typing import Any, TypeVar, Type, cast
from datetime import datetime
import dateutil.parser


T = TypeVar("T")


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_datetime(x: Any) -> datetime:
    return dateutil.parser.parse(x)


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


class AuthorChannelID:
    value: str

    def __init__(self, value: str) -> None:
        self.value = value

    @staticmethod
    def from_dict(obj: Any) -> 'AuthorChannelID':
        assert isinstance(obj, dict)
        value = from_str(obj.get("value"))
        return AuthorChannelID(value)

    def to_dict(self) -> dict:
        result: dict = {}
        result["value"] = from_str(self.value)
        return result


class TopLevelCommentSnippet:
    video_id: str
    text_display: str
    text_original: str
    author_display_name: str
    author_profile_image_url: str
    author_channel_url: str
    author_channel_id: AuthorChannelID
    can_rate: bool
    viewer_rating: str
    like_count: int
    published_at: datetime
    updated_at: datetime

    def __init__(self, video_id: str, text_display: str, text_original: str, author_display_name: str, author_profile_image_url: str, author_channel_url: str, author_channel_id: AuthorChannelID, can_rate: bool, viewer_rating: str, like_count: int, published_at: datetime, updated_at: datetime) -> None:
        self.video_id = video_id
        self.text_display = text_display
        self.text_original = text_original
        self.author_display_name = author_display_name
        self.author_profile_image_url = author_profile_image_url
        self.author_channel_url = author_channel_url
        self.author_channel_id = author_channel_id
        self.can_rate = can_rate
        self.viewer_rating = viewer_rating
        self.like_count = like_count
        self.published_at = published_at
        self.updated_at = updated_at

    @staticmethod
    def from_dict(obj: Any) -> 'TopLevelCommentSnippet':
        assert isinstance(obj, dict)
        video_id = from_str(obj.get("videoId"))
        text_display = from_str(obj.get("textDisplay"))
        text_original = from_str(obj.get("textOriginal"))
        author_display_name = from_str(obj.get("authorDisplayName"))
        author_profile_image_url = from_str(obj.get("authorProfileImageUrl"))
        author_channel_url = from_str(obj.get("authorChannelUrl"))
        author_channel_id = AuthorChannelID.from_dict(
            obj.get("authorChannelId"))
        can_rate = from_bool(obj.get("canRate"))
        viewer_rating = from_str(obj.get("viewerRating"))
        like_count = from_int(obj.get("likeCount"))
        published_at = from_datetime(obj.get("publishedAt"))
        updated_at = from_datetime(obj.get("updatedAt"))
        return TopLevelCommentSnippet(video_id, text_display, text_original, author_display_name, author_profile_image_url, author_channel_url, author_channel_id, can_rate, viewer_rating, like_count, published_at, updated_at)

    def to_dict(self) -> dict:
        result: dict = {}
        result["videoId"] = from_str(self.video_id)
        result["textDisplay"] = from_str(self.text_display)
        result["textOriginal"] = from_str(self.text_original)
        result["authorDisplayName"] = from_str(self.author_display_name)
        result["authorProfileImageUrl"] = from_str(
            self.author_profile_image_url)
        result["authorChannelUrl"] = from_str(self.author_channel_url)
        result["authorChannelId"] = to_class(
            AuthorChannelID, self.author_channel_id)
        result["canRate"] = from_bool(self.can_rate)
        result["viewerRating"] = from_str(self.viewer_rating)
        result["likeCount"] = from_int(self.like_count)
        result["publishedAt"] = self.published_at.isoformat()
        result["updatedAt"] = self.updated_at.isoformat()
        return result


class TopLevelComment:
    kind: str
    etag: str
    id: str
    snippet: TopLevelCommentSnippet

    def __init__(self, kind: str, etag: str, id: str, snippet: TopLevelCommentSnippet) -> None:
        self.kind = kind
        self.etag = etag
        self.id = id
        self.snippet = snippet

    @staticmethod
    def from_dict(obj: Any) -> 'TopLevelComment':
        assert isinstance(obj, dict)
        kind = from_str(obj.get("kind"))
        etag = from_str(obj.get("etag"))
        id = from_str(obj.get("id"))
        snippet = TopLevelCommentSnippet.from_dict(obj.get("snippet"))
        return TopLevelComment(kind, etag, id, snippet)

    def to_dict(self) -> dict:
        result: dict = {}
        result["kind"] = from_str(self.kind)
        result["etag"] = from_str(self.etag)
        result["id"] = from_str(self.id)
        result["snippet"] = to_class(TopLevelCommentSnippet, self.snippet)
        return result


class CommentSnippet:
    video_id: str
    top_level_comment: TopLevelComment
    can_reply: bool
    total_reply_count: int
    is_public: bool

    def __init__(self, video_id: str, top_level_comment: TopLevelComment, can_reply: bool, total_reply_count: int, is_public: bool) -> None:
        self.video_id = video_id
        self.top_level_comment = top_level_comment
        self.can_reply = can_reply
        self.total_reply_count = total_reply_count
        self.is_public = is_public

    @staticmethod
    def from_dict(obj: Any) -> 'CommentSnippet':
        assert isinstance(obj, dict)
        video_id = from_str(obj.get("videoId"))
        top_level_comment = TopLevelComment.from_dict(
            obj.get("topLevelComment"))
        can_reply = from_bool(obj.get("canReply"))
        total_reply_count = from_int(obj.get("totalReplyCount"))
        is_public = from_bool(obj.get("isPublic"))
        return CommentSnippet(video_id, top_level_comment, can_reply, total_reply_count, is_public)

    def to_dict(self) -> dict:
        result: dict = {}
        result["videoId"] = from_str(self.video_id)
        result["topLevelComment"] = to_class(
            TopLevelComment, self.top_level_comment)
        result["canReply"] = from_bool(self.can_reply)
        result["totalReplyCount"] = from_int(self.total_reply_count)
        result["isPublic"] = from_bool(self.is_public)
        return result


class Comment:
    kind: str
    etag: str
    id: str
    snippet: CommentSnippet

    def __init__(self, kind: str, etag: str, id: str, snippet: CommentSnippet) -> None:
        self.kind = kind
        self.etag = etag
        self.id = id
        self.snippet = snippet

    @staticmethod
    def from_dict(obj: Any) -> 'Comment':
        assert isinstance(obj, dict)
        kind = from_str(obj.get("kind"))
        etag = from_str(obj.get("etag"))
        id = from_str(obj.get("id"))
        snippet = CommentSnippet.from_dict(obj.get("snippet"))
        return Comment(kind, etag, id, snippet)

    def to_dict(self) -> dict:
        result: dict = {}
        result["kind"] = from_str(self.kind)
        result["etag"] = from_str(self.etag)
        result["id"] = from_str(self.id)
        result["snippet"] = to_class(CommentSnippet, self.snippet)
        return result


def comment_from_dict(s: Any) -> Comment:
    return Comment.from_dict(s)


def comment_to_dict(x: Comment) -> Any:
    return to_class(Comment, x)
