def a():        # public
    print("I am from test1.py function a")

def b():        # public
    print("I am from test1.py function b")

def _c(_d):     # "private" by convention
    print("private function within test 1")
    _d()

def _d():       # "private" by convention
    print("private function within test 1")

x = 10          # public variable
_y = 20         # "private" variable by convention
