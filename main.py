"""
Program generates "best acts" statements.
"""
# ....................................................................... Imports
import random
import pyperclip
import word_list
import time
# ....................................................................... Main Function
def main():
    ALL_OUTPUTS = []
    while True:
        #print(brand_name())
        print("Enter Number of Acts to generate:")
        response = (input("> "))
# .......................................................................       
        if not response.isdecimal():
            print("Enter another number".title())
        else:
            number_of_acts = int(response)
            break
# .......................................................................
    print("Best Acts for {}".format(b).title())
# .......................................................................
    for index, statement in enumerate(range(number_of_acts)):
        act = best_act_statement()
        print(f'{index:02d}', act)
        time.sleep(.50)
        ALL_OUTPUTS.append(act)
# .......................................................................
    ALL_OUTPUTS = "\n".join(ALL_OUTPUTS)
    pyperclip.copy(ALL_OUTPUTS)
    print("\nAll Results copied to clipboard.\nEdit from here :)")
# ....................................................................... Sub Functions
def title():
    string = "july 2021\tbest acts generator\tjack allan\n"
    print(string.title())
def brand_name():
    brand_name = str(input("what brand are you representing? ".title()))
    return brand_name
def rand_emo_pos():
    string = random.choice(word_list.POSITIVE_NOUN)
    return "{}".format(string)
def rand_emo_neg():
    string = random.choice(word_list.ALT_EMOTION)
    return "{}".format(string)
def rand_prep():
    string = random.choice(word_list.PREPOSITION)
    return "{}".format(string)
def rand_time():
    string = random.choice(word_list.TIME_REF)
    return "{}".format(string)
def best_act_statement():
    build = "{} {} {} of {}".format(rand_emo_pos(), rand_prep(), rand_time(), rand_emo_neg())
    return build.title()
# ....................................................................... On Run, Export, Import
if __name__ == "__main__":
    title()
    runs = 0
    max_runs = 10
    while True:
        runs += 1
        b = brand_name()
        main()
        run_again = str(input("do you want to run again? type (y)es or (n)o: "))
# .......................................................................
        if run_again == "n" or run_again == "N" or run_again == "no" or run_again == "No" or run_again == "NO":
            print("thanks for using this program\nprogram ending.")
            exit()
# .......................................................................
        if run_again == "y" or run_again == "Y" or run_again == "yes" or run_again == "Yes" or run_again == "YES":
            b = brand_name()
            main()
 # .......................................................................           
        elif runs >= max_runs:
            print("max runs reached\namost recent results copied to clipboard\nexiting...")
            exit()
# 
# ....................................................................... Updates
"""
date | update note
"""
# ....................................................................... Bugs / Errors
"""
date | bug note | at-large/patched
"""
