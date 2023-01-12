def transcribe(sequence):

    if check_seq(sequence) == True:
        transcribe_dict = {
            'A': 'A',
            'a': 'a',
            'T': 'U',
            't': 'u',
            'U': 'T',
            'u': 'T',
            'C': 'C',
            'c': 'c',
            'G': 'G',
            'g': 'g',
        }

        result = ''
        for nt in sequence:
            result += transcribe_dict[nt]

        return result

def complement(sequence):

    if check_seq(sequence) == True:
        complement_dict = {
            'A': 'T',
            'a': 't',
            'T': 'A',
            't': 'a',
            'C': 'G',
            'c': 'g',
            'G': 'C',
            'g': 'c',
        }
        result = ''
        for nt in sequence:
            result += complement_dict[nt]
        return result

def reverse(sequence):
    if check_seq(sequence) == True:
        return sequence[::-1]

def reverse_complement(sequence):
    if check_seq(sequence) == True:
        result = ''
        for nt in sequence:
            result += complement(nt)
        return result[::-1]

def check_seq(sequence):
    check_seq = True

    if check_seq is True:
        for nt in sequence:

            if check_seq is False:
                break

            if nt in 'AaTtUuCcGg':
                check_seq = True
            else:
                check_seq = False

    return check_seq

# sequence = 'ATCG'
# print(reverse_complement(sequence))
