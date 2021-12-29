# CHARACTERS
define y = Character(_("Yeni"), color="#5a0ee7")
define a = Character(_("Azem"), color="#006300")
define w = Character(_("??"), color="#006300")
define u = Character(_("Urta"), color="#683904")
define t = Character(_("Tzeh tl'Un"), color="#98f8ff")


# START
label start:
    #### ACT ONE ####
    scene bg_village
    show yeni at left

    "The last bands of orange light have given way to blackness on the horizon, and the sounds of the village have died down as people retire for the night."

    "I swaddle Arizet in more layers than I normally would and wrap her tight to my body before pulling a thick cloak over both of us and strapping a travelling pack of dried food and a waterskin to my back." 

    "It's warm this far north, even at night. But the farther we get from the coast and the closer to the mountains, the colder and harsher it'll be, even when the sun comes up."

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

    scene bg_village
    show yeni at left

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

    show yeni_worried at left

    y "Hold on, Ari. I'm taking you to someone who can help."

    show yeni_neutral at left

    "After eating the food in the pack, I shake the cloth out and wrap it around my shoulders as another layer against the cold."

    "I stand back up, and orient myself using the unique peaks of the mountains as landmarks."

    "It's easy to orient myself, it comes naturally as if I'd left home yesterday." 
    
    "Last night as I made preparations to leave, I had been worried I'd forgotten how to find my way on the steppe, and would wind up wandering until I died of thirst."

    "But that fear was far overshadowed by the fear of losing Arizet."

    "No one in the village could help me. They don't know anything of magic, or even medicine. They lost it all when their ancestors planted roots and began to adopt the way of the coastal cities."

    "Now they practiced a bastardized version of our ancient religion, stripped of all its power and reduced to symbolic rites and empty words."

    "But my own clan, we kept the old ways, along with its power."

    "Since the equinox has just passed, I know they'll be at the base of the eastern peak, where twice a year they convene with their sister clans to make political deals, including marriages."

    "A few more hours of walking, and I'll see my family again."

    "I hadn't even allowed myself to feel the excitement of seeing them, I was so consumed with getting help for Ari."

    "But now I allow myself to remember their faces--my parents, my younger brothers, my older sister. The elders--Auntie Urta, Uncle Tun."

    "I feel my heart growing lighter. I imagine the relief of seeing my parents again, eating the food I grew up with, speaking my own dialect."
    
    "If anyone can save Ari, it's them."

    #### ACT TWO ####

    scene camp
    show yeni at left
    show urta_neutral at right

    u "Absolutely not. You shouldn't have come here, Yeni."

    show yeni_worried at left

    "Her words stung. I thought she'd be happier to see me, at least, even if she wasn't thrilled about what I had come to ask for."

    y "Please, Auntie. You're my last hope. If I lost Ari, I think I'd die."

    show yeni_neutral at left

    u "I know. You're just doing what you feel you have to for your daughter."

    u "But what you're asking for, I don't even think it's possible. Let alone a good idea."

    y "You always said there was great power in the steppe, in the mountains. Power that our ancestors used, that still guides our way of life."

    y "You told me it could help me in my darkest times, if I just asked for it."

    y "I'm asking you now. Show me the ritual. I know where to go, just show me how to call--"

    scene camp_darkened
    show urta_angry at right
    show yeni_worried at left

    u "TZEH TL'UN IS NOT TO BE TRIFLED WITH!"

    "Suddenly her voice is thunderous. I feel static fill the air around me."

    scene camp

    show urta_neutral at right
    show yeni_worried at left

    u "What makes you think she'd help you, anyway? Even if we could succeed in calling her from her hiding place."

    u "Which no one has managed to do in a thousand years, I might add."

    show yeni_neutral at left

    y "I don't know, really. She's a tl'Un. We always help each other, and she was the strongest of us."

    u "Until she wasn't."

    y "What do you mean?"

    u "You only know part of the story. The one we tell children, and those not trained in magic."

    u "It's time I told you the rest of Tzeh's story, and then you'll understand why I cannot help you."

    scene story_bg

    "Her words weave an image in my mind, transporting me one thousand years back."

    "{i}As Tzeh came of age, the steppe was being torn apart by clan war.{/i}" 

    "{i}Blood soaked the grasslands like a marsh. Warriors would raid the camp of an enemy clan and slaughter their animals, so that everyone from the youngest child to the oldest man would starve.{/i}"

    "{i}The Un clan, which Tzeh was adopted into as a young girl, was small and weak. She knew that her family would not survive long if the battles continued.{/i}" 

    "{i}All children of the steppe feel a connection to Mratam Kah. It is the holiest of holy peaks in our beloved mountains, and even during the time of Tzeh’s life it held great importance.{/i}"

    "{i}But Tzeh had always felt a stronger pull to the sacred mountain, a call that gnawed at her psyche more insistently as the war grew closer and more disastrous.{/i}"

    "{i}The day of the equinox was approaching, and the leaders of the largest clans were planning to arrange a truce through the marriage of one of the great kings to the daughter of another.{/i}"

    "{i}But the night before the equinox, a group of warriors raided the Un clan, and slaughtered everyone they could find. Only Tzeh survived.{/i}"

    "{i}No one knows why the warriors raided that day, perhaps they thought the Un clan would be an easy target because of their small size and lack of political standing.{/i}"
    
    "{i}We’ll never know why, since even name of that clan is now lost to history. Because the revenge that Tzeh tl’Un exacted was swift, and complete.{/i}" 

    "{i}On the day of the equinox, Tzeh ascended the sacred mountain that had called her name all her life.{/i}"

    "{i}There she found a wellspring of power and knowledge, and drank from it. From that day forward, she wielded the power of a god.{/i}"

    "{i}She came down the mountain and unleashed her grief and anger on the assembled clans. The sky was darkened, though there were no clouds.{/i}"
    
    "{i}She killed the leaders of every clan, and their families down to the last child.{/i}"

    "{i}It took her no more effort than the blink of an eye.{/i}"

    "{i}The survivors fell to their knees in awe and fear, and Tzeh became Queen of the Steppe.{/i}"

    "{i}She united the warring clans under her name, and forged an empire that spanned from the trading ports of the northern coast to the southern tundra.{/i}"

    "{i}It wasn't just her magical prowess that caused the people to follow her, or allowed her success in battle.{/i}"
    
    "{i}She also had a natural inclination for leadership, a charisma that won people to her side, and a ruthless and brilliant mind for military strategy.{/i}"

    "{i}In her fiftieth year, she announced that she was being called back to the mountain, and that she didn't know when she would return.{/i}"

    "{i}This is the story you know. Without Tzeh's leadership, her inner circle tore itself apart to grab power for themselves.{/i}"

    "{i}The empire crumbled.{/i}"

    "{i}Since then, we have been waiting for her to return and bring back the glory of the empire she forged.{/i}"

    "{i}This is the story you know.{/i}"

    "{i}But what you haven't been told is the toll that Tzeh's power took on her mind, on her soul.{/i}"

    "{i}Tzeh was changed by her journey to the top of Mratam Kah.{/i}"
    
    "{i}She was consumed by otherworldly visions, and she possessed a bloodlust that unnerved even the most battle-hardened of her generals.{/i}"

    "{i}It wasn't the mountain that called her back to it.{/i}"
    
    "{i}It was her own inner circle, motivated as much by fear of what Tzeh had become as they were by their own ambition, that betrayed Tzeh and banished her to the other realm.{/i}"
    
    "{i}Those that pray for her return do not know what they ask for. But those of us with this knowledge know we would be seen as heretics and traitors to our own history if we revealed it widely.{/i}"
    
    "{i}We share it only with those trained in magic so that they know the danger of the path they walk.{/i}"

    "{i}Tzeh tl'Un was imprisoned to keep the children of the steppe safe from her insatiable wrath.{/i}"

    "{i}She must never be released, or the whole world will suffer the consequences.{/i}"

    scene camp 
    show yeni_neutral at left
    show urta_neutral at right

    u "Do you understand now?"


    #### ACT THREE ####

    scene camp

    "The story unnerves me, but Auntie Urta's moralizing tale isn't going to dissuade me now."

    "If she won't help me, I'll "

    scene mountain

label ritual:
    "The ritual has three parts. All of our rites start with an offering."



    # This ends the game.
    return
