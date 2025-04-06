# Personal finance
 I have created this App to keep track of my daily finances. (Credit and Debit)

## Setup guide
1. Clone the repository using `git clone` comand.
2. Go to the Cloned folder and open terminal and type in following command
   ```
   make setup
   ```
   **You Must have conda previously installed**
   This will create a conda environment named credit debit.
4. Activate the conda environment by typing following in the terminal;
   ```
   conda activate credit-debit
   ```
7. Now you can install dependencies by executing Following command
   ```
   make pip-tools
   ```
10. After all the dependencies havce been installed. Run the application:
    ```
    python app.py
    ```
