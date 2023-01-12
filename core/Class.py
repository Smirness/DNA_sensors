from na_tools import na_tools
from na_tools.tp_dna import *
from na_tools.gc import *
import sys


class Analyte:
    """ The class stores information about Analyte"""

    def __init__(self, sequence, conc_analyte, conc_salt, conc_mg, temp):
        self.sequence = sequence
        self.conc_analyte = int(conc_analyte)
        self.conc_salt = int(conc_salt)
        self.conc_mg = int(conc_mg)
        self.temp = int(temp)
        self.tm_parameter = 'all'
        self.unit = 'kcal'
        self.length = len(self.sequence)
        self.gc = gc(self.sequence)
        self.Tm_duplex, self.dG_duplex, self.dH_duplex, self.dS_duplex = \
            dna_hybr(self.sequence, self.conc_analyte, self.conc_salt, self.conc_mg, self.temp,
                     tm_parameter=self.tm_parameter, unit=self.unit)


class Dnsorder:
    """ The class stores parameters about DNA-sensors"""
   # linkers
    linker = {"HEG": '/HEG/',
              '6T': 'TTTTTT'}
    # scaffolding sequence. The second sequence is created automatically
    scaffold = {'G4_1': 'CGTACTAATCTAATCATATCTACTATATCATGC',
                'Dz_1': 'GCAGACTACTGTCACCTGACGTAC',
                }
    scaffold['G4_2'] = na_tools.reverse_complement(scaffold['G4_1'])
    scaffold['Dz_2'] = na_tools.reverse_complement(scaffold['Dz_1'])

    # cores and arms for substrate
    G4 = 'GGGTTGGG'
    Dza = 'TGCCCAGGG AGGCTAGCT'
    Dzb = 'ACAACGA GAGGAAACCTT'

    def __init__(self, analyte, position, len_arm1, len_arm2, len_arm3, len_arm4, type_core, variant, linker):

        self.analyte = analyte
        self.position = int(position)
        self.len_arm1 = int(len_arm1)
        self.len_arm2 = int(len_arm2)
        self.len_arm3 = int(len_arm3)
        self.len_arm4 = int(len_arm4)
        self.type_core = type_core
        self.variant = int(variant)
        self.linker = Dnsorder.linker[linker]

        if self.len_arm3 != 0 and self.len_arm4 == 0:
            self.arms = 3
        elif self.len_arm3 != 0 and self.len_arm4 != 0:
            self.arms = 4
        else:
            self.arms = 2

    def check_len_arms(self):
        """checking length of arms"""
        if self.arms == 2:
            if self.len_arm1 > self.position:
                print('1st arm length is longer than analyte region')
                sys.exit(0)
            elif self.len_arm2 > (len(self.analyte) - self.position):
                print('2nd arm length is longer than analyte region')
                sys.exit(0)

        elif self.arms == 3 and self.variant == 3:
            if self.len_arm1 > self.position:
                print('1st arm length is longer than analyte region')
                sys.exit(0)
            elif (self.len_arm2 + self.len_arm3) > (len(self.analyte) - self.position):
                print('Arms (2nd and/or 3rd) length is longer than analyte region')
                sys.exit(0)

        elif self.arms == 3 and self.variant == 5:
            if (self.len_arm1 + self.len_arm2) > self.position:
                print('Arms (1st and/or 2nd) length is longer than analyte region')
                sys.exit(0)
            elif self.len_arm3 > (len(self.analyte) - self.position):
                print('3rd arm length is longer than analyte region')
                sys.exit(0)

        elif self.arms == 4:
            if (self.len_arm1 + self.len_arm2) > self.position:
                print('Arms (1st and/or 2nd) length is longer than analyte region')
                sys.exit(0)
            elif (self.len_arm3 + self.len_arm4) > (len(self.analyte) - self.position):
                print('Arms (3st and/or 4nd) length is longer than analyte region')
                sys.exit(0)

    def seq_sensor(self):
        """The choice of method depends on the number of arms"""
        # checking length of arms
        self.check_len_arms()

        # run one of methods
        if self.arms == 2:
            method = self.twoarms()
        elif self.arms == 3:
            method = self.threearms()
        elif self.arms == 4:
            method = self.fourarms()

        return method

    def twoarms(self):
        analyte_r1 = list(self.analyte)[self.position - self.len_arm1:self.position]
        analyte_r2 = list(self.analyte)[self.position:self.position + self.len_arm2]

        analyte_r1 = "".join(analyte_r1)
        analyte_r2 = "".join(analyte_r2)

        arm1 = na_tools.reverse_complement(analyte_r1)
        arm2 = na_tools.reverse_complement(analyte_r2)

        if self.type_core == "G4":
            seq_sensor1 = ' '.join([Dnsorder.G4, self.linker, arm1])
            seq_sensor2 = ' '.join([arm2, self.linker, Dnsorder.G4])

        elif self.type_core == "Dz":
            seq_sensor1 = ' '.join([Dnsorder.Dza, self.linker, arm1])
            seq_sensor2 = ' '.join([arm2, self.linker, Dnsorder.Dzb])

        return arm1, arm2, seq_sensor1, seq_sensor2

    def threearms(self):

        if self.variant == 5:
            analyte_r1 = list(self.analyte)[self.position - self.len_arm2 - self.len_arm1:self.position - self.len_arm2]
            analyte_r2 = list(self.analyte)[self.position - self.len_arm2:self.position]
            analyte_r3 = list(self.analyte)[self.position:self.position + self.len_arm3]

        elif self.variant == 3:
            analyte_r1 = list(self.analyte)[self.position - self.len_arm1:self.position]
            analyte_r2 = list(self.analyte)[self.position:self.position + self.len_arm2]
            analyte_r3 = list(self.analyte)[self.position + self.len_arm2:self.position + self.len_arm2 + self.len_arm3]

        analyte_r1 = "".join(analyte_r1)
        analyte_r2 = "".join(analyte_r2)
        analyte_r3 = "".join(analyte_r3)

        arm1 = na_tools.reverse_complement(analyte_r1)
        arm2 = na_tools.reverse_complement(analyte_r2)
        arm3 = na_tools.reverse_complement(analyte_r3)

        if self.type_core == "G4":
            print("You can create a G-quadruplex-based sensor with two or four arms.")
            sys.exit(0)

        elif self.type_core == "Dz":
            if self.variant == 5:
                seq_sensor1 = ' '.join([Dnsorder.Dza, arm2, self.linker, Dnsorder.scaffold['Dz_2']])
                seq_sensor2 = ' '.join([arm3, Dnsorder.Dzb])
                seq_sensor3 = ' '.join([arm1, self.linker, Dnsorder.scaffold['Dz_1']])

            elif self.variant == 3:
                seq_sensor1 = ' '.join([Dnsorder.Dza, arm1])
                seq_sensor2 = ' '.join([Dnsorder.scaffold['Dz_2'], self.linker, arm2, Dnsorder.Dzb])
                seq_sensor3 = ' '.join([arm3, self.linker, Dnsorder.scaffold['Dz_1']])

            return arm1, arm2, arm3, seq_sensor1, seq_sensor2, seq_sensor3

    def fourarms(self):
        analyte_r1 = list(self.analyte)[self.position - self.len_arm2 - self.len_arm1:self.position - self.len_arm2]
        analyte_r2 = list(self.analyte)[self.position - self.len_arm2:self.position]
        analyte_r3 = list(self.analyte)[self.position:self.position + self.len_arm3]
        analyte_r4 = list(self.analyte)[self.position + self.len_arm3:self.position + self.len_arm3 + self.len_arm4]

        analyte_r1 = "".join(analyte_r1)
        analyte_r2 = "".join(analyte_r2)
        analyte_r3 = "".join(analyte_r3)
        analyte_r4 = "".join(analyte_r4)

        arm1 = na_tools.reverse_complement(analyte_r1)
        arm2 = na_tools.reverse_complement(analyte_r2)
        arm3 = na_tools.reverse_complement(analyte_r3)
        arm4 = na_tools.reverse_complement(analyte_r4)

        if self.type_core == "G4":
            seq_sensor1 = ' '.join([Dnsorder.G4, self.linker, arm2])
            seq_sensor2 = ' '.join([Dnsorder.scaffold['G4_1'], self.linker, arm3, self.linker, Dnsorder.G4])
            seq_sensor3 = ' '.join([arm4, self.linker, self.scaffold['G4_2'], self.linker, arm1])
            return arm1, arm2, arm3, arm4, seq_sensor1, seq_sensor2, seq_sensor3

        elif self.type_core == "Dz":
            print("You can create a DNAzyme-based sensor with three arms.")
            sys.exit(0)


