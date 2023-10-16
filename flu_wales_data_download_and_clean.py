import requests
import pandas as pd


def drop_nas_rows_in_col(df, col):
    return df[df[col].notna()]


def remove_cols_containing_text(df, col, text):
    return df[df[col] != text]


def concat_sheets(df, sheet_names):
    concat_df = pd.DataFrame()
    for s in sheet_names:
        concat_df = pd.concat([concat_df, df.get(s)])
    return concat_df


def load_data(sheet_names: list):
    return pd.read_excel(
        io="Weekly ARI hospital dashboard data - last 90 days.xlsx",
        sheet_name=sheets
    )


def clean(df: object, sheet_names: list) -> object:
    df = concat_sheets(df, sheet_names)
    df = pd.melt(frame=df,
                 id_vars=['Wk_End_Date', 'Infection', 'HB', 'Age_Group', 'Sex'],
                 value_vars=['Com_Acq_Cases_Adm_Hosp', 'Com_Acq_Cases_Adm_CC', 'Com_Acq_Hosp_Cases',
                             'Ind_Acq_Hosp_Cases', 'Def_Hosp_Acq_Hosp_Cases', 'Com_Acq_Cases_CC_Adm',
                             'Ind_Acq_Cases_CC_Adm', 'Hosp_Acq_Cases_CC_Adm',
                             'Com_Acq_Hosp_IP_Cases', 'Ind_Acq_Hosp_IP_Cases',
                             'Hosp_Acq_Hosp_IP_Cases', 'CC_IP_Cases'],
                 var_name='measure'
                 )
    df = drop_nas_rows_in_col(df, 'value')
    df = remove_cols_containing_text(df, 'HB', 'Wales')
    return df


if __name__ == '__main__':
    # download data
    url = "https://www2.nphs.wales.nhs.uk/CommunitySurveillanceDocs.nsf/3dc04669c9e1eaa880257062003b246b/023d7e78efdbcc3980258917005779d4/$FILE/Weekly%20ARI%20hospital%20dashboard%20data%20-%20last%2090%20days.xlsx"
    url_response = requests.get(url)
    data = url_response.content

    out_path = "Weekly ARI hospital dashboard data - last 90 days.xlsx"
    with open(out_path, 'wb') as file:
        file.write(data)

    # clean data
    sheets = ["Flu com acq cases adm to hosp", "Flu com acq cases adm to CC",
              "Flu hosp cases by acq", "Flu hosp cases adm to CC by acq",
              "Flu hosp IP cases", "Flu CC IP cases"]

    clean_data = clean(load_data(sheets), sheets)
    clean_data.to_csv('wales_flu_data.csv', index=False)
