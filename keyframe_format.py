__author__ = 'david'
import ae_key_frame

# keyframe_boiler_plate = "Adobe After Effects 8.0 Keyframe Data"
# keyframe_end_line = "End of Keyframe Data"
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

