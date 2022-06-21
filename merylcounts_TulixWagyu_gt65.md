reads-Tuli_sire.statistics and reads-Wagyu_dam.statistics are the same as the original meryl files.

==> reads-Tuli_sire.statistics <==
Number of 21-mers that are:
  unique             3374650988  (exactly one instance of the kmer is in the input)
  distinct           5660194178  (non-redundant kmer sequences in the input)
  present           70335511124  (...)
  missing         4392386316926  (non-redundant kmer sequences not in the input)

             number of   cumulative   cumulative     presence
              distinct     fraction     fraction   in dataset
frequency        kmers     distinct        total       (1e-6)
--------- ------------ ------------ ------------ ------------

==> reads-Wagyu_dam.statistics <==
Number of 21-mers that are:
  unique             3126815003  (exactly one instance of the kmer is in the input)
  distinct           5418962796  (non-redundant kmer sequences in the input)
  present           65598961334  (...)
  missing         4392627548308  (non-redundant kmer sequences not in the input)


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


haplotype-Tuli_sire.meryl and haplotype-Wagyu_dam.meryl are the same as the father_not_mother.meryl and mother_not_father.meryl

(base) [a1812753@l01 0-kmers]$ singularity exec /apps/containers/merqury_v1.3.sif meryl statistics haplotype-Tuli_sire.meryl | head

Found 1 command tree.
Number of 21-mers that are:
  unique             3195621406  (exactly one instance of the kmer is in the input)
  distinct           3434873944  (non-redundant kmer sequences in the input)
  present            5190364902  (...)
  missing         4394611637160  (non-redundant kmer sequences not in the input)

             number of   cumulative   cumulative     presence
              distinct     fraction     fraction   in dataset
frequency        kmers     distinct        total       (1e-6)
--------- ------------ ------------ ------------ ------------
(base) [a1812753@l01 0-kmers]$ singularity exec /apps/containers/merqury_v1.3.sif meryl statistics haplotype-Wagyu_dam.meryl/ | head

Found 1 command tree.
Number of 21-mers that are:
  unique             2946027558  (exactly one instance of the kmer is in the input)
  distinct           3193642562  (non-redundant kmer sequences in the input)
  present            4400908036  (...)
  missing         4394852868542  (non-redundant kmer sequences not in the input)

             number of   cumulative   cumulative     presence
              distinct     fraction     fraction   in dataset
frequency        kmers     distinct        total       (1e-6)
--------- ------------ ------------ ------------ ------------

father_not_mother.meryl

    Found 1 command tree.
    Number of 21-mers that are:
      unique             3195621406  (exactly one instance of the kmer is in the input)
      distinct           3434873944  (non-redundant kmer sequences in the input)
      present            5190364902  (...)
      missing         4394611637160  (non-redundant kmer sequences not in the input)

mother_not_father.meryl

    Found 1 command tree.
    Number of 21-mers that are:
      unique             2946027558  (exactly one instance of the kmer is in the input)
      distinct           3193642562  (non-redundant kmer sequences in the input)
      present            4400908036  (...)
      missing         4394852868542  (non-redundant kmer sequences not in the input)


canu filter kmers that are at least 5

(base) [a1812753@l01 haplotype]$ cat haplotype.log
--  Haplotype './0-kmers/haplotype-Tuli_sire.meryl':
--   use kmers with frequency at least 5.
--  Haplotype './0-kmers/haplotype-Wagyu_dam.meryl':
--   use kmers with frequency at least 5.
-- Begin    processing file /hpcfs/groups/phoenix-hpc-avsci/Lloyd_Low/Tuli_x_Wagyu_data/F1_longreads/all_ONT_tulixwagyu.fastq.gz
-- Finished processing file /hpcfs/groups/phoenix-hpc-avsci/Lloyd_Low/Tuli_x_Wagyu_data/F1_longreads/all_ONT_tulixwagyu.fastq.gz with 14157283 records
--
--  6658510 reads 141920511404 bases written to haplotype file ./haplotype-Tuli_sire.fasta.gz.
--  6540514 reads 145718799501 bases written to haplotype file ./haplotype-Wagyu_dam.fasta.gz.
--   458476 reads   1201292989 bases written to haplotype file ./haplotype-unknown.fasta.gz.
--
--   499783 reads    300424677 bases filtered for being too short.

however, I can't find the script if "5" is a fixed-number of if it is computed. From the issues in canu github, it seems like the filter number is computed.
