import turtle
import time

#Hello there Diffy02, if you are reading this, then there is a chance you are looking back at your old codes and want to know how this class works
#Don't worry, I'll be giving you the explanation you need!

#The dash class works is whenever the user presses a certain key, the padel will multiply its speed for a split second,
#Before going off cool down again.
class DashSystem:
    def __init__(self, duration=0.25, cooldown=2, multiplier=5): #This is the constructor for the attributes of the dash system.
        self.duration = duration #It will then be stored into these 'self'
        self.cooldown = cooldown #So that the computer would always know about these datas
        self.multiplier = multiplier

        self.is_dashing = False #Booleans that are switches towards the functions that are inside this class.
        self.is_cooling = False #Both of them are set to false
        self.dash_start_time = 0 #These 2 variables will hold the timer for the duration
        self.cooldown_start_time = 0 #And the cooldown.

        self.indicator = turtle.Turtle() #This turtle is to indicate the user whether the dash is ready or not
        self.indicator.shape('square')
        self.indicator.color((255,255,255))
        self.indicator.penup()
        self.indicator.goto(-485,-225)

#Now, this is the hard part, so bear with me.

#There are 2 functions that holds its own timers.
#These timers will count, and doesn't stop the moment you hit the run button. (time.time())
    def trigger(self): #This function will activate some of its codes, if the user presses the key.
        current_time = time.time() #Once the run button starts, this current_time will always count
        if not self.is_dashing and not self.is_cooling: #These 2 booleans are a way to make the user not spam the dash ability.
                                                        #If the is_dashing is true and the is_cooling is true, then it would not go any further
            self.is_dashing = True #If both of them are still false, then will make the is_dashing into True
            self.dash_start_time = current_time #And the current timer will be taken if the user uses the ability, and is put inside in this dash_start_time
            #This dash_start_time will always keep its current time taken,
            #Until the function below this text has moved onto its second if() and resets its timer taken,
            #To take another time from time.time() if the function manages to pass its if() again.

#Even if this function has the same variable for the time.time() as the function above,
#It is actually different and is considered as its own timer.
#However, this current_time doesn't stop on counting.
    def update(self):
        current_time = time.time()

        #Get ready for the hard part! (I think)
        #This if() checks whether the is_dashing is true or not.
        if self.is_dashing:
            self.indicator.color((102,200,255))
            #If it is, then it would do some math down below.
            #The math works by taking the current_time from this function,
            #And subtracting the timer from the trigger function.
            #Don't forget, that the current_time in here always keep on counting.
            if current_time - self.dash_start_time >= self.duration: #If the given float is equal
                                                                     #Or more than the duration of the dash,
                self.is_dashing = False #Then it will make instantly turn the is_dashing into false,
                self.is_cooling = True #Making the cooldown boolean to true,
                self.cooldown_start_time = current_time #And starting the timer for the cooldown.
                self.indicator.color((220,55,43)) #Also changing the indicator to red

        #Oh also, this elif statement applies the same math logic as the if statement above this text.
        #But this elif reserves for the cooldown duration for the dash ability.
        elif self.is_cooling:
            if current_time - self.cooldown_start_time >= self.cooldown:
                self.is_cooling = False
                self.indicator.color((102,255,153)) #This changes the square to green

    #Finally, the if() in this function will turn on whenever the is_dashing boolean goes to true.
    def get_speed(self, base_speed):
        if self.is_dashing:
            return base_speed * self.multiplier #It multiplies the base speed to the multiplier attribute
        return base_speed #If the is_dashing is still False, then it would return the normal speed.