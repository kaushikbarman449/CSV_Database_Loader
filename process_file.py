import pandas as pd

df = pd.read_csv("adult.csv")

df = df.drop(columns=['education.num', 'fnlwgt'])

df.columns = df.columns.str.replace(".", "_", regex=False)

df = df.astype(
    {col: "string" for col in df.select_dtypes(include="object").columns})

replacement = {
    "-": "_",
    "(": "_",
    ")": "_",
    "Female": "F",
    "Male": "M",
    "Asian_Pac_Islander": "Asian",
    "Outlying_US_Guam_USVI_etc_": "US_Territories"
}

for old, new in replacement.items():
    df[df.select_dtypes(include="string").columns] = (
        df.select_dtypes(include="string").apply(
            lambda s: s.str.replace(old, new, regex=False)
        )
    )

print(df.drop_duplicates(subset=["education"]))
