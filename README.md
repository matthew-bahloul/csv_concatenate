# csv concatenate

A script to concatenate an arbitrary amount of CSV files into one master file

To use this script
<br>
<ul>
  <li>Script must be in a directory with sub-directories named after dates in the format YYYY-MM-DD</li>
  <li>Each sub-directory can have any amount of CSV files, the names of the CSV files don't matter</li>
  <li> Running the script
    <ul>
      <li>Windows: in command prompt or powershell type: "py csvConcat.py"</li>
      <li>MacOS: in terminal type "python3 csvConcat.py"</li>
    </ul>
    </ul>
  <li>You will be prompted for the name of a directory. The name of must be of the form "YYYY-MM-DD". If the name of the directory matches the current date, you can also just type "today"</li>
  <li>The script will run and concatenate all the files in to a master file in the directory
</ul>
