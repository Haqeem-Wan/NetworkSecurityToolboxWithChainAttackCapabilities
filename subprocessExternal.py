import subprocess
import threading
import signal
import time

# This function reads the process' output
def reader(proc):
    while True:
        output = proc.stdout.readline().decode()
        if output == '' and proc.poll() is not None:
            break
        if output:
            print(output.strip())

# Start your subprocess
process = subprocess.Popen(["bettercap", "-iface", "eth0"], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
print("Started bettercap")

# Start the reader function in a separate thread
thread = threading.Thread(target=reader, args=(process,))
thread.start()

#Now you can send the commands
commands = ["help", "active"]
for command in commands:
    print(f"Sending command : {command}")
    process.stdin.write(f"{command}\n".encode())
    process.stdin.flush()
    # Give it some time to process the command and generate output
    time.sleep(2)

# To end the process, send a KeyboardInterrupt
print("Stopping bettercap")
process.send_signal(signal.SIGINT)

# Wait for the process to terminate
process.wait()
thread.join()