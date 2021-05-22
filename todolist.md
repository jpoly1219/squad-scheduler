# Feature Requests and Issues

## Feature Requests

- Run the program until it generates 5 candidates for the schedule.

- Fix a person to certain timeslots and run the program. (IN PROGRESS)
  - The UI will be a bit cumbersome in CLI, so I think the best way to do this is to create a separate Excel spreadsheet.
  - Sheet1 will hold the pre-assigned schedule, and Sheet2 will hold the 5 candidates for the finalized schedule.
  - Read from Sheet1 > calculate positions > output five different schedules into Sheet2
  - This may need an overhaul of some functions as the desired workflow of the users isn't a CLI-based one.

- Automatically save the end results to an Excel spreadsheet.

- Show total hours worked and total free time lost. (DONE)

- Format the output better. (DONE)

- Dynamically add people via an external text file. (DONE)

## Issues

- Some runs don't yield a result.
  - Due to the random nature of the assigning process, this could happen if all the logical arrays are full.
  - This will be solved if I set a timer for one second and see if the run yields a result.
  - If the run doesn't generate a result by one second, then the program will re-run.

- Some runs have "ㅡㅡㅡ" in the end result.
  - Due to the random nature of the assigning process, this could happen if all the logical arrays are full.
  - This will be solved if I set a timer for one second and see if the run yields a result.
  - If the run doesn't generate a result by one second, then the program will re-run.