# import datetime
# import os

# def log(message):
#     if not os.path.exists("logs"):
#         os.makedirs("logs")

#     with open("logs/scan_log.txt", "a") as f:
#         time = datetime.datetime.now()
#         f.write(f"[{time}] {message}\n")

import datetime
import os

def log(message):
    if not os.path.exists("output"):
        os.makedirs("output")

    log_file = os.path.join("output", "scan_log.txt")
    with open(log_file, "a") as f:
        time = datetime.datetime.now()
        f.write(f"[{time}] {message}\n")