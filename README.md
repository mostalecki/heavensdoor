# Skychallenge - Python
Recruitment task for python internship, consisting of 3 tasks called "chapters".
## Chapter 1
Implementation of **Car** class that has following attributes:  
* pax_count - number of passengers riding in the car (including the driver)
* car_mass - mass of the empty car (in kg)
* gear_count - number of gears
* **@property** total_mass - retrieves empty car mass plus mass of passengers, with assumed mass of 70kg per passenger  

Use of class:
```python
from car import Car

my_car = Car(4, 1600, 6)
```
To satisfy legal terms, **pax_count** must be in 1-5 range and **car_mass** cannot be greater than 2000kg. If illegal values will be
used to construct object or assigned to existing object, **IllegalCarError** exception, with an appropriate message, will be raised.  

For a quick demonstration of class run:
```bash
python car.py
```
in console.
## Chapter 2
tasks.py  - Command line tool for managing a list of tasks.  
Provides CRUD functionality and stores tasks in json file.
### Commands
#### Adding new task
```bash
tasks.py add --name  [--deadline] [--description]
```
&nbsp;&nbsp;&nbsp;&nbsp;Parameters:
```
  --name          name of the task (required, max. 20 characters)
  --deadline      task's deadline in ISO format (yyyy-mm-dd)
  --description   description of the task
```
#### Updating task
```bash
tasks.py update TASK_HASH [--name] [--deadline] [--description]
```
&nbsp;&nbsp;&nbsp;&nbsp;Parameters:
```
  TASK_HASH       Task identifier
  --name          name of the task
  --deadline      task's deadline in ISO format (yyyy-mm-dd)
  --description   description of the task
```
#### Deleting task
```bash
tasks.py delete TASK_HASH
```
&nbsp;&nbsp;&nbsp;&nbsp;Parameters:
```
  TASK_HASH       Task identifier
```
#### Listing tasks
```bash
tasks.py list (--all | --today)
```
&nbsp;&nbsp;&nbsp;&nbsp;Parameters:
```
  --all       list every task
  --today     list tasks with today's date as deadline
```
**TASK_HASH** is an identifier assigned to task upon creating with **add** command, based on tasks content. It is used for task identification by other commands.  
Multi-word arguments have to be encased in quotes, e.g. **--name "Paint garage"**.  
Script, as well as all commands also have **--help** switch that essentialy prints what's written here.  


## Chapter 3
This script finds numbers that meet 3 criteria listed below:
1. There are at least two groups of identical adjacent digits (like 11 and 33 in 1123345).
2. Going from left to right, the digits never decrease; they only ever increase or stay the same
3. It is a number in the range between 372\**2 and 809\**2 (both ends inclusive).

To run the script, simply type:
```bash
python chapter3.py
``` 
in console, and script will print how many numbers meet the given criteria along with list containg all the numbers.
