# IoT-Simulation-Platform
Please go to CupCarbon official site download user guide, learn the basic CupCarbon first.

### Our IoT-Simulation-Platform User Document is 'IoT-Simulation-Platform User Document.pdf'

### Our API document that includes our modification is under doc folder

### Our database schema is 'Database Schema.html'

Here is the CupCarbon official site: https://cupcarbon.com/

Installation (Java party)

1. Download the source code form our GitHub (or use the link bellow) - Choose clone or download -> Download ZIP

2. Unzip the ZIP file to get your source code directory: CupCarbon-master

3. Install the JDK 8 (Get the JDK 8 here)

4. Install Eclipse

5. Import the project CupCarbon-master from Eclipse:

Go to File -> Import -> General -> Existing Projects into Workspace -> Click on Next >

Click on the button Brows and choose only the CupCarbon-master directory without selecting any file then click on Finish.

Now the project is ready: Congratulations!

On Eclipse, verify that the compiler uses the version 1.8. If it is not the case, then many files and packages will be highlighted in red color. In this case, do the following changes:

Go to the root of the projet (CupCarbon), click right and choose "Properties"

Click on Java Compiler (on the left) and uncheck the box "Enable project specific settings", click then on the link (on the right) "Configure Workspace Settings ..."

In this window, change the value of "Compiler compliance level" to 1.8.

Then click on the link configure.

Select the last version Java SE 8, then click on "Apply and Close".

Click again on Apply and Close. Chick that all the errors have been eliminated.

Install JavaFx for Eclipse

Use Scene Builder (get Scene Builder): if you want to modify or add GUIs



Installation (Python party)

Make sure your python environment has csv module, pymongo module and pandas module installed.

Recommend using Spyder IDE.



Installation (MongoDB)

Go to: https://www.mongodb.com/

Download MongoDB community server. Using default setting.



Instruction (Python party)

There is no interface for the python project. Last line of generator.py file is actually the interface.

Input the required parameters, save it and run the file.

genSimulationUnit(longitude_of_point_one, latitude_of_point_one, longitude_of_point_two, latitude_of_point_two, number_of_sensors, number_of_users)

After running generator.py, run importToMongoDB.py (Before running importToMongoDB.py, check your MongoDB make sure you have copy of all collections in cs682 database. importToMongoDB.py will clean that database and import new generated data)



Instruction (CupCarbon)

Run the CupCarbon project, when it start successfully, right click your mouse, left click your mouse on "Rest/Reload from DB".

In your left tool bar, choose Users, click Connection button. choose Simulation Parameters, check Mobility/Events check-box.  

At bottom of the window, click the "Sensors" button. Then run simulation. 

If you want to hide user's concern area, check the hide area box at Users left tool bar before running simulation.

All your data are in the cs682 database. Enjoy!!!

