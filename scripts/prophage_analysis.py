import os
import glob
import pandas as pd
from Bio import SeqIO
from Bio.Align import PairwiseAligner
import matplotlib.pyplot as plt


input_folder = os.path.join("data", "input")
output_folder = os.path.join("data", "output")

os.makedirs(output_folder, exist_ok=True)



summary = []

for fasta in glob.glob(os.path.join(input_folder, "*.fasta")):

    strain = os.path.basename(fasta).replace(".fasta", "")

    for i, record in enumerate(SeqIO.parse(fasta, "fasta"), start=1):

        summary.append({
            "Strain": strain,
            "Prophage": f"{strain}_P{i}",
            "Length(bp)": len(record.seq),
            "Sequence": str(record.seq)
        })

summary_df = pd.DataFrame(summary)

summary_df.to_excel(
    os.path.join(output_folder, "Prophage_Summary.xlsx"),
    index=False
)

print(summary_df)

print("\nTotal number of prophages:", len(summary_df))



aligner = PairwiseAligner()
aligner.mode = "global"

names = summary_df["Prophage"].tolist()
seqs = summary_df["Sequence"].tolist()

matrix = pd.DataFrame(index=names, columns=names)

for i in range(len(seqs)):
    for j in range(len(seqs)):

        if i == j:

            matrix.iloc[i, j] = 100

        else:

            score = aligner.score(seqs[i], seqs[j])

            similarity = score / max(len(seqs[i]), len(seqs[j])) * 100

            matrix.iloc[i, j] = round(similarity, 2)

matrix.to_excel(
    os.path.join(output_folder, "Prophage_Similarity_Matrix.xlsx")
)

print("\nSimilarity matrix created.")



plt.figure(figsize=(10, 8))

plt.imshow(matrix.astype(float), aspect="auto")

plt.colorbar(label="Similarity (%)")

plt.xticks(range(len(names)), names, rotation=90)

plt.yticks(range(len(names)), names)

plt.tight_layout()

plt.savefig(
    os.path.join(output_folder, "Prophage_Heatmap.png"),
    dpi=300
)

plt.close()

print("Heatmap created.")
