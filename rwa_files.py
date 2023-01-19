with open('etx.txt', 'r') as a:
    # a.readline()
    for ab in a:
        print(ab, end='')
#there is an issiue in reading .docx files though we know it handles text and binary files.
#how can i read .docx