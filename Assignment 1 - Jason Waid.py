from numpy import *
from math import *
from os import *

set_printoptions(precision=4, linewidth=160)

def PrintMatrix(name,x):
 print
 print (name,"=")
 print (x)


# data 

NumData = mat("""10.  68. 58. 125. 82. 80.;
                 45. 175. 73. 121. 78. 68.;
                 35. 156. 63. 115. 70. 82.;
                 18. 210. 75. 123. 81. 90.;
                 51. 145. 64. 135. 83. 85.;
                 63. 131. 66. 155. 91. 65.;
                 27. 182. 71. 142. 85. 73.;
                 28. 125. 60. 118. 75. 70.;
                 75. 219. 72. 151. 88. 91.;
                 77. 158. 68. 140. 92. 75.""")
         
BinaryDataSymm = mat("""0 0 1 1 0 1 0;
                        0 0 0 0 1 0 0;
                        1 0 0 0 0 0 0;
                        0 0 0 0 1 0 0;
                        1 0 0 1 0 1 0;
                        1 1 0 0 0 0 1;
                        0 1 0 0 0 0 0;
                        1 0 0 0 0 0 0;
                        0 1 1 0 1 0 0;
                        0 0 0 0 1 0 0""")
                 
BinaryDataAsymm = mat("""0 1 1 0 1 0;
                         0 0 0 1 0 0;
                         0 0 0 0 0 0;
                         0 0 0 1 0 0;
                         0 0 1 0 1 0;
                         1 0 0 0 0 1;
                         1 0 0 0 0 0;
                         0 0 0 0 0 0;
                         1 1 0 1 0 0;
                         0 0 0 1 0 0""")
                 
OrdinalData = mat("""2. 1. 3. 2. 4.;
                     4. 4. 2. 3. 2.;
                     5. 4. 2. 4. 2.;
                     5. 5. 2. 4. 1.;
                     3. 3. 3. 3. 2.;
                     3. 4. 5. 3. 3.;
                     2. 3. 2. 1. 3.;
                     4. 5. 1. 4. 2.;
                     2. 2. 5. 2. 4.;
                     3. 3. 4. 3. 3.""")
             
NominalData = mat("""4 4 3 3 4;
                     2 2 4 3 1;
                     2 3 4 2 2;
                     1 1 4 3 1;
                     2 2 2 3 2;
                     3 3 1 2 3;
                     3 4 4 3 1;
                     2 1 4 1 4;
                     4 4 1 3 3;
                     3 4 3 3 1""")

#Q1
print("Q1. From Table 1, determine dissimilarity matrices for the numeric data using the following metrics:")

DNumE = mat(zeros((10,10)))
DNumM = mat(zeros((10,10)))
DNumMax = mat(zeros((10,10)))
DMax = mat(zeros((6,1)))
for i in range(10):
    for j in range(10):
        for k in range(6):
            DNumE[i,j] = DNumE[i,j] + (NumData[i,k]-NumData[j,k])**2.0
            DNumM[i,j] = DNumM[i,j] + abs(NumData[i,k]-NumData[j,k])
            DMax[k] = abs(NumData[i,k]-NumData[j,k])
        DNumE[i,j] = (DNumE[i,j])**0.5
        DNumMax[i,j] = max(DMax)


PrintMatrix("(a) Euclidean",DNumE)
PrintMatrix("(b) Manhattan",DNumM)
PrintMatrix("(c) Supremum",DNumMax)


#Q2
print("Q2. From Table 1, determine dissimilarity matrices for the binary data:")

DBinSymm = mat(zeros((10,10)))
for i in range(10):
    for j in range(10):
        for k in range(7):
            DBinSymm[i,j] = DBinSymm[i,j] + int(BinaryDataSymm[i,k]==BinaryDataSymm[j,k])
        DBinSymm[i,j] = (7-DBinSymm[i,j])/7.0;

PrintMatrix("(a) Assuming that all of the attributes are symmetric (Y and N are equally important)",DBinSymm)

