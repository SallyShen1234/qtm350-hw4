def exploratory_summary(df):
    return {"rows": getattr(df, "shape", (0,0))[0],
            "cols": getattr(df, "shape", (0,0))[1]}
