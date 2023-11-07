import pysam
# Hello

def read_bam(bam_file=None):
    """


    :param bam_file: A bam format alignment file.
    :return:
        name: sequence name
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
        samfile1 = pysam.AlignmentFile(bam_file, "rb", check_sq=False)
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
            seq = read1.seq
            qual = read1.qual
            # Information from BAM tags in each read
            start_time_pr = read1.get_tag('st')
            channel = read1.get_tag('ch')
            read_basecall_id = read1.get_tag('RG')
            # seq_to_signal = read1.get_tag('mv:B:c')
            yield name, seq, qual, start_time_pr, channel, read_basecall_id, run_id, flow_cell_id, start_time, basecall_method_run_id


for name, seq, qual, start_time_pr, channel, read_basecall_id, run_id, flow_cell_id, start_time, basecall_method_run_id in read_bam(
        bam_file="sort_ds1263_NUH7_M1.sup.meth.hg38.bam"):
"""

Parameters 
----------
name : str 
    BAM read ID
seq : str
    Sequence string for BAM read
qual : str
    Quality string for BAM read
start_time_per_read : str
    Start time for each read
channel : int
    Channel for each read
read_basecall_id : str
    Basecall ID for each read
run_id : str
    ID for the run
flow_cell_id : str
    ID for the flow cell used
start_time : str
    Start time found in @RG (start of whole run?
basecall_method_run_id: str
    The basecall method used and run ID

Returns
---------
"""
    bam_read = {"read_id": name,
                "sequence": seq,
                "sequence_length": len(str(seq)),
                "quality": qual,
                "start_time_per_read": start_time_pr,
                "channel": channel,
                "read_basecall_id": read_basecall_id,
                "run_id": run_id,
                "flow_cell_id": flow_cell_id,
                "start_time": start_time,
                "basecall_method_run_id": basecall_method_run_id}
