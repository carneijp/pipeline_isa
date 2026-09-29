from ImpararePackage import dataRequest
import matplotlib.pyplot as plt

query = """
    SELECT proba_1 FROM imparare2_new_isa_set_scored_casos_infeccao
"""
df = dataRequest.get_data(queryText= query, chunck= None)
df["count"] = 1
df["proba_1"] = df["proba_1"].values.round(2)

df_result_GROUPED = df.groupby(by="proba_1").sum()
path = "/workspaces/imparare-surface-materdei-neo/ScriptsLibrary/pipeline/T6/utilities"
df_result_GROUPED.to_csv(f"{path}/distribution.csv", sep= ";")
print(df_result_GROUPED)
plt.figure(figsize=(20, 10))
plt.plot(df_result_GROUPED["count"], label= "Acontecimentos")
plt.title("frequencia de proba")
plt.ylabel("repeticoes")
plt.xlabel("proba")
plt.legend()
plt.show()