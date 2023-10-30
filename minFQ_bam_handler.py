"""
Very basic reader for BAM files and extracting fastq parameters
import pysam
"""
import pysam


bam_file = "input.bam"  # place holder

def read_bam():
    samfile1 = pysam.AlignmentFile(bam_file, "rb")
    for read1 in samfile1.fetch():
        # Defines fastq data for each read
        name = read1.query_name
        desc = "+"
        seq = read1.seq
        qual = read1.qual
        # Into fastq format
        fastq1 = '\n'.join([str(i) for i in [name, seq, desc, qual]]) 

        yield fastq1


