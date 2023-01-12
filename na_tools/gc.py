import sys

def gc(seq):
    """Calculate GC share in NA sequence"""

    # checking corrected writing DNA/RNA seq
    for nt in seq:
        if nt not in ['A', 'T', 'U', 'C', 'G', 'a', 't', 'u', 'c', 'g']:
            sys.exit(0)

    seq = seq.upper()
    gc = ((seq.count("G") + seq.count("C")) / len(seq)) * 100

    return round(gc, 2)
