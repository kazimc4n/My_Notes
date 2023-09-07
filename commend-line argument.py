import sys

if len(sys.argv) < 2:
    sys.exit("too many argument")

for arg in sys.argv[1:]:
    print("hello there!: ", arg)
