import pandas as pd
import requests
from bs4 import BeautifulSoup


def retrieve_first_url(webpage, text_in_url):
    data = requests.get(url=webpage)
    data_soup = BeautifulSoup(data.content, "html.parser")

    # find all <a href> references
    for link in data_soup.find_all("a"):
        # Retrieve the first URL with the text bellow
        if link["href"].find(text_in_url) > -1:
            # Use this link to scrape
            linkToScrape = link["href"]
            return linkToScrape


def is_even(value):
    if value % 2 == 0:
        return True
    else:
        return False


def fill_from_cell_before(df, row, col_before):
    col_after = col_before + 1
    df.loc[row, col_after] = df.loc[row, col_before]


def fill_merged_dates(df, row, col_start):
    """This assumes that the dates start from column 5 and the date is in the odd columns and there are two columns
    per date"""
    max_cols = len(df.columns)
    for col in range(col_start, max_cols + 1):
        if is_even(col):
            fill_from_cell_before(df, row, col - 1)
    return df


def remove_column(df, columns_to_remove):
    return df.drop(columns=columns_to_remove)


def drop_nas_rows_in_col(df, col):
    return df[df[col].notna()]


def set_multiindex_headers(df, header_rows):
    df.columns = pd.MultiIndex.from_frame(df.T.iloc[:, header_rows])
    # df.drop(labels=header_rows, axis=0, inplace=True)
    return df


def set_index_cols(df, index_col_names):
    return df.set_index(index_col_names)


def remove_cols_containing_text(df, col, text):
    return df[df[col] != text]


def clean(
    df: object,
    na_col1: int,
    date_row: int,
    date_col_start: int,
    columns_to_remove: int,
    header_rows: list,
    index_col_names: list,
    na_col2: int,
    remove_col1: int,
    remove_text1: str,
    remove_col2: int,
    remove_text2: str,
) -> object:
    fill_merged_dates(df, date_row, date_col_start)
    df = remove_column(df, columns_to_remove)
    df = set_index_cols(df, index_col_names)
    df = drop_nas_rows_in_col(df, na_col1)
    df = set_multiindex_headers(df, header_rows)
    df = df.melt(ignore_index=False)
    df = df.reset_index()
    df = drop_nas_rows_in_col(df, na_col2)
    df = remove_cols_containing_text(df, remove_col1, remove_text1)
    df = remove_cols_containing_text(df, remove_col2, remove_text2)
    return df


if __name__ == "__main__":
    url_to_use = retrieve_first_url(
        "https://www.england.nhs.uk/statistics/statistical-work-areas/uec-sitrep/urgent-and-emergency-care-daily-situation-reports-2023-24/",
        "UEC-Daily-SitRep",
    )

    # "https://www.england.nhs.uk/statistics/wp-content/uploads/sites/2/2023/12/Web-File-Timeseries-UEC-Daily-SitRep.xlsm"

    data = pd.read_excel(
        io=url_to_use, sheet_name="Flu", header=None, usecols="B:XFD", skiprows=13
    )

    clean_data = clean(
        df=data,
        na_col1=5,
        date_row=0,
        date_col_start=5,
        columns_to_remove=2,
        index_col_names=[1, 3, 4],
        header_rows=[0, 1],
        na_col2=3,
        remove_col1=3,
        remove_text1="Code",
        remove_col2=3,
        remove_text2="-",
    ).dropna(how="all")

    clean_data.columns = [
        "region",
        "trust_code",
        "trust_name",
        "date",
        "measure",
        "value",
    ]

    with open("england_flu_data.csv", "w+") as f:
        f.write(clean_data.to_csv(index=False))