class Dnsorder_tp:
    def __init__(self, arms, arm1, arm2, conc_seq, conc_salt, conc_mg, temp, arm3=0, arm4=0):
        tm_parameter = 'all'
        unit = 'kcal'
        self.arms = int(arms)

        if self.arms == 2:
            self.arm1_Tm, self.arm1_dG, self.arm1_dH, self.arm1_dS = dna_hybr(primer_seq=arm1, conc_primer=conc_seq,
                                                                              conc_salt=conc_salt, conc_mg=conc_mg,
                                                                              temp=temp, tm_parameter=tm_parameter,
                                                                              unit=unit)
            self.arm2_Tm, self.arm2_dG, self.arm2_dH, self.arm2_dS = dna_hybr(primer_seq=arm2, conc_primer=conc_seq,
                                                                              conc_salt=conc_salt, conc_mg=conc_mg,
                                                                              temp=temp, tm_parameter=tm_parameter,
                                                                              unit=unit)

        elif self.arms == 3:
            self.arm1_Tm, self.arm1_dG, self.arm1_dH, self.arm1_dS = dna_hybr(primer_seq=arm1, conc_primer=conc_seq,
                                                                              conc_salt=conc_salt, conc_mg=conc_mg,
                                                                              temp=temp, tm_parameter=tm_parameter,
                                                                              unit=unit)
            self.arm2_Tm, self.arm2_dG, self.arm2_dH, self.arm2_dS = dna_hybr(primer_seq=arm2, conc_primer=conc_seq,
                                                                              conc_salt=conc_salt, conc_mg=conc_mg,
                                                                              temp=temp, tm_parameter=tm_parameter,
                                                                              unit=unit)
            self.arm3_Tm, self.arm3_dG, self.arm3_dH, self.arm3_dS = dna_hybr(primer_seq=arm3, conc_primer=conc_seq,
                                                                              conc_salt=conc_salt, conc_mg=conc_mg,
                                                                              temp=temp, tm_parameter=tm_parameter,
                                                                              unit=unit)

        elif self.arms == 4:
            self.arm1_Tm, self.arm1_dG, self.arm1_dH, self.arm1_dS = dna_hybr(primer_seq=arm1, conc_primer=conc_seq,
                                                                              conc_salt=conc_salt, conc_mg=conc_mg,
                                                                              temp=temp, tm_parameter=tm_parameter,
                                                                              unit=unit)
            self.arm2_Tm, self.arm2_dG, self.arm2_dH, self.arm2_dS = dna_hybr(primer_seq=arm2, conc_primer=conc_seq,
                                                                              conc_salt=conc_salt, conc_mg=conc_mg,
                                                                              temp=temp, tm_parameter=tm_parameter,
                                                                              unit=unit)
            self.arm3_Tm, self.arm3_dG, self.arm3_dH, self.arm3_dS = dna_hybr(primer_seq=arm3, conc_primer=conc_seq,
                                                                              conc_salt=conc_salt, conc_mg=conc_mg,
                                                                              temp=temp, tm_parameter=tm_parameter,
                                                                              unit=unit)
            self.arm4_Tm, self.arm4_dG, self.arm4_dH, self.arm4_dS = dna_hybr(primer_seq=arm4, conc_primer=conc_seq,
                                                                              conc_salt=conc_salt, conc_mg=conc_mg,
                                                                              temp=temp, tm_parameter=tm_parameter,
                                                                              unit=unit)
