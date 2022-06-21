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
