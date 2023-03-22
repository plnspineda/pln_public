# Assembling Tuli and Wagyu with Flye using ONT reads

        flye --threads 24 --nano-hq haplotype/haplotype-Tuli_sire.fasta -o haplotype_flye_Tuli_sire_nanohq
        flye --threads 24 --nano-hq haplotype/haplotype-Wagyu_dam.fasta -o haplotype_flye_Wagyu_dam_nanohq  

output files:

        2.7G	00-assembly
        2.8G	10-consensus
        24G	  20-repeat
        7.4G	30-contigger
        5.0G	40-polishing
        2.5G	assembly.fasta
        2.5G	assembly_graph.gfa
        740K	assembly_graph.gv
        228K	assembly_info.txt
        8.4M	flye.log
        4.0K	params.json

**Result:**

| Assembly                   |  Tuli_flye | Tuli_shasta | Wagyu_flye | Wagyu_shasta |
|----------------------------|-----------:|------------:|-----------:|-------------:|
| # contigs (>= 0 bp)        | 2118       | 1568        | 1787       | 1518         |
| # contigs (>= 1000 bp)     | 2082       | 1460        | 1753       | 1396         |
| # contigs (>= 5000 bp)     | 1733       | 1251        | 1415       | 1182         |
| # contigs (>= 10000 bp)    | 1362       | 1095        | 1137       | 1039         |
| # contigs (>= 25000 bp)    | 832        | 788         | 712        | 761          |
| # contigs (>= 50000 bp)    | 566        | 514         | 476        | 497          |
| Total length (>= 0 bp)     | 2612640510 | 2572648131  | 2711677997 | 2691890265   |
| Total length (>= 1000 bp)  | 2612616980 | 2572602907  | 2711655119 | 2691842586   |
| Total length (>= 5000 bp)  | 2611605565 | 2572005932  | 2710712804 | 2691256656   |
| Total length (>= 10000 bp) | 2608840048 | 2570835882  | 2708626156 | 2690211777   |
| Total length (>= 25000 bp) | 2600562563 | 2565669285  | 2701861993 | 2685577338   |
| Total length (>= 50000 bp) | 2591158320 | 2555807741  | 2693436613 | 2676041839   |
| # contigs                  | 2116       | 1503        | 1784       | 1442         |
| Largest contig             | 156401090  | 136239588   | 156450840  | 136048618    |
| Total length               | 2612640017 | 2572634030  | 2711677675 | 2691875595   |
| GC (%)                     | 42.3       | 42.14       | 42.03      | 42.02        |
| N50                        | 70217624   | 73170537    | 71001583   | 58176654     |
| N75                        | 43089568   | 45718182    | 44098164   | 36917800     |
| L50                        | 14         | 13          | 14         | 16           |
| L75                        | 25         | 24          | 25         | 31           |
| # N's per 100 kbp          | 0          | 0           | 0          | 0            |
| Merqury_QV                 | 40.7343    | 41.0187     | 40.8899    | 40.9735      |

**Assembly metrics summary**

| **Assembly** | **Size (Gb)** | **Contig** | **N50 (Mb)** | **Max contig (Mb)** |  **QV** |
|--------------|--------------:|-----------:|-------------:|--------------------:|--------:|
| Tuli flye    | 2.61          | 2116       | 70.22        | 156.40              | 40.7343 |
| Tuli shasta  | 2.57          | 1503       | 73.17        | 136.24              | 41.0187 |
| Wagyu flye   | 2.71          | 1784       | 71.00        | 156.45              | 40.8899 |
| Wagyu shasta | 2.69          | 1442       | 58.18        | 136.05              | 40.9735 |

**IGH FLYE**

| Pied_vs_Pied | Pied_vs_Tuli | Tuli_vs_Tuli |
|---------------|---------------|-------------|
| <img src="https://github.com/plnspineda/pln_public/blob/pln/images/IGH/Pied_vs_Pied.jpeg" width="550" /> | <img src="https://github.com/plnspineda/pln_public/blob/pln/images/IGH/Pied_vs_Tuli_contig595.jpeg" width="550" /> | <img src="https://github.com/plnspineda/pln_public/blob/pln/images/IGH/Tuli_vs_Tuli_1contg.jpeg" width="550" /> |

| Pied_vs_Pied | Pied_vs_Wagyu | Wagyu_vs_Wagyu |
|---------------|---------------|-------------|
| <img src="https://github.com/plnspineda/pln_public/blob/pln/images/IGH/Pied_vs_Pied.jpeg" width="550" /> | <img src="https://github.com/plnspineda/pln_public/blob/pln/images/IGH/Pied_vs_Wagyu_9contigs.jpeg" width="550" /> | <img src="https://github.com/plnspineda/pln_public/blob/pln/images/IGH/Wagyu_vs_Wagyu.jpeg" width="550" /> |

