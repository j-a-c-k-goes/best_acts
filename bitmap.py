"""
display text emssage according to bitmap image
"""
import sys
# ................................................................ Imports
bitmap = """....................................................................
   **************   *  *** **  *      ******************************
  ********************* ** ** *  * ****************************** *
 **      *****************       ******************************
          *************          **  * **** ** ************** *
           *********            *******   **************** * *
            ********           ***************************  *
   *        * **** ***         *************** ******  ** *
               ****  *         ***************   *** ***  *
                 ******         *************    **   **  *
                 ********        *************    *  ** ***
                   ********         ********          * *** ****
                   *********         ******  *        **** ** * **
                   *********         ****** * *           *** *   *
                     ******          ***** **             *****   *
                     *****            **** *            ********
                    *****             ****              *********
                    ****              **                 *******   *
                    ***                                       *    *
                    **     *                    *
...................................................................."""
def spaces_in_map(bitmap):
    spaces = bitmap.count(" ")
    return spaces

def make_bitmap_message(message):
    for line in bitmap.splitlines():
        for i, bit in enumerate(line):
            if bit == " ":
                print(" ", end="")
            else:
                print(message[i % len(message)], end="")
        print()
        
if __name__ == "__main__":

    print("enter a message to dispaly with global bitmap...")
    message = input(str("> "))
    if message == "":
        exit()
    else:
        print("Your map has {} spaces.".format(spaces_in_map(bitmap)))
        print()
        make_bitmap_message(message)
    
