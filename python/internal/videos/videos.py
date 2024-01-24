from googleapiclient.http import MediaFileUpload

from pkg.oauth2.youtube import get_youtube_api_instance

scopes = [
    "https://www.googleapis.com/auth/youtube.readonly",
    "https://www.googleapis.com/auth/youtube.upload",
]


class Videos:
    def __init__(self) -> None:
        self.youtube = get_youtube_api_instance(
            credentials_name=self.__class__.__name__, scopes=scopes
        )

    def get_videos(self, video_id):
        request = self.youtube.videos().list(
            part="snippet,contentDetails,statistics", id=video_id
        )
        response = request.execute()
        return response

    def upload_video(self, file):
        request = self.youtube.videos().insert(
            part="snippet,status",
            body={
                "snippet": {
                    "categoryId": "22",
                    "description": "Description of uploaded video.",
                    "title": "Test video upload.",
                },
                "status": {"privacyStatus": "private"},
            },
            media_body=MediaFileUpload(file),
        )
        response = request.execute()
        return response
