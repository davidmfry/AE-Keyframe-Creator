__author__ = 'david'
# Creates a keyframe for adobe After Effects


class AE_Keyframe():

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

    def make_pos_keyframe(self, frame, x_pos, y_pos, z_pos):
        return "{frame} {x_pos} {y_pos} {z_pos}".format(frame=frame, x_pos=x_pos, y_pos=y_pos, z_pos=z_pos)

    def make_rot_keyframe(self, frame, degree):
        return "{frame} {degree}".format(frame=frame, degree=degree)

