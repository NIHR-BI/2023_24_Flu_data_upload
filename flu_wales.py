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


def wales_flu_retrieve_published_date():
    data = requests.get(url="https://www2.nphs.wales.nhs.uk/CommunitySurveillanceDocs.nsf/61c1e930f9121fd080256f2a004937ed/023d7e78efdbcc3980258917005779d4?OpenDocument&AutoFramed")
    data_soup = BeautifulSoup(data.content, 'html.parser')

    text = ''
    # concat all <font> references
    for font in data_soup.find_all("font"):
        text += ' '
        text += font.text
    
    # find the text immediately after the text below
    find_text = 'Published on this site :  '
    start = len(find_text) + text.find(find_text)
    length = 10
    end = start + length

    date = text[start: end]
    return date


if __name__ == '__main__':
    # save data
    sheets = ["Flu com acq cases adm to hosp", "Flu com acq cases adm to CC",
              "Flu hosp cases by acq", "Flu hosp cases adm to CC by acq",
              "Flu hosp IP cases", "Flu CC IP cases"]

    clean_data = clean(load_data(sheets), sheets)

    with open('wales_flu_data.csv', 'w+') as f:
        f.write(clean_data.to_csv(index=False))

    # print(1404*3 + 117*3 + 1404*3 + 1404 + 117 + 117)
    
    # save published date
    with open('wales_flu_published_date.csv', 'w+') as f:
        f.write(wales_flu_retrieve_published_date())
