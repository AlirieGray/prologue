define y = Character("Yeni")
define u = Character("Urta")
define w = Character("??")
 
image yeni neutral_scaled = im.Scale("yeni_neutral.png", 500, 700)
image yeni angry_scaled = im.Scale("yeni_angry.png", 500, 700)
image yeni scared_scaled = im.Scale("yeni_scared.png", 500, 700)

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

    show yeni angry_scaled at left

    y "Just tell me the truth."

    # show yeni crying

    show yeni neutral_scaled at left

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
    
    u "And one of his students was also able to recover from nearly fatal battle wounds, though he had never even met Tzeh."

    "I want to believe, but there's something bothering me about all this."

    y "Why is there no record of these miracles? Why do none of the priests have any record of anything like this happening after Tzeh's death?"

    u "Tzeh's disciples wanted her legacy and message to be preserved only in the revelations, not by the word of anyone who lived after her time."

    u "They made sure that only the miracles that occurred in her time were preserved."

    y "Then how do you know all of this?"

    u "Some priests preserved the knowledge, mostly in the form of poetry, which they never wrote down."

    u "It was passed only from teacher to student, down through the generations."

    y "So all this time, these priests knew about a way to cure blindness, fatal wounds, all sorts of things, and they kept it to themselves?"

    y "Why?"

    u "It's not that simple."

    u "Some of them were cured, yes, but at great cost. And for others it didn't work at all. Their hearts had to be pure."

    y "What cost?"

    "Not that it matters. I would pay any price there was to be paid, if there was a chance it would save Ari."

    u "It's... it's not so clear. The closest explanation to the truth is that they went mad."

    u "But I suspect it's more than that. The forces they were invoking, they have their own agendas."

    u "There's no way to know what you might be agreeing to if you accept that help, what you might be giving up."

    y "So what do I have to do?"

    u "I keep telling you, it's not that simple!"

    u "You can't just walk up the mountain and have all your problems solved."

    show yeni angry_scaled at left

    y "I don't care what the cost is! Don't you understand?"

    y "There's nothing could lose that's worth more than her life."

    show yeni neutral_scaled at left

    # Urta finally comes around

    y "If it's such a bad idea, why do you want to come with me?"

    u "I have to admit a certain curiosity."

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

    label i_have_questions:

        menu: 
            "What should I ask her?"

            "So how {i}do{/i} you know how to set up a ger?":

                u "I wasn't born in Eyun. Actually I was born into clan Yanaat."

                jump i_have_questions

            "Have you ever been to the Mratam?":

                u "No. Actually, I've never even been this far south."

                y "Never?"

                # u "No. My grandparents went north looking for a more comfortable life, and I think they were in some bad politics with the local lords."

                # u "They were probably aiming to go all the way to the coast like a lot of that generation, but stopped at the river Eyuna and just stayed there."

                jump i_have_questions

            "How did you learn to use your powers?":

                u "I had a teacher."
                
                u "He was a little... eccentric. But he passed down the knowledge pure, unadulterated."

                "Her voice sounds wistful, or is it regret?"

                u "Not like some of the charlatans these days. They have no respect for the tradition, they just want what they think it can give them."

                u "Though of course, it can't actually give them anything if they don't understand it."

                u "They think they can replicate what they do in the northern universities, even though that's a bastardization of our own practice."

                # maybe at the end Yeni has the option to be her apprentice?

                y "I see."

                jump i_have_questions

            "I don't have any more questions.":
                jump dream_sequence

    label dream_sequence:

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

        # TODO: connect this vision with Yeni being able to see the portal at the end

        # is it Tzehs influence somehow

        scene battle_720 with fade

        "{i}The smell of blood, smoke in my eyes.{/i}"

        "{i}The land of my forebears, soaked in destruction.{/i}"

        "{i}And all of it, to what end?{/i}"

        "{i}Did I bring the unity the Three Brothers promised?{/i}"

        "{i}The Mratim circle like great wolves, waiting for an opportunity.{/i}"

        "{i}All of this death...{/i}"

        "{i}The Brothers' words to me the last time I sought their aid haunt me everywhere I go.{/i}"

        "{i}\"Something about a great future promised idk\"{/i}"


        # TODO: write some revelations verses

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

    # wind sound

    play sound wind_sound loop

    
    "And thus the climb begins."

    "One step."

    "Another."

    "Then another."

    "Hours pass this way, as we ascend into the clouds."

    "The wind threatens to break my spine. The bitter cold of the steppe below is incomparable to the bite of the mountain air."

    "I keep Ari as protected as I can, wrapped inside my heavy coat. But still, this cold isn't good for her already frail body."
    
    "Climbing the sacred Mratam Kah is a feat supposed to be reserved for the gods and their prophets."
    
    "Well, now I understand why, at least."
    
    # TODO: crossfade wind and music

    # TODO: trim mystical sound

    stop sound fadeout 2.0

    play music mystical loop

    show yeni neutral_scaled at left

    "At long last, as the sun crests in the sky and begins to make its earthside return, we reach the peak."

    u "How is she?"

    y "Cold. But alright."

    u "Good. I'll start a fire."

    "Urta unfolds the cloth she's wrapped the fire starter in and sets about making a fire."

    "I should be doing it, as the younger of the two of us, but I don't think I can without exposing Ari to the cold air."

    "Urta nestles a tea pot in the coals. It doesn't get to a boil, but it gets hot at least."

    "She pours us each a cup."

    "I take a sip and almost spit it out."

    y "What is this??"

    u "What, you don't like my brewing technique?"

    y "It's, um---"

    u "Only teasing. This isn't regular tea, it's a special tea to increase the mind's capacity to connect to the Lattice."

    u "So, drink up."

    "I brace myself and down the bitter drink in two gulps."

    "Within a few minutes, I feel a tingling sensation in my hands."

    "Like static electricity."

    u "Now, breathe in through your nose and out through your mouth."

    y "What is this supposed to do?"

    u "It's supposed to condense thirty years of training into five minutes because that's about how much time we've got up here before we start to freeze."

    u "Now, stop asking questions and breathe. Focus on what you feel."

    u "And if we meet anyone, let me do the talking, alright?"

    y "Alright."

    "The static feeling in my fingers grows stronger, travelling up my arms."
    
    "I feel foggy, like I have a head cold. But also, somehow, sharper? Like everything is more vibrant."
    
    "I keep looking around, thinking I see something in the corner of my eye. Little threads like spiderwebs."

    scene portal_720

    # play lighting crack sound

    show yeni scared_scaled at left

    "!!"

    y "What is this??"

    u "This is..."

    u "Not what I expected."

    w "{i}Wtalta ymk altachiya?{/i}"

    "It's a strange voice, not quite like a man's but almost. It sounds like it's coming from everywhere all at once."

    "Even stranger is the language. It doesn't sound like anything I've ever heard."

    u "Spirit of the Beyond. We've come to your sacred place to ask for your help."

    "There's more strange sounds, like a high-pitched ringing."

    w "Hello? Is someone there?"

    show yeni neutral_scaled at left

    y "Yes, yes, we're here! We've come all this way because my daughter is sick. Please, can you help her?"

    "I remember too late that Urta told me to let her do the talking. I feel almost dizzy with hope and relief."
    
    w "Who is speaking with us?"

    u "We are devoted followers of Tzeh tl'Un, loyal to her and her revelations."

    u "We come in humility only, to save the life of an innocent."

    "My heart races. All this time, I kept pushing back my doubts, my fear that this would all amount to nothing."

    "But this, this is real!"

    w "What year is it?"

    "The question throws me, but Urta answers smoothly."

    u "It's 1032 Ascension."

    "There's a long pause. I want to say something else, worried that the mysterious voice has gone, but Urta stops me with a shake of her head."

    w "Did you change your calendar system?"

    u "Yes, the calendar counts the years since Tzeh tl'Un ascended Mratam Kah."

    "Another long pause. I'm almost about to speak again, but then--"

    w "You said your daughter is sick?"

    y "Yes, she was born early. She's frail, doesn't breathe well."

    w "Bring the child to the portal."

    "Portal?"

    "They must mean this thing that appeared in front of us."

    "For some reason, I hesitate. Urta gives me an incredulous look." 
    
    "After crossing the steppe, climbing the peak, do I really want to give up now?"

    "I step closer to the web--the portal. The static feeling in my head grows stronger, almost overwhelming, as I get closer."

    "Finally, I'm close enough to touch it."

    w "We're going to establish a link."

    y "What?"

    stop music fadeout 2.0

    scene black with fade 

    "Suddenly, everything goes black."

    "..."

    # wrap-up

    scene mountain_720 with fade

    show yeni neutral_scaled at left #show surprised

    y "What happened?"

    y "They took her? What do you mean, they took her??"

    "I look down."

    y ""

    # show yeni happy

    y "Ari. You're going to be okay."

    # back at the village, Yeni asks to be Urta's apprentice?

    # to credits 
    call credits 

    return

