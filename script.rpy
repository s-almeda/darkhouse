# comments that don’t affect the code start with this # symbol!
# Declare characters used by this game.
init:
    #1024x768
    $ playerName = "You"
    $ pmName = "Middle-aged Woman"
    $ hsName = "Teenage Boy"
    $ ppName = "Little Girl"
    
    
    
    #(cps = text speed for each character)
    $ mc = DynamicCharacter("playerName", color="#006400", what_prefix= "{cps=60}\"", what_suffix = "\"", window_left_padding = 175, image = "mc",)
    $ pm = DynamicCharacter("pmName", color="#800000", what_prefix= "{cps=50}\"", what_suffix = "\"")
    $ hs = DynamicCharacter("hsName", color="#A64CA6", what_prefix= "{cps=50}\"", what_suffix = "\"")
    $ pp = DynamicCharacter("ppName", color="#FFFFFF", what_prefix= "{cps=50}\"", what_suffix = "\"")
    #$ pp.what_font = "font.ttf"


    
    
    $ pm_points = 0
    $ hs_points = 0
    $ c_points = 0
    $ other_points = 0




# Declare images below this line, using the image statement.
# EXAMPLE IMAGE STATEMENT:
# image eileen happy = "eileen_happy.png"
#*****************
# HEY FRIENDS! if you haven't already, download the zip file called
# PLACEHOLDER IMAGES and unzip all the images in that file to your 
# "game" folder in order to run the game with placeholder images!!
#******************




#### BACKGROUND IMAGES ####
    image bg lhTrapdoor = "trapdoor.jpg"
    image bg lhWindow = "window.jpg"
    image bg lhLight = "light.jpg"
    image bg stairs1 = "stairs1.jpg"
    image bg stairs2 = "stairs2.jpg"
    image bg stairs3 = "stairs3.jpg"
    image bg sideroom = "sideroom.jpg"
    image bg bottomFloor = "bottomfloor.jpg"
    image bg lock = "lock.jpg"
    image bg goodEnding = "goodending.jpg"
    image bg okayEnding = "okayending.jpg"
    
    image bg black = "#000"
    image bg red = "#FF0000"
    
##### TRANSITIONS: ######
    define slowDissolve = Dissolve(1.0)




##### CHARACTER IMAGES #####
    image side mc neutral = "mcNormal.jpg"
    image side mc happy = "mcHappy.jpg"
    image side mc shock = "mcShock.jpg"
    image side mc sad = "mcSad.jpg"
    image side mc angry = "mcAngry.jpg"
    
    image pm normal = "pmNormal.png"
    image pm happy = "pmHappy.png"
    image pm shock = "pmShock.png"
    image pm sad = "pmSad.png"
    image pm angry = "pmAngry.png"
    
    image hs normal = "hsNormal.png"
    image hs happy = "hsHappy.png"
    image hs shock = "hsShock.png"
    image hs sad = "hsSad.png"
    image hs angry = "hsAngry.png"
    
    image pp normal = "ppNormal.png"
    image pp happy = "ppHappy.png"
    image pp shock = "ppShock.png"
    image pp sad = "ppSad.png"
    image pp angry = "ppAngry.png"



# The game starts here.
label start:

    jump Introduction

label Example:
    show bg black
    centered "The Beginning"
    mc "..."
    show bg lhLight with slowDissolve
    narrator "You are in a lighthouse." with dissolve

    #I copy pasted all of Sarah’s coding so thank her for the example coding, she da best <33333
    
    menu:
        narrator "What do you say?"
    
        "\"I say First choice\"":
            mc "First choice"
            show hs happy at left
            hs "Remember to copy paste these straight quotes when writing dialogue"
            hs "I am creepily happy about this deranged situation!"
            show pm happy at right
            hs "I am an amazing anime mom until you ask about me about my baby!"
            show pp happy at right
            hs "I am a ghost who is trying to detective solve and pretend that I can only speak Russian! Help me solve the mystery so I can pass on!"
        
        "\"I say Second choice\"":
            mc sad "Second choice"
            show hs happy
            hs "I can’t feel my fingers :D But I am so happy to have friends!"
            #We should decide what way the baby is in pieces for best creep factor!
            #I copy pasted all of Sarah’s coding so thank her for the example coding, she da best <33333
            #This is probably one of the few times we’ll ever see all of the happy character sprites at once! hahahaha
    
    mc "I am now saying the thing that will always be said after the choice dialogue finished! Back to the main plotline and conversation guys!"
    
    #I am going to add a comment here for examples!
    
    hs "What’s your name protag? Ie how to let the player input text!"
    
    $ playerName = renpy.input("What is your name? ")
    if playerName == "":
        $playerName = "default"
    
    
    mc "My name is %(playerName)s."
    
