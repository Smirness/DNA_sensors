#!/usr/bin/env python3

from core.Class import *
from dataframe_working.output_file import *
import argparse

parser = argparse.ArgumentParser(prog='DNsorder', description="DNsorder (DNA-sensor builder) is an application enabling\
                                             the in situ choice and assembly DNA-sensors based on 10-23 DNAzyme or G-quadruplex.")
parser.add_argument("-a", "--analyte", help="analyte sequence", required=True)
parser.add_argument("-p", "--position", help="sensor position", required=False)
parser.add_argument("-l1", "--len_arm1", help="length of 1st sensor arm", required=False)
parser.add_argument("-l2", "--len_arm2", help="length of 2nd sensor arm", required=False)
parser.add_argument("-l3", "--len_arm3", help="length of 3rd sensor arm", required=False, default="0")
parser.add_argument("-l4", "--len_arm4", help="length of 4th sensor arm", required=False, default="0")
parser.add_argument("-c_arm", "--conc_arms", help="arms concentration in nM", required=False)
parser.add_argument("-tc", "--type_core", help="type sensor core (Dz or G4)", required=False)
parser.add_argument("-lin", "--linker", help="sensor linker (HEG or 6T)", required=False, default="HEG")
parser.add_argument("-var", "--variant",
                    help="Variant for 3 arms sensor. Adding an arm closer to the 5' or 3' ends of the position. Default = 3",
                    required=False, default="3")
parser.add_argument("-c_a", "--conc_analyte", help="analyte concentration in nM", required=False)
parser.add_argument("-c_s", "--conc_salt", help="salt concentration in mM", required=False)
parser.add_argument("-c_m", "--conc_mg", help="Mg2+ concentration in mM", required=False)
parser.add_argument("-t", "--temp", help="temperature of solution,ºC", required=False)
parser.add_argument("-o", "--output", help="output folder", required=False, default="./")
parser.add_argument("-s", "--save", help="save result (analyte; arms; all)", required=True)
parser.add_argument('-version', action='version', version='%(prog)s 1.0')

args = parser.parse_args()

# the designation of variables from the command
analyte = args.analyte
position = args.position
len_arm1 = args.len_arm1
len_arm2 = args.len_arm2
len_arm3 = args.len_arm3
len_arm4 = args.len_arm4
conc_arms = args.conc_arms
type_core = args.type_core
variant = args.variant
linker = args.linker
conc_analyte = args.conc_analyte
conc_salt = args.conc_salt
conc_mg = args.conc_mg
temp = args.temp
output_dir = args.output
save = args.save

# Сreating analyte object
analyte_obj = Analyte(analyte, conc_analyte, conc_salt, conc_mg, temp)

# Defining parameters into a variable
param_analyte = [analyte_obj.length, analyte_obj.gc, analyte_obj.Tm_duplex,
                 analyte_obj.dG_duplex, analyte_obj.dH_duplex, analyte_obj.dS_duplex]
param_reaction = [analyte_obj.conc_analyte, analyte_obj.conc_salt, analyte_obj.conc_mg, analyte_obj.temp]

# Creating dnasensor object
dnasensor_obj = Dnsorder(analyte_obj.sequence, position, len_arm1, len_arm2, len_arm3, len_arm4, type_core, variant, linker)

# calculate thermodynamic parameters for duplex arm/analyte
if dnasensor_obj.arms == 2:
       arm1, arm2, seq_sensor1, seq_sensor2 = dnasensor_obj.seq_sensor()
       dnasensor_tp_obj = Dnsorder_tp(arms=dnasensor_obj.arms, arm1=arm1, arm2=arm2,  conc_seq=conc_arms,
                                      conc_salt=conc_salt, conc_mg=conc_mg, temp=temp)
       # Defining parameters into a variable
       seq_arms = [arm1, arm2]
       seq_sensor = [seq_sensor1, seq_sensor2]
       arms_Tm = [dnasensor_tp_obj.arm1_Tm, dnasensor_tp_obj.arm2_Tm]
       arms_dG = [dnasensor_tp_obj.arm1_dG, dnasensor_tp_obj.arm2_dG]
       arms_dH = [dnasensor_tp_obj.arm1_dH, dnasensor_tp_obj.arm2_dH]
       arms_dS = [dnasensor_tp_obj.arm1_dS, dnasensor_tp_obj.arm2_dS]

