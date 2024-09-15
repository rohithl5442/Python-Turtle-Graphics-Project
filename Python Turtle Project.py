
# Turtle lab 5 


#Created by:         # Rohith Suresh


#Date created 04/29/2022


'''Program Summary :    This program  will basically mimic a bored turtle who decides to go on vacation. It has been
                        given two options whether to move to California or Washington. If it chooses California the map will
                        choose the location and picks a place near the mountain area. Then it builds a house and a 
                        Christmas tree and spends some time there. If it chooses Washington, it'll go to a small town somewhere 
                        in washington and builds a house there. It plants trees around it's house and enjoys the sunny weather 
                        among the shades of the trees it planted. Then it gets a chance to see some amazing rainbow 
                        in the evening and then spends the whole night gazing at the moon and the stars around its house.'''    









######################################################### ~~~~* CODE *~~~~ ###############################################################################

# import functions in turtle

import turtle as t #importing turtle as t
import random      #importing random to create random numbers needed for specific function
import time        #importing time to make the screen stay awake for some seconds 
import math        #importing math to do some math caluclations in the functions



#page setup
t.setup(1200,900)
t.speed(0)
sc = t.Screen()
t.hideturtle()
t.shape("turtle")
t.bgcolor("dark cyan")
t.pencolor("orange")
t.pensize(10)
t.penup()
t.goto(-60, 200)
t.write("      Story of a bored Turtle 🐢", align="center", font=("Century", 50, "bold"))
t.goto(0, -100)
t.shape("turtle")
t.fillcolor("red")
t.shapesize(14, 14, 1)
t.left(90)
t.showturtle()
time.sleep(5)
t.reset()







