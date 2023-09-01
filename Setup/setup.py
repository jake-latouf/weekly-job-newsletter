import platform
import subprocess

system = platform.system()

if system == "Linux":
    try:
        # Check if 'apt' (Debian) package manager exists
        subprocess.check_output(["apt", "--version"], stderr=subprocess.STDOUT)
        subprocess.run(['bash', '/app/setup-cron-deb.sh'])
    except FileNotFoundError:
        try:
            # Check if 'yum' (RPM) package manager exists
            subprocess.check_output(["yum", "--version"], stderr=subprocess.STDOUT)
            subprocess.run(['bash', '/app/setup-cron-rpm.sh'])
        except FileNotFoundError:
            print("Neither 'apt' (Debian) nor 'yum' (RPM) package manager found.")