# Feature Requests and Issues

## Feature Requests

- Run the program until it generates 5 candidates for the schedule. (IN PROGRESS)
  - Would be a bit tricky to implement. The program sometimes doesn't run because of its random  
  nature, and then it would be the halting problem, which is impossible to solve.
  - I could implement a timer that counts 0.5 seconds or so and re-run the program if results are  
  not given.
  - I need to re-write the code so that there is a sort of a "main" function that runs the program  
  once, which can be then looped over as needed.

- Fix a person to certain timeslots and run the program. (IN PROGRESS)
  - The UI will be a bit clunky in CLI, so I think the best way to do this is to create a separate  
  Excel spreadsheet.
  - Sheet1 will hold the pre-assigned schedule, and Sheet2 will hold the 5 candidates for the  
  finalized schedule.
  - Read from Sheet1 > calculate positions > output five different schedules into Sheet2.
  - This may need an overhaul of some functions as the desired workflow of the users isn't a  
  CLI-based one.

- Automatically save the end results to an Excel spreadsheet. (IN PROGRESS)
  - This will be solved automatically once the fixed timeslot feature is implemented.

- Show total hours worked and total free time lost. (DONE)
  - Simple, just add some instance variables for the Person class which will keep track of the hours  
  for each instance of the class.

- Format the output better. (DONE)
  - Would be a simple print statement fix with some for loops to print out each row of the calendar.

- Dynamically add people via an external text file. (DONE)
  - Will need to do some re-writing of the code. Change hard-coded loop counts and get rid of  
  literals. This will reduce repeating code and make the code more maintainable.
  - Use open() and read each line, then append them to the list of names.
  - Since dynamically creating variables with different names inside a for loop is bad practice and  
  probably a debugging nightmare, I will make use of Python's dictionary feature to generate key  
  names and just create class instances as values.

## Issues

- Some runs don't yield a result.
  - Due to the random nature of the assigning process, this could happen if all the logical arrays  
  are full.
  - This will be solved if I set a timer for one second and see if the run yields a result.
  - If the run doesn't generate a result by one second, then the program will re-run.

- Some runs have "ㅡㅡㅡ" in the end result.
  - Due to the random nature of the assigning process, this could happen if all the logical arrays  
  are full.
  - This will be solved if I set a timer for one second and see if the run yields a result.
  - If the run doesn't generate a result by one second, then the program will re-run.

- Assigning each person n times vs. assigning everyone once n times
  - Assign each person x times, because this way we can implement a counter that counts the number  
  of shifts a person takes, and assign different amount of times for each person.
  - This is especially important because the program is now pre-loading the calendar from the Excel  
  sheet.