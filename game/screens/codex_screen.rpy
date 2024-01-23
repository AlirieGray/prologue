
init python:
    codex_dict = {
        "History": {
            "The Prophet's Daughter": {
                "text": """Our beloved Tzeh was fierce in battle but gentle in words and demeanor. Many came from the distant reaches of the new empire to meet her and seek her wisdom, and she treated all these guests with the same grace and honor of her closest disciples. The guests were surprised to find Tzeh soft-spoken and mild, and that she rarely used her gifts except when necessary. She instructed us also to use the gifts only when necessary, warning us constantly of the great dangers of excess.\n\nIt was her youngest daughter Uli that did not heed her warnings. In the pride of youth, she sought after more than had been given to her. As she feasted on the immense power she was given to wield, her mind slipped further and further until she was beyond even her mother's grasp. I knew Uli as a girl, and she was always lively and gregarious. Now she wore a blank stare, interspersed with periods of madness where she lingered in visions that no one could understand, not even the Prophet.\n\nIt broke Tzeh's heart to lose her daughter in this way, to have to see her live in a waking state of emptiness. It pained me greatly to see Tzeh so despondent, and one day I attended to the girl to see if I might speak with her. At first she was blank-faced as usual, but then she turned to me and her eyes had a clarity and a menace that chilled me, she spoke in a voice that sounded not her own:\n\nYou make a mockery of things you do not understand, you are like children playing in the dirt. When the successor finds the conduit of the Miracle, the gate will open again and the weight of your folly will be brought to bear.\n\nI did not stay to hear if there was more the girl had to say. I fled, and from then on stayed clear of her.\n\n-Account of Mrena tl'Un, one of the honored disciples""",
                "revealed": False
            },
        },
        "Religion": {
            "Revelation on the Mysterious Beings": {
                "text": """Indeed, on the mountaintop a Gate was opened.\nAnd from the Gate there came a pure ringing, as if from great bells,\nAnd from beyond the Gate I was beckoned, as if by outstretched hands.\nAnd so I crossed, as if pulled by a string of light.\nIs this not a clear sign, for those of you who see?\n\nWhereupon I met with three of the Blue Ones,\nWho bid me to stay and drink from the healing water.\nAnd the water ran hot like the sun that burns away the mist,\nAnd washed away those wounds left by treachery and deceit.\nIs this not a clear sign, for those of you who see?\n\nWhereupon I was shown the wonders, which were blinding to the eye.\nAnd these wonders were that of knowledge and long life.\nIs that which is given to humanity also given to the Blue Ones,\nAnd that which is given to the Blue Ones also given to humanity?\nThey asked, did I not love the people who sent me?\nSurely this is a clear sign, for those of you who understand.""",
                "revealed": False
            },
            "Revelation on Magic": {
                "text": """Indeed, I was sent to return with a clear message, if only you knew,\nThat my people might all be amongst those who see.\nFor the children until 
                they learn to ride, remind them of the Realm of Wonders,\nAnd the Blue Ones who reside there.\nFor the children who have learned to ride,\nThen teach them 
                to focus their thoughts, like milk that runs through a sieve,\nUntil they too can see.\nAnd when they can see, then teach them to carry lightning,\nAs I have 
                shown you.\nAnd when your sons and daughters have married, \nThen it is given to them to refrain from the excess of power.\nFor surely there is great danger, 
                if you only knew.\n\n\nThe one who submits to the seduction of excess,\nIs more lowly than even those creatures which slither on the ground.\nSo refrain from 
                drunkenness and do not display your wealth,\nAnd do not boast with the lightning in your hands.\n\n\nAnd from amongst you, there must be one who can open the 
                Gate,\nAnd to her alone I will impart the secret,\nFor surely the Blue Ones know that which you do not.\nAnd have you not seen the wonders that they have 
                sent me with?\nSurely the falcon cannot write.""",
                "revealed": False
            },
            "Revelation on War": {
                "text": """On the tenth day of the winteryear, it is given that the land will be united
                \nFrom the Sacred Peak to the Northern Sea.
                \nAnd this land will be divided fairly amongst you,
                \nThat you might build halls of learning and wonders.
                \nIt is given that you should teach the children of distant lands as you do your own,
                \nThat they might also be of those who are united.
                \nSurely this is a revelation, for those of you who understand.\n
                \nIt is given that those of you strong of body and will
                \nShould draw your bows, both the women and the men.
                \nThat the land, already fractured and wounded,
                \nMight be healed as if in the marriage of two clans. 
                \nSurely this is a revelation, for those of you who understand.\n
                \nAnd take not prisoners of war, except that you grant them full rights in your clan.
                \nAnd dishonor not the women nor the men, for indeed this is a grave wrong.
                \nAnd spill not needless blood, for indeed amongst our enemies are those who see.
                \nSurely this is a commandment, for those of you who understand.""",
                "revealed": False
            }
        },
        "People": {
            "...": {
                "text": "....",
                "revealed": False
            }
        },
        "Places": {
            "Badour": {
                "text": "....",
                "revealed": False
            },
            "Kingdom of Suren": {
                "text": "....",
                "revealed": False
            },
        }
    }


    class CodexLibrary:
        def __init__(self):
            self.current_topic = "Religion"
            self.available_entries = ["Revelation on the Mysterious Beings", "Revelation on Magic", "Revelation on War"]
            self.current_entry = "Revelation on the Mysterious Beings"
            self.current_entry_text = codex_dict[self.current_topic][self.current_entry]["text"]

        def set_current_topic(self, topic):
            self.current_topic = topic
            self.current_entry = ""
            self.current_entry_text = ""
            self.available_entries = codex_dict[topic].keys()

        def set_current_entry(self, entry): 
            self.current_entry = entry
            self.current_entry_text = codex_dict[self.current_topic][self.current_entry]["text"]

    my_codex = CodexLibrary()



# Codex Screen
screen codex():
    tag menu
    predict False

    frame: 
        xmaximum 1600
        ymaximum 900
        xalign .5
        yalign .5
        hbox:
            vbox: 
                xpos .2
                ypos .1
                spacing 10
                for topic in codex_dict.keys():
                    textbutton topic action Function(my_codex.set_current_topic, topic)
            vbox:
                ypos .1
                xpos .15
                spacing 10
                for entry in my_codex.available_entries:
                    textbutton entry action Function(my_codex.set_current_entry, entry)
            vbox:
                ypos .1
                xpos .15
                ymaximum 900
                xmaximum 900
                viewport:
                    scrollbars "vertical"
                    mousewheel True
                    side_ysize 500
                    side_xsize 800
                    side_xpos 10
                    # side_ypos 10
                    # has vbox
                    vbox:
                        ymaximum 900
                        text my_codex.current_entry
                        text my_codex.current_entry_text
                        
