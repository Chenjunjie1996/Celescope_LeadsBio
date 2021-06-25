## Features
- Replace rate in each cluster
- Top replace genes in each cluster

## Output
- `{sample}.rep_in_tsne.txt` Replace rate in each cluster.
- `{sample}.rep_in_tsne_top10` Top 10 replace genes in each cluster.


## Arguments
`--tsne` tsne file

`--mat` matrix rep file

`--rep` cell rep file

`--mincell` turn-over in at least cells, default 5

`--topgene` top N genes,default 10

`--outdir` Output diretory.

`--assay` Assay name.

`--sample` Sample name.

`--thread` Thread to use.

`--debug` If this argument is used, celescope may output addtional file for debugging.
