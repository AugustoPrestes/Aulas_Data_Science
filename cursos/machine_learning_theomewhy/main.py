#%%
import pandas as pd

df = pd.read_excel("../machine_learning_theomewhy/data/dados_cerveja.xlsx")

df.head()
# %%
features = ["temperatura","copo", "espuma", "cor"]
target = "classe"

X = df[features]
y = df[target]
# %%
X = X.replace({
    "mud": 1, "pint":0,
    "sim": 1, "não": 0,
    "escura": 1, "clara": 0 
})
# %%
# Treinando a arvore
from sklearn import tree

arvore = tree.DecisionTreeClassifier()
arvore.fit(X, y)
# %%
import matplotlib.pyplot as plt

plt.figure(dpi=600)

tree.plot_tree(arvore, 
               class_names=arvore.classes_,
               feature_names=features,
               filled=True)
# %%
