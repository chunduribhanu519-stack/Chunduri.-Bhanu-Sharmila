import sys

def Timevalidation(Time):
    if Time in ["full-time", "part-time"]:
        return Time
    else:
        return sys.exit("Invalid time. Please enter 'Full-time' or 'Part-time'.")
    
def Religionvalidation(Religion):
    if Religion in ["hindu", "muslim", "christian", "sikh", "buddhist", "jain", "parsi", "judaism", "bahai", "taoism", "shintoism", "confucianism", "zoroastrianism", "animism", "atheism", "agnosticism", "other"]:
        return Religion
    else:
        return sys.exit("Invalid religion. Please enter a valid religion from the list.")
    
def Mother_tonguevalidation(Mother_tongue):
    if Mother_tongue in ["hindi", "english", "spanish", "french", "german", "chinese", "japanese", "brazilian portuguese", "italian", "russian", "mexican spanish", "south african afrikaans", "nigerian pidgin", "egyptian arabic", "argentinian spanish", "saudi arabic", "turkish", "indonesian", "pakistani urdu", "bangladeshi bengali", "vietnamese", "philippine tagalog", "malaysian malay", "thai", "iranian persian", "iraqi arabic", "afghan pashto"]:
        return Mother_tongue
    else:
        return sys.exit("Invalid mother tongue. Please enter a valid mother tongue from the list.")
    
def Nationalityvalidation(Nationality):
    if Nationality in ["indian", "american", "british", "canadian", "australian", "french", "german", "chinese", "japanese", "brazilian", "italian", "spanish", "russian", "mexican", "south african", "nigerian", "egyptian", "argentinian", "saudi", "turkish", "indonesian", "pakistani", "bangladeshi", "vietnamese", "philippine", "malaysian", "thai", "iranian", "iraqi", "afghan", "sudanese", "algerian", "moroccan", "tunisian", "libyan"]:
        return Nationality
    else:
        return sys.exit("Invalid nationality. Please enter a valid nationality.")

def is_valid_phone(phone):
    if  len(phone)==10 and  phone.isdigit( ):
               return phone
    elif phone.isalpha():
        print('your entering the letters instead of numbers')
        print("Try Again")
        phone = input("Enter Your Mobile Number? ")
        phone = is_valid_phone(phone)
        return phone
    elif phone.isdigit( ) and len(phone) < 10:
        print('phone number should be 10 digits long')
        print("Try Again")
        phone = input("Enter Your Mobile Number? ")
        phone = is_valid_phone(phone)
        return phone
    elif phone.isdigit( ) and len(phone) > 10:
        print('phone number should be 10 digits long')
        print("you are entering more than 10 digits")
        print("Try Again")
        phone = input("Enter Your Mobile Number? ")
        phone = is_valid_phone(phone)
        return phone
    else:
        print("Try again")
        phone = input("Enter Your Mobile Number? ")
        phone = is_valid_phone(phone)
        return phone

def is_valid_name(name):
    name2 = name.strip().replace(" ", "")
    if name2.isalpha() and len(name2) >= 2 and len(name2) <= 50:
        return name
    elif name.isdigit():
        print('your entering the numbers instead of name')
        print("Try Again")
        name = input("Enter your  name: ")
        name = is_valid_name(name)
        return name
    else:
        print('Invalid name. Please enter a valid name.')
        print("your are using special characters\n or using both letters and numbers")
        print("Try Again")
        name = input("Enter your  name: ")
        name = is_valid_name(name)
        return name

def email_validation(email):
    if email.endswith("@gmail.com"):
        if email.islower() and email.count("@") == 1 and email.index("@") > 0 and email.index("@") < len(email) - 10 :
            return email
    else:
        return sys.exit("Invalid email address. Please enter a valid Gmail address.")
    
def cityvalidation(city):
    if city.isalpha():
        return city
    else:
        return sys.exit("Invalid city name. Please enter a valid city name containing only letters.")
    
def Gendervalidation(gender):
    if gender.lower() in ["male", "female", "other"]:
        return gender
    else:     
        return sys.exit("Invalid gender. Please enter 'Male', 'Female',    or 'Other'.")
    
def password_validation(password):    
    if len(password) >= 8 and any(char.isdigit() for char in password) and any(char.isalpha() for char in password) and any(char in "!@#$%^&*()-_=+[]{}|;:,.<>?/" for char in password) and not any(char.isspace() for char in password):
        return password
    else:
        return sys.exit("Invalid password. Password must be at least 8 characters long, contain at least one digit, one letter, one special character, and no spaces.")
    
def Languagevalidation(Language):
    if Language.lower() in ["french", "germany"]:
        return Language
    else:
        return sys.exit("Invalid language. Please enter 'French' or 'Germany'.")
    
