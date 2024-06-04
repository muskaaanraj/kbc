name = input("Enter your name: ")
print("Main Amitabh Bachchan aapka", name, "swagat karta hu is khel mein.")


questions=[
    
 ["Grand Central Terminal Park Avenue New York is the worlds",
  "largest railway station",
  "highest railway station",
  "longest railway station",
  "None of the above",1
  ],
 [
    "Entomology is the science that studies",
    "Behavior of human beings",
    "Insects",
    "The origin and history of technical and scientific terms",
    "The formation of rocks",2
 ],
 [
    "Eritrea, which became the 182nd member of the UN in 1993, is in the continent of",
    "Asia",
    "Africa",
    "Europe",
    "Australia",2
 ],
 [
 "Garampani sanctuary is located at",
 "Junagarh, Gujarat",
 "Diphu, Assam",
 "Kohima, Nagaland",
 "Gangtok, Sikkim",2
 ],
 [
 "For which of the following disciplines is Nobel Prize awarded?",
 "Physics and Chemistry",
 "Physiology or Medicine",
 "Literature, Peace and Economics",
 "All of the above",4
 ],
 [
 "Hitler party which came into power in 1933 is known as",
 "Labour Party",
 "Nazi Party",
 "Ku-Klux-Klan",
 "Democratic Party",2
 ],
 [
 "FFC stands for",
 "Foreign Finance Corporation",
 "Film Finance Corporation",
 "Federation of Football Council",
 "None of the above",2
 ],
 [
 "Fastest shorthand writer was",
 "Dr. G. D. Bist",
 "J.R.D. Tata",
 "J.M. Tagore",
 "Khudada Khan",1
 ],
 [
 "Epsom (England) is the place associated with",
 "Horse racing"
 "Polo",
 "Shooting",
 "Snooker",1
 ],
 [
 "First human heart transplant operation conducted by Dr. Christiaan Barnard on Louis Washkansky, was conducted in",
 "1967",
 "1968",
 "1958",
 "1922",1
 ],
 [
 "Galileo was an Italian astronomer who",
 "developed the telescope",
 "discovered four satellites of Jupiter",
 "discovered that the movement of pendulum produces a regular time measurement",
 "All of the above",4  
 ],
 [
 "Habeas Corpus Act 1679",
 "states that no one was to be imprisoned without a writ or warrant stating the charge against him",
 "provided facilities to a prisoner to obtain either speedy trial or release in bail",
 "safeguarded the personal liberties of the people against arbitrary imprisonment by the king's orders",
 "All of the above",4
 ],
 [
 "Exposure to sunlight helps a person improve his health because",
 "the infrared light kills bacteria in the body",
 "resistance power increases",
 "the pigment cells in the skin get stimulated and produce a healthy tan",
 "the ultraviolet rays convert skin oil into Vitamin D",4
 ],
 [
 "Gulf cooperation council was originally formed by",
 "Bahrain, Kuwait, Oman, Qatar, Saudi Arabia and United Arab Emirates",
 "Second World Nations",
 "Third World Nations",
 "Fourth World Nations",1
 ],
]
levels=[1000,2000,3000,4000,5000,10000,20000,40000,800000,1600000,320000]
money=0
for i in range (0, len(questions)):
    question = questions[i]
    print(f"yeh raha aapke screen pe prashn dhanrashi {levels[i]} ke liye")
    print(f"{question[0]}")
    print(f"a.{question[1]}              b.{question[2]}")
    print(f"c.{question[3]}              d.{question[4]}")
    reply=int(input("lock kar diya jaaye!"))
    if(reply==question[-1]):
        print(f"mubarak ho aap jeet gaye hai dhanrashi{levels[i]}")
        if(i==4):
            money==10000
        elif(i==9):
            money==320000    
    else:
        print("galat jawab")
        break            
print(f"Aap kya kariyega iss dhanrashi ka {money}") 
jawab=input("yaha bataye: ")  