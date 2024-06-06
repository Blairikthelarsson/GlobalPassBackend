# FastApi Server

## Overview
This a sBackend Server For Globass PASS Backend Application 

use Fastapi for API REST Structure and documentation



## Requirements
Python 3.5.2+

## Usage
To run the server, please execute the following from the root directory:

```
We strongly recommand to create a virtual environment .venv 
pip3 install -r requirements.txt
python3 -m main.py
```

and open your browser to here:

```
http://localhost:8000/docs/
```

```
before Test 
RUN the script schema.py for create Database on SQLlite for this test environment
From project's root directory 

python.exe ./db/schema.py 
will create a dabatase on SQLlite just for testing name globalpass lying on sub directory db
globalpass.db 