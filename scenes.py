SCENES = {

# =====================================================
# CHAPTER I — SHADOWS IN WINTERFELL
# =====================================================

"intro_winterfell": {
    "chapter": "Chapter 1",
    "bg": "assets/backgrounds/winterfell.jpg",
    "music": "assets/audio/winterfell.mp3",
    "title": "Shadows in Winterfell",
    "text": """
    <div class="narration">
    Snow drifts lazily across the courtyard of Winterfell.
    Jon Snow waits with Ghost at his side.
    </div>

    <div class="dialogue jon">
    <b>Jon Snow:</b> Someone tried to kill Tyrion last night.
    Daenerys is angry — but anger won’t find the truth.
    I need someone I trust. Will you help me?
    </div>
    """,
    "choices": [
        ("Agree to help Jon investigate.", "council_hall", {"jon_trust": 1}),
        ("Refuse — stay out of the conflict.", "ending_coward", {})
    ]
},

"council_hall": {
    "chapter": "Chapter 1",
    "bg": "assets/backgrounds/council.jpg",
    "music": "assets/audio/winterfell.mp3",
    "title": "The Great Hall",
    "text": """
    <div class="dialogue dany">
    <b>Daenerys:</b> Prove your gift for seeing through lies.
    Find who dared strike my Hand.
    </div>

    <div class="dialogue tyrion">
    <b>Tyrion:</b> And if you could prove I’m more useful alive,
    I would be deeply grateful.
    </div>
    """,
    "choices": [
        ("Speak with Sansa in private.", "talk_sansa1", {"visited_sansa_early": True}),
        ("Train with Arya.", "talk_arya1", {"visited_arya_early": True}),
        ("Visit Bran in the godswood.", "talk_bran1", {"visited_bran_early": True})
    ]
},

"talk_sansa1": {
    "chapter": "Chapter 1",
    "bg": "assets/backgrounds/winterfell.jpg",
    "title": "Sansa Stark",
    "text": """
    <div class="dialogue sansa">
    <b>Sansa:</b> Someone wants the Queen to doubt the North.
    That is the real game.
    </div>
    """,
    "choices": [
        ("Press her harder.", "night_ambush", {"sansa_trust": -1}),
        ("Assure her you trust her.", "night_ambush", {"sansa_trust": 1})
    ]
},

"talk_arya1": {
    "chapter": "Chapter 1",
    "bg": "assets/backgrounds/winterfell.jpg",
    "title": "Needle",
    "text": """
    <div class="dialogue arya">
    <b>Arya:</b> An amateur leaves noise.
    A professional leaves confusion.
    </div>
    """,
    "choices": [
        ("Train with Arya.", "night_ambush", {"arya_trust": 1, "asked_arya_for_help": True}),
        ("Keep your distance.", "night_ambush", {"arya_trust": -1})
    ]
},

"talk_bran1": {
    "chapter": "Chapter 1",
    "bg": "assets/backgrounds/godswood.jpg",
    "music": "assets/audio/godswood.mp3",
    "title": "The Three-Eyed Raven",
    "text": """
    <div class="dialogue bran">
    <b>Bran:</b> Time is a river.
    I can follow the ripples — if you wish.
    </div>
    """,
    "choices": [
        ("Accept the vision.", "night_ambush", {"saw_bran_vision": True}),
        ("Refuse.", "night_ambush", {})
    ]
},

"night_ambush": {
    "chapter": "Chapter 1",
    "bg": "assets/backgrounds/winterfell.jpg",
    "title": "Night Ambush",
    "text": """
    <div class="narration">
    That night, Winterfell feels wrong.
    Footsteps echo. A blade flashes.
    </div>
    """,
    "choices": [
        ("Survive the attack.", "after_ambush_report", {})
    ]
},

"after_ambush_report": {
    "chapter": "Chapter 1",
    "bg": "assets/backgrounds/council.jpg",
    "title": "After the Ambush",
    "text": """
    <div class="narration">
    The falcon pin changes everything.
    </div>
    """,
    "choices": [
        ("Report to Daenerys.", "library_sam", {"dany_trust": 1}),
        ("Report privately to Jon.", "library_sam", {"jon_trust": 2}),
        ("Speak to both together.", "library_sam", {"jon_trust": 1, "dany_trust": 1})
    ]
},

# =====================================================
# CHAPTER II — THE RAVEN'S SECRET
# =====================================================

"library_sam": {
    "chapter": "Chapter 2",
    "bg": "assets/backgrounds/library.jpg",
    "title": "The Raven's Secret",
    "text": """
    <div class="dialogue sam">
    <b>Sam:</b> Ravens from the Vale.
    Coded. Frequent.
    </div>
    """,
    "choices": [
        ("Study the ravens.", "decode_ravens", {})
    ]
},

"decode_ravens": {
    "chapter": "Chapter 2",
    "bg": "assets/backgrounds/library.jpg",
    "title": "Hidden Messages",
    "text": """
    <div class="narration">
    The cipher reveals a dangerous pattern.
    </div>
    """,
    "choices": [
        ("Ask Arya for help.", "messenger_interrogation", {"arya_trust": 1}),
        ("Ask Tyrion for help.", "messenger_interrogation", {"tyrion_trust": 1})
    ]
},

"messenger_interrogation": {
    "chapter": "Chapter 2",
    "bg": "assets/backgrounds/dungeon.jpg",
    "title": "The Messenger",
    "text": """
    <div class="narration">
    The truth breaks free.
    Jon Snow was the real target.
    </div>
    """,
    "choices": [
        ("Face the truth.", "truth_about_target", {"knows_target_is_jon": True})
    ]
},

"truth_about_target": {
    "chapter": "Chapter 2",
    "bg": "assets/backgrounds/winterfell.jpg",
    "title": "The True Target",
    "text": """
    <div class="narration">
    If Jon falls, the alliance falls.
    </div>
    """,
    "choices": [
        ("Tell Jon.", "travel_dragonstone", {"jon_trust": 2, "told_jon_truth": True}),
        ("Tell Daenerys.", "travel_dragonstone", {"dany_trust": 2, "told_dany_truth": True}),
        ("Tell no one yet.", "travel_dragonstone", {})
    ]
},

# =====================================================
# CHAPTER III — DRAGONSTONE DIVIDED
# =====================================================

"travel_dragonstone": {
    "chapter": "Chapter 3",
    "bg": "assets/backgrounds/dragonstone.jpg",
    "music": "assets/audio/dragonstone.mp3",
    "title": "Dragonstone Divided",
    "text": """
    <div class="narration">
    Black stone rises from the sea.
    Dragons circle overhead.
    </div>
    """,
    "choices": [
        ("Enter Dragonstone.", "audience_with_dany", {})
    ]
},

"audience_with_dany": {
    "chapter": "Chapter 3",
    "bg": "assets/backgrounds/dragonstone.jpg",
    "title": "Audience with the Queen",
    "text": """
    <div class="dialogue dany">
    <b>Daenerys:</b> Tell me plainly.
    Who is my enemy?
    </div>
    """,
    "choices": [
        ("Blame the Vale.", "grey_worm_warning", {"dany_trust": 1}),
        ("Blame the North.", "grey_worm_warning", {"dany_trust": -1}),
        ("Refuse to guess.", "grey_worm_warning", {"tyrion_trust": 1})
    ]
},

"grey_worm_warning": {
    "chapter": "Chapter 3",
    "bg": "assets/backgrounds/dragonstone.jpg",
    "title": "Grey Worm",
    "text": """
    <div class="dialogue greyworm">
    <b>Grey Worm:</b> Some do not trust the North.
    </div>
    """,
    "choices": [
        ("Argue for unity.", "forged_decree", {"jon_trust": 1, "dany_trust": 1}),
        ("Argue separation.", "forged_decree", {"dany_trust": -1}),
        ("Say little.", "forged_decree", {})
    ]
},

"forged_decree": {
    "chapter": "Chapter 3",
    "bg": "assets/backgrounds/dragonstone.jpg",
    "title": "The Forged Decree",
    "text": """
    <div class="dialogue tyrion">
    <b>Tyrion:</b> Someone forged the Queen’s seal.
    Jon Snow was meant to die quietly.
    </div>
    """,
    "choices": [
        ("Accuse the generals.", "return_north", {"accused_generals": True}),
        ("Accuse Tyrion.", "return_north", {"accused_tyrion": True, "tyrion_trust": -2}),
        ("Hold back.", "return_north", {"held_back_on_dragonstone": True})
    ]
},

"return_north": {
    "chapter": "Chapter 4",
    "bg": "assets/backgrounds/road.jpg",
    "title": "Return North",
    "text": """
    <div class="narration">
    You ride north as falcons gather.
    </div>
    """,
    "choices": [
        ("Continue.", "vale_ambush", {})
    ]
},

# =====================================================
# CHAPTER IV — THE VALE’S SHADOW WAR
# =====================================================

"vale_ambush": {
    "chapter": "Chapter 4",
    "bg": "assets/backgrounds/vale.jpg",
    "title": "The Vale Ambush",
    "text": """
    <div class="narration">
    Vale knights block the road, falcon sigils gleaming.
    </div>

    <div class="dialogue">
    “Our quarrel is not with you. We seek only the wolf who bows to dragons.”
    </div>
    """,
    "choices": [
        ("Order your men to fight.", "vale_prisoner", {"arya_trust": 1}),
        ("Let Arya strike from the shadows.", "vale_prisoner", {"arya_trust": 2, "supported_arya_plan": True}),
        ("Try to talk them down.", "vale_prisoner", {"attempted_peace": True, "jon_trust": 1})
    ]
},

"vale_prisoner": {
    "chapter": "Chapter 4",
    "bg": "assets/backgrounds/camp.jpg",
    "title": "The Prisoner",
    "text": """
    <div class="narration">
    A captured Vale knight spits blood into the snow.
    </div>
    """,
    "choices": [
        ("Press him for names.", "sansa_plan", {}),
        ("Question his beliefs.", "sansa_plan", {})
    ]
},

"sansa_plan": {
    "chapter": "Chapter 4",
    "bg": "assets/backgrounds/winterfell.jpg",
    "title": "A Choice of Shadows",
    "text": """
    <div class="dialogue sansa">
    <b>Sansa:</b> We draw them into the open and expose them.
    </div>

    <div class="dialogue arya">
    <b>Arya:</b> Or we end it quietly.
    </div>
    """,
    "choices": [
        ("Support Sansa’s political trap.", "final_council_intro", {"supported_sansa_plan": True, "sansa_trust": 2}),
        ("Support Arya’s covert strike.", "final_council_intro", {"supported_arya_plan": True, "arya_trust": 2}),
        ("Attempt a fragile peace.", "final_council_intro", {"attempted_peace": True, "jon_trust": 2})
    ]
},

# =====================================================
# CHAPTER V — THE LAST EMBER
# =====================================================

"final_council_intro": {
    "chapter": "Chapter 5",
    "bg": "assets/backgrounds/finale.jpg",
    "music": "assets/audio/finale.mp3",
    "title": "The Last Ember",
    "text": """
    <div class="narration">
    Wolves. Dragons. Falcons.
    The hall waits for your words.
    </div>
    """,
    "choices": [
        ("Step forward.", "final_choice", {})
    ]
},

"final_choice": {
    "chapter": "Chapter 5",
    "bg": "assets/backgrounds/finale.jpg",
    "title": "The Final Choice",
    "text": """
    <div class="narration">
    You can speak in many ways — but choose only one path.
    </div>
    """,
    "choices": [
        ("Call for unity under Jon and Daenerys.", "ending_unity", {}),
        ("Back Jon Snow.", "ending_jon", {}),
        ("Back Daenerys Targaryen.", "ending_dany", {}),
        ("Back Sansa Stark.", "ending_sansa", {}),
        ("Back Tyrion Lannister.", "ending_tyrion", {})
    ]
},

# =====================================================
# ENDINGS
# =====================================================

"ending_coward": {
    "bg": "assets/backgrounds/winterfell.jpg",
    "title": "The World Without You",
    "text": """
    <div class="narration">
    You walked away. Westeros burned anyway.
    </div>
    """,
    "choices": [("Play Again", "intro_winterfell", {})]
},

"ending_unity": {
    "bg": "assets/backgrounds/finale.jpg",
    "title": "The Wolf and the Dragon",
    "text": """
    <div class="narration">
    Against all odds, unity holds — fragile, but real.
    </div>
    """,
    "choices": [("Play Again", "intro_winterfell", {})]
},

"ending_jon": {
    "bg": "assets/backgrounds/finale.jpg",
    "title": "The Wolf at the Crossroads",
    "text": """
    <div class="narration">
    Jon Snow rules not as a king, but as a shield.
    </div>
    """,
    "choices": [("Play Again", "intro_winterfell", {})]
},

"ending_dany": {
    "bg": "assets/backgrounds/finale.jpg",
    "title": "Fire and Blood",
    "text": """
    <div class="narration">
    The realm holds — beneath dragonfire.
    </div>
    """,
    "choices": [("Play Again", "intro_winterfell", {})]
},

"ending_sansa": {
    "bg": "assets/backgrounds/winterfell.jpg",
    "title": "The Queen Who Remembers",
    "text": """
    <div class="narration">
    The North stands alone — and endures.
    </div>
    """,
    "choices": [("Play Again", "intro_winterfell", {})]
},

"ending_tyrion": {
    "bg": "assets/backgrounds/finale.jpg",
    "title": "The Hand in the Shadows",
    "text": """
    <div class="narration">
    Peace is written in margins, not songs.
    </div>
    """,
    "choices": [("Play Again", "intro_winterfell", {})]
},

"ending_bran_secret": {
    "bg": "assets/backgrounds/godswood.jpg",
    "title": "The River and the Stone",
    "text": """
    <div class="narration">
    For once, the future bends.
    </div>
    """,
    "choices": [("Play Again", "intro_winterfell", {})]
},

}