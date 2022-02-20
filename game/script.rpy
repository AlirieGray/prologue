# CHARACTERS
define y = Character(_("Yeni"), color="#5a0ee7")
define u = Character(_("Urta"), color="#683904")
define t = Character(_("Tzeh tl'Un"), color="#98f8ff")


# START
label start:
    #### ACT ONE ####

    scene bg_village
    show yeni_neutral at left
    show urta_neutral at right

    u "Absolutely not."

    show yeni_worried at left

    "Her words stung."

    y "Please, Auntie. You're my last hope. If I lost Ari, I think I'd die."

    show yeni_neutral at left

    u "I know. You're just doing what you feel you have to for your daughter."

    u "But what you're asking for, I don't even think it's possible. Let alone a good idea."

    u "I've given her what help I can already. The herbs will help, but I can't offer you the certainty you're looking for."

    y "You always said there was great power in the steppe, in the mountains."

    y "You told me it could help me in my darkest times, if I just asked for it."

    y "I'm asking you now. Show me the ritual. I know where to go, just show me how to call--"

    show urta_angry at right
    show yeni_worried at left

    u "TZEH TL'UN IS NOT TO BE TRIFLED WITH!"

    "Suddenly her voice is thunderous. I feel static fill the air around me."

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

    scene bg_village 
    show yeni_neutral at left
    show urta_neutral at right

    u "Do you understand now?"

    "The story unnerves me, but Auntie Urta's moralizing tale isn't going to dissuade me now."

    "If she won't help me, I'll find my own way."

    #### ACT THREE ####

    scene painting_steppe

    "The last bands of orange light give way to blackness on the horizon, and the sounds of the village have died down as people retire for the night."

    "I swaddle Arizet in more layers than I normally would and wrap her tight to my body before pulling a thick cloak over both of us and strapping a travelling pack of dried food and a waterskin to my back." 

    "It's warm this far north, even at night. But the farther we get from the coast and the closer to the mountains, the colder and harsher it'll be, even when the sun comes up."

    "Arizet is unnaturally silent for an infant, and far too pale. She doesn’t make a noise as I slip out of the house and make my way to the edge of the village."

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

    "After eating the food in the pack, I shake the cloth out and wrap it around my shoulders as another layer against the cold."

    "I stand back up, and orient myself using the unique peaks of the mountains as landmarks."

    "It's easy to orient myself, it comes naturally as if I'd left home yesterday." 
    
    "Last night as I made preparations to leave, I had been worried I'd forgotten how to find my way on the steppe, and would wind up wandering until I died of thirst."

    "But that fear was far overshadowed by the fear of losing Arizet."

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


    #### ACT THREE ####

    scene bg_mountain

    "I tuck Ari closer to my body, covering her from the harsh winds with my cloak."

    "The air grows thin, and every breath stings with cold and effort."

    "I’m sweating from exertion, but every time I stop to catch my breath, it cools instantly on my skin, turning into an icy chill under my thick clothes."
    
    "My boots are soaked through with snow, burning my feet with every step, and I nearly slip and fall several times."
    
    "I grit my teeth and focus on one step after the one. One foot, then the other. One foot, then the other."
    
    "Hours pass this way, the sun grows high, though still cold in the pale sky. It reflects off the snow and burns my eyes."
    
    "One foot, then the other. I have to reach the top before the night chill sets in. I’ll never make it back down if that happens. I’m not even sure how I’ll make it back down as it is. "
    
    "It only occurs to me halfway up the mountain that I’m crazy, though that’s what Urta was trying to tell me, back at the village."
    
    "I’m betting my life on a threadbare chance that a warrior prophet out of ancient fable is waiting for me at the top of this climb, and that she’s going to be willing to help me for some reason."
    
    "I can’t think about that now, though. This is my only chance. If there was any other way to save her, I would have taken it."
    
    "Finally, as the sun crests in the sky and begins its fall to earth, I reach the top of the mountain."
    
    "I throw my pack on the ground and rest on it, taking heaving breaths. For a second, I’m so absorbed in my own exhaustion and relief that I don’t even notice it."
    
    "The Threshold."
    
    "It just looks like a hazy spot about six feet of the ground at first, like the blur around a cooking fire. But as my breath steadies, I notice something else in the air. Like static electricity."
    
    "The hazy spot shifts when I try to look at it, like I can’t focus my eyes on it."
    
    "This is it."
    
    "I reach into my pack and pull out the offerings I’ve brought, and array them on the ground before me."
    
    "I sit cross-legged on the ground, below and a few feet in front of the hazy spot."
    
    "I spent so much time thinking about how I’d get here that I didn’t really consider what I’d do one I got here.""


label ritual:
    "The ritual has three parts. All of our rites start with an offering."



    # This ends the game.
    return
