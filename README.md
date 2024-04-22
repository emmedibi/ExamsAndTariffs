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
## gui package
The package has the classic python package structure:
- __init__.py file
- constants.py
- helpers.py
No classes.py file is needed here.
### __init__.py
In this file we initialize the window through which the applciation receives the input. The file calls "createForm" function from the package's helpers.py file.
### constans.py 
I created this mapping file for keeping track of the tariff requested by the user. The input form translates the user's choice in number to better manage the data (e.g. Private tariff has value equal to 1, National Health Service tariff has value equal to 2). I think it was the easies way to manage this kind of data in the planning phase, giving space eventually to future tariffs addition or deletions.
### helpers.py
It contains all the function useful to create the form and manage the input. The main function is called "createForm" and draws the form window. The other principal function is "submit", that sends the data to "createDataForExcel" function of the excelCreation package. If something goes wrong, the function returns an error window, otherwise the function terminates correctly displaying a information message that ends the application.

## sampleTariff.xslx
The file Excel is divided in two sheets: private tariff and SSN (= NHS for UK) tariff. Every sheet has a list of exemplicative tariffs and their percentage of discount. 
For example in the second row of Privato sheet we have:
ID TARIFFARIO: tariff id - 2
NOME TARIFFARIO: tariff name - Privato Scontato 20% (Discounted Private Tariff)
REGOLA DI SCONTO: discount rule - 80% (so the user will have the 20% off the full price)
Note: I didn't change the label, leaving them in italian.