*Length of each contigs*

| **Wagyu**              | **553438** |   | **Tuli**                     | **562766** |
|------------------------|-----------:|---|------------------------------|-----------:|
| contig_2392:1-70179/rc |      70179 |   | contig_595:69106311-69669076 | 562766     |
| contig_2391            |      44351 |   |         |    |
| contig_2385            |     297510 |   |                              |            |
| contig_2389/rc         |      17336 |   |                              |            |
| contig_2394/rc         |      26235 |   |                              |            |
| contig_2384            |      23125 |   |                              |            |
| contig_2388/rc         |      10624 |   |                              |            |
| contig_2380/rc         |      33336 |   |                              |            |
| contig_2379/rc         |      30742 |   |                              |            |

**IGH SHASTA**

| Pied_vs_Pied | Pied_vs_Tuli | Tuli_vs_Tuli |
|---------------|---------------|-------------|
| <img src="https://github.com/plnspineda/pln_public/blob/pln/images/IGH/Pied_vs_Pied.jpeg" width="550" /> | <img src="https://github.com/plnspineda/pln_public/blob/pln/images/IGH/shasta_Tuli_vs_Pied.jpeg" width="550" /> | <img src="https://github.com/plnspineda/pln_public/blob/pln/images/IGH/shasta_Tuli_vs_Tuli.jpeg" width="550" /> |

| Pied_vs_Pied | Pied_vs_Wagyu | Wagyu_vs_Wagyu |
|---------------|---------------|-------------|
| <img src="https://github.com/plnspineda/pln_public/blob/pln/images/IGH/Pied_vs_Pied.jpeg" width="550" /> | <img src="https://github.com/plnspineda/pln_public/blob/pln/images/IGH/shasta_Pied_vs_Wagyu.jpeg" width="550" /> | <img src="https://github.com/plnspineda/pln_public/blob/pln/images/IGH/shasta_Wagyu_vs_Wagyu.jpeg" width="550" /> |

*Length of each contigs*

| Wagyu             | 641625 |   | Tuli                | 665214 |
|-------------------|-------:|---|---------------------|-------:|
| 38:1-153025.fa/rc | 153025 |   | 2:45119379-45437849 | 218471 |
| 464               | 38270  |   | 358.fa/rc           | 23948  |
| 466               | 13167  |   | 476                 | 22702  |
| 468               | 152277 |   | 954                 | 23632  |
| 216               | 119933 |   | 1190                | 12046  |
| 214               | 36185  |   | 978                 | 116612 |
| 212/rc            | 128768 |   | 1318                | 80336  |
|                   |        |   | 292.fa/rc           | 52123  |
|                   |        |   | 498.fa/rc           | 72174  |
|                   |        |   | 736.fa/rc           | 31042  |
|                   |        |   | 1666                | 12128  |

**SUMMARY**

| Assembly IGH    | Size (bp) |
|--------------|-----------|
| Gaur         | 545789    |
| Pied         | 651224    |
| Tuli flye    | 562766    |
| Tuli shasta  | 665214    |
| Wagyu flye   | 553438    |
| Wagyu shasta | 641625    |


**will use Flye assembly since it resolves IGH better and increases Wagyu N50

-----------------------

### Purge dups

*Purging result*

|          | Tuli | total length | Wagyu | total length |             |
|----------|------|--------------|-------|--------------|-------------|
| HAPLOTIG | 148  | 4,161,752    | 126   | 3,768,412    |             |
| HIGHCOV  | 89   | 2,336,907    | 292   | 8,690,036    |             |
| JUNK     | 387  | 3,775,524    | 218   | 2,155,089    | will remove |
| OVLP     | 8    | 1,157,034    | 1     | 92,435       |             |
| REPEAT   | 954  | 48,283,079   | 564   | 21,913,575   | will remove |
|          |      | 59,714,296   |       | 36,619,547   |             |

**Tuli**

| REPEATS | OTHERS IN HAPLOBIN |
|-----|-----|
| <img src="https://github.com/plnspineda/pln_public/blob/pln/images/purge_dups/flye/Rplot_Tuli_repeat.png" width="450" /> | <img src="https://github.com/plnspineda/pln_public/blob/pln/images/purge_dups/flye/Rplot_Tuli_haps.png" width="450" /> |

**Wagyu**

| REPEATS | OTHERS IN HAPLOBIN |
|-----|-----|
| <img src="https://github.com/plnspineda/pln_public/blob/pln/images/purge_dups/flye/Rplot_Wagyu_repeat.png" width="450" /> | <img src="https://github.com/plnspineda/pln_public/blob/pln/images/purge_dups/flye/Rplot_Wagyu_haps.png" width="450" /> |

