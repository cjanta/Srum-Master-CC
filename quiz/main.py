import csv


def main():
    print("\nREAD CSV\n")
    with open('quiz/test.csv', newline='\n',  encoding='utf-8') as f:
        reader = csv.reader(f)
        count = 0
        for row in reader:
            if count > 0 and count < 3:
                if count == 1: #question
                    print(row[0])
                if count == 2: #answers
                    splitted = row[0].split('\n')
                    for i in range(0,len(splitted)): 
                        print(splitted[i])
                        print(i)
            count += 1
                
           
            


if __name__ == "__main__":
    main()