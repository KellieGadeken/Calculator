# Calculator

This is written in python using jupyter notebook. The .py file is also available.

This is a calculator that performs 3 functions: 
1. Cartesian distance
2. Vector x matrix
3. Normalize


For cartesian distance: You need to have four floating point inputs: x1, y1 and x2, y2.

For vector x matrix: You will need 3 floating point inputs for the vector followed by 9 row-major, floating point inputs for the matrix, for a total of 12 floating point. Row major means that m11, m12, and m13 will be the first three floats for the matrix input (i.e., the row is specified first) followed by m21, m22, m23, m31, m32, and m33.

For normalize: You will need 3 floating point inputs for the vector. Normalize will transform a vector into a "unit length" where every value is a fraction of its original value from 0.0 to 1.0.

Menu will display until user selects to quit (option 4). Program will prompt user to enter correct format for menu and selected calculation input. If the correct format is not inputed, the user will be informed they entered it incorrectly. Program will return to menu for user to try again. There are error checks for special characters and letters when performing the calculations. 