**SUMMARY**

- removed the 954 repeats and 387 junks in Tuli (total of 52 Mb)
- removed the 564 repeats and 218 junks in Wagyu (total of 24 Mb)

purged assembly in comparison with before purging:

| assembly     | size | contig |   N50 | max contig |
|--------------|-----:|-------:|------:|-----------:|
| Tuli         | 2.61 | 2116   | 70.22 | 156.4      |
| Tuli purged  | 2.56 | 773    | 70.22 | 156.4      |
| Wagyu        | 2.71 | 1784   | 71    | 156.45     |
| Wagyu purged | 2.69 | 1002   | 71    | 156.45     |

**will proceed polishing with this


## YaHS scaffolding
*2023.03.05*

        #!/bin/bash
        #SBATCH -p batch
        #SBATCH -N 1            # number of nodes
        #SBATCH -n 12            # number of cores
        #SBATCH --time=60:00:00 # time allocation (D-HH:MM:SS)
        #SBATCH --mem=128GB       # memory pool for all cores

        module load arch/haswell
        module load quast/4.5-foss-2016uofa-Python-2.7.11

        # scaffolding cattle genome with repeats less than 1Mb and junks purged
        export PATH=$PATH:/hpcfs/users/a1812753/tools/yahs

        ASM=/hpcfs/groups/phoenix-hpc-avsci/Lloyd_Low/Tuli_x_Wagyu_data/purge_dups/flye_Tuli/filter/Tuli_flyev29_hq_purged.fasta
        BED=/hpcfs/groups/phoenix-hpc-avsci/Lloyd_Low/Tuli_x_Wagyu_data/scaffolding/SALSA_flye/Tuli/Tuli_flyev29_hq_purged_rep1.bed

        yahs --no-contig-ec $ASM $BED
        quast.py yahs.out_scaffolds_final.fa -o quast_yahs.out_scaffolds_final

#### Create juicer hic map

        module load arch/haswell
        module load SAMtools/1.10-foss-2016b
        export PATH=$PATH:/hpcfs/users/a1812753/tools/yahs

        samtools faidx yahs.out_scaffolds_final.fa
        /hpcfs/users/a1812753/tools/yahs/juicer pre -a -o out_JBAT yahs.out.bin yahs.out_scaffolds_final.agp /hpcfs/groups/phoenix-hpc-avsci/Lloyd_Low/Tuli_x_Wagyu_data/purge_dups/flye_Tuli/filter/Tuli_flyev29_hq_purged.fasta.fai > out_JBAT.log 2>&1


        module load juicer_tools/1.8.9-Java-1.8.0_121 SAMtools/1.10-foss-2016b

        ## create scaffolds_final.chrom.sizes

        samtools faidx yahs.out_scaffolds_final.fa
        cut -f 1,2 yahs.out_scaffolds_final.fa.fai > scaffolds_final.chrom.sizes

        (java -jar ${EBROOTJUICER_TOOLS}/juicer_tools.1.8.9_jcuda.0.8.jar pre out_JBAT.txt out_JBAT.hic.part <(cat out_JBAT.log  | grep PRE_C_SIZE | awk '{print $2" "$3}')) && (mv out_JBAT.hic.part out_JBAT.hic)

Statistic results:

| Assembly                   | Tuli       | Wagyu      |
|----------------------------|------------|------------|
| # contigs (>= 0 bp)        | 690        | 880        |
| # contigs (>= 1000 bp)     | 669        | 851        |
| # contigs (>= 5000 bp)     | 533        | 656        |
| # contigs (>= 10000 bp)    | 454        | 553        |
| # contigs (>= 25000 bp)    | 335        | 377        |
| # contigs (>= 50000 bp)    | 264        | 274        |
| Total length (>= 0 bp)     | 2560599307 | 2687634333 |
| Total length (>= 1000 bp)  | 2560586638 | 2687614744 |
| Total length (>= 5000 bp)  | 2560239087 | 2687106583 |
| Total length (>= 10000 bp) | 2559663983 | 2686316574 |
| Total length (>= 25000 bp) | 2557759508 | 2683544914 |
| Total length (>= 50000 bp) | 2555106630 | 2679913117 |
| # contigs                  | 688        | 877        |
| Largest contig             | 156401090  | 156450840  |
| Total length               | 2560598814 | 2687634011 |
| GC (%)                     | 42.12      | 41.97      |
| N50                        | 101914841  | 103799677  |
| N75                        | 69673243   | 70154425   |
| L50                        | 11         | 11         |
| L75                        | 19         | 20         |
| # N's per 100 kbp          | 0.68       | 0.93       |

