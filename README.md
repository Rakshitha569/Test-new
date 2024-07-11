### ✨ Python Basics
 - **application.py:** The \*.py file contains source code for python application
 - **requirements.txt:** This file contains list of open source modules used in the application 



### ✨ Blackduck scan on Python application

#### Prerequisite
- Login to Blackduck - https://bdscan.i.mercedes-benz.com/
- You have created a Project in Blackduck - [Project request tool](https://bdscan-request.app.corpintra.net)
- You have Blackduck API token - [Generate Access Token in Blackduck](https://git.i.mercedes-benz.com/foss/BlackDuckSupport/blob/master/1.%20Create%20a%20Project%20and%20Generate%20Access%20Token%20in%20Blackduck.md)

### 👩‍💻 <ins> How to Run Blackduck scan on a Linux System </ins>
**Run the application & install dependencies**
``` 
pip install -r requirements.txt
python application.py  
```

Basic linux scan command:
```
bash <(curl -s https://detect.synopsys.com/detect9.sh)
--blackduck.url="https://bdscan.i.mercedes-benz.com/" 
--blackduck.api.token="XXXXXXXXXXXXXXXXXXXX"
--blackduck.timeout="300" 
--detect.project.name="Your_Project_Name" 
--detect.project.version.name="Version_Number"
--detect.code.location.name="Your_Project_Name-Version_Number"
```
For more details, please refer the [documentation](https://git.i.mercedes-benz.com/foss/BlackDuckSupport/blob/master/2.%20Blackduck%20Scanning%20Methods-Linux%2CWindows.md#a-on-linux)

### 👩‍💻 <ins> How to Run Blackduck scan on a Windows System </ins>
**Run the application & install dependencies**
``` 
pip install -r requirements.txt
python application.py  
```
**Powershell:**
```
powershell "[Net.ServicePointManager]::SecurityProtocol = 'tls12'; irm https://detect.synopsys.com/detect8.ps1?$(Get-Random) | iex; detect"  --blackduck.url="https://bdscan.i.mercedes-benz.com/"  --blackduck.api.token="XXXXXXXXX"  --detect.project.name='Your_Project_Name'  --detect.project.version.name="Version_Number"  --detect.code.location.name="Your_Project_Name-Version_Number"  
```

**Command_line : <br />**

**Pre-requisite: Install Synopsys_detect_jar from [here](https://sig-repo.synopsys.com/artifactory/bds-integrations-release/com/synopsys/integration/synopsys-detect/)**
```
java -jar  C:/Users/SHETRAK/Downloads/synopsys-detect-9.2.0.jar  --blackduck.url=https://bdscan.i.mercedes-benz.com/  --blackduck.api.token="XXXXX"  --detect.project.name="Your_Project_Name"  --detect.project.version.name="Version_Number"  --detect.code.location.name="Your_Project_Name-Version_Number"
```

Please refer this [documentation](https://git.i.mercedes-benz.com/foss/BlackDuckSupport/blob/master/2.%20Blackduck%20Scanning%20Methods-Linux%2CWindows.md#c-on-synopsys-detect-desktop)

### 👩‍💻 <ins> How to do a Rapid scan </ins>
**Run the application & install dependencies**
``` 
pip install -r requirements.txt
python application.py  
```

Basic rapid scan command:
```
bash <(curl -s -L https://detect.synopsys.com/detect9.sh)
--blackduck.url=https://bdscan.i.mercedes-benz.com/
--blackduck.api.token=$TOKEN
--detect.blackduck.scan.mode=RAPID
```
For more details, please refer the [documentation](https://git.i.mercedes-benz.com/foss/BlackDuckSupport/blob/master/Rapid-Scan.md)


### 👩‍💻 <ins> How to Run IAC and Snippet scan </ins>
**Run the application & install dependencies**
``` 
pip install -r requirements.txt
python application.py  
```

IAC_Scan:
```
bash <(curl -s https://detect.synopsys.com/detect9.sh)
--blackduck.url="https://bdscan.i.mercedes-benz.com/" 
--blackduck.api.token="XXXXXXXXXXXXXXXXXXXX"
--blackduck.timeout="300" 
--detect.project.name="Your_Project_Name" 
--detect.project.version.name="Version_Number"
--detect.code.location.name="Your_Project_Name-Version_Number"
--detect.tools=IAC_SCAN
```

Snippet_Scan:
```
bash <(curl -s https://detect.synopsys.com/detect9.sh)
--blackduck.url="https://bdscan.i.mercedes-benz.com/" 
--blackduck.api.token="XXXXXXXXXXXXXXXXXXXX"
--blackduck.timeout="300" 
--detect.project.name="Your_Project_Name" 
--detect.project.version.name="Version_Number"
--detect.code.location.name="Your_Project_Name-Version_Number"
--detect.blackduck.signature.scanner.snippet.matching="SNIPPET_MATCHING" 
--detect.blackduck.signature.scanner.upload.source.mode=true
```

### 👉 Useful Synopsys detect  commands

For more details on the synopsys detect commands refer here [detect_properties](https://sig-product-docs.synopsys.com/bundle/integrations-detect/page/properties/all-properties.html)
 

       
