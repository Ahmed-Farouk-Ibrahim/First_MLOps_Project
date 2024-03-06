# os: to interact with the Operating System
import os
# Path: to create a system compatible path, so no need to write it down manually, you can import this Path which will automatically take care. for ex, Linux uses  forward slash /, but in windows it uses Backward \
'''Using `from pathlib import Path` allows you to work with file paths and directories in a more object-oriented and platform-independent way. It provides an intuitive interface for manipulating file paths and avoids common pitfalls associated with string manipulation, making code more robust and readable. Additionally, it simplifies working with file systems by providing convenient methods for file operations.'''
from pathlib import Path

''' Next script creates a list of file paths and iterates through each path:
It converts each file path to a 'Path' object using Path(filepath).
It separates the directory path and filename using os.path.split(filepath).
If the directory path is not empty (i.e., if the file is not in the root directory), it creates the directory using os.makedirs(filedir, exist_ok=True).
It checks if the file does not exist or if its size is 0 bytes.
If either condition is true, it creates an empty file at that path. This script ensures that all specified files exist and are not empty, creating them if necessary.
'''
package_name = "components"

list_of_files = [
    # The file ".gitkeep" within this directory is typically used as a placeholder file to ensure that the directory is tracked by Git, even if it's empty. This is necessary because Git does not track empty directories by default. Therefore, adding a ".gitkeep" file to an otherwise empty directory allows it to be included in the Git repository.
    ".github/workflows/.gitkeep",  # workflows for CI/CD, Continuous Integration & Continuous Deployment 
    "src/__init__.py", 
    f"src/{package_name}/__init__.py", 
    f"src/{package_name}/data_ingestion.py", 
    f"src/{package_name}/data_transformation.py", 
    f"src/{package_name}/model_trainer.py", 
    f"src/{package_name}/model_evaluation.py", 
    "src/pipeline/__init__.py", 
    "src/pipeline/training_pipeline.py", 
    "src/pipeline/prediction_pipeline.py", 
    "src/logger/logging.py", 
    "src/exception/exception.py", 
    
    
    "src/utils/utils.py", 
    "src/utils/__init__.py", 

    "tests/__init__.py",  # It indicates that the directory contains Python unit tests.
    "tests/unit/__init__.py", # Unit Test is for the individual component, single unit
    "tests/integration/__init__.py", # Integration Testing is for all the units means to combine all the units, all the components
    "init_setup.sh",  # This path represents a shell script file named init_setup.sh. It may contain setup commands to initialize the project environment.
    
    "requirements.txt", #  It typically contains a list of Python dependencies required for the project.
    "requirements_dev.txt",
    "setup.py",  # It is commonly used to define metadata about the project and to facilitate its distribution and installation using tools like pip.
    
    "setup.cfg", # This path represents a configuration file named setup.cfg. It may contain additional settings for the project setup process.

    "pyproject.toml", # It may contain project-specific configuration settings, such as build system configuration or dependency specifications.

    "tox.ini", #  It is commonly used in Python projects to define testing environments and configurations for the tox testing tool.

    # Experiment: Because if I want to run a small small code or snippit, so instead of running it on the python kernel I can directly run inside the experiments.ipynb file 
    "experiments/experiments.ipynb", ]

# It converts each file path to a 'Path' object using Path(filepath).
# It separates the directory path and filename using os.path.split(filepath).
for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    # If the directory path is not empty (i.e., if the file is not in the root directory), it creates the directory using os.makedirs(filedir, exist_ok=True).

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
    # Check if the file does not exist or if its size is 0 bytes. If either condition is true, it creates an empty file at that path. This script ensures that all specified files exist and are not empty, creating them if necessary.
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass # create an empty file

#its updated



'''
package_name = "mongodb_connect"
# src: represents the Source Code Folder, where we write down the project code inside. Everything and apart from that, whatever other infrastructure is there, I will keep outside the SRC folder. 
#  List of file paths representing various files and directories in a project. 
list_of_files = [
   ".github/workflows/ci.yaml", # This path represents a YAML file in the .github/workflows directory. It likely contains configuration for continuous integration workflows.

   "src/__init__.py", # This file is commonly used to indicate that the directory should be treated as a Python package.
   
   f"src/{package_name}/__init__.py", 
   f"src/{package_name}/mongo_crud.py", 
   "tests/__init__.py",  # It indicates that the directory contains Python unit tests.
   "tests/unit/__init__.py", # Unit Test is for the individual component, single unit
   "tests/integration/__init__.py", # Integration Testing is for all the units means to combine all the units, all the components
   "init_setup.sh",  # This path represents a shell script file named init_setup.sh. It may contain setup commands to initialize the project environment.
   "requirements.txt", #  It typically contains a list of Python dependencies required for the project.

   "setup.py",  # It is commonly used to define metadata about the project and to facilitate its distribution and installation using tools like pip.
   
   "setup.cfg", # This path represents a configuration file named setup.cfg. It may contain additional settings for the project setup process.

   "pyproject.toml", # It may contain project-specific configuration settings, such as build system configuration or dependency specifications.

   "tox.ini", #  It is commonly used in Python projects to define testing environments and configurations for the tox testing tool.

   "experiments/experiments.ipynb", 
]
# It converts each file path to a 'Path' object using Path(filepath).
# It separates the directory path and filename using os.path.split(filepath).
for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    # If the directory path is not empty (i.e., if the file is not in the root directory), it creates the directory using os.makedirs(filedir, exist_ok=True).

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
    # Check if the file does not exist or if its size is 0 bytes. If either condition is true, it creates an empty file at that path. This script ensures that all specified files exist and are not empty, creating them if necessary.
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass # create an empty file

#its updated
'''