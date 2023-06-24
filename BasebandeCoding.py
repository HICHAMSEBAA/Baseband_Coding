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
        FIRST_BIT = True
        for bit in Coding.Convert_list(Data):
            if bit == 1:
                if FIRST_BIT:
                    NRZ_CODE.append(-5)
                    FIRST_BIT = False
                NRZ_CODE.append(-5)
            else:
                if FIRST_BIT:
                    NRZ_CODE.append(5)
                    FIRST_BIT = False
                NRZ_CODE.append(5)
        return np.array(NRZ_CODE)

    @staticmethod
    def RZ(Data):
        # 1 = 5v / 0 = -5v
        RZ_CODE = []
        FIRST_BIT = True
        for bit in Coding.Convert_list(Data):
            if bit == 1:
                if FIRST_BIT:
                    RZ_CODE.append(5)
                    FIRST_BIT = False
                RZ_CODE.append(5)
                RZ_CODE.append(0)
            else:
                if FIRST_BIT:
                    RZ_CODE.append(5)
                    FIRST_BIT = False
                RZ_CODE.append(-5)
                RZ_CODE.append(0)
        return np.array(RZ_CODE)

    @staticmethod
    def NRZI(Data):
        NRZI = []
        BIT = 5
        FIRST_BIT = True
        for bit in Coding.Convert_list(Data):
            if bit == 1:
                if FIRST_BIT:
                    NRZI.append(BIT)
                    FIRST_BIT = False
                NRZI.append(BIT)
            else:
                if FIRST_BIT:
                    NRZI.append(BIT)
                    FIRST_BIT = False
                NRZI.append(-BIT)
                BIT = -BIT
        return NRZI

    @staticmethod
    def Manchester(Data):
        Manchester = []
        FIRST_BIT = True
        for bit in Coding.Convert_list(Data):
            if bit == 1:
                if FIRST_BIT:
                    Manchester.append(5)
                    FIRST_BIT = False
                Manchester.append(5)
                Manchester.append(0)
            else:
                if FIRST_BIT:
                    Manchester.append(0)
                    FIRST_BIT = False
                Manchester.append(0)
                Manchester.append(5)
        return Manchester

    @staticmethod
    def Differential_Manchester(Data):
        Manchester_D = []
        FIRST_BIT = True
        for bit in Coding.Convert_list(Data):
            if bit == 1:
                if FIRST_BIT:
                    Manchester_D.append(5)
                    Manchester_D.append(5)
                    Manchester_D.append(0)
                    FIRST_BIT = False
                else:
                    if Manchester_D[len(Manchester_D) - 1] == 5:
                        Manchester_D.append(5)
                        Manchester_D.append(0)
                    else:
                        Manchester_D.append(0)
                        Manchester_D.append(5)
            else:
                if FIRST_BIT:
                    Manchester_D.append(5)
                    Manchester_D.append(0)
                    Manchester_D.append(5)
                    FIRST_BIT = False
                else:
                    if Manchester_D[len(Manchester_D) - 1] == 5:
                        Manchester_D.append(0)
                        Manchester_D.append(5)
                    else:
                        Manchester_D.append(5)
                        Manchester_D.append(0)
        return Manchester_D

    @staticmethod
    def MILLER(Data):
        MILLER = []
        DATA = Coding.Convert_list(Data)
        FIRST_BIT = True
        for i in range(len(DATA)):
            if DATA[i] == 1:
                if FIRST_BIT:
                    MILLER.append(5)
                    MILLER.append(5)
                    MILLER.append(0)
                    FIRST_BIT = False
                else:
                    if MILLER[len(MILLER) - 1] == 5:
                        MILLER.append(5)
                        MILLER.append(0)
                    else:
                        MILLER.append(0)
                        MILLER.append(5)
            else:
                if FIRST_BIT:
                    MILLER.append(0)
                    MILLER.append(0)
                    MILLER.append(0)
                    FIRST_BIT = False
                else:
                    if DATA[i - 1] == 1:
                        if MILLER[len(MILLER) - 1] == 5:
                            MILLER.append(5)
                            MILLER.append(5)
                        else:
                            MILLER.append(0)
                            MILLER.append(0)
                    else:
                        if MILLER[len(MILLER) - 1] == 0:
                            MILLER.append(5)
                            MILLER.append(5)
                        else:
                            MILLER.append(0)
                            MILLER.append(0)
        return MILLER

