import subprocess
import sys

def install_package(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Replace 'pandas' with the package you want to install
install_package('pandas')
