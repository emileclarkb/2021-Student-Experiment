# Incline Mechanics Data Analysis
## 2021 Student Investigation

## Overview
It's kinda messy but in a nutshell all the data is stored in the Test-20/40/etc folders.
It is further divided into raw, styled, and styled (cutoff) data tables. Raw being data
with absolutely no changes done to it. Styled being data that has uses some custom data
cleaning subroutines to make it "look better" (more so when it is graphed). And the cutoff
stylized data is the styled data with a set "cutoff point", basically for the 20cm tests
it will ignore all measured values above 20cm.


## Basic Processes
The actual code is a little more sophisticated than that. Having short term recursive
memory, release detection, fall detection, compensation for human interference and
reaction times, as well compensation as collision interference. Not sure if any of that
is important but might be nice to put into the research investigations to show the
steps taken to reduce possible sources of uncertainty.


## How to Use
The time data table: [brief.csv](brief.csv), and velocity data table:
[vbrief.csv](vbrief.csv) will most likely be the most useful files here for you
guys at the moment. They correspond to the time and velocity tables we constructed
previously. The first line in each file is a list of names: 1,2,3,4,5 are the
different trials, avg is the average of the 5 trials, abs is the absolute uncertainty,
and perc is the percentage uncertainty. Each of the next 5 lines follows the same
format: 5 trials, average, absolute, percentage.

Don't worry about the [.gitignore](.gitignore) file, it just makes this repository
look a little nicer.

If you want to see/modify the code check out [data.py](data.py) and its utility
module [util.py](util.py).
