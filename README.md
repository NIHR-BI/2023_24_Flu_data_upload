# Flu_data_upload

Repeated action to clean and save flu data for Wales and England

## Data sources

| County | Name | Website link | Direct data link |
| --- | --- | --- | --- |
| England	| UEC Daily SitRep – Web File Timeseries| https://www.england.nhs.uk/statistics/statistical-work-areas/uec-sitrep/urgent-and-emergency-care-daily-situation-reports-2022-23/ | [Direct download](https://www.england.nhs.uk/statistics/wp-content/uploads/sites/2/2022/12/UEC-Daily-SitRep-Web-File-Timeseries-2.xlsx) |
| Wales	| Weekly ARI Hospital Dashboard Data | https://www2.nphs.wales.nhs.uk/CommunitySurveillanceDocs.nsf | [Direct download](https://www2.nphs.wales.nhs.uk/CommunitySurveillanceDocs.nsf/3dc04669c9e1eaa880257062003b246b/023d7e78efdbcc3980258917005779d4/$FILE/Weekly%20ARI%20hospital%20dashboard%20data%20-%20last%2090%20days.xlsx) |

## How does the data get cleaned and saved in GitHub?

- There is a recurring trigger for this to automatically happen in GitHub Actions. [England trigger](https://github.com/SallySamNIHR/Flu_data_upload/actions/workflows/flu_england.yml) and [Wales trigger](https://github.com/SallySamNIHR/Flu_data_upload/actions/workflows/flu_wales.yml).
- Each trigger triggers the code to run in its respective yml files stored in the [.github/workflows folder](https://github.com/SallySamNIHR/Flu_data_upload/tree/main/.github/workflows).
- As part of the yml code, they run respective .py code. This .py code contains Python code which extracts the data from the link, cleans it and then saves it as a csv. [England .py code](https://github.com/SallySamNIHR/Flu_data_upload/blob/main/flu_england.py) and [Wales .py code](https://github.com/SallySamNIHR/Flu_data_upload/blob/main/flu_wales.py)
