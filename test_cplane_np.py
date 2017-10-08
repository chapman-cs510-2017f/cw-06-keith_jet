'''
test each methods in the class of cplane 
check the expect setting/output equal the result
'''

import cplane_np as cn
from cplane_np import ArrayComplexPlane as ACP
import numpy as np
#from cplane import doubleplane 


def test_init():
    CP = ACP(1,4,3,2,5,3)
    expVal = np.array([[(1+2j), (2.5+2j), (4+2j)], [(1+3.5j), (2.5+3.5j), (4+3.5j)], [(1+5j), (2.5+5j), (4+5j)]])
    boolCmpArray = (expVal == CP.plane) # get a boolean array which shows true/flase for the comparsion of each element
    assert boolCmpArray.all()
    
def test_refresh():
    CP = ACP(1,4,3,2,5,3)
    CP.apply(cn.doubleplane)
    CP.apply(cn.powerplane)
    CP.refresh()
    expVal = np.array([[(1+2j), (2.5+2j), (4+2j)], [(1+3.5j), (2.5+3.5j), (4+3.5j)], [(1+5j), (2.5+5j), (4+5j)]])
    boolCmpArray = (expVal == CP.plane) # get a boolean array which shows true/flase for the comparsion of each element
    assert boolCmpArray.all()
    
def test_apply():
    CP = ACP(1,4,3,2,5,3)
    CP.apply(cn.doubleplane)
    expVal = np.array([[(2+4j), (5+4j), (8+4j)], [(2+7j), (5+7j), (8+7j)], [(2+10j), (5+10j), (8+10j)]])
    boolCmpArray = (expVal == CP.plane) # get a boolean array which shows true/flase for the comparsion of each element
    assert boolCmpArray.all()

def test_zoom():
    CP = ACP(1,4,3,2,5,3)
    CP.apply(cn.doubleplane)
    CP.apply(cn.powerplane)
    CP.zoom(1,4,3,2,5,3)
    expVal = np.array([[(-12+16j), (9+40j), (48+64j)], [(-45+28j), (-24+70j), (15+112j)], [(-96+40j), (-75+100j), (-36+160j)]])
    boolCmpArray = (expVal == CP.plane) # get a boolean array which shows true/flase for the comparsion of each element
    assert boolCmpArray.all()
                       
