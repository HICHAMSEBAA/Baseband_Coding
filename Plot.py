import matplotlib.pyplot as plt
import numpy as np


class Plot:

    def __int__(self):
        pass

    @staticmethod
    def Convert_array(Data):
        Data = list(map(lambda a: eval(a), Data.split()))
        bit = Data[0]
        Data.insert(0, bit)
        return np.array(Data)

    @staticmethod
    def Visualization(Data, title):
        plt.plot(Plot.Convert_array(Data))
        plt.title(title)
        plt.xlabel("Time")
        plt.ylabel("Voltage")
        plt.grid()
        plt.show()

    @staticmethod
    def Visualization_(Data, Code, Title1, Title2):
        code, test = Code
        # plot 1
        plt.subplot(2, 1, 1)
        Data = Plot.Convert_array(Data)
        T = np.arange(0, len(Data))
        plt.step(T, Data, color='b')
        plt.title(Title1)
        plt.xlabel("Time(s)")
        plt.xlim(0)
        plt.ylabel("Binary")
        plt.grid()
        # plot 2
        if test:
            plt.subplot(2, 1, 2)
            T = np.arange(0, len(code))
            plt.step(T, code, color='r')
            plt.title(Title2)
            plt.xlabel("Time(s)")
            plt.xlim(0)
            plt.ylabel("Voltage")
            plt.grid()
        else:
            plt.subplot(2, 1, 2)
            T = np.arange(0, len(Data) - 0.5, 0.5)
            plt.step(T, code, color='r')
            plt.title(Title2)
            plt.xlabel("Time(s)")
            plt.xlim(0)
            plt.ylabel("Voltage")
            plt.grid()

        plt.show()