# TODO add credits tab to main menu

label credits:
    $ credits_speed = 25 #scrolling speed in seconds
    scene black #replace this with a fancy background
    with dissolve
    # show theend:
    #     yanchor 0.5 ypos 0.5
    #     xanchor 0.5 xpos 0.5
    # with dissolve
    # with Pause(3)
    # hide theend
    show cred at Move((0.5, 5.0), (0.5, 0.0), credits_speed, repeat=False, bounce=False, xanchor="center", yanchor="bottom")
    with Pause(credits_speed)
    show thanks:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    with Pause(3)
    hide thanks
    return

init python:
    credits = ('Creative Director', 'Alirie Gray'), ('Backgrounds', 'Meluvi'), ('Character Art', 'Seiji'), ('Writing', 'Alirie Gray'), ('Writing', 'Adrienne'), ('Song: Running Through Woodland', 'Message To Bears, In Autumnal Fog - Chapter III: Nightfall In The Darkstone Forest, Skeksis Netlabel Project'), ('Song - Evocation', 'Stjarana, In Autumnal Fog - Chapter III: Nightfall In The Darkstone Forest, Skeksis Netlabel Project'), ('Song: Reaching the Summit at Nightfall', 'Novemthree, Skeksis Netlabel Project'), ('Song: Kontio', 'Nest, Skeksis Netlabel Project')
    credits_s = "{size=80}Credits\n\n"
    c1 = ''
    for c in credits:
        if not c1==c[0]:
            credits_s += "\n{size=40}" + c[0] + "\n"
        credits_s += "{size=60}" + c[1] + "\n"
        c1=c[0]
    credits_s += "\n{size=40}Engine\n{size=60}Ren'py\n7.4.11.2266"
    
init:
#    image cred = Text(credits_s, font="myfont.ttf", text_align=0.5) #use this if you want to use special fonts
    image cred = Text(credits_s, text_align=0.5)
    image theend = Text("{size=80}The end", text_align=0.5)
    image thanks = Text("{size=80}Thanks for Playing! Arizet will return in Part One.", text_align=0.5)