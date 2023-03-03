# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define y = Character("Yeni")
define u = Character("Urta")
define w = Character("??")
 
image yeni neutral_scaled = im.Scale("yeni_neutral.png", 500, 700)
image yeni angry_scaled = im.Scale("yeni_angry.png", 500, 700)
image yeni scared_scaled = im.Scale("yeni_scared.png", 500, 700)

# The game starts here.

label start:
    # Part One: The Village

    scene village_720 # TODO: change image based on screen size/resolution

    play music bell_fade 

    queue music no_bell_fade loop

    show yeni neutral_scaled at left

    "It’s nearly sunset by the time the village is in sight."

    "I glance down to check on my daughter again, swaddled tight against the cold of the journey here."

    "She’s breathing. But still her breaths come shallow, and too slow."

    "Her eyes are closed, her skin clammy." 

    "I'm relieved to have made it before nightfall and not have to set up camp again."

    "The journey here wasn’t easy on her, but I had no other options."

    "Babies born in a winteryear are supposed to be hardy, healthy, the way babies born in a summeryear are said to be prone to colic."

    "Arizet was born on the first day of the new year. I named for the fierce bird that travels north to the coast each winteryear seeking warmth, and returns south when the sun is strong again over the steppe."

    "But she wasn't supposed to arrive this early." 

    "In the past week since her birth, she has just barely clung to life. She’s hardly nursed, hardly opened her eyes, and has yet to make a sound."

    "None of the usual remedies helped, none of the advice that had worked for my first child when he fell ill."

    "It sends an ache through my chest to think of him, but I push it aside."

    "By the third night, Ari’s condition was only getting worse, and it was clear to me I had to look elsewhere if I was going to save her."

    "So just before the sun rose that morning, I got on my old mare Hialen and left the Anaak clan for the first time since I married into it."

    "Now I just have to find the woman I’ve only heard about in rumors. My last hope to save my daughter."

    y "Excuse me, auntie–"

    w "Well, well, a visitor! A little early in the year for trading. What brought you here?"

    y "I’m looking for a woman named Urta tl’Eyun."

    w "Is that right?"

    y "My sister-in-law says she’s a woman wise in medicine who helped her cousin when her baby was sick."

    w "Hmm, so she helped the cousin of a sister-in-law. That’s not a lot to go on. This ‘Urta’ could be a quack for all you know, couldn’t she?"

    y "No, she–"

    w "A grifter. An old Lattice-addled woman."

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

    y "Wait. You’re… her?"

    u "That’s me, Urta the miracle worker, apparently. Eh, I’ve heard worse, at least."

    "Why didn’t she start with that??"

    y "Please, you have to help me. I–"

    u "Slow down, child. You haven’t even told me your name."

    y "Yeni tl’Anaak."

    u "Well, Yeni tl’Anaak. I don’t work for free, not outside the Eyun. And more importantly, I don’t even know if I can help your daughter. Despite what you’ve heard. I can try, but I can make no promises." # TODO: player has to pick how to convince her, one of the ways is offering money since it would be considered gauche for her to just ask

    "I sigh. I guess that’s to be expected."

    "I pull out a pouch of gold from inside my coat. Some bangles, some coins. It’s the last that remains of my dowry, the rest has been spent over the past five years."

    "I hand it over to Urta, and wait anxiously while she inspects the contents of the bag."

    u "You said it’s your daughter that’s sick, hmm?"

    y "That’s right."

    u "How old is she?"

    y "A week. But she was born early."

    "She stops counting the gold abruptly."

    u "You brought an infant all the way from Anaak territory? All the way south of the Naang river?"

    y "That’s right."

    u "Hmm. Does your family know the amount you’re shelling out? Wait, do they even know you’re here?"

    y "...No."

    u "Hmm."

    u "Well, you’ve went to a lot of trouble."

    "She pockets the pouch of gold."

    u "Let’s bring you both inside. This cold isn’t good for either of you."

    "Relief washes over me so strong I almost feel my knees go weak, the exhaustion of the past few days catching up with me."

    y "Thank you, Auntie." # blessing of some sort

    "She waves her hand."

    u "Just come inside. I’ll have my daughter-in-law serve some tea."

    "She leads me to one of the houses on the outskirts of the village, and shows me a place to tie my mare."

    "Her daughter-in-law, who introduces herself as Nali tl'Eyun, serves Urta and I both sheep yogurt with salt and fresh green, and some boiled sheep rump in sourbroth." #herb name

    "I eat all of it gratefully and a little too quickly. "

    "After we eat, Nali serves us tea and is pulled outside to resolve something that her two young sons assure her is an urgent situation."

    "My breath catches when I see them tug her with their small hands. I look down at Ari, still asleep in her swaddle."

    y "She hasn't made hardly a sound since she was born. She barely nurses, mostly just sleeps."

    u "Let me take a look at her."

    "I watch as Urta listens to her breathing, her heart, and gently opens her eyes and her mouth to check them."

    "Then she closes her eyes and is silent for a moment."

    "It doesn't look like she's doing anything. But I can feel a prickling on my arms, like the static before a lightning storm."

    "For a second, I think I see thin lines, like spiderwebs, glowing faintly around her hands as they trace over my daughter's tiny limbs."

    "I want to ask Urta what she's doing, but she seems so deep in concentration that I don't want to disturb her."

    "Finally, she sighs and steps back."

    u "I'm sorry, child. There's nothing I can do for her."

    # show Yeni angry 

    y "You just looked at her! How do you know there's nothing you can do? You won't even try?"

    u "There's nothing to try, girl. A baby born this early rarely makes it past their first night."

    u "You must know this already. Don't beat the horse because its rider brings bad news."

    y "What was that spiderweb thing you were doing? Can't you use that to help her?"

    # show urta surprised

    u "You could see that?"

    # show urta neutral

    y "I knew it! You were doing something. So do it again. Please just try."

    u "It doesn't work like that. No one has used the Lattice for healing since the time of Tzeh and maybe the two or three generations after that."

    # show yeni surprised 

    y "What? That spiderweb thing, that's how Tzeh tl'Un was healed?"

    y "And what do you mean, the generations after? The miracles were only given in the prophet's lifetime."

    u "It's not a 'spiderweb.' It's the Lattice."

    u "And it wasn't only using for healing during Tzeh's life. Some of her disciples were able to access this power in the years following her death, as well."

    u "And some of them were able to pass on the skill."

    u "But hardly anyone even knows the basics of how to wield it anymore."

    u "And certainly it's not some miracle cure for premature births."

    y "But you said it used to be used for healing. So it's possible."

    u "I don't want to promise you something I can't give."

    y "Just tell me the truth."

    # show yeni crying

    y "Please, I've already lost one child."

    y "I couldn't survive if I lost Ari, too."

    y "I know you don't know me. I don't have a lot of money to give you. But you're my only hope."

    y "If you know something, if there's {i}any{/i} chance it could save my daughter, please tell me."

    "She seems to hesitate a moment, but relents with a heavy sigh."

    # show yeni neutral

    u "It's dangerous, what you're asking for. There are only stories. I don't even know how true they are."

    u "When Tzeh came down from Mratam Kah with the revelations, with her wounds healed and her arms restored, she found she had also returned with special gifts and powers."

    u "Some of these we know about already through the revelations."

    u "She was never able to heal others the way she had been healed."

    u "But some of her disciples, both in her time and in the years after her death, did receive those miracles."

    # show yeni surprised

    y "How did they do it?"

    u "According to the few stories that have been preserved, they went to the peak of Mratam Kah with pure hearts and asked the Three Brothers to heal them."

    y "And they were?"

    u "Yes. One of Tzeh's closest disciples had his vision restored many years after her death."
    
    u "And one of his students was also able to recover from nearly fatal battle wounds in the "

    "I want to believe, but there's something bothering me about all this."

    y "Why is there no record of these miracles? Why do none of the priests have any record of anything like this happening after Tzeh's death?"

    u "Tzeh's disciples wanted her legacy and message to be preserved only in the revelations, not by the word of anyone who lived after her time."

    u "They made sure that only the "

    "........."

    u "We'll leave at first light."

    stop music fadeout 2.0

    show yeni neutral_scaled at left

    ################ Part Two: The Dream ##################

    scene camp_sketch


    "After a day of travelling, we have to stop for the night."

    "I move gather dung and some dry chaparral for the fire and help Urta set up the ger."

    "We work in silence, but I can't help glancing over at Urta, wondering about her past."

    u "Well, spit it out."

    y "Huh?"

    u "You're wondering how I know how to set up a ger, when I was raised in a village?"

    #show yeni surprised 

    y "What, did you use your magic powers to read my mind?"

    u "No, child. It's just written all over your face."

    u "Well, if you have questions, then ask."

    menu: 
        "What should I ask her?"

        "So how {i}do{/i} you know how to set up a ger?":

            u "I wasn't born in Eyun. Actually I was born into clan Un."

        "Have you ever been to the Mratam?":

            # u "No. Actually, I've never even been this far south."

            # y "Never?"

            # u "No. My grandparents went north looking for a more comfortable life, and I think they were in some bad politics with the local lords."

            # u "They were probably aiming to go all the way to the coast like a lot of that generation, but stopped at the river Eyuna and just stayed there."

            y ""

        "How did you learn to use your powers?":

            u "I had a teacher."
            
            u "He was a little... eccentric. But he passed down the knowledge pure, unadulterated."

            "Her voice sounds wistful, or is it regret?"

            u "Not like some of the charlatans these days. They have no respect for the tradition, they just want what they think it can give them."

            u "Though of course, it can't actually give them anything if they don't understand it."

            u "They think they can replicate what they do in the northern universities, even though that's a bastardization of our own practice."

            # maybe at the end Yeni has the option to be her apprentice?

            y ""

    # loyalty came from Tzeh's personal relationships a la Hilo

    u "Get some sleep. You'll need it for tomorrow."

    y "Goodnight..."

    scene black with fade

    "It's hard to fall asleep, my mind is swimming with doubt and fear."

    play music foreboding loop

    "I keep checking Ari, sleeping on my chest."

    "She's hanging on, my brave girl. I'm not giving up on her."

    "At last, I drift away into sleep..."

    # Dream transition here

    scene battle_720 with fade

    "{i}Battle flashback.....{/i}"

    "{i}.....{/i}"

    # scene camp again

    scene camp_sketch with fade

    show yeni scared_scaled at left

    stop music fadeout 2.0

    "What was that??"

    "It didn't feel like any dream I've ever had."

    "It was so real..."

    show yeni neutral_scaled at left

    "??"

    scene black with fade

    scene mountain_720 with fade
    
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

    play music mystical loop

    show yeni neutral_scaled at left

    "At long last, as the sun crests in the sky and begins to make its earthside return, we reach the peak."

    # she does the ritual

    scene portal_720

    # play lighting crack sound

    show yeni scared_scaled at left

    "!!"

    "What is this...?"



    # sound effect

    return
