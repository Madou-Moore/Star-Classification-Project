import pandas as pd

stars = pd.read_csv("sdss_star.csv", skiprows=1)
galaxies = pd.read_csv("sdss_galaxy.csv", skiprows=1)
quasars = pd.read_csv("sdss_qso.csv", skiprows=1)

df = pd.concat([stars, galaxies, quasars], ignore_index=True)

# Clean column names just in case
df.columns = df.columns.str.strip()

print(df.columns.tolist())
print(df["class"].value_counts())

# Shuffle the rows
df = df.sample(frac=1, random_state=42).reset_index(drop=True)

# Create color-index features
df["u_g"] = df["u"] - df["g"]
df["g_r"] = df["g"] - df["r"]
df["r_i"] = df["r"] - df["i"]
df["i_z"] = df["i"] - df["z"]

# Save final dataset
df.to_csv("sdss_star_galaxy_quasar_with_features.csv", index=False)

print("Saved combined dataset!")
