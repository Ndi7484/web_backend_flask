import numpy as np
import pandas as pd
def numpTest():
    arr = np.array([[1,2,3],[4,5,6]])
    arr2=np.ones(5)
    return [
        {
            "type":"numpy",
            "text": str(arr),
            "text2": str(arr2),
            "arr":[1,2,3,4,5]
        }
    ]

def pandTest():
    data ={
        "name_lengkap_bud":['Andy','Budi',"Cind"],
        "cls_n":['XIA','XA','VIIA'],
        "aging":[12,13,14],
    }
    return [
        {
            "type":"pandas",
            "text":str(pd.DataFrame(data))
        }
    ]