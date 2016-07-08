#!/usr/bin/env python

#
# Creates a new image with duplicates of what is visible in the current image,
# each scaled to a standard icon size.
#

from gimpfu import *

def plugin_main(img, drawable):  
    iconimg = gimp.Image(img.width, img.height, RGB)

    pdb.gimp_undo_push_group_start(iconimg)
    lcopy = pdb.gimp_layer_new_from_visible(img, iconimg, "original")
    
    scale_copy_layer(256, lcopy, iconimg)
    scale_copy_layer(48, lcopy, iconimg)
    scale_copy_layer(32, lcopy, iconimg)
    scale_copy_layer(16, lcopy, iconimg)
    
    # Clean up the new image: discard the copied layer and resize to fit
    #iconimg.remove_layer(lcopy)
    pdb.gimp_image_resize_to_layers(iconimg)
    
    # Display it
    gimp.Display(iconimg)
    gimp.displays_flush()

    pdb.gimp_undo_push_group_end(iconimg)

def scale_copy_layer(size, original, image):
    newlayer = original.copy()
    newlayer.name = str(size)+"x"+str(size)
    image.add_layer(newlayer, 0)
    newlayer.scale(size, size, 1)

register(
        "python_fu_makeico",
        "Create a new image with layers corresponding to standard icon sizes",
        """Create a new image with duplicates of what is visible in the current image,
        each scaled to a standard icon size""",
        "Jan Singon Slany",
        "Jan Singon Slany",
        "2016",
        "<Image>/Python-Fu/Icons/Make icon",
        "RGB*, GRAY*",
        [],
        [],
        plugin_main)

main()