import csv

def get_subjects_from_csv():
    """
    Reads subjects data from subjects.csv and returns it as a dictionary.
    """
    subjects = {}
    with open('subjects.csv', mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            program = row['Program']
            semester = int(row['Semester'])
            subject_name = row['Subject']
            credits = int(row['Credits'])
            description = row['Description']
            
            if program not in subjects:
                subjects[program] = {}
            if semester not in subjects[program]:
                subjects[program][semester] = []
            
            subjects[program][semester].append({"name": subject_name, "credits": credits, "description": description})
    return subjects

import pandas as pd

def get_subjects(program_subjects):
    """
    Prints subjects for a specified program up to a given semester in a tabular format using DataFrame.
    
    Args:
    - program_subjects (dict): Dictionary containing subjects data.
    """
    program = input("Enter the program you're interested in: ").capitalize()
    semester = int(input("Enter the semester up to which you want to see the subjects: "))
    
    print(f"Subjects for {program} up to Semester {semester}:\n")
    semesters = program_subjects.get(program)
    if semesters:
        data = []
        for sem in range(1, semester + 1):
            subjects = semesters.get(sem)
            if subjects:
                for subject in subjects:
                    data.append({"Semester": f"Semester {sem}", "Subject": subject['name'], "Credits": subject['credits'], "Description": subject['description']})
        if data:
            df = pd.DataFrame(data)
            print(df.to_string(index=False))
        else:
            print("No subjects found for the specified program and semester.")
    else:
        print("Program not found in the database.")



def add_program(program_subjects):
    """
    Adds a new program and its subjects to the program_subjects dictionary.
    
    Args:
    - program_subjects (dict): Dictionary containing existing subjects data.
    """
    program = input("Enter the name of the program you want to add: ").capitalize()
    program_subjects[program] = {}
    max_semester = int(input("Enter the maximum semester for this program: "))
    for sem in range(1, max_semester + 1):
        program_subjects[program][sem] = []
        while True:
            subject_name = input(f"Enter subject name for Semester {sem} (or type 'done' to finish): ")
            if subject_name.lower() == 'done':
                break
            subject_credits = int(input(f"Enter credits for {subject_name}: "))
            subject_description = input(f"Enter description for {subject_name}: ")
            program_subjects[program][sem].append({"name": subject_name, "credits": subject_credits, "description": subject_description})
    print("Program and subjects added successfully!")  

def save_subjects_to_csv(program_subjects):
    """
    Saves subjects from the program_subjects dictionary to a CSV file named subjects.csv.
    
    Args:
    - program_subjects (dict): Dictionary containing subjects data.
    """
    with open('subjects.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Program', 'Semester', 'Subject', 'Credits', 'Description'])
        for program, semesters in program_subjects.items():
            for semester, subjects in semesters.items():
                for subject in subjects:
                    writer.writerow([program, semester, subject['name'], subject['credits'], subject['description']])
    print("Subjects saved to subjects.csv file.")

def display_programs_with_semesters(program_subjects):
    """
    Displays available programs with the number of semesters in brackets.
    
    Args:
    - program_subjects (dict): Dictionary containing subjects data.
    """
    print("Available Programs:")
    for program, semesters in program_subjects.items():
        print(f"{program} ({len(semesters)} semesters)")

def search_subjects(program_subjects):
    """
    Enables searching within all program subjects, credits, and descriptions.
    
    Args:
    - program_subjects (dict): Dictionary containing subjects data.
    """
    search_query = input("Enter search query: ").lower()
    search_option = input("Would you like to search within subjects, credits, or descriptions? (s/c/d): ").lower()
    if search_option not in ['s', 'c', 'd']:
        print("Invalid search option.")
        return
    
    print("Search Results:\n")
    found = False
    for program, semesters in program_subjects.items():
        for semester, subjects in semesters.items():
            for subject in subjects:
                if search_query in subject['name'].lower() or search_query in subject['description'].lower() or (search_option == 'c' and search_query in str(subject['credits'])):
                    if not found:
                        print("Program | Semester | Subject | Credits | Description")
                        print("-" * 60)
                        found = True
                    print(f"{program:<7} | {semester:<9} | {subject['name']:<7} | {subject['credits']:<7} | {subject['description']}")
    if not found:
        print("No matching subjects found.")

        
        
def main():
    """
    Main function to interact with the program.
    """
    print("Welcome to the Dashboard!")
    program_subjects = get_subjects_from_csv()  # Load subjects data from CSV file
    
    while True:
        print("\nMenu:")
        print("1. View subjects from the program")
        print("2. Add a new program")
        print("3. Save subjects to CSV file")
        print("4. Search subjects")
        print("5. Exit")
        choice = input("Enter your choice (1/2/3/4/5): ")
        
        if choice == '1':
            display_programs_with_semesters(program_subjects)
            program = input("Enter the program you're interested in: ").capitalize()
            if program in program_subjects:
                get_subjects(program_subjects)
            else:
                print("Invalid program.")
        elif choice == '2':
            add_program(program_subjects)
        elif choice == '3':
            save_subjects_to_csv(program_subjects)
        elif choice == '4':
            search_subjects(program_subjects)
        elif choice == '5':    
            print("Exiting...")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
