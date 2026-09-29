import pandas as pd


def CleanF1Results(df_in: pd.DataFrame) -> pd.DataFrame:
    df = df_in.copy()

    df.columns = [c.strip().lower().replace(" ", "_") for c in df.columns]

    df["position"] = pd.to_numeric(
        df["position"].astype(str).str.replace(r"[^0-9]", "", regex=True),
        errors="coerce"
    ).astype("Int64")

    df["grid"] = pd.to_numeric(
        df["grid"].astype(str).str.replace(r"[^0-9]", "", regex=True),
        errors="coerce"
    ).astype("Int64")

    df["points"] = pd.to_numeric(
        df["points"].astype(str).str.replace(r"[^0-9.\-]", "", regex=True),
        errors="coerce"
    )

    df["laps"] = pd.to_numeric(
        df["laps"].astype(str).str.replace(r"[^0-9]", "", regex=True),
        errors="coerce"
    ).astype("Int64")

    df["fastest_lap_rank"] = pd.to_numeric(df["fastest_lap_rank"], errors="coerce").astype("Int64")

    df["finished"] = df["status"].str.strip().str.lower() == "finished"

    df = df.sort_values(["season", "round", "position"], na_position="last")
    df = df.drop_duplicates(subset=["season", "round", "driver_id"], keep="first").reset_index(drop=True)

    return df
