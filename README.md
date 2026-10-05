
Bioinformatics Analysis and Visualization

Bioinformatics scripts for genomic and comparative analyses of *Photobacterium damselae* subsp. *piscicida*.

Repository Contents

The `scripts` directory contains scripts used for bioinformatics analyses and visualization in the associated study.

Available scripts

- `Defense_analysis.py` — script for defense-related genomic analysis.
- `Genomic_Distance_Heatmap` — script for genomic distance analysis and heatmap visualization.
- `Pangenome_Pie` — script for pangenome analysis and visualization.
- `prophage_analysis.py` — script for prophage sequence analysis and pairwise sequence similarity calculation.

Prophage Analysis

The `prophage_analysis.py` script:

1. Reads prophage sequences from FASTA files.
2. Extracts strain information, prophage identifiers, sequence lengths, and sequences.
3. Generates a summary table of prophage sequences.
4. Calculates pairwise sequence similarity using global pairwise alignment.
5. Generates a prophage similarity matrix.
6. Produces a heatmap representing pairwise prophage sequence similarity.

Output files

The prophage analysis generates:

- `Prophage_Summary.xlsx`
- `Prophage_Similarity_Matrix.xlsx`
- `Prophage_Heatmap.png`

Requirements

The Python scripts require Python 3 and the relevant Python packages used by each analysis.

For prophage analysis, the following packages are required:

- pandas
- Biopython
- matplotlib
- openpyxl

They can be installed using:

```bash
pip install pandas biopython matplotlib openpyxl
