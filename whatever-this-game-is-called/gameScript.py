# story by Daniel Kim
# converted into proper format by Daniel Shin
script = {
  "t": [
    {
      "script": "Welcome to whatever this game is called.\nTry pressing the SPACE key to continue.",
      "character": "Tori",
      "action": "normal",
      "background": "black"
    },
    {
      "script": "Now if you hold the SPACE key down\nyou can speed the text up\nNeat, eh? Go ahead, try it."
    },
    {
      "script": "*squawk* *squawk* *squawk* *squawk* *squawk*\n*squawk* *squawk* *squawk* *squawk* *squawk*\n*squawk* Don't forget DL-6 — *squawk* *squawk*\n*squawk* *squawk* *squawk* *squawk* *squawk*"
    },
    {
      "script": "By the way, my name is Tori\nbecause the only reason I exist is to\ngive you this tutorial."
    },
    {
      "script": "You can also use the UP and DOWN keys\nto choose an option if presented with choices.\nGot it?"
    },
    {
      "script": [
        ("Yeah", "t_y"),
        ("No", "t_n"),
        ("Kinda...", "t_n")
      ]
    }
  ],
  "t_n": [
    {
      "script": "Let's try resetting.\nLooks like you need to rewind a bit..."
    },
    {
      "script": ("t",)
    }
  ],
  "t_y": [
    {
      "script": "Nice, you got it!"
    },
    {
      "script": "Now without further ado,\nhere is your interactive novel...\n(Story by Daniel Kim\nProgrammed by Daniel Shin)"
    },
    {
      "script": ("s0",)
    }
  ],
  "r": [
    {
      "script": [
        ("Restart from beginning", "s0"),
        ("Return to first decision", "s0_1"),
        ("Endings", "e"),
        ("Game Credits", "c"),
        ("", "ee")
      ],
    "character": "Ending"
    }
  ],
  "s0": [
    {
      "script": "One Spring Day\nSome Random High School",
      "character": "Narrator",
      "action": "None",
      "background": "school"
    },
    {
      "script": "I-I have a crush on you Ari!",
      "character": "Daisuke",
      "action": "shy"
    },
    {
      "script": "Please go out with me!"
    },
    {
      "script": "Here we have a pathetic attempt of a\nconfession to the girl, Ari.",
      "character": "Narrator",
      "action": "None"
    },
    {
      "script": "The man, Daisuke, has finally mustered up\nthe courage to ask her out, only for\nit to fold out like this."
    },
    {
      "script": "I-I’m sorry Daisuke-san,\nbut I cannot accept your confession…",
      "character": "Ari",
      "action": "shocked"
    },
    {
      "script": ("s0_1",)
    }
  ],
  "s0_1": [
    {
      "script": [
        ("Ah my apologies, sorry for taking up your time.", "s1"),
        ("Please consider again I’m begging you…", "s2"),
        ("Could I ask why?", "s3"),
        ("HOW COULD YOU!!!!!!!!!", "s4")
      ],
      "character": "Daisuke",
      "action": "normal",
      "background": "school"
    }
  ],
  "s1": [
    {
      "script": "Ah my apologies, sorry for taking up your time.",
      "action": "shy"
    },
    {
      "script": "Thank you for being so understanding.\nI’m sure one of my friends\nmight like a guy like you…",
      "character": "Ari",
      "action": "normal"
    },
    {
      "script": [
        ("Oh no that's ok, I was only interested in you.", "s1_1"),
        ("Who might that be?", "s1_2")
      ],
      "character": "Daisuke",
      "action": "normal"
    }
  ],
  "s1_1": [
    {
      "script": "Oh no that's ok, I was only interested in you.",
      "action": "shy"
    },
    {
      "script": "If that’s all you need to say to me,\nI’ll be heading back home now.",
      "character": "Ari",
      "action": "confident"
    },
    {
      "script": "Ah yea I’ll see you at school tomorrow,\nplease act like this didn’t happen at all.",
      "character": "Daisuke",
      "action": "normal"
    },
    {
      "script": "Well I guess it was worth a shot,\nthere's plenty of fish in the sea after all…",
      "action": "despair"
    },
    {
      "script": "The defeated Daisuke heads home in solitude,\nperforming coping mechanisms to himself\nalong the way.",
      "character": "Narrator",
      "action": "None"
    },
    {
      "script": "GENTLEMAN ENDING",
      "ending": "GENTLEMAN",
      "character": "Ending"
    },
    {
      "script": ("r",)
    }
  ],
  "s1_2": [
    {
      "script": "Who might that be?",
      "action": "thinking"
    },
    {
      "script": "She’s in class 3-A and\nher name is Yukino, she’s had a\ncrush on you for a while.",
      "character": "Ari",
      "action": "thinking"
    },
    {
      "script": "Oh well…",
      "character": "Daisuke",
      "action": "shy"
    },
    {
      "script": [
        ("I’ve never heard about her before\nso I’ll have to refuse, sorry.", "s1_2_1"),
        ("Oh I think she’s in the same club as me.", "s1_2_2")
      ]
    }
  ],
  "s1_2_1": [
    {
      "script": "I’ve never heard about her before\nso I’ll have to refuse, sorry.",
      "action": "confident"
    },
    {
      "script": "Oh what a shame…\nI was hoping you two could become close.",
      "character": "Ari",
      "action": "sad"
    },
    {
      "script": "Now if you’ll excuse me I need to leave now.\nThe bus is almost here.",
      "character": "Daisuke",
      "action": "normal"
    },
    {
      "script": "The defeated Daisuke heads home in solitude,\nmissing his second chance at love…",
      "character": "Narrator",
      "action": "None"
    },
    {
      "script": "DENSE AS A BRICK WALL ENDING",
      "ending": "DENSE AS A BRICK WALL",
      "character": "Ending"
    },
    {
      "script": ("r",)
    }
  ],
  "s1_2_2": [
    {
      "script": "Oh I think she’s in the\nsame club as me.",
      "action": "thinking"
    },
    {
      "script": "Oh so you do know her, that’s a relief…",
      "character": "Ari",
      "action": "normal"
    },
    {
      "script": "Expect something soon Daisuke…\nI’m rooting for you!",
      "action": "confident"
    },
    {
      "script": "W-wait! What do you mean by that!",
      "character": "Daisuke",
      "action": "despair"
    },
    {
      "script": "Ari prances away, leaving Daisuke alone\nto contemplate what just happened to him.",
      "character": "Narrator",
      "action": "None"
    },
    {
      "script": "SEQUEL? ENDING",
      "ending": "SEQUEL?",
      "character": "Ending"
    },
    {
      "script": ("r",)
    }
  ],
  "s2": [
    {
      "script": "Please consider again I’m begging you…",
      "action": "shy"
    },
    {
      "script": "What is there to consider, Daisuke.\nI do not have a romantic interest in you.",
      "character": "Ari",
      "action": "determined"
    },
    {
      "script": [
        ("*sigh* that’s fine then…", "s2_1"),
        ("PLEAAASEEEEE", "s2_2")
      ],
      "character": "Daisuke",
      "action": "shocked"
    }
  ],
  "s2_1": [
    {
      "script": "*sigh* that’s fine then…",
      "action": "despair"
    },
    {
      "script": "I’ll be on my way…"
    },
    {
      "script": "Hmph, better be off!",
      "character": "Ari",
      "action": "confident"
    },
    {
      "script": "And so the defeated Daisuke sluggishly walks\nhome, realizing that he should’ve just\ntaken no for an answer",
      "character": "Narrator",
      "action": "None"
    },
    {
      "script": "FRIENDSHIP RUINED ENDING",
      "ending": "FRIENDSHIP RUINED",
      "character": "Ending",
      "action": "None"
    },
    {
      "script": ("r",)
    }
  ],
  "s2_2": [
    {
      "script": "PLEAAASEEEEE",
      "action": "despair"
    },
    {
      "script": "HOW MANY TIMES DO I HAVE TO SAY NO",
      "character": "Ari",
      "action": "determined"
    },
    {
      "script": "*starts to cry heavily*",
      "character": "Daisuke",
      "action": "despair"
    },
    {
      "script": "Ew, weirdo.",
      "character": "Ari",
      "action": "shocked"
    },
    {
      "script": "The defeated Daisuke is left at school\nall alone as Ari runs away in fear of\nDaisuke’s broken mentality.",
      "character": "Narrator",
      "action": "None"
    },
    {
      "script": "OUTCAST AT SCHOOL ENDING",
      "ending": "OUTCAST AT SCHOOL",
      "character": "Ending"
    },
    {
      "script": ("r",)
    }
  ],
  "s3": [
    {
      "script": "Could I ask why?",
      "action": "thinking"
    },
    {
      "script": "I’m sorry Daisuke,\nI just don’t want a relationship currently…",
      "action": "sad",
      "character": "Ari"
    },
    {
      "script": [
        ("O-oh alright then, I respect your decision.", "s3_1"),
        ("But have I shown you my League of Legends\nskin collection?", "s3_2")
      ],
      "action": "normal",
      "character": "Daisuke"
    }
  ],
  "s3_1": [
    {
      "script": "O-oh alright then, I respect your decision.",
      "action": "shy",
    },
    {
      "script": "Thanks Daisuke, see you around!",
      "action": "confident",
      "character": "Ari"
    },
    {
      "script": "Aha… yea…",
      "action": "despair",
      "character": "Daisuke"
    },
    {
      "script": "The defeated Daisuke lost all confidence\nin himself with this rejection, never speaking\nto another woman about love ever again.",
      "action": "None",
      "character": "Narrator"
    },
    {
      "script": "BETA MALE ENDING",
      "ending": "BETA MALE",
      "character": "Ending"
    },
    {
      "script": ("r",)
    }
  ],
  "s3_2": [
    {
      "script": "But have I shown you my League of Legends\nskin collection?",
      "action": "confident",
    },
    {
      "script": "Oh, would you like to show me then?\nAt your house.",
      "action": "normal",
      "character": "Ari"
    },
    {
      "script": "With pleasure",
      "action": "confident",
      "character": "Daisuke"
    },
    {
      "script": "The successful Daisuke now walks away\nwith a girl beside him, towards his own home.",
      "action": "None",
      "character": "Narrator"
    },
    {
      "script": "TRUE ENDING",
      "ending": "TRUE",
      "character": "Ending"
    },
    {
      "script": "(Seriously Daniel...?)",
      "character": "Unknown"
    },
    {
      "script": ("r",)
    }
  ],
  "s4": [
    {
      "script": "HOW COULD YOU!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!",
      "action": "shocked"
    },
    {
      "script": "KYYYAAAAAAAHHHHH!!!",
      "character": "Ari"
    },
    {
      "script": "*Runs away*"
    },
    {
      "script": "*Furiously crying*",
      "character": "Daisuke",
      "action": "despair"
    },
    {
      "script": "The defeated Daisuke is later arrested for being\na public nuisance and sent to a mental asylum,\nnever to be heard from again.",
      "character": "Narrator",
      "action": "None"
    },
    {
      "script": "EMOTIONAL DAMAGE ENDING",
      "ending": "EMOTIONAL DAMAGE",
      "character": "Ending"
    },
    {
      "script": ("r",)
    }
  ],
  "e": [
  ],
  "ee": [
    {
      "script": "Huh? What's this?",
      "character": "Unknown",
      "action": "None",
      "background": "black"
    },
    {
      "script": "Someone actually found the easter egg."
    },
    {
      "script": "Hopefully you didn't cheat by\nlooking through the code."
    },
    {
      "script": "Regardless, congrats!\nHere's the 'Secret Ending.'"
    },
    {
      "script": "(It's actually a test script that\nI used for debugging...)"
    },
    {
      "script": ("ee0",)
    }
  ],
  "ee0": [
    {
      "script": "(Hmmm... that doesn't sound right)", 
      "character": "Pheonix", 
      "action": "thinking",
      "background": "court"
    },
    {
      "script": "(If I refer to Larry's statement back\nwhen I was at the school...)",
      "background": "school"
    },
    {
      "script": "(Something seems off...)"
    },
    {
      "script": "(Should I raise an objection?...)",
      "background": "court",
      "action": "normal"
    },
    {
      "script": [
        ("Raise an objection", "ee0_1"),
        ("Objection!!!", "ee0_1"),
        ("There's definitely a contradiction", "ee0_1")
      ], 
    }    
  ],
  "ee0_1": [
    {
      "script": "OBJECTION!!!",
      "action": "point"
    },
    {
      "script": "There is definitely a contradiction in the\nwitness' testimony just now, Your Honor",
      "action": "confident"
    },
    {
      "script": "Uh, where you ask?",
      "action": "abash"
    },
    {
      "script": "(Shoot, I lost my train of thought)"
    },
    {
      "script": "(Damn...)",
      "action": "despair",
      "background": "black"
    },
    {
      "script": "(Think Pheonix, think...\nWhat can I do?)"
    },
    {
      "script": "(Oh! I got an idea)",
      "background": "court",
      "action": "confident"
    },
    {
      "script": "My client is guilty af, Your Honor"
    },
    {
      "script": "SECRET ENDING",
      "character": "Ending",
      "ending": "SECRET",
      "action": "None"
    },
    {
      "script": ("r",)
    }
  ],
  "c": [
    {
      "script": "Game Credits",
      "character": "Tori",
      "action": "normal",
      "background": "black"
    },
    {
      "script": "Game created by the Daniel's",
      "background": "school"
    },
    {
      "script": "Idea by Daniel Kim\nStory by Daniel Kim",
      "character": "Daisuke",
      "action": "confident"
    },
    {
      "script": "Programming by Daniel Shin\nAssets editing by Daniel Shin",
      "character": "Ari",
      "action": "thinking"
    },
    {
      "script": "Assets from Ace Attorney Series\nGameplay inspired by Ace Attorney Series",
      "character": "Tori",
      "action": "normal",
      "background": "court"
    },
    {
      "script": "Thank you for playing!"
    },
    {
      "script": "This will lead you back to the\nbeginning of the game."
    },
    {
      "script": ("s0",)
    }
  ]
}