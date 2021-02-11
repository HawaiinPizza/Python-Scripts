import getopt, sys

import Main

def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hn", ["help", "next"])
    except getopt.GetoptError as err:
        # print help information and exit:
        print(err) # will print something like "option -arg not recognized"
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print("Help menu ")
            sys.exit()
        elif opt in ("-n", "--next"):
            print(Main.nextPrayer())

        else:
            assert False, "unhandled option"
    # ...

main()
