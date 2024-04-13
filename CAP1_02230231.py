#######################################
#Ugyen Wangchuk
#1-ICE
#02230231
######################################
#REFERENCES
#https://www.studytonight.com/python-projects/python-game-rock-paper-scissors
#https://realpython.com/lessons/rock-paper-scissors-overview/
######################################
#SOLUTION
#My solution score is: 50055
######################################
def read_input(inputting): #defines the function "read_input" that takes a filename (inputting) as input.
    games_played = [] #storing the game_played in an empty list
    with open(inputting, 'r') as py_file: #Opening the file in read mode ('r') and assigns it to the variable py_file and it iterates over each line
        for line in py_file: 
            outline, result_declared = line.strip().split() # splits the line into outline and result_declared
            games_played.append((outline, result_declared)) #it appends a tuple containing outline and result_declared to the list games_played.
    return games_played       #Returns the list games_played containing all the data from the file.                      

def score_calculation(games_played):    #It defines a function named score_calculation that takes a list of tuples (games_played) as input.       
    points = 0         #Initializing score to zero(0)                
    for outline, over_view in games_played: #Iterates through each tuple in games_played.
        if outline == "A":    #determinng the score for the current outline and outline_points               
            if over_view == "X":            
                outline_points = 3            
            elif over_view == "Y":          
                outline_points = 4            
            else:                          
                outline_points = 8    

        elif outline == "B":                 
            if over_view == "X":            
                outline_points = 1             
            elif over_view == "Y":          
                outline_points = 5            
            else:                         
                outline_points = 9           
        

        else:                           
            if over_view == "X":           
                outline_points = 2             
            elif over_view == "Y":        
                outline_points = 6           
            else:                           
                outline_points = 7          


        points += outline_points #calculates the final score 
    
    return points  #returns the total points             
inputting = "input_1_cap1.txt"   #Defines the filename (inputting) as "input_1_cap1.txt".
games_played = read_input(inputting)   #Calls the read_input function with the filename to get the data from the file.
overall_outline_points = score_calculation(games_played)  #Calls the score_calculation function with games_played to calculate the total score
print("Total Score:", overall_outline_points)    #Prints the overall_outline_points