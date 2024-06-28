define y = Character("Yeni", color="#0390fc")
define u = Character("Urta", color="#fc8803")
define w = Character("??", color="#fc8803")
define m = Character("??", color="#6f03fc")
define t = Character("Tzeh", color="#8f0013")
define c = Character("Cheinan", color="#007519")
 
image yeni neutral = "Yeni_Neutral.png"
image yeni angry = "Yeni_Angry.png"
image yeni scared = "Yeni_Scared.png"

label start:
    # Part One: The Village

    scene village_720 with fade  # TODO: change image based on screen size/resolution

    play music bell_fade 

    queue music no_bell_fade loop

    show yeni neutral at left

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

    "As if my mother might have chosen differently, might have regretted her decision to cast me out..."

    "But only because of this. Only because of the inconvenience."

    "But I keep quiet, and sprinkle salt in the broth."

    "It's just easier this way. I can let my hands work of their own accord, pulling dried meat down from the rafters and shredding it to bits, then throwing it in the broth to soften."

    u "Now, you didn't come here on a pigeon's trip. Are you going to tell me why you're here?"

    y "It's... Well, it's better if I tell you after we eat."

    "I'm obviously already on icy ground with her. I don't want to also bring bad luck by sharing the news I have over a meal."

    "To my relief, my mother just nods."

    "We remain in silence until the soup is finished cooking and we've both eaten and Ari has fallen asleep nursing in her sling."

    "Now it's time for the real reason I came all this way, but I'm not sure how to start."

    "I decide to just show her. I go to the bag I left by the door, under my heavy overcoat. I reach inside and pull out the strange artifact."

    "It's a disk shaped like two soup bowls stacked one upside-down on the other. It's heavy and gray, but not made of any stone or metal I've ever seen before."
    
    "It has a strange gleam to it, almost like glass, and it's covered in these tiny grooves and raised circles that form a web-like pattern across the surface."

    "I've spent countless hours staring at it over the past week it took for me to travel here. But I still haven't been able to discern any pattern in these strange markings."

    "It feels familiar, but every time I try to focus on that sense of recognition, my focus slips and I find myself putting the strange thing away again."

    "When I bring it to my mother, I expect to see confusion in her eyes. Or curiosity, or even disdainful disinterest."

    "But instead her eyes grow wide, and she snatches it from my hands."

    u "Where did you get this?"

    "I'm so surprised by this that it takes me a moment to respond."

    y "From my husband. But I don't understand. You know what it is?"

    u "From you husband? When? How did he find this?"

    y "Last week, before he..."

    y "...before he died."

    "It takes me a moment to steady my voice before I can continue. Ari wakes and starts fussing and I rock her back and forth in the sling."

    y "He said his family had passed it down, waiting for the right time to use it for... something. He said he knew the time had come, but he was too sick to make the journey by then."

    y "That was his last request of me. That I finish what his ancestors started."

    "I look down at Ari. She's the only thing that's kept me moored, in the cold days of the past week."

    u "Oh, my girl!"

    "She crosses over to sweep me up in a hug. I feel my body stiffen, but I force myself to return the hug."

    "My eyes sting, and I squeeze them shut."

    "My mother sits back and holds me by the shoulders at arm's length for a moment, studying me with some concern in her eyes."

    "I don't trust my face not to betray me, so I look away."

    y "He asked me to bring it to the top of the holy mountain. He didn't tell me why. He just said there was a ritual I had to do with it once I got there."
    
    y "He kept saying it was important, more important than anything else."

    y "He made me promise. So I did."

    "My mother is tracing the grid on the disk with her fingers, her eyes unfocused. She speaks softly, as if to herself."

    u "I don't understand. After all this time, why now?"

    "I feel my teeth clench and unclench."

    y "What do you mean? What is this thing, what do you know about it?"

    u "You came to ask me if I'll go to the mountaintop with you. To see this through."

    y "I... Yes."

    u "Alright, then. We'll leave at dawn."

    u "Get some sleep. I'll pack for us."

    "I want to protest, to demand she explain what she knows."

    "But then Ari starts crying, and my mother is already standing up to lay out felts for us to sleep on."

    "It's another few days' journey to the mountain. We'll have nothing else to do but talk, and I'm going to get the answers I need."

    # Part Two: The Camp

    scene black with fade 

    stop music fadeout 2.0

    scene camp_720 with fade

    show yeni neutral at left

    play sound night_crickets loop

    # play fire/outdoors ambience 

    "After three days of travel, we approach the base of the tallest, holiest mountain."

    "The one the prophet herself ascended to receive her gifts."

    "The early summeryear weather is fair for traveling, but it has turned cold as we began to ascend in altitude."

    "We'll make camp here for the night, and begin the climb up the mountain in the morning."

    "We set up the shelter, then I go to collect grass and dry dung for the fire, with Ari strapped to my back."

    "When I return and build up the fire, my mother sets a pot of water and dried meat to boil over it."

    "I unwrap Ari from the swaddle and set her on her stomach on the felt floor."

    "She props herself up somewhat unsteadily, gazing between me and the grandmother she only met a few days ago. I give my daughter a wide smile."

    y "Who's that?"

    "Ari gurgles and coos in response."

    y "That's your momo. Tell her hi!"

    "My mother gives Ari a beaming smile, then a surprised look, and then a raised eyebrow. Ari gazes back with a look of consternation."

    "Then she reaches over and picks up Ari, sitting the baby up in front of her. Ari's arms flail about wildly and she graps at her grandmother's hands."

    "My mother makes silly faces until Ari giggles with glee, kicking her tiny feet."

    "I sit back on the cushion and stretch out my legs before the fire."

    u ".."

    hide yeni 

    "..."

    # show the camp scene by itself for a couple lines

    stop sound fadeout 2.0

    scene black with fade 

    "I don't know what it is, but as we've gotten closer to the mountain, little by little this uneasy feeling grows in the pit of my stomach."

    "Not even just the nervous anticipation of the unknown ritual we're about to conduct, or the trepidation of bringing Arizet to such a dangerous enviornment." 
    # TODO play eerie ringing sound 
    
    "But a low, steady humming that reverberates through my body. I feel like I can't quite sit still, I can't quite get comfortable enough to sleep." 
    
    "Pins and needles in my fingers, and a headache that won't go away." 

    play music foreboding fadein 2.0 loop
    
    "As I finally drift off to sleep, the images that play in my mind are... unsettling."

    
    "{i}The pins and needles bloom into a fiery crackle of lightning that shot through my hands, burning the ground, burning the air around me.{/i}" 
    
    "{i}And the smell, intimately familiar and awful. Blood and smoke, the smell of death.{/i}"


    # dream transition

    scene battle_720 with fade

    "{i}My men were fighting bravely, but I felt the battle turning against us. We were losing ground, losing men too fast.{/i}"

    "{i}I shot lightning enough to light the steppe like a thunderstorm. I felled soldier after soldier. It wasn't enough.{/i}"

    "{i}I reached for the relic in the bag at my hip, pulling from it to restore my energy.{/i}"

    "{i}We would not lose this battle. I led us here and through all the battles before. It would not be the Traitor King and his army of cowards that ended my reign. Not when I still had so much to accomplish.{/i}"

    c "{i}General!"
    
    "{i}I whipped my head around at the sound of Cheinan's voice, clear even over the din of battle, and saw her riding towards me.{/i}"
    
    c "{i}It's Vhiranzesh!{/i}"
    
    t "{i}What?? He’s here?{/i}"
    
    "{i}The Traitor King hasn't been in the grass of any of his battles since consolidating his power, I never thought I'd have a chance at killing him short of sacking the capital.{/i}" 
    
    c"{i}He’s on the riverbank, trying to escape. Tzeh, you have to catch him!{/i}"

    "{i}Without even waiting for a response, Cheinan was gallopping through the battlefield, knowing I would follow her.{/i}" 
    
    "{i}Distantly, I was aware of my second-in-command shouting for me to wait, to bring backup, but I could hardly hear him. I could hardly even hear battle anymore, the cries, the bellow of horses.{/i}" 
    
    "{i}I heard only the rush of blood in my ears, and the last words he said to me on that night, echoing...{/i}"

    "{i}\"...would be beneath me to kill you.\"{/i}"

    "{i}Cheinan tore through the battle, like a bird of prey.{/i}" 

    "{i}She always was the fastest rider of all of us. I always said I’d beat her in a race one day, but I never got the chance.{/i}" 

    "{i}Though I never minded. I preferred it that way.{/i}" 

    c "{i}Tzeh, catch up! Come on! If he crosses the river, we’ve lost him!{/i}"

    "{i}The route she led me on passed the line of battle into enemy territory, and she didn’t slow down for a moment.{/i}" 

    "{i}I didn’t either, urging my horse forward over every obstacle.{/i}"

    t "{i}Cheinan! We’re going north! The river is east.{/i}"

    c "{i}He won’t cross this far south, it’s too wide and the current too strong. We’ll catch him at the crossing point, it’s faster this way.{/i}"

    "{i}As we continued north, the river looped around to meet us, and my revenge drew closer. My justice.{/i}" 

    "{i}I nocked an arrow, feeling the lightning course through my hands and through the bowstring, through the arrow. I pictured myself aiming, over and over again, like I’d done for the past fifteen years.{/i}"

    "{i}One arrow through the abdomen. One through the neck. I wouldn’t draw out his suffering. I wouldn’t break the covenants of war.{/i}"

    "{i}But I wanted him to know it was me.{/i}"

    "{i}Suddenly, we came upon the slope down to the river. Cheinan pulled her horse to a stop, and I did the same.{/i}" 

    "{i}I scanned the bank, the narrow point of the river, the steppe beyond. All empty, except for me and Cheinan.{/i}" 

    t "{i}Cheinan. Where is he? He’s not here, where is he?{/i}"

    "{i}I felt panic gripping my chest. He’d gotten away. He was finally in my grasp and he’d escaped, it couldn’t be! I lowered my bow and spun my horse around to face Cheinan.{/i}" 
    
    "{i}What I saw confused me at first. Cheinan had her bow drawn, aimed at chest height. I turned to look over my shoulder. Had she seen something I had not?{/i}"
    
    "{i}Then I felt a sharp, searing pain in my chest. I must have lost my balance, the next thing I knew I was on the ground, on my back. I was confused, though I shouldn’t have been. It was a sensation I’d felt before.{/i}" 
    
    "{i}My vision was blurry as I looked up into the sky, aware in the periphery of Cheinan dismounting her horse and coming to kneel at my side.{/i}"
    
    t "{i}Chei...{/i}"
    
    "{i}Next I felt her open my outercoat, searching through my inner pockets. I weakly reached for the dagger at my belt, but she easily tore it from my hands and threw it far out of reach.{/i}" 

    t "{i}Chei... why... I don’t...{/i}"
    
    "{i}I didn’t have a lot of time. I didn’t know what else to ask her. It didn’t even matter why. It was already done.{/i}"
    
    c "{i}Kind of a risk, don’t you think? Bringing this into battle. What if it fell into enemy hands?{/i}"

    "{i}Cheinan lifted the disk from the satchel I had attached to my belt, and it disappeared in the folds of her own coat.{/i}"
    
    t "{i}No one could have... Could have...{/i}"
    
    "{i}My voice gurgled with liquid. Blood seeped from my mouth like drool, down my chin.{/i}"
    
    c "{i}Could have defeated you?{/i}"
    
    "{i}She lifted my head into her lap, and wiped away the blood from my lips with a finger, tenderly. I looked up into her face, thrown into shadow by the sun behind her.{/i}" 
    
    "{i}Like the first time I’d crossed the gate, and the kind Blue Ones scooped me into their arms and took me to their infirmary, tended my wounds, brought me back to life.{/i}" 
    
    "{i}Of all those who had spared me, who had saved me, who had betrayed me, who had died by my hand. It would be my own Cheinan that was my end.{/i}"
    
    "{i}It could have been no one else, I realized.{/i}" 
    
    "{i}Because I never could have fought her. Not even for my own life.{/i}" 
    
    "{i}Through my confusion and fading vision I heard the distant sounds of battle.{/i}"
    
    "{i}My men... what would happen to them... Without the relic to aid them, Vhiranzesh's forces would...{/i}"
    
    "{i}Why would she...{/i}"
    
    "{i}Why would...{/i}"

    # TODO use more of the battle sequence by having this take place on the battlefield itself, the battle turns because of the betrayal. 

    # have the battle start turning, then Cheinan leads her away a little bit but don't lean into the river description as much



    #back to camp

    scene camp_720 with fade

    show yeni scared at left

    stop music fadeout 2.0 
    
    "What was that??"

    "..."

    scene black with fade



    # Part Three: The mountaintop

    play sound wind_sound loop

    scene mountain_720 with fade

    show yeni neutral at left

    "And so, the climb begins."

    "Less than halfway up, the path becomes too irregular for the horses to continue."

    "Approaching the tree line, we tie our horses to one of the few remaining trees near a small brook."

    "The way we're travelling can't even properly be called a path at this point, since large stretches consist of climbing over boulders and winding through plants."

    "But soon the vegetation becomes even sparser, replaced by only rocks, and then snow and ice."

    "The air begins to thin, and we need to take breaks more and more frequently to catch our breath."

    "Each time I stand up from a rest and begin walking, I wind up out of breath again within a few minutes, my lungs stinging."

    "I feel nauseated, and even worse is my constant fear that the lack of air is even worse for Ari."

    "But we keep walking. Slowly, painfully."

    "When we finally reach the peak, I sink to my knees in the snow."

    stop sound fadeout 2.0

    "My whole body is trembling. It feels like all the grief and anger from the past year is hitting me all at once."

    "I just want to cry, or scream, or just grab fistfuls of snow until my hands turn numb and raw and sting with pain."

    "But I'm too dehydrated to and exhausted to cry. To do anything but sit here, and regain my breath."

    "My mother comes to stand next to me."

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

    scene portal_720

    show yeni scared at left

    play music portal_mp3

    "..."

    y "What is it??"

    u "It's a tear in the web..."

    y "A what??"

    # urta explains a little bit more

    "And then, blackness..."

    scene black with fade

    "Blackness, threaded through with multicolored light, and the sound of running water..."

    "..."

    scene mountain_720 with fade

    show yeni neutral at left

    stop music fadeout 2.0

    "The next moment I'm aware of myself, I'm lying in the snow, with a splitting pain wracking one side of my head. My arms are empty."

    y "Where's--??"

    "Then I see my mother sitting at my side, Ari in her arms."

    "I reach immediately to take my daughter."

    y "Hey, you're ok. I'm right here. Your mama's right here."

    "As I'm searching her face, I spot something that wasn't there before."

    "A small scar, with two lines intersecting in the middle, on Ari's left temple."

    "The skin is raised and dark red, but there's no blood. Like it was healed over the course of a day or two."

    "But I know it wasn't there the last time I saw her, which couldn't have been more than a couple minutes ago."

    "I feel a cold dread settle in the pit of my stomach."

    y "What happened?"

    u "You... I don't know. You both... you both disappeared for a moment."

    show yeni angry at left

    y "Disappeared? What do you mean, disappeared??"

    u "I don't know. That thing that came from the disk, it started getting bigger."

    u "It was like it... swallowed you. You and Ari both."

    show yeni neutral at left

    "A chill runs down my spine, and I squeeze Ari in my arms. It takes me a moment to find my voice."

    y "How did she get this? This scar. It wasn't there before."

    "My mother doesn't answer, and I feel anger rising in my throat."

    y "You knew about the disk. You agreed to come here even before I asked. Did you know this would happen?"

    u "No! No, I didn't know."

    # expand on the dialog between them

    "I rise unsteadily to my feet. Ari begins to cry in my arms."

    "The past year, all I'd wanted was for my mom to accept me again. For her to tell me she'd been wrong to banish me."

    "Now, I just wish I'd destroyed this cursed, evil disk immediately."
    
    "No matter how much my husband begged me on his deathbed to see this fool's errand through."

    "It's only just now that I realize, the object itself is nowhere to be seen."

    y "We'll go down the mountain. But I'm not going back to the village."

    y "Whatever that thing did to Ari, I'm going to find out."

    y "I'm going north. To the city."

    "My mother comes to stand beside me."

    u "Let me carry her a little ways. You'll need your strength."

return