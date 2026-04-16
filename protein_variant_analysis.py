from Bio.Seq import Seq

def analyze_variant(sequence, position, new_nucleotide):
    """
    Analyzes the effect of a SNP on the protein sequence.
    """
    # Adjust for 0-based indexing
    idx = position - 1

    # Create mutated sequence
    seq_list = list(sequence)
    seq_list[idx] = new_nucleotide
    mut_seq = "".join(seq_list)

    # Translation
    ref_pro = Seq(sequence).translate()
    mut_pro = Seq(mut_seq).translate()

    # Identify AA change
    ref_aa = ref_pro[idx // 3]
    mut_aa = mut_pro[idx // 3]

    print(f"--- Variant Analysis at Position {position} ---")
    print(f"Reference AA: {ref_aa} | Mutated AA: {mut_aa}")

    if ref_aa == mut_aa:
        print("Effect: Synonymous (No change)")
    else:
        print(f"Effect: MISSENSE MUTATION ({ref_aa} to {mut_aa})")

# mecR1 reference sequence (Truncated for display)
mecR1_ref = "ATGTTA" # Replace with your actual genetic sequence
analyze_variant(mecR1_ref, 47299, "A")