## Dotplot

|    | Tuli           | contigs |   | alignment proportion | length proportion |   | Wagyu       | contigs |   | alignment proportion | length proportion |
|----|----------------|---------|---|----------------------|-------------------|---|-------------|---------|---|----------------------|-------------------|
| 1  | scaffold_1, 39 | 3       | - | 92.53                | 98.65             |   | scaffold_1  | 1       | + | 95.93                | 98.69             |
| 2  | scaffold_2     | 1       | - | 97.75                | 100.20            |   | scaffold_3  | 1       | - | 97.60                | 99.97             |
| 3  | scaffold_5     | 6       | + | 95.80                | 99.79             |   | scaffold_5  | 6       | - | 93.95                | 99.79             |
| 4  | scaffold_4     | 1       | + | 94.65                | 100.88            |   | scaffold_4  | 2       | - | 96.65                | 101.04            |
| 5  | scaffold_3     | 3       | + | 97.35                | 100.92            |   | scaffold_6  | 5       | + | 97.58                | 99.63             |
| 6  | scaffold_6     | 7       | + | 94.20                | 99.83             |   | scaffold_7  | 2       | + | 96.34                | 99.83             |
| 7  | scaffold_8     | 1       | + | 91.06                | 99.96             |   | scaffold_9  | 2       | - | 93.82                | 100.08            |
| 8  | scaffold_7     | 3       | + | 93.81                | 99.73             |   | scaffold_8  | 3       | + | 96.95                | 99.90             |
| 9  | scaffold_10    | 2       | + | 97.13                | 98.69             |   | scaffold_11 | 1       | - | 96.65                | 98.43             |
| 10 | scaffold_11    | 3       | - | 92.92                | 98.65             |   | scaffold_12 | 3       | + | 93.38                | 98.96             |
| 11 | scaffold_9     | 2       | + | 98.12                | 100.01            |   | scaffold_10 | 1       | - | 98.28                | 99.81             |
| 12 | scaffold_12    | 3       | - | 94.44                | 101.98            |   | scaffold_13 | 5       | - | 95.07                | 99.24             |
| 13 | scaffold_14    | 6       | - | 98.15                | 100.04            |   | scaffold_15 | 6       | + | 97.97                | 99.84             |
| 14 | scaffold_15    | 2       | - | 99.09                | 99.33             |   | scaffold_17 | 3       | + | 98.81                | 99.74             |
| 15 | scaffold_13    | 1       | + | 92.61                | 98.50             |   | scaffold_14 | 1       | - | 91.09                | 98.78             |
| 16 | scaffold_16    | 5       | + | 96.13                | 100.67            |   | scaffold_16 | 3       | - | 96.11                | 102.33            |
| 17 | scaffold_17    | 2       | - | 98.27                | 99.70             |   | scaffold_18 | 2       | - | 97.97                | 100.33            |
| 18 | scaffold_20    | 7       | + | 95.36                | 99.75             |   | scaffold_21 | 3       | + | 93.57                | 101.19            |
| 19 | scaffold_21    | 2       | - | 97.01                | 100.34            |   | scaffold_22 | 1       | + | 98.07                | 99.84             |
| 20 | scaffold_18    | 1       | - | 98.58                | 99.54             |   | scaffold_19 | 1       | + | 98.39                | 99.59             |
| 21 | scaffold_19    | 1       | - | 96.96                | 99.73             |   | scaffold_20 | 4       | - | 96.73                | 100.42            |
| 22 | scaffold_23    | 1       | + | 99.87                | 100.20            |   | scaffold_24 | 1       | + | 99.84                | 100.11            |
| 23 | scaffold_24    | 2       | - | 93.53                | 101.57            |   | scaffold_25 | 7       | + | 93.89                | 102.85            |
| 24 | scaffold_22    | 1       | - | 99.13                | 99.85             |   | scaffold_23 | 1       | + | 98.54                | 101.27            |
| 25 | scaffold_29    | 1       | - | 99.81                | 100.31            |   | scaffold_30 | 1       | + | 99.87                | 100.31            |
| 26 | scaffold_25    | 3       | + | 94.24                | 99.59             |   | scaffold_26 | 3       | - | 94.15                | 99.24             |
| 27 | scaffold_28    | 3       | + | 95.85                | 99.14             |   | scaffold_29 | 3       | + | 96.69                | 98.67             |
| 28 | scaffold_27    | 2       | - | 99.62                | 100.16            |   | scaffold_28 | 2       | - | 99.67                | 100.32            |
| 29 | scaffold_26    | 4       | + | 97.44                | 100.35            |   | scaffold_27 | 4       | - | 97.25                | 100.34            |
| X  |                |         |   |                      |                   |   | scaffold_2  | 49      | + | 75.71                | 102.21            |

