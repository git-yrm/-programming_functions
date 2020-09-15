def multimaxvalue(arr):
    if isinstance(arr, list):
        arr=list(set(filter(lambda v: isinstance(v, int) and v > 0, arr)))
        if len(arr) >= 2:
            vm=max(arr)
            arr.remove(vm)
            pvm=max(arr)
            return vm*pvm
        else:
            return False
    else:
        return False

#Assert
assert multimaxvalue([14,33,24,56,500.5,480,300,480,88]) == 300*480


#edge cases
arrays=[
    [
        [50,60,10,33,56,99,4,1000.5],
        [10,6,7,3,50.6,50,60,60,60.5],
        [-5,-10,100],
        [-10,10.5,50.5,-30],
        [-1,-2,10,20,500.4,400.8,13],
        ["t","e","x","t"],
        ["t","e","x","t",1,2,3,4,5,5,6,6,6],
        100,
        "text"
    ],
     [60*99,50*60,False,False,20*13,False,5*6,False,False]   
]

for n in range(0,len(arrays[0])):
    assert multimaxvalue(arrays[0][n]) == arrays[1][n]
    
