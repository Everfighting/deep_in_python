gv = ['a','global','var']

def func(v):
    global gv
    gv = ['gv'] + gv
    lv = []
    print()