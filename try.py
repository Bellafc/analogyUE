from lm_polygraph.estimators import Eccentricity

from src.lm_polygraph.utils.model import WhiteboxModel, BlackboxModel
from src.lm_polygraph import estimate_uncertainty
from src.lm_polygraph.estimators import MaximumTokenProbability, LexicalSimilarity, SemanticEntropy, PointwiseMutualInformation, EigValLaplacian, Focus,DegMat,KernelLanguageEntropy,LUQ, Verbalized1S
import pandas as pd

model = BlackboxModel('','gpt-3.5-turbo'
)
eigv = EigValLaplacian(verbose=True)
deg = DegMat(verbose=True)
ecc = Eccentricity(verbose=True)
lexsim = LexicalSimilarity()
kle = KernelLanguageEntropy()
luq = LUQ()


df=pd.read_csv("gms8k.csv")
for idx, row in df.iterrows():
    if idx <200:
        input=row['question']

        input = f"""Raise three examples of code promples that are relavant to the initial prompt. Then solve the three relavant problem only.
# Problem:
{input}
# Instructions:
## Relevant Problems:
- After "Q: ", describe the problem
- After "A: ", explain the solution and enclose the ultimate answer here.e"""
        estimator_list=[lexsim,kle]
        for estimator in estimator_list:
            thisue=estimate_uncertainty(model, estimator, input_text=input).uncertainty
            print(idx,estimator,thisue)
            df.at[idx, f"an PRR {estimator}"] = thisue
    df.to_csv("gms8k.csv")