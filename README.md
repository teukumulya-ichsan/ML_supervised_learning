# Supervised Learning by [Teuku Mulia Ichsan](https://github.com/teukumulya-ichsan) 
Learning the basics of machine learning from scratch. For the first phase, we will learn supervised learning techniques using scikit-learn and dondOml.

# Starter Guide

## Step 1: Installation Miniconda

### **Mac user**
- Download miniconda for Python 3.7
    - Open this link to download: [Miniconda Mac OS X 64-bit](https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.pkg)
    - Note: Skip this step if you have used Anaconda before. However, I will explain the reasons why you should use the miniconda later in this course.

- Install miniconda
    - Install without changing any options
    - Wait until the installation is complete

- Run the Terminal/Console

### **Linux user**
- Download miniconda untuk Python 3.7
    - Open this link to download: [Miniconda Linux 64-bit](https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh)
    - Note : Skip this step if you have used Anaconda before. However, I will explain the reasons why you should use the miniconda later in this course.
    
- Install miniconda
    - Run terminal/console
    - Install miniconda with command below:
        ```
        bash Miniconda3-latest-Linux-x86_64.sh
        ```
    - Type `yes` for agree a License, therefore `yes` again for  `prepend miniconda install location to PATH`
    - Wait until the installaion is complete
    
- Just to be sure, close and open the terminal again

## Step 2: Installation Jupyter 
- We will install 2 things in the base environment
    ```
    conda install --name base jupyter nb_conda_kernels
    ```

## Step 3: Installation Environment
- Change directory `cd` to work directory folder
    ```
    cd ML_supervised_learning/
    ```
- Run this command to install the environment `dondOml`
    ```
    conda env create -f env_dondOml.yml
    ```

## Step 4: Make sure the environment is installed properly
- Run the following command to check the installation and follow the instructions generated
    ```
    python check_installation.py
    ```
- If it's safe, then we can start studying. Go Ahead!