def usamap(): # function usamap is defined
  t.speed(1000)

  answer=str()
  destination = str()
  destination2 = str()
  answer=input("Do you wanna go travelling:  ") #input


  if answer=="yes":                             #IF statement & output

      t.speed(10)
      t.bgcolor("dodger blue")
      t.fillcolor("sandy brown")

      

      t.penup()
      t.goto(-350,290)
      t.pendown()

      t.begin_fill()
      t.goto(100,250)
      t.circle(-50,50)
      t.goto(150,170)
      t.circle(-50,80)

      for i in range (0,9):
          t.circle(20,20)
      t.goto(280,270)
      for i in range (0,12):
          t.circle(-5,10)
      t.goto(300,220)
      for i in range (0,5):
          t.circle(-5,10)

      t.goto(295,180)
      t.goto(290,120)
      t.goto(285,80)

      t.goto(250,0)

      for i in range (0,3):
          t.circle(30,20)

      t.goto(270,-80)

      for i in range (0,3):
          t.circle(-30,20)
      t.goto(220,-180)
      for i in range (0,3):
          t.circle(30,20)
      t.forward(80)
      for i in range (0,9):
          t.circle(-30,20)
      t.forward(200)
      for i in range (0,5):
          t.circle(10,10)
      t.forward(70)
      t.left(45)
      t.forward(60)
      t.right(30)
      t.forward(70)
      for i in range (0,3):
          t.circle(30,20)
      t.forward(70)
      t.right(75)
      t.forward(50)
      t.right(60)
      t.forward(90)
      for i in range (0,6):
          t.circle(20,20)
      t.right(90)
      t.forward(70)
      for i in range (0,3):
          t.circle(30,30)
      t.right(110)
      t.forward(200)
      for i in range (0,4):
          t.circle(-30,20)
      t.goto(-350,290)

      t.end_fill()
      
      
      desination=input("Where do you wanna go? (California/Washington) ")  #input

      if desination=="California":                                         #output
            t.speed(0)
            t.penup()
            t.hideturtle()
            


            

            # Creating a module which will show the welcome screen of the story. ~ 
            
            def welcome_screen():
                t.bgcolor("goldenrod")
                t.hideturtle()
                time.sleep(3)
                t.goto(0, 0)
                t.write("He has decided to move to the mountains in California 🏔 🌲", align="center", font=("Century", 20, "bold"))
                time.sleep(3)
                t.reset()

            # Creating a module for drawing base of the tree. ~ 

            def tree_base():
                t.penup()
                t.goto(0,0)
                t.pendown()
                t.color("chocolate")
                t.right(90)
                t.pensize(60)
                t.penup()
                t.forward(100)
                t.pendown()
                t.forward(200)

            # Creating a module for drawing 3 mountains for the beautiful scene.  ~   

            def mountain_view():
                t.bgcolor("sky blue")
                # Left Mountain
                t.speed(5)
                t.penup()
                t.goto(-320, -308)
                t.pendown()
                t.color("dimgray")
                t.begin_fill()
                for i in range(3):
                    t.forward(300)
                    t.left(120)
                t.end_fill()

                # Right Mountain
                t.penup()
                t.goto(0, -308)
                t.pendown()
                t.begin_fill()
                for i in range(3):
                    t.forward(300)
                    t.left(120)
                t.end_fill()

                # Middle Mountain
                t.penup()
                t.goto(-260, -308)
                t.pendown()
                t.color("gray")
                t.begin_fill()
                for i in range(3):
                    t.forward(400)
                    t.left(120)
                t.end_fill()
                t.hideturtle()

            # Creating a module named draw_tree() which will draw the tree using a Tuple of position. ~ 

            def draw_tree():                                                   #CREATED USING TUPLES/LISTS
                branch_position = ((50, 20), (80, 0), (120, -30), (150, -60))
                for size,top in branch_position:    # turtle creating Christmas tree
                    t.color("forest green")
                    t.penup()
                    t.begin_fill()
                    t.goto(0, top)
                    t.pendown()
                    t.penup()
                    t.goto(size, top-size)
                    t.pendown()
                    t.penup()
                    t.goto(-size, top-size)
                    t.pendown()
                    t.penup()
                    t.goto(0, top)
                    t.pendown()
                    t.end_fill()

            # Creating a module for drawing a line for the ground. ~ 

            def draw_line():
                t.penup()
                t.left(90)
                t.goto(-450, -320)
                t.pendown()
                t.pensize(25)
                t.pencolor("teal")
                t.forward(950)
                t.hideturtle()
                time.sleep(3)

            # Creating a module that builds the house ~ 

            def build_house():
                side = 125    
                roof = math.sqrt(side**2 / 2)
                t.speed(100)
                t.penup()
                t.goto(300,-308)
                t.showturtle()
                t.fillcolor("chocolate")
                t.begin_fill()
                t.forward(side)
                t.left(90)
                t.forward(side)
                t.left(90)
                t.forward(side)
                t.left(90)
                t.forward(side)
                t.left(90)
                t.end_fill()
                t.forward(side)
                t.left(90)
                t.forward(side)
                t.pendown()
                t.end_fill()
                t.penup()
                t.fillcolor("olive")
                t.begin_fill()
                t.left(45)
                t.forward(roof)
                t.left(90)
                t.forward(roof)
                t.left(90)
                t.pendown()
                t.end_fill()
                windows()
                time.sleep(3)

            # Creating a module that draws windoes of the house     ~ 

            def windows():
                t.penup()
                t.goto(325, -280)
                for x in range(2):
                    t.fillcolor("black")
                    t.begin_fill()
                    t.left(45)
                    t.forward(20)
                    t.left(90)
                    t.forward(35)
                    t.left(90)
                    t.forward(20)
                    t.left(90)
                    t.forward(35)
                    t.end_fill()
                    t.goto(380, -280)
                    t.left(45)
                t.hideturtle()

            # Creating a module for drawing the Sun ~ 

            def draw_sun(radius, pen_size, pen_color):
                t.speed(200)
                t.hideturtle()
                t.penup()
                t.goto(300,200)                
                t.fillcolor("red")
                t.begin_fill()
                t.circle(radius)
                t.end_fill()
                t.pendown()
                t.pensize(pen_size)
                t.pencolor(pen_color)


                for i in range(9):
                    t.speed(200)
                    t.right(90)
                    t.forward(40)
                    t.back(40)
                    t.left(90)
                    t.circle(radius, 40)

                t.penup()
                t.hideturtle()

            # Creating a module for taking the turtle for sun bathing 

            def resting_inHome():
                t.penup()
                t.fillcolor("darkgreen")
                t.shape("turtle")
                t.shapesize(2, 2, 1)
                t.showturtle()
                t.speed(1)
                t.goto(215, -300)
                t.right(135)
                
            # Creating a module for the end message. 

            def write_endmessage():
                userInput = "Welcome to my World!"
                t.penup()
                t.goto(-200, -400)
                t.pencolor("black")
                t.pendown()
                t.write(userInput, font = ("Century", 30, "bold"))   

            # Selecting California region from Usa map. ~ 

            def california():
                t.speed(10)
                t.bgcolor("dodger blue")
                t.fillcolor("sandy brown")
                t.penup()
                t.goto(-407,150)
                t.pendown()

                t.fillcolor('green')
                t.begin_fill()
                t.right(45)
                t.forward(60)
                t.right(90)
                t.forward(70)
                t.left(45)
                t.forward(100)
                t.right(45)
                t.forward(60)
                t.right(90)
                t.forward(85)
                t.right(52)
                t.forward(150)
                for i in range (0,4):
                    t.circle(-20,20)
                t.forward(80)
                t.end_fill()

                t.penup()
                t.goto(0,0)
                t.pendown()

                t.shape('turtle')

                t.fillcolor('green')

                t.goto(-380,0)

                t.write('Hurray, I am in California', align="center", font=("Century", 30, "bold"))
                t.penup()
                t.goto(-60, 350)
                t.write("Map of USA 🇺🇸 ", align="center", font=("Century", 30, "bold")) 
                t.hideturtle()
                time.sleep(4)
                t.reset()
                
            # defining funcion call_california that calls all the functions in the program ~     
            def call_california():

                
                # Calling welcome screen- 
                california() 

                welcome_screen()
                
                # Draw mountains for a nice mountain_view- 
                mountain_view()

                # Calling tree_base module- 
                tree_base()

                # turtle creating Christmas tree- 
                draw_tree()
                    
                # Drawing baseline- 
                draw_line()

                # Building a beautiful house next to the tree- 
                build_house()

                # turtle drawing the Sun- 
                draw_sun(90, 2, "red")

                # End message- 
                write_endmessage()

                # After a long tiring day, Mr. turtle wanted to enjoy the day- 
                resting_inHome()

            # function call_california calls every other function inside the if statement     
            call_california()
            

            time.sleep(5)
          
