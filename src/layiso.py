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

register(
        "python_fu_layiso",
        "Isolate the active layer",
        "Hide all layers except the active one.",
        "Jan Singon Slany",
        "Jan Singon Slany",
        "2016",
        "<Image>/Layer/Isolate Layer",
        "RGB*, GRAY*",
        [],
        [],
        plugin_main)

main()