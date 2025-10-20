#!/usr/bin/env python3
"""
Script d'exploration rapide des données de naissances 2021
Version simplifiée pour une première analyse
"""

import pandas as pd


def create_column_metadata_table(df):
    """Crée un tableau de métadonnées pour toutes les colonnes"""
    print("\n📊 TABLEAU DE MÉTADONNÉES DES COLONNES")
    print("=" * 50)

    metadata_list = []

    for column in df.columns:
        # Informations de base
        column_type = str(df[column].dtype)
        total_rows = len(df)
        distinct_count = df[column].nunique()
        null_count = df[column].isnull().sum()

        # Valeurs statistiques (pour les colonnes numériques)
        if df[column].dtype in ["int64", "float64", "int32", "float32"]:
            try:
                avg_value = round(df[column].mean(), 2)
                min_value = df[column].min()
                max_value = df[column].max()
            except Exception:
                avg_value = None
                min_value = None
                max_value = None
        else:
            avg_value = None
            min_value = None
            max_value = None

        metadata_list.append(
            {
                "COLUMN_NAME": column,
                "COLUMN_TYPE": column_type,
                "TOTAL_ROWS": total_rows,
                "DISTINCT_COUNT": distinct_count,
                "NULL_COUNT": null_count,
                "AVG_VALUE": avg_value,
                "MIN_VALUE": min_value,
                "MAX_VALUE": max_value,
            }
        )

    # Création du DataFrame de métadonnées
    metadata_df = pd.DataFrame(metadata_list)

    print(metadata_df.to_string(index=False))

    return metadata_df


def main():
    """Exploration rapide des données"""
    print("🔍 EXPLORATION RAPIDE DES DONNÉES DE NAISSANCES")
    print("=" * 50)

    # Chargement des données
    print("📂 Chargement des données...")
    df = pd.read_csv("sample_data/extrait_donnees_naissances_2021.csv", sep=";")
    print(f"✅ {df.shape[0]} lignes et {df.shape[1]} colonnes chargées")

    # Tableau de métadonnées
    create_column_metadata_table(df)

    # Aperçu des données
    print("\n📋 Aperçu des données:")
    print(df.head())

    print("\n📊 Informations générales:")
    print(df.info())

    # Statistiques descriptives pour les variables numériques
    print("\n📈 Statistiques descriptives:")
    print(df.describe())


if __name__ == "__main__":
    main()