############################################################## * CODE ENDS* ######################################################################
            
            

      ####################  CODE ##########################
      elif desination == "Washington":


          #page setup
            t.setup(1200,900)
            t.speed(500)
            sc = t.Screen()
            
            
            # Selecting California region from Usa map. ~ 

            def washington():

                t.speed(10)
                t.bgcolor("dodger blue")
                t.fillcolor("sandy brown")
                t.penup()
                t.goto(-423,150)
                t.pendown()

                t.fillcolor('green')
                t.begin_fill()
                t.right(45)
                t.forward(80)
                t.left(10)
                t.forward(60)
                t.left(90)
                t.forward(30)
                t.right(45)
                t.forward(5)
                t.left(45)
                t.forward(10)
                t.right(45)
                t.forward(25)
                t.left(45)
                t.forward(10)
                t.left(45)
                t.forward(10)
                t.right(5)
                t.forward(20)
                t.left(45)
                t.forward(30)
                t.left(2)
                t.forward(40)
                t.right(80)
                t.forward(10)
                t.left(90)
                t.forward(11)
                t.goto(-423,150)
                t.end_fill()

                t.penup()
                t.goto(0,0)
                t.pendown()

                t.shape('turtle')

                t.fillcolor('green')

                t.goto(-350,180)

                t.write('Hurray, I am in Washington', align="center", font=("Century", 30, "bold"))
############################################################## * CODE ENDS* ##############################################################################                



