import pysam


def read_bam(bam_file=None):
    """


    :param bam_file: A bam format alignment file.
    :return:
        name: sequence name
        part: text divider
        seq: sequence
        qual: quality of reads
        start_time_pr: start time of run (per read)
        read_basecall_id: Read ID and basecall ID

        run_id: id for run
        flow_cell_id: id of flow cell
        start_time: start time of run
        basecall_method_run_id: Basecall method and run ID combined
    """
    
    if bam_file:
        samfile1 = pysam.AlignmentFile(bam_file, "rb")
        sequence_dict = samfile1.header.to_dict()['RG']
        # Information from BAM header
        for sequence_info in sequence_dict:
            run_id = sequence_info['ID']
            flow_cell_id = sequence_info['PU']
            start_time = sequence_info['DT']
            basecall_method_run_id = sequence_info['DS']
        for read1 in samfile1.fetch():
            # From each read
            name = read1.query_name
            part = '+'
            seq = read1.seq
            qual = read1.qual
            # Information from BAM tags in each read
            start_time_pr = read1.get_tag('st')
            read_basecall_id = read1.get_tag('RG')
            yield name, part, seq, qual, start_time_pr, read_basecall_id, run_id, flow_cell_id, start_time, basecall_method_run_id

count = 0
for values in read_bam(bam_file="sort_ds1263_NUH7_M1.sup.meth.hg38.bam"):
    print(*values)
    count += 1
    if count > 1:
        break
