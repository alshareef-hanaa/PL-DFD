# PL-DFD
PL-DFD is loot for the framework of modeling purposes in DFD comprising two algorithms (Compatibility Checking and Propagating purpose Labels).


Prerequisites
------------

 - DFD Refinery is written in Python, which can be run by interpreter that is Python 3.7 or later. Python 3.7 can be dowmload from (https://www.python.org/downloads/) 
 
 - Download draw.io from (https://about.draw.io/integrations/#integrations_offline) for drawing DFDs
 
 - Draw.io does not come with dedicated libraries for DFDs, download libraries for DFD from (https://github.com/michenriksen/drawio-threatmodeling)

Usage
------------

1- Draw your DFD by using draw.io

2- Export xml files of DFDs from draw.io

3- Clone the [GitHub repository](https://github.com/alshareef-hanaa/PL-DFD.git):
  
  $ git clone https://github.com/alshareef-hanaa/PL-DFD.git

4- PL-DFD tool comprises two algorithms: the Consistency Checking algorithm and the Purpose Inference algorithm.

Consistency Checking  
---------------------

 1- Go into the directory where the script (main.py)
 
 
 2- To run the script (main.py.) from the terminal, you need to provide the file names of the CSV files for privacy signatures ( from designer and domain expert), XML files for DFD,  and CSV files for system purposes and writing consistency checking result. 
 
 
Purpose Inference 
------------------

 1- Go into the directory where the script (main.py)
 
 2- To run the script (main.py.) from the terminal, you need to provide the file names of the CSV files for privacy signatures ( from designer and domain expert), XML files for DFD,  and CSV files for system purposes and writing the inferred purpose(s) for each flow in your DFD. 

