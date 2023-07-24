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

### Scaffolding comparison (default run vs no-error correction)

Statistic results:

*2023.03.18*

| Assembly                   | Tuli_default | Wagyu_default | Tuli_noerror-corr | Wagyu_noerror-corr |
|----------------------------|--------------|---------------|-------------------|--------------------|
| # contigs (>= 0 bp)        | 730          | 913           | 690               | 880                |
| # contigs (>= 1000 bp)     | 709          | 884           | 669               | 851                |
| # contigs (>= 5000 bp)     | 570          | 687           | 533               | 656                |
| # contigs (>= 10000 bp)    | 490          | 584           | 454               | 553                |
| # contigs (>= 25000 bp)    | 372          | 406           | 335               | 377                |
| # contigs (>= 50000 bp)    | 299          | 301           | 264               | 274                |
| Total length (>= 0 bp)     | 2560600107   | 2687634733    | 2560599307        | 2687634333         |
| Total length (>= 1000 bp)  | 2560587438   | 2687615144    | 2560586638        | 2687614744         |
| Total length (>= 5000 bp)  | 2560233887   | 2687102983    | 2560239087        | 2687106583         |
| Total length (>= 10000 bp) | 2559652783   | 2686312974    | 2559663983        | 2686316574         |
| Total length (>= 25000 bp) | 2557771513   | 2683507314    | 2557759508        | 2683544914         |
| Total length (>= 50000 bp) | 2555055301   | 2679807919    | 2555106630        | 2679913117         |
| # contigs                  | 728          | 910           | 688               | 877                |
| Largest contig             | 156401090    | 156450840     | 156401090         | 156450840          |
| Total length               | 2560599614   | 2687634411    | 2560598814        | 2687634011         |
| GC (%)                     | 42.12        | 41.97         | 42.12             | 41.97              |
| N50                        | 101914841    | 103799677     | 101914841         | 103799677          |
| N75                        | 69673243     | 71675967      | 69673243          | 70154425           |
| L50                        | 11           | 11            | 11                | 11                 |
| L75                        | 19           | 19            | 19                | 20                 |
| # N's per 100 kbp          | 0.71         | 0.95          | 0.68              | 0.93               |


Comparison on the size of chromosomes and number of contigs

| Chromosomes | Tuli        | deafult run contigs | size      | with contig breaks? | no errro corr contigs | size      | size difference |
|-------------|-------------|---------------------|-----------|---------------------|-----------------------|-----------|-----------------|
| 1           | scaffold_1  | 1                   | 156401090 |                     | 1                     | 156401090 | 0               |
| 2           | scaffold_2  | 1                   | 136506533 |                     | 1                     | 136506533 | 0               |
| 3           | scaffold_5  | 6                   | 120752645 |                     | 6                     | 120752645 | 0               |
| 4           | scaffold_4  | 1                   | 121056641 |                     | 1                     | 121056641 | 0               |
| 5           | scaffold_3  | 3                   | 121194679 |                     | 3                     | 121194679 | 0               |
| 6           | scaffold_6  | 7                   | 117602346 | Yes (1) 11/13       | 7                     | 117608346 | 6000            |
| 7           | scaffold_8  | 1                   | 110569000 | Yes (1) 1/1         | 1                     | 110636286 | 67286           |
| 8           | scaffold_7  | 3                   | 113011192 |                     | 3                     | 113011192 | 0               |
| 9           | scaffold_10 | 2                   | 104069468 |                     | 2                     | 104069468 | 0               |
| 10          | scaffold_11 | 3                   | 101914841 |                     | 3                     | 101914841 | 0               |
| 11          | scaffold_9  | 2                   | 106993904 |                     | 2                     | 106993904 | 0               |
| 12          | scaffold_12 | 3                   | 88765974  | Yes (1) 5/5         | 3                     | 88940898  | 174924          |
| 13          | scaffold_14 | 6                   | 83502111  |                     | 6                     | 83502111  | 0               |
| 14          | scaffold_15 | 4                   | 82066655  | Yes (2) 1/7         | 2                     | 81847367  | -219288         |
| 15          | scaffold_13 | 1                   | 83729664  |                     | 1                     | 83729664  | 0               |
| 16          | scaffold_16 | 5                   | 81560757  |                     | 5                     | 81560757  | 0               |
| 17          | scaffold_17 | 2                   | 72946751  |                     | 2                     | 72946751  | 0               |
| 18          | scaffold_20 | 7                   | 65603004  | Yes (1) 11/13       | 7                     | 65657273  | 54269           |
| 19          | scaffold_21 | 3                   | 63595365  | Yes (1)* 3,5/5      | 2                     | 63668066  | 72701           |
| 20          | scaffold_18 | 1                   | 71644399  |                     | 1                     | 71644399  | 0               |
| 21          | scaffold_19 | 1                   | 69673243  |                     | 1                     | 69673243  | 0               |
| 22          | scaffold_23 | 1                   | 60896241  |                     | 1                     | 60896241  | 0               |
| 23          | scaffold_24 | 2                   | 53320223  |                     | 2                     | 53320223  | 0               |
| 24          | scaffold_22 | 1                   | 62221011  |                     | 1                     | 62221011  | 0               |
| 25          | scaffold_29 | 1                   | 42480646  |                     | 1                     | 42480646  | 0               |
| 26          | scaffold_25 | 3                   | 51777404  |                     | 3                     | 51777404  | 0               |
| 27          | scaffold_28 | 3                   | 45220362  |                     | 3                     | 45220362  | 0               |
| 28          | scaffold_27 | 2                   | 45927334  | Yes (1) 3/3         | 2                     | 46014334  | 87000           |
| 29          | scaffold_26 | 5                   | 51191488  | Yes (2)* 5,7,9/9    | 4                     | 51275218  | 83730           |

