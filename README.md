### Python Requests Library
Requests is a python library for sending HTTP request. (https://requests.readthedocs.io/en/latest/)
This projects follows simple steps to use the requests library to get a JSON data in any format from a url, convert it into a dataframe using pandas and save it as a csv for downstream analysis.

### The Data
The JSON data consists of flight logs simulated from Mockaroo (https://www.mockaroo.com/), and two dummy datasets from https://dummyjson.com/carts and https://dummyjson.com/products. The carts dataset has a nested structure which presents an interesting challenge.

### Libraries
* Pandas
* Requests

### Steps for Data Conversion
1. Clone the repository and download it to you local folder
2. Create a virtual environment in the root directory ```python3 venv your_virtual_env_name``
3. Activate the virtual environment ```source your_virtual_env_name/bin/activate``` in Mac or ```.\.venv\Scripts\Activate.ps1`` for PowerShell in Windows
4. Install the requests and the pandas library in your activated environment ```pip install requests pandas```
5. At the root, Run the ```main.py``` file, like ```python3 main.py```.
6. Enter the url to extract data from.
7. The program runs and extracts data from the specified url and converts it into a csv. Modify the path if you want it in a different location.

