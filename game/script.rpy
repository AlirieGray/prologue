# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define y = Character(_("Yeni"), color="#5a0ee7")
define a = Character(_("Azem"), color="#006300")
define u = Character(_("??"), color="#006300")
define t = Character(_("Tam Un"), color="#98f8ff")


# The game starts here.

label start:
    scene bg_village
    show yeni at left

    "The last bands of orange light have given way to blackness on the horizon, and the sounds of the village have died down as people retire for the night."

    "Guess that means it’s time to go." 

    "I swaddle Arizet in more layers than I normally would and wrap her tight to my body before putting on a thick cloak over both of us." 

    "It isn’t very cold this far north, even at night, but the farther we get from the coast and the closer to the mountains, the more harsh and biting the air will be. Even though it will be midday by the time we come in view of the mountains."

    "Arizet is unnaturally silent for an infant, and far too pale. She doesn’t make a noise as I slip out of the house and make my way to the edge of the village."

    "I’m almost through the pastures that form a ring around the village when I hear someone call my name."

    u "Yeni!"

    "Shit."

    "I turn to see Azem, one of the young shepherd boys, jogging up the hill towards me."

    show azem neutral at right

    a "What are you doing out this late, Auntie? I didn’t expect to see anyone else up."

    "I have to come up with something convincing, or he’ll think I’m running away and stop me. And I certainly can’t tell him where I’m really going."

    menu:

        "What do I tell him?"

        "Make something up":

            jump lie

        "Flip the question on him":

            jump flip


label lie:

    y "It’s the first full moon after my daughter’s birth. In my own–"
    
    y "I mean, in the clan I was born into, there’s a ritual you’re supposed to do on this day."

    "It’s only partially a lie."

    a "Oh, I see. For good luck, you mean?"

    y "Yes."

    "That’s definitely not what the ritual is for, but he doesn’t need to know that. Either way, the explanation seems to satisfy him."

    a "Well, be safe out there, Auntie. Are you sure you wouldn’t like someone to escort you?"

    y "No, it has to be me alone. Give my greetings to your parents for me, would you?"

    "I hurry off before he has the chance to ask any more questions." 

    jump main_branch


label flip:
    y "That’s my business. What are you doing up so late, Azem? Surely all the sheep have been returned to the pen by now?"

    show azem abashed at right

    a "I, um… may have lost one." 

    show azem happy at right

    a "But not to worry! I am sure I can find her before dawn."

    y "I’m sure you can. Better go before she gets too far." 

    show azem neutral at right

    a "Of course, Auntie. Don’t worry, I’ll have her back before anyone even notices she was missing. No sheep are getting eaten on my watch!"

    "He makes a quick bow before departing, hurrying past me into the night."

    scene bg_village
    show yeni at left
    
    "He doesn’t look back at me as I continue south, walking until the village is out of sight."

    jump main_branch

label main_branch:

    "It could have been real bad if he had thought I was leaving for good."

    "Azem is a good kid, but his first duty is to the clan. "

    "I’ve lived here seven years, since my parents arranged for my marriage, to strengthen blood ties between our clans. Seven years since I became Yeni tl’Anak, instead of Yeni tl’Un."

    "I thought about leaving often in the first year I lived here. I felt alone, frightened." 

    "But then I had my son. Since then, I never fantasized about leaving."

    "Even when he was kidnapped and taken to the city, I couldn’t leave. I had friends by then who had suffered the same loss."

    "Though they didn’t know why, every few years a company of soldiers would ride in from the city, taking a group of children between the ages of four to seven with them."

    "It happened to the neighboring villages, too. And though they all lived in fear of it happening to their own children, their roots were too deep in the land for them to leave." 

    "They weren’t like my own clan, wandering from pasture to pasture, and from oasis to oasis, carrying all of their belongings on their horses and their carts."

    "And I wasn’t either, I had to admit. I had planted roots, too." 

    "I walked until the sun began to rise, following the arc of the Hunter's Bow south."












    # This ends the game.
    return
