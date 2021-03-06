# -*- coding: utf-8 -*-
"""
This module contains utils and classes for X-ray wavefront propagation. The most propagation methods based on SRW library.

.. module:: wpg
   :platform: Linux, Mac OSX, Windows

.. moduleauthor:: Alexey Buzmakov <buzmakov@gmail.com>
"""

import warnings

#This deprecate warnings form SRWLib visualization module 
warnings.filterwarnings("ignore")
import srwlib
warnings.resetwarnings()

#Create aliases for simple importing
from wavefront import Wavefront
from beamline import Beamline
from glossary import print_glossary