# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define y = Character("Yeni")
define u = Character("Urta")


# The game starts here.

label start:


    scene village_720 # TODO: change image based on screen size/resolution

    play music no_bell_fade

    show yeni_neutral at left

    "The sun has been up a couple hours. My husband "

    # show Urta at right

    u "Thought you could sneak out without anyone noticing, is that right?"

    menu:
        "What do I tell her?"

        "Lie":
            jump Lie

        "Tell the truth":
            jump Truth

    label Lie:
        ""

    label Truth:
        y "I'm sorry, Auntie. I have no options left here for my daughter. I have to go back to my own clan, while they're still in the summer gathering spot."

        y "It's my only chance."

    u "She's getting worse, then?"



    y "I can't escape this. I would do anything to save her."

    u "I know you fear for you child, my Yeni, but you have not felt the true depths that fear can reach."

    u "What you're seeking, what you're asking for, comes at a price you cannot begin to imagine."

    y "I understand, Auntie. But I have no other choice."





    #

    y "I've heard this story before. What more is there to tell?"

    # show urta sad/concerned

    stop music fadeout 2.0

    "For generations before Tzeh came to this life, our land had been fractured. Tzeh was born into a world that had known nothing but bloodshed for generations."

    "As Tzeh came of age, our steppe was ravaged by this era of war among clans."

    "Blood soaked the grasslands to marsh, and the memory of peace had turned an otherworldly dream."

    "Warring clans would raid their enemy leaving nothing in the aftermath of their devastation. Animals and farmland alike would be burned in their path, and all from the eldest to youngest of our people felt the agony of famine."

    "Tzeh was adopted into a small, passive clan as a young girl. She feared for their future, being surrounded to the north and the south by stronger, more warlike clans."

    "Since the dawn of time, all our people have honored our ancestral connection to Mratam Kah, the holiest of peaks in our sacred mountains."

    "But Tzeh had begun to feel the sacred peak calling to her. This call was unlike anything felt by her ancestors before her, nor any of us who have come after."

    "This call became a pull, and this pull began to gnaw at young Tzeh. While the warring world drew nearer to her clan, this ache of hers grew bigger."

    "As Tzeh's hunger grew, the day of the equinox neared. The equinox brought the promise of truce through marriage as the largest clan's chieftains agreed to marry their daughters and end this warring era."

    "However, the night before the equinox, our world changed forever."

    "An opportunistic clan, under the guise of night, slaughtered the Un clan leaving none but Tzeh alive. Elders, children, mothers, fathers: a brutal massacre on the very cusp of peace."

    "There was no grief. There was no mourning. There were no tears shed for her clan. There was nothing but swift and absolute vengeance."

    "As the moons set and morning neared, Tzeh ascended the sacred mountain which had called her name all her life."

    "What she found on the mountain remains unspoken, but when she descended she wielded an unworldly rage and the power of the gods themselves."

    scene battle_720 with fade

    "Tzeh found the clan which had massacred hers, and in turn this clan found no mercy in her vengeance."

    "Each clan on this steppe of ours found their chieftain's bloodlines ended that day."

    "Tzeh had unleashed an insatiable wrath upon our land. The skies blackened, the rains turned to ash, and our mountains shed the mournful tears which Tzeh herself had not."

    "The steppes themselves were left unrecognizable, scarred with gorges and deep wounds stretching from the mountains to the oceans, an everlasting memory of the bloodlust which broke apart our world."

    "When the darkness lifted, the survivors fell to the earth in awe and horror, and Tzeh became Mrat of the Steppe, the first and only leader of all our land."

    "Tzeh united the warring clans under her Mrat'im, which quickly grew to reach from the trading ports of the northern coast to the southern tundra."

    "It was not her mystical ability, nor her capacity for great violence, which drew our people so swiftly under her Mrat'im. No, it was her charisma and brilliance, unmatched but for the gods."

    "In her fiftieth sun, Tzeh was called once more to Mratam Kah. She returned to our sacred mountains to become the southerly wind, the winter frost, the aching chill of night. Tzeh was no longer of this earth."

    "Her Mrat'im then soon fell without her. The steppe was divided once again."

    "This is the story our people have held. We have openly and desperately awaited her return, praying for her to heal the scars on our land, to reunite us under her Mrat'im."

    "However, in the shadows, there are few of us who speak in hushed whispers of the raw evil Tzeh possessed, who hold memory of her bloodlust in our bones, who feel dread when we hear her name carried on the wind."

    "It has been told in our tradition that the abilities gifted to her that day on the mountains were a symbol of the gods blessing her as our leader. It pains me deeply to tell you that this could not be."

    "Tzeh's tie to the mountain is the only grace by which we have survived in this world. Her eternal bloodlust knows no bounds."

    "There are those of us across clans who have been performing our sacred duty, our secret ritual practice, to keep her at bay."

    "Each sun, as we age and lose our eldest to the ancestral realm, our strength here wanes. The gods, may they protect us, would not have done this. If the gods did this themselves, then they have forsaken us."

    scene village_720 with fade

    show yeni_neutral at left

    u "There is nothing but peril to be found on this path. My sacred duty is to protect our village, our people, our world from the horror Tzeh yearns to unleash upon all of us."

    u "I have no choice but to do everything in my power to prevent you from finding what you seek."

    # ............

    # trek across the steppe


    
    scene black

    play sound wind_sound loop
    
    # wind howling sound
    "And thus the climb begins."

    "One step."

    "Another."

    "Then another."

    "Hours pass this way, as we ascend into the clouds."

    "The wind threatens to break my spine. The bitter cold of the tundra below is incomparable to the mountain air. I now know why climbing our sacred Mratam Kah is a feat reserved for the gods."
    
    scene mountain_720

    show yeni_neutral at left

    "At long last, as the sun crests in the sky and begins to make its earthside return, I reach the peak."

    "At my chest, Arizet silently sleeps."

    # she does the ritual

    scene portal_720

    show yeni_scared at left

    "It's her!"

    "...."

    # sound effect

    return