elif dnasensor_obj.arms == 3:
       arm1, arm2, arm3, seq_sensor1, seq_sensor2, seq_sensor3 = dnasensor_obj.seq_sensor()
       dnasensor_tp_obj = Dnsorder_tp(arms=dnasensor_obj.arms, arm1=arm1, arm2=arm2, arm3=arm3, conc_seq=conc_arms,
                                      conc_salt=conc_salt, conc_mg=conc_mg, temp=temp)
       # Defining parameters into a variable
       seq_arms = [arm1, arm2, arm3]
       seq_sensor = [seq_sensor1, seq_sensor2, seq_sensor3]
       arms_Tm = [dnasensor_tp_obj.arm1_Tm, dnasensor_tp_obj.arm2_Tm, dnasensor_tp_obj.arm3_Tm]
       arms_dG = [dnasensor_tp_obj.arm1_dG, dnasensor_tp_obj.arm2_dG, dnasensor_tp_obj.arm3_dG]
       arms_dH = [dnasensor_tp_obj.arm1_dH, dnasensor_tp_obj.arm2_dH, dnasensor_tp_obj.arm3_dH]
       arms_dS = [dnasensor_tp_obj.arm1_dS, dnasensor_tp_obj.arm2_dS, dnasensor_tp_obj.arm3_dS]

elif dnasensor_obj.arms == 4:
       arm1, arm2, arm3, arm4, seq_sensor1, seq_sensor2, seq_sensor3 = dnasensor_obj.seq_sensor()
       dnasensor_tp_obj = Dnsorder_tp(arms=dnasensor_obj.arms, arm1=arm1, arm2=arm2, arm3=arm3, arm4=arm4, conc_seq=conc_arms,
                                      conc_salt=conc_salt, conc_mg=conc_mg, temp=temp)
       # Defining parameters into a variable
       seq_arms = [arm1, arm2, arm3,arm4]
       seq_sensor = [seq_sensor1, seq_sensor2, seq_sensor3]
       arms_Tm = [dnasensor_tp_obj.arm1_Tm, dnasensor_tp_obj.arm2_Tm, dnasensor_tp_obj.arm3_Tm, dnasensor_tp_obj.arm4_Tm]
       arms_dG = [dnasensor_tp_obj.arm1_dG, dnasensor_tp_obj.arm2_dG, dnasensor_tp_obj.arm3_dG, dnasensor_tp_obj.arm4_dG]
       arms_dH = [dnasensor_tp_obj.arm1_dH, dnasensor_tp_obj.arm2_dH, dnasensor_tp_obj.arm3_dH, dnasensor_tp_obj.arm4_dH]
       arms_dS = [dnasensor_tp_obj.arm1_dS, dnasensor_tp_obj.arm2_dS, dnasensor_tp_obj.arm3_dS, dnasensor_tp_obj.arm4_dS]

# making .csv file
if save == "analyte":
       save_analyte(analyte_obj.sequence, param_analyte, param_reaction, output_dir)
elif save == "arms":
       save_arms_all_param(analyte_obj.sequence, seq_sensor, seq_arms, arms_Tm, arms_dG, arms_dH, arms_dS,
                           conc_arms, param_reaction, output_dir)
elif save == "all":
       save_all(analyte_obj.sequence, param_analyte, seq_sensor, seq_arms, arms_Tm, arms_dG, arms_dH, arms_dS,
                conc_arms, param_reaction, output_dir)