DBinAsymm = mat(zeros((10,10)))
for i in range(10):
    for j in range(10):
        unimportant = 0
        for k in range(6):
            DBinAsymm[i,j] = DBinAsymm[i,j] + int(BinaryDataAsymm[i,k]==BinaryDataAsymm[j,k])
            unimportant = unimportant + (BinaryDataAsymm[i,k]&BinaryDataAsymm[j,k])
        DBinAsymm[i,j] = (6-DBinAsymm[i,j])/(6-unimportant);

PrintMatrix("(b) Assuming that all of the attributes are asymmetric (where we consider Y to be unimportant)",DBinAsymm)

#Q3
print("Q3. From Table 1, determine a dissimilarity matrix for the entire table, (assuming that the binary attributes are symmetric and that we used a Manhattan distance for numeric data).")
DNumM = mat(zeros((10,10)))
for i in range(10):
    for j in range(10):
        for k in range(6):
            DNumM[i,j] = DNumM[i,j] + abs(NumData[i,k]-NumData[j,k])/(6.0*(max(NumData[:,k]) - min(NumData[:,k])))

DTotalQ3 = (7.0*DBinSymm + 6.0*DNumM)/13.0

PrintMatrix("Total Distance Table 1",DTotalQ3)

#Q4
print("Q4. From Table 2, determine a dissimilarity matrix for ordinal data (assume that the first 5 columns are ordinal).")
Mf = tile(mat("4. 4. 4. 3. 3."),(10,1))
OrdData = (OrdinalData-1) / Mf
DOrdE = mat(zeros((10,10)))
DOrdM = mat(zeros((10,10)))
DOrdMax = mat(zeros((10,10)))
DMax = mat(zeros((5,1)))
for i in range(10):
    for j in range(10):
        for k in range(5):
            DOrdE[i,j] = DOrdE[i,j] + (OrdData[i,k]-OrdData[j,k])**2.0
            DOrdM[i,j] = DOrdM[i,j] + abs(OrdData[i,k]-OrdData[j,k])
            DMax[k] = abs(OrdData[i,k]-OrdData[j,k])
        DOrdE[i,j] = (DOrdE[i,j])**0.5
        DOrdMax[i,j] = max(DMax);

PrintMatrix("Ordinal Euclidean Distance",DOrdE)
PrintMatrix("Ordinal Manhattan Distance",DOrdM)
PrintMatrix("Ordinal Supremum Distance",DOrdMax)

#Q5
print("Q5. From Table 2, determine a dissimilarity matrix for nominal data (assume that the last 5 columns are nominal).")
DNom = mat(zeros((10,10)))
for i in range(10):
    for j in range(10):
        for k in range(5):
            DNom[i,j] = DNom[i,j] + int(NominalData[i,k]==NominalData[j,k])
        DNom[i,j] = (5-DNom[i,j])/5.0;

PrintMatrix("Nominal Distance",DNom)

#Q6
print("Q6. From Table 2, determine a dissimilarity matrix for the entire table (under the same assumptions as for Q4 and Q5).")

Mf = tile(mat("4. 4. 4. 3. 3."),(10,1))
OrdData = (OrdinalData-1)/Mf;
DOrdM = mat(zeros((10,10)))
for i in range(10):
    for j in range(10):
        for k in range(5):
            DOrdM[i,j] = DOrdM[i,j] + abs(OrdData[i,k]-OrdData[j,k])/(5.0*(max(OrdData[:,k]) - min(OrdData[:,k])))


DTotalQ6 = (5.0*DNom + 5.0*DOrdM)/10.0

PrintMatrix("Total Distance Table 2",DTotalQ6)

#Q7
print("Q7. For the combination of both tables, determine a dissimilarity matrix (under the assumptions given in Q3, Q4 and Q5).")

DTotal = (13.0*DTotalQ3 + 10.0*DTotalQ6)/23.0

PrintMatrix("Total Distance Both Tables",DTotal)

system("pause")

