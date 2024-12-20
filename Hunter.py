import sys
import time

def type_out_message(message, delay=0.025):
    """Types out a message letter by letter with a delay."""
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()  # Move to the next line after the message

def wait_for_input():
    """Waits for the user to press Enter to proceed."""
    input("Press Enter to continue...")

def main():
    """Main function to execute the typewriter-style message display."""
    messages = [
	"\n\033[31m#####################################################################################"
	"\n\033[31m####   ###   ###    ###   ###     ##     ##   ########    #######      ######    ####"
	"\n\033[31m####   ###   ###    ###   ###     ####   ##      ##       ##           ##  ###   ####"
	"\n\033[31m####   #########    ###   ###     #####  ##      ##       #######      #####     ####"
	"\n\033[31m####   ###   ###    #### ####     ## ### ##      ##       ##           ##  ##    ####"
	"\n\033[31m####   ###   ###     #######      ##   ####      ##       #######      ##   ##   ####"
	"\n\033[31m#####################################################################################\033[0m",
	"\033[0m"
        "\nHey Hunter, I learned how to write functions for this, hope it turns out well. All of us here want to wish you well and say a few words before you go!",
        "\n\033[33mHunter, I just wanted to say how much I’ve appreciated working with you over the past several years. You’ll definitely be missed, Keep up the good work! I Wish you all the best in your next adventure. Keep in touch! Take care \n\033[32m -Aron\033[0m",
        "\n\033[33mHunter, It has been a pleasure working with you. I wish you all the best in your future endeavors. I hope wherever you end up, it’s a great move and you excel as I am sure you will.  Please don’t be a stranger and if you find yourself on St. Croix, dinner is on me 😊  \n\033[32m -Sairys\033[0m",
       	"\n\033[33mWishing a successful build on all your projects and I hope you get all the help whenever you need it. To better things, heap heap array!\n\033[32m -Ash\033[0m",
	"\n\033[33mHi Hunter, You've been a great colleague. I'll miss seeing you around the office, but I know you'll do great things in your future endeavors! .Wishing you all the very best and continued success in your career.\n\033[32m -Tamara\033[0m ",
	"\n\033[33mIt's been a pleasure working with you, thank you for all your hard work and support. I'll miss having you around, but wish you the best of luck in your new role!\n\033[32m -Dmytro\033[0m",
	"\n\033[33mHey Hunter, you have been a Spectacular mentor to me and have taught us all a great deal! I don't know what else to say but thank you and everything you've done has been appreciated more than you could think. I'll miss you around here and it's going to be extremely boring without you. Thank you \n\033[32m  -Adam.\033[0m",
	"\n\033[33mI can't speak for everyone, but I can say I hope wherever you end up I hope you enjoy what you do!\033[0m",
    ]

    for message in messages:
        type_out_message(message)
        wait_for_input()

if __name__ == "__main__":
    main()
