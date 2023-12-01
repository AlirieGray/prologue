define y = Character("Yeni", color="#0390fc")
define u = Character("Urta", color="#fc8803")
define w = Character("??", color="#fc8803")
define m = Character("??", color="#6f03fc")
 
image yeni neutral_scaled = im.Scale("yeni_neutral.png", 500, 700)
image yeni angry_scaled = im.Scale("yeni_angry.png", 500, 700)
image yeni scared_scaled = im.Scale("yeni_scared.png", 500, 700)

label start:
    # Part One: The Village

    scene village_720 # TODO: change image based on screen size/resolution

    play music bell_fade 

    queue music no_bell_fade loop

    show yeni neutral_scaled at left

    "There's still enough light by the setting sun and the rise of the moons to find my way to the house."

    "This is the village I grew up in, but the familiar faces of my childhood avoid my gaze when I try to catch their eyes."

    "The shepherds are bringing their flocks in for the night." 

    "I guide my horse to the house on the west side of the village and dismount, then tie the mare to a post outside the house."

    "My daughter is fussing in her sling, and I bounce her gently to soothe her."

    y "It's alright, beautiful girl. Yes, it'll be alright."

    "I'm trying to convince myself as much as the baby in my arms."

    "The door looms daunting and closed in front of me."

    "I steel myself and knock."

    # play knocking sound effect

    "..."

    "The central chimney is giving off smoke, so I know the house isn't empty."

    #play knocking sound effect

    "I try knocking again."

    u "Go away. Come back in the morning."

    "I feel a sinking feeling in my stomach."

    y "It's me. It's Yeni."

    "There's the sound of movement on the other side of the door, but it still doesn't open."

    "I feel too warm, like I can't catch my breath, even though the evening air is chilly."

    "I'm wondering if I should say something else, when finally I get a response."

    u "What are you doing here? Your husband left you, then?"

    y "Can you just open the door?"

    "I'm kicking myself for the desperate edge I hear in my voice."

    u "I said come back in the morning."

    y "Don't you even want to meet your granddaughter?"

    "..."

    # play door unlocking sounds

    "Finally, the sound of the door unlocking."

    # Show urta

    "My breath catches in my throat and I feel myself hold my daughter a little tighter."

    "Somehow, I thought my mother would be taller, like when I was a young girl. Even though she was already taller than me when I left home."

    "I feel my resolve waver as she stares stone-faced at me, but then she looks down at the baby, and I see my mother's expression soften as her granddaughter looks at her with rapt curiosity and babbles softly."

    y "Her name is Arizet. Ari."

    "Finally, she opens the door the rest of the way, and gestures for me to enter."

    "I feel relief sweep over me like a windstorm. I hadn't allowed myself to think too much about this moment, on the week-long ride here. But now all the doubt I'd been keeping beneath the surface finally leaves me as I step into my childhood home."

    "The house is comprised of one round room, with a fire in the center over which a pot of soup is boiling. A low table is set off to one side, and cushions line the walls. Dried herbs and smoked sheep meat hang from the rafters in long strips."

    "I instinctively start for the fire at the center, but then as I'm about to pass the guests' seat to the right of the door."

    "Am I guest now? Do I have to wait to be invited to the center of the house where I grew up?"

    "My mother has already crossed to the fire and is stirring the soup. She looks up at me and frowns, waving a hand breezily."

    u "Don't be petulant. Come and help me cook."

    "I join my mother at the fire. It's been a long journey, and I'm very hungry."

    u "Winteryear babies are strong, you know. That's what they all told me when you were born. She has our chin, too."

    u "How old is she?"

    y "Two months."

    u "Hm. Two months."

    u "It hasn't been easy the past year, you know. A woman at my age, doing everything alone."

    "The comment is so offhand, almost casual."

    "As if for her, that was the worst thing to come out of not seeing her daughter for a whole year. As if I had any say in the matter."

    "As if my mother might have chosen differently, might have regretted her decision to cast me out…"

    "But only because of this. Only because of the inconvenience."

    "But I keep quiet, and sprinkle salt in the broth."

    "It's just easier this way. I can let my hands work of their own accord, pulling dried meat down from the rafters and shredding it to bits, then throwing it in the broth to soften."

    u "Now, you didn't come here on a pigeon's trip. Are you going to tell me why you're here?"

    y "It's… Well, it's better if I tell you after we eat."

    "I'm obviously already on icy ground with her. I don't want to also bring bad luck by sharing the news I have over a meal."

    "To my relief, my mother just nods."

    "We remain in silence until the soup is finished cooking and we've both eaten and Ari has fallen asleep nursing in her sling."

    "Now it's time for the real reason I came all this way, but I'm not sure how to start."

    "I decide to just show her. I go to the bag I left by the door, under my heavy overcoat. I reach inside and pull out the strange artifact."

    "It's a disk shaped like two soup bowls stacked one upside-down on the other. It's heavy and gray, but not made of any stone or metal I've ever seen before. It has a strange gleam to it, almost like glass, and it's covered in these tiny grooves and raised circles that form a web-like pattern across the surface."

    "I've spent countless hours staring at it over the past week it took for me to travel here. But I still haven't been able to discern any pattern in these strange markings."

    "It feels familiar, but every time I try to focus on that sense of recognition, my focus slips and I find myself putting the strange thing away again."

    "When I bring it to my mother, I expect to see confusion in her eyes. Or curiosity, or even disdainful disinterest."

    "But instead her eyes grow wide, and she snatches it from my hands."

    u "Where did you get this?"

    "I'm so surprised by this that it takes me a moment to respond."

    y "From my husband. But I don't understand. You know what it is?"

    u "From you husband? When? How did he find this?"

    y "Last week, before he…"

    y "...before he died."

    "It takes me a moment to steady my voice before I can continue. Ari wakes and starts fussing and I rock her back and forth in the sling."

    y "He said his family had passed it down, waiting for the right time to use it for… something. He said he knew the time had come, but he was too sick to make the journey by then."

    y "That was his last request of me. That I finish what his ancestors started."

    "I look down at Ari. She's the only thing that's kept me moored, in the cold days of the past week."

    u "Oh, my girl!"

    "She crosses over to sweep me up in a hug. I feel my body stiffen, but I force myself to return the hug."

    "My eyes sting, and I squeeze them shut."

    "My mother sits back and holds me by the shoulders at arm's length for a moment, studying me with some concern in her eyes."

    "I don't trust my face not to betray me, so I look away."

    y "He asked me to bring it to the top of the holy mountain. He didn't tell me why. He just said there was a ritual I had to do with it once I got there.  He kept saying it was important, more important than anything else."

    y "He made me promise. So I did."

    "My mother is tracing the grid on the disk with her fingers, her eyes unfocused. She speaks softly, as if to herself."

    u "I don't understand. After all this time, why now?"

    "I feel my teeth clench and unclench."

    y "What do you mean? What is this thing, what do you know about it?"

    u "You came to ask me if I'll go to the mountaintop with you. To see this through."

    y "I… Yes."

    u "Alright, then. We'll leave at dawn."

    u "Get some sleep. I'll pack for us."

    # Part Two: The Camp

    scene black with fade 

    "..."

    stop music fadeout 2.0

    scene camp_720 with fade

    "Good place to camp. todo: add camp scene here..."

    scene black with fade 

    "It's hard to fall asleep, my mind is swimming with doubt and fear."

    play music foreboding loop

    # dream transition

    "...."

    scene battle_720 with fade

    "{i}The smell of blood, smoke in my eyes.{/i}"


    "{i}....{/i}"


    #back to camp

    scene camp_720 with fade

    show yeni scared_scaled at left

    stop music fadeout 2.0 
    
    "What was that??"

    "..."

    scene black with fade

    scene mountain_720 with fade

    # wind sound

    play sound wind_sound loop















    # Part Three: The mountaintop

    u "Are you ready?"

    "Her voice is so gentle, for once, that for a brief moment it actually feels like I have it choice. For a split second, I feel like it matters, whether or not I'm ready."

    "I take in a deep, shaky breath, and pull the disk out of my pack."

    "I cast back my memory to the instructions my husband gave me on his deathbed. I press on two small raised circles on the disk until I hear a soft click."

    # play button clicking sound

    "Then I take the two halves of the disk and spin them around until the grooves are aligned with each other."

    "!!"

    "The disk grows hot in my hand immediately, and I drop it out of shock. The grooves are shot through with light of every color. It sizzles where it meets the snow, steam rising around it."

    u "What are you——"

    "Around us, the air blurs as if from the heat around a stove. Then it begins to shimmer with every color."

    # play low ringing sound

    "There's a low ringing sound that seems to come from all around me."

    "Then, a defeaning boom like the snap of thunder, shuddering all through my body. And something incomprehensible materializes before us."

    play music portal

    y "What is it??"

    u "It's a tear in the web..."

    y "A what??"

    # urta explains a little bit more

    "And then, blackness..."

    "Blackness, threaded through with multicolored light..."

    "..."

    "The next moment I'm aware of myself, I'm lying in the snow, with a splitting pain wracking one side of my head. My arms are empty."

    y "Where's--??"

    "Then I see my mother sitting at my side, Ari in her arms."

    "I reach immediately to take my daughter."

    # expand on the dialog between them


    u "Let me carry her a little ways. You'll need your strength."

return