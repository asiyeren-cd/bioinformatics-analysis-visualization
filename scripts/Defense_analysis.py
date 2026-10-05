import os
import glob
import pandas as pd

folder = r"C:\Users\asiye\Downloads\DefenseFinder"

files = glob.glob(os.path.join(folder, "*.tabular"))

all_data = []

for file in files:

    strain = os.path.splitext(os.path.basename(file))[0]

    df = pd.read_csv(file, sep="\t")

    print("\n", strain)

    print(df.head())

    genes = df["gene_name"].unique()

    for gene in genes:
        all_data.append([strain, gene])

result = pd.DataFrame(all_data, columns=["Strain", "Gene"])

result.to_excel("Defense_Genes.xlsx", index=False)

print("\nTamamlandı!")
print(result.head())
