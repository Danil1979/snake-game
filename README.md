# Setup

1. Download this repository OR clone this repository to your machine.

# Python Environment Setup

## With Anaconda

1. Open a terminal at the root directory of this repository. 
   
2. If you have an anaconda environment called `snake-game` and you do not wish to replace it, go to `environment.yml` and change the name of the environment on the first line:
   
   ```
   name: snake-game
   ```

3. Create an anaconda environment with the `environment.yml` file:
   
   ```
   conda env create -f environment.yml
   ```

   | &#8505; The `environment.yml` was created with `conda env export --from-history > environment.yml` |
   | --- |

   | &#9888; If the command `conda` cannot be found, you can either add the anaconda binaries folder to system path, or open the terminal from anaconda navigator by clicking the triangle icon next to the `base` environment |
   | --- |

4. Activate the environment (replace `snake-game` with your environment name if you have changed it in step 2):
   
   ```conda activate snake-game```

## Without Anaconda

1. Open a terminal at the root directory of this repository.

2. [*Optional*] Create a virtual environment called `snake-game` to avoid messing with your python installation. 
   
   ```
   python -m venv snake-game
   ```

   Activate the virtual environment

   POSIX (Linux/macOS): `source snake-game/bin/activate`

   Windows (cmd.exe): `snake-game\Scripts\activate.bat`

   Windows (PowerShell): `snake-game\Scripts\Activate.ps1`

3. Install the required libraries.
   
   ```
   pip install -r environment.txt
   ```

   | &#8505; The `environment.txt` was created with `pip list --format=freeze > environment.txt` |
   | --- |

# Activate the Python Server

1. Activate the environment if it is not activated yet.
   
2. Change into the `app` directory.

   ```
   cd app
   ```
   
3. Run the server with:

   ```
   uvicorn server:app --reload
   ```

   The terminal output will display this if the server is started correctly. You may have a different URL.

   ```
   INFO: Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
   INFO: Started reloader process [28720]
   INFO: Started server process [28722]
   INFO: Waiting for application startup.
   INFO: Application startup complete.
   ```

4. Open your browser, go to the URL that has been provided in the terminal.

# API testing

1. [Activate the python server](#activate-the-python-server)
   
2. Append `/docs` to the end of the local server URL. For instance, if the URL is http://127.0.0.1:8000, then go to http://127.0.0.1:8000/docs