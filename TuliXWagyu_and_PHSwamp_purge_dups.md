# Purge dups result

## Tuli and Wagyu

**Tuli assembly stats:**

| Assembly                       | size (Gb) | contig | N50 (Mb) | max_contig (Mb) | QV      |
|--------------------------------|-----------|--------|----------|-----------------|---------|
| Tuli_shastav10                 | 2.5726    | 1503   | 73.1705  | 136.24          | 41.0187 |
| Tuli_shastav10_complete_purged | 2.5279    | 565    | 73.1705  | 136.24          | 41.8958 |
| Tuli_shastav10_haplo_purged**  | 0.0448    | 947    |          | 1.07            |         |
| Tuli_shastav10_filtered_purged | 2.5383    | 850    | 73.1705  | 136.24          | 41.5655 |


Tuli purge dups haplo stats:

| category | num_contig | total_len  | max_contig | min_contig |
|----------|------------|------------|------------|------------|
| REPEAT   | 589*       | 34,095,357 | 1,071,852  | 683        |
| OVLP     | 9          | 1,308,773  | 495,531    | 35,823     |
| JUNK     | 82*        | 236,416    | 28,833     | 80         |
| HAPLOTIG | 137        | 3,703,211  | 326,864    | 550        |
| HIGHCOV  | 148        | 5,434,338  | 311,823    | 688        |

*removed

Repeat files result:

        (base) [a1812753@l01 RM_out_REPEAT]$ cat hap_REPEAT.fa.tbl
        ==================================================
        file name: hap_REPEAT.fa            
        sequences:           589
        total length:   34095357 bp  (34095357 bp excl N/X-runs)
        GC level:         51.08 %
        bases masked:    1830047 bp ( 5.37 %)
        ==================================================


| REPEATS | OTHERS IN HAPLOBIN |
|-----|-----|
| <img src="https://github.com/plnspineda/pln_public/blob/pln/images/purge_dups/T_%20Rplot_repeat.png" width="450" /> | <img src="https://github.com/plnspineda/pln_public/blob/pln/images/purge_dups/T_Rplot_haps.png" width="450" /> |

Final assembly for Tuli assembly after purge dups (removing the repeats and junks)

        Assembly                    Tuli_shastav10_1K_purged
        # contigs (>= 0 bp)         897                     
        # contigs (>= 1000 bp)      825                     
        # contigs (>= 5000 bp)      712                     
        # contigs (>= 10000 bp)     655                     
        # contigs (>= 25000 bp)     479                     
        # contigs (>= 50000 bp)     312                     
        Total length (>= 0 bp)      2538316358              
        Total length (>= 1000 bp)   2538289958              
        Total length (>= 5000 bp)   2537975256              
        Total length (>= 10000 bp)  2537551036              
        Total length (>= 25000 bp)  2534537116              
        Total length (>= 50000 bp)  2528605380              
        # contigs                   850                     
        Largest contig              136239588               
        Total length                2538307708              
        GC (%)                      42.02                   
        N50                         73170537                
        N75                         47569152                
        L50                         13                      
        L75                         23                      
        # N's per 100 kbp           0.00

**Wagyu assembly stats:**

| Assembly                        | size (Gb) | contig | N50 (Mb) | max_contig (Mb) |      QV |
|---------------------------------|----------:|-------:|---------:|----------------:|--------:|
| Wagyu_shastav10                 | 2.6919    | 1442   | 58.1767  | 136.05          | 40.9735 |
| Wagyu_shastav10_complete_purged | 2.6515    | 446    | 58.1767  | 136.05          | 41.4811 |
| Wagyu_shastav10_haplo_purged**  | 0.0404    | 1008   |          | 0.5342          |         |
| Wagyu_shastav10_filtered_purged | 2.6633    | 760    | 58.1767  | 136.05          | 41.2585 |

Wagyu purge dups haplo stats:

| category | num_contig | total_len  | max_contig | min_contig |
|----------|------------|------------|------------|------------|
| REPEAT   | 599*       | 28,266,706 | 534,220    | 136        |
| OVLP     | 12         | 1,221,624  | 402,878    | 18,106     |
| JUNK     | 99*        | 295,947    | 26,150     | 80         |
| HAPLOTIG | 131        | 4,578,846  | 483,264    | 89         |
| HIGHCOV  | 189        | 5,998,107  | 276,696    | 83         |

*removed

Repeat files result:

