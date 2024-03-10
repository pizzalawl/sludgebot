from moviepy.editor import *
import sys
import random

video = sys.argv[1]
overlay = sys.argv[2]
duration = int(sys.argv[3])

videoClip = VideoFileClip(f"video/{video}")
videoClipDuration = videoClip.duration
overlayClip = VideoFileClip(f"video/{overlay}")
overlayClipDuration = overlayClip.duration

videoClipSize = videoClip.size

def randomSecondGen(duration):
    integerDuration = int(round(float(duration)))

    second = random.randint(0, integerDuration)

    return second

videoClipRandomSec = randomSecondGen(videoClipDuration)-duration
overlayClipRandomSec = randomSecondGen(overlayClipDuration)-duration
trimmedVideoClip = videoClip.subclip(videoClipRandomSec, videoClipRandomSec+duration)
trimmedOverlayClip = overlayClip.subclip(overlayClipRandomSec, overlayClipRandomSec+duration)

editedVideoClip = trimmedVideoClip.without_audio()
editedOverlayClip = trimmedOverlayClip.resize(width=videoClipSize[0], height=videoClipSize[1]/2)

finalVideo = CompositeVideoClip([editedVideoClip, 
                                editedOverlayClip.set_position(("center", "top"))])

finalVideo.write_videofile('output.mp4',codec='libx264')
