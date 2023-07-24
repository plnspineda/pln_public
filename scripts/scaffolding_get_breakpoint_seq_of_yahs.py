import pandas as pd
import subprocess
import os
from Bio import SeqIO

agpfile = pd.read_table("/hpcfs/groups/phoenix-hpc-avsci/Lloyd_Low/Tuli_x_Wagyu_data/scaffolding/YaHS_flye/Tuli/default_run/yahs.out_scaffolds_final.agp", header=None)
agpfile.columns = ["scaffold", "begin", "end", "pos", "category", "contig", "contig_begin", "contig_end", "type"]

# 1. get the duplicate contig in .agp file at column 6, ignoring the "200" since it's a gap
# 2. extract the region from the scaffold fasta file, and take only column 3 + 10200bp if column 7 is "1",
# otherwise get column 2 + 5000bp and column 2 - 10200bp.
# 3. blast the scaffold region
# 4. analyse...

### extracting duplicated contigs
dup_file = agpfile[agpfile.duplicated(["contig"], keep = False)]
dup_file = dup_file[dup_file.contig != "200"]
#print(dup_file)

dup_file["search_begin"] = 0
dup_file["search_end"] = 0

### getting the region of the breakpoint, extracting location at 5000bp sequences at each ends
for line, row in dup_file.iterrows():
    if row["contig_begin"] == "1":
        dup_file.at[line, "search_begin"] = dup_file.at[line, "end"]
        dup_file.at[line, "search_begin"] -= 5000
        dup_file.at[line, "search_end"] = dup_file.at[line, "end"] + 5000
    else:
        dup_file.at[line, "search_begin"] = dup_file.at[line, "begin"]
        dup_file.at[line, "search_begin"] -= 5000
        dup_file.at[line, "search_end"] = dup_file.at[line, "begin"] + 5000

pos_file = dup_file[["scaffold", "search_begin", "search_end"]].copy()
new_pos_file = pos_file[pos_file["search_end"] >= 1000000]
#print(new_pos_file)

### output position file to extract within the fasta file
new_pos_file.to_csv("breakpoints_position.tsv", sep="\t")
###

new_pos_file = "breakpoints_position.tsv"
fasta_file = "/hpcfs/groups/phoenix-hpc-avsci/Lloyd_Low/Tuli_x_Wagyu_data/scaffolding/YaHS_flye/Tuli/default_run/yahs.out_scaffolds_final.fa"

# Define the Bash script as a string
bash_script = '''
#!/bin/bash
module load arch/haswell SAMtools/1.10-foss-2016b
while IFS=$'\t' read -r f1 f2 f3 f4
do
	samtools faidx /hpcfs/groups/phoenix-hpc-avsci/Lloyd_Low/Tuli_x_Wagyu_data/scaffolding/YaHS_flye/Tuli/default_run/yahs.out_scaffolds_final.fa "$f2:$f3-$f4" > "$f2"_"$f3"-"$f4.fa"
done < <(tail -n +2 "$1")
'''

# Open the FASTA file with BioPython
with open(fasta_file) as handle:
    # Run the Bash script with the arguments
    subprocess.run(["bash", "-c", bash_script, "--", new_pos_file], stdin=handle)

## blast the fasta files with UOA_WB_1

# Set the directory where the input files are located
input_dir = "/hpcfs/groups/phoenix-hpc-avsci/Lloyd_Low/Tuli_x_Wagyu_data/scaffolding/YaHS_flye/Tuli/default_run/looking_at_breakpoints"

# Set the name of the BLASTN database file
db_file = "/hpcfs/groups/phoenix-hpc-avsci/Lloyd_Low/Tuli_x_Wagyu_data/scaffolding/YaHS_flye/Tuli/default_run/looking_at_breakpoints/database/GCF_002263795.2_ARS-UCD1.3_genomic.fna"

# Set the directory where the output files will be saved
output_dir = "/hpcfs/groups/phoenix-hpc-avsci/Lloyd_Low/Tuli_x_Wagyu_data/scaffolding/YaHS_flye/Tuli/default_run/looking_at_breakpoints/output"

# Load the BLAST+ module
subprocess.run(["module", "load", "arch/haswell", "BLAST+/2.2.31-foss-2015b-Python-2.7.11"])

# Create the BLASTN database
subprocess.run(["makeblastdb", "-in", db_file, "-dbtype", "nucl", "-parse_seqids"])

# Loop over all files in the input directory that end in ".fa"
for input_file in os.listdir(input_dir):
    if input_file.endswith(".fa"):
        # Set the name of the output file
        output_file = os.path.join(output_dir, "ARS_UCD1.3_vs_" + input_file + ".blnm7")

        # Set the BLASTN command as a string
        blastn_cmd = "blastn -db {} -query {} -outfmt 7 -evalue 1e-10 -perc_identity 90 -out {}".format(db_file, os.path.join(input_dir, input_file), output_file)

        # Run the BLASTN command using subprocess
        subprocess.run(blastn_cmd, shell=True)
