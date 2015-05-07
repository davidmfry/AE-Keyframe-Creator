__author__ = 'david'

from ae_key_frame import AE_Keyframe


def create_keyframe(data, base_keyframe_type, keyframe_type):
    """

    :param data, base_keyframe_type, keyframe_type:
    :param data:
    """

    keyframe_list = []

    for data_item in data:
        (frame, key_data) = data_item
        keyframe_list.append(AE_Keyframe(frame, base_keyframe_type, keyframe_type, key_data))
    return keyframe_list



# my_key_data = [(0, [960, 540, 0]), (10, [980, 540, 0]), (20, [1000, 560, 0])]
#
# my_keyframes = create_keyframe(my_key_data, "Transform", "Position")
#
# for item in my_keyframes:
#     print(item.base_keyframe_type)