# Flu_data_upload

Repeated action to clean and save flu data for Wales and England

## Data sources

| Country | Name | Website link | Public dashboard Link | Direct data link |
| --- | --- | --- | --- | --- |
| England	| UEC Daily SitRep – Web File Timeseries| https://www.england.nhs.uk/statistics/statistical-work-areas/uec-sitrep/urgent-and-emergency-care-daily-situation-reports-2022-23/ | None | The link changes, see the "UEC Daily SitRep – Web File Timeseries" link on the website. |
| Wales	| Weekly ARI Hospital Dashboard Data | https://www2.nphs.wales.nhs.uk/CommunitySurveillanceDocs.nsf | [Tableau](https://public.tableau.com/app/profile/public.health.wales.health.protection/viz/ARI-Hospitaladmissionsdashboard/ARIhospitaladmissionsdashboard?publish=yes) | [Direct download](https://www2.nphs.wales.nhs.uk/CommunitySurveillanceDocs.nsf/3dc04669c9e1eaa880257062003b246b/023d7e78efdbcc3980258917005779d4/$FILE/Weekly%20ARI%20hospital%20dashboard%20data%20-%20last%2090%20days.xlsx) |

## What does the cleaned data look like?
- [England csv file](https://raw.githubusercontent.com/SallySamNIHR/Flu_data_upload/main/england_flu_data.csv)
- [Wales csv file](https://raw.githubusercontent.com/SallySamNIHR/Flu_data_upload/main/wales_flu_data.csv)

## How does the data get cleaned and saved in GitHub?

- There is a recurring trigger for this to automatically happen in GitHub Actions. [England trigger](https://github.com/SallySamNIHR/Flu_data_upload/actions/workflows/flu_england.yml) and [Wales trigger](https://github.com/SallySamNIHR/Flu_data_upload/actions/workflows/flu_wales.yml).
- Each trigger triggers the code to run in its respective yml files stored in the [.github/workflows folder](https://github.com/SallySamNIHR/Flu_data_upload/tree/main/.github/workflows). This yml code is where any changes in the data sets get saved in GitHub.
- As part of the yml code, they run their respective .py code. The [England .py code](https://github.com/SallySamNIHR/Flu_data_upload/blob/main/flu_england.py) contains Python code which extracts the data from the link, cleans it and then saves it as a csv. The [Wales .py code](https://github.com/SallySamNIHR/Flu_data_upload/blob/main/flu_wales.py) contains Python code which takes the [Weekly ARI hospital dashboard data - last 90 days.xlsx file in the GitHub repository](https://github.com/SallySamNIHR/Flu_data_upload/blob/main/Weekly%20ARI%20hospital%20dashboard%20data%20-%20last%2090%20days.xlsx), cleans it and then saves it as a csv. **The Wales data must be manually saved into the GitHub repository for it to be updated as this data can only be accessed from the UK.**
- The yml files contain the code below which outlines how frequently the code is triggered and run. This example says that this schedule will run every day at 10:00am. Search cron to understand more about this syntax.

```
schedule:
  - cron: "0 10 * * *"
```

## How often does the data refresh?

- Data will only be saved in GitHub if it has changed.
- The England website says that the data refreshes every Thursday at 9:30am. The trigger in GitHub is therefore set to 10:00am everyday, in case there are delays.
- The Wales website says that the data is refreshed weekly but it is not clear when exactly this happens. The trigger in GitHub is therefore set to 10:00am everyday.
 
