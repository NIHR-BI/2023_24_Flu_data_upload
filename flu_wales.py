import pandas as pd


def save_url(url):
    return pd.read_excel(url)


if __name__ == '__main__':
    data = save_url("https://www2.nphs.wales.nhs.uk/CommunitySurveillanceDocs.nsf/3dc04669c9e1eaa880257062003b246b"
                    "/023d7e78efdbcc3980258917005779d4/$FILE/Weekly%20ARI%20hospital%20dashboard%20data%20-%20last"
                    "%2090%20days.xlsx")
    out_path = "test_wales.xlsx"

    with pd.ExcelWriter(
            path=out_path,
            mode="w",
            engine="xlsxwriter") as writer:
        data.to_excel(writer, sheet_name="Sheet1")
