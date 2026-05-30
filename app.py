import os
import sys

def execute_user_command():
    # Intentionally unsafe: reading directly from command line arguments
    user_input = sys.argv[1]
    
    print(f"Running custom maintenance routine for: {user_input}")
    
    # Classic Command Injection vulnerability
    # An attacker passing "test; rm -rf /" would break out of the intended command
    os.system("echo " + user_input)

if __name__ == "__main__":
    execute_user_command()
