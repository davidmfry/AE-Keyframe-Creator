__author__ = 'david'
# Creates a keyframe for adobe After Effects


class AE_Keyframe():
    frame = 0
    base_keyframe_type = ""
    key_frame_type = ""
    keyframe_data = []

    def __init__(self, frame, base_keyframe_type, key_frame_type):
        self.frame = frame
        self.base_keyframe_type = base_keyframe_type
        self.key_frame_type = key_frame_type
