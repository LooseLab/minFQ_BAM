import pysam


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
        sam_file = pysam.AlignmentFile(bam_file, "rb", check_sq=False)
        sequence_dict = sam_file.header.to_dict()['RG']
        # Information from BAM header
        for sequence_info in sequence_dict:
            run_id = sequence_info['ID']
            flow_cell_id = sequence_info['PU']
            start_time = sequence_info['DT']
            basecall_method_run_id = sequence_info['DS']
        for bam_read in sam_file.fetch():
            # From each read
            name = bam_read.query_name
            seq = bam_read.seq
            qual = bam_read.qual
            # Information from BAM tags in each read
            start_time_pr = bam_read.get_tag('st')
            channel = bam_read.get_tag('ch')
            read_basecall_id = _bam_read.get_tag('RG')
            # seq_to_signal = bam_read.get_tag('mv:B:c')
            yield (
                name,
                seq,
                qual,
                start_time_pr,
                channel,
                read_basecall_id,
                run_id,
                flow_cell_id,
                start_time,
                basecall_method_run_id,
            )

for (
    name,
    seq,
    qual,
    start_time_pr,
    channel,
    read_basecall_id,
    run_id,
    flow_cell_id,
    start_time,
    basecall_method_run_id,
) in read_bam(bam_file="sort_ds1263_NUH7_M1.sup.meth.hg38.bam"):

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
                "basecall_method_run_id": basecall_method_run_id
               }
