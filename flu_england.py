import pandas as pd


def save_url(url):
    return pd.read_excel(url)


if __name__ == '__main__':
    data = save_url("https://www.england.nhs.uk/statistics/wp-content/uploads/sites/2/2022/12/UEC-Daily-SitRep-Web-File-Timeseries-2.xlsx")
    out_path = "test_eng.xlsx"

    with pd.ExcelWriter(
            path=out_path,
            mode="w",
            engine="xlsxwriter") as writer:
        data.to_excel(writer, sheet_name="Sheet1")
