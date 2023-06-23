import numpy as np


class Coding:

    def __int__(self):
        pass

    @staticmethod
    def Convert_list(Data):
        return list(map(lambda a: eval(a), Data.split()))

    @staticmethod
    def NRZ(Data):
        # 1 = -5v / 0 = 5v
        NRZ_CODE = []
        for bit in Coding.Convert_list(Data):
            if bit == 1:
                NRZ_CODE.append(-5)
            else:
                NRZ_CODE.append(5)

        return np.array(NRZ_CODE)

    @staticmethod
    def RZ(Data):
        RZ_CODE = []
        for bit in Coding.Convert_list(Data):
            if bit == 1:
                RZ_CODE.append(5)
                RZ_CODE.append(0)
            else:
                RZ_CODE.append(-5)
                RZ_CODE.append(0)
        return np.array(RZ_CODE)

    @staticmethod
    def NRZI(Data):
        pass
