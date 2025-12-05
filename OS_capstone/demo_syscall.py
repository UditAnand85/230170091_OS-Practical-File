import os

def demo_system_call():
    print("Process ID:", os.getpid())

    filename = "system_call_demo.txt"

    with open(filename, "w") as f:
        f.write("This file is created using system calls invoked through Python.\n")
        f.write("Operating Systems Course – System Call Demonstration.\n")

    print(f"File '{filename}' created successfully.")

    print("\nReading file contents:")
    with open(filename, "r") as f:
        for line in f:
            print(line.strip())

if __name__ == "__main__":
    demo_system_call()
