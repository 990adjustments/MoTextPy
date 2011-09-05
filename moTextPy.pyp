"""
moTextPy.pyp

Author: Erwin Santacruz
www.990adjustments.com

Written for CINEMA 4D R12

Name-US: MoTextPy


Description-US: This is a simple Cinema 4D python script that is meant to be used on a
python tag. Just add a python tag to your MoText object and paste the
script into the code field of the tag. You can then save the tag as a
preset or save the MoText object with the tag as a default.
import c4d.

The script just links together a few of the Motext object's parameters.
Specifically, the text field is linked to the MoText object name, the star cap to
the end cap, the start steps to the end steps, and start radius to the end radius.

Creation Date: 06.04.11

"""

import c4d

def main():
    obj = op.GetObject()
    obj[c4d.ID_BASELIST_NAME] = obj[c4d.PRIM_TEXT_TEXT]
    obj[c4d.CAP_END] = obj[c4d.CAP_START]
    obj[c4d.CAP_ENDSTEPS] = obj[c4d.CAP_STARTSTEPS]
    obj[c4d.CAP_ENDRADIUS] = obj[c4d.CAP_STARTRADIUS]
