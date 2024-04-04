import random
import pandas as pd

no_of_subjects = int(input("Enter No.of subjects: "))
no_of_periods = int(input("Enter no of Periods: "))
no_of_days = int(input("Enter No. of Days: "))

time_table = [[""]*no_of_periods for _ in range(no_of_days)]

time_table_df = pd.DataFrame(time_table, index=["Day-"+str(i) for i in range(1,1+no_of_days)], columns=["T-"+str(i) for i in range(1,1+no_of_periods)])

subjects = ["Sub-"+str(i) for i in range(1,1+no_of_subjects)]

for i in range(no_of_days):
    random.shuffle(subjects)
    for j in range(no_of_periods):
        time_table_df.iloc[i][j] = subjects[j%no_of_subjects]

print(f"Time Table for {no_of_subjects} Subjects and {no_of_days} Days is:")
print(time_table_df)