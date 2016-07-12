#!/usr/bin/env python

#
# Creates a new image with duplicates of what is visible in the current image,
# each scaled to a standard icon size.
#

from gimpfu import *

def plugin_main(img, drawable):  
    active = pdb.gimp_image_get_active_layer(img)
    layers = img.layers
    for layer in layers:
        if layer==active:
            layer.visible = True
        else:
            layer.visible = False

# Placed in Layer context menu
register(
        "python_layiso2",
        "Isolate this layer",
        "Hide all layers except the active one.",
        "Jan Singon Slany",
        "Jan Singon Slany",
        "2016",
        "Isolate Layer",
        "RGB*, GRAY*",
        [
            (PF_IMAGE, "image", "Input image", None),
            (PF_DRAWABLE, "drawable", "Input drawable", None)
        ],
        [],
        plugin_main,
        "<Layers>")

# Placed in main Layer menu
register(
        "python_layiso",
        "Isolate this layer",
        "Hide all layers except the active one.",
        "Jan Singon Slany",
        "Jan Singon Slany",
        "2016",
        "Isolate Layer",
        "RGB*, GRAY*",
        [
            (PF_IMAGE, "image", "Input image", None),
            (PF_DRAWABLE, "drawable", "Input drawable", None)
        ],
        [],
        plugin_main,
        "<Image>/Layer")

main()