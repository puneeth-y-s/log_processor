import sys
from collections import defaultdict
from typing import List, Tuple

def process_log_file(file_path: str) -> List[Tuple[str, int, int]]:
    """Process the log file and generate a report of user session details.

    Args:
        file_path (str): The path to the log file to be processed.

    Returns:
        List[Tuple[str, int, int]]: A list of tuples containing user session details.
            Each tuple consists of three elements:
            - username (str): The username of the user.
            - number_of_sessions (int): The number of sessions for the user.
            - total_duration (int): The total duration of sessions for the user in seconds.

    Raises:
        Exception: If an invalid session detail is encountered in the log file.
    """
    # Dictionary for storing sessions for each user
    user_sessions = defaultdict(list)
    # Store earliest start time
    earliest_start_time = None

    # Open the log file in read mode
    with open(file_path, 'r') as file:
        # Iterate through each line in the file
        for line in file:
            # Split the line into session details: timestamp, username, action
            session_details = line.strip().split()

            # Check if all necessary session details are present in the given log file
            if len(session_details) != 3:
                raise Exception("Provided log file contains an invalid session details")

            # Extract session information
            timestamp, username, action = session_details

            # Handle "Start" action
            if action == "Start":
                # Add the username and start time to the user_sessions dictionary
                user_sessions[username].append((timestamp, None))

                # Update the earliest start time if it is None
                if earliest_start_time is None:
                    earliest_start_time = timestamp

            # Handle "End" action
            elif action == "End":
                # If there is a matching "Start" action, update its end time
                if username in user_sessions and user_sessions[username]:
                    for index, session in enumerate(user_sessions[username]):
                        end_time = session[1]
                        if end_time is None:
                            user_sessions[username][index] = (session[0], timestamp)
                            break
                    else:
                        # If no matching "Start" action is found, create a session with the earliest start time
                        user_sessions[username].append((earliest_start_time, timestamp))
                else:
                    # If no sessions found for the user, create a session with the earliest start time
                    user_sessions[username] = []
                    user_sessions[username].append((earliest_start_time, timestamp))

    # Generate the report for each user
    report = []

    for username, sessions in user_sessions.items():
        total_duration = 0
        num_sessions = len(sessions)

        # Calculate total duration for each session
        for start_time, end_time in sessions:
            start_hour, start_min, start_sec = map(int, start_time.split(':'))
            # If end time is available, calculate duration, else use start time as end time
            if end_time:
                end_hour, end_min, end_sec = map(int, end_time.split(':'))
            else:
                end_hour, end_min, end_sec = map(int, start_time.split(':'))
            duration = (end_hour - start_hour) * 3600 + (end_min - start_min) * 60 + (end_sec - start_sec)

            total_duration += duration

        # Append user's report to the final report list
        report.append((username, num_sessions, total_duration))

    return report

def main():
    if len(sys.argv) != 2:
        print("Usage details: python session_info.py <file_path>")
        return

    # Process the log file and generate the report
    file_path = sys.argv[1]

    report = process_log_file(file_path)

    # Print the report
    print("Username number_of_sessions total_duration(secs)")
    for entry in report:
        print(f"{entry[0]} \t {entry[1]} \t\t {entry[2]} \t")

if __name__ == "__main__":
    main()