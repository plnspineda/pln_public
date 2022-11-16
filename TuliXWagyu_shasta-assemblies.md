# Tuli X Wagyu shasta assemblies

*2022.06.21*

Table. Summary of assemblies statistics using Quast and Merqury

| Assembly       | Size     | No. of contigs | Largest contig | N50      | QV      | K-mer completeness | Switch-error |
|----------------|----------|----------------|----------------|----------|---------|--------------------|--------------|
| Tuli_v9_10Krl  | 2.59E+09 | 1623           | 120844177      | 71706705 | 41.0099 | 90.6965            | 0.195522%    |
| Tuli_v10_1Krl   | 2.57E+09 | 1503           | 136239588      | 73170537 | 41.0187 | 90.6345            | 0.19384%     |
| Tuli_v10_5Krl   | 2.58E+09 | 1582           | 136253024      | 73210116 | 40.7159 | 90.6512            | 0.19444%     |
| Tuli_v10_10Krl  | 2.59E+09 | 1616           | 120843555      | 71705857 | 41.0097 | 90.6973            | 0.194533%    |
| Wagyu_v9_10Krl | 2.70E+09 | 1640           | 119523932      | 43812055 | 40.5337 | 94.4876            | 0.422887%    |
| Wagyu_v10_1Krl  | 2.69E+09 | 1442           | 136048618      | 58176654 | 40.9735 | 94.5336            | 0.414957%    |
| Wagyu_v10_5Krl  | 2.70E+09 | 1482           | 136132470      | 57085142 | 40.7162 | 94.5296            | 0.422241%    |
| Wagyu_v10_10Krl | 2.70E+09 | 1620           | 119523442      | 43811850 | 40.5871 | 94.4844            | 0.421901%    |


Notes:
- Lowest number of contigs: 1Krl
- Largest N50: Tuli_v10_5Krl and Wagyu_v10_1Krl
- Highest QV: Tuli_v10_1Krl and Wagyu_v10_1Krl
- Highest K-mer completeness: Tuli_v10_10Krl and Wagyu_v10_1Krl
- Lowest switch-error rate: Tuli_v10_1Krl and Wagyu_v10_1Krl

Hapmer blobs for each assemblies

| TulixWagyu_v10_1Krl | TulixWagyu_v10_5Krl | TulixWagyu_v10_10Krl|
|---------------------|---------------------|---------------------|
|<img src="https://github.com/plnspineda/pln_public/blob/pln/images/rl1k-QV.hapmers.blob.png" width="450" /> | <img src="https://github.com/plnspineda/pln_public/blob/pln/images/rl5k-QV.hapmers.blob.png" width="450" /> | <img src="https://github.com/plnspineda/pln_public/blob/pln/images/rl10k-QV.hapmers.blob.png" width="450" /> |

Spectra of assemblies (stacked)

| TulixWagyu_v10_1Krl | TulixWagyu_v10_5Krl | TulixWagyu_v10_10Krl|
|---------------------|---------------------|---------------------|
|<img src="https://github.com/plnspineda/pln_public/blob/pln/images/rl1k-QV.spectra-asm.st.png" width="450" /> | <img src="https://github.com/plnspineda/pln_public/blob/pln/images/rl5k-QV.spectra-asm.st.png" width="450" /> | <img src="https://github.com/plnspineda/pln_public/blob/pln/images/rl10k-QV.spectra-asm.st.png" width="450" /> |

Switch-blocks (number of switches: 100, short-range: 20,000)\
  switch=100 and range=20000 allows 0.5% of switches in ~20kb window

| Tuli_v10_1Krl (blocks) | Tuli_v10_1Krl (continuity)|
|---------------------|---------------------|
| <img src="https://github.com/plnspineda/pln_public/blob/pln/images/rl1k-QV.Tuliv10rl1000.block.N.png" width="450" /> | <img src="https://github.com/plnspineda/pln_public/blob/pln/images/rl1k-QV.Tuliv10rl1000.continuity.N.png" width="450" /> |

| Wagyu_v10_1Krl (blocks) | Wagyu_v10_1Krl (continuity)|
|---------------------|---------------------|
| <img src="https://github.com/plnspineda/pln_public/blob/pln/images/rl1k-QV.Wagyuv10rl1000.block.N.png" width="450" /> | <img src="https://github.com/plnspineda/pln_public/blob/pln/images/rl1k-QV.Wagyuv10rl1000.continuity.N.png" width="450" /> |

Table. Switch-rate errors statistics

