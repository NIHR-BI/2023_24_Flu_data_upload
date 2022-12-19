import pandas as pd

url = "https://www2.nphs.wales.nhs.uk/CommunitySurveillanceDocs.nsf/3dc04669c9e1eaa880257062003b246b/023d7e78efdbcc3980258917005779d4/$FILE/Weekly%20ARI%20hospital%20dashboard%20data%20-%20last%2090%20days.xlsx"

a = pd.read_excel(url)

# a.to_excel('test.xlsx')

# out_path = "test.xlsx"

# out_path = "/Users/ssam/PycharmProjects/flu/test/test.xlsx"

# with pd.ExcelWriter(
#         path=out_path,
#         mode="w",
#         engine="xlsxwriter") as writer:
#     a.to_excel(writer, sheet_name="Sheet1")
