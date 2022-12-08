import sys

def gc(primer_seq):
    """Calculate GC share in NA sequence"""

    for nt in primer_seq:
        if nt not in ['A', 'T', 'C', 'G', 'a', 't', 'c', 'g']:
            sys.exit(0)

    seq = primer_seq.upper()
    gc = ((seq.count("G") + seq.count("C")) / len(seq)) * 100

    return gc
