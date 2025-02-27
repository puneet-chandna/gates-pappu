# Gates-Pappu

Gates-Pappu is a Python script designed to automate Bing searches, enabling users to accumulate Microsoft Rewards points effortlessly. By performing random searches, users can earn points that can be redeemed for various rewards, including gift cards and donations.

## Features

- **Automated Random Searches**: The script generates random search terms and performs searches on Bing using the Microsoft Edge browser.
- **Customizable Search Intervals**: Users can set the time interval between searches to mimic natural browsing behavior.
- **Logging**: Each search term is logged into a file (`search_log.txt`) for reference.

## Prerequisites

- **Operating System**: Linux
- **Python**: Ensure Python 3.x is installed on your system.
- **Microsoft Edge**: The script utilizes Microsoft Edge for performing searches.
- **xdotool**: A tool to simulate keyboard input and control window focus. Install it using your package manager:

  ```bash
  sudo apt-get install xdotool
  ```


## Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/puneet-chandna/gates-pappu.git
   cd gates-pappu
   ```


2. **Install Required Python Packages**:

   The script does not require any external Python packages beyond the standard library.

## Usage

1. **Run the Script**:

   ```bash
   python3 bing.py
   ```


   The script will start performing random Bing searches at specified intervals.

2. **Customize Search Terms**:

   You can modify the list of search terms within the `bing.py` script to include topics of your interest.

3. **Adjust Search Intervals**:

   The default interval between searches is set within the script. You can modify the `sleep_time` variable to change this interval.

## Important Notes

- **Ethical Considerations**: Automating searches to earn rewards may violate Microsoft's Terms of Service. Use this script responsibly and at your own discretion.
- **Logging**: All performed search terms are logged in `search_log.txt` for your reference.
- **Termination**: To stop the script, press `Ctrl + C` in the terminal.

## Disclaimer

This project is intended for educational purposes only. The author is not responsible for any misuse of this script.

---

*Note: Automating searches to earn rewards may violate Microsoft's Terms of Service. Ensure you understand and comply with all applicable terms and conditions before using this script.* 
