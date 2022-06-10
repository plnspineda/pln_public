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


father_not_mother kmers | mother_not_father kmers | zoom-in mother_not_father kmers (60-70)
----------|-----------|--------------------
<img src="https://github.com/plnspineda/pln_public/blob/pln/images/Rplot_father_not_mother.histo.png" width="450" /> | <img src="https://github.com/plnspineda/pln_public/blob/pln/images/Rplot_mother_not_father.histo.png" width="450" /> | <img src="https://github.com/plnspineda/pln_public/blob/pln/images/Rplot_mother_not_father_zoomin.histo.png" width="450" /> red arrow indicates that detected "peak"

this is the number of k-mers for parental only meryl (hapmers with no F1 yet). This is the data wherein the .hist file from the above table and plot was derived. seems normal.

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