label Introduction:
    show bg black
    centered "The Beginning" 
    mc angry "The record ends here, but-"
    mc " - he was definitely onto something."
    mc "These implications, they don’t make any sense."
    mc "It must be because I can’t think straight anymore.{p} I need sleep."
    narrator "You yawn."
    mc neutral "What time is it? 5 am."
    narrator "You feel yourself nodding off."
    mc "I think… I’ll continue in the morning…"
    mc "zzZZZzzZZZ"
    show bg black
    narrator "You shiver."
    mc angry "{size=-5}mooOOOom…{p} I told you to stop leaving the window open{/size}"
    narrator "You try pulling the blanket closer in an attempt to shut the world out."
    narrator "You grab air and end up clawing at the wooden floor instead."
    mc neutral "………"
    narrator "The smell of seawater and dust hits you in the face."
    mc shock "Wha?!?"
#### ~change "This isn’t home." later~ ####
    show bg lhLight with slowDissolve
    narrator "You are in a lighthouse!" with dissolve
    
    
    menu:
        narrator "What do you say?"
        
        "\"Huh, where am I?!\"":
            mc shock "Where am I?!"
            show hs happy at left
            hs "Is there somebody else here?"
            hs "Thank goodness!{p} I’m happy to see another friendly face!"
            $ hs_points += 1
            
            
        "\"Who brought me here? Show yourself!\"":
            mc shock "Who brought me here?{p} Show yourself!"
            show hs angry at left
            hs "Where do you get off introducing yourself like that!"
            $ hs_points -= 1
            mc "Oh? So you didn't kidnap me?"
            hs "No! I went to bed last night and woke up here."
            mc neutral "Oh..."
    
    show pm normal at right
    pm "SHHHHHHH! YOU'LL WAKE UP MASON!"
    
    ###some plot transition here?###
    
    show hs normal at left
    show pm normal at right
    hs "So, who are all of you?"
    
    $ playerName = renpy.input("What is your name? ")
    if playerName == "":
        $playerName = "Kris"
    
    
    mc "I'll go first. I'm %(playerName)s. {p} I'm an aspiring detective."
    mc "While I'm at it, mind if I take notes? {p} It could help us figure out why we're here and how to get out."
    hs "I'm cool with it."
    pm "Yes. That's fine, sweetheart."
    mc happy "My father used to solve all these cases. It was really cool, and I wanted to be just like him."
    
    show pm happy at right
    
    pm "That's wonderful! Are you going to work alongside your dad?"
    
    show hs shock at left
    show pm sad at right
    
    mc sad "No, he's dead now..."
    hs "Oh, my gosh…{p} I'm so sorry."
    pm "Me too! If I had known, I wouldn't have brought it up.{p} My sincerest apologies!"
    mc neutral "It's fine. Let's continue with the introductions, okay?"
    
    show hs normal at left
    show pm normal at right
    
    $ hsName = "Maximillian"
    hs "Got it. {w} 'Sup, I'm %(hsName)s."
    ### more introduction for Maximillian
    $ pmName = "Grace"
    pm "Hello, darlings! You can just call me %(pmName)s.{p} Oh! And this here is Mason!"
    pm "{size=-5}We should talk quietly, though.{w} He's sleeping.{/size}"
    
    
    
    jump Event1



label Event1:
    
    mc "Now we have to decide..."
    
    ## CHOICE 1 ##
    
    menu:
        "this choice leads to a bad ending lol":
            "wow you're dumb"
            "literally so stupid"
            jump BadEnding1
            ## BAD ENDING 1 ##
        "this choice gives you some points maybe i guess":
            "you make the second decision"
            mc "maybe we could stick a puzzle in here?"
            "stop breaking the 4th wall"
            $ pm_points +=1 ## THIS IS HOW YOU ADD POINTS
            $ hs_points += 2 ## EXAMPLE 2
            
           
            
    ## CHOICE 1 OVER ##
   
    mc "well its a good thing we didn't get a bad ending there"
    
    ## CHOICE 2 ##
    
    menu:
        " stick your hand in or something. this choice gives you a character1 point.":
            $ pm_points +=1
            "you stick your hand in or something. like a bawss"
            
        "this choice doesn't gives you a character 2 point":
            $ hs_points +=1
            "yay"
            
        "this choice gives you a character 2 and 3 point idk":
            $ hs_points +=1
            $ c_points +=1
            "yay!"
            "woot"
            
            
        "this choice gives you a character 1 and 2 point":
            $ pm_points +=1
            $ hs_points +=1
            "AYOOO"
            "yay"
            
            
        "this choice does nothing you fool":
            mc "why did i pick this"
            
    ## CHOICE 2 OVER ##
    
    jump Event2
    
    
## EVENT 2 ##




label Event2:
    "event2"
    jump Event3
    
    
## EVENT 3 ##



label Event3:
    "event3"
    if pm_points >= 1 and hs_points >=1:
        jump bestending
    elif pm_points >=1 or hs_points >=1:
        jump okayending
    else:
        jump BadEnding3
        
        
        
###************###
### END GAME ###
###************###






label bestending:
    "you got the best ending!"
    return
    
label okayending:
    "you got the okay ending"
    return
    
label BadEnding1:
    "you got bad ending 1 dummy"
    return
    
label BadEnding3:
    "you got the bad ending betch"
    return
   
  