*proportion with ARS-UCD1.3

| Tuli_Chromosome_1 | Wagyu_Chromosome_1|
|---------------------|---------------------|
| <img src="https://github.com/plnspineda/pln_public/blob/pln/images/YaHS/Tuli/Chromosome_10.png" width="550" /> | <img src="https://github.com/plnspineda/pln_public/blob/pln/images/YaHS/Wagyu/Chromosome_10.png" width="550" /> |

| Tuli_Chromosome_2 | Wagyu_Chromosome_2|
|---------------------|---------------------|
| <img src="https://github.com/plnspineda/pln_public/blob/pln/images/YaHS/Tuli/Chromosome_20.png" width="550" /> | <img src="https://github.com/plnspineda/pln_public/blob/pln/images/YaHS/Wagyu/Chromosome_20.png" width="550" /> |

| Tuli_Chromosome_3 | Wagyu_Chromosome_3|
|---------------------|---------------------|
| <img src="https://github.com/plnspineda/pln_public/blob/pln/images/YaHS/Tuli/Chromosome_30.png" width="550" /> | <img src="https://github.com/plnspineda/pln_public/blob/pln/images/YaHS/Wagyu/Chromosome_30.png" width="550" /> |

| Tuli_Chromosome_4 | Wagyu_Chromosome_4|
|---------------------|---------------------|
| <img src="https://github.com/plnspineda/pln_public/blob/pln/images/YaHS/Tuli/Chromosome_40.png" width="550" /> | <img src="https://github.com/plnspineda/pln_public/blob/pln/images/YaHS/Wagyu/Chromosome_40.png" width="550" /> |

| Tuli_Chromosome_5 | Wagyu_Chromosome_5|
|---------------------|---------------------|
| <img src="https://github.com/plnspineda/pln_public/blob/pln/images/YaHS/Tuli/Chromosome_50.png" width="550" /> | <img src="https://github.com/plnspineda/pln_public/blob/pln/images/YaHS/Wagyu/Chromosome_50.png" width="550" /> |

| Tuli_Chromosome_6 | Wagyu_Chromosome_6|
|---------------------|---------------------|
| <img src="https://github.com/plnspineda/pln_public/blob/pln/images/YaHS/Tuli/Chromosome_60.png" width="550" /> | <img src="https://github.com/plnspineda/pln_public/blob/pln/images/YaHS/Wagyu/Chromosome_60.png" width="550" /> |

| Tuli_Chromosome_7 | Wagyu_Chromosome_7|
|---------------------|---------------------|
| <img src="https://github.com/plnspineda/pln_public/blob/pln/images/YaHS/Tuli/Chromosome_70.png" width="550" /> | <img src="https://github.com/plnspineda/pln_public/blob/pln/images/YaHS/Wagyu/Chromosome_70.png" width="550" /> |

| Tuli_Chromosome_8 | Wagyu_Chromosome_8|
|---------------------|---------------------|
| <img src="https://github.com/plnspineda/pln_public/blob/pln/images/YaHS/Tuli/Chromosome_80.png" width="550" /> | <img src="https://github.com/plnspineda/pln_public/blob/pln/images/YaHS/Wagyu/Chromosome_80.png" width="550" /> |

| Tuli_Chromosome_9 | Wagyu_Chromosome_9|
|---------------------|---------------------|
| <img src="https://github.com/plnspineda/pln_public/blob/pln/images/YaHS/Tuli/Chromosome_90.png" width="550" /> | <img src="https://github.com/plnspineda/pln_public/blob/pln/images/YaHS/Wagyu/Chromosome_90.png" width="550" /> |

| Tuli_Chromosome_10 | Wagyu_Chromosome_10|
|---------------------|---------------------|
| <img src="https://github.com/plnspineda/pln_public/blob/pln/images/YaHS/Tuli/Chromosome_100.png" width="550" /> | <img src="https://github.com/plnspineda/pln_public/blob/pln/images/YaHS/Wagyu/Chromosome_100.png" width="550" /> |

| Tuli_Chromosome_11 | Wagyu_Chromosome_11|
|---------------------|---------------------|
| <img src="https://github.com/plnspineda/pln_public/blob/pln/images/YaHS/Tuli/Chromosome_110.png" width="550" /> | <img src="https://github.com/plnspineda/pln_public/blob/pln/images/YaHS/Wagyu/Chromosome_110.png" width="550" /> |

