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
    `       channel: channel ID
            seq_to_signal :sequence to signal move table
            dt: time of run
            ds: run ID in basecall mode
            lb: sample ID
            pl: outputs 'ONT', device organisation?
            pm: device position
            pu: flow cell ID
            al: unknown (outputs unclassified)
    """

    if bam_file:
        sam_file = pysam.AlignmentFile(bam_file, "rb", check_sq=False)
        # Access the RG section of the header
        rg_tags = sam_file.header.get("RG", [])
        # Iterate through groups and extract tags
        for rg_tag in rg_tags:
            ident = rg_tag.get("ID")
            dt = rg_tag.get("DT")  # Time of run
            ds = rg_tag.get("DS")  # Run ID and basecall mode
            lb = rg_tag.get("LB")  # Sample ID
            pl = rg_tag.get("PL")  # outputs 'ONT', device organisation?
            pm = rg_tag.get("PM")  # Device position
            pu = rg_tag.get("PU")  # Flow cell ID
            al = rg_tag.get("al")  # outputs 'unclassified'

        for read in sam_file.fetch(until_eof=True):
            # From each read
            name = read.query_name
            seq = read.seq
            qual = read.qual
            # From BAM tags in each read
            start_time_pr = read.get_tag("st")
            channel = read.get_tag("ch")
            read_basecall_id = read.get_tag("RG")
            seq_to_signal = read.get_tag("mv:B:c")

            yield (
                name,
                seq,
                qual,
                start_time_pr,
                channel,
                read_basecall_id,
                seq_to_signal,
                ident,
                dt,
                ds,
                lb,
                pl,
                pu,
                pm,
                al,
            )


for (
    name,
    seq,
    qual,
    start_time_pr,
    channel,
    read_basecall_id,
    seq_to_signal,
    ident,
    dt,
    ds,
    lb,
    pl,
    pu,
    pm,
    al,
) in read_bam(bam_file="230498_pass_68a2633f_385676fd_0.bam"):
    bam_read = {
        "id": ident,
        "dt": dt,
        "ds": ds,
        "lb": lb,
        "pl": pl,
        "pu": pu,
        "pm": pm,
        "al": al,
        "read_id": name,
        "sequence": seq,
        "sequence_length": len(str(seq)),
        "quality": qual,
        "start_time_per_run": start_time_pr,
        "channel": channel,
        "read_basecall_id": read_basecall_id,
        "seq_to_signal": seq_to_signal,
    }
    print(bam_read)
    break
