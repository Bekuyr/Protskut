

import statistics as stat
import matplotlib.pyplot as mat

mat.figure()

def index_responses(list_of_responses):
    """
    This function will create a dictionary connecting the response to a question
    :param list_of_responses: A list of responses seperated by a comma
    :return: The dictionary with question number as key and response as value
    """
    responses={}
    qnumber=1
    for r in list_of_responses:
        responses["Q"+str(qnumber)]=r
        qnumber+=1
    return responses


print('Testing index_responses()')
print(index_responses(['a', 'b', 'c']))
print(index_responses(['a','a','c','b']))
print(index_responses(['d','d','b','e','e','e','d','a']))
print("")

def index_student(student_data):
    """
     This function puts a students name, student ID and responses in a dictionary,
     out of these the responses are in another dictionary inside the dictionary
     :param student_data: The data of a student in a list with order [ID,Name,response1,response2...]
     :return:It returns a dictionary consisting of keys Name, ID and Responses.
     The value for Name is student's name, for ID it is the student's ID
     and for Responses it is a new dictionary for the grades (see index_responses for more info)
     """
    student = {}
    student["ID"] = student_data[0]
    student["Name"] = student_data[1]
    student["Responses"] = index_responses(student_data[2:])
    return student




# Question 2
# 11:15am 20 Oct 2016: corrected second test
print('Testing index_student()')
print(index_student(['345','xyzzy','a','a','c','b']))
print(index_student(['10021795','Samden Cross', 'd','d','b','e','e','e','d','a']))
print("")



def index_class(class_data):
    """
    This function computes the same data as function index_student, but goes through a list of correctly written lists.
    The function makes a key from student ID and the value is the value of the return value of function index_student.
    It creates a new dictionary entry for each student on the list
    :param class_data: List of lists including the same data in the same order as index_student
    :return: The function returns a dictionary with keys consisting of student IDs and values consisting of
    return values of index_student
    """
    c_data={}
    for r in class_data:
        c_data[r[0]] = index_student(r)
    return c_data


# Question 3
print('Testing index_class()')
print(index_class([['123','foo', 'a','b','c','a'],
                   ['234','bar', 'a','b','c','b'],
                   ['345','xyzzy','a','a','c','b']]))
print(index_class([['10021795','Samden Cross', 'd','d','b','e','e','e','d','a'],
                   ['11051158','Jenni Nuxulon','d','d','b','e','e','d','d','a']]))
print("")


def grade_student(answers,responses):
    """
    This function takes two lists:answers and responses and returns the value of similiar values for each index
    :param answers: A list consisting correct answers
    :param responses: A list consisting responses by the student
    :return: Number of responses matching the answers
    """
    correct_responses=0
    for q in responses:
        if responses[q]==answers[q]:
            correct_responses+=1
    return correct_responses

# Question 4
print('Testing grade_student')
answers = index_responses(['a','b','c'])
resp1 = index_responses(['a','b','b'])
resp2 = index_responses(['a','b','c'])
print('Correct responses for first example:', grade_student(answers,resp1))
print('Correct responses for second example:', grade_student(answers,resp2))
print("")


def grade(answers,student_data):
    """
    This function compares the responses made by the student to the answer sheet and adds a new entry to the dictionary entered
    as the argument to student_data as 'Score'. The value to this key is the value of responses matching the same question on answer
    :param answers:A dictionary of correct answers
    :param student_data: List of lists including the same data in the same order as index_student
    :return: The function doesn't return anything, but it adds the entry 'Score' to each key
    """
    for r in student_data:
        student_data[r]['Score']=grade_student(answers,student_data[r]['Responses'])



# Question 5
print('Testing grade')
answers = index_responses(['a','b','c','b'])
response_db = index_class([['123','foo', 'a','b','c','a'],
                           ['234','bar', 'a','b','c','b'],
                           ['345','xyzzy','a','a','c','b']])


# Question 5
print('Response DB before')
print(response_db)
grade(answers,response_db)
print('Response DB after')
print(response_db)
print(" ")