| Tuli_Chromosome_12 | Wagyu_Chromosome_12|
|---------------------|---------------------|
| <img src="https://github.com/plnspineda/pln_public/blob/pln/images/YaHS/Tuli/Chromosome_120.png" width="550" /> | <img src="https://github.com/plnspineda/pln_public/blob/pln/images/YaHS/Wagyu/Chromosome_120.png" width="550" /> |

| Tuli_Chromosome_13 | Wagyu_Chromosome_13|
|---------------------|---------------------|
| <img src="https://github.com/plnspineda/pln_public/blob/pln/images/YaHS/Tuli/Chromosome_130.png" width="550" /> | <img src="https://github.com/plnspineda/pln_public/blob/pln/images/YaHS/Wagyu/Chromosome_130.png" width="550" /> |

| Tuli_Chromosome_14 | Wagyu_Chromosome_14|
|---------------------|---------------------|
| <img src="https://github.com/plnspineda/pln_public/blob/pln/images/YaHS/Tuli/Chromosome_140.png" width="550" /> | <img src="https://github.com/plnspineda/pln_public/blob/pln/images/YaHS/Wagyu/Chromosome_140.png" width="550" /> |

| Tuli_Chromosome_15 | Wagyu_Chromosome_15|
|---------------------|---------------------|
| <img src="https://github.com/plnspineda/pln_public/blob/pln/images/YaHS/Tuli/Chromosome_150.png" width="550" /> | <img src="https://github.com/plnspineda/pln_public/blob/pln/images/YaHS/Wagyu/Chromosome_150.png" width="550" /> |

| Tuli_Chromosome_16 | Wagyu_Chromosome_16|
|---------------------|---------------------|
| <img src="https://github.com/plnspineda/pln_public/blob/pln/images/YaHS/Tuli/Chromosome_160.png" width="550" /> | <img src="https://github.com/plnspineda/pln_public/blob/pln/images/YaHS/Wagyu/Chromosome_160.png" width="550" /> |

| Tuli_Chromosome_17 | Wagyu_Chromosome_17|
|---------------------|---------------------|
| <img src="https://github.com/plnspineda/pln_public/blob/pln/images/YaHS/Tuli/Chromosome_170.png" width="550" /> | <img src="https://github.com/plnspineda/pln_public/blob/pln/images/YaHS/Wagyu/Chromosome_170.png" width="550" /> |

| Tuli_Chromosome_18 | Wagyu_Chromosome_18|
|---------------------|---------------------|
| <img src="https://github.com/plnspineda/pln_public/blob/pln/images/YaHS/Tuli/Chromosome_180.png" width="550" /> | <img src="https://github.com/plnspineda/pln_public/blob/pln/images/YaHS/Wagyu/Chromosome_180.png" width="550" /> |

| Tuli_Chromosome_19 | Wagyu_Chromosome_19|
|---------------------|---------------------|
| <img src="https://github.com/plnspineda/pln_public/blob/pln/images/YaHS/Tuli/Chromosome_190.png" width="550" /> | <img src="https://github.com/plnspineda/pln_public/blob/pln/images/YaHS/Wagyu/Chromosome_190.png" width="550" /> |

| Tuli_Chromosome_20 | Wagyu_Chromosome_20|
|---------------------|---------------------|
| <img src="https://github.com/plnspineda/pln_public/blob/pln/images/YaHS/Tuli/Chromosome_200.png" width="550" /> | <img src="https://github.com/plnspineda/pln_public/blob/pln/images/YaHS/Wagyu/Chromosome_200.png" width="550" /> |

| Tuli_Chromosome_21 | Wagyu_Chromosome_21|
|---------------------|---------------------|
| <img src="https://github.com/plnspineda/pln_public/blob/pln/images/YaHS/Tuli/Chromosome_210.png" width="550" /> | <img src="https://github.com/plnspineda/pln_public/blob/pln/images/YaHS/Wagyu/Chromosome_210.png" width="550" /> |

| Tuli_Chromosome_22 | Wagyu_Chromosome_22|
|---------------------|---------------------|
| <img src="https://github.com/plnspineda/pln_public/blob/pln/images/YaHS/Tuli/Chromosome_220.png" width="550" /> | <img src="https://github.com/plnspineda/pln_public/blob/pln/images/YaHS/Wagyu/Chromosome_220.png" width="550" /> |

| Tuli_Chromosome_23 | Wagyu_Chromosome_23|
|---------------------|---------------------|
| <img src="https://github.com/plnspineda/pln_public/blob/pln/images/YaHS/Tuli/Chromosome_230.png" width="550" /> | <img src="https://github.com/plnspineda/pln_public/blob/pln/images/YaHS/Wagyu/Chromosome_230.png" width="550" /> |

