# Tuli x Wagyu

[Checking the mother hapmer](#hapmer)

## Why is the Wagyu hapmer kind of strange? Checking the mother hapmer... <a name="hapmer"></a>

Short reads coverage:

- F1: 90.89874
- mother: 42.36248
- father: 44.53369

meryl output size:

- F1.meryl (24G)
- mother.meryl (28G)
- father.meryl (29G)

a bit strange...? mother inherited hapmer is only 1.2M size?

        (base) [a1812753@l01 hapmer-dbs]$ du -sh *inherited.gt*
        382M	father.inherited.gt7.meryl
        1.2M	mother.inherited.gt7.meryl
        11G	shrd.inherited.gt10.meryl

This is for the previous Angus x Brahamn hapmer dbs

        (base) [a1812753@l01 build_hapmers]$ du -sh *inherited.gt*
        720M	Dam_truncated.inherited.gt2.meryl
        10G	shrd.inherited.gt5.meryl
        432M	Sire_truncated.inherited.gt2.meryl

meryl filtered kmers with frequency less than 65 thus the few mother hapmers. Below is the number of remaining kmers for each parents after filtering.

        (base) [a1812753@l01 hapmer-dbs]$ singularity exec /apps/containers/merqury_v1.3.sif meryl statistics mother_not_father.gt65.meryl | head

        Found 1 command tree.
        Number of 21-mers that are:
          unique                      0  (exactly one instance of the kmer is in the input)
          distinct                60870  (non-redundant kmer sequences in the input)
          present               9737439  (...)
          missing         4398046450234  (non-redundant kmer sequences not in the input)

          (base) [a1812753@l01 hapmer-dbs]$ singularity exec /apps/containers/merqury_v1.3.sif meryl statistics father_not_mother.gt5.meryl/ | head

        Found 1 command tree.
        Number of 21-mers that are:
          unique                      0  (exactly one instance of the kmer is in the input)
          distinct            100258031  (non-redundant kmer sequences in the input)
          present            1675959122  (...)
          missing         4397946253073  (non-redundant kmer sequences not in the input)


this is the number of k-mers for parental only meryl (hapmers not filtered yet and with no F1 yet).

father_not_mother kmers | mother_not_father kmers | zoom-in mother_not_father kmers (60-70)
----------|-----------|--------------------
<img src="https://github.com/plnspineda/pln_public/blob/pln/images/Rplot_father_not_mother.histo.png" width="450" /> | <img src="https://github.com/plnspineda/pln_public/blob/pln/images/Rplot_mother_not_father.histo.png" width="450" /> | <img src="https://github.com/plnspineda/pln_public/blob/pln/images/Rplot_mother_not_father_zoomin.histo.png" width="400" /> red arrow indicates the detected "peak"

Below is the data wherein the .hist file from the above table and plot was derived.

`father_not_mother.meryl`

        Found 1 command tree.
        Number of 21-mers that are:
          unique             3195621406  (exactly one instance of the kmer is in the input)
          distinct           3434873944  (non-redundant kmer sequences in the input)
          present            5190364902  (...)
          missing         4394611637160  (non-redundant kmer sequences not in the input)

`mother_not_father.meryl`

        Found 1 command tree.
        Number of 21-mers that are:
          unique             2946027558  (exactly one instance of the kmer is in the input)
          distinct           3193642562  (non-redundant kmer sequences in the input)
          present            4400908036  (...)
          missing         4394852868542  (non-redundant kmer sequences not in the input)

<<Rplot>>

I also did not notice anything strange from the original meryl files of the mother and the father:

`mother.meryl`

        Found 1 command tree.
        Number of 21-mers that are:
          unique             3126815003  (exactly one instance of the kmer is in the input)
          distinct           5418962796  (non-redundant kmer sequences in the input)
          present           65598961334  (...)
          missing         4392627548308  (non-redundant kmer sequences not in the input)

`father.meryl`

        Found 1 command tree.
        Number of 21-mers that are:
          unique             3374650988  (exactly one instance of the kmer is in the input)
          distinct           5660194178  (non-redundant kmer sequences in the input)
          present           70335511124  (...)
          missing         4392386316926  (non-redundant kmer sequences not in the input)

**QV Merqury**

Hapmers for the Tuli x Wagyu assembly did not separate nicely.

Tuli X Wagyu hapmer blobs | Angus X Brahman hapmer blobs
----------|-----------
<img src="https://github.com/plnspineda/pln_public/blob/pln/images/3.QV.hapmers.blob.png" width="450" /> | <img src="https://github.com/plnspineda/pln_public/blob/pln/images/3.shasta.hapmers.blob.png" width="450" />

## setting the first filter manually

QV Merqury result location: /hpcfs/groups/phoenix-hpc-avsci/Lloyd_Low/Tuli_x_Wagyu_data/QV_estimation/merqury-gt5

This is the result when filtering for the wagyu meryl short read is set to less than 5.

          (base) [a1812753@l01 mother-gt5-hapmer]$ du -sh *inherited.gt*
          382M	father.inherited.gt7.meryl
          283M	mother.inherited.gt6.meryl
          11G	shrd.inherited.gt10.meryl

(for context, filtering for kmers are done twice. First is after getting the hapmers, and then second after getting the inherited hapmers)

first filter
- father < 5
- mother < 5 *manually set

second filter
- father < 7
- mother < 6
- shared < 10

Tuli X Wagyu hapmer blob (filter < 5)

<img src="https://github.com/plnspineda/pln_public/blob/pln/images/gt5-QV.hapmers.blob.png" width="450" />


## ONT reads

| readl         | sumfreq | sumlen       | percentage_reads | percentage_len |
|---------------|---------|--------------|------------------|----------------|
| (0,1e+03]     | 500496  | 301137677    | 3.535255         | 0.1041491      |
| (1e+03,1e+04] | 6181338 | 29582076342  | 43.661895        | 10.23102       |
| (1e+04,5e+04] | 5845512 | 139231240796 | 41.289787        | 48.1534016     |
| (5e+04,1e+05] | 1419527 | 96587542964  | 10.026832        | 33.4049939     |
| (1e+05,Inf]   | 210410  | 23439030792  | 1.486232         | 8.1064354      |

Human dataset
  390 Gbp of data (126x coverage)
  N50 is 58 kbp
  219 Gbp bases in reads >50 kbp (71x)
  longest full-length mapping read is 1.3 Mbp

Tuli x Wagyu dataset
  289 Gb of data (107x coverage)
  N50 is 41.9 Kbp
  120.03 Gbp in reads >50 Kbp (44.45x)
  23.44 Gbp in reads >100 Kbp (8.68x)
  1.48% of the reads are >100Kbp, 8.11% of the total length
