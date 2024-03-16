# Log File Processor

This script processes a log file containing session details and generates a report of user session details.

## Usage

1. **Clone the Repository**: Clone this repository to your local machine.

   ```bash
   git clone https://github.com/puneeth-y-s/log_processor.git
   ```

2. Navigate to the Directory: Navigate to the directory containing the script using the below given command.

   ```
   cd log_processor
   ```

3. Run the Script: Run the script by providing the path to the log file as a command-line argument.

   ```
   python session_info.py path/to/log/file.txt
   ```

   Ex: python session_info.py samplelog1.txt or
   python3 session_info.py samplelog1.txt (for above python 3.x.x version)

4. For running test cases, install pytest using the following command.

   ```
   pip install pytest
   ```

5. Run the testcases using the below command

   ```
   pytest test_session_info.py
   ```
