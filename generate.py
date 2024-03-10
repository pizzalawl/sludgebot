import ffmpeg
import sys
import random

video = sys.argv[1]
overlay = sys.argv[2]
length = int(sys.argv[3])

video_duration = ffmpeg.probe(video)['streams'][0]['duration']
overlay_duration = ffmpeg.probe(overlay)['streams'][0]['duration']

def randomSecondGen(duration):
    integerDuration = int(round(float(duration)))

    second = random.randint(0, integerDuration)

    return second

if __name__ == "__main__":
    videoRandomSec = randomSecondGen(video_duration)-length
    overlayRandomSec = randomSecondGen(overlay_duration)-length

    edited_video = (
        ffmpeg
        .input(video)
        .trim(start=videoRandomSec, end=videoRandomSec+length, duration=length)
        .output("edited-video.mp4")
        .run()
    )
    edited_overlay = (
        ffmpeg
        .input(overlay)
        .trim(start=overlayRandomSec, end=overlayRandomSec+length, duration=length)
        .output("edited-overlay.mp4")
        .run()
    )