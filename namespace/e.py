gv = ['a','global', 'var']

def func(v):
    gv = ['gv'] + gv
    lv = []
    def inn_func():
        lv = lv + [v]
        gv.insert(1,1v[0])
        return gv
    return inn_func