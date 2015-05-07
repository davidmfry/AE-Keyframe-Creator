__author__ = 'david'
from create_keyframes import *

keyframe_boiler_plate = "Adobe After Effects 8.0 Keyframe Data"
keyframe_end_line = "End of Keyframe Data"
#
# keyframe_list = []
#
# def add_keyframe_to_list(keyframe_type):
#
#
#
# def export_keyframe_data():
#     pass

class Keyframe_Formatter():

    units_per_sec = 0.0             # Also frame per second for the video clip
    src_width = 0                   # Video width IE: 1920
    src_height = 0                  # Video height IE: 1080
    src_pixel_aspect_ratio = 0      # Normal aspect would be 1
    comp_pixel_aspect_ratio = 0     # Normal aspect would be 1

    def __init__(self, units_per_sec, src_width, src_height, src_pixel_aspect_ratio=1, comp_pixel_aspect_ratio=1):
        self.units_per_sec = units_per_sec
        self.src_width = src_width
        self.src_height = src_height
        self.src_pixel_aspect_ratio = src_pixel_aspect_ratio
        self.comp_pixel_aspect_ratio = comp_pixel_aspect_ratio


def add_video_clip_stats(units_per_sec, src_width, src_height, src_pixel_aspect_ratio=1, comp_pixel_aspect_ratio=1):
    return units_per_sec, src_width, src_height, src_pixel_aspect_ratio, comp_pixel_aspect_ratio

def format_keyframe_type():
    return '''Transform	Position
        Frame	X pixels    Y pixels    Z pixels
        0	    960	        540	        -2666.67

    '''

def format_keyframe_file(video_stats, keyframes):

    # unpacks the video_stats tupel
    (frames_per_sec, width, height, src_aspect, comp_aspect) = video_stats



    top = '''{boiler_plate}

    Units Per Second	{frames_per_sec}
    Source Width	{width}
    Source Height	{height}
    Source Pixel Aspect Ratio	{src_aspect}
    Comp Pixel Aspect Ratio	{comp_aspect}

{keyframes}

{end_line}

    '''.format(boiler_plate=keyframe_boiler_plate, frames_per_sec=frames_per_sec, width=width, height=height,
               src_aspect=src_aspect, comp_aspect=comp_aspect, keyframes=keyframes, end_line=keyframe_end_line)


    return top

print(format_keyframe_file(add_video_clip_stats(29.97, 1920, 1080), format_keyframe_type()))