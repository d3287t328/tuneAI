import sys
from youtube_transcript_api import YouTubeTranscriptApi

def get_clean_transcript(video_id):
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1)

    return "".join(f"{line['text']} " for line in transcript)

if __name__ == "__main__":
    video_id = sys.argv[1]
    clean_transcript = get_clean_transcript(video_id)
    print(clean_transcript)
