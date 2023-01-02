# Up Initialization
 An executable that reads information from a spreadsheet and then sets the desired settings for the Up Image
## Setup
1. First download Anaconda3 for windows here: [Anaconda Download](https://www.anaconda.com/products/distribution)
2. By downloading Anaconda, Spyder-3 should also be installed. Open this by searching for Spyder in the Windows search bar. If a popup displays follow the instructions.
3. If Spyder-3 is not installed then open up an anaconda terminal by typing anconda into the windows search bar. Once opened type conda install -c anaconda spyder
4. The code requires the pandas package so to install this open an anconda prompt and type the following conda install -c anaconda pandas
5. Download Github Desktop here: [Github Desktop Download](https://desktop.github.com) and follow installation instructions.
6. Once installed open Github Desktop to access initialization.py got File-> Clone Repository select URL, enter the following https://github.com/bgolias/Up-Initialization url and then select where you would like to clone the local repository and press Clone.
7. Using the Spyder IDE you can now open and edit the initialization.py file by going to File-> Open and then selecting the local initialization.py file
8. Any edits that need to be made can be done in the IDE now and testing can be done by pressing F5 in the console which will run the script. The sript however looks for a csv file present in the C:\Utils folder so if that is not present the program will not work.
9. Once the neccessary changes are made the user can commit the changes by opening github desktop selecting the repository and hitting commit to main. To fully commit the changes the user should then select Push Origin which will then update the repository at the GitHub URL.
10. Once all changes are made and pushed to the remote repository the user should delete all of the local repository files to ensure that in the future the most up to date files are used. 
## Code Functions
- The code asks the user for a Device Type and SN (Plan is to change it so the new audio board will send this information)
* Based on the entered information the program will select a single row in the csv file and populate an array with the device information. If the entry in the row is empty the default is used. If a column is not present the default is also used however certain columns are required to be entered in the csv file which are BCG Serial, Unit Number, and UID as well as entering the Temphare Computer IP. All must be written exactly how they are written here or else the program will not detect them. The following are the column names with there corresponing default value.
1. Unit Name: No default as this a required entry
	- Entries must contain one of the following:
		- SPP
		* Red
		+ UHF
		- NET-15
		* TT-NET
		+ 1MC
		- IVCS
		+ LS-654
		* SPP-PM
2. Equipment Type: ""
3. Station: 1
4. Default Group: 23
5. Co-Loc: 0
6. IC-Offset: 0
7. Override Frequency: 0
8. Circuit Number: 1
9. Ring Line: N
10. Instructor Flag: N
11. IP Address: 10.10.17.21
12. Subnet Mask: 255.255.255.0
13. Gateway: NONE
14. Multicast IP: 225.0.2.
15. GMDSS Net Port: 5020
16. UID: 13
17. Recording: N
18. PC NAME: DESKTOP-F61EA5
19. VHF MMSI: ""
20. BCG Serial: ""
21. Mic Type: Hand
22. Firmware: 4.1
23. IVCS\LS654 Loc: 2
24. Open Lines: 1
25. Circuits: 1
26. Left and Right UID: 1
 