| Tuli_Chromosome_24 | Wagyu_Chromosome_24|
|---------------------|---------------------|
| <img src="https://github.com/plnspineda/pln_public/blob/pln/images/YaHS/Tuli/Chromosome_240.png" width="550" /> | <img src="https://github.com/plnspineda/pln_public/blob/pln/images/YaHS/Wagyu/Chromosome_240.png" width="550" /> |

| Tuli_Chromosome_25 | Wagyu_Chromosome_25|
|---------------------|---------------------|
| <img src="https://github.com/plnspineda/pln_public/blob/pln/images/YaHS/Tuli/Chromosome_250.png" width="550" /> | <img src="https://github.com/plnspineda/pln_public/blob/pln/images/YaHS/Wagyu/Chromosome_250.png" width="550" /> |

| Tuli_Chromosome_26 | Wagyu_Chromosome_26|
|---------------------|---------------------|
| <img src="https://github.com/plnspineda/pln_public/blob/pln/images/YaHS/Tuli/Chromosome_260.png" width="550" /> | <img src="https://github.com/plnspineda/pln_public/blob/pln/images/YaHS/Wagyu/Chromosome_260.png" width="550" /> |

| Tuli_Chromosome_27 | Wagyu_Chromosome_27|
|---------------------|---------------------|
| <img src="https://github.com/plnspineda/pln_public/blob/pln/images/YaHS/Tuli/Chromosome_270.png" width="550" /> | <img src="https://github.com/plnspineda/pln_public/blob/pln/images/YaHS/Wagyu/Chromosome_270.png" width="550" /> |

| Tuli_Chromosome_28 | Wagyu_Chromosome_28|
|---------------------|---------------------|
| <img src="https://github.com/plnspineda/pln_public/blob/pln/images/YaHS/Tuli/Chromosome_280.png" width="550" /> | <img src="https://github.com/plnspineda/pln_public/blob/pln/images/YaHS/Wagyu/Chromosome_280.png" width="550" /> |

| Tuli_Chromosome_29 | Wagyu_Chromosome_29|
|---------------------|---------------------|
| <img src="https://github.com/plnspineda/pln_public/blob/pln/images/YaHS/Tuli/Chromosome_290.png" width="550" /> | <img src="https://github.com/plnspineda/pln_public/blob/pln/images/YaHS/Wagyu/Chromosome_290.png" width="550" /> |

| Tuli_Chromosome_Y | Wagyu_Chromosome_X|
|---------------------|---------------------|
| -Y-still to assemble- | <img src="https://github.com/plnspineda/pln_public/blob/pln/images/YaHS/Wagyu/Chromosome_X0.png" width="550" /> |


*2023.03.20*

## Scaffolding comparison (default run vs no-error correction)


## Polishing with Pepper-Margin-DeepVariant and Merfin

1. First map the reads to the reference assembly using minimap2

        module purge
        module load arch/haswell
        module load minimap2/2.24
        module load SAMtools/1.10-foss-2016b

        READS=/hpcfs/groups/phoenix-hpc-avsci/Lloyd_Low/Tuli_x_Wagyu_data/haplotype/haplotype-Tuli_sire.fastq.gz
        ASM=/hpcfs/groups/phoenix-hpc-avsci/Lloyd_Low/Tuli_x_Wagyu_data/purge_dups/flye_Tuli/filter/Tuli_flyev29_hq_purged.fasta

        read_base=(`basename $READS`)
        read_base=${read_base%.fasta}

        minimap2 -ax map-ont -t 24 $ASM $READS | samtools view -hb -F 0x904 > $read_base'_unsorted_0x904.bam'
        samtools sort -@24 -o $read_base'_sorted_0x904.bam' $read_base'_unsorted_0x904.bam'
        samtools index -@24 $read_base'_sorted_0x904.bam'

        # -F 0x904 -> count only primary alignments and exclude uncertain alignments
        # -hb -> output in bam with header

2. Run pepper-DeepVariant

Note: had to change `tmp` folder to the group account because it requires ~2Gb of tmp memory

        module load arch/haswell
        module load Singularity/3.7.4
        export TMPDIR=./tmp

        # singularity pull docker://kishwars/pepper_deepvariant:r0.8
        # r0.8 does not support polishing, it's only up to r0.4

        singularity exec --bind /usr/lib/locale/ \
        ../../docker_images/pepper_deepvariant_r0.8.sif \
        run_pepper_margin_deepvariant call_variant \
        -b haplotype-Tuli_sire.fastq.gz_sorted_0x904.bam \
        -f /hpcfs/groups/phoenix-hpc-avsci/Lloyd_Low/Tuli_x_Wagyu_data/purge_dups/flye_Tuli/filter/Tuli_flyev29_hq_purged.fasta \
        -o output \
        -t 24 \
        -p Tuli_flyev29_hq_purged \
        --ont_r9_guppy5_sup

