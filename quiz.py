def menu():
    print("Select an option")
    print("1.Start")
    print("2.Quit")
    n=input("Enter your option number:")
    if(n=="1"):
        return Start()
    elif(n=="2"):
        print("You are exiting from the quiz")
        return None
    else:
        print("Invalid option, again select")
        return menu()
def Start():
    t=input("Enter your name:")
    levels(t)
    return 0
def levels(t):
    print("1.Easy")
    print("2.Medium")
    print("3.Hard")
    r=input("Enter your level number:")
    if(r=="1"):
        return Easy(t)
    elif(r=="2"):
        return Medium(t)
    elif(r=="3"):
        return Hard(t)
    else:
        print("Invalid Selection, again select properly")
        return levels(t)
def Easy(t):
    q=[
      {"question":"What is the national animal of India?","answer":"Tiger"},
      {"question":"What is the national bird of India?","answer":"Peacock"},
      {"question":"What is the name of India's currency?","answer":"Rupees"},
      {"question":"What is the national sport of India?","answer":"Hockey"},
      {"question":"What is the national song of India?","answer":"Vande Maatram"}
    ]
    return quiz(q,t)
def Medium(t):
    q=[
      {"question":"Which river is the longest in India?","answer":"Ganges/Ganga"},
      {"question":"Who was India's first prime minister?","answer":"Jawaharlal Nehru"},
      {"question":"Which state in India is known as 'Land of five rivers'?","answer":"Punjab"},
      {"question":"Name the major mountain range near India.","answer":"Himalayas"},
      {"question":"In which year did India got independence?","answer":"1947"}
    ]
    return quiz(q,t)
def Hard(t):
    q=[
      {"question":"What is the name of the highest peak of India?","answer":"Kanchenjunga"},
      {"question":"Which river is the lifeline for southern India?","answer":"Kaveri"},
      {"question":"Who is the author of India's national epic,The Ramayana?","answer":"Valmiki"},
      {"question":"Who is the chairman of Rajya Sabha?","answer":"President"},
      {"question":"What is the name of India's central bank?","answer":"RBI"}
    ]
    return quiz(q,t)
def quiz(q,t):
    score=0
    for item in q:
        print(item["question"])
        p=item["answer"]
        n=input("Enter your answer:")
        if(n.strip().lower()==item["answer"].lower()):
            print("Correct answer")
            score=score+1
        else:
            print("Incorrect answer, The correct answer is {}".format(p))
            score=score-0
    print("Congratulations {}, The quiz is over and your final score is {}".format(t,score))

menu()
            
        
