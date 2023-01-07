def len_analyte(analyte):
    print(len(analyte))

analyte = "AATGCAACGCCAGCTGCTAAAGTATTAGTAGAAGGTAACACT"

arms = 4
len_arm1 = 10
len_arm2 = 10
len_arm3 = 10
len_arm4 = 10
position = len(analyte)//2

if arms == 4:

    analyte_r1 = list(analyte)[position-len_arm2-len_arm1:position-len_arm2]
    analyte_r2 = list(analyte)[position-len_arm2:position]
    analyte_r3 = list(analyte)[position:position+len_arm3]
    analyte_r4 = list(analyte)[position+len_arm3:position+len_arm3+len_arm4]

    analyte_r1 = "".join(analyte_r1)
    analyte_r2 = "".join(analyte_r2)
    analyte_r3 = "".join(analyte_r3)
    analyte_r4 = "".join(analyte_r2)

print(analyte)
print(analyte_r1, analyte_r2,  analyte_r3, analyte_r4)