==================================================
file name: hap_REPEAT.fa            
sequences:           599
total length:   28266706 bp  (28266706 bp excl N/X-runs)
GC level:         50.97 %
bases masked:    1012084 bp ( 3.58 %)
==================================================

| REPEATS | OTHERS IN HAPLOBIN |
|-----|-----|
| <img src="https://github.com/plnspineda/pln_public/blob/pln/images/purge_dups/W_Rplot_repeat.png" width="450" /> | <img src="https://github.com/plnspineda/pln_public/blob/pln/images/purge_dups/W_Rplot_haps.png" width="450" /> |

Final assembly for Tuli assembly after purge dups (removing the repeats and junks)

        Assembly                    Wagyu_shastav10_1K_purged
        # contigs (>= 0 bp)         820                      
        # contigs (>= 1000 bp)      742                      
        # contigs (>= 5000 bp)      668                      
        # contigs (>= 10000 bp)     614                      
        # contigs (>= 25000 bp)     465                      
        # contigs (>= 50000 bp)     321                      
        Total length (>= 0 bp)      2663327612               
        Total length (>= 1000 bp)   2663304805               
        Total length (>= 5000 bp)   2663122103               
        Total length (>= 10000 bp)  2662718720               
        Total length (>= 25000 bp)  2660201815               
        Total length (>= 50000 bp)  2655043875               
        # contigs                   760                      
        Largest contig              136048618                
        Total length                2663317029               
        GC (%)                      41.92                    
        N50                         58176654                 
        N75                         36917800                 
        L50                         16                       
        L75                         31                       
        # N's per 100 kbp           0.00

## Philippine Swamp Buffalo

**Swamp assembly stats**

| Assembly               |          size | contig |        N50 |  max_contig | QV      |
|------------------------|--------------:|-------:|-----------:|------------:|---------|
| ctg_dc                 | 2,950,156,688 | 500    | 85,467,828 | 168,927,125 | 44.571  |
| ctg_dc_purged          | 2,729,592,170 | 125    | 99,836,121 | 168,927,125 |         |
| ctg_dc_haplo_purged**  | 220,564,518   | 380    | 2,660,129  | 10,860,900  |         |
| ctg_dc_filtered_purged | 2,949,616,321 | 478    | 85,467,828 | 168,927,125 | 45.6715 |

purge_dups haplo stats:

| category | num_contigs |   total_len | max_contig | min_contig |
|----------|------------:|------------:|-----------:|-----------:|
| REPEAT   |         344 | 213,402,902 | 10,860,900 |     18,786 |
| OVLP     | 5           | 299,565     | 133,918    | 21,497     |
| JUNK     | 22*          | 540,367     | 66,610     | 10,963     |
| HAPLOTIG | 8           | 6,128,221   | 5,560,144  | 39,007     |
| HIGHCOV  | 1           | 193,463     | 193,463    | 193,463    |

*removed

Repeat contig result:

        ==================================================
        file name: hap_rm_REPEAT.fa         
        sequences:           344
        total length:  213402902 bp  (213402902 bp excl N/X-runs)
        GC level:         55.93 %
        bases masked:   15165061 bp ( 7.11 %)
        ==================================================

        | REPEATS | OTHERS IN HAPLOBIN |
        |-----|-----|
        | <img src="https://github.com/plnspineda/pln_public/blob/pln/images/purge_dups/SP_Rplot_repeats.png" width="450" /> | <img src="https://github.com/plnspineda/pln_public/blob/pln/images/purge_dups/SP_Rplot_haps.png" width="450" /> |

Final assembly for swamp buffalo after purge dups (junks removed)

        Assembly                    sp_buf_dc.asm.bp.p_ctg_junkpurged
        # contigs (>= 0 bp)         478                              
        # contigs (>= 1000 bp)      478                              
        # contigs (>= 5000 bp)      478                              
        # contigs (>= 10000 bp)     472                              
        # contigs (>= 25000 bp)     439                              
        # contigs (>= 50000 bp)     366                              
        Total length (>= 0 bp)      2949616321                       
        Total length (>= 1000 bp)   2949616321                       
        Total length (>= 5000 bp)   2949616321                       
        Total length (>= 10000 bp)  2949567630                       
        Total length (>= 25000 bp)  2949007524                       
        Total length (>= 50000 bp)  2946248138                       
        # contigs                   478                              
        Largest contig              168927125                        
        Total length                2949616321                       
        GC (%)                      43.11                            
        N50                         85467828                         
        N75                         55573485                         
        L50                         13                               
        L75                         23                               
        # N's per 100 kbp           0.00
