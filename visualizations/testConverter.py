import decimal
import math
from sat_act_conv import *

def SATcompToACTread(value):
    return sat_to_act_read(value)

def SATmathToACTmath(value):
    return sat_to_act_math(value)

def SATwritToACTwrit(value):
    return sat_to_act_writing(value)

def SATtotalToACTtotal(value):
    return value

def ACTreadToSATcomp(value):
    return act_to_sat_read(value)

def ACTmathToSATmath(value):
    return act_to_sat_math(value)

def ACTwritToSATwrit(value):
    return act_to_sat_writing(value)

def ACTtotalToSATtotal(value):
    return value