| Chromosomes | Wagyu       | deafult run contigs | size      | with contig breaks? | no errro corr contigs | size      | size difference |
|-------------|-------------|---------------------|-----------|---------------------|-----------------------|-----------|-----------------|
| 1           | scaffold_1  | 1                   | 156450840 |                     | 1                     | 156450840 | 0               |
| 2           | scaffold_3  | 1                   | 136113000 | Yes (1) 1/1         | 1                     | 136188231 | 75231           |
| 3           | scaffold_5  | 5                   | 120709671 |                     | 6                     | 120747761 | 38090           |
| 4           | scaffold_4  | 2                   | 121167618 | Yes (1) 3/3         | 2                     | 121252075 | 84457           |
| 5           | scaffold_6  | 5                   | 119641076 |                     | 5                     | 119641076 | 0               |
| 6           | scaffold_7  | 2                   | 117602180 |                     | 2                     | 117602180 | 0               |
| 7           | scaffold_9  | 2                   | 110766233 |                     | 2                     | 110766233 | 0               |
| 8           | scaffold_8  | 3                   | 113209785 |                     | 3                     | 113209785 | 0               |
| 9           | scaffold_11 | 1                   | 103799677 |                     | 1                     | 103799677 | 0               |
| 10          | scaffold_12 | 3                   | 102234956 |                     | 3                     | 102234956 | 0               |
| 11          | scaffold_10 | 1                   | 106778547 |                     | 1                     | 106778547 | 0               |
| 12          | scaffold_13 | 15                  | 89761376  | Yes (2) 1,13/29     | 5                     | 86557175  | -3204201        |
| 13          | scaffold_15 | 6                   | 83336454  |                     | 6                     | 83336454  | 0               |
| 14          | scaffold_17 | 3                   | 82129270  | Yes (1) 3/5         | 3                     | 82184713  | 55443           |
| 15          | scaffold_14 | 1                   | 83972338  |                     | 1                     | 83972338  | 0               |
| 16          | scaffold_16 | 3                   | 82897991  |                     | 3                     | 82897991  | 0               |
| 17          | scaffold_18 | 2                   | 73407576  |                     | 2                     | 73407576  | 0               |
| 18          | scaffold_21 | 3                   | 66601248  |                     | 3                     | 66601248  | 0               |
| 19          | scaffold_22 | 1                   | 63347965  |                     | 1                     | 63347965  | 0               |
| 20          | scaffold_19 | 1                   | 71675967  |                     | 1                     | 71675967  | 0               |
| 21          | scaffold_20 | 5                   | 69891745  | Yes (3) 3,5,7/9     | 4                     | 70154425  | 262680          |
| 22          | scaffold_24 | 1                   | 60838928  |                     | 1                     | 60838928  | 0               |
| 23          | scaffold_25 | 7                   | 53992448  |                     | 7                     | 53992448  | 0               |
| 24          | scaffold_23 | 1                   | 63105737  |                     | 1                     | 63105737  | 0               |
| 25          | scaffold_30 | 1                   | 42428083  | Yes (1) 1/1         | 1                     | 42480083  | 52000           |
| 26          | scaffold_26 | 3                   | 51594877  |                     | 3                     | 51594877  | 0               |
| 27          | scaffold_29 | 3                   | 45004584  |                     | 3                     | 45004584  | 0               |
| 28          | scaffold_28 | 2                   | 45933414  |                     | 2                     | 46086501  | 153087          |
| 29          | scaffold_27 | 4                   | 51274347  |                     | 4                     | 51274347  | 0               |
| X           | scaffold_2  | 52                  | 141785956 | Yes (5) 13,29,83,89,97/103   | 49                    | 142086358 | 300402          |

