import csv

class Option:
    def __init__(self, text :str):
        self.text = text
        self.is_answer = False

class Question:

    def __init__(self):
        self.options = []
        self.text = ''
        self.instruction = ''

    def add_option(self, opt :Option):
        self.options.append(opt)
    
    def has_options(self):
        return len(self.options) > 0
    
    def finalize_import(self):
        index = self.text.find(r'(')
        self.instruction = self.text[index:]

        if len(self.instruction) > 1:
            self.text = self.text.replace(self.instruction, '')
        else:
            self.instruction = ''

    def __str__(self) -> str:
        opt_text = ''
        for opt in self.options:
            opt_text += opt.text + '\n'   
        return  self.text + '\n' + opt_text + self.instruction + '\n'

def is_an_answer(textline :str):
    prefixes = ["A)", "B)", "C)", "D)", "E)", "F)", "G)", "H)", "I)", "J)"]
    for prefix in prefixes:
        if textline.startswith(prefix):
            return True
    return False

def import_from_csv(path :str):
    questions = []
    with open(path, newline='',  encoding='utf-8') as f:
        reader = csv.reader(f, delimiter=';')
        quest :Question= None
        for row in reader:
            if not is_an_answer(row[0]):
                if quest == None:
                    quest = Question()
                elif quest.has_options():
                    questions.append(quest)
                    quest = Question()
                quest.text += row[0]
            else:
                splitted = row[0].split('\n')
                for i in range(0,len(splitted)): 
                    quest.add_option(Option(splitted[i]))
        for q in questions:
            q.finalize_import()
    return questions

def main():
    test_csv = 'quiz/test.csv'
    sm_csv = 'quiz/q_a_scrum_master_2.csv'
    print("\nREAD CSV\n")
    imported_questions = import_from_csv(sm_csv)
    for q in imported_questions:
        print(q)
                
            


if __name__ == "__main__":
    main()