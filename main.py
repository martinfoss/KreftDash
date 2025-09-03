
from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
import pandas as pd

# Load data
df_all = pd.read_csv("Alle kreftformer Norge RHF 2024.csv", sep=';')
df_breast = pd.read_csv("Brystkreft RHF Alle Stadier 2024.csv", sep=';')

# Combine datasets
df_all["Dataset"] = "Alle kreftformer"
df_breast["Dataset"] = "Brystkreft"
df = pd.concat([df_all, df_breast], ignore_index=True)

# Create FastAPI app
app = FastAPI(title="Kreftdashboard Norge")

@app.get("/kreftformer")
def get_kreftformer():
    kreftformer = sorted(df["Kreftform"].dropna().unique().tolist())
    return {"kreftformer": kreftformer}

@app.get("/regioner")
def get_regioner():
    regioner = sorted(df["Region"].dropna().unique().tolist())
    return {"regioner": regioner}

@app.get("/data")
def get_data(kreftform: str = Query(None), region: str = Query(None), kjønn: str = Query(None)):
    filtered = df.copy()
    if kreftform:
        filtered = filtered[filtered["Kreftform"] == kreftform]
    if region:
        filtered = filtered[filtered["Region"] == region]
    if kjønn:
        filtered = filtered[filtered["Kjønn"] == kjønn]
    result = filtered[["Kreftform", "Region", "Kjønn", "År", "Tilfeller", "Rate_ujustert", "ASR_Norge"]].dropna()
    return JSONResponse(content=result.to_dict(orient="records"))

@app.get("/statistikk")
def get_statistikk():
    stats = df.groupby(["Kreftform", "Region", "Kjønn"]).agg({
        "Tilfeller": "sum",
        "Personår": "sum"
    }).reset_index()
    stats["Rate_per_100k"] = (stats["Tilfeller"] / stats["Personår"] * 100000).round(1)
    return JSONResponse(content=stats.to_dict(orient="records"))