*Chromosome 12 of Wagyu has 3Mb difference between scaffolder default run and no error correction. Dotplot comparison below:

This is due to additional contigs after breaking a contig_772 (70Mbbp vs 71Mbbp) and contig_943 (542kb vs 600kb)

        scaffold_13	1	70940000	1	W	contig_772*	1	70940000	-
        scaffold_13	70940201	71103027	3	W	contig_3190*	1	162827	-
        scaffold_13	71103228	71127801	5	W	contig_951*	1	24574	-
        scaffold_13	71128002	71295610	7	W	contig_2463*	1	167609	-
        scaffold_13	71295811	71475573	9	W	contig_948	1	179763	+
        scaffold_13	71475774	71614103	11	W	contig_2985	1	138330	-
        scaffold_13	71614304	72156614	13	W	contig_943	58001	600311	+
        scaffold_13	72156815	72270226	15	W	contig_937	1	113412	-
        scaffold_13	72270427	72366151	17	W	contig_938	1	95725	-
        scaffold_13	72366352	72540258	19	W	contig_936	1	173907	-
        scaffold_13	72540459	72736907	21	W	contig_952	1	196449	+
        scaffold_13	72737108	73106580	23	W	contig_953	1	369473	-
        scaffold_13	73106781	73914318	25	W	contig_940	1	807538	-
        scaffold_13	73914519	74561394	27	W	contig_947	1	646876	+
        scaffold_13	74561595	89761376	29	W	contig_941*	1	15199782	+

*contigs from the no-error correction

| default run | no-error correction|
|---------------------|---------------------|
| <img src="https://github.com/plnspineda/pln_public/blob/pln/images/YaHS/Wagyu/default_run_Chromosome_120.png" width="550" /> | <img src="https://github.com/plnspineda/pln_public/blob/pln/images/YaHS/Wagyu/Chromosome_120.png" width="550" /> |


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

| Assembly                             | Tuli_purged | Tuli_purged_polished | Wagyu_purged | Wagyu_purged_polished |
|--------------------------------------|-------------|----------------------|--------------|-----------------------|
| QV                                   | 41.1746     | 44.5215              | 41.1734      | 44.3003               |
| K-mer completeness                   | 97.2915     | 93.6457              | 98.1108      | 96.6503               |
| Number of blocks                     | 1034        | 1280                 | 1648         | 1822                  |
| Total bases in blocks (block sum)    | 2541973861  | 2534543002           | 2656508329   | 2649199310            |
| Smallest block size                  | 22          | 22                   | 22           | 22                    |
| Avg. Block size                      | 2458389     | 1980112              | 1611959      | 1454006               |
| Block N50 size                       | 16193355    | 12151121             | 8905807      | 7594324               |
| Longest block size                   | 88307157    | 43776608             | 41396731     | 34440230              |
| Num. of markers from other haplotype | 136413      | 133900               | 213646       | 198939                |
| total num. of markers in block       | 64906474    | 62530878             | 47130708     | 46422800              |
| switch error rate                    | 0.21017%    | 0.21413%             | 0.45331%     | 0.42854%              |

| spectra_asm_purged | spectra_asm_purged_polished|
|---------------------|---------------------|
| <img src="https://github.com/plnspineda/pln_public/blob/pln/images/polishing/QV.spectra-asm_purged.fl.png" width="550" /> | <img src="https://github.com/plnspineda/pln_public/blob/pln/images/polishing/QV.spectra-asm.fl_polished.png" width="550" /> |

Continuity of the phasing

| Tuli_purged | Tuli_purged_polished|
|---------------------|---------------------|
| <img src="https://github.com/plnspineda/pln_public/blob/pln/images/polishing/QV.Tuli_flyev29_hq_purged.continuity.N.png" width="550" /> | <img src="https://github.com/plnspineda/pln_public/blob/pln/images/polishing/QV.Tuli_flyev29_hq_purged_filtered_merfinpolish_H1.continuity.N.png" width="550" /> |

