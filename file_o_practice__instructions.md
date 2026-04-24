## Setup
- `file_o_practice.py`

Your job is to create a python script that asks the user to enter (using an `input()` function)

- The name to one of "Explore", "Investigate", "Practice", or "Make" (aka EIPM) folder (from where your terminal is opening your folder, use the relative path)
- The name of the file they wish to create (example: "easy_practice") Call this variable `filename`
- The name of the author
- A one sentence description

And it will output a python skeleton to a file called "{filename}.py" in either your explore, investigate, practice, or make folder. 
So if the user specified the filename to be "easy_practice", then write the skeleton to a file called "easy_practice.py"

Given the following input:
```plaintext
>>> EIPM: practice
>>> Enter the file name: easy_practice
>>> Enter the author: Mr. Nguyen
>>> Enter a description: A skeleton file for a python project
```

This is how I want the skeleton to look:

## Output 
### practice / easy_practice.py
```python
"""
author: Mr. Nguyen
date: November 24, 2025
A skeleton file for a python project
"""

def main():
    # Input
    # Processing
    # Output
    pass

if __name__ == "__main__":
    main()
```
Note: you will need to use `"\n" for newline` and `"\t" for tab` to format it as the sample output
### The date
Notice how I didn't ask the user to input the date? We are going to ask python to calculate today's date for us :)

```python
from datetime import datetime

# gets the date and  time in format (year, month, day, hour, minute, second, microsecond)
todays_date = datetime(2024, 11, 24, 8, 30, 5, 294577)
# format as {Month's name} {day of the month}, {year} 
todays_date = todays_date.strftime("%B %d, %Y") 
# alternate: todays_date = datetime.today().strftime("%B %d, %Y")
print(todays_date)  # November 24, 2025
```