########################################################### ~~~*  CODE BEGINS *~~~ #######################################################################
                
                t.penup()
                t.goto(-60, 350)
                t.write("Map of USA 🇺🇸 ", align="center", font=("Century", 30, "bold")) 
                t.hideturtle()
                time.sleep(3)
                t.reset()
                
            # Creating a welcoming screen for the turtle when he chooses to go to Washington. ~ 

            def welcome_screen2():
                t.hideturtle()
                t.shape("turtle")
                t.bgcolor("steel blue")
                t.pencolor("orange")
                t.pensize(10)
                t.penup()
                t.goto(-60, 200)
                t.write("\tIf the turtle went to Washington 🐢", align="center", font=("Century", 50, "bold"))
                t.goto(0, -100)
                t.shape("turtle")
                t.fillcolor("red")
                t.shapesize(14, 14, 1)
                t.left(90)
                t.showturtle()
                time.sleep(3)
                t.reset()

                t.hideturtle()
                time.sleep(3)
                t.goto(0, 0)
                t.write("He'll move to the Small Towns 🏡 🌈 🌳 ", align="center", font=("Century", 50, "bold"))
                time.sleep(3)
                t.reset()
    
            # Creating a beautiful blue sky with some green grass. ~ 

            def sky():
                t.speed(1000)
                
                #sky 
                t.bgcolor("deep sky blue")
                

                #grass
                t.penup()
                t.goto(-800, -250)
                t.pendown()
                t.color("green")
                t.begin_fill()
                for i in range(2):
                    t.forward(1700)
                    t.right(90)
                    t.forward(300)
                    t.right(90)
                t.end_fill()

            # Creating a shiny yellow sun in the mid afternoon. ~  

            def sun():
                t.speed(1000)
                t.penup()
                t.goto(400,225)
                t.pendown()
                t.color("yellow")
                t.begin_fill()
                t.circle(50)
                t.end_fill()
                t.hideturtle()
                for i in range(9):
                    t.speed(200)
                    t.right(90)
                    t.forward(40)
                    t.back(40)
                    t.left(90)
                    t.circle(50, 40)

            # Creating a night time grass when the background is black. ~       

            def nightgrass():
                t.speed(1000)

                #grass
                t.penup()
                t.goto(-800, -250)
                t.pendown()
                t.color("green")
                t.begin_fill()
                for i in range(2):
                    t.forward(1700)
                    t.right(90)
                    t.forward(300)
                    t.right(90)
                t.end_fill()
            
            # Creating an evening sun with some orange look to it before it sets. ~ 

            def sun2():
                t.pensize(5)
                t.speed(10)
                t.penup()
                t.goto(400,225)
                t.left(54)
                t.pendown()
                t.color("orange red")
                t.begin_fill()
                t.circle(50)
                t.end_fill()
                t.hideturtle()
                
                for i in range(9):
                    t.speed(10)
                    t.right(90)
                    t.forward(40)
                    t.back(40)
                    t.left(90)
                    t.circle(50, 40)

            # Creating an cloud in the top left with a white smoke color to math with the sun and sky. ~             

            def cloud():                    # Function created using NESTED LOOPS
                t.speed(100)
                t.penup()
                t.goto(-300, 200)
                t.color("white smoke")
                t.begin_fill()
                for i in range(0, 8):

                    for i in range (0,20):
                        t.forward(5)
                        t.left(9)
                    t.left(180 + 27)
                t.end_fill()
                t.hideturtle()
                time.sleep(3)
                t.penup()
                t.left(90)
                t.pendown()
                time.sleep(5)

            # Creating an text at the top of the screen before setting up the rainbow. ~ 

            def evening_screen():
                t.speed(0)
                t.hideturtle()
                t.shape("turtle")
                t.pencolor("black")
                t.pensize(10)
                t.penup()
                t.goto(-60, 300)
                t.write("\tWanna see some colorful rainbows? 🌈", align="center", font=("Century", 20, "bold"))
                time.sleep(3)
                t.undo()
            
            # Creating an beautiful house with windows, chimney, roof and door. ~ 

            def house():
                t.speed(1000)

                #house
                t.penup()
                t.goto(-100, -250)
                t.pendown()
                t.pensize(3)
                t.color("chocolate", "gold") 
                t.begin_fill()
                for i in range(4):
                    t.forward(170)
                    t.left(90)
                t.end_fill()

                #chimney
                t.penup()
                t.goto(20, -80)
                t.color("brown", "dim grey")
                t.begin_fill()
                for i in range(2):
                    t.forward(40)
                    t.left(90)
                    t.forward(170)
                    t.left(90)
                t.end_fill()

                #Roof
                t.penup()
                t.goto(-127, -80)
                t.pendown()
                t.fillcolor("brown")
                t.begin_fill()
                for i in range(3):
                    t.forward(225)
                    t.left(120)
                t.end_fill()
                t.penup()
                t.goto(-300, -250)
                t.pendown()

                # Window 1
                t.penup()
                t.goto(0,-150)
                t.pendown()
                t.color("black", "gainsboro")
                t.begin_fill()

                for i in range(4):
                    t.forward(50)
                    t.left(90)
                t.end_fill()

                # Window 1 horizontal
                t.penup()
                t.goto(0, -125)
                t.pendown()
                t.color("black")
                t.forward(50)

                #Window 1 cross
                t.penup()
                t.goto(25, -150)
                t.pendown()
                t.left(90)
                t.forward(50)

                t.penup()
                t.right(90)
                t.pendown()
                

                # Window 2
                t.penup()
                t.goto(0,-240)
                t.pendown()
                t.color("black", "gainsboro")
                t.begin_fill()

                for i in range(4):
                    t.forward(50)
                    t.left(90)
                t.end_fill()

                # Window 2 horizontal
                t.penup()
                t.goto(0, -215)
                t.pendown()
                t.color("black")
                t.forward(50)

                #Window 2 cross
                t.penup()
                t.goto(25, -240)
                t.pendown()
                t.left(90)
                t.forward(50)
                t.penup()
                t.right(90)
                t.pendown()

                # Door
                t.penup()
                t.goto(-80, -243)
                t.pendown()
                t.color("dark orange")
                t.begin_fill()
                for i in range(2):
                    t.forward(60)
                    t.left(90)
                    t.forward(100)
                    t.left(90)
                t.end_fill()

                t.pencolor("black")
                t.pensize(3)
                t.penup()
                t.goto(-50, -120)
                t.write("Welcome", align="center", font=("Century", 20, "bold"))

                # Door handle
                t.penup()
                t.goto(-70, -200)
                t.pendown()
                t.color("black")
                t.begin_fill()
                t.circle(5)
                t.end_fill()

                t.penup()
                t.right(90)
                t.pendown()

            # Creating a tree near the house. ~     

            def tree():
                t.speed(1000)

                # Tree trunk
                t.color("saddlebrown")
                t.begin_fill()
                for i in range(2):
                    t.forward(40)
                    t.left(90)
                    t.forward(10)
                    t.left(90)
                t.end_fill()

                #Turning turtle around
                t.forward(10)
                t.left(90)
                t.forward(5)

                # Leaves
                t.color("dark green")
                t.begin_fill()
                t.circle(25)
                t.end_fill()
                t.right(90)

            # Planting the tree using tree() function randomly in a given location near the house. ~ 

            def plantingtrees():            # Function created using NESTED LOOPS
                t.speed(1000)

                
                y = -212

                for i in range(10):
                    x = random.randint(-500, -150)
                    t.penup()
                    t.goto(x,y)
                    t.pendown()
                    tree()              #Calling tree() function to print in left. ~ 
            
                    for j in range(1):
                        z = random.randint(150, 500)
                        t.penup()
                        t.goto(z,y)
                        t.pendown()
                        tree()          #Calling tree() function to print in right. ~ 
                    
                t.penup()
                t.left(90)
                t.pendown()

            # Creating an text at the top of the screen before setting up the night mode. ~             

            def night_screen():
                t.speed(0)
                t.hideturtle()
                t.shape("turtle")
                t.bgcolor("dark orange")
                t.pencolor("black")
                t.pensize(10)
                t.penup()
                t.goto(-60, 350)
                t.write("\tReady for Night time? 🌙 ", align="center", font=("Century", 30, "bold"))
                time.sleep(4)
                t.bgcolor("black")
                t.reset()





            # Code to draw the first full moon. ~   
            def moon1():
                t.speed(0)
                t.penup()
                t.goto(-325,200)
                t.color("gold")
                t.begin_fill()
                t.circle(50)
                t.end_fill()
                t.hideturtle()

            # Code to draw the second full moon to make it half. ~   

            def moon2():
                t.speed(0)
                t.penup()
                t.goto(-300,222)
                t.color("black")
                t.begin_fill()
                t.circle(50)
                t.end_fill()
                t.hideturtle()

            # Code to draw the random stars in the night sky. ~       

            def stars():                            # Function created using NESTED LOOPS
                t.speed(1000)
                num_stars = 0
                while num_stars < 60:
                    x = random.randint(-700, 700)
                    y = random.randint(100,500)
                    t.penup()
                    t.goto(x,y)
                    turns = 5
                    t.color("white smoke")
                    t.begin_fill()
                    while turns > 0:
                        t.forward(15)
                        t.left(145)
                        turns = turns - 1
                    t.end_fill()
                    t.pendown()
                    num_stars = num_stars + 1

                t.penup()
                t.left(90)
                t.left(190)
                t.goto(150,-250)
                t.fillcolor("red")
                t.speed(1)
                t.goto(-60, -235)
                t.showturtle()
                t.right(135)
                
                
