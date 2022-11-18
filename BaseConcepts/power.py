class Power(object):
    """class that computes specific power of other numbers"""
    default_exponent=3

    def __init__(self, exponent=default_exponent):
        self.exponent=exponent

    def calc(self,x):
        return x**self.exponent

class RealPower(Power):
    def calc(self,x):
        if isinstance(self.exponent,int) or x>=0:
            return x**self.exponent
        raise ValueError(f"Fractional powers of negative numbers are imaginary")


print('Power:', Power)
print('Power.default_exponent:', Power.default_exponent)
square = Power()
root = Power(0.5)
print('square: ', square)
print('square.of(3) =', square.calc(3))
print('root.of(3) =', root.calc(3))
#print('root.of(-3) =', root.calc(-3))
real_root = RealPower(0.5)
print('real_root.of(3) =', real_root.calc(3))
print('real_root.of(-3) =', real_root.calc(-3))
print('Done.')