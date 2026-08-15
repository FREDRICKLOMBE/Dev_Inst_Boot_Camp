import os

main_directory = r"C:\Users\LOMBE\Desktop\Dev_Inst_Boot_Camp"

folders = ["DailyChallenge", "ExerciseXP", "Notes_Exercise"]

for week in range(2, 14):

    week_folder = os.path.join(main_directory, f"Week{week}")

    for day in range(1, 5):

        day_folder = os.path.join(week_folder, f"Day{day}")

        for folder in folders:

            folder_path = os.path.join(day_folder, folder)

            os.makedirs(folder_path, exist_ok=True)