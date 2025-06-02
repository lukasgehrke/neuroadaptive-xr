import os
import random
import subprocess
import signal
import sys
import time

seed = 1
random.seed(seed)

# Create an environment dictionary that includes our seed.
env = os.environ.copy()
env["MY_RANDOM_SEED"] = str(seed)

script1 = '/Users/schnuckiputz/other/git/2022-CHI-neuroadaptive-haptics/neuroadaptive-xr/NahEnvironment.py'
script2 = '/Users/schnuckiputz/other/git/2022-CHI-neuroadaptive-haptics/neuroadaptive-xr/aleks/run_experiment_lsl.py'

processes = []
processes.append(subprocess.Popen(["python", script1], preexec_fn=os.setsid, env=env))
processes.append(subprocess.Popen(["python", script2], preexec_fn=os.setsid, env=env))

def shutdown_handler(sig, frame):
    print("Received SIGINT, shutting down processes...")
    for proc in processes:
        proc.terminate()
    sys.exit(0)

signal.signal(signal.SIGINT, shutdown_handler)

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    shutdown_handler(None, None)