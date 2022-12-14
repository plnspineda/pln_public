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

- removed the 954 repeats and 387 junks in Tuli
- removed the 564 repeats and 218 junks in Wagyu

purged assembly in comparison with before purging:

| assembly     | size | contig |   N50 | max contig |
|--------------|-----:|-------:|------:|-----------:|
| Tuli         | 2.61 | 2116   | 70.22 | 156.4      |
| Tuli purged  | 2.56 | 773    | 70.22 | 156.4      |
| Wagyu        | 2.71 | 1784   | 71    | 156.45     |
| Wagyu purged | 2.69 | 1002   | 71    | 156.45     |

**will proceed polishing with this
