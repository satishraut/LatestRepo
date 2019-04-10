class Dept:
    def __init__(self,dcode,dnm,dprof):
        self.dname=dnm
        self.dcode=dcode
        self.dprof=dprof

    def __str__(self):
        return f'{self.__dict__}'

    def __repr__(self):
        return str(self)