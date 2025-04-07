# Personal finance
 I have created this App to keep track of my daily finances. (Credit and Debit)

## Setup guide
1. Clone the repository using `git clone` comand.
2. Go to the Cloned folder and open terminal and type in following command
   ```
   make setup
   ```
   **NOTE: You Must have conda previously installed**

   This will create a conda environment named credit-debit.
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
    make run
    ```

## Future Updates:

🗓️ Add a range feature that filters the transactions between the given range of dates and calculate the total credit/ Debit, Remaining Balance and No. of transactions in those dates.

🕐 Make UI more dynamic; suitable for resizing window.

🕐 Add a pdf creation feature that creates a report that includes Time series plots for credit/ debit and balance.
### Legend

🗓️ = In progress

🕐 = Pending