| Assembly       | Number of blocks | Total bases in blocks (block sum) | Smallest block size | Avg. Block size | Block N50 size | Longest block size | Num. of markers from other haplotype | total num. of markers in block | Switch-error rate |
|----------------|------------------|-----------------------------------|---------------------|-----------------|----------------|--------------------|--------------------------------------|--------------------------------|-------------------|
| Tuli_v9_10Krl  | 1941             | 2566722393                        | 22                  | 1322371         | 19046386       | 59902359           | 132461                               | 67747289                       | 0.195522%         |
| Tuli_v10_1Kr   | 1768             | 2552926411                        | 22                  | 1443963         | 19881514       | 87365924           | 129821                               | 66973108                       | 0.19384%          |
| Tuli_v10_5Kr   | 1885             | 2558183351                        | 22                  | 1357127         | 19302345       | 70522016           | 130442                               | 67086067                       | 0.19444%          |
| Tuli_v10_10Kr  | 1947             | 2566432330                        | 22                  | 1318147         | 18301306       | 70488106           | 131779                               | 67741037                       | 0.194533%         |
| Wagyu_v9_10Krl | 2331             | 2666971482                        | 22                  | 1144132         | 9628018        | 35850846           | 199975                               | 47288053                       | 0.422887%         |
| Wagyu_v10_1Kr  | 2166             | 2662155664                        | 22                  | 1229066         | 10101723       | 56098866           | 195991                               | 47231661                       | 0.414957%         |
| Wagyu_v10_5Kr  | 2239             | 2665466786                        | 22                  | 1190472         | 10296890       | 56098977           | 199605                               | 47272786                       | 0.422241%         |
| Wagyu_v10_10Kr | 2296             | 2666883035                        | 22                  | 1161535         | 9350663        | 56471284           | 199500                               | 47285958                       | 0.421901%         |


**2021.11.14**

Flye vs Shasta assembly

file location: /hpcfs/groups/phoenix-hpc-avsci/Lloyd_Low/Tuli_x_Wagyu_data/assembly_contig/Flye

        #!/bin/bash
        #SBATCH -p batch
        #SBATCH -N 1            # number of nodes
        #SBATCH -n 32            # number of cores
        #SBATCH --time=70:00:00 # time allocation (D-HH:MM:SS)
        #SBATCH --mem=1TB       # memory pool for all cores

        module load arch/haswell
        module load Anaconda3/2020.07
        source activate flye


        ### flye version 2.8.1-b1676 installed using `conda install flye` (latest is 2.9.1)
        flye --threads 32 --nano-raw ../../haplotype/haplotype-Tuli_sire.fasta -o haplotype_flye_Tuli_sire_raw ## takes 2-20:04:42 to finish
        flye --threads 32 --nano-raw ../../haplotype/haplotype-Wagyu_dam.fasta -o haplotype_flye_Wagyu_dam_raw ## takes 2-22:56:58 to finish


| Assembly                        | size (Gb) | contig | N50 (Mb) | max_contig (Mb) |      QV |
|---------------------------------|----------:|-------:|---------:|----------------:|--------:|
| Tuli_shastav10                  | 2.5726    | 1503   | 73.1705  | 136.24          | 41.0187 |
| Tuli_shastav10_complete_purged  | 2.5279    | 565    | 73.1705  | 136.24          | 41.8958 |
| Tuli_shastav10_filtered_purged  | 2.5383    | 850    | 73.1705  | 136.24          | 41.5655 |
| Tuli_flyev2.6                   | 2.5092    | 834    | 38.3670  | 105.60          | 40.7343 |
| Wagyu_shastav10                 | 2.6919    | 1442   | 58.1767  | 136.05          | 40.9735 |
| Wagyu_shastav10_complete_purged | 2.6515    | 446    | 58.1767  | 136.05          | 41.4811 |
| Wagyu_shastav10_filtered_purged | 2.6633    | 760    | 58.1767  | 136.05          | 41.2585 |
| Wagyu_flyev2.6                  | 2.6331    | 766    | 42.4578  | 106.64          | 40.8899 |

seems like I need to rerun Flye with the latest version.

Purge dups

for filtered purged

| PURGE_DUPS   | Tuli | Wagyu |-------|
|--------------|-----:|------:|-------|
| HAPLOTIG     | 137  | 131   | *kept |
| HIGHCOV      | 148  | 189   | *kept |
| JUNK         | 82   | 99    | *rm |
| OVLP         | 9    | 12    | *kept |
| REPEAT       | 589  | 599   | *rm |
| less than 1M | 588  | 599   | |

for Tuli repeats: bases masked:    1830047 bp ( 5.37 %)