def read_response_file(file_name):
    """
    This function reads a text file and creates a list from each line and appends it to the list students
    The function skips the first line, since it doesn't have any data from the students
    :param file_name: The name of the file, needs to have the format after the filename (.txt etc)
    :return: Function returns the list of lists. Each list consists of student ID, student name and responses
    """
    f = open(file_name ,'r')

    students=[]
    for line in f:
        mapping = line.rstrip()
        mapping = mapping.split(",")
        students.append(mapping)
    f.close()
    return students

# Question 6
print('Testing read_response_file')
data = read_response_file('cmpt181_midterm.txt')
print(data[0:3])

def write_score_file(output_name,response_db):
    """
    This function takes writes to a text file the student ID, Name and score of the student
    :param output_name: the filename you wish to give to your text file, needs the file type (.txt etc)
    :param response_db: Dictionary containing the student id as the key, the name as a sub-key 'Name' and score as a sub-key 'Score'
    :return: Function doesn't return anything but creates a new text file with the output_name as the file name
    """
    f=open(output_name,'w')
    for r in response_db:
        f.write(str(r)+','+response_db[r]['Name']+','+str(response_db[r]['Score'])+'\n')
    f.close()


# Question 7
print('Testing write_score_file')
answers = index_responses(['a','b','c','b'])
response_db = index_class([['123','foo', 'a','b','c','a'],
                           ['234','bar', 'a','b','c','b'],
                           ['345','xyzzy','a','a','c','b']])
grade(answers,response_db)
#write_score_file('score_file_example.txt', response_db)

def get_answers(list_name):
    """
    This function takes the answer key from the first line and then deletes the row from the list of ID, Name and responses
    :param list_name:The name of the list to process
    :return:Function returns a list of only the answers not the place holder name or ID
    """
    answers=(list_name[0][2:])
    list_name.remove(list_name[0])
    return answers


def print_socres_report(number_of_questions,list_of_scores):

    print("*****Scores summary*****")
    print("Number of sutdents: ",str(len(list_of_scores)))
    print("Number of questions: ",(number_of_questions))
    print("Minium score: ",str(min(list_of_scores)))
    print("Average score: ",str(stat.mean(list_of_scores)))
    print("Median score: ",str(stat.median(list_of_scores)))
    print("Maxium score: ",str(max(list_of_scores)))

def getListOfScores(dic_of_students):
    """
    This function will collect the scores of every student into a list from a correctly build dictionary
    :param dic_of_students: The dictionary containing the name,ID, responses and score of a sutdent as value and student
    ID as key
    :return: returns a list of scores
    """
    list_of_scores=[]
    for r in dic_of_students:
        list_of_scores.append(dic_of_students[r]['Score'])
    return(list_of_scores)

def plot(list_of_scores):
    mat.hist(list_of_scores,histtype='barstacked',bins=len(list_of_scores))
    mat.xlabel("Score")
    mat.ylim(0,5)
    mat.ylabel("Number of students")
    mat.title("Score assosiated with number of students")
    mat.show()





print("")
print("")
print("")
print("")
response_list=read_response_file("cmpt181_midterm.txt") #Read the data from the file and store it in response_list
first_row=index_student(response_list[0])   #Take the first row of the list and make it into a dictionary and save it for later
answer_sheet=get_answers(response_list)     #Delete the first row from response_list and remove useless info from it and store the answer sheet into answer_sheet
response_list=index_class(response_list)       #Make the response_list into a correctly built dictionary
answer_sheet=index_responses(answer_sheet)      #Make the answer_sheet into a correctly built dictionary
grade(answer_sheet,response_list)  #The dictionaries must exist before putting them into the grade function because it doesn't return anythign
list_of_scores=getListOfScores(response_list)   #Take the dictionary response_list and create a new list only consisting of scores from it
print_socres_report(len(first_row['Responses']),list_of_scores)    #Print the summary from the test
plot(list_of_scores)    #Plot the data into a histograph
write_score_file("cmpt181_scores.txt",response_list)   #Write the student's name, student ID and score into a new text file





