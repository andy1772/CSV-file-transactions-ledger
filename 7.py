"""Import Pandas in order to read the csv files and import them to transaction_ledger. Pandas is also used to add the total"""
"""Pending status for statistics. Import csv in order to write and open a csv file named transactions_ledger"""
import pandas as pd
import csv
print("Welcome to the Adrek Robotics transaction tracker!")
"""While true will be used throughout the program in case something is misspelled. So the user can try again from the beginning without having to run the program again"""
while True:
    modes = input("What would you like to perform (import/statistics)? ")

    mode_1 = "import"
    mode_2 = "statistics"

    if modes.lower().strip() == mode_1.lower().strip():
        print("Awesome!")
        files = input("Which file would you like to import? The options are transactions_q1.csv or transactions_q2.csv: ")
        file_1 = "transactions_q1.csv"
        file_2 = "transactions_q2.csv"
        """csv.writer was used to create the csv file transaction_ledger. pd.read_csv is necessary before using pd.concat in order to read the csv file. Pd.concat was used in order to import a csv file into transaction_ledger. With Pd.concat you could import one or both files at once"""
        if files.lower().strip() == file_1.lower().strip():
            with open("transaction_ledger.csv", "w") as transaction_ledger:
                writer = csv.writer(transaction_ledger)
            df_1 = pd.read_csv(r'transactions_q1.csv')
            transaction_ledger = pd.concat([df_1]).to_csv('transaction_ledger.csv', index=False)
            transaction_ledger = pd.read_csv("transaction_ledger.csv")
            print(len(transaction_ledger), " Transactions records successfully loaded.")
            options = input("Would you like to run any further analyses (yes/no)? ")

            option_1 = "yes"
            option_2 = "no"
            """The user has the option to end the program after importing any mode or running a statistic. Once the program ends the file transaction_ledger.csv will contain the csv file or files the user imported"""
            if options.lower().strip() == option_2.lower().strip():
                print("Have a good day!")
                break
            modes_2 = input("What further analyses would you like to do (import/statistics)? ")

            mode_1 = "import"
            mode_2 = "statistics"

            if modes_2.lower().strip() == mode_1.lower().strip():
                print("Awesome!")
                files_2 = input("Which file would you like to import? The only option is transactions_q2.csv: WARNING if you choose transactions_q1.csv again program will restart! ")

                file_1 = "transactions_q1.csv"
                file_2 = "transactions_q2.csv"

                if files_2.lower().strip() == file_1.lower().strip():
                    print("We warned you")

                elif files_2.lower().strip() == file_2.lower().strip():
                    df_2 = pd.read_csv(r'transactions_q2.csv')
                    transaction_ledger = pd.concat([df_2]).to_csv('transaction_ledger.csv', index=False)
                    transaction_ledger = pd.read_csv("transaction_ledger.csv")
                    transaction_ledger = pd.concat([df_1, df_2]).to_csv('transaction_ledger.csv', index=False)
                    df_3 = pd.read_csv(r'transaction_ledger.csv')
                    print("Ids already in transaction records")
                    print(df_3.drop(['COMPANY','DATE', 'AMOUNT', 'STATUS'], axis= 1)[df_3.duplicated()])
                    transaction_ledger = pd.concat([df_1, df_2]).drop_duplicates().to_csv('transaction_ledger.csv', index=False)
                    transaction_ledger = pd.concat([df_1, df_2]).drop_duplicates()
                    print(len(transaction_ledger), "Transaction records successfully loaded in total.")
                    print("Congratulations! you have successfully imported both CSV files")
                    options = input("Would you like to run any further analyses (yes/no)? ")

                    """print(len) was used throughout the program to print the number of rows in the requested csv file """

                    option_1 = "yes"
                    option_2 = "no"

                    if options.lower().strip() == option_2.lower().strip():
                        print("Have a good day!")
                        break
                    modes_3 = input("Your only option left is to write statistics: ")

                    mode_3 = "statistics"

                    if modes_3.lower().strip() == mode_3.lower().strip():
                        print("Awesome!")
                        transaction_ledger = pd.read_csv("transaction_ledger.csv")
                        print(transaction_ledger)
                        print("Number of Current Transactions: ", (len(transaction_ledger)))
                        money = transaction_ledger.loc[transaction_ledger['STATUS'] == 'PENDING', 'AMOUNT'].sum()
                        print("Total amount pending: ", money)
                        print("Congratulations! You have performed all modes")
                        options = input("Would you like to restart the program (yes/no)? ")

                        option_1 = "yes"
                        option_2 = "no"
                        if options.lower().strip() == option_2.lower().strip():
                            print("Have a good day!")
                            break
                        elif options.lower().strip() == option_1.lower().strip():
                            print("Ok Weirdo!")
                        else:
                            print("Check your spelling and start again")
                    else:
                        print("Check your spelling and start again")

                else:
                    print("Sorry, that file could not be found/Check your spelling. Please start again.")

            elif modes_2.lower().strip() == mode_2.lower().strip():
                transaction_ledger = pd.read_csv("transaction_ledger.csv")
                print("Number of Current Transactions: ", (len(transaction_ledger)))
                money = transaction_ledger.loc[transaction_ledger['STATUS'] == 'PENDING', 'AMOUNT'].sum()
                print("Total amount pending: ", money)
                print(transaction_ledger)
                options = input("Would you like to run any further analyses (yes/no)? ")

                option_1 = "yes"
                option_2 = "no"
                if options.lower().strip() == option_2.lower().strip():
                    print("Have a good day!")
                    break
                modes_2 = input("What further analyses would you like to do (import/statistics)? ")

                mode_1 = "import"
                mode_2 = "statistics"

                if modes_2.lower().strip() == mode_1.lower().strip():
                    print("Awesome!")
                    files_2 = input("Which file would you like to import? The only option is transactions_q2.csv: WARNING if you choose transactions_q1.csv again program will restart! ")

                    file_1 = "transactions_q1.csv"
                    file_2 = "transactions_q2.csv"

                    if files_2.lower().strip() == file_1.lower().strip():
                        print("We warned you!")

                    elif files_2.lower().strip() == file_2.lower().strip():
                        df_2 = pd.read_csv(r'transactions_q2.csv')
                        transaction_ledger = pd.concat([df_2]).to_csv('transaction_ledger.csv', index=False)
                        transaction_ledger = pd.read_csv("transaction_ledger.csv")
                        transaction_ledger = pd.concat([df_1, df_2]).to_csv('transaction_ledger.csv', index=False)
                        df_3 = pd.read_csv(r'transaction_ledger.csv')
                        print("Ids already in transaction records")
                        print(df_3.drop(['COMPANY', 'DATE', 'AMOUNT', 'STATUS'], axis=1)[df_3.duplicated()])
                        transaction_ledger = pd.concat([df_1, df_2]).drop_duplicates().to_csv('transaction_ledger.csv',index=False)
                        transaction_ledger = pd.concat([df_1, df_2]).drop_duplicates()
                        print(len(transaction_ledger), "Transaction records successfully loaded in total.")
                        print("Congratulations! you have successfully imported both CSV files")
                        options = input("Would you like to run any further analyses (yes/no)? ")

                        option_1 = "yes"
                        option_2 = "no"
                        if options.lower().strip() == option_2.lower().strip():
                            print("Have a good day!")
                            break
                        modes_3 = input("Your only option left is to write statistics: ")

                        mode_3 = "statistics"

                        if modes_3.lower().strip() == mode_3.lower().strip():
                            print("Awesome!")
                            transaction_ledger = pd.read_csv("transaction_ledger.csv")
                            print("Number of Current Transactions: ", (len(transaction_ledger)))
                            money = transaction_ledger.loc[transaction_ledger['STATUS'] == 'PENDING', 'AMOUNT'].sum()
                            print("Total amount pending: ", money)
                            print(transaction_ledger)
                            print("Congratulations! You have performed all modes")
                            options = input("Would you like to restart the program (yes/no)? ")

                            option_1 = "yes"
                            option_2 = "no"
                            if options.lower().strip() == option_2.lower().strip():
                                print("Have a good day!")
                                break
                            else:
                                print("Ok Weirdo!")
                    else:
                        print("Sorry, that file could not be found/Check your spelling. Please start again.")
                elif modes_2.lower().strip() == mode_2.lower().strip():
                    print("Use common sense! You don't run statistics on the same file twice! Start again and remember what you learned")
                else:
                    print("Check your spelling and start again.")
            else:
                print("Check your spelling. Please start again.")

        elif files.lower().strip() == file_2.lower().strip():
            with open("transaction_ledger.csv", "w") as transaction_ledger:
                writer = csv.writer(transaction_ledger)
            df_2 = pd.read_csv(r'transactions_q2.csv')
            transaction_ledger = pd.concat([df_2]).to_csv('transaction_ledger.csv', index=False)
            transaction_ledger = pd.read_csv("transaction_ledger.csv")
            print(len(transaction_ledger), " Transactions records successfully loaded.")
            options = input("Would you like to run any further analyses (yes/no)? ")

            option_1 = "yes"
            option_2 = "no"
            if options.lower().strip() == option_2.lower().strip():
                print("Have a good day!")
                break
            modes_2 = input("What further analyses would you like to do (import/statistics)? ")

            mode_1 = "import"
            mode_2 = "statistics"

            if modes_2.lower().strip() == mode_1.lower().strip():
                print("Awesome!")
                files_2 = input("Which file would you like to import? The only option is transactions_q1.csv: WARNING if you choose transactions_q2.csv again program will restart! ")

                file_1 = "transactions_q1.csv"
                file_2 = "transactions_q2.csv"
                if files_2.lower().strip() == file_2.lower().strip():
                    print("We warned you")

                elif files_2.lower().strip() == file_1.lower().strip():
                    df_1 = pd.read_csv(r'transactions_q1.csv')
                    transaction_ledger = pd.concat([df_1]).to_csv('transaction_ledger.csv', index=False)
                    transaction_ledger = pd.read_csv("transaction_ledger.csv")
                    transaction_ledger = pd.concat([df_1, df_2]).to_csv('transaction_ledger.csv', index=False)
                    df_3 = pd.read_csv(r'transaction_ledger.csv')
                    print("Ids already in transaction records")
                    print(df_3.drop(['COMPANY', 'DATE', 'AMOUNT', 'STATUS'], axis=1)[df_3.duplicated()])
                    transaction_ledger = pd.concat([df_1, df_2]).drop_duplicates().to_csv('transaction_ledger.csv', index=False)
                    transaction_ledger = pd.concat([df_1, df_2]).drop_duplicates()
                    print(len(transaction_ledger), "Transaction records successfully loaded in total.")
                    print("Congratulations! you have successfully imported both CSV files")
                    options = input("Would you like to run any further analyses (yes/no)? ")

                    option_1 = "yes"
                    option_2 = "no"

                    if options.lower().strip() == option_2.lower().strip():
                        print("Have a good day!")
                        break
                    modes_3 = input("Your only option left is to write statistics: ")

                    mode_3 = "statistics"

                    if modes_3.lower().strip() == mode_3.lower().strip():
                        print("Awesome!")
                        transaction_ledger = pd.read_csv("transaction_ledger.csv")
                        print(transaction_ledger)
                        print("Number of Current Transactions: ", (len(transaction_ledger)))
                        money = transaction_ledger.loc[transaction_ledger['STATUS'] == 'PENDING', 'AMOUNT'].sum()
                        print("Total amount pending: ", money)
                        print("Congratulations! You have performed all modes")
                        options = input("Would you like to restart the program (yes/no)? ")

                        option_1 = "yes"
                        option_2 = "no"
                        if options.lower().strip() == option_2.lower().strip():
                            print("Have a good day!")
                            break
                        elif options.lower().strip() == option_1.lower().strip():
                            print("Ok Weirdo!")
                        else:
                            print("Check your spelling and start again")
                    else:
                        print("Check your spelling and start again")

                else:
                    print("Sorry, that file could not be found/Check your spelling. Please start again.")

            elif modes_2.lower().strip() == mode_2.lower().strip():
                transaction_ledger = pd.read_csv("transaction_ledger.csv")
                print("Number of Current Transactions: ", (len(transaction_ledger)))
                money = transaction_ledger.loc[transaction_ledger['STATUS'] == 'PENDING', 'AMOUNT'].sum()
                print("Total amount pending: ", money)
                print(transaction_ledger)
                options = input("Would you like to run any further analyses (yes/no)? ")

                option_1 = "yes"
                option_2 = "no"
                if options.lower().strip() == option_2.lower().strip():
                    print("Have a good day!")
                    break
                modes_2 = input("What further analyses would you like to do (import/statistics)? ")

                mode_1 = "import"
                mode_2 = "statistics"

                if modes_2.lower().strip() == mode_1.lower().strip():
                    print("Awesome!")
                    files_2 = input("Which file would you like to import? The only option is transactions_q1.csv: WARNING if you choose transactions_q2.csv again program will restart! ")

                    file_1 = "transactions_q1.csv"
                    file_2 = "transactions_q2.csv"

                    if files_2.lower().strip() == file_2.lower().strip():
                        print("We warned you!")

                    elif files_2.lower().strip() == file_1.lower().strip():
                        df_1 = pd.read_csv(r'transactions_q1.csv')
                        transaction_ledger = pd.concat([df_1]).to_csv('transaction_ledger.csv', index=False)
                        transaction_ledger = pd.read_csv("transaction_ledger.csv")
                        transaction_ledger = pd.concat([df_1, df_2]).to_csv('transaction_ledger.csv', index=False)
                        df_3 = pd.read_csv(r'transaction_ledger.csv')
                        print("Ids already in transaction records")
                        print(df_3.drop(['COMPANY', 'DATE', 'AMOUNT', 'STATUS'], axis=1)[df_3.duplicated()])
                        transaction_ledger = pd.concat([df_1, df_2]).drop_duplicates().to_csv('transaction_ledger.csv',index=False)
                        transaction_ledger = pd.concat([df_1, df_2]).drop_duplicates()
                        print(len(transaction_ledger), "Transaction records successfully loaded in total.")
                        print("Congratulations! you have successfully imported both CSV files")
                        options = input("Would you like to run any further analyses (yes/no)? ")

                        option_1 = "yes"
                        option_2 = "no"
                        if options.lower().strip() == option_2.lower().strip():
                            print("Have a good day!")
                            break
                        modes_3 = input("Your only option left is to write statistics: ")

                        mode_3 = "statistics"

                        if modes_3.lower().strip() == mode_3.lower().strip():
                            print("Awesome!")
                            transaction_ledger = pd.read_csv("transaction_ledger.csv")
                            print(transaction_ledger)
                            print("Number of Current Transactions: ", (len(transaction_ledger)))
                            money = transaction_ledger.loc[transaction_ledger['STATUS'] == 'PENDING', 'AMOUNT'].sum()
                            print("Total amount pending: ", money)
                            print("Congratulations! You have performed all modes")
                            options = input("Would you like to restart the program (yes/no)? ")

                            option_1 = "yes"
                            option_2 = "no"
                            if options.lower().strip() == option_2.lower().strip():
                                print("Have a good day!")
                                break
                            else:
                                print("Ok Weirdo!")
                    else:
                        print("Sorry, that file could not be found/Check your spelling. Please start again.")
                elif modes_2.lower().strip() == mode_2.lower().strip():
                    print("Use common sense! You don't run statistics on the same file twice! Start again and remember what you learned")
                else:
                    print("Check your spelling and start again.")
            else:
                print("Check your spelling. Please start again.")
        else:
            print("Sorry, that file could not be found/Check your spelling. Please start again.")

    elif modes.lower().strip() == mode_2.lower().strip():
        print("Sorry no transaction data was loaded yet. Please try again")
        options = input("Would you like to run any further analyses (yes/no)? ")

        option_1 = "yes"
        option_2 = "no"

        if options.lower().strip() == option_2.lower().strip():
            print("Have a good day!")
            break

    else:
        print("Check your spelling and try again.")