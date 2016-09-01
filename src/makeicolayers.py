#!/usr/bin/env python

# Creates duplicates of the active layer, each scaled to a standard icon size.

from gimpfu import *

def plugin_main(img, drawable):
    pdb.gimp_undo_push_group_start(img)

    layer(256, img.active_layer, img)
    layer(48, img.active_layer, img)
    layer(32, img.active_layer, img)
    layer(16, img.active_layer, img)

    pdb.gimp_undo_push_group_end(img)

def layer(size, original, image):
    newlayer = original.copy()
    newlayer.name = str(size)+"x"+str(size)
    image.add_layer(newlayer, 0)
    newlayer.scale(size, size, 1)

register(
        "python_fu_makeicolayers",
        "Create layers for an .ico file",
        "Creates duplicates of the active layer, each scaled to a standard icon size",
        "Jan Singon Slany",
        "Jan Singon Slany",
        "2016",
        "<Image>/Python-Fu/Icons/Make icon layers",
        "RGB*, GRAY*",
        [],
        [],
        plugin_main)

main()