| Wagyu_purged | Wagyu_purged_polished|
|---------------------|---------------------|
| <img src="https://github.com/plnspineda/pln_public/blob/pln/images/polishing/QV.Wagyu_flyev29_hq_purged.continuity.N.png" width="550" /> | <img src="https://github.com/plnspineda/pln_public/blob/pln/images/polishing/QV.Wagyu_flyev29_hq_purged_filtered_merfinpolish_H1.continuity.N.png" width="550" /> |

Phased blocks

| Tuli_purged | Tuli_purged_polished|
|---------------------|---------------------|
| <img src="https://github.com/plnspineda/pln_public/blob/pln/images/polishing/QV.Tuli_flyev29_hq_purged.block.N.png" width="550" /> | <img src="https://github.com/plnspineda/pln_public/blob/pln/images/polishing/QV.Tuli_flyev29_hq_purged_filtered_merfinpolish_H1.block.N.png" width="550" /> |

| Wagyu_purged | Wagyu_purged_polished|
|---------------------|---------------------|
| <img src="https://github.com/plnspineda/pln_public/blob/pln/images/polishing/QV.Wagyu_flyev29_hq_purged.block.N.png" width="550" /> | <img src="https://github.com/plnspineda/pln_public/blob/pln/images/polishing/QV.Wagyu_flyev29_hq_purged_filtered_merfinpolish_H1.block.N.png" width="550" /> |

Notes:

Determining peak with genomescope:

  As a rule of thumb, the -peak should be chosen from: \
  - haploid peak: partially-phased (assembly has both primary and alternate haplotigs) or fully-phased assemblies (i.e. trio-binning, trio-hifiasm, ...)

There is recommendation to create --fitted_hist: \
*The lookup table can be generated with --fitted_hist option we added to GenomeScope 2.0. The probability is estimated for 0 to 4-copy kmer multiplicity and is prioritized over the estimates from -peak. Providing the fitted probability significantly improves the accuracy of all analyses.*

From the paper: \
 *In a trio setting, the optimal approach is to polish each parental assembly separately, by aligning the binned reads and performing variant calling. This will reduce the introduction of haplotype switches. However, our k-mer-based evaluation of the corrections is best performed on a combined assembly so that it faithfully represents the expected copy-number of each k-mer given the read set.*

---------------------------

To identify breakpoints from YaHS with default run (with error correction), will run the following:

input data: scaffold.agp file and scaffold.fasta file

1. get the duplicate contig in .agp file at column 6, ignoring the "200" since it's a gap
2. if the duplicate contig starts with "1" at column 7, get the scaffold gap region after at column 3, otherwise get the scaffold region at column 2.
3. extract the region from the scaffold fasta file, and take only column 3 + 10200bp if column 7 is "1", otherwise get column 2 + 5000bp and column 2 - 10200bp.
4. blast the scaffold region
5. analyse...

