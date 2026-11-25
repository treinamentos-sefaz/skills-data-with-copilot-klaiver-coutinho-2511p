"""Módulo 2 — Manipulação de DataFrames com pandas.

Complete cada função com o apoio do GitHub Copilot. Prefira operações
vetorizadas e evite alterar o DataFrame original (use ``.copy()``).

Valide com:  ``python lab/check.py --module pandas``
"""
from __future__ import annotations

import numpy as np
import pandas as pd


def load_wines(path: str) -> pd.DataFrame:
    """Leia o CSV em ``path`` e retorne um DataFrame do pandas."""
    return pd.read_csv(path)


def clean_ratings(df: pd.DataFrame) -> pd.DataFrame:
    """Converta a coluna ``rating`` para numérico e remova as linhas cujo
    ``rating`` seja nulo. Retorne o DataFrame limpo."""
    out = df.copy()
    out["rating"] = pd.to_numeric(out["rating"], errors="coerce")
    return out.dropna(subset=["rating"])


def top_varieties_by_avg_rating(df: pd.DataFrame, n: int = 10) -> pd.DataFrame:
    """Retorne as ``n`` variedades com maior média de ``rating`` (colunas:
    variety, avg_rating), ordenadas da maior para a menor."""
    medias = df.groupby("variety", as_index=False)["rating"].mean()
    medias = medias.rename(columns={"rating": "avg_rating"})
    return medias.sort_values("avg_rating", ascending=False).head(n)


def add_rating_category(df: pd.DataFrame) -> pd.DataFrame:
    """Adicione a coluna ``rating_category`` com as faixas: "Baixa" (< 85),
    "Média" (85 a 90) e "Alta" (> 90). Dica: use ``pd.cut``."""
    out = df.copy()
    out["rating_category"] = pd.cut(
        out["rating"],
        bins=[-np.inf, 85, 90, np.inf],
        labels=["Baixa", "Média", "Alta"],
        right=False,
    )
    return out


def enrich_with_country(df: pd.DataFrame) -> pd.DataFrame:
    """Adicione a coluna ``country`` extraindo o último trecho após a vírgula de
    ``region`` (ex.: "Mendocino, California" -> "California")."""
    out = df.copy()
    out["country"] = out["region"].str.split(",").str[-1].str.strip()
    return out
