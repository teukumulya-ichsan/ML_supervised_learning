import subprocess

req = {
    "python", "tqdm", "nb_conda_kernels", "pip", "ipython", "numpy", "scipy", "pandas", 
    "scikit-learn", "matplotlib", "seaborn", "ipywidgets", "nltk", 
    "xgboost", "scikit-optimize", "jcopml", "luwiji", "pillow"
}
env_name = "jcopml"
working_folder = "ML_supervised_learning"
env_file = "env_jcopml.yml"


def existing_env():
    result = subprocess.run(["conda", "env", "list"], stdout=subprocess.PIPE)
    result = result.stdout.decode('utf-8').split("\n")
    return [r.split()[0] for r in result if "envs" in r]


def existing_package(env):
    result = subprocess.run(["conda", "list", "--name", env], stdout=subprocess.PIPE)
    result = result.stdout.decode('utf-8').split("\n")
    return [r.split()[0] for r in result[4:-1]]


def main():
    if "jupyter" in existing_package("base"):
        print("✓ jupyter is installed correctly\n")
        if "nb_conda_kernels" in existing_package("base"):
            print("✓ nb_conda_kernels is installed correctly\n")
            if env_name in existing_env():
                print(f"✓ Environment {env_name} detected\n")
                exist = set(existing_package(env_name))
                if req.issubset(exist):
                    print(f"✓ The package is installed correctly in the environment {env_name}\n")
                    print("✓ Installation went well. Have a good study!")                
                else:
                    print(f"It looks like a package {req - exist} Not yet installed, maybe because of internet problems")
                    print("The easiest way to solve this is to reinstall the environment")
                    print("Note: No need to worry because everything that has been downloaded will be skip")
                    print()
                    print("First remove the environment that is already created")
                    print(f">> conda env remove --name {env_name}")
                    print(f"Then re-create the environment. Make sure it's in the work folder `{working_folder}`")
                    print(f">> conda env create -f {env_file}")
            else:
                print(f"Environment {env_name} not found.")
                print(f"Please run the following command in the work folder `{working_folder}`")
                print(f">> conda env create -f {env_file}")
        else:
            print("Do you use Anaconda? I recommend using a miniconda.")
            print("For now, please run the following command")
            print(">> conda install nb_conda_kernels")
    else:
        print("Please run the following command")
        print(">> conda install jupyter nb_conda_kernels")
        
if __name__ == "__main__":
    main()
