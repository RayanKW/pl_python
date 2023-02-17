import sys
def main():
    if len(sys.argv) <2:
        print('usage greater')
        print('hello')
    else:
        filename = sys.argv[1]
        groups = {}
        with open(filename, 'r') as f:
            content = f.read()
            words = content.split()
            for word in words:
                word =word.upper()
                size =len(word)
                if size in groups:
                    if word not in groups[size]:
                        groups[size] += [word]
                else:
                    groups[size] = [word]
            for size, group in groups.items():
                print (size, ':', group)
if __name__ == '__main__':
    main()