############################################################## * CODE* #######################################################################

            # Code to draw Rainbow. ~

            def Rainbow(col, rad, val):
                t.color(col)
                t.circle(rad, -180)
                t.up()
                t.goto(val, -250)
                t.down()
                t.right(180)
                
            # Code to draw multiple Rainbows using LOOPS. ~

            def rainbow2():                 #CREATED USING LOOPS
                t.bgcolor('dark orange')
                t.penup()
                t.goto(-490, -250)
                t.right(54) 
                t.pendown()
                col = ['sky blue', 'purple', 'pink', 'indigo',
                    'blue', 'green', 'yellow', 'orange', 'red']
                t.right(36)
                t.pensize(10)
                t.speed(1000)
                
                for i in range(9):
                    Rainbow(col[i], 10*(i+48), -10*(i + 50))
                time.sleep(8)

           
 ############################################################## * CODE ENDS* #######################################################################               
                
#############################################################  CODE CONTD #######################################################################            
            
            # Defining the function called_washington that calls every other functions. ~ 

            def called_washington():

                # Calling the func washington to draw the outline in USA map. ~ Kaysar
                washington()

                # Calling the func to do set the screen for second welcome page. ~ 
                welcome_screen2()

                # Calling the func to do set the sky. ~ 
                sky()

                # Calling the func to create the sun. ~ 
                sun()

                # Calling the func to draw the house. ~ 
                house()

                # Calling the func to plant the trees. ~ 
                plantingtrees()

                # Calling the func to do set the cloud on top left. ~ 
                cloud()

                # Calling the func to do set the screen for evening time with some texts at top of the page. ~ 
                evening_screen()

                # Calling the func to do set the screen for second welcome page. ~ 
                sun2()

                # Calling the func to print beautiful rainbows in the sky. ~ 
                rainbow2()

                # Calling the func to do set the screen for night time with some texts at the top. ~ 
                night_screen()

                # Calling the func to print the full moon. ~ 
                moon1()

                # Calling the func to print another full moon to make it look half. ~ 
                moon2()

                # Calling the func to do set the grass to green for the night time. ~ 
                nightgrass()

                # Calling the func to build the house at night time once again. ~ 
                house()

                # Calling the func to plant the trees at night time once again. ~ 
                plantingtrees()

                # Calling the func to print the stars at night. ~ 
                stars()

                # Code to print the Thank You page. ~ 
                time.sleep(7)
                t.reset()
                t.bgcolor("black")
                t.pencolor("azure")
                t.pensize(10)
                t.penup()
                t.goto(-60, 0)
                t.write("   Thank you!!!", align="center", font=("style", 50, "bold"))
                t.hideturtle()
                
                

                

                #makes the last printed screen visible in the program until done.
                t.done()

            #Ending the called_washington function
            called_washington()
######################################################################## ~~~ CODE ENDS~~~ #######################################################################   

  #else function if neither California or Washington is selected. ~           
  else:
      t.write('Try again')      

# Calling func main() to run the whole program. 
def main():
    usamap() # Calling the func usamap() in main

main()       # Ending the main

t.done()

######################################################################## *END OF PROGRAM* #######################################################################   



