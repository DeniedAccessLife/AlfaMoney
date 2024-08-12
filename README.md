# AlfaMoney
Script for simulating user interactions with the AlfaMoney game, designed to perform synchronized actions.

# View
Window of the program.

![alt text](https://raw.githubusercontent.com/DeniedAccessLife/AlfaMoney/master/view.png)

## Installation and Setup
### Step 1: Clone the Repository
Clone this repository to your local machine using the following command:
```bash
git clone https://github.com/DeniedAccessLife/AlfaMoney.git
```
### Step 2: Navigate to the Project Directory
Move into the cloned project directory:
```bash
cd AlfaMoney
```
### Step 3: Create and Activate a Virtual Environment (Optional but Recommended)
It's a good practice to use a virtual environment to manage dependencies for your project.
#### Windows
1. Create a virtual environment:
    ```cmd
    python -m venv venv
    ```
2. Activate the virtual environment:
    ```cmd
    .\venv\Scripts\activate
    ```
#### Linux
1. Create a virtual environment:
    ```bash
    python3 -m venv venv
    ```
2. Activate the virtual environment:
    ```bash
    source venv/bin/activate
    ```
### Step 4: Install Dependencies
With the virtual environment activated, install the required dependencies:
#### Windows
```cmd
pip install -r requirements.txt
```
#### Linux
```bash
pip3 install -r requirements.txt
```
### Step 5: Configure the Script
Create or edit the `Config.json` file in the project directory to include your specific settings. An example of the `Config.json` format:
```json
{
  "user_id": "your_user_id",
  "api_key": "your_api_key",
  "delay_range": [3, 10],
  "click_count_range": [10, 60],
  "energy_delay_range": [100, 350]
}
```
Make sure `user_id` and `api_key` are not empty.
### Step 6: Run the Script
To start the script:
#### Windows
```cmd
python AlfaMoney.py
```
#### Linux
```bash
python3 AlfaMoney.py
```

# License
This project is licensed under the unlicensed license - see the [LICENSE](LICENSE) file for details.
