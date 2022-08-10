# Tuli x Wagyu dotplot against ARS-UCD1.3

1. [Summary Notes](#summary)
    - [Proportion per chromosomes](#proportion)
2. [Dotplot per chromosomes](#dotplot)
    - [Chromosome 21 and 22](#chr21_22)
3. [Improving/Correcting Chromosome X and Y](#chromosomeXY)

Summary Notes: <a name="summary"></a>

List and number of chromosomes with 1:1 contig-chromosome proportion.
- Tuli => 13 contigs (Chromosomes 2, 3, 7, 9, 10, 14, 17, 18, 22, 24, 25, 26, 27)
- Wagyu => 9 contigs (Chromosomes 2, 3, 10, 14, 15, 16, 25, 26, 28)

**Notes on Wagyu Chromosome_21 and Chromosome_22: contig_28 mapped with both chromosomes and was split to be included to both chromosomes

<img src="https://github.com/plnspineda/pln_public/blob/pln/images/dotplot_Tuli/comparison_chromosome_sizes_withsexchr.png" />

<a name="proportion"></a>

| Chromosome | Proportion of Tuli aligned in ARS-UCD1.3 (%) | Proportion of ARS-UCD1.3 aligned in Tuli (%) | Number of contigs | Proportion of Wagyu aligned in ARS-UCD1.3 (%) | Proportion of ARS-UCD1.3 aligned in Wagyu (%) | Number of contigs |
|-----------:|---------------------------------------------:|---------------------------------------------:|------------------:|----------------------------------------------:|----------------------------------------------:|------------------:|
|          1 |                                        99.20 |                                       100.81 |                 4 |                                         99.03 |                                        100.98 |                 5 |
|          2 |                                       100.01 |                                        99.99 |                 1 |                                         99.87 |                                        100.13 |                 1 |
|          3 |                                        99.86 |                                       100.14 |                 1 |                                         99.77 |                                        100.23 |                 1 |
|          4 |                                        99.94 |                                       100.06 |                 2 |                                         99.93 |                                        100.07 |                 4 |
|          5 |                                        99.90 |                                       100.10 |                 3 |                                         99.54 |                                        100.46 |                 2 |
|          6 |                                       100.10 |                                        99.90 |                 4 |                                        100.05 |                                         99.95 |                 3 |
|          7 |                                        99.89 |                                       100.11 |                 1 |                                         99.79 |                                        100.21 |                 8 |
|          8 |                                        99.59 |                                       100.42 |                 2 |                                         99.43 |                                        100.58 |                 5 |
|          9 |                                        97.54 |                                       102.53 |                 1 |                                         98.29 |                                        101.74 |                 3 |
|         10 |                                        98.61 |                                       101.41 |                 1 |                                         98.26 |                                        101.77 |                 1 |
|         11 |                                        99.81 |                                       100.19 |                 3 |                                         99.71 |                                        100.29 |                 4 |
|         12 |                                       101.84 |                                        98.19 |                 2 |                                         99.80 |                                        100.20 |                 5 |
|         13 |                                        99.86 |                                       100.14 |                 5 |                                         99.77 |                                        100.23 |                 7 |
|         14 |                                        99.60 |                                       100.40 |                 1 |                                         98.15 |                                        101.89 |                 1 |
|         15 |                                       100.97 |                                        99.04 |                 6 |                                         98.73 |                                        101.29 |                 1 |
|         16 |                                        99.56 |                                       100.44 |                 7 |                                        100.62 |                                         99.38 |                 1 |
|         17 |                                       100.00 |                                       100.00 |                 1 |                                         99.49 |                                        100.51 |                 2 |
|         18 |                                       100.08 |                                        99.92 |                 1 |                                        100.02 |                                         99.98 |                 4 |
|         19 |                                       100.16 |                                        99.84 |                 4 |                                         99.64 |                                        100.37 |                 5 |
|         20 |                                        98.51 |                                       101.51 |                 3 |                                         99.63 |                                        100.38 |                 2 |
|         21 |                                       100.54 |                                        99.46 |                10 |                                         99.80 |                                        100.20 |                 8 |
|         22 |                                       100.57 |                                        99.43 |                 1 |                                        100.09 |                                         99.91 |                 2 |
|         23 |                                       102.68 |                                        97.39 |                 5 |                                        101.81 |                                         98.22 |                 2 |
|         24 |                                       100.99 |                                        99.02 |                 1 |                                        100.57 |                                         99.43 |                 8 |
|         25 |                                        99.93 |                                       100.07 |                 1 |                                        100.07 |                                         99.93 |                 1 |
|         26 |                                        99.62 |                                       100.39 |                 1 |                                         99.51 |                                        100.49 |                 1 |
|         27 |                                       100.23 |                                        99.77 |                 1 |                                         98.90 |                                        101.12 |                 2 |
|         28 |                                        99.90 |                                       100.10 |                 4 |                                        100.88 |                                         99.13 |                 1 |
|         29 |                                       100.64 |                                        99.36 |                11 |                                        101.13 |                                         98.88 |                 4 |
|      X / Y |                                        69.80 |                                       143.26 |                 4 |                                         97.52 |                                        102.55 |                49 |
|            |                                              |                          TOTAL CONTIGS       | 92                |                                               |                         TOTAL CONTIGS         | 142                |

## Dot plot per chromosomes <a name="dotplot"></a>

Prop_ref (Proportion reference) = query length / reference length

| Tuli_Chromosome_1 | Wagyu_Chromosome_1|
|---------------------|---------------------|
| 4 contigs | 5 contigs |
| Prop_ref (%) = 0.38, 42.64, 55.14, 0.01 | Prop_ref (%) = 0.10, 0.33, 6.40, 35.95, 55.27 |
| <img src="https://github.com/plnspineda/pln_public/blob/pln/images/dotplot_Tuli/Chromosome_1.png" width="550" /> | <img src="https://github.com/plnspineda/pln_public/blob/pln/images/dotplot_Wagyu/Chromosome_1.png" width="550" /> |

| Tuli_Chromosome_2 | Wagyu_Chromosome_2|
|---------------------|---------------------|
| 1 contig | 1 contig |
| Prop_ref (%) = 100.00 | Prop_ref (%) = 99.87 |
| <img src="https://github.com/plnspineda/pln_public/blob/pln/images/dotplot_Tuli/Chromosome_2.png" width="550" /> | <img src="https://github.com/plnspineda/pln_public/blob/pln/images/dotplot_Wagyu/Chromosome_2.png" width="550" /> |

| Tuli_Chromosome_3 | Wagyu_Chromosome_3|
|---------------------|---------------------|
| 1 contig | 1 contig |
| Prop_ref (%) = 99.86 | Prop_ref (%) = 99.77 |
| <img src="https://github.com/plnspineda/pln_public/blob/pln/images/dotplot_Tuli/Chromosome_3.png" width="550" /> | <img src="https://github.com/plnspineda/pln_public/blob/pln/images/dotplot_Wagyu/Chromosome_3.png" width="550" /> |

| Tuli_Chromosome_4 | Wagyu_Chromosome_4|
|---------------------|---------------------|
| 2 contigs | 4 contig |
| Prop_ref (%) = 99.94, 0.02 | Prop_ref (%) = 36.04, 54.99, 8.89, 0.01 |
| <img src="https://github.com/plnspineda/pln_public/blob/pln/images/dotplot_Tuli/Chromosome_4.png" width="550" /> | <img src="https://github.com/plnspineda/pln_public/blob/pln/images/dotplot_Wagyu/Chromosome_4.png" width="550" /> |

| Tuli_Chromosome_5 | Wagyu_Chromosome_5|
|---------------------|---------------------|
| 3 contig | 2 contig |
| Prop_ref (%) = 3.46, 86.74, 9.70 | Prop_ref (%) = 0.01, 99.52 |
| <img src="https://github.com/plnspineda/pln_public/blob/pln/images/dotplot_Tuli/Chromosome_5.png" width="550" /> | <img src="https://github.com/plnspineda/pln_public/blob/pln/images/dotplot_Wagyu/Chromosome_5.png" width="550" /> |

| Tuli_Chromosome_6 | Wagyu_Chromosome_6|
|---------------------|---------------------|
| 4 contigs | 3 contigs |
| Prop_ref (%) = 4.88, 0.07, 94.65, 0.50 | Prop_ref (%) = 65.83, 33.56, 0.67 |
| <img src="https://github.com/plnspineda/pln_public/blob/pln/images/dotplot_Tuli/Chromosome_6.png" width="550" /> | <img src="https://github.com/plnspineda/pln_public/blob/pln/images/dotplot_Wagyu/Chromosome_6.png" width="550" /> |

| Tuli_Chromosome_7 | Wagyu_Chromosome_7|
|---------------------|---------------------|
| 1 contig | 8 contigs |
| Prop_ref (%) = 99.89 | Prop_ref (%) = 17.91, 2.86, 13.87, 0.26, 4.19, 0.65, 7.49, 52.56 |
| <img src="https://github.com/plnspineda/pln_public/blob/pln/images/dotplot_Tuli/Chromosome_7.png" width="550" /> | <img src="https://github.com/plnspineda/pln_public/blob/pln/images/dotplot_Wagyu/Chromosome_7.png" width="550" /> |

| Tuli_Chromosome_8 | Wagyu_Chromosome_8|
|---------------------|---------------------|
| 2 contigs | 5 contigs |
| Prop_ref (%) = 41.98, 57.61 | Prop_ref (%) = 0.01, 61.59, 0.23, 20.48, 17.12 |
| <img src="https://github.com/plnspineda/pln_public/blob/pln/images/dotplot_Tuli/Chromosome_8.png" width="550" /> | <img src="https://github.com/plnspineda/pln_public/blob/pln/images/dotplot_Wagyu/Chromosome_8.png" width="550" /> |

| Tuli_Chromosome_9 | Wagyu_Chromosome_9|
|---------------------|---------------------|
| 1 contig | 3 contigs |
| Prop_ref (%) = 97.54 | Prop_ref (%) = 1.21, 55.78, 41.30 |
| <img src="https://github.com/plnspineda/pln_public/blob/pln/images/dotplot_Tuli/Chromosome_9.png" width="550" /> | <img src="https://github.com/plnspineda/pln_public/blob/pln/images/dotplot_Wagyu/Chromosome_9.png" width="550" /> |

| Tuli_Chromosome_10 | Wagyu_Chromosome_10|
|---------------------|---------------------|
| 1 contig | 1 contig |
| Prop_ref (%) = 98.61 | Prop_ref (%) = 98.26 |
| <img src="https://github.com/plnspineda/pln_public/blob/pln/images/dotplot_Tuli/Chromosome_10.png" width="550" /> | <img src="https://github.com/plnspineda/pln_public/blob/pln/images/dotplot_Wagyu/Chromosome_10.png" width="550" /> |

| Tuli_Chromosome_11 | Wagyu_Chromosome_11|
|---------------------|---------------------|
| 3 contigs | 4 contigs |
| Prop_ref (%) = 23.56, 69.30, 6.95 | Prop_ref (%) = 56.99, 31.23, 3.06, 8.43 |
| <img src="https://github.com/plnspineda/pln_public/blob/pln/images/dotplot_Tuli/Chromosome_11.png" width="550" /> | <img src="https://github.com/plnspineda/pln_public/blob/pln/images/dotplot_Wagyu/Chromosome_11.png" width="550" /> |

| Tuli_Chromosome_12 | Wagyu_Chromosome_12|
|---------------------|---------------------|
| 2 contigs | 5 contigs |
| Prop_ref (%) = 101.84, 0.01 | Prop_ref (%) = 0.20, 81.01, 0.05, 0.83, 17.71 |
| <img src="https://github.com/plnspineda/pln_public/blob/pln/images/dotplot_Tuli/Chromosome_12.png" width="550" /> | <img src="https://github.com/plnspineda/pln_public/blob/pln/images/dotplot_Wagyu/Chromosome_12.png" width="550" /> |

| Tuli_Chromosome_13 | Wagyu_Chromosome_13|
|---------------------|---------------------|
| 5 contig | 7 contigs |
| Prop_ref (%) = 12.88, 0.02, 0.04, 0.10, 86.85 | Prop_ref (%) = 12.90, 0.13, 0.06, 31.69, 13.26, 26.58, 15.15 |
| <img src="https://github.com/plnspineda/pln_public/blob/pln/images/dotplot_Tuli/Chromosome_13.png" width="550" /> | <img src="https://github.com/plnspineda/pln_public/blob/pln/images/dotplot_Wagyu/Chromosome_13.png" width="550" /> |

| Tuli_Chromosome_14 | Wagyu_Chromosome_14|
|---------------------|---------------------|
| 1 contig | 1 contig |
| Prop_ref (%) = 99.60 | Prop_ref (%) = 98.15 |
| <img src="https://github.com/plnspineda/pln_public/blob/pln/images/dotplot_Tuli/Chromosome_14.png" width="550" /> | <img src="https://github.com/plnspineda/pln_public/blob/pln/images/dotplot_Wagyu/Chromosome_14.png" width="550" /> |

| Tuli_Chromosome_15 | Wagyu_Chromosome_15|
|---------------------|---------------------|
| 6 contig | 1 contig |
| Prop_ref (%) = 57.52, 0.66, 0.02, 17.46, 22.60, 2.72 | Prop_ref (%) = 98.73 |
| <img src="https://github.com/plnspineda/pln_public/blob/pln/images/dotplot_Tuli/Chromosome_15.png" width="550" /> | <img src="https://github.com/plnspineda/pln_public/blob/pln/images/dotplot_Wagyu/Chromosome_15.png" width="550" /> |

| Tuli_Chromosome_16 | Wagyu_Chromosome_16|
|---------------------|---------------------|
| 7 contigs | 1 contig |
| Prop_ref (%) = 9.19, 0.01, 0.02, 0.01, 0.03, 54.07,36.25 | Prop_ref (%) = 100.62 |
| <img src="https://github.com/plnspineda/pln_public/blob/pln/images/dotplot_Tuli/Chromosome_16.png" width="550" /> | <img src="https://github.com/plnspineda/pln_public/blob/pln/images/dotplot_Wagyu/Chromosome_16.png" width="550" /> |

| Tuli_Chromosome_17 | Wagyu_Chromosome_17|
|---------------------|---------------------|
| 1 contig | 2 contigs |
| Prop_ref (%) = 100.00 | Prop_ref (%) = 28.75, 70.73 |
| <img src="https://github.com/plnspineda/pln_public/blob/pln/images/dotplot_Tuli/Chromosome_17.png" width="550" /> | <img src="https://github.com/plnspineda/pln_public/blob/pln/images/dotplot_Wagyu/Chromosome_17.png" width="550" /> |

| Tuli_Chromosome_18 | Wagyu_Chromosome_18|
|---------------------|---------------------|
| 1 contig | 4 contigs |
| Prop_ref (%) = 100.08 | Prop_ref (%) = 19.84, 57.20, 0.11, 22.86 |
| <img src="https://github.com/plnspineda/pln_public/blob/pln/images/dotplot_Tuli/Chromosome_18.png" width="550" /> | <img src="https://github.com/plnspineda/pln_public/blob/pln/images/dotplot_Wagyu/Chromosome_18.png" width="550" /> |

| Tuli_Chromosome_19 | Wagyu_Chromosome_19|
|---------------------|---------------------|
| 4 contigs | 5 contigs |
| Prop_ref (%) = 0.01, 0.01, 58.26, 41.89 | Prop_ref (%) = 0.01, 39.00, 0.01, 16.36, 44.24 |
| <img src="https://github.com/plnspineda/pln_public/blob/pln/images/dotplot_Tuli/Chromosome_19.png" width="550" /> | <img src="https://github.com/plnspineda/pln_public/blob/pln/images/dotplot_Wagyu/Chromosome_19.png" width="550" /> |

| Tuli_Chromosome_20 | Wagyu_Chromosome_20|
|---------------------|---------------------|
| 3 contigs | 2 contigs |
| Prop_ref (%) = 0.03, 0.04, 98.48 | Prop_ref (%) = 98.41, 1.22 |
| <img src="https://github.com/plnspineda/pln_public/blob/pln/images/dotplot_Tuli/Chromosome_20.png" width="550" /> | <img src="https://github.com/plnspineda/pln_public/blob/pln/images/dotplot_Wagyu/Chromosome_20.png" width="550" /> |

<a name="chr21_22"></a>
| Tuli_Chromosome_21 | Wagyu_Chromosome_21 **| Wagyu_chromosome_21-split |
|---------------------|---------------------|----------------------------|
| 10 contigs | 8 contigs | 8 contigs (1 contig is split) |
| Prop_ref (%) = 0.03, 0.02, 0.02, 0.03, 0.17, 0.12, 3.37, 31.89, 64.90, 0.07 | Prop_ref (%) = 0.02, 0.05, 0.02, 0.22, 0.17, 70.7, 0.09, 52.84 | ?44.95? |
| <img src="https://github.com/plnspineda/pln_public/blob/pln/images/dotplot_Tuli/Chromosome_21.png" width="550" /> | <img src="https://github.com/plnspineda/pln_public/blob/pln/images/dotplot_Wagyu/Chromosome_21.png" width="550" /> | <img src="https://github.com/plnspineda/pln_public/blob/pln/images/dotplot_Wagyu/Chromosome_21-break.png" width="550" /> |

| Tuli_Chromosome_22 | Wagyu_Chromosome_22 **| Wagyu_Chromosome_22-merge |
|---------------------|---------------------|----------------------------|
| 1 contig | 1 contig | 2 contigs (1 contig was broken and merged here)
| Prop_ref (%) = 100.57 | Prop_ref (%) = 72.12 | |
| <img src="https://github.com/plnspineda/pln_public/blob/pln/images/dotplot_Tuli/Chromosome_22.png" width="550" /> | <img src="https://github.com/plnspineda/pln_public/blob/pln/images/dotplot_Wagyu/Chromosome_22.png" width="550" /> | <img src="https://github.com/plnspineda/pln_public/blob/pln/images/dotplot_Wagyu/Chromosome_22-merge.png" width="550" /> |

**Notes on Wagyu Chromosome_21 and Chromosome_22: contig_28 mapped with both chromosomes\
Chromosome_21:1-32406303 (-)\
Chromosome_22:32406304-49406441 (+)\
but still has to check the positions since this is just based on mapping.

| Wagyu_Chromosome_21_10Krl | Wagyu_Chromosome_22_10Krl|
|---------------------|---------------------|
| 5 contigs | 2 contigs |
| Prop_ref (%) = 0.06, 0.37, 0.09, 46.18, 52.90 | Prop_ref (%) = 28.09, 72.09  |
| <img src="https://github.com/plnspineda/pln_public/blob/pln/images/dotplot_Wagyu/Chromosome_21_10Krl.png" width="550" /> | <img src="https://github.com/plnspineda/pln_public/blob/pln/images/dotplot_Wagyu/Chromosome_22_10Krl.png" width="550" /> |

**This is the dot plot for Wagyu Chromosome 21 (total proportion = 99.51) and 22 (total proportion = 100.18) with the 10K read length assembly. Contigs mapped accordingly.

| Tuli_Chromosome_23 | Wagyu_Chromosome_23|
|---------------------|---------------------|
| 5 contigs | 2 contigs |
| Prop_ref (%) = 4.40, 51.04, 0.05, 0.44, 46.76 | Prop_ref (%) = 0.06, 101.75 |
| <img src="https://github.com/plnspineda/pln_public/blob/pln/images/dotplot_Tuli/Chromosome_23.png" width="550" /> | <img src="https://github.com/plnspineda/pln_public/blob/pln/images/dotplot_Wagyu/Chromosome_23.png" width="550" /> |

| Tuli_Chromosome_24 | Wagyu_Chromosome_24|
|---------------------|---------------------|
| 1 contig | 8 contigs |
| Prop_ref (%) = 100.99 | Prop_ref (%) = 22.09, 2.19, 2.86, 1.99, 2.94, 2.04, 66.44, 0.01 |
| <img src="https://github.com/plnspineda/pln_public/blob/pln/images/dotplot_Tuli/Chromosome_24.png" width="550" /> | <img src="https://github.com/plnspineda/pln_public/blob/pln/images/dotplot_Wagyu/Chromosome_24.png" width="550" /> |

| Tuli_Chromosome_25 | Wagyu_Chromosome_25|
|---------------------|---------------------|
| 1 contig | 1 contig |
| Prop_ref (%) = 99.93 | Prop_ref (%) = 100.07 |
| <img src="https://github.com/plnspineda/pln_public/blob/pln/images/dotplot_Tuli/Chromosome_25.png" width="550" /> | <img src="https://github.com/plnspineda/pln_public/blob/pln/images/dotplot_Wagyu/Chromosome_25.png" width="550" /> |

| Tuli_Chromosome_26 | Wagyu_Chromosome_26|
|---------------------|---------------------|
| 1 contig | 1 contig |
| Prop_ref (%) = 99.62 | Prop_ref (%) = 99.51 |
| <img src="https://github.com/plnspineda/pln_public/blob/pln/images/dotplot_Tuli/Chromosome_26.png" width="550" /> | <img src="https://github.com/plnspineda/pln_public/blob/pln/images/dotplot_Wagyu/Chromosome_26.png" width="550" /> |

| Tuli_Chromosome_27 | Wagyu_Chromosome_27|
|---------------------|---------------------|
| 1 contig | 2 contigs |
| Prop_ref (%) = 100.23 | Prop_ref (%) = 40.98, 57.91 |
| <img src="https://github.com/plnspineda/pln_public/blob/pln/images/dotplot_Tuli/Chromosome_27.png" width="550" /> | <img src="https://github.com/plnspineda/pln_public/blob/pln/images/dotplot_Wagyu/Chromosome_27.png" width="550" /> |

| Tuli_Chromosome_28 | Wagyu_Chromosome_28|
|---------------------|---------------------|
| 4 contigs | 1 contig |
| Prop_ref (%) = 89.54, 0.02, 0.07, 10.36 | Prop_ref (%) = 100.88 |
| <img src="https://github.com/plnspineda/pln_public/blob/pln/images/dotplot_Tuli/Chromosome_28.png" width="550" /> | <img src="https://github.com/plnspineda/pln_public/blob/pln/images/dotplot_Wagyu/Chromosome_28.png" width="550" /> |

| Tuli_Chromosome_29 | Wagyu_Chromosome_29|
|---------------------|---------------------|
| 11 contig | 4 contigs |
| Prop_ref (%) = 0.13, 0.06, 0.01, 10.71, 0.01, 0.23, 0.15, 0.11, 0.25, 0.08, 89.16 | Prop_ref (%) = 11.23, 0.66, 87.17, 2.08 |
| <img src="https://github.com/plnspineda/pln_public/blob/pln/images/dotplot_Tuli/Chromosome_29.png" width="550" /> | <img src="https://github.com/plnspineda/pln_public/blob/pln/images/dotplot_Wagyu/Chromosome_29.png" width="550" /> |

| Tuli_Chromosome_Y_vs_UOA_Angus_1 | Wagyu_Chromosome_X_vs_ARS-UCD1.3
|----------------------------------|---------------------------------|
| 4 contigs, 52.68, 0.76, 8.23, 8.14 | 49 contigs |
| <img src="https://github.com/plnspineda/pln_public/blob/pln/images/dotplot_Tuli/Chromosome_Y_vs_Angus.png" width="550" /> | <img src="https://github.com/plnspineda/pln_public/blob/pln/images/dotplot_Wagyu/Chromosome_X_vs_ARS-UCD1.3.png" width="550" /> |

## Improvement on Chromosome_X and Y <a name="chromosomeXY"></a>

#### Chromosome X

file_location: /hpcfs/users/a1812753/TulixWagyu_backup/reorder_contigs/TW_vs_ARS-UCD/dot_plot/Wagyu_final/Chromosome_X_v2

| Wagyu_Chromosome_X_vs_ARS-UCD1.3 | Wagyu_Chromosome_X_vs_UOA_Brahman_1
|----------------------------------|---------------------------------|
| 50 contigs (104.08%) | 50 contigs (99.03%) |
| <img src="https://github.com/plnspineda/pln_public/blob/pln/images/dotplot_Wagyu/Chromosome_X_v2.png" width="550" /> | <img src="https://github.com/plnspineda/pln_public/blob/pln/images/dotplot_Wagyu/Chromosome_X_v2_Brahman.png" width="550" /> |

**I just stitched contig56 which was not included in the previous image. It got filtered out although it maps 6.56% to the Chromosome_X\
**total proportion = 104.08% | 99.03%
**contig 194 and 834 (2.25% and 0.09%) was the inverted in Wagyu_Chromosome_X_vs_UOA_Brahman_1

file location: /hpcfs/users/a1812753/TulixWagyu_backup/reorder_contigs/sex_chromosomes/chromosome_X

Charolais X is probably only 1 contig which is haplotype1-0000042 (determined using winnowmap)

| ARSUCD1.3_Chromosome_X_vs_T2T_Charolais | Wagyu_Chromosome_X_vs_T2T_Charolais
|----------------------------------|---------------------------------|
| 50 contigs (104.08%) | 50 contigs (99.03%) |
| <img src="https://github.com/plnspineda/pln_public/blob/pln/images/dotplot_Wagyu/contig_haplotype1-0000042_Chromosome_X0.png" width="550" /> | <img src="https://github.com/plnspineda/pln_public/blob/pln/images/dotplot_Wagyu/contig_haplotype1-0000042_Chromosome_X_v2.fasta0.png" width="550" /> |

Brahman_Chromosome_X_vs_T2T_Charolais

<img src="https://github.com/plnspineda/pln_public/blob/pln/images/dotplot_Wagyu/contig_haplotype1-0000042_UOA_Brahman_Chromosome_X0.png" width="550" />

Zoom-in

<img src="https://github.com/plnspineda/pln_public/blob/pln/images/sex_chromosomes/dotplot_zoom-in_T2T_Charolais_vs_Brahman_X.jpeg" width="550" />


#### Chromosome Y

file location: /hpcfs/users/a1812753/TulixWagyu_backup/reorder_contigs/sex_chromosomes/chromosome_Y

T2T_Wagyu Y is found at haplotype2-0001634\
Nelore Y is found at X_N_shasta which is quite confusing since shoudn't it be at Y_N_shasta? *Answer*: Must be the PAR. Will still use Y_N_shasta which is the Nellore Y.

| Tuli assembly Y vs T2T_Wagyu Y | Tuli assembly Y vs Nelore_X
|----------------------------------|---------------------------------|
| <img src="https://github.com/plnspineda/pln_public/blob/pln/images/sex_chromosomes/chrY_Wagyu_ref_v2_Tuli_Chromosome_Y.fasta0.png" width="550" /> | <img src="https://github.com/plnspineda/pln_public/blob/pln/images/sex_chromosomes/X_N_shasta.fna_Tuli_Chromosome_Y.fasta0.png" width="550" /> |


Tully assembly Y vs Nelore_Y

<img src="https://github.com/plnspineda/pln_public/blob/pln/images/sex_chromosomes/Y_N_shasta.fna_chrY_Tuli_asm.fasta0.png" width="550" />


| Angus reference Y vs T2T_Wagyu Y | Angus reference Y vs Nelore_X
|----------------------------------|---------------------------------|
| <img src="https://github.com/plnspineda/pln_public/blob/pln/images/sex_chromosomes/chrY_Wagyu_ref_v2_Angus_Chromosome_Y.png" width="550" /> | <img src="https://github.com/plnspineda/pln_public/blob/pln/images/sex_chromosomes/X_N_shasta_Angus_Chromosome_Y0.png" width="550" /> |

------------------------------------------------------------------------------------
#### Finding Y-contigs

Y-chromosome is supposedly ~50Mb and we only usually get ~13Mb for the Y_chromosome. In T2T_Wagyu_Y, it could be two contigs which are **haplotype2-0001634 and haplotype2-0001654** since these two mapped well with the Y Angus as from the screenshot below.

total length for the two contigs = 59500937bp \
<img src="https://github.com/plnspineda/pln_public/blob/pln/images/sex_chromosomes/winnowmap_Y_angus_vs_T2T_wagyu.png" width="550" />

also, looking at the sizes of all the contigs from T2T_Wagyu_Y, haplotype2-0001654 is at 29th largest contig while haplotype2-0001634 is the least largest contig before the next contig dropped to half its length suggesting it might be a real contig for a chromosome. In this case, it's Y. \
<img src="https://github.com/plnspineda/pln_public/blob/pln/images/sex_chromosomes/contig_length_T2T_Wagyu.png" width="550" />

**Y-SNP markers alignment**

sam files can be found here:
- [1373 SNP probe markers](https://github.com/plnspineda/pln_public/blob/pln/alignment_files/y_SNP_markers/aln-se_Tuli_shastav10_1K_y_snp_probes.sam)
- [additional 4 SNP probe marker (longer sequence)](https://github.com/plnspineda/pln_public/blob/pln/alignment_files/y_SNP_markers/aln-se_Tuli_shastav10_1K_additional_Y_SNP_markers.fa.sam)
- [summary of the SNPs filtered at MAPQ>25 (table below)](https://github.com/plnspineda/pln_public/blob/pln/alignment_files/y_SNP_markers/aln-se_Tuli_shastav10_1K_y_snp_probes_filteredQ25.tsv)

**Summary of the contigs that has the SNP markers, filtered at MAPQ>25**\
total length: 13795544 (excluding contig 40 because it's 50% of chromosome 23)

| ref_name | MAPQ_ave | marker_count | contig_length | 50Mb_ref_proportion (%) | remarks          |orientation|
|----------|:--------:|:------------:|--------------:|------------------------:|------------------|---|
| 120      |   36.82  |      65      |       1288355 |                    2.58 | contig_for_Y     | + |
| 276      |    37    |       2      |        339059 |                    0.68 | unplaced         | - |
| 538      |    37    |       1      |        118244 |                    0.24 | contig_for_Y     | + |
| 92       |    37    |      231     |       8248324 |                   16.50 | contig_for_Y     | - |
| 470      |    37    |       1      |         72243 |                    0.14 | unplaced         | - |
| 104      |    37    |       3      |        383264 |                    0.77 | unplaced         | + |
| 314      |    37    |       3      |        326864 |                    0.65 | unplaced         | - |
| 144      |    37    |       8      |        158553 |                    0.32 | unplaced         | + |
| 184      |    37    |      38      |       1071852 |                    2.14 | unplaced         | + |
| 1716     |    37    |       2      |         59971 |                    0.12 | unplaced         | + |
| 1026     |    37    |       3      |         22617 |                    0.05 | unplaced         | - |
| 804      |    37    |       2      |         23428 |                    0.05 | unplaced         | - |
| 1726     |    37    |       1      |         35887 |                    0.07 | unplaced         | - |
| 506      |    37    |       1      |        253442 |                    0.51 | unplaced         | - |
| 1778     |    37    |       1      |         19046 |                    0.04 | unplaced         | - |
| 1390     |    37    |       2      |         95101 |                    0.19 | unplaced         | - |
| 82       |    37    |      50      |       1274574 |                    2.55 | contig_for_Y     | - |
| 672      |    37    |       2      |          4720 |                    0.01 | unplaced         |   |
| 40       |    37    |      20      |      26792771 |                   53.59 | contig_for_chr23 |   |

possible order of contigs: [paf_file_here](https://github.com/plnspineda/pln_public/blob/pln/alignment_files/y_SNP_markers/df_Wagyu_New_Angus.tsv)

dot_plot with T2T_Wagyu_Y

<img src="https://github.com/plnspineda/pln_public/blob/pln/images/sex_chromosomes/contigs_mapped_to_YSNP_37Q_winnowmap0.png" width="550" />

hehe. seems like there's a large chunk of repeat region?

**Finding PAR in T2T_Wagyu_Y and Tuli_Y from Angus_Y annotation**

Hypothesis: That good line at the start of the dotplot is possibly the PAR.

file location of gtf files: /hpcfs/users/a1812753/TulixWagyu_backup/reorder_contigs/sex_chromosomes/chromosome_Y/ref_genome/Angus_annotation

1. Found PAR by lifting annotations from the ARS-UCD1.2 X chromosome using [liftoff](https://github.com/agshumate/Liftoff), looked for GPR143 to locate [boundary](https://bmcgenomics.biomedcentral.com/articles/10.1186/s12864-019-6364-z/figures/1), however, I can't find PLCXD1 in the annotations so I downloaded from NCBI instead. I aligned the [PLCXD1](https://asia.ensembl.org/Bos_taurus/Transcript/Exons?db=core;g=ENSBTAG00000035144;r=1:88340909-88350179;t=ENSBTAT00000066297) to Tuli Y Chromosome and found the gene to find the following PAR positions.

2. Possible PAR lengths of each assemblies:

| **Assembly**    | **Contig_Length** | **PAR_length** | **PAR_position**    |
|-----------------|-------------------|----------------|---------------------|
| Tuli_Y          | 13792424          | 6775140        | 1776269-8551408     |
| Wagyu_X         | 144677779         | 6760422        | 137886957-144647378 |
| Angus_Y         | 15658480          | 6728939        | 39897-6768835       |
| Brahman_X       | 146092946         | 6780506        | 30693-6811198       |
| ARS-UCD1.2_X    | 139009144         | 5899046        | 133110099-139009144 |
| Nelore_X        | 11171212          | 6753620        | 4387323-11140942    |
| Nelore_Y        | 10500703          |                |                     |
| T2T_Wagyu_Y     | 59501037          | 6738563        | 47845-6786407       |
| T2T_Charolais_X | 169155847         | 6729907        | 162375123-169105029 |

3. Dotplot with Tuli Y Chromosome PAR region which align well with Chromosome X as well.

| Tuli_Y_PAR vs Angus_Y_PAR | Tuli_Y_PAR vs ARS-UCD1.2_X_PAR
|-----------|------------|
| <img src="https://github.com/plnspineda/pln_public/blob/pln/images/sex_chromosomes/PAR_Angus_Y_CM011803-1_PAR_Tuli_Y_18contigs0.png" width="550" /> | <img src="https://github.com/plnspineda/pln_public/blob/pln/images/sex_chromosomes/PAR_ARS-UCD1-2_X_CM008197-2_PAR_Tuli_Y_18contigs0.png" width="550" /> |

| Tuli_Y_PAR vs Wagyu_X_PAR | Tuli_Y_PAR vs T2T_Wagyu_Y_PAR
|-----------|------------|
| <img src="https://github.com/plnspineda/pln_public/blob/pln/images/sex_chromosomes/PAR_Wagyu_X_50contigs_PAR_Tuli_Y_18contigs0.png" width="550" /> | <img src="https://github.com/plnspineda/pln_public/blob/pln/images/sex_chromosomes/PAR_T2T_Wagyu_Y_haplo-1634-1654_PAR_Tuli_Y_18contigs0.png" width="550" /> |


4. Which contig in Tuli Y is the PAR?
  - contig_92 [paf_file](https://github.com/plnspineda/pln_public/blob/pln/alignment_files/PAR_Tuli_Y_18contigs.fa_Tuli_Y_18contigs_separate.paf)

5. Wagyu Y vs Human Y chromosome

**Aligning the Tuli assembly to T2T Wagyu Y contig**

Since it seems like the T2T Wagyu Y has the complete Y, I aligned the Tuli assembly to Wagyu Y and see which contigs in the Tuli assembly I could use to assemble the Y chromosome.
