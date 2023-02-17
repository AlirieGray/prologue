# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define y = Character("Yeni")
define u = Character("Urta")
define w = Character("??")
 
image yeni_neutral_scaled = im.Scale("yeni_neutral.png", 500, 700)
image yeni_angry_scaled = im.Scale("yeni_angry.png", 500, 700)
image yeni_scared_scaled = im.Scale("yeni_scared.png", 500, 700)

# The game starts here.

label start:
    # Part One: The Village

    scene village_720 # TODO: change image based on screen size/resolution

    play music bell_fade 

    queue music no_bell_fade loop

    show yeni_neutral_scaled at left
    "It’s nearly sunset by the time the village is in sight."

    "I glance down to check on my daughter again, swaddled tight against the cold of the journey here."

    "She’s breathing. But still her breaths come shallow, and too slow."

    "Her eyes are closed, her skin clammy." 

    "The journey here wasn’t easy on her, but I had no other options."

    "Babies born in a winteryear are supposed to be hardy, healthy, the way babies born in a summeryear are said to be prone to colic."

    "Arizet was born on the first day of the new year, named for the fierce bird that travels north to the coast each winteryear seeking warmth, and returns south when the sun is strong again over the steppe."

    "But in the past three days since her birth, she has just barely clung to life. She’s hardly nursed, hardly opened her eyes, and has yet to make a sound."

    "None of the standard remedies worked. Not the advice of the aunties or the medicine woman, though they had always worked for my first child when he fell ill."

    "It sends an ache through my chest to think of him, but I push it aside."

    "By the third day, Ari’s condition was only getting worse, and it was clear to me I had to look elsewhere if I was going to save her."

    "So just before the sun rose this morning, I got on my old mare Hialen and left the Anaak clan for the first time since I married into it."

    "Now I just have to find the woman I’ve only heard about in rumors. My last hope to save my daughter."

    y "Excuse me, auntie–"

    w "Well, well, a visitor! A little early in the year for trading. What brought you here?"

    y "I’m looking for a woman named Urta tl’Eyun."

    w "Is that right? And what are you going to do once you’ve found her?"

    y "Ask for her help. My sister-in-law says she’s a woman wise in medicine who helped her cousin when her baby was sick."

    w "Hmm, so she helped the cousin of a sister-in-law. That’s not a lot to go on. This ‘Urta’ could be a quack for all you know, couldn’t she?"

    y "No, she–"

    w "A grifter. An old woman with her head in the Web."

    "I’ve heard enough. I don’t have time for this."

    y "Look, can you help me find her or not? I was told she lived in this village."

    w "That’s no way to talk to your elder, now is it?"

    "I take a deep breath and bite back my initial response."

    y "I’m sorry, auntie. Let me explain."

    y "I came looking for help for my daughter. She was born sick and she doesn’t have much time left."

    y "I’ve tried everything. I need a miracle. I was told Urta was the only person who could save her."

    w "Oh now, who’s been making promises on my behalf?"

    y "On… your behalf?"

    u "You said you were looking for Urta tl’Eyun. Well, you’ve found her!"

    y "So, you’re… her?"

    u "That’s me, Urta the miracle worker, apparently. Eh, I’ve heard worse, at least."

    "Why didn’t she start with that??"

    y "Please, you have to help me. I–"

    u "I have to do nothing of the sort. You haven’t even told me your name."

    y "Yeni tl’Anaak."

    u "Well, Yeni tl’Anaak. I don’t work for free, not outside the Eyun. And more importantly, I don’t even know if I can help your daughter. Despite what you’ve heard. I can try, but I can make no promises."

    "I sigh. I guess that’s to be expected."

    "I pull out a pouch of gold from inside my coat. Some bangles, some coins. It’s the last that remains of my dowry, the rest has been spent over the past five years."

    "I hand it over to Urta, and wait anxiously while she inspects the contents of the bag."

    u "You said it’s your daughter that’s sick, hmm?"

    y "That’s right."

    u "How old is she?"

    y "Three days."

    "She stops counting the gold abruptly."

    u "You brought an infant, not even past her (age ritual ~1 week to 1 month?) all the way from Anaak?"

    y "That’s right."

    u "Hmm. Does your family know the amount you’re shelling out to save an infant? Wait, do they even know you’re here?"

    y "...No."

    u "Hmm."

    "She’s guessed the whole story, no doubt. It would be seen as highly wasteful and inappropriate, even shameful, if my relatives by marriage knew the lengths I was going to in order to save an infant."

    "It’s normal to seek medical care for a baby that is born ill or develops an illness in their first year. But the first month is a period when the soul is just passing through the body, which is why many babies die around this time, because the soul decides to move on."

    "Many souls decide only to visit this plane, not to stay, and those are the babies that live no more than a week or two."

    "This is also why mothers tend to die in childbirth, because of the pull caused by the child’s spirit being partially in one world and partially in the next."

    "After a month, the infants go through (age ritual). This is when their souls are fully realized in their bodies and there’s a big celebration."

    "So while the midwives and the doctor might help me treat my daughter in her first days of life, they would just as likely tell me: this one is just a visitor."

    u "Well, you’ve went to a lot of trouble. This "

    "She pockets the pouch of gold."

    u "Let’s bring you both inside. This cold isn’t good for either of you."

    "Relief washes over me so strong I almost feel my knees go weak, the exhaustion of the past few days catching up with me."

    y "Thank you, Auntie, (blessing of some sort.)"

    "She waves her hand."

    u "Just come inside. I’ll have my daughter-in-law serve some tea."

    "She leads me to one of the houses on the outskirts of the village, and shows me a place to tie my mare."

    "Her daughter-in-law, who introduces herself as Nali tl'Eyun, serves Urta and I both sheep yogurt with salt and fresh green (herb name), and some boiled sheep rump in sourbroth."

    "I eat all of it gratefully and a little too quickly, it's been a long day on the road."

    "After we eat, Nali serves us tea and is pulled outside to resolve something that her two young sons assure her is an urgent situation."

    "My breath catches when I see them tug her with their small hands. I look down at Ari, still asleep in her swaddle."

    y "She barely nurses. At this rate she has days... maybe less."

    # show urta sad/concerned

    stop music fadeout 2.0

    show yeni_neutral_scaled at left


    ################ Part Two: The Dream ##################

    "The two moons are high in the sky. We've been travelling the better part of the night."

    "The cold of night bites like a grass spider. It's the kind of cold that will burn your skin if you leave it exposed."

    "I'm exhausted, but it won't be safe to sleep until the sun rises."

    "I keep Arizet close to my body, inside my overcoat."

    "It's considered inadvisable to travel the steppe at night, especially during a winteryear."

    "And for two women alone with a newborn, it would probably be considered downright suicidal."

    "But I have to make as much progress as I can, in as little time as possible."

    "Normally the distance from my village to the base of the mountain would take a travelling clan three days to cross."

    "I don't have three days. I don't even know if I have one day, or one hour to spare."

    "In the war days of our clan, our ancestors used to cross the steppe from west to east or south to north without stopping even to eat or water the horses."

    "Those days have long passed, but still any child of the steppe is born with one foot in the saddle."
    
    "I remind myself that the mountains draw closer with each step, but I cannot see them. Only the dim glow of my lantern, and the mane of my mare."

    "In the silence and darkness, it's too easy to succumb to memories."
    
    "My son Ohzin, crying out to me for help. The helplessness I felt when he was torn from my arms, and dragged away."

    "The guilt and every sleepless night I've spent since then."

    "The other women told me it would get easier, but it never has."

    "Still, it was only them who kept me alive, kept me from losing hope altogether."

    u "There, the oasis."

    y "I see it. We don't have time to stop. Another few hours and--"

    u "We've been riding all night. The horses need water and grazing and we both need some sleep."

    u "The hardest part will be the climb up the mountain, not this little jaunt."

    "I sigh, but she's right."

    y "Alright. But just for a couple hours. Then we need to move on."

    u "Just for a few hours."

    "We get off our horses and begin to untack them."

    "Next I help Urta gather some branches for a fire, and I suddenly notice--"

    y "It's odd not to find anyone here. Usually there's at least a party of merchants camped here, if not a whole clan."

    u "Mm."

    "But at this time of year, everyone is already farther west, travelling to the gathering of the clans."

    "Business deals and trade negotiations are made at that gathering every year, but most importantly marriages are arranged between clans."

    "That's how we keep the peace on the steppe. It's how I wound up with the Anaak, the northernmost of the twenty or so clans."

    u "You sleep first. I'll wake you."

    "I go to sleep..."

    # Dream transition here?


    scene battle_720



    # scene camp again

    stop music fadeout 2.0

    "What was that?"

    
    scene black

    play sound wind_sound loop
    
    "And thus the climb begins."

    "One step."

    "Another."

    "Then another."

    "Hours pass this way, as we ascend into the clouds."

    "The wind threatens to break my spine. The bitter cold of the steppe below is incomparable to the mountain air."
    
    "Climbing the sacred Mratam Kah is a feat supposed to be reserved for the gods and their prophets. Now, at least, I understand why."

    "I spent so long thinking about how to get up here... but how am I going to get back down?"

    "Well, one thing at a time."

    "..."

    stop sound fadeout 2.0
    
    scene mountain_720 with fade

    play music foreboding loop

    show yeni_neutral_scaled at left

    "At long last, as the sun crests in the sky and begins to make its earthside return, we reach the peak."

    # she does the ritual

    scene portal_720

    # play lighting crack sound

    show yeni_scared_scaled at left

    "!!"

    "What is this...?"

    w "Well, well, little one."

    w "It's been a while since anyone knocked on my door. At least, I think it has. What year is it?"

    "I hear her voice, it's deep and strong, though not through my ears. It sounds like it's coming from everywhere at once."

    "Shit, I haven't even thought about how I should address her."

    y "Revered Prophet, this humble servant--"

    w "Oh, enough! I just asked what year it is. It's a simple enough question."

    show yeni_neutral_scaled at left

    y "It's 1012."

    w "That makes no sense. I was born in 3037." # TODO what are the different calendars called 

    y "We changed the calendar to year one after your ascension."

    w "So it's been a thousand years..."

    w "Well, in all that time no one's ever come by just to have tea. What is it you want?"

    y "It's my daughter... She's dying."

    y "She was born frail. She doesn't nurse. Please, this humble servant begs you. Help my daughter. Save her."

    w "Hmm... Well I don't know what you expect me to do from here."

    y "From here?"

    w "Yes, girl, from the other side of the Web. Keep up!"

    w "Do I look like a medicine woman? No, I don't look like anything at all! I don't have a body anymore."

    w "If I could have "

    # sound effect

    return
