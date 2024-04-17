# ExamsAndTariffs

(COMPLETED) A simple tool I used during a specific tasks at my previous workplace. It helps me create a structured Excel file, given a set of inputs that I enter into a window.

# Setup
xThe language used is Python
## Python and packages used
- Python version: 3.12
- GUI: `tkinter`
- Read/write Excel files: `openpyxl`
- Classes: `dataclass`

# Structure
![pythonProjectTree](https://github.com/emmedibi/ExamsAndTariffs/assets/55384897/87e1d83b-9dd8-49f3-9de7-897b03a35ed5)

The project is divided in three part:
- main.py
- excelCreation package
- gui package
I decided to create two packages to divided the interface and the calculation part.
## Main.py
Main.py contains only the gui package import, that allows the app to start correctly.
## excelCreation package
The package has the classic python package structure:
- __init__.py file (in this case, it is empty)
- classes.py
- constants.py
- helpers.py
### classes.py
Using the Python library `dataclass` I created the classes usefull to manage data from and excel files.
- ExamData: contains the input from the user
- Tariff contains the tariff's information that will be paired with ExamData element
### contants.py
I created this mapping file for keeping track of the excels' columns label. If something is modified in sampleTariff.xlsx, constants.py has to align.
### helpers.py
This file contains all the logic of the library. It consists in four functions:
- extractTariffesInformation: extracts the sale rules and all the other tariff's information from the sheet selected by the user
- calculatePrice: simply calculates tariffs based by the sale rules
- createExcelFileForNewExam: creates the output file that contains all the tariffs for the exam requested by the user
- createDataForExcel: structures and verifies tha data that receives from the user's input
