import requests
import pandas as pd


def drop_nas_rows_in_col(df, col):
    return df[df[col].notna()]


def remove_cols_containing_text(df, col, text):
    return df[df[col] != text]


def include_cols_containing_text(df, col, text):
    return df[df[col] == text]


def concat_sheets(df, sheet_names):
    concat_df = pd.DataFrame()
    for s in sheet_names:
        concat_df = pd.concat([concat_df, df.get(s)])
    return concat_df


def load_data(sheet_names: list):
    return pd.read_excel(
        io="Weekly ARI hospital dashboard data - last 90 days.xlsx", sheet_name=sheets
    )


def clean(df: object, sheet_names: list) -> object:
    df = concat_sheets(df, sheet_names)
    df = pd.melt(
        frame=df,
        id_vars=["Date", "Infection", "HB", "Age_Group", "Sex"],
        value_vars=[
            # "Roll_ARI_HB_COHA_Cases",  # "Com_Acq_Cases_Adm_Hosp",
            # "Roll_ARI_COCCA_Cases",  # "Com_Acq_Cases_Adm_CC",
            "Roll_ARI_HB_COHA_Cases",  # "Com_Acq_Hosp_Cases",
            "Roll_ARI_HB_IO_Cases",  # "Ind_Acq_Hosp_Cases",
            "Roll_ARI_HB_DHO_Cases",  # "Def_Hosp_Acq_Hosp_Cases",
            # "Roll_ARI_HB_PHO_Cases",  # unk
            "Roll_ARI_CC_COHA_Cases",  # "Com_Acq_Cases_CC_Adm",
            "Roll_ARI_CC_IO_Cases",  # "Ind_Acq_Cases_CC_Adm",
            "Roll_ARI_CC_HO_Cases",  # "Hosp_Acq_Cases_CC_Adm",
            # "ARI_HB_COHA_IPs",  # "Com_Acq_Hosp_IP_Cases",
            # "ARI_HB_IO_IPs",  # "Ind_Acq_Hosp_IP_Cases",
            # "ARI_HB_HO_IPs",  # "Hosp_Acq_Hosp_IP_Cases",
            # "ARI_HB_IPs",  # unk
            # "ARI_CC_IPs",  # "CC_IP_Cases",
        ],
        var_name="measure",
    )
    df = drop_nas_rows_in_col(df, "value")
    df = remove_cols_containing_text(df, "HB", "Wales")
    df = include_cols_containing_text(df, "Infection", "Influenza")
    return df


if __name__ == "__main__":
    # download data
    url = "https://www2.nphs.wales.nhs.uk/CommunitySurveillanceDocs.nsf/61c1e930f9121fd080256f2a004937ed/023d7e78efdbcc3980258917005779d4/$FILE/Weekly%20integrated%20ARI%20hospital%20dashboard%20data%20-%20last%2090%20days.xlsx"
    url_response = requests.get(url)
    data = url_response.content

    out_path = "Weekly ARI hospital dashboard data - last 90 days.xlsx"
    with open(out_path, "wb") as file:
        file.write(data)

    # clean data
    sheets = [
        # "Com acq cases adm to hosp",
        # "Com acq cases adm to CC",
        "Hosp cases by acq",
        "Hosp cases adm to CC by acq",
        # "Hosp IP cases",
        # "CC IP cases",
    ]

    clean_data = clean(load_data(sheets), sheets)
    clean_data.to_csv("wales_flu_data.csv", index=False)
