from Plot import Plot
from BasebandeCoding import Coding


def switch(ID):
    title = "Data"
    if ID == 1:
        Plot.Visualization_(Data, Coding.NRZ(Data), title, "NRZ Code")
    elif ID == 2:
        Plot.Visualization_(Data, Coding.RZ(Data), title, "RZ Code")
    elif ID == 3:
        Plot.Visualization_(Data, Coding.NRZI(Data), title, "NRZI Code")
    elif ID == 4:
        Plot.Visualization_(Data, Coding.Manchester(Data), title, "Manchester Code")
    elif ID == 5:
        Plot.Visualization_(Data, Coding.Differential_Manchester(Data), title, "Differential Manchester Code")
    elif ID == 6:
        Plot.Visualization_(Data, Coding.MILLER(Data), title, "Miller Code")
    else:
        print("ERROR")


print("+++++++++++++++++++ Base Band Coding Types +++++++++++++++++++++")
print(" 1 --> NRZ")
print(" 2 --> RZ")
print(" 3 --> NRZI")
print(" 4 --> Manchester")
print(" 5 --> Differential_Manchester")
print(" 6 --> MILLER")
code_id = int(input("Choice One Of This Code  : "))
Data = str(input("Enter Your Binary Sequence : "))

switch(code_id)


