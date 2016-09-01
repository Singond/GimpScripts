#!/usr/bin/env python

#
# Hides all custom channels except the active one.
#

from gimpfu import *

def plugin_main(img, drawable):  
    active = pdb.gimp_image_get_active_channel(img)
    channels = img.channels
    for channel in channels:
        if channel==active:
            channel.visible = True
        else:
            channel.visible = False

# Placed in Channel context menu
register(
        "python_chaniso",
        "Isolate this channel",
        "Hide all custom channels except the active one.",
        "Jan Singon Slany",
        "Jan Singon Slany",
        "2016",
        "Isolate Channel",
        "RGB*, GRAY*",
        [
            (PF_IMAGE, "image", "Input image", None),
            (PF_DRAWABLE, "drawable", "Input drawable", None)
        ],
        [],
        plugin_main,
        "<Channels>")

# Placed in main Layer menu
"""register(
        "python_chaniso",
        "Isolate this channel",
        "Hide all layers except the active one.",
        "Jan Singon Slany",
        "Jan Singon Slany",
        "2016",
        "Isolate Channel",
        "RGB*, GRAY*",
        [
            (PF_IMAGE, "image", "Input image", None),
            (PF_DRAWABLE, "drawable", "Input drawable", None)
        ],
        [],
        plugin_main,
        "<Image>/Layer")"""

main()