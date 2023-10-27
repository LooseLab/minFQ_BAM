"""
Very basic reader for BAM files and extracting fastq parameters
import pysam
"""

bam_file = "input.bam"  # place holder


def read_bam():
    samfile1 = pysam.AlignmentFile(bam_file, "rb")
    for read1 in samfile1.fetch():
        # Defines fastq data for each read
        qry_name = read1.query_name
        desc = "+"
        seq = read1.query_alignment_sequence
        qual = read1.query_alignment_qualities

        yield qry_name, desc, seq, qual


