# Purge dups result

## Tuli and Wagyu

Tuli assembly stats:

| Assembly                       | size (Gb) | contig | N50 (Mb) | max_contig (Mb) | QV      |
|--------------------------------|-----------|--------|----------|-----------------|---------|
| Tuli_shastav10                 | 2.5726    | 1503   | 73.1705  | 136.24          | 41.0187 |
| Tuli_shastav10_complete_purged | 2.5279    | 565    | 73.1705  | 136.24          | 41.8958 |
| Tuli_shastav10_haplo_purged**  | 0.0448    | 947    |          | 1.07            |         |
| Tuli_shastav10_filtered_purged | 2.5383    | 850    | 73.1705  | 136.24          | 41.5655 |


Tuli purge dups haplo stats:

| category | num_contig | total_len  | max_contig | min_contig |
|----------|------------|------------|------------|------------|
| REPEAT   | 589        | 34,095,357 | 1,071,852  | 683        |
| OVLP     | 9          | 1,308,773  | 495,531    | 35,823     |
| JUNK     | 82         | 236,416    | 28,833     | 80         |
| HAPLOTIG | 137        | 3,703,211  | 326,864    | 550        |
| HIGHCOV  | 148        | 5,434,338  | 311,823    | 688        |

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
