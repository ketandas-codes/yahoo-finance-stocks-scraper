import pandas as pd 

row_data = pd.read_csv("yaho_fininces_stocks.csv")
df = row_data.copy()


df = df.drop_duplicates().apply(lambda col: col.str.strip().str.lower()if col.dtype == "object" else col)

# cleaning price
df["price"] = pd.to_numeric(df["price"], errors="coerce")


# cleaning change
df["change"] = pd.to_numeric(df["change"],errors="coerce")



# cleaning volume
df['volume'] = df['volume'].str.replace("m", "", regex=False).str.strip()
df["volume"] = pd.to_numeric(df["volume"],errors="coerce") * 1_000_000

# cleaning market_cap
df["market_cap"] = (df["market_cap"].astype(str) .str.strip().str.lower())
df["market_cap"] = df["market_cap"].apply(
        lambda x:
            float(x.replace("b", "")) * 1_000_000_000 if "b" in x else
            float(x.replace("t", "")) * 1_000_000_000_000 if "t" in x else
            None
    )
df["market_cap"] = df["market_cap"].round(0).astype("Int64")
print(df['market_cap'].to_string())

# cleaning pe_ratio
df["pe_ratio"] =pd.to_numeric(df["pe_ratio"],errors="coerce")
df["pe_ratio"] = df["pe_ratio"].fillna("--")




df.to_csv("yaho_fininces_stocks_data.csv",index=False)
print("data is stored")



