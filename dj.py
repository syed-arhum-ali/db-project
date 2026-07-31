import os
import filecmp

while True:
    print(
        "it is a function to identify two looking files or known as file duplicate checker, here you go: "
    )
    choice = input("1.start opening the function\n2.exit\nchoose now: ")
    if choice == "1":
        try:
            file1 = input("enter the file name:\n")
            file2 = input("enter the copy file you wanna check:\n")

            if  os.path.isfile(file1) and os.path.isfile(file2):
                if os.path.getsize(file1) != os.path.getsize(file2):
                    print("Files are not duplicates.")
                else:
                    if filecmp.cmp(file1, file2, shallow=False):
                        print("these files are exact duplicate of each other")
                    else:
                        print("they are different")
            else:
                print("please enter a valid file")

        except Exception as e:
            print(e)
            print("pls try again")

    elif choice == "2":
        print("okay bye! have a great day")
        break

    else:
        print("please choose 1 or 2, try gain! ")