*can't work this out...
---------------------------
 did this instead...

        library(readr)
        library(dplyr)
        library(tidyr)


        ### TULI DEFAULT RUN###

        scaffold_agp_tuli <- read_delim("/home/polen/Documents/Tuli_and_Wagyu/scaffolding/default_run/Tuli-yahs.out_scaffolds_final.agp",
                                   "\t", col_names = FALSE)
        names(scaffold_agp_tuli) <- c("scaffold", "start", "end", "number", "categ", "contig", "con_start", "con_end", "type")

        tuli_number_of_contigs_per_scaffold <- scaffold_agp_tuli %>% subset(contig != "200") %>% group_by(scaffold) %>% tally() %>% mutate(scaffold = as.numeric(gsub("scaffold_","", scaffold)))

        tuli_contig_all_break <- scaffold_agp_tuli %>% subset(contig != "200") %>% group_by(contig) %>% filter(n()>1) %>% mutate(con_len = end - start)
        tuli_contig_non_break <- scaffold_agp_tuli %>% subset(contig != "200") %>% group_by(scaffold, contig) %>% filter(n()>1)
        tuli_contig_break <- tuli_contig_all_break %>% distinct(scaffold, contig, .keep_all = TRUE)

        ### WAGYU DEFAULT RUN###

        scaffold_agp_wagyu <- read_delim("/home/polen/Documents/Tuli_and_Wagyu/scaffolding/default_run/Wagyu-yahs.out_scaffolds_final.agp",
                                   "\t", col_names = FALSE)
        names(scaffold_agp_wagyu) <- c("scaffold", "start", "end", "number", "categ", "contig", "con_start", "con_end", "type")

        wagyu_number_of_contigs_per_scaffold <- scaffold_agp_wagyu %>% subset(contig != "200") %>% group_by(scaffold) %>% tally() %>% mutate(scaffold = as.numeric(gsub("scaffold_","", scaffold)))


        wagyu_contig_all_break <- scaffold_agp_wagyu %>% subset(contig != "200") %>% group_by(contig) %>% filter(n()>1)
        wagyu_contig_non_break <- scaffold_agp_wagyu %>% subset(contig != "200") %>% group_by(scaffold, contig) %>% filter(n()>1)
        wagyu_contig_break <- wagyu_contig_all_break %>% distinct(scaffold, contig, .keep_all = TRUE)


        ##### trying again with a different approach...
        # 1. Make table with contig name and start-end from the agp and get the scaffold name with the breaks
        # 2. Get the whole sequence if end - begin < 50,000 else get the sequence from begin to 50,000.
        # 3. map the sequences
        ### result will give me a paf file with contigs aligned to the reference. I will then compare the contig that broke if the alignment is continuous in the reference

        # 1. Get the contig after the break contig if begin = 1 else, get the contig before
        # 2. map the sequences
        ### result will give me a paf file then I will compare if the contig next to the broken contig aligned continuously with the ref
        # analyse both files; shortest gap with the reference means the correct alignment

        tuli_break_list <- tuli_contig_all_break %>%
          mutate(con_end = as.numeric(con_end), con_start = as.numeric(con_start)) %>%
          mutate(map_len = ifelse(con_len < 50000, NA,
                                  ifelse(con_start == 1, as.character(con_end - 50000), as.character(con_start + 50000)))) %>%
          mutate(map_reg = case_when(
            con_start == 1 & con_len < 50000 ~ paste0(contig, ":", con_start, "-", con_end),
            con_start == 1 & con_len > 50000 ~ paste0(contig, ":", map_len, "-", con_end),
            con_start != 1 & con_len > 50000 ~ paste0(contig, ":", con_start, "-", map_len),
            con_start != 1 & is.na(map_len) ~ paste0(contig, ":", con_start, "-", con_end),
            con_start != 1 & con_len < 50000 ~ paste0(contig, ":", con_start, "-", map_len),
            TRUE ~ NA_character_
          )) %>% select(scaffold, contig, map_reg, type)

        write_delim(tuli_break_list, delim = "\t", file = "/home/polen/Documents/Tuli_and_Wagyu/scaffolding/default_run/looking_at_breakpoints/fourth_attempt/tuli_break.list")

        ##### looking at breakpoints with paf file

        library(pafr)
        paf <- read_paf("/home/polen/Documents/Tuli_and_Wagyu/scaffolding/default_run/looking_at_breakpoints/fourth_attempt/ARSUCD13_vs_contigbreak.paf")
        paf_filtered <- filter_secondary_alignments(paf) %>% subset(mapq > 0)

        merged_paf <- merge(paf_filtered, tuli_break_list, by.x = "qname", by.y = "map_reg", all.x = TRUE, all.y = FALSE)
        merged_paf <- merged_paf %>%
          select(scaffold, contig, type, qname, qlen, qstart, qend, strand, tname, tstart, tend, nmatch, alen, mapq) %>% arrange(qname, tstart) %>%
          mutate(alen_proportion = alen/qlen*100) %>% filter(alen_proportion >= 30) #%>%
          #group_by(qname) %>%
          #summarise(scaffold = names(which.max(table(scaffold))), contig = names(which.max(table(contig))), min_qstart = min(qstart), max_qend = max(qend), strand = names(which.max(table(strand))),
          #                             min_tstart = min(tstart), max_tend = max(tend), sum_nmatch = sum(nmatch), sum_alen = sum(alen), mapq = round(mean(mapq)), alen_proportion = mean(alen_proportion))


        count_paf <- merged_paf %>% summarise(count = n_distinct(qname))

        ##### locate gaps in the regions

        mapped_regions <- merged_paf %>% group_by(contig) %>% mutate(diff = tstart - lag(tend, default = first(tstart)))
        # mapped_regions <- merged_paf %>% group_by(contig) %>% mutate(diff = min_tstart - lag(max_tend, default = first(min_tstart)))
