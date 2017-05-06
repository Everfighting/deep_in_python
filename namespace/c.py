v1 = 'a global var'

def func(v):
    v2 = 'a local var'
    def inn_func():
        v3 = v2 + v
        return v3
    return inn_func