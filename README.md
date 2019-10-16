##  **[File-Integrity-Monitor](https://github.com/MaksimEkin/File-Integrity-Monitor)**

File Integrity Monitor is written to be used by Blue Team. It can be used in events such as CDE; however, you can also use the code to monitor integrity of your files. 

**What Can the Script Do?**

The script recursively scan the given directory tree (default is from where the driver.py is). Then, script will log any file changes including;
 1. Modified files
 2. Removed files
 3. Added files

**How to Use?**

We will assume you are running the script on Ubuntu for the rest of the documentation.
* Make sure you have python 3 installed.
	* `sudo apt-get install python`
* Make sure you have the python libraries installed.
	* If you don't have pip: `sudo apt-get install pip`
	* `pip install dictdiffer`
	* Other libraries should already come with default python installation. If you, however, still see errors due to missing library, reference the *Libraries Used* section below to install all the missing libraries. 
* Next, you may simply run **[driver.py](https://github.com/MaksimEkin/File-Integrity-Monitor/blob/master/driver.py)** to start the integrity check.
	* python **[driver.py](https://github.com/MaksimEkin/File-Integrity-Monitor/blob/master/driver.py)**
* There are settings in  **[driver.py](https://github.com/MaksimEkin/File-Integrity-Monitor/blob/master/driver.py)**  that you can change;
	* `ROOT_DIRECTORY` : which directory to start the scan (default = '.')
	* `SCAN_STORAGE` : where to store the hashes (default = 'hashes.pkl')
	* `LOG_FILE` : where to store application log such as errors or events (default = 'app.log')
	* `ALERT_FILE` : where to store integrity alerts (default = 'alert.log')
	* `IGNORE_LIST` : which files are ignored in the integrity check (default is the files created by the script such as the alert, log, and hash storage files)
	* `SLEEP_TIME_SECONDS` : how many seconds to wait between each scan (default = 5). This is recommended when you are working on a device with scarce resources. 

**Recommendations**

 - You should probably change where you will store the hashes, and logs. 
 - You can use the settings in the  **[driver.py](https://github.com/MaksimEkin/File-Integrity-Monitor/blob/master/driver.py)** to change the scan directory, log file, and alert logs location. This will allow you to hide the script, and the logs while still running the integrity check. 
 - Backing-up the hashes, logs, and alerts may be a good idea.

**Use Cases**

 * You may monitor the integrity of the files that may have PII. In this case, you can place the script where your files live, and create a crontab or use task scheduler to run the script. 
 *  You can use the script to monitor the files stored in the web app. 
 * If you are in the Blue Team at a CCDC competition, you can use this script to monitor your server and easily see which files modified. 

**Example Crontab Setup**

Run the integrity checker at reboot.
1. `sudo crontab -e`
2. At the end, add: `@reboot (cd directory_path_to_driver.py && driver.py)`
3. Reboot

**Libraries Used**

1. logging
2. time
3. dictdiffer --> pip install dictdiffer
4. datetime
5. pickle
6. os
7. hashlib


> Written with [StackEdit](https://stackedit.io/).
