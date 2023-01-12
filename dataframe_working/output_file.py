import os

type_file = ".csv"
open_mode = "a"
end_line = "\n"

def save_analyte(sequence, param_analyte, param_reaction, output_dir):

    param_analyte = list(map(str, param_analyte))
    param_reaction = list(map(str, param_reaction))

    with open(output_dir + '/analyte' + type_file, open_mode) as file:
        file.write('analyte_sequence;'
                   'length;GC_content;Tm_analyte;dG_analyte;dH_analyte;dS_analyte;'
                   '[analyte];[cat+];[cat2+];temperature \n')
        parameters = [sequence] + param_analyte + param_reaction + [end_line]
        file.write(';'.join(parameters))

def save_arms_all_param(sequence, seq_sensor, seq_arms, arms_Tm, arms_dG, arms_dH, arms_dS, conc_arms, param_reaction, output_dir):

    arms_Tm = list(map(str, arms_Tm))
    arms_dG = list(map(str, arms_dG))
    arms_dH = list(map(str, arms_dH))
    arms_dS = list(map(str, arms_dS))
    param_reaction = list(map(str, param_reaction))

    with open(output_dir + '/arms_all_param' + type_file, open_mode) as file:
        if len(seq_arms) == 2:
            file.write('analyte_sequence;'
                       'seq_sensor1;seq_sensor2;'
                       'arm1;arm2;'
                       'arm1_Tm;arm2_Tm;'
                       'arm1_dG;arm2_dG;'
                       'arm1_dH;arm2_dH;'
                       'arm1_dS;arm2_dS;'
                       '[arms];[analyte];[cat+];[cat2+];temperature \n')
        elif len(seq_arms) == 3:
            file.write('analyte_sequence;'
                       'seq_sensor1;seq_sensor2;seq_sensor3;'
                       'arm1;arm2;arm3;'
                       'arm1_Tm;arm2_Tm;arm3_Tm;'
                       'arm1_dG;arm2_dG;arm3_dG;'
                       'arm1_dH;arm2_dH;arm3_dH;'
                       'arm1_dS;arm2_dS;arm3_dS;'
                       '[arms];[cat+];[cat2+];temperature \n')
        elif len(seq_arms) == 4:
            file.write('analyte_sequence;'
                       'seq_sensor1;seq_sensor2;seq_sensor3;'
                       'arm1;arm2;arm3;arm4;'
                       'arm1_Tm;arm2_Tm;arm3_Tm;arm4_Tm;'
                       'arm1_dG;arm2_dG;arm3_dG;arm4_dG;'
                       'arm1_dH;arm2_dH;arm3_dH;arm4_dH;'
                       'arm1_dS;arm2_dS;arm3_dS;arm4_dS;'
                       '[arms];[cat+];[cat2+];temperature \n')
        parameters = [sequence] + seq_sensor + seq_arms + \
                     arms_Tm + arms_dG + arms_dH + arms_dS + [conc_arms] + param_reaction + [end_line]
        file.write(';'.join(parameters))

def save_all(sequence, param_analyte, seq_sensor, seq_arms,
             arms_Tm, arms_dG, arms_dH, arms_dS, conc_arms, param_reaction, output_dir):

    param_analyte = list(map(str, param_analyte))
    arms_Tm = list(map(str, arms_Tm))
    arms_dG = list(map(str, arms_dG))
    arms_dH = list(map(str, arms_dH))
    arms_dS = list(map(str, arms_dS))
    param_reaction = list(map(str, param_reaction))

    with open(os.path.join(output_dir, 'all' + type_file), open_mode) as file:
        if len(seq_arms) == 2:
            file.write('analyte_sequence;'
                       'length;GC_content;Tm_analyte;dG_analyte;dH_analyte;dS_analyte;'
                       'seq_sensor1;seq_sensor2;'
                       'arm1;arm2;'
                       'arm1_Tm;arm2_Tm;'
                       'arm1_dG;arm2_dG;'
                       'arm1_dH;arm2_dH;'
                       'arm1_dS;arm2_dS;'
                       '[analyte];[cat+];[cat2+];temperature \n')
        elif len(seq_arms) == 3:
            file.write('analyte_sequence;'
                       'length;GC_content;Tm_analyte;dG_analyte;dH_analyte;dS_analyte;'
                       'seq_sensor1;seq_sensor2;seq_sensor3;'
                       'arm1;arm2;arm3;'
                       'arm1_Tm;arm2_Tm;arm3_Tm;'
                       'arm1_dG;arm2_dG;arm3_dG;'
                       'arm1_dH;arm2_dH;arm3_dH;'
                       'arm1_dS;arm2_dS;arm3_dS;'
                       '[analyte];[cat+];[cat2+];temperature \n')
        elif len(seq_arms) == 4:
            file.write('analyte_sequence;'
                       'length;GC_content;Tm_analyte;dG_analyte;dH_analyte;dS_analyte;'
                       'seq_sensor1;seq_sensor2;seq_sensor3;'
                       'arm1;arm2;arm3;arm4;'
                       'arm1_Tm;arm2_Tm;arm3_Tm;arm4_Tm;'
                       'arm1_dG;arm2_dG;arm3_dG;arm4_dG;'
                       'arm1_dH;arm2_dH;arm3_dH;arm4_dH;'
                       'arm1_dS;arm2_dS;arm3_dS;arm4_dS;'
                       '[analyte];[cat+];[cat2+];temperature \n')
        parameters = [sequence] + param_analyte + seq_sensor + seq_arms + \
                     arms_Tm + arms_dG + arms_dH + arms_dS + [conc_arms] + param_reaction + [end_line]
        file.write(';'.join(parameters))
