from pkg.oauth2.youtube import get_youtube_api_instance

scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]


class CommentThreads:
    def __init__(self) -> None:
        self.youtube = get_youtube_api_instance(
            credentials_name=self.__class__.__name__, scopes=scopes
        )

    def get_comments(self, video_id):
        request = self.youtube.commentThreads().list(part="snippet", videoId=video_id)
        response = request.execute()
        return response
