BabyNamePopularity
==================

Graphs the popularity of two first names against each other over time.

Requires the download of a zipped set of files from the Social Secutiry Administration (http://www.ssa.gov/oact/babynames/names.zip).  This batch of tab separated values is the total accumulation of names by birth year (each file is a different year), given that there are at least 5 of the name in a given year.  The code parses the file, searches for the baby names (takes both male and female births together) and graphs the popularity over time together.

The program should be run with three arguments: 2 names, separated by spaces, followed by the file path to the folder in which you saved the baby names files downloaded from the SSA. The formatting should be something like : "python NamesMulti.py John Mary /home/Downloads/Baby Names/" (without outer quotes).

Dependencies:

http://matplotlib.org/index.html (matplotlib)

http://www.ssa.gov/oact/babynames/names.zip (zipped files)

