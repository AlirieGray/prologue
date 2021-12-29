# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define y = Character(_("Yeni"), color="#5a0ee7")
define a = Character(_("Azem"), color="#006300")
define w = Character(_("??"), color="#006300")
define u = Character(_("Urta"), color="#683904")
define t = Character(_("Tam Un"), color="#98f8ff")


# The game starts here.

label start:
    #### ACT ONE ####
    scene bg_village
    show yeni at left

    "The last bands of orange light have given way to blackness on the horizon, and the sounds of the village have died down as people retire for the night."

    "I swaddle Arizet in more layers than I normally would and wrap her tight to my body before putting on a thick cloak over both of us and strapping a travelling pack of dried food and a waterskin to my back." 

    "It isn’t very cold this far north, even at night, but the farther we get from the coast and the closer to the mountains, the more harsh the cold will be. Even though it will be midday by the time we come in view of the mountains."

    "Arizet is unnaturally silent for an infant, and far too pale. She doesn’t make a noise as I slip out of the house and make my way to the edge of the village."

    "I’m almost through the pastures that form a ring around the village when I hear someone call my name."

    w "Yeni!"

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
    y "I could ask you the same thing, Azem. Surely all the sheep have been returned to the pen by now?"

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

    "When he was kidnapped and taken to the city, I felt the same grief as when I had first been sent away from my family, like a piece of myself had been ripped out. Only worse this time." 
    
    "But I wasn't alone anymore. By then, I had friends who had suffered the same loss. They kept me alive."

    "Though no one knew why, every few years a company of soldiers would ride in from the city, taking a group of children between the ages of four to seven with them."

    "It happened to the neighboring villages, too. And though they all lived in fear of it happening to their own children, their roots were too deep in the land for them to leave." 

    "They weren’t like my own clan, wandering from pasture to pasture, and from oasis to oasis, carrying all of their belongings on their horses and carts."

    "And I wasn't the same as I had been when I left my clan, I had to admit. I had planted roots, too." 

    "I walk until the sun begins to rise, following the arc of the Hunter's Bow south."

    scene bg_steppe
    show yeni at left

    "By now, my husband will have noticed I'm gone, and will have alerted the neigbors. They'll be searching for me."

    "But they don't know the steppe as I do. I'm not worried about them finding me, even though it's slow going for me on foot and with a baby."

    "Every hour or so I pull the folds of my dress aside so Arizet can nurse, making sure the cloak is still covering her from the cold."

    "She's eating, but not enough. Her grip on life is fading, and I have to fight down a swell of panic, even as I can see the peaks of the mountains rising to meet me on the horizon."

    "I won't lose another child."

    "The air is growing cold and dry, biting the exposed skin of my face and hands. But I feel somewhat comforted by the plains of my youth."

    "I was born for these harsh lands, from a long line of herders and warriors too proud and restless to stay in one place very long."

    "I sing a travelling song under my breath, one my Auntie Urta taught me as a girl."

    "By midday, I have to stop to rest and eat."

    "I pull the pack off my back and set it on the ground. I untie the knot that holds the cloth together, turning it into a tarp to sit on and setting out the dried fruit and meat."

    "By now, Arizet should have cried to let me know her swaddling needed changing. She hasn't."

    "I peer beneath my cloak to check on her."

    "She's asleep, breathing slowly. Her skin is still a sickly pale color."

    y "Hold on, Ari. I'm taking you to someone who can help."

    "After eating the food in the pack, I shake the cloth out and wrap it around my shoulders as another layer against the cold."

    "I stand back up, and orient myself using the unique peaks of the mountains as landmarks."

    "It's easy to orient myself, it comes naturally as if I'd left home yesterday." 
    
    "Last night as I made preparations to leave, I had been worried I'd forgotten how to find my way on the steppe, and would wind up wandering until I died of thirst."

    "But that fear was far overshadowed by the fear of losing Arizet."

    "No one in the village could help me. They didn't know anything of magic, or even medicine. They had lost it all when their ancestors planted roots and began to adopt the way of the coastal cities."

    "Now they practiced a bastardized version of our ancient religion, stripped of all its power and reduced to symbolic rites and empty words."

    "But my own clan, we kept the old ways, along with its power."

    "Since the equinox has just passed, I know they'll be at the base of the eastern peak, where twice a year they convene with their sister clans to make political deals, including marriages."

    "A few more hours of walking, and I'll see my family again."

    "I hadn't even allowed myself to feel the excitement of seeing them, I was so consumed with getting help for Ari."

    "But now I allow myself to remember their faces--my parents, my younger brothers, my older sister. The elders--Auntie Urta, Uncle Tun."

    "I feel my heart growing lighter. I imagine the relief of seeing my parents again, eating the food I grew up with, speaking my own dialect."
    
    "If anyone can save Ari, it's them."

    #### ACT TWO ####

    scene un_camp
    show yeni at left
    show urta_angry at right

    u "Absolutely not. You shouldn't have come here, Yeni."

    show yeni_worried at left

    "Her words stung. I thought she'd be happier to see me, at least, even if she wasn't thrilled about what I had come to ask for."

    y "Please, Auntie. You're my last hope. If I lose Ari, I'll die. I swear it, I'll die."

    show urta_neutral at right

    u ""


    #### ACT THREE ####

label ritual:
    "The ritual has three parts. All of our rites start with an offering."



    # This ends the game.
    return
