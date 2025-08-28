# Mode
# r -> Read
# w -> Write
# a -> Append

file = open(r"C:\Python Training\file_handling\wiki.txt", mode="a")
file.write("\n123456789")

file.close()