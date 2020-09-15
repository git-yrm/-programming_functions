#The decision is solely for obtaining the result, taking into account the correct type of the passed arguments. (When using the passed arguments specified in the task, an error will not occur and the function will return the required result).
def msPad_1(s,il):
    il=" "*il
    return il+s.replace("\n","\n"+il)
                
#The same function, but with argument checking             
def msPad_2(s=None,il=0):
    if type(s) == str and type(il) == int:
        if il > 0:
            il=" "*il
            return il+s.replace("\n","\n"+il)
        else:
            return s
    else:
            return False


#Assert for a def without cheking arguments msPad_1(), and for a def with checking arguments msPad_2()

assert msPad_1("blah\nblah",4) == "    blah\n    blah"

assert msPad_2("blah\nblah",4) == "    blah\n    blah"


#Edge cases for demo why need to test argument in a def, as in def msPad_2()

values=[
    ["","str",5,[1,2,3,4],"STRTEXT1\nSTRTEXT2\nSTRTEXT3",None,"string number 1\nstring number 2","string"],
    [5,10,4,2,8,6,0,1.6],
    ["     ","          str",False,False,"        STRTEXT1\n        STRTEXT2\n        STRTEXT3",False,"string number 1\nstring number 2",False]
]

for n in range(0,len(values[0])):
    response=msPad_2(values[0][n],values[1][n])
    assert response == values[2][n]
