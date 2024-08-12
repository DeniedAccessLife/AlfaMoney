# AlfaMoney
Script for simulating user interactions with the AlfaMoney game, designed to perform synchronized actions.

## View
Window of the program.

![alt text](https://raw.githubusercontent.com/DeniedAccessLife/AlfaMoney/master/view.png)

## License
This project is licensed under the unlicensed license - see the [LICENSE](LICENSE) file for details.

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

### Step 3: Install Dependencies

#### Windows

1. Ensure that Python is installed. You can download it from [python.org](https://www.python.org/downloads/).
2. Open a Command Prompt or PowerShell and run:

    ```cmd
    pip install -r requirements.txt
    ```

#### Linux

1. Ensure that Python is installed. You can do this by running:

    ```bash
    sudo apt-get install python3
    ```

2. Install the required dependencies:

    ```bash
    pip3 install -r requirements.txt
    ```

### Step 4: Configure the Script

Create or edit the `config.json` file in the project directory to include your specific settings. An example of the `config.json` format:

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

### Step 5: Run the Script

To start the script:

#### Windows

```cmd
python alfa.py
```

#### Linux

```bash
python3 alfa.py
```