DeepVariant VCF output notes: PASS -> When an entry has PASS, it means that a candidate was generated and the neural network classifier gave the probability of the non-reference genotype call as higher than for reference; RefCall -> When an entry has RefCall present, it means that a candidate was generated and the neural network classifier gave a higher probability for a reference call [github query](https://github.com/google/deepvariant/issues/278)


3. Filter spurious variant calls with low stringency filters (QUAL less than 1)

        bcftools filter -e 'GT=="RR" || QUAL<=1' -Ov output/Tuli_flyev29_hq_purged.vcf.gz >  output/Tuli_flyev29_hq_purged_filtered.vcf

        # -e 'GT=="RR" || QUAL<=1' -> exclude homozygous ref calls (0/0) and quals that are less than 1
        # -Ov -> (output type) output vcf

4. Polish assembly with merfin

        # a. Create a meryl file of the assembly
        singularity exec /apps/containers/merqury_v1.3.sif meryl count k=21 $ASM output merfin_polish/assembly.meryl

        # b. Filter F1 meryl with kmer count less than 10
        singularity exec /apps/containers/merqury_v1.3.sif meryl greater-than 10 F1.meryl output F1_reads_k21.gt10.meryl

        # c. To get the -peak value, run the short reads with genomescope and use the haploid peak.
        export PATH=$PATH:/hpcfs/users/a1812753/tools/genomescope2.0
        genomescope.R -i F1.histo -o genomescope_output -k 21

<img src="https://github.com/plnspineda/pln_public/blob/pln/images/polishing/genomescope_gt_and_peak.png" width="550" />

        Run with merfin

        module load arch/haswell Singularity/3.7.4
        export PATH=$PATH:/hpcfs/users/a1812753/tools/merfin/merfin/build/bin

        merfin -polish -sequence $ASM -seqmers merfin_polish/assembly.meryl -readmers $READMR -peak 27 -vcf output/Tuli_flyev29_hq_purged_filtered.vcf -output merfin_polish/Tuli_flyev29_hq_purged_filtered_merfinpolish.vcf 2> merfin_polish/Tuli_flyev29_hq_purged_filtered_merfinpolish.err

5. Create consensus sequence by applying VCF variants to a reference fasta file

        module load arch/haswell BCFtools/1.9

        bcftools view -Oz merfin_polish/Tuli_flyev29_hq_purged_filtered_merfinpolish.vcf.polish.vcf -o merfin_polish/Tuli_flyev29_hq_purged_filtered_merfinpolish.vcf.polish.vcf.gz

        bcftools index --threads 16 merfin_polish/Tuli_flyev29_hq_purged_filtered_merfinpolish.vcf.polish.vcf.gz

        bcftools consensus -H1 -f /hpcfs/groups/phoenix-hpc-avsci/Lloyd_Low/Tuli_x_Wagyu_data/purge_dups/flye_Tuli/filter/Tuli_flyev29_hq_purged.fasta -o merfin_polish/Tuli_flyev29_hq_purged_filtered_merfinpolish_H1.fasta merfin_polish/Tuli_flyev29_hq_purged_filtered_merfinpolish.vcf.polish.vcf.gz

        ## -Oz -> (output type) output compressed vcf file
        ## -H1 -> use the first allele, regardless of phasing
        ## -f -> reference sequence in fasta format

Output files:

location: /hpcfs/groups/phoenix-hpc-avsci/Lloyd_Low/Tuli_x_Wagyu_data/polishing/flye_nanohq/Tuli_pepper_r0.8/output

        intermediate_files  Tuli_flyev29_hq_purged_filtered.vcf  Tuli_flyev29_hq_purged.vcf.gz.tbi
        logs                Tuli_flyev29_hq_purged.vcf.gz        Tuli_flyev29_hq_purged.visual_report.html

location: /hpcfs/groups/phoenix-hpc-avsci/Lloyd_Low/Tuli_x_Wagyu_data/polishing/flye_nanohq/Tuli_pepper_r0.8/merfin_polish

        assembly.meryl                                         Tuli_flyev29_hq_purged_filtered_merfinpolish.vcf.polish.vcf
        Tuli_flyev29_hq_purged_filtered_merfinpolish.err       Tuli_flyev29_hq_purged_filtered_merfinpolish.vcf.polish.vcf.gz
        Tuli_flyev29_hq_purged_filtered_merfinpolish_H1.fasta  Tuli_flyev29_hq_purged_filtered_merfinpolish.vcf.polish.vcf.gz.csi

final polished assembly.fasta -> Tuli_flyev29_hq_purged_filtered_merfinpolish_H1.fasta

#### Result
