import sys
import random
import datetime
import Validation_Functions as is_valid
from OTP import Saketh_Module
List_strong_Capitals_alphabets = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
List_strong_Small_alphabets = ["a","b","c","d","e","f","g","h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
List_strong_digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
List_strong_special_characters = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", "|", ";", ",", ".", "<" ,">?", "/"]
Registrationnumber =74108520963  
Admissionnumber = 7410
AdmissionInstructornumber = 8520
list_instructor = {}
list_of_students = {}
List_ofDeleted_Students = {}
List_ofDeleted_Instructors = {}
StrongPassword=[]
List_ofUnique_codes=[]
answer_validation_counter=0
Score=0
Discount_percentage=0

def Main_Menu_students(j):
                            print("1. Press 'V' to view your profile      |", end=" ")
                            print("2. Press 'C' for Courses               |", end=" ")
                            print("3. Press 'A' for Assements")
                            print("4. Press 'K' for Calender              |", end=" ")
                            print("5. Press 'R' for Course catalog        |", end=" ")
                            print("6. Press 'T' for Attendence")
                            print("7. Press 'E' for Course Evalution      |", end=" ")
                            print("8. Press 'F' for Fee Details           |", end=" ")
                            print("9. Press 'S' for Survey")
                            print("10. Press 'L' for Logout")
                            choice = input("                           Enter your choice: ")
                            if choice in ["V", "C", "A", "K", "R", "T", "E", "F", "S","L"]:
                                if choice == "V":
                                    j.profile()
                                elif choice == "C":
                                    j.Courses()
                                elif choice == "A":
                                    j.Assessments()
                                elif choice == "K":
                                    j.Calender()
                                elif choice == "R":
                                    j.Course_Catalogue()
                                elif choice == "T":
                                    j.Attendance()    
                                elif choice == "E":
                                    j.Course_Evalution()
                                elif choice == "F":
                                    j.Fee_Details()
                                elif choice == "S":
                                    j.Survey()
                                elif choice == "L":
                                    print("Logging out...")
                                    return 10

def Main_Menu_Instructors(j):
                            print("1. Press 'V' to view your profile      |", end=" ")
                            print("Student Profile Update: Press 'P' to the entering percentage of the students: ")
                            print("Attendance Update: Press 'A' to update the attendance of the students: ")
                            print("press 'L' to Logout")
                            instChoice=input()
                            if instChoice not in ["V", "P", "A","L"]:
                                print("Invalid choice. Please try again.")
                            if instChoice=="P":
                                j.percentageChange()  
                            elif instChoice=="A":
                                j.update_percentage()
                            elif instChoice=="V":
                                j.profile()  
                            elif instChoice=="L":
                                print("Logging out...")
                                return 10
                            else:
                                    print("Invalid input") 

def Main_Menu_Admin():
            print("Press 'D' to display all students and instructors")
            print("Press 'S' to search for a student or instructor by email")
            print("Press 'C' to change the talent enrichment program of a student")
            print("Press 'L' to change the Foreign language of a student")
            print("Press 'R' to remove a student or instructor by email")
            print("Press 'V' to drop out students or resigned instructors")
            print("Press 'RA' to readmit dropped out students or resigned instructors")
            print("Press 'P' to Logout")
            choice = input("Enter your choice: ")
            if choice not in ["D", "S", "C", "L", "R", "V", "RA", "P"]:
                print("Invalid choice. Please try again.")
            
            if choice == "D":
                print("Instructors:")
                for i in list_instructor.values():
                    print(f"Name: {i[2]}, Email: {i[0]}, Phone Number: {i[1]}, Age: {i[3]}, Status: {i[5]},") 
                print("Students:")
                for i in list_of_students.values():
                    print(f"Name: {i[2]}, Email: {i[0]}, Phone Number: {i[1]}, Age: {i[3]}, Status: {i[5]}, Availed Discount: {i[23]}, Unique Code: {i[24]}")
            
            elif choice == "S":
                print("email should be in lowercase and should end with @gmail.com and should not contain spaces and special characters except @ and . and should contain only one @ and should have at least one character before @ and should have at least one character between @ and . and should have at least 2 characters after .")
                email = input("Enter the email to search: ")
                is_valid.email_validation(email)
                found = False
                for j,i in list_instructor.items():
                    if i[0] == email:
                        print(f"Instructor Found: Name: {i[2]}, Email: {i[0]}, Phone Number: {i[1]}, Age: {i[3]}, Status: {i[5]},")
                        found = True
                        break
                if not found:
                    for j,i in list_of_students.items():
                        if i[0] == email:
                            print(f"Student Found: Name: {i[2]}, Email: {i[0]}, Phone Number: {i[1]}, Age: {i[3]}, Status: {i[5]},")
                            found = True
                            break
                if not found:
                    print("No instructor or student found with that email.")
            
            elif choice == "C":
                print("email should be in lowercase and should end with @gmail.com and should not contain spaces and special characters except @ and . and should contain only one @ and should have at least one character before @ and should have at least one character between @ and . and should have at least 2 characters after .")
                email = input("Enter the email of the student to change the talent enrichment program: ")
                is_valid.email_validation(email)
                found = False
                for j,i in list_of_students.items():
                    if i[0] == email:
                        print(f"Student Found: Name: {i[2]}, Email: {i[0]}, Current Talent Enrichment Program: {i[12]},")
                        new_program = input("Enter the new talent enrichment program (Sports, Music, Arts, Dance, Yoga, Musical Instrument): ")
                        if new_program.lower() not in ["sports", "singing", "arts", "dance", "yoga", "musical instrument"]:
                            print("Invalid talent enrichment program. No changes made.")
                        if new_program.lower() in ["sports", "music", "arts", "dance", "yoga", "musical instrument"]:
                            i[12] = new_program
                            j.TalentEnrichMentProgram = new_program
                            print(f"Talent Enrichment Program updated successfully for {i[2]}. New Program: {i[12]}")
                        else:
                            print("Invalid talent enrichment program. No changes made.")
                        found = True
                        break
                if not found:
                    print("No student found with that email.")
            
            elif choice == "L":
                print("email should be in lowercase and should end with @gmail.com and should not contain spaces and special characters except @ and . and should contain only one @ and should have at least one character before @ and should have at least one character between @ and . and should have at least 2 characters after .")
                email = input("Enter the email of the student to change the foreign language: ")
                is_valid.email_validation(email)
                found = False
                for j,i in list_of_students.items():
                    if i[0] == email:
                        print(f"Student Found: Name: {i[2]}, Email: {i[0]}, Current Foreign Language: {i[11]},")
                        new_language = input("Enter the new foreign language (French or German): ")
                        if new_language.lower() not in ["french", "german"]:
                            print("Invalid foreign language. No changes made.")
                        if new_language.lower() in ["french", "german"]:
                            i[11] = new_language
                            j.Language = new_language
                            print(f"Foreign Language updated successfully for {i[2]}. New Language: {i[11]}")
                        else:
                            print("Invalid foreign language. No changes made.")
                        found = True
                        break
                if not found:
                    print("No student found with that email.")
            
            elif choice == "R":
                print("email should be in lowercase and should end with @gmail.com and should not contain spaces and special characters except @ and . and should contain only one @ and should have at least one character before @ and should have at least one character between @ and . and should have at least 2 characters after .")
                email = input("Enter the email of the student or instructor to remove: ")
                is_valid.email_validation(email)
                found = False
                for j,i in list_instructor.items():
                    if i[0] == email:
                        List_ofDeleted_Instructors[j] = i
                        del list_instructor[j]
                        print(f"Instructor with email {email} has been removed.")
                        found = True
                        break
                if not found:
                    for j,i in list_of_students.items():
                        if i[0] == email:
                            List_ofDeleted_Students[j] = i
                            del list_of_students[j]
                            print(f"Student with email {email} has been removed.")
                            found = True
                            break
                if not found:
                    print("No instructor or student found with that email.")
            
            elif choice == "V":
                print("Deleted Instructors:")
                print(List_ofDeleted_Instructors)
                print("Deleted Students:")
                print(List_ofDeleted_Students)
            
            elif choice == "RA":
                print("email should be in lowercase and should end with @gmail.com and should not contain spaces and special characters except @ and . and should contain only one @ and should have at least one character before @ and should have at least one character between @ and . and should have at least 2 characters after .")
                email = input("Enter the email of the student or instructor to readmit: ")
                is_valid.email_validation(email)
                found = False
                for j,i in List_ofDeleted_Instructors.items():
                    if i[0] == email:
                        list_instructor[j] = i
                        del List_ofDeleted_Instructors[j]
                        print(f"Instructor with email {email} has been readmitted.")
                        found = True
                        break
                if not found:
                    for j,i in List_ofDeleted_Students.items():
                        if i[0] == email:
                            list_of_students[j] = i
                            del List_ofDeleted_Students[j]
                            print(f"Student with email {email} has been readmitted.")
                            found = True
                            break
                if not found:
                    print("No instructor or student found with that email.")
            elif choice == "P":
                print("Logging out...")
                return 10

def MCQ():
    maths_questions = [
        {"question":"Deck of cards we pic two cards one after one but we not replaced the first card what is the probability of the first card is Spade or Ace and the second card is Must be Queen Heart ? ",
                "options":["A)16/51*52","B)16/52*52","C)15/52*52","D)15/51*52"],
                "answer":"A"
        },

    {
        "question": "Evaluate: lim (x→0) (sin x - x cos x) / x^3",
        "options": ["A) 1/3", "B) 1/2", "C) 0", "D) -1/3"],
        "answer": "A"
    },

    {
        "question": "Number of solutions of |x^2 - 4x + 3| = 1 is:",
        "options": ["A) 2", "B) 3", "C) 4", "D) 5"],
        "answer": "C"
    },

    {
        "question": "If |A| = 5 for a 3x3 matrix, then |2A| equals:",
        "options": ["A) 10", "B) 20", "C) 40", "D) 8"],
        "answer": "C"
    },

    {
        "question": "If roots of x^2 - 4x + k = 0 are real and distinct, then:",
        "options": ["A) k < 4", "B) k > 4", "C) k = 4", "D) k ≤ 4"],
        "answer": "A"
    },

    {
        "question": "Integral from 0 to 1 of (3x^2 + 2x + 1) dx equals:",
        "options": ["A) 2", "B) 3", "C) 4", "D) 5"],
        "answer": "B"
    },

    {
        "question": "If z = 1 + i, then |z^3| equals:",
        "options": ["A) 2", "B) 4", "C) 8", "D) 16"],
        "answer": "C"
    },

    {
        "question": "Probability of getting exactly 2 heads in 3 tosses:",
        "options": ["A) 1/8", "B) 3/8", "C) 1/4", "D) 1/2"],
        "answer": "B"
    },

    {
        "question": "Derivative of ln(sin x) is:",
        "options": ["A) cot x", "B) tan x", "C) sec x", "D) csc x"],
        "answer": "A"
    },

    {
        "question": "If A.P. has first term 5 and common difference 3, sum of first 10 terms:",
        "options": ["A) 185", "B) 200", "C) 215", "D) 230"],
        "answer": "A"
    },

    {
        "question": "If vectors a and b are perpendicular, then:",
        "options": ["A) a·b = 0", "B) a×b = 0", "C) |a| = |b|", "D) None"],
        "answer": "A"
    }

    ]

    physics_questions = [

    {
        "question": "Range of a projectile is maximum at:",
        "options": ["A) 30°", "B) 45°", "C) 60°", "D) 90°"],
        "answer": "B"
    },

    {
        "question": "Work done in isothermal process is:",
        "options": ["A) 0", "B) nRT ln(V2/V1)", "C) nCvΔT", "D) PΔV"],
        "answer": "B"
    },

    {
        "question": "If kinetic energy doubles, momentum becomes:",
        "options": ["A) √2 times", "B) 2 times", "C) 4 times", "D) Same"],
        "answer": "A"
    },

    {
        "question": "Escape velocity of earth is approximately:",
        "options": ["A) 7.9 km/s", "B) 11.2 km/s", "C) 9.8 km/s", "D) 12.5 km/s"],
        "answer": "B"
    },

    {
        "question": "Unit of electric flux:",
        "options": ["A) Nm^2/C", "B) N/C", "C) C/N", "D) V/m"],
        "answer": "A"
    },

    {
        "question": "Magnetic field inside a long solenoid is:",
        "options": ["A) μ0nI", "B) μ0I", "C) nI", "D) I"],
        "answer": "A"
    },

    {
        "question": "Capacitance of parallel plate capacitor is:",
        "options": ["A) ε0A/d", "B) ε0d/A", "C) A/ε0d", "D) d/ε0A"],
        "answer": "A"
    },

    {
        "question": "If temperature doubles (in Kelvin), rms speed becomes:",
        "options": ["A) √2 times", "B) 2 times", "C) Same", "D) 4 times"],
        "answer": "A"
    },

    {
        "question": "Lens formula is:",
        "options": ["A) 1/f = 1/v - 1/u", "B) 1/f = 1/v + 1/u", "C) f = uv", "D) f = u + v"],
        "answer": "B"
    },

    {
        "question": "Energy stored in capacitor:",
        "options": ["A) 1/2 CV^2", "B) CV^2", "C) V^2/2C", "D) CV"],
        "answer": "A"
    }

    ]

    chemistry_questions = [

    {
        "question": "Rate law for first order reaction is:",
        "options": ["A) Rate = k[A]", "B) k[A]^2", "C) k", "D) k[A][B]"],
        "answer": "A"
    },

    {
        "question": "Bond order of O2 molecule:",
        "options": ["A) 1", "B) 2", "C) 3", "D) 2.5"],
        "answer": "B"
    },

    {
        "question": "Hybridization of BF3:",
        "options": ["A) sp", "B) sp2", "C) sp3", "D) dsp2"],
        "answer": "B"
    },

    {
        "question": "Strongest acid among hydrogen halides:",
        "options": ["A) HCl", "B) HBr", "C) HI", "D) HF"],
        "answer": "C"
    },

    {
        "question": "Mole fraction of solute equals:",
        "options": ["A) moles solute / total moles", "B) moles solvent / total", "C) mass ratio", "D) volume ratio"],
        "answer": "A"
    },

    {
        "question": "Half-life of first order reaction is:",
        "options": ["A) 0.693/k", "B) 1/k", "C) k", "D) k/0.693"],
        "answer": "A"
    },

    {
        "question": "Electronic configuration of Fe3+:",
        "options": ["A) [Ar]3d5", "B) [Ar]3d6", "C) [Ar]4s2", "D) [Ar]3d4"],
        "answer": "A"
    },

    {
        "question": "Number of sigma bonds in ethene:",
        "options": ["A) 4", "B) 5", "C) 6", "D) 7"],
        "answer": "B"
    },

    {
        "question": "Oxidation state of Cr in K2Cr2O7:",
        "options": ["A) +6", "B) +3", "C) +4", "D) +7"],
        "answer": "A"
    },

    {
        "question": "Ideal gas equation is:",
        "options": ["A) PV = nRT", "B) PV = RT", "C) PV = nR", "D) P = RT"],
        "answer": "A"
    }

    ]

    aptitude_questions = [

    {
        "question": "A and B can complete a work in 12 days and 18 days respectively. If they work together for 4 days and then B leaves, in how many more days will A complete the remaining work?",
        "options": ["A) 4", "B) 5", "C) 6", "D) 8"],
        "answer": "A"
    },

    {
        "question": "A sum becomes 4 times in 10 years at compound interest. What is the annual rate (approx)?",
        "options": ["A) 12%", "B) 14.8%", "C) 15%", "D) 18%"],
        "answer": "B"
    },

    {
        "question": "A train 180 m long moving at 72 km/h crosses a pole in:",
        "options": ["A) 6 s", "B) 8 s", "C) 9 s", "D) 10 s"],
        "answer": "C"
    },

    {
        "question": "If CP = ₹800 and SP = ₹920, what is the profit percentage?",
        "options": ["A) 10%", "B) 12%", "C) 15%", "D) 18%"],
        "answer": "C"
    },

    {
        "question": "Average of first 50 natural numbers is:",
        "options": ["A) 24.5", "B) 25", "C) 25.5", "D) 26"],
        "answer": "C"
    },

    {
        "question": "If 20% of x equals 40% of y, then x:y equals:",
        "options": ["A) 1:2", "B) 2:1", "C) 3:2", "D) 4:1"],
        "answer": "B"
    },

    {
        "question": "A boat goes 30 km downstream in 2 hours. If upstream speed is 10 km/h, speed of stream is:",
        "options": ["A) 2.5 km/h", "B) 5 km/h", "C) 7.5 km/h", "D) 10 km/h"],
        "answer": "B"
    },

    {
        "question": "Simple interest on ₹5000 at 8% per annum for 3 years is:",
        "options": ["A) 1000", "B) 1100", "C) 1200", "D) 1300"],
        "answer": "C"
    },

    {
        "question": "The ratio of ages of A and B is 4:5. After 6 years, the ratio becomes 5:6. Present age of A is:",
        "options": ["A) 18", "B) 24", "C) 30", "D) 36"],
        "answer": "B"
    },

    {
        "question": "A number is increased by 20% and then decreased by 20%. The net change is:",
        "options": ["A) 0%", "B) 4% decrease", "C) 4% increase", "D) 2% decrease"],
        "answer": "B"
    }

    ]

    reasoning_questions = [

    {
        "question": "Find the next term: 2, 6, 12, 20, 30, ?",
        "options": ["A) 40", "B) 42", "C) 44", "D) 46"],
        "answer": "B"
    },

    {
        "question": "If A + B means A is father of B, and A - B means A is sister of B, what is relation of P to R in P + Q - R?",
        "options": ["A) Aunt", "B) Mother", "C) Father", "D) Sister"],
        "answer": "A"
    },

    {
        "question": "Mirror image of 3:15 on a clock will be:",
        "options": ["A) 8:45", "B) 9:45", "C) 6:45", "D) 7:45"],
        "answer": "A"
    },

    {
        "question": "Coding: CAT = DBU, then DOG = ?",
        "options": ["A) EPH", "B) EOG", "C) FPH", "D) FOG"],
        "answer": "A"
    },

    {
        "question": "Find odd one out: 3, 5, 11, 14, 17",
        "options": ["A) 3", "B) 5", "C) 11", "D) 14"],
        "answer": "D"
    },

    {
        "question": "If South-East becomes North, North becomes West, then West becomes:",
        "options": ["A) South", "B) East", "C) North", "D) West"],
        "answer": "A"
    },

    {
        "question": "A man walks 5 km north, then 3 km east. How far is he from starting point?",
        "options": ["A) 5 km", "B) 8 km", "C) √34 km", "D) √25 km"],
        "answer": "C"
    },

    {
        "question": "Find next number: 1, 4, 9, 16, 25, ?",
        "options": ["A) 30", "B) 36", "C) 49", "D) 64"],
        "answer": "B"
    },

    {
        "question": "If in a code, LIGHT = MJHIU, then DARK = ?",
        "options": ["A) EBSL", "B) EBQL", "C) EBRL", "D) EBQK"],
        "answer": "B"
    },

    {
        "question": "Angle between hands of clock at 5:20 is:",
        "options": ["A) 40°", "B) 50°", "C) 60°", "D) 70°"],
        "answer": "B"
    }

    ]

    english_questions = [

    {
        "question": "Choose the correct sentence:",
        "options": ["A) Each of the players have arrived", "B) Each of the players has arrived", "C) Each of the players are arriving", "D) Each of the players were arriving"],
        "answer": "B"
    },

    {
        "question": "Synonym of 'Meticulous' is:",
        "options": ["A) Careless", "B) Careful", "C) Aggressive", "D) Lazy"],
        "answer": "B"
    },

    {
        "question": "Antonym of 'Benevolent' is:",
        "options": ["A) Kind", "B) Cruel", "C) Helpful", "D) Generous"],
        "answer": "B"
    },

    {
        "question": "Identify the error: 'Neither of the answers are correct.'",
        "options": ["A) Neither", "B) answers", "C) are", "D) No error"],
        "answer": "C"
    },

    {
        "question": "Choose correct preposition: He is proficient ___ mathematics.",
        "options": ["A) in", "B) on", "C) at", "D) for"],
        "answer": "A"
    },

    {
        "question": "Correct indirect speech: She said, 'I will come tomorrow.'",
        "options": ["A) She said she will come tomorrow", "B) She said she would come the next day", "C) She says she would come tomorrow", "D) She said she come tomorrow"],
        "answer": "B"
    },

    {
        "question": "Meaning of 'Ubiquitous':",
        "options": ["A) Rare", "B) Present everywhere", "C) Unknown", "D) Hidden"],
        "answer": "B"
    },

    {
        "question": "Choose correct conditional form: If I ___ rich, I would travel the world.",
        "options": ["A) am", "B) was", "C) were", "D) be"],
        "answer": "C"
    },

    {
        "question": "No sooner had he reached the station ___ the train left.",
        "options": ["A) than", "B) when", "C) then", "D) that"],
        "answer": "A"
    },

    {
        "question": "Choose correct spelling:",
        "options": ["A) Occassion", "B) Occasion", "C) Ocassion", "D) Occassionn"],
        "answer": "B"
    }

    ]

    def answer_validation(answer):
        global answer_validation_counter
        if answer not in ["A","B","C","D"]:
            print("Invalid input! Please enter A, B, C, or D.")
            answer_validation_counter += 1
            if answer_validation_counter <=3:
                answer = input("Your choice (A/B/C/D):").upper()
                answer_validation(answer)
            else:
                print("Too many invalid attempts. Moving to next question.")
        else:
            answer_validation_counter=0
            
    def Question(question_dict):
        global Score
        print(question_dict["question"])
        for i in question_dict["options"]:
            print(i)
        answer=input("Your choice (A/B/C/D):").upper()
        answer_validation(answer)
        if answer==question_dict["answer"]:
            print("Correct answer!")
            Score+=1
        else:

            print(f"Wrong answer! The correct answer is {question_dict['answer']}.")

    def Default_Question_Call():
        global Discount_percentage
        Random_Math_question_index=random.randint(0,len(maths_questions)-1)
        Random_Physics_question_index=random.randint(0,len(physics_questions)-1)
        Random_Chemistry_question_index=random.randint(0,len(chemistry_questions)-1)
        Random_Aptitude_question_index=random.randint(0,len(aptitude_questions)-1)
        Random_Reasoning_question_index=random.randint(0,len(reasoning_questions)-1)
        Random_English_question_index=random.randint(0,len(english_questions)-1)
        Question(maths_questions[Random_Math_question_index])
        Question(physics_questions[Random_Physics_question_index])
        Question(chemistry_questions[Random_Chemistry_question_index])
        Question(aptitude_questions[Random_Aptitude_question_index])
        Question(reasoning_questions[Random_Reasoning_question_index])
        Question(english_questions[Random_English_question_index])
        print(f"Your total Score :{Score} out of 6")
        if Score == 4:
            Discount_percentage=30
            print(f"You Availed  {Discount_percentage}% Discount of Your Acadamic Fee")
        
        elif Score==5:
            Discount_percentage=42
            print(f"You Availed  {Discount_percentage}% Discount of Your Acadamic Fee")
    
        elif Score==6:
            Discount_percentage=51
            print(f"You Availed  {Discount_percentage}% Discount of Your Acadamic Fee")
        else:
            print("Better luck next time..! you didn't availed any discount on your academic fee")
            Discount_percentage =0
        return Discount_percentage
    
    return Default_Question_Call()

def Suggest_strong_password():
            a=random.randint(0,len(List_strong_Capitals_alphabets)-1)
            a2=random.randint(0,len(List_strong_Capitals_alphabets)-1)
            b=random.randint(0,len(List_strong_Small_alphabets)-1)
            b2=random.randint(0,len(List_strong_Small_alphabets)-1)
            c=random.randint(0,len(List_strong_digits)-1)
            c2=random.randint(0,len(List_strong_digits)-1)
            d=random.randint(0,len(List_strong_special_characters)-1)
            d2=random.randint(0,len(List_strong_special_characters)-1)
            password=[]
            password.append(List_strong_Capitals_alphabets[a])
            password.append(List_strong_Capitals_alphabets[a2])
            password.append(List_strong_Small_alphabets[b])
            password.append(List_strong_Small_alphabets[b2])
            password.append(List_strong_digits[c])
            password.append(List_strong_digits[c2])
            password.append(List_strong_special_characters[d])
            password.append(List_strong_special_characters[d2])
            final=""
            j=random.randint(0,len(password)-1)
            final+=password[j]
            password.remove(password[j])
            k=random.randint(0,len(password)-1)
            final+=password[k]
            password.remove(password[k])
            l=random.randint(0,len(password)-1)
            final+=password[l]
            password.remove(password[l])
            m=random.randint(0,len(password)-1)
            final+=password[m]
            password.remove(password[m])
            n=random.randint(0,len(password)-1)
            final+=password[n]
            password.remove(password[n])
            o=random.randint(0,len(password)-1)
            final+=password[o]
            password.remove(password[o])
            p=random.randint(0,len(password)-1)
            final+=password[p]
            password.remove(password[p])
            q=password[0]
            final+=password[0]
            return final

def MCQ_Code():
            a=random.randint(0,len(List_strong_Capitals_alphabets)-1)
            b=random.randint(0,len(List_strong_Small_alphabets)-1)
            c=random.randint(0,len(List_strong_digits)-1)
            d=random.randint(0,len(List_strong_special_characters)-1)
            password=[]
            password.append(List_strong_Capitals_alphabets[a])
            password.append(List_strong_Small_alphabets[b])
            password.append(List_strong_digits[c])
            password.append(List_strong_special_characters[d])
            final=""
            j=random.randint(0,len(password)-1)
            final+=password[j]
            password.remove(password[j])
            k=random.randint(0,len(password)-1)
            final+=password[k]
            password.remove(password[k])
            l=random.randint(0,len(password)-1)
            final+=password[l]
            password.remove(password[l])
            final+=password[0]
            return final

def Instructor_account():
    print("email should be in lowercase and should end with @gmail.com \nshould not contain spaces and special characters except @ and .\nshould contain only one @ and should have at least one character before @ \nshould have at least one character between @ and .\nshould have at least 2 characters after .")
    email=Saketh_Module()
    is_valid.email_validation(email)
    if email in [i[0] for i in list_instructor.values()]  or email in [i[0] for i in list_of_students.values()] or email in [i[0] for i in List_ofDeleted_Instructors.values()] or email in [i[0] for i in List_ofDeleted_Students.values()]:
        return sys.exit("Email already exists.")
    print("Do you want a suggested strong password? (Y/N): ")
    choice = input().lower()
    if choice not in ["y","n"]:
        print("Invalid input! Please enter Y or N.")
        choice = input("Do you want a suggested strong password? (Y/N): ").lower()
    if choice == "y":
        password = Suggest_strong_password()
        if password in [i[4] for i in list_instructor.values() ] or password in [i[4] for i in list_of_students.values()] or password in [i[4] for i in List_ofDeleted_Instructors.values()] or password in [i[4] for i in List_ofDeleted_Students.values()] or password in StrongPassword:
            password = Suggest_strong_password()
        StrongPassword.append(password)
        print(f"Suggested strong password: {password}")
    elif choice == "n":
        password = input("Enter your password: ")
        is_valid.password_validation(password)
        if password in [i[4] for i in list_instructor.values() ] or password in [i[4] for i in list_of_students.values()] or password in [i[4] for i in List_ofDeleted_Instructors.values()] or password in [i[4] for i in List_ofDeleted_Students.values()] or password in StrongPassword:
            print("Password already exists. Please try again with a different password.")
            password = input("Enter your password: ")
            is_valid.password_validation(password)
            if password in [i[4] for i in list_instructor.values() ] or password in [i[4] for i in list_of_students.values()] or password in [i[4] for i in List_ofDeleted_Instructors.values()] or password in [i[4] for i in List_ofDeleted_Students.values()] or password in StrongPassword:
                print("Password already exists. Please try again with a different password.")
                password = input("Enter your password: ")
                is_valid.password_validation(password)
                if password in [i[4] for i in list_instructor.values() ] or password in [i[4] for i in list_of_students.values()] or password in [i[4] for i in List_ofDeleted_Instructors.values()] or password in [i[4] for i in List_ofDeleted_Students.values()] or password in StrongPassword:
                    print("Password already exists")
    phone_number = input("Enter your phone number: ")
    phone_number = is_valid.is_valid_phone(phone_number)
    name = input("Enter Your name with out dots : ")
    name = is_valid.is_valid_name(name)
    City = input("Enter your city: ")
    is_valid.cityvalidation(City)
    Gender= input("Enter your gender: ")
    is_valid.Gendervalidation(Gender)
    Date_of_birth = f" {input("Enter your Date of Birth \n DD: ")}/{input(" MM: ")}/{input(" YYYY: ")}".split()[-1]
    Date_of_birth = is_valid.is_validInstructor_date_of_birth(Date_of_birth)
    age=datetime.datetime.now().year - int(Date_of_birth.split('/')[-1])
    Language=input("Which Language that you teach in this ('python,web development,mathematics,aptitude,design and drafting,physics,chemistry','english',sports, singing, arts, dance, yoga, musical instrument'): ")
    is_valid.LanguageInstructorvalidation(Language)
    Blood_group = input("Enter your Blood group: ")
    is_valid.Blood_groupvalidation(Blood_group)
    Time=input("Enter Full_time or Part_time: ")
    is_valid.Timevalidation(Time)
    Date_of_Joining = f" {input('Enter your Date of Joining \n DD: ')}/{input(' MM: ')}/{input(' YYYY: ')}".split()[-1]
    Date_of_Joining = is_valid.is_validInstructor_date_of_birth(Date_of_Joining)
    global AdmissionInstructornumber
    AdmissionInstructornumber += 1
    print("Enter in this list of Religion ('hindu', 'muslim', 'christian', 'sikh', 'buddhist', 'jain', 'parsi', 'judaism', 'bahai', 'taoism', 'shintoism', 'confucianism', 'zoroastrianism', 'animism', 'atheism', 'agnosticism', 'other': ")
    Religion = input("Enter your Religion: ")
    is_valid.Religionvalidation(Religion)
    print("Enter in this list of Mother Tongue ('hindi', 'english', 'spanish', 'french', 'german', 'chinese', 'japanese', 'brazilian portuguese', 'italian', 'russian', 'mexican spanish', 'south african afrikaans', 'nigerian pidgin', 'egyptian arabic', 'argentinian spanish', 'saudi arabic', 'turkish', 'indonesian', 'pakistani urdu', 'bangladeshi bengali', 'vietnamese', 'philippine tagalog', 'malaysian malay', 'thai', 'iranian persian', 'iraqi arabic', 'afghan pashto, sudanese arabic, algerian arabic, moroccan arabic, tunisian arabic, libyan arabic': ")
    Mother_tongue = input("Enter your Mother Tongue: ")
    is_valid.Mother_tonguevalidation(Mother_tongue)
    print("Enter in this list of Nationality ('indian", "american", "british", "canadian", "australian", "french", "german", "chinese", "japanese", "brazilian", "italian", "spanish", "russian", "mexican", "south african", "nigerian", "egyptian", "argentinian", "saudi", "turkish", "indonesian", "pakistani", "bangladeshi", "vietnamese", "philippine", "malaysian", "thai", "iranian", "iraqi", "afghan", "sudanese", "algerian", "moroccan", "tunisian", "libyan'")
    Nationality = input("Enter your Nationality: ")
    is_valid.Nationalityvalidation(Nationality)
    Object = Instructor(email,phone_number, name, age, password,"Active",AdmissionInstructornumber,City,Gender,Date_of_birth,Language,Blood_group,Time,Date_of_Joining,Religion,Mother_tongue,Nationality) 
    list_instructor[Object] = [Object.email,Object.phone_number,Object.name,Object.age,Object.__password,Object.status,Object.AdmissionInstructornumber,Object.City,Object.Gender,Object.Date_of_birth,Object.Language,Object.Blood_group,Object.Time,Object.Date_of_joining,Object.Religion,Object.Mother_tongue,Object.Nationality]#self, email, name, age,password,status,Admissionnumber,City,Gender,Date_of_birth,Language,Blood_group
    Object.greet()

def Student_account():
        print("email should be in lowercase and should end with @gmail.com \nshould not contain spaces and special characters except @ and .\nshould contain only one @ and should have at least one character before @ \nshould have at least one character between @ and .\nshould have at least 2 characters after .")
        email=Saketh_Module()
        is_valid.email_validation(email)
        if email in [i[0] for i in list_of_students.values()] or email in [i[0] for i in list_instructor.values()] or email in [i[0] for i in List_ofDeleted_Instructors.values()] or email in [i[0] for i in List_ofDeleted_Students.values()]:
            return sys.exit("Email already exists. Please try again with a different email.")
        print("Do you want a suggested strong password? (Y/N): ")
        choice = input().lower()
        if choice not in ["y","n"]:
            print("Invalid input! Please enter Y or N.")
            choice = input("Do you want a suggested strong password? (Y/N): ").lower()
        if choice == "y":
            password = Suggest_strong_password()
            if password in [i[4] for i in list_instructor.values() ] or password in [i[4] for i in list_of_students.values()] or password in [i[4] for i in List_ofDeleted_Instructors.values()] or password in [i[4] for i in List_ofDeleted_Students.values()] or password in StrongPassword:
                password = Suggest_strong_password()
            StrongPassword.append(password)
            print(f"Suggested strong password: {password}")
        elif choice == "n":
            password = input("Enter your password: ")
            is_valid.password_validation(password)
            if password in [i[4] for i in list_instructor.values() ] or password in [i[4] for i in list_of_students.values()] or password in [i[4] for i in List_ofDeleted_Instructors.values()] or password in [i[4] for i in List_ofDeleted_Students.values()] or password in StrongPassword:
                print("Password already exists. Please try again with a different password.")
                password = input("Enter your password: ")
                is_valid.password_validation(password)
                if password in [i[4] for i in list_instructor.values() ] or password in [i[4] for i in list_of_students.values()] or password in [i[4] for i in List_ofDeleted_Instructors.values()] or password in [i[4] for i in List_ofDeleted_Students.values()] or password in StrongPassword:
                    print("Password already exists. Please try again with a different password.")
                    password = input("Enter your password: ")
                    is_valid.password_validation(password)
                    if password in [i[4] for i in list_instructor.values() ] or password in [i[4] for i in list_of_students.values()] or password in [i[4] for i in List_ofDeleted_Instructors.values()] or password in [i[4] for i in List_ofDeleted_Students.values()] or password in StrongPassword:
                        print("Password already exists")
        phone_number = input("Enter your phone number: ")
        phone_number = is_valid.is_valid_phone(phone_number)
        name = input("Enter Your name with out dots : ")
        name = is_valid.is_valid_name(name)
        City = input("Enter your city: ")
        is_valid.cityvalidation(City)
        Gender= input("Enter your gender: ")
        is_valid.Gendervalidation(Gender)
        Language = input("Enter Which language do you prefer French or Germany: ")
        is_valid.Languagevalidation(Language)
        TalentEnrichMentProgram = input("Which are the following do you Prefer :Sports, Singing, Arts, Dance, Yoga, Musical Instrument: ")
        is_valid.TalentEnrichMentProgramvalidation(TalentEnrichMentProgram)
        Blood_group = input("Enter your Blood group: ")
        is_valid.Blood_groupvalidation(Blood_group)
        Percentage = 0
        Date_of_birth = f" {input("Enter your Date of Birth \n DD: ")}/{input(" MM: ")}/{input(" YYYY: ")}".split()[-1]
        Date_of_birth = is_valid.is_valid_dob(Date_of_birth)
        age=datetime.datetime.now().year - int(Date_of_birth.split('/')[-1])
        Father_name = input("Enter your Father's name: ")
        Father_name=is_valid.is_valid_name(Father_name)
        Mother_name = input("Enter your Mother's name: ")
        Mother_name=is_valid.is_valid_name(Mother_name)
        Guardian_name = input("Enter your Guardian's name: ")
        Guardian_name=is_valid.is_valid_name(Guardian_name)
        Emergency_contact_number = input("Enter your Emergency contact number: ")
        Emergency_contact_number = is_valid.is_valid_phone(Emergency_contact_number)
        print("Enter in this list of Nationality ('indian", "american", "british", "canadian", "australian", "french", "german", "chinese", "japanese", "brazilian", "italian", "spanish", "russian", "mexican", "south african", "nigerian", "egyptian", "argentinian", "saudi", "turkish", "indonesian", "pakistani", "bangladeshi", "vietnamese", "philippine', 'malaysian', 'thai', 'iranian', 'iraqi', 'afghan', 'sudanese', 'algerian', 'moroccan', 'tunisian', 'libyan'")
        Nationality = input("Enter your Nationality: ")
        is_valid.Nationalityvalidation(Nationality)
        print("Enter in this list of Mother Tongue ('hindi', 'english', 'spanish', 'french', 'german', 'chinese', 'japanese', 'brazilian portuguese', 'italian', 'russian', 'mexican spanish', 'south african afrikaans', 'nigerian pidgin', 'egyptian arabic', 'argentinian spanish', 'saudi arabic', 'turkish', 'indonesian', 'pakistani urdu', 'bangladeshi bengali', 'vietnamese', 'philippine tagalog', 'malaysian malay', 'thai', 'iranian persian', 'iraqi arabic', 'afghan pashto, sudanese arabic, algerian arabic, moroccan arabic, tunisian arabic, libyan arabic': ")
        Mother_tongue = input("Enter your Mother tongue: ") 
        is_valid.Mother_tonguevalidation(Mother_tongue)
        print("Enter in this list of Religion ('hindu', 'muslim', 'christian', 'sikh', 'buddhist', 'jain', 'parsi', 'judaism', 'bahai', 'taoism', 'shintoism', 'confucianism', 'zoroastrianism', 'animism', 'atheism', 'agnosticism', 'other': ")
        Religion = input("Enter your Religion: ")
        is_valid.Religionvalidation(Religion)
        Parent_Mobile_number = input("Enter your Parent's Mobile number: ")
        Parent_Mobile_number = is_valid.is_valid_phone(Parent_Mobile_number)
        MCQDiscount=input("Do you want to take MCQ test for discount on your academic fee? (Y/N): ").lower()
        Availed_Dis=0
        Uniq_Code=0
        if MCQDiscount == "y":
            Availed_Dis=MCQ()
            global Score
            Score=0
            if Availed_Dis > 0:
                Uniq_Code=MCQ_Code()
                while Uniq_Code in List_ofUnique_codes:
                    Uniq_Code = MCQ_Code()
                List_ofUnique_codes.append(Uniq_Code)
                print(f"You Availed {Availed_Dis}% Discount on Your Academic Fee")
                print("Use this code at the time of payment to get your discount")
                print("Note: This code is unique and can be used only once. Please keep it safe.")
                print(f"Unique code for the discount: {Uniq_Code}")
        elif MCQDiscount == "n":
                pass
        global Registrationnumber
        Registrationnumber += 1
        global Admissionnumber
        Admissionnumber += 1
        Object = Saketh(email,phone_number, name, age, password,"Active",Registrationnumber,Admissionnumber,City,Gender,Date_of_birth,Language,TalentEnrichMentProgram,Percentage,Blood_group,Father_name,Mother_name,Guardian_name,Emergency_contact_number,Nationality,Mother_tongue,Religion,Parent_Mobile_number,Availed_Dis,Uniq_Code)
        Object.greet()
        list_of_students[Object] = [Object.email,Object.phone_number,Object.name,Object.age,Object._Saketh__password,Object.status,Object.Registrationnumber,Object.Admissionnumber,Object.City,Object.Gender,Object.Date_of_birth,Object.Language,Object.TalentEnrichMentProgram,Object.Percentage,Object.Blood_group,Object.Father_name,Object.Mother_name,Object.Guardian_name,Object.Emergency_contact_number,Object.Nationality,Object.Mother_tongue,Object.Religion,Object.Parent_Mobile_number,Object.Availed_Discount,Object.Unique_Code]#self, email, name, age,password,status,Registrationnumber,Admissionnumber

class Instructor:
    def __init__(self, email,phone_number, name, age,password,status,AdmissionInstructornumber,City,Gender,Date_of_birth,Language,Blood_group,Time,Date_of_joining,Religion,Mother_tongue,Nationality):
        self.email = email
        self.phone_number = phone_number
        self.name = name
        self.age = age
        self.__password = password
        self.status = status
        self.AdmissionInstructornumber=AdmissionInstructornumber
        self.City = City
        self.Gender = Gender
        self.Date_of_birth = Date_of_birth
        self.Language = Language
        self.Blood_group = Blood_group
        self.Time = Time
        self.Date_of_joining = Date_of_joining
        self.Religion = Religion
        self.Mother_tongue = Mother_tongue
        self.Nationality = Nationality
    def profile(self):
        print("Your Profile:")
        print("--------------------------------------------------")
        print("Basic Information:")
        print(f"Name: {self.name}                              " )
        if self.Gender.lower() == "male":
            print("Salutation: Mr")
        elif self.Gender.lower() == "female":
            print("Salutation: Ms")
        print(f"phone number: {self.phone_number}              " )
        print(f"Emplyee Type : {self.Time}                                " )
        print(f"Department: {self.Language}                                " )
        print(f"Employee ID: {self.AdmissionInstructornumber}                                " )
        print(f"Roles  : Faculty                             " )
        print(f"Date of Joining: {self.Date_of_joining}                                " )
        print(f"Status: {self.status}                              " )
        print("--------------------------------------------------")
        print("Personal Information:")
        print(f"Gender: {self.Gender}                          " )
        print(f"Date of Birth: {self.Date_of_birth}             " )
        print(f"Email: {self.email}                              " )
        print(f"Phone Number: {self.phone_number}              " )
        print(f"Blood Group: {self.Blood_group}                          " )
        print(f"Religion: {self.Religion}                          " )
        print(f"Mother Tongue: {self.Mother_tongue}                          " )
        print(f"Nationality: {self.Nationality}                          " )
        print(f"City: {self.City}                          " )
        print("--------------------------------------------------")
        print("Academic Qualifications:")

    def Assened_section(self):
        pass
    def Calender(self):
        pass
    def Survey(self):
        pass
    def greet(self):
        print(f"Hello, {self.name}! Welcome to the Instructor Portal.")

    def percentageChange(self):
        print("Student Data:")
        print("Student Name       Registration Number")
        for i in list_of_students.values():
           
            print(str(i[2])+"             "+str(i[6]))
            Registrationnumber=input("Enter the Registration number of the student whose percentage you want to update: ")
            if Registrationnumber.isdigit() and int(Registrationnumber) in [i[6] for i in list_of_students.values()]:
                pass
            if self.Language.lower() == "python":
                for j,i in list_of_students.items():
                    if i[6] == Registrationnumber:
                        newPercentage = input("Enter the new percentage for the student: ")
                        is_valid.PercentageVlidation(newPercentage)
                        j.Python_Status="Published"
                        j.pythonPercentage=int(newPercentage)
                        j.PythonDate=str(datetime.datetime.now())

            elif self.Language.lower() == "web development":
                for j,i in list_of_students.items():
                    if i[6] == Registrationnumber:
                        newPercentage = input("Enter the new percentage for the student: ")
                        is_valid.PercentageVlidation(newPercentage)
                        j.WebDevelopment_Status="Published"
                        j.webDevelopmentPercentage=int(newPercentage)
                        j.WebDevelopmentDate=str(datetime.datetime.now())

            elif self.Language.lower() == "design and drafting":
                for j,i in list_of_students.items():
                    if i[6] == Registrationnumber :
                        newPercentage = input("Enter the new percentage for the student: ")
                        is_valid.PercentageVlidation(newPercentage)
                        j.DesignDrafting_Status="Published"
                        j.DesignDraftingPercentage=int(newPercentage)
                        j.DesignDraftingDate=str(datetime.datetime.now())

            elif self.Language.lower() == "aptitude":
                for j,i in list_of_students.items():
                    if i[6] == Registrationnumber:
                        newPercentage = input("Enter the new percentage for the student: ")
                        is_valid.PercentageVlidation(newPercentage)
                        j.Aptitude_Status="Published"
                        j.AptitudePercentage=int(newPercentage)
                        j.AptitudeDate=str(datetime.datetime.now())

            elif self.Language.lower() == "mathematics":
                for j,i in list_of_students.items():
                    if i[6] == Registrationnumber:
                        newPercentage = input("Enter the new percentage for the student: ")
                        is_valid.PercentageVlidation(newPercentage)
                        j.Calculus_Status="Published"
                        j.CalculusPercentage=int(newPercentage)
                        j.CalculusDate=str(datetime.datetime.now())

            elif self.Language.lower() == "english":
                for j,i in list_of_students.items():
                    if i[6] == Registrationnumber:
                        newPercentage = input("Enter the new percentage for the student: ")
                        is_valid.PercentageVlidation(newPercentage)
                        j.English_Status="Published"
                        j.EnglishPercentage=int(newPercentage)
                        j.EnglishDate=str(datetime.datetime.now())

            elif self.Language.lower() == "physics":
                for j,i in list_of_students.items():
                    if i[6] == Registrationnumber:
                        newPercentage = input("Enter the new percentage for the student: ")
                        is_valid.PercentageVlidation(newPercentage)
                        j.Physics_Status="Published"
                        j.PhysicsPercentage=int(newPercentage)
                        j.PhysicsDate=str(datetime.datetime.now())

            elif self.Language.lower() == "chemistry":
                for j,i in list_of_students.items():
                    if i[6] == Registrationnumber:
                        newPercentage = input("Enter the new percentage for the student: ")
                        is_valid.PercentageVlidation(newPercentage)
                        j.Chemistry_Status="Published"
                        j.ChemistryPercentage=int(newPercentage)
                        j.ChemistryDate=str(datetime.datetime.now())

            elif self.Language.lower() == "germany":
                for j,i in list_of_students.items():
                    if i[6] == Registrationnumber:
                        newPercentage = input("Enter the new percentage for the student: ")
                        is_valid.PercentageVlidation(newPercentage)
                        j.German_Status="Published"
                        j.GermanPercentage=int(newPercentage)
                        j.GermanDate=str(datetime.datetime.now())

            elif self.Language.lower() == "french":
                for j,i in list_of_students.items():
                    if i[6] == Registrationnumber:
                        newPercentage = input("Enter the new percentage for the student: ")
                        is_valid.PercentageVlidation(newPercentage)
                        j.French_Status="Published"
                        j.FrenchPercentage=int(newPercentage)
                        j.FrenchDate=str(datetime.datetime.now())
                        
    def update_percentage(self):
        if self.Language.lower() == "python":
            for j,i in list_of_students.items():
                print(str(i[2])+"             "+str(i[6]))
                Present_or_Absent = input("Is the student present or absent (Y/N): ")
                if Present_or_Absent.lower() == "y":
                    j.PythonAttendance += 1
                    j.PythonClasses += 1    
                    j.TotalAttendance += 1
                    j.TotalClasses += 1
                elif Present_or_Absent.lower() == "n":
                    j.PythonClasses += 1
                    j.TotalClasses += 1
                else:
                    print("Invalid input! Please enter Y or N.")
                    Present_or_Absent = input("Is the student present or absent (Y/N): ")
                    if Present_or_Absent.lower() == "y":
                        j.PythonAttendance += 1
                        j.PythonClasses += 1    
                        j.TotalAttendance += 1
                        j.TotalClasses += 1
                    elif Present_or_Absent.lower() == "n":
                        j.PythonClasses += 1
                        j.TotalClasses += 1
        elif self.Language.lower() == "web development":
            for j,i in list_of_students.items():
                print(str(i[2])+"             "+str(i[6]))
                Present_or_Absent = input("Is the student present or absent (Y/N): ")
                if Present_or_Absent.lower() == "y":
                    j.WebDevelopmentAttendance += 1
                    j.WebDevelopmentClasses += 1
                    j.TotalAttendance += 1
                    j.TotalClasses += 1
                elif Present_or_Absent.lower() == "n":
                    j.WebDevelopmentClasses += 1
                    j.TotalClasses += 1
                else:
                    print("Invalid input! Please enter Y or N.")
                    Present_or_Absent = input("Is the student present or absent (Y/N): ")
                    if Present_or_Absent.lower() == "y":
                        j.WebDevelopmentAttendance += 1
                        j.WebDevelopmentClasses += 1
                        j.TotalAttendance += 1
                        j.TotalClasses += 1
                    elif Present_or_Absent.lower() == "n":
                        j.WebDevelopmentClasses += 1
                        j.TotalClasses += 1
        elif self.Language.lower() == "french":
            for j,i in list_of_students.items():
                print(str(i[2])+"             "+str(i[6]))
                Present_or_Absent = input("Is the student present or absent (Y/N): ")
                if Present_or_Absent.lower() == "y":
                    j.FrenchAttendance += 1
                    j.FrenchClasses += 1
                    j.TotalAttendance += 1
                    j.TotalClasses += 1 
                elif Present_or_Absent.lower() == "n":
                    j.FrenchClasses += 1
                    j.TotalClasses += 1
                else:
                    print("Invalid input! Please enter Y or N.")
                    Present_or_Absent = input("Is the student present or absent (Y/N): ")
                    if Present_or_Absent.lower() == "y":
                        j.FrenchAttendance += 1
                        j.FrenchClasses += 1
                        j.TotalAttendance += 1
                        j.TotalClasses += 1 
                    elif Present_or_Absent.lower() == "n":
                        j.FrenchClasses += 1
                        j.TotalClasses += 1
        elif self.Language.lower() == "design and drafting":
            for j,i in list_of_students.items():
                print(str(i[2])+"             "+str(i[6]))
                Present_or_Absent = input("Is the student present or absent (Y/N): ")
                if Present_or_Absent.lower() == "y":
                    j.DesignDraftingAttendance += 1
                    j.DesignDraftingClasses += 1
                    j.TotalAttendance += 1
                    j.TotalClasses += 1
                elif Present_or_Absent.lower() == "n":
                    j.DesignDraftingClasses += 1
                    j.TotalClasses += 1
                else:
                    print("Invalid input! Please enter Y or N.")
                    Present_or_Absent = input("Is the student present or absent (Y/N): ")
                    if Present_or_Absent.lower() == "y":
                        j.DesignDraftingAttendance += 1
                        j.DesignDraftingClasses += 1
                        j.TotalAttendance += 1
                        j.TotalClasses += 1
                    elif Present_or_Absent.lower() == "n":
                        j.DesignDraftingClasses += 1
                        j.TotalClasses += 1
        elif self.Language.lower() == "aptitude":
            for j,i in list_of_students.items():
                print(str(i[2])+"             "+str(i[6]))
                Present_or_Absent = input("Is the student present or absent (Y/N): ")
                if Present_or_Absent.lower() == "y":
                    j.AptitudeAttendance += 1
                    j.AptitudeClasses += 1
                    j.TotalAttendance += 1
                    j.TotalClasses += 1
                elif Present_or_Absent.lower() == "n":
                    j.AptitudeClasses += 1
                    j.TotalClasses += 1
                else:
                    print("Invalid input! Please enter Y or N.")
                    Present_or_Absent = input("Is the student present or absent (Y/N): ")
                    if Present_or_Absent.lower() == "y":
                        j.AptitudeAttendance += 1
                        j.AptitudeClasses += 1
                        j.TotalAttendance += 1
                        j.TotalClasses += 1
                    elif Present_or_Absent.lower() == "n":
                        j.AptitudeClasses += 1
                        j.TotalClasses += 1
        elif self.Language.lower() == "mathematics":
            for j,i in list_of_students.items():
                print(str(i[2])+"             "+str(i[6]))
                Present_or_Absent = input("Is the student present or absent (Y/N): ")
                if Present_or_Absent.lower() == "y":
                    j.CalculusAttendance += 1
                    j.CalculusClasses += 1
                    j.TotalAttendance += 1
                    j.TotalClasses += 1
                elif Present_or_Absent.lower() == "n":
                    j.CalculusClasses += 1
                    j.TotalClasses += 1
                else:
                    print("Invalid input! Please enter Y or N.")
                    Present_or_Absent = input("Is the student present or absent (Y/N): ")
                    if Present_or_Absent.lower() == "y":
                        j.CalculusAttendance += 1
                        j.CalculusClasses += 1
                        j.TotalAttendance += 1
                        j.TotalClasses += 1
                    elif Present_or_Absent.lower() == "n":
                        j.CalculusClasses += 1
                        j.TotalClasses += 1
        elif self.Language.lower() == "english":
            for j,i in list_of_students.items():
                print(str(i[2])+"             "+str(i[6]))
                Present_or_Absent = input("Is the student present or absent (Y/N): ")
                if Present_or_Absent.lower() == "y":
                    j.EnglishAttendance += 1
                    j.EnglishClasses += 1
                    j.TotalAttendance += 1
                    j.TotalClasses += 1
                elif Present_or_Absent.lower() == "n":
                    j.EnglishClasses += 1
                    j.TotalClasses += 1
                else:
                    print("Invalid input! Please enter Y or N.")
                    Present_or_Absent = input("Is the student present or absent (Y/N): ")
                    if Present_or_Absent.lower() == "y":
                        j.EnglishAttendance += 1
                        j.EnglishClasses += 1
                        j.TotalAttendance += 1
                        j.TotalClasses += 1
                    elif Present_or_Absent.lower() == "n":
                        j.EnglishClasses += 1
                        j.TotalClasses += 1
        elif self.Language.lower() == "physics":
            for j,i in list_of_students.items():
                print(str(i[2])+"             "+str(i[6]))
                Present_or_Absent = input("Is the student present or absent (Y/N): ")
                if Present_or_Absent.lower() == "y":
                    j.PhysicsAttendance += 1
                    j.PhysicsClasses += 1
                    j.TotalAttendance += 1
                    j.TotalClasses += 1
                elif Present_or_Absent.lower() == "n":
                    j.PhysicsClasses += 1
                    j.TotalClasses += 1
                else:
                    print("Invalid input! Please enter Y or N.")
                    Present_or_Absent = input("Is the student present or absent (Y/N): ")
                    if Present_or_Absent.lower() == "y":
                        j.PhysicsAttendance += 1
                        j.PhysicsClasses += 1
                        j.TotalAttendance += 1
                        j.TotalClasses += 1
                    elif Present_or_Absent.lower() == "n":
                        j.PhysicsClasses += 1
                        j.TotalClasses += 1
        elif self.Language.lower() == "chemistry":
            for j,i in list_of_students.items():
                print(str(i[2])+"             "+str(i[6]))
                Present_or_Absent = input("Is the student present or absent (Y/N): ")
                if Present_or_Absent.lower() == "y":
                    j.ChemistryAttendance += 1
                    j.ChemistryClasses += 1
                    j.TotalAttendance += 1
                elif Present_or_Absent.lower() == "n":
                    j.ChemistryClasses += 1
                    j.TotalClasses += 1
                else:
                    print("Invalid input! Please enter Y or N.")
                    Present_or_Absent = input("Is the student present or absent (Y/N): ")
                    if Present_or_Absent.lower() == "y":
                        j.ChemistryAttendance += 1
                        j.ChemistryClasses += 1
                        j.TotalAttendance += 1
                    elif Present_or_Absent.lower() == "n":
                        j.ChemistryClasses += 1
                        j.TotalClasses += 1
        elif self.Language.lower() == "germany":
            for j,i in list_of_students.items():
                print(str(i[2])+"             "+str(i[6]))
                Present_or_Absent = input("Is the student present or absent (Y/N): ")
                if Present_or_Absent.lower() == "y":
                    j.GermanAttendance += 1
                    j.GermanClasses += 1
                    j.TotalAttendance += 1
                    j.TotalClasses += 1
                elif Present_or_Absent.lower() == "n":
                    j.GermanClasses += 1
                    j.TotalClasses += 1
                else:
                    print("Invalid input! Please enter Y or N.")
                    Present_or_Absent = input("Is the student present or absent (Y/N): ")
                    if Present_or_Absent.lower() == "y":
                        j.GermanAttendance += 1
                        j.GermanClasses += 1
                        j.TotalAttendance += 1
                        j.TotalClasses += 1
                    elif Present_or_Absent.lower() == "n":
                        j.GermanClasses += 1
                        j.TotalClasses += 1
        elif self.Language.lower() == "sports":
            for j,i in list_of_students.items():
                print(str(i[2])+"             "+str(i[6]))
                Present_or_Absent = input("Is the student present or absent (Y/N): ")
                if Present_or_Absent.lower() == "y":
                    j.SportsAttendance += 1
                    j.SportsClasses += 1
                    j.TotalAttendance += 1
                    j.TotalClasses += 1
                elif Present_or_Absent.lower() == "n":
                    j.SportsClasses += 1
                    j.TotalClasses += 1
                else:
                    print("Invalid input! Please enter Y or N.")
                    Present_or_Absent = input("Is the student present or absent (Y/N): ")
                    if Present_or_Absent.lower() == "y":
                        j.SportsAttendance += 1
                        j.SportsClasses += 1
                        j.TotalAttendance += 1
                        j.TotalClasses += 1
                    elif Present_or_Absent.lower() == "n":
                        j.SportsClasses += 1
                        j.TotalClasses += 1
        elif self.Language.lower() == "singing":
            for j,i in list_of_students.items():
                print(str(i[2])+"             "+str(i[6]))
                Present_or_Absent = input("Is the student present or absent (Y/N): ")
                if Present_or_Absent.lower() == "y":
                    j.SingingAttendance += 1
                    j.SingingClasses += 1
                    j.TotalAttendance += 1
                    j.TotalClasses += 1
                elif Present_or_Absent.lower() == "n":
                    j.SingingClasses += 1
                    j.TotalClasses += 1
                else:
                    print("Invalid input! Please enter Y or N.")
                    Present_or_Absent = input("Is the student present or absent (Y/N): ")
                    if Present_or_Absent.lower() == "y":
                        j.SingingAttendance += 1
                        j.SingingClasses += 1
                        j.TotalAttendance += 1
                        j.TotalClasses += 1
                    elif Present_or_Absent.lower() == "n":
                        j.SingingClasses += 1
                        j.TotalClasses += 1
        elif self.Language.lower() == "arts":
            for j,i in list_of_students.items():
                print(str(i[2])+"             "+str(i[6]))
                Present_or_Absent = input("Is the student present or absent (Y/N): ")
                if Present_or_Absent.lower() == "y":
                    j.ArtsAttendance += 1
                    j.ArtsClasses += 1
                    j.TotalAttendance += 1
                    j.TotalClasses += 1
                elif Present_or_Absent.lower() == "n":
                    j.ArtsClasses += 1
                    j.TotalClasses += 1
                else:
                    print("Invalid input! Please enter Y or N.")
                    Present_or_Absent = input("Is the student present or absent (Y/N): ")
                    if Present_or_Absent.lower() == "y":
                        j.ArtsAttendance += 1
                        j.ArtsClasses += 1
                        j.TotalAttendance += 1
                        j.TotalClasses += 1
                    elif Present_or_Absent.lower() == "n":
                        j.ArtsClasses += 1
                        j.TotalClasses += 1
        elif self.Language.lower() == "dance":
            for j,i in list_of_students.items():
                print(str(i[2])+"             "+str(i[6]))
                Present_or_Absent = input("Is the student present or absent (Y/N): ")
                if Present_or_Absent.lower() == "y":
                    j.DanceAttendance += 1
                    j.DanceClasses += 1
                    j.TotalAttendance += 1
                    j.TotalClasses += 1
                elif Present_or_Absent.lower() == "n":
                    j.DanceClasses += 1
                    j.TotalClasses += 1
                else:
                    print("Invalid input! Please enter Y or N.")
                    Present_or_Absent = input("Is the student present or absent (Y/N): ")
                    if Present_or_Absent.lower() == "y":
                        j.DanceAttendance += 1
                        j.DanceClasses += 1
                        j.TotalAttendance += 1
                        j.TotalClasses += 1
                    elif Present_or_Absent.lower() == "n":
                        j.DanceClasses += 1
                        j.TotalClasses += 1
        elif self.Language.lower() == "yoga":
            for j,i in list_of_students.items():
                print(str(i[2])+"             "+str(i[6]))
                Present_or_Absent = input("Is the student present or absent (Y/N): ")
                if Present_or_Absent.lower() == "y":
                    j.YogaAttendance += 1
                    j.YogaClasses += 1
                    j.TotalAttendance += 1
                    j.TotalClasses += 1
                elif Present_or_Absent.lower() == "n":
                    j.YogaClasses += 1
                    j.TotalClasses += 1
                else:
                    print("Invalid input! Please enter Y or N.")
                    Present_or_Absent = input("Is the student present or absent (Y/N): ")
                    if Present_or_Absent.lower() == "y":
                        j.YogaAttendance += 1
                        j.YogaClasses += 1
                        j.TotalAttendance += 1
                        j.TotalClasses += 1
                    elif Present_or_Absent.lower() == "n":
                        j.YogaClasses += 1
                        j.TotalClasses += 1
        elif self.Language.lower() == "musical instrument":
            for j,i in list_of_students.items():
                print(str(i[2])+"             "+str(i[6]))
                Present_or_Absent = input("Is the student present or absent (Y/N): ")
                if Present_or_Absent.lower() == "y":
                    j.MusicalInstrumentAttendance += 1
                    j.MusicalInstrumentClasses += 1
                    j.TotalAttendance += 1
                    j.TotalClasses += 1
                elif Present_or_Absent.lower() == "n":
                    j.MusicalInstrumentClasses += 1
                    j.TotalClasses += 1
                else:
                    print("Invalid input! Please enter Y or N.")
                    Present_or_Absent = input("Is the student present or absent (Y/N): ")
                    if Present_or_Absent.lower() == "y":
                        j.MusicalInstrumentAttendance += 1
                        j.MusicalInstrumentClasses += 1
                        j.TotalAttendance += 1
                        j.TotalClasses += 1
                    elif Present_or_Absent.lower() == "n":
                        j.MusicalInstrumentClasses += 1
                        j.TotalClasses += 1

class Saketh:   

    def __init__(self, email,phone_number, name, age,password,status,Registrationnumber,Admissionnumber,City,Gender,Date_of_birth,Language,TalentEnrichMentProgram,Percentage,Blood_group,Father_name,Mother_name,Guardian_name,Emergency_contact_number,Nationality,Mother_tongue,Religion,Parent_Mobile_number,Availed_Discount,Unique_Code):
        self.Availed_Discount=Availed_Discount
        self.Unique_Code=Unique_Code
        self.PythonAttendance=0
        self.PythonClasses=0
        self.WebDevelopmentAttendance=0
        self.WebDevelopmentClasses=0
        self.CalculusAttendance=0
        self.CalculusClasses=0
        self.DesignDraftingAttendance=0
        self.DesignDraftingClasses=0
        self.AptitudeAttendance=0
        self.AptitudeClasses=0
        self.EnglishAttendance=0
        self.EnglishClasses=0
        self.FrenchAttendance=0
        self.FrenchClasses=0
        self.GermanAttendance=0
        self.GermanClasses=0
        self.PhysicsAttendance=0
        self.PhysicsClasses=0
        self.ChemistryAttendance=0
        self.ChemistryClasses=0
        self.SportsAttendance=0
        self.SportsClasses=0
        self.SingingAttendance=0
        self.SingingClasses=0
        self.ArtsAttendance=0
        self.ArtsClasses=0
        self.DanceAttendance=0
        self.DanceClasses=0
        self.YogaAttendance=0
        self.YogaClasses=0
        self.MusicalInstrumentAttendance=0
        self.MusicalInstrumentClasses=0
        self.TotalAttendance=0
        self.TotalClasses=0
        self.email = email
        self.phone_number = phone_number
        self.name = name
        self.age = age
        self.__password = password
        self.status = status
        self.Registrationnumber = Registrationnumber
        self.Admissionnumber = Admissionnumber
        self.City = City
        self.Gender = Gender
        self.Date_of_birth = Date_of_birth
        self.Language = Language
        self.TalentEnrichMentProgram = TalentEnrichMentProgram
        self.Percentage = int(Percentage)
        self.Blood_group = Blood_group
        self.Father_name = Father_name
        self.Mother_name = Mother_name
        self.Guardian_name = Guardian_name
        self.Emergency_contact_number = Emergency_contact_number
        self.Nationality = Nationality
        self.Mother_tongue = Mother_tongue
        self.Religion = Religion
        self.Parent_Mobile_number = Parent_Mobile_number
        self.pythonPercentage=0
        self.webDevelopmentPercentage=0
        self.CalculusPercentage=0
        self.DesignDraftingPercentage=0
        self.AptitudePercentage=0
        self.EnglishPercentage=0
        self.English_Status="Not Published" 
        self.Python_Status="Not Published"
        self.WebDevelopment_Status="Not Published"
        self.Calculus_Status="Not Published"
        self.DesignDrafting_Status="Not Published"
        self.Aptitude_Status="Not Published"
        self.PhysicsPercentage=0
        self.Physics_Status="Not Published"
        self.ChemistryPercentage=0
        self.Chemistry_Status="Not Published"
        self.SportsPercentage=0
        self.Sports_Status="Not Published"
        self.SingingPercentage=0
        self.Singing_Status="Not Published" 
        self.ArtsPercentage=0
        self.Arts_Status="Not Published"
        self.DancePercentage=0
        self.Dance_Status="Not Published"
        self.YogaPercentage=0
        self.Yoga_Status="Not Published"
        self.MusicalInstrumentPercentage=0
        self.MusicalInstrument_Status="Not Published"
        self.PythonDate=""
        self.WebDevelopmentDate=""
        self.CalculusDate=""
        self.DesignDraftingDate=""
        self.AptitudeDate=""
        self.EnglishDate=""
        self.FrenchDate=""
        self.GermanDate=""
        self.PhysicsDate=""
        self.ChemistryDate=""
        if self.Language.lower() == "french":
            self.FrenchPercentage=0
            self.French_Status="Not Published"
        else:
            self.GermanPercentage=0
            self.German_Status="Not Published"

    def profile(self):
        print("Your Profile:")
        print("--------------------------------------------------")
        print("Detalils: ")
        print(f"Status: {self.status}                          " )
        print(f"Registration Number: {self.Registrationnumber} ")
        print(f"Admission Number: {self.Admissionnumber}       ")
        print(f"Name: {self.name}                              " )
        print("Batch: 2025-2029                                ")
        print("Course: B.Tech Computer Science and Engineering     ")
        if self.Gender.lower() == "male":
            print("Salutation: Mr")
        elif self.Gender.lower() == "female":
            print("Salutation: Ms")
        print("Adress :#city is "+self.City)
        print("--------------------------------------------------")
        print("Personal Information:")
        print(f"Gender: {self.Gender}                          " )
        print(f"Email: {self.email}                            " )
        print(f"Father's Name: {self.Father_name}              " )
        print(f"Mother's Name: {self.Mother_name}              " )
        print(f"Guardian's Name: {self.Guardian_name}          " )
        print(f"Date of Birth: {self.Date_of_birth}            " )
        print(f"My Phone Number: {self.phone_number}              " )
        print(f"Nationality: {self.Nationality}                          " )
        print(f"Blood Group: {self.Blood_group}                          " )
        print(f"Mother Tongue: {self.Mother_tongue}                          " )
        print(f"Parent's Mobile Number: {self.Parent_Mobile_number}                          " )
        print(f"RELIGION: {self.Religion}                          " )
        print(f"Emergency Contact Number: {self.Emergency_contact_number}                          " )
        print("Achevements:")
        print("1. Completed Python Basics Course")
        print("2. Built a Simple Web Application")
        print("3. Participated in a Coding Competition")

    def Courses(self):
        print("Your Courses:")
        print("--------------------------------------------------")
        print("1. Python Programming")
        print("2. Quantum Aptitude")
        print("3. Web Development")
        print("4. Cambrige English")
        print("5. Calculus and Differential Equations")
        print("6. Design and Drafting")
        print(f"7. Language: {self.Language}")
        print(f"8. Talent Enrichment Program: {self.TalentEnrichMentProgram}")

    def Assessments(self):
        print("Your Assessments:")
        print("--------------------------------------------------")
        print(f"Lab Participation   Problem Solving with Python            Feb 20 2026 (02.20AM)[Start Date]   Feb 27 2026 (11.59PM)[End Date]   {self.Python_Status}[Status]          [Results] {self.pythonPercentage}         {self.PythonDate }")
        print(f"Lab Participation   Web Development                        Feb 05 2026 (02.20AM)[Start Date]   Feb 15 2026 (11.59PM)[End Date]   {self.WebDevelopment_Status}[Status]  [Results] {self.webDevelopmentPercentage}       {self.WebDevelopmentDate}")
        print(f"Lab Participation   {self.Language}                                Feb 10 2026 (02.20AM)[Start Date]   Feb 17 2026 (11.59PM)[End Date]   {self.French_Status if self.Language.lower() == 'french' else self.German_Status}[Status]          [Results] {self.FrenchPercentage if self.Language.lower() == 'french' else self.GermanPercentage}        {self.FrenchDate if self.Language.lower() == 'french' else self.GermanDate} ")
        print(f"Lab Participation   Calculus and Differential Equations    Feb 20 2026 (02.20AM)[Start Date]   Feb 27 2026 (11.59PM)[End Date]   {self.Calculus_Status}[Status]        [Results] {self.CalculusPercentage}         {self.CalculusDate} ")    
        print(f"Lab Participation   Design and Drafting                    Feb 05 2026 (02.20AM)[Start Date]   Feb 15 2026 (11.59PM)[End Date]   {self.DesignDrafting_Status}[Status]  [Results] {self.DesignDraftingPercentage}      {self.DesignDraftingDate} ")
        print(f"Lab Participation   Quantum Aptitude                       Feb 10 2026 (02.20AM)[Start Date]   Feb 17 2026 (11.59PM)[End Date]   {self.Aptitude_Status}[Status]        [Results] {self.AptitudePercentage}          {self.AptitudeDate} ")
        print(f"Lab Participation   Physics                       Feb 10 2026 (02.20AM)[Start Date]   Feb 17 2026 (11.59PM)[End Date]   {self.Physics_Status}[Status]          [Results] {self.PhysicsPercentage}          {self.PhysicsDate} ")
        print(f"Lab Participation   Chemistry                       Feb 10 2026 (02.20AM)[Start Date]   Feb 17 2026 (11.59PM)[End Date]   {self.Chemistry_Status}[Status]          [Results] {self.ChemistryPercentage}          {self.ChemistryDate} ")
        print(f"Lab Participation   Cambrige English                       Feb 10 2026 (02.20AM)[Start Date]   Feb 17 2026 (11.59PM)[End Date]   {self.English_Status}[Status]          [Results] {self.EnglishPercentage}          {self.EnglishDate} ")

    def Calender(self):
        print("Your Calendar:")
        print("--------------------------------------------------")
        print("1. Python Programming: Every Monday and Wednesday at 10:00 AM")
        print("2. Web Development: Every Tuesday and Thursday at 2:00 PM")
        print(f"3. {self.Language}: Every Friday at 11:00 AM")
        print("4. Calculus and Differential Equations: Every Monday and Wednesday at 3:00 PM")
        print("5. Design and Drafting: Every Tuesday and Thursday at 4:00 PM")
        print("6. Quantum Aptitude: Every Friday at 2:00 PM")
        print("7. Cambrige English: Every Monday and Wednesday at 1:00 PM")

    def Course_Catalogue(self):
        pass
    
    def Attendance(self):
        print("Your Attendance:")
        print("--------------------------------------------------")
        print(f"Total Present Classes:                      {self.TotalAttendance}              Total Classes: {self.TotalClasses}              Total Attendance Percentage: {(self.TotalAttendance/self.TotalClasses*100) if self.TotalClasses > 0 else 0}%")
        print(f"Python Programming Present Classes:         {self.PythonAttendance}             Total Classes: {self.PythonClasses}             Attendance Percentage: {(self.PythonAttendance/self.PythonClasses*100) if self.PythonClasses > 0 else 0}%")
        print(f"Web Development Present Classes:            {self.WebDevelopmentAttendance}     Total Classes: {self.WebDevelopmentClasses}     Attendance Percentage: {(self.WebDevelopmentAttendance/self.WebDevelopmentClasses*100) if self.WebDevelopmentClasses > 0 else 0}%")
        print(f"Mathematics Present Classes:                {self.CalculusAttendance}           Total Classes: {self.CalculusClasses}           Attendance Percentage: {(self.CalculusAttendance/self.CalculusClasses*100) if self.CalculusClasses > 0 else 0}%")
        print(f"Design and Drafting Present Classes:        {self.DesignDraftingAttendance}     Total Classes: {self.DesignDraftingClasses}     Attendance Percentage: {(self.DesignDraftingAttendance/self.DesignDraftingClasses*100) if self.DesignDraftingClasses > 0 else 0}%")
        print(f"Quantum Aptitude Present Classes:           {self.AptitudeAttendance}           Total Classes: {self.AptitudeClasses}           Attendance Percentage: {(self.AptitudeAttendance/self.AptitudeClasses*100) if self.AptitudeClasses > 0 else 0}%")
        print(f"Cambrige English Present Classes:           {self.EnglishAttendance}            Total Classes: {self.EnglishClasses}            Attendance Percentage: {(self.EnglishAttendance/self.EnglishClasses*100) if self.EnglishClasses > 0 else 0}%")
        if self.Language.lower() == "french":
            print(f"French Present Classes:                     {self.FrenchAttendance}             Total Classes: {self.FrenchClasses}             Attendance Percentage: {(self.FrenchAttendance/self.FrenchClasses*100) if self.FrenchClasses > 0 else 0}%")
        else:
            print(f"German Present Classes:                     {self.GermanAttendance}             Total Classes: {self.GermanClasses}             Attendance Percentage: {(self.GermanAttendance/self.GermanClasses*100) if self.GermanClasses > 0 else 0}%")
        if self.TalentEnrichMentProgram.lower() == "sports":
            print(f"Sports Present Classes:                     {self.SportsAttendance}             Total Classes: {self.SportsClasses}             Attendance Percentage: {(self.SportsAttendance/self.SportsClasses*100) if self.SportsClasses > 0 else 0}%")
        elif self.TalentEnrichMentProgram.lower() == "singing":
            print(f"Singing Present Classes:                    {self.SingingAttendance}            Total Classes: {self.SingingClasses}            Attendance Percentage: {(self.SingingAttendance/self.SingingClasses*100) if self.SingingClasses > 0 else 0}%")
        elif self.TalentEnrichMentProgram.lower() == "arts":
            print(f"Arts Present Classes:                       {self.ArtsAttendance}               Total Classes: {self.ArtsClasses}               Attendance Percentage: {(self.ArtsAttendance/self.ArtsClasses*100) if self.ArtsClasses > 0 else 0}%")
        elif self.TalentEnrichMentProgram.lower() == "dance":
            print(f"Dance Present Classes:                      {self.DanceAttendance}              Total Classes: {self.DanceClasses}              Attendance Percentage: {(self.DanceAttendance/self.DanceClasses*100) if self.DanceClasses > 0 else 0}%")
        elif self.TalentEnrichMentProgram.lower() == "yoga":
            print(f"Yoga Present Classes:                       {self.YogaAttendance}               Total Classes: {self.YogaClasses}               Attendance Percentage: {(self.YogaAttendance/self.YogaClasses*100) if self.YogaClasses > 0 else 0}%")
        elif self.TalentEnrichMentProgram.lower() == "musical instrument": 
            print(f"Musical Instrument Present Classes:         {self.MusicalInstrumentAttendance}  Total Classes: {self.MusicalInstrumentClasses}  Attendance Percentage: {(self.MusicalInstrumentAttendance/self.MusicalInstrumentClasses*100) if self.MusicalInstrumentClasses > 0 else 0}%")

    def Course_Evalution(self):
        pass

    def Fee_Details(self):
        print("Your Fee Details:")
        print("--------------------------------------------------")
        TOTAL_FEE = 1000000
        print(f"Total Course Fee: {TOTAL_FEE}")
        if self.Availed_Discount > 0 and self.Unique_Code:
            Coupon_Code = input("Enter the unique code to avail the discount: ").strip()
            if not Coupon_Code:
                print("Invalid code. Code cannot be empty.")
                return

            if Coupon_Code.lower() == "none":
                print("Invalid code entered.")
                return

            if Coupon_Code == self.Unique_Code:
                Discounted_Amount = TOTAL_FEE * (self.Availed_Discount / 100)
                Total_Fee = TOTAL_FEE - Discounted_Amount

                print(f"Congratulations! You have availed {self.Availed_Discount}% discount.")
                print(f"Your total fee after discount is: {Total_Fee}")
                self.Unique_Code = None
                self.Availed_Discount = 0
            else:
                print("Invalid or already used coupon code.")

        else:
            print("You have no active discount.")
            print(f"Your Total Fee is: {TOTAL_FEE}")
    
    def Survey(self):
        pass

    def greet(self):
        print(f"Hello, {self.name}! Welcome to the world of Python programming.")

def defalut_instructors():
    python =Instructor("python90@gmail.com",9876543210,"python instructor",35,"Python@123","Active",1,"Hyderabad","Male","1989-05-15","Python","O+","full-time","2024-06-01","Hindu","Telugu","Indian")
    WebDev =Instructor("webdev123@gmail.com",9876543211,"web developer",30,"WebDev@123","Active",2,"Bangalore","Male","1994-08-20","Web Development","B+","full-time","2024-06-01","Hindu","Kannada","Indian")
    Math =Instructor("math123@gmail.com",9876543212,"math teacher",40,"Math@123","Active",3,"Chennai","Female","1984-02-10","Mathematics","A+","full-time","2024-06-01","Hindu","Tamil","Indian")
    Aptitude =Instructor("aptitude123@gmail.com",9876543213,"aptitude teacher",35,"Aptitude@123","Active",4,"Mumbai","Female","1989-07-05","Aptitude","AB+","full-time","2024-06-01","Hindu","Marathi","Indian")
    French =Instructor("french123@gmail.com",9876543214,"french teacher",30,"French@123","Active",5,"Paris","Female","1994-01-20","French","B+","full-time","2024-06-01","Hindu","French","Indian")
    Design =Instructor("design123@gmail.com",9876543215,"design teacher",35,"Design@123","Active",6,"Delhi","Male","1989-03-10","Design","O+","full-time","2024-06-01","Hindu","Hindi","Indian")
    German =Instructor("german123@gmail.com",9876543216,"german teacher",30,"German@123","Active",7,"Berlin","Male","1994-05-15","German","A+","full-time","2024-06-01","Hindu","German","Indian")
    English =Instructor("english123@gmail.com",9876543217,"english teacher",30,"English@123","Active",8,"London","Female","1994-02-15","English","B+","full-time","2024-06-01","Hindu","English","Indian")
    Physics =Instructor("physics123@gmail.com",9876543218,"physics teacher",35,"Physics@123","Active",9,"New York","Male","1989-04-10","Physics","O+","full-time","2024-06-01","Hindu","English","Indian")
    Chemistry =Instructor("chemistry123@gmail.com",9876543219,"chemistry teacher",35,"Chemistry@123","Active",10,"Boston","Female","1989-06-15","Chemistry","AB+","full-time","2024-06-01","Hindu","English","Indian")
    Sports =Instructor("sports123@gmail.com",9876543220,"sports teacher",30,"Sports@123","Active",11,"Mumbai","Male","1994-03-15","Sports","B+","part-time","2024-06-01","Hindu","English","Indian")
    Singing =Instructor("singing123@gmail.com",9876543221,"singing teacher",30,"Singing@123","Active",12,"London","Female","1994-04-15","Singing","A+","part-time","2024-06-01","Hindu","English","Indian")
    Arts =Instructor("arts123@gmail.com",9876543222,"arts teacher",30,"Arts@123","Active",13,"Paris","Female","1994-05-15","Arts","B+","part-time","2024-06-01","Hindu","French","Indian")
    Dance =Instructor("dance123@gmail.com",9876543223,"dance teacher",30,"Dance@123","Active",14,"Tokyo","Female","1994-06-15","Dance","AB+","part-time","2024-06-01","Hindu","Japanese","Indian")
    Yoga =Instructor("yoga123@gmail.com",9876543224,"yoga teacher",30,"Yoga@123","Active",15,"Delhi","Male","1994-07-15","Yoga","O+","part-time","2024-06-01","Hindu","Hindi","Indian")
    MusicalInstrument =Instructor("musicalinstrument123@gmail.com",9876543225,"musical instrument teacher",30,"MusicalInstrument@123","Active",16,"New York","Female","1994-08-15","Musical Instrument","B+","part-time","2024-06-01","Hindu","English","Indian")
    #Sports, Music, Arts, Dance, Yoga, Musical Instrument
    list_instructor[python] = [python.email, python.phone_number, python.name, python.age, python._Instructor__password, python.status, python.AdmissionInstructornumber, python.City, python.Gender, python.Date_of_birth, python.Language, python.Blood_group, python.Time,python.Date_of_joining,python.Religion,python.Mother_tongue,python.Nationality]
    list_instructor[WebDev] = [WebDev.email, WebDev.phone_number, WebDev.name, WebDev.age, WebDev._Instructor__password, WebDev.status, WebDev.AdmissionInstructornumber, WebDev.City, WebDev.Gender, WebDev.Date_of_birth, WebDev.Language, WebDev.Blood_group, WebDev.Time,WebDev.Date_of_joining,WebDev.Religion,WebDev.Mother_tongue,WebDev.Nationality]
    list_instructor[Math] = [Math.email, Math.phone_number, Math.name, Math.age , Math._Instructor__password, Math.status, Math.AdmissionInstructornumber, Math.City, Math.Gender, Math.Date_of_birth, Math.Language, Math.Blood_group, Math.Time,Math.Date_of_joining,Math.Religion,Math.Mother_tongue,Math.Nationality]
    list_instructor[Aptitude] = [Aptitude.email,Aptitude.phone_number,Aptitude.name,Aptitude.age,Aptitude._Instructor__password,Aptitude.status,Aptitude.AdmissionInstructornumber,Aptitude.City,Aptitude.Gender,Aptitude.Date_of_birth,Aptitude.Language,Aptitude.Blood_group,Aptitude.Time,Aptitude.Date_of_joining,Aptitude.Religion,Aptitude.Mother_tongue,Aptitude.Nationality]
    list_instructor[French] = [French.email,French.phone_number,French.name,French.age,French._Instructor__password,French.status,French.AdmissionInstructornumber,French.City,French.Gender,French.Date_of_birth,French.Language,French.Blood_group,French.Time, French.Date_of_joining, French.Religion, French.Mother_tongue, French.Nationality]   
    list_instructor[Design] = [Design.email , Design.phone_number , Design.name , Design.age , Design._Instructor__password , Design.status , Design.AdmissionInstructornumber , Design.City , Design.Gender , Design.Date_of_birth , Design.Language , Design.Blood_group , Design.Time,Design.Date_of_joining,Design.Religion,Design.Mother_tongue,Design.Nationality]
    list_instructor[German] = [German.email , German.phone_number , German.name , German.age , German._Instructor__password , German.status , German.AdmissionInstructornumber , German.City , German.Gender , German.Date_of_birth , German.Language , German.Blood_group , German.Time,German.Date_of_joining,German.Religion,German.Mother_tongue,German.Nationality]
    list_instructor[English] = [English.email, English.phone_number, English.name, English.age, English._Instructor__password, English.status, English.AdmissionInstructornumber, English.City, English.Gender, English.Date_of_birth, English.Language, English.Blood_group, English.Time,English.Date_of_joining,English.Religion,English.Mother_tongue,English.Nationality] 
    list_instructor[Physics] = [Physics.email, Physics.phone_number, Physics.name, Physics.age, Physics._Instructor__password, Physics.status, Physics.AdmissionInstructornumber, Physics.City, Physics.Gender, Physics.Date_of_birth, Physics.Language, Physics.Blood_group, Physics.Time,Physics.Date_of_joining,Physics.Religion,Physics.Mother_tongue,Physics.Nationality]
    list_instructor[Chemistry] = [Chemistry.email, Chemistry.phone_number, Chemistry.name, Chemistry.age, Chemistry._Instructor__password, Chemistry.status, Chemistry.AdmissionInstructornumber, Chemistry.City, Chemistry.Gender, Chemistry.Date_of_birth, Chemistry.Language, Chemistry.Blood_group, Chemistry.Time,Chemistry.Date_of_joining,Chemistry.Religion,Chemistry.Mother_tongue,Chemistry.Nationality] 
    list_instructor[Sports] = [Sports.email, Sports.phone_number, Sports.name, Sports.age, Sports._Instructor__password, Sports.status, Sports.AdmissionInstructornumber, Sports.City, Sports.Gender, Sports.Date_of_birth, Sports.Language, Sports.Blood_group, Sports.Time,Sports.Date_of_joining,Sports.Religion,Sports.Mother_tongue,Sports.Nationality]
    list_instructor[Singing] = [Singing.email, Singing.phone_number, Singing.name, Singing.age, Singing._Instructor__password, Singing.status, Singing.AdmissionInstructornumber, Singing.City, Singing.Gender, Singing.Date_of_birth, Singing.Language, Singing.Blood_group, Singing.Time,Singing.Date_of_joining,Singing.Religion,Singing.Mother_tongue,Singing.Nationality]
    list_instructor[Arts] = [Arts.email, Arts.phone_number, Arts.name, Arts.age, Arts._Instructor__password, Arts.status, Arts.AdmissionInstructornumber, Arts.City,Arts.Gender, Arts.Date_of_birth, Arts.Language, Arts.Blood_group, Arts.Time,Arts.Date_of_joining,Arts.Religion,Arts.Mother_tongue,Arts.Nationality]
    list_instructor[Dance] = [Dance.email, Dance.phone_number, Dance.name, Dance.age, Dance._Instructor__password, Dance.status, Dance.AdmissionInstructornumber, Dance.City,Dance.Gender, Dance.Date_of_birth,Dance.Language,Dance.Blood_group,Dance.Time,Dance.Date_of_joining,Dance.Religion,Dance.Mother_tongue,Dance.Nationality]
    list_instructor[Yoga] = [Yoga.email,Yoga.phone_number,Yoga.name,Yoga.age,Yoga._Instructor__password,Yoga.status,Yoga.AdmissionInstructornumber,Yoga.City,Yoga.Gender,Yoga.Date_of_birth,Yoga.Language,Yoga.Blood_group,Yoga.Time,Yoga.Date_of_joining,Yoga.Religion,Yoga.Mother_tongue,Yoga.Nationality]
    list_instructor[MusicalInstrument] = [MusicalInstrument.email,MusicalInstrument.phone_number,MusicalInstrument.name,MusicalInstrument.age,MusicalInstrument._Instructor__password,MusicalInstrument.status,MusicalInstrument.AdmissionInstructornumber,MusicalInstrument.City,MusicalInstrument.Gender,MusicalInstrument.Date_of_birth,MusicalInstrument.Language,MusicalInstrument.Blood_group,MusicalInstrument.Time,MusicalInstrument.Date_of_joining,MusicalInstrument.Religion,MusicalInstrument.Mother_tongue,MusicalInstrument.Nationality]  

def defalut_students():
    student_1=Saketh("praveenkumar@gmail.com",9099455810,"PraveenKumar",18,"Praveen@123","Active",74108520936,7401,"Vijayawada","male","19/06/2008","French","Sports",0,"A+","Saketh Srinu","Saketh Srilatha","Saketh Srinu",7410852090,"Indian","Telugu","Hindu",7410852090,0,0)
    student_2=Saketh("varshithkumar@gmail.com",9440025408,"VarshithKumar",18,"Varshith@123","Active",74108520937,7402,"Hyderabad","male","20/07/2007","English","Music",0,"B+","Rahul Srinu","Rahul Srilatha","Rahul Srinu",7410852091,"Indian","Hindi","Hindu",7410852091,0,0)
    student_3=Saketh("chunduridhanush@gmail.com",9391899088,"Dhanush",18,"Chinnu@123","Active",74108520938,7403,"Chennai","male","21/08/2006","German","Dance",0,"O+","Sai Srinu","Sai Srilatha","Sai Srinu",7410852092,"Indian","Tamil","Hindu",7410852092,0,0)
    student_4=Saketh("saisathwik@gmail.com",6301556419,"Sai",18,"Sai@123","Active",74108520939,7404,"Bangalore","male","22/09/2005","Hindi","Yoga",0,"AB+","Kiran Srinu","Kiran Srilatha","Kiran Srinu",7410852093,"Indian","Kannada","Hindu",7410852093,0,0)
    student_5=Saketh("ramtejareddy@gmail.com",9908369027,"RamTejaReddy",18,"Ram@123","Active",74108520940,7405,"Mumbai","female","23/10/2004","Tamil","MusicalInstrument",0,"B-","Lakshmi Srinu","Lakshmi Srilatha","Lakshmi Srinu",7410852094,"Indian","Tamil","Hindu",7410852094,0,0)
    student_6=Saketh("charansagar@gmail.com",9347660058,"CharanSagar",18,"Charan@123","Active",74108520941,7406,"Delhi","female","24/11/2003","Telugu","Arts",0,"O-","Ananya Srinu","Ananya Srilatha","Ananya Srinu",7410852095,"Indian","Telugu","Hindu",7410852095,0,0)
    list_of_students[student_1] = [student_1.email, student_1.phone_number, student_1.name, student_1.age, student_1._Saketh__password, student_1.status, student_1.Registrationnumber, student_1.Admissionnumber, student_1.City, student_1.Gender, student_1.Date_of_birth, student_1.Language, student_1.TalentEnrichMentProgram, student_1.Percentage, student_1.Blood_group, student_1.Father_name, student_1.Mother_name, student_1.Guardian_name, student_1.Emergency_contact_number, student_1.Nationality, student_1.Mother_tongue, student_1.Religion, student_1.Parent_Mobile_number,student_1.Availed_Discount, student_1.Unique_Code]
    list_of_students[student_2] = [student_2.email, student_2.phone_number, student_2.name, student_2.age, student_2._Saketh__password, student_2.status, student_2.Registrationnumber, student_2.Admissionnumber, student_2.City, student_2.Gender, student_2.Date_of_birth, student_2.Language, student_2.TalentEnrichMentProgram, student_2.Percentage, student_2.Blood_group, student_2.Father_name, student_2.Mother_name, student_2.Guardian_name, student_2.Emergency_contact_number, student_2.Nationality, student_2.Mother_tongue,student_2.Religion ,student_2.Parent_Mobile_number,student_2.Availed_Discount, student_2.Unique_Code]
    list_of_students[student_3] = [student_3.email, student_3.phone_number, student_3.name, student_3.age ,student_3._Saketh__password ,student_3.status ,student_3.Registrationnumber ,student_3.Admissionnumber ,student_3.City ,student_3.Gender ,student_3.Date_of_birth ,student_3.Language ,student_3.TalentEnrichMentProgram ,student_3.Percentage ,student_3.Blood_group, student_3.Father_name, student_3.Mother_name, student_3.Guardian_name, student_3.Emergency_contact_number, student_3.Nationality, student_3.Mother_tongue, student_3.Religion, student_3.Parent_Mobile_number,student_3.Availed_Discount, student_3.Unique_Code]
    list_of_students[student_4] = [student_4.email, student_4.phone_number, student_4.name, student_4.age ,student_4._Saketh__password ,student_4.status ,student_4.Registrationnumber ,student_4.Admissionnumber ,student_4.City ,student_4.Gender ,student_4.Date_of_birth ,student_4.Language ,student_4.TalentEnrichMentProgram ,student_4.Percentage ,student_4.Blood_group, student_4.Father_name, student_4.Mother_name, student_4.Guardian_name, student_4.Emergency_contact_number, student_4.Nationality, student_4.Mother_tongue, student_4.Religion, student_4.Parent_Mobile_number,student_4.Availed_Discount, student_4.Unique_Code]
    list_of_students[student_5] = [student_5.email, student_5.phone_number, student_5.name, student_5.age ,student_5._Saketh__password ,student_5.status ,student_5.Registrationnumber ,student_5.Admissionnumber ,student_5.City ,student_5.Gender ,student_5.Date_of_birth ,student_5.Language ,student_5.TalentEnrichMentProgram ,student_5.Percentage ,student_5.Blood_group, student_5.Father_name, student_5.Mother_name, student_5.Guardian_name, student_5.Emergency_contact_number, student_5.Nationality, student_5.Mother_tongue, student_5.Religion, student_5.Parent_Mobile_number,student_5.Availed_Discount, student_5.Unique_Code]
    list_of_students[student_6] = [student_6.email, student_6.phone_number, student_6.name, student_6.age ,student_6._Saketh__password ,student_6.status ,student_6.Registrationnumber ,student_6.Admissionnumber ,student_6.City ,student_6.Gender ,student_6.Date_of_birth ,student_6.Language ,student_6.TalentEnrichMentProgram ,student_6.Percentage ,student_6.Blood_group, student_6.Father_name, student_6.Mother_name, student_6.Guardian_name, student_6.Emergency_contact_number, student_6.Nationality, student_6.Mother_tongue, student_6.Religion, student_6.Parent_Mobile_number,student_6.Availed_Discount, student_6.Unique_Code]

defalut_instructors()
defalut_students()

while True:
        print("Welcome to Advanced AURORA x NIAT ERP System!")
        print("Please select an option:")
        print("--------------------------------------------------")
        Instructor_or_Student=input("Press 'I' for Instructor or 'S' for Student: ")
        if Instructor_or_Student not in ['I', 'S', 'A2151']:
            print("Invalid option. Please enter 'I' for Instructor or 'S' for Student.")
            continue
        if Instructor_or_Student=="A2151":
            print("Welcome Admin!")
            a=Main_Menu_Admin()
            if a == 10:
                break
       
        elif Instructor_or_Student == "I":
            secret_code = input("Enter the secret code to access instructor features: ")
            if secret_code != "!@#":
                print("Invalid secret code. Access denied.")
                continue
            print("Press 'C' to create an account")
            print("Press 'L' to login")
            choice = input("Enter your choice: ")
            if choice not in ['C', 'L']:
                print("Invalid choice. Please enter 'C' to create an account or 'L' to login.")
                continue
            if choice == "C":
                Instructor_account()
           
            elif choice == "L":
                print("email should be in lowercase and should end with @gmail.com and should not contain spaces and special characters except @ and . and should contain only one @ and should have at least one character before @ and should have at least one character between @ and . and should have at least 2 characters after .")
                email = input("Enter your email: ")
                is_valid.email_validation(email)
                for j,i in list_instructor.items():
                    if i[0] == email:
                        password = input("Enter your password: ")
                        is_valid.password_validation(password)
                        if i[4] == password:
                            print(f"Welcome back, {i[2]}!")
                            while True:
                                    a=Main_Menu_Instructors(j)
                                    if a == 10:
                                        break
        
        elif Instructor_or_Student == "S":
            print("Press 'C' to create an account")
            print("Press 'L' to login")
            choice = input("Enter your choice: ")
            
            if choice == "C":
                Student_account()
            elif choice == "L":
                print("email should be in lowercase and it should end with @gmail.com and should not contain spaces and special characters except '@' and '.' and should contain only one @ and should have at least one character before @ and should have at least one character between @ and . and should have at least 2 characters after .")
                email = input("Enter your email: ")
                is_valid.email_validation(email)
                for j,i in list_of_students.items():
                    if i[0] == email:
                        password = input("Enter your password: ")
                        is_valid.password_validation(password)
                        if i[4] == password:
                            print(f"Welcome back, {i[2]}!")
                            while True:
                                a=Main_Menu_students(j)
                                if a == 10:
                                    break