**2022.11.15**

Scaffolding...

file location: /hpcfs/groups/phoenix-hpc-avsci/Lloyd_Low/Tuli_x_Wagyu_data/scaffolding/Arima_pipeline

        #! /bin/bash
        #SBATCH -p batch
        #SBATCH -N 1            # number of nodes
        #SBATCH -n 12            # number of cores
        #SBATCH --time=72:00:00 # time allocation (D-HH:MM:SS)
        #SBATCH --mem=128GB       # memory pool for all cores
        #SBATCH --mail-type=END
        #SBATCH --mail-type=FAIL
        #SBATCH --mail-user=paulene.pineda@adelaide.edu.au


        module load arch/haswell
        module load BWA/0.7.17
        module load SAMtools/1.10-foss-2016b
        module load Java/13.0.2
        module load picard/2.22.3-Java-1.8.0_121

        ##############################################
        # ARIMA GENOMICS MAPPING PIPELINE 02/08/2019 #
        ##############################################

        #Below find the commands used to map HiC data.

        #Replace the variables at the top with the correct paths for the locations of files/programs on your system.

        #This bash script will map one paired end HiC dataset (read1 & read2 fastqs). Feel to modify and multiplex as you see fit to work with your volume of samples and system.

        ##########################################
        # Commands #
        ##########################################

        SRA='3DWFS0412_HTWHYDRX2_TGTCGTTT_L001'
        LABEL='Tuli_shastav10_1K_purged'
        BWA='/apps/skl/software/BWA/0.7.17/bin/bwa'
        SAMTOOLS='/apps/software/SAMtools/1.10-foss-2016b/bin/samtools'
        IN_DIR='/hpcfs/groups/phoenix-hpc-avsci/Lloyd_Low/Tuli_x_Wagyu_data/scaffolding/raw_data_hic/clean_reads/SAGCQA0486'
        REF='Tuli_shastav10_1K_purged.fasta'
        FAIDX='$REF.fai'
        PREFIX='Tuli_shastav10_1K_purged.fasta'
        RAW_DIR='raw_dir'
        FILT_DIR='filtered'
        FILTER='/hpcfs/groups/phoenix-hpc-avsci/Lloyd_Low/Tuli_x_Wagyu_data/tools/mapping_pipeline/filter_five_end.pl'
        COMBINER='/hpcfs/groups/phoenix-hpc-avsci/Lloyd_Low/Tuli_x_Wagyu_data/tools/mapping_pipeline/two_read_bam_combiner.pl'
        STATS='/hpcfs/groups/phoenix-hpc-avsci/Lloyd_Low/Tuli_x_Wagyu_data/tools/mapping_pipeline/get_stats.pl'
        PICARD='/apps/software/picard/2.22.3-Java-1.8.0_121/picard.jar'
        TMP_DIR='tmp'
        PAIR_DIR='paired'
        REP_DIR='duplicate'
        REP_LABEL=$LABEL'_rep1'
        MERGE_DIR='final_merge'
        MAPQ_FILTER=10
        CPU=12

        echo "### Step 0: Check output directories exist & create them as needed"
        [ -d $RAW_DIR ] || mkdir -p $RAW_DIR
        [ -d $FILT_DIR ] || mkdir -p $FILT_DIR
        [ -d $TMP_DIR ] || mkdir -p $TMP_DIR
        [ -d $PAIR_DIR ] || mkdir -p $PAIR_DIR
        [ -d $REP_DIR ] || mkdir -p $REP_DIR
        # [ -d $MERGE_DIR ] || mkdir -p $MERGE_DIR

        # echo "### Step 0: Index reference" # Run only once! Skip this step if you have already generated BWA index files
        bwa index -a bwtsw $REF

        echo "### Step 1.A: FASTQ to BAM (1st)"
        bwa mem -t $CPU $REF $IN_DIR/$SRA'_R1_val_1.fq.gz' | $SAMTOOLS view -@ $CPU -Sb - > $RAW_DIR/$SRA'_1.bam'

        echo "### Step 1.B: FASTQ to BAM (2nd)"
        bwa mem -t $CPU $REF $IN_DIR/$SRA'_R2_val_2.fq.gz' | $SAMTOOLS view -@ $CPU -Sb - > $RAW_DIR/$SRA'_2.bam'

        echo "### Step 2.A: Filter 5' end (1st)"
        samtools view -h $RAW_DIR/$SRA'_1.bam' | perl $FILTER | $SAMTOOLS view -Sb - > $FILT_DIR/$SRA'_1.bam'

        echo "### Step 2.B: Filter 5' end (2nd)"
        samtools view -h $RAW_DIR/$SRA'_2.bam' | perl $FILTER | $SAMTOOLS view -Sb - > $FILT_DIR/$SRA'_2.bam'

        echo "### Step 3A: Pair reads & mapping quality filter"
        perl $COMBINER $FILT_DIR/$SRA'_1.bam' $FILT_DIR/$SRA'_2.bam' $SAMTOOLS $MAPQ_FILTER | $SAMTOOLS view -bS -t $FAIDX - | $SAMTOOLS sort -@ $CPU -o $TMP_DIR/$SRA'.bam' -

        echo "### Step 3.B: Add read group"
        java -Xmx4G -Djava.io.tmpdir=temp/ -jar $PICARD AddOrReplaceReadGroups INPUT=$TMP_DIR/$SRA'.bam' OUTPUT=$PAIR_DIR/$SRA'.bam' ID=$SRA LB=$SRA SM=$LABEL PL=ILLUMINA PU=none

        ###############################################################################################################################################################
        ###                                           How to Accommodate Technical Replicates                                                                       ###
        ### This pipeline is currently built for processing a single sample with one read1 and read2 fastq file.                                                    ###
        ### Technical replicates (eg. one library split across multiple lanes) should be merged before running the MarkDuplicates command.                          ###
        ### If this step is run, the names and locations of input files to subsequent steps will need to be modified in order for subsequent steps to run correctly.###
        ### The code below is an example of how to merge technical replicates.                                                                                      ###
        ###############################################################################################################################################################
        #	REP_NUM=X #number of the technical replicate set e.g. 1
        #	REP_LABEL=$LABEL\_rep$REP_NUM
        #	INPUTS_TECH_REPS=('bash' 'array' 'of' 'bams' 'from' 'replicates') #BAM files you want combined as technical replicates
        #   example bash array - INPUTS_TECH_REPS=('INPUT=A.L1.bam' 'INPUT=A.L2.bam' 'INPUT=A.L3.bam')
        #	java -Xmx8G -Djava.io.tmpdir=temp/ -jar $PICARD MergeSamFiles $INPUTS_TECH_REPS OUTPUT=$TMP_DIR/$REP_LABEL.bam USE_THREADING=TRUE ASSUME_SORTED=TRUE VALIDATION_STRINGENCY=LENIENT

        echo "### Step 4: Mark duplicates"
        java -Xmx30G -XX:-UseGCOverheadLimit -Djava.io.tmpdir=temp/ -jar $PICARD MarkDuplicates INPUT=$PAIR_DIR/$SRA.bam OUTPUT=$REP_DIR/$REP_LABEL.bam METRICS_FILE=$REP_DIR/metrics.$REP_LABEL.txt TMP_DIR=$TMP_DIR ASSUME_SORTED=TRUE VALIDATION_STRINGENCY=LENIENT REMOVE_DUPLICATES=TRUE

        samtools index $REP_DIR/$REP_LABEL'.bam'

        perl $STATS $REP_DIR/$REP_LABEL'.bam' > $REP_DIR/$REP_LABEL'.bam.stats'

        echo "Finished Mapping Pipeline through Duplicate Removal"

        #########################################################################################################################################
        ###                                       How to Accommodate Biological Replicates                                                    ###
        ### This pipeline is currently built for processing a single sample with one read1 and read2 fastq file.                              ###
        ### Biological replicates (eg. multiple libraries made from the same sample) should be merged before proceeding with subsequent steps.###
        ### The code below is an example of how to merge biological replicates.                                                               ###
        #########################################################################################################################################
        #
        #	INPUTS_BIOLOGICAL_REPS=('bash' 'array' 'of' 'bams' 'from' 'replicates') #BAM files you want combined as biological replicates
        #   example bash array - INPUTS_BIOLOGICAL_REPS=('INPUT=A_rep1.bam' 'INPUT=A_rep2.bam' 'INPUT=A_rep3.bam')
        #
        #	java -Xmx8G -Djava.io.tmpdir=temp/ -jar $PICARD MergeSamFiles $INPUTS_BIOLOGICAL_REPS OUTPUT=$MERGE_DIR/$LABEL.bam USE_THREADING=TRUE ASSUME_SORTED=TRUE VALIDATION_STRINGENCY=LENIENT
        #
        #	$SAMTOOLS index $MERGE_DIR/$LABEL.bam

        # perl $STATS $MERGE_DIR/$LABEL.bam > $MERGE_DIR/$LABEL.bam.stats

        # echo "Finished Mapping Pipeline through merging Biological Replicates"
