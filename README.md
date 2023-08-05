Running the Python Script

Prerequisites
Python 3.x installed on your machine. If you don't have Python installed, you can download it from the official website: https://www.python.org/downloads/
Instructions
Clone the repository or download the Python script (update-files.py) to your local machine.

Open a terminal or command prompt and navigate to the directory where the script is located.

Run the Python script using the following command:

	python update-files.py

The script will start executing, and you will see the output in the terminal or command prompt.


1) Select multiple files: Users can use the "Select Files" button to choose multiple files from the system using a file dialog.

Display key-value pairs from selected files: The selected files' content will be read, and key-value pairs separated by a colon (':') will be displayed in the text area of the GUI. If a line in the file does not contain a colon, a warning message will be displayed for that line.

2) Select keys and their values will be stored temporary to use later: Users can specify fields to store. In our example we are storing keys- tag,name,repository,applicationName,releaseName

3) Click Save

4) Select a file to replace the content: Users can select a file using the "Select File Content" button. The content of this file will be used to replace the content of the selected files.

5) Replace the content of selected files: Users can click the "Replace Content" button to replace the content of the selected files with the content of the specified replacement file.

6) Change the value of Stored Key: User can Click on "Replace Values from stored values" to have the value replaced with the list of keys that were stored in Step 2

7) Find and Replace the text in all selected files: User can find and replace the text in all selected files. User can provide the text in Find field and the provide the new value in Replace

9) Click Find and Replace and all files will be updated with new text.