def TalentEnrichMentProgramvalidation(TalentEnrichMentProgram):
    if TalentEnrichMentProgram.lower() in ["sports", "singing", "arts", "dance", "yoga", "musical instrument"]:
        return TalentEnrichMentProgram
    else:
        return sys.exit("Invalid choice. Please enter one of the following: Sports, Singing, Arts, Dance, Yoga, Musical Instrument.")
    
def PercentageVlidation(Percentage):
    try:
        percentage = float(Percentage)
        if 0 <= percentage <= 100:
            return percentage
        else:
            return sys.exit("Invalid percentage. Please enter a value between 0 and 100.")
    except ValueError:
        return sys.exit("Invalid input. Please enter a numeric value for percentage.")
    
def Blood_groupvalidation(Blood_group):
    valid_blood_groups = ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-","hh"]
    if Blood_group in valid_blood_groups:   
                pass
    else:
        return sys.exit("Invalid blood group. Please enter a valid blood group (e.g., A+, O-, etc.).")
    
def is_validInstructor_date_of_birth(Date_of_birth):
    list_of_leap_years = [1928,1932,1936,1940,1944,1948,1952,1956,1960,1964,1968,1972,1976,1980,1984,1988,1992,1996,2000,2004,2008,2012,2016,2020,2024]
    day, month, year = map(int, Date_of_birth.split('/'))
    if 1 <= day <= 31 and 1 <= month <= 12 and 2009 > year > 1926:
        if (month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12) and day <= 31:
            return Date_of_birth
        elif (month == 4 or month == 6 or month == 9 or month == 11) and day <= 30:
            return Date_of_birth
        elif (month == 2 and day <= 28) or year in list_of_leap_years and day == 29:
            return Date_of_birth
        else:
            print("Invalid Date of Birth")

def is_valid_dob(Date_of_birth):
    list_of_leap_years = [2004,2008]
    day, month, year = map(int, Date_of_birth.split('/'))
    if 1 <= day <= 31 and 1 <= month <= 12 and 2009 > year > 2001:
        if (month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12) and day <= 31:
            return Date_of_birth
        elif (month == 4 or month == 6 or month == 9 or month == 11) and day <= 30:
            return Date_of_birth
        elif (month == 2 and day <= 28) or year in list_of_leap_years and day == 29:
            return Date_of_birth
        else:
            print("Invalid Date of Birth")
    if year >= 2026:
        print('Invalid Date of Birth. Year should be less than 2026.')
        print("Try Again")
        print("Re enter the Full Date of Birth")
        Date_of_birth = f" {input("Enter your Date of Birth \n DD: ")}/{input(" MM: ")}/{input(" YYYY: ")}".split()[-1]
        Date_of_birth = is_valid_dob(Date_of_birth)
        return Date_of_birth
    if year <= 1926:
        print('Invalid Date of Birth. Year should be greater than 1926.')
        print("Try Again")
        print("Re enter the Full Date of Birth")
        Date_of_birth = f" {input("Enter your Date of Birth \n DD: ")}/{input(" MM: ")}/{input(" YYYY: ")}".split()[-1]
        Date_of_birth = is_valid_dob(Date_of_birth)
        return Date_of_birth
    if not (1 <= day <= 31):
        print('Invalid Date of Birth. Day should be between 1 and 31.')
        print("Try Again")
        print("Re enter the Full Date of Birth")
        Date_of_birth = f" {input("Enter your Date of Birth \n DD: ")}/{input(" MM: ")}/{input(" YYYY: ")}".split()[-1]
        Date_of_birth = is_valid_dob(Date_of_birth)
        return Date_of_birth
    if not (1 <= month <= 12):
        print('Invalid Date of Birth. Month should be between 1 and 12.')
        print("Try Again")
        print("Re enter the Full Date of Birth")
        Date_of_birth = f" {input("Enter your Date of Birth \n DD: ")}/{input(" MM: ")}/{input(" YYYY: ")}".split()[-1]
        Date_of_birth = is_valid_dob(Date_of_birth)
        return Date_of_birth
    else :
        print("Try Again")
        print("Re enter the Full Date of Birth")
        Date_of_birth = f" {input("Enter your Date of Birth \n DD: ")}/{input(" MM: ")}/{input(" YYYY: ")}".split()[-1]
        Date_of_birth = is_valid_dob(Date_of_birth)
        return Date_of_birth    
     
def LanguageInstructorvalidation(Language):
    if Language.lower() in ["python","web development","mathematics","aptitude","design and drafting","physics","chemistry","english","sports", "singing", "arts", "dance", "yoga", "musical instrument"]:
        pass
    else:
        return sys.exit("Invalid language. Please enter 'Python', 'Web Development', 'Mathematics', 'Aptitude', 'Design and Drafting', 'Physics', 'Chemistry', 'Sports', 'Singing', 'Arts', 'Dance', 'Yoga', or 'Musical Instrument '.")