import markovify
import random
from textblob import TextBlob

f = open("corpus/J.R.R. Tolkien_The_lord_of_the_rings_djvu.txt")
file_contents = f.read()
text_model = markovify.Text (file_contents)

story = {
    "start": {
        "message": "Welcome, Frodo Baggins. Your task is to find Sauron's ring and destroy it before it falls into the wrong hands. Are you ready? a) Yes, b) Nope, count me out!",
        "keywords": ["Sauron", "ring", "destroy"],
        "a": "yes",
        "b": "no"
    },

    "yes": {
        "message": "As you leave the shire, you are tempted to put the ring on. Do you a) ignore your temptations and continue along your journey, or b) give in and put it on?",
        "keywords": ["shire", "ring", "temptation"],
        "a": "Aragon",
        "b": "corrupt end"
    },

    "no": {
        "message": "Too late! Gandalf has packed the ring in your bag and send you away from the shire. As you leave the shire, you are tempted to put the ring on. Do you a) ignore your temptations and continue along your journey, or b) give in and put it on?",
        "keywords": ["shire", "ring", "temptation"],
        "a": "Aragon",
        "b": "corrupt end"
    },

    "Aragon": {
        "message": "You arrive at the Prancing Pony in Bree and the ring accidentally slips on your finger! This alerts the ringwraiths. A man named Aragon warns you and urges you to hide in the stables. Do you a) trust him, or b) run away on your own?",
        "keywords": ["town", "inn", "hotel"],
        "a": "trust",
        "b": "boom end"
    },

    "trust": {
        "message": "There are three different paths infront of you. Would you like to explore a) Rivendell – the world of the elves, or b) Moria – the world of the dwarves?",
        "keywords": ["mountain", "paths", "scenery"],
        "a": "elf",
        "b": "dwarf",
    },

    "elf": {
        "message": "The sun has set and you need to set up camp near Rivendell. Do you a) light a fire and set up camp, or b) set up camp in the dark?",
        "keywords": ["elves", "hill", "Rivendell"],
        "a": "fire end",
        "b": "dark"
    },

    "dark": {
        "message": "The Elven princess Arwen welcomes you into their land. You are not sure if you trust them. Do you a) keep that thought to yourself, or b) whisper it into your companion Sam's ear?",
        "keywords": ["princess", "elf", "Arwen"],
        "a": "Arwen",
        "b": "caught"
    },

    "Arwen": {
        "message": "The elves welcome you into their library of extensive books and scriptures, where you learn about the history of the elven world, and even your own kind! Proceed by a) display gratitude to the elves.",
        "keywords": ["books", "library", "scriptures"],
        "a": "hills",
        "b": "hills"
    },

    "caught": {
        "message": "Arwen chuckled as she tells you how elves have incredible hearing and you find out that everyone heard you whispers to Sam! They brushed it off and the elves welcome you into their library of extensive books and scriptures, where you learn about the history of the elven world, and even your own kind! Proceed by a) display gratitude to the elves.",
        "keywords": ["hearing", "ears", "secrets", "elves"],
        "a": "hills",
        "b": "hills"
    },

    "dwarf": {
        "message": "You found a dwarf named Gimli right infront of the mines of Moria. He was about to go into explore the ancient home to the dwarves. He invites you to go along with him. Do you a) explore Moria with Gimli, or b) go into the mines alone?",
        "keywords": ["dwarves", "mines", "Moria"],
        "a": "Gimli",
        "b": "alone"
    },

    "Gimli": {
        "message": "As you and Gimli walk inside the mines, you discovered that a group of dwarves have been killed by an army of orcs that is charging at you! Do you a) run away, or b) pick up Gimli's sword and fight them with him?",
        "keywords": ["orcs", "dwarves", "blood"],
        "a": "run",
        "b": "fight"
    },

    "run": {
        "message": "You were blocked by an orc but Gimli noticed immediately and killed them for you. Proceed by a) display gratitude to Gimli and leave the mines.",
        "keywords": ["orcs", "run", "mines"],
        "a": "hills",
        "b": "hills"
    },

    "fight": {
        "message": "You managed to slash a few orcs while Gimli took care of the rest. All of the orcs have been slain and you can now leave safely. Proceed by a) display gratitude to Gimli and leave the mines.",
        "keywords": ["orcs", "dwarves", "blood"],
        "a": "hills",
        "b": "hills"
    },

    "alone": {
        "message": "As you walk inside the mines, you discovered that a group of dwarves have been killed by an army of orcs that is charging at you! Do you a) run away, or b) cry for help?",
        "keywords": ["orcs", "dwarves", "blood"],
        "a": "run away",
        "b": "cry"
    },

    "cry": {
        "message": "Gimli heard your scream and came to the rescue, killing all of the orcs while you helped with one of the dead dwarves' knife. Proceed by a) display gratitude to Gimli and leave the mines.",
        "keywords": ["scream", "orcs", "run"],
        "a": "hills",
        "b": "hills"
    },

    "hills": {
        "message": "You come across a wizard who is not Gandalf, and asks you to trust him with the ring. Do you a) trust him, or b) call for Gandalf immediately?",
        "keywords": ["snow", "icy", "tower"],
        "a": "Saruman",
        "b": "Gandalf"
    },

    "Gandalf": {
        "message": "You have come to the mountains of Mordor with Gandalf's assitance as the last part of your mission to destroy the ring in the fires of Mount Doom. After he leaves, creature Gollum stops you right infront of lava pit, demanding the ring. Do you a) brush him off and race him to the pit, or b) push him into the pit before dropping the ring in afterwards?",
        "keywords": ["Gandalf", "rescue", "fight", "Saruman", "Mordor", "fire"],
        "a": "Gollum",
        "b": "win"
    },

    "win": {
        "message": "Gollum dies after 500 years of torment by the ring's temptation, and you successfully dropped the ring into the fires of Mount Doom. Your mission was a success! Congratulations! The end.",
        "keywords": ["fire", "destroy", "success"],
        "exit": True
    },

    "corrupt end": {
        "message": "Sauron's ring corrupts your soul and you die from the overflow of dark power! Game over.",
        "keywords": ["corrupt", "soul", "death"],
        "exit": True
    },

    "boom end": {
        "message": "The ringwraiths caught up, took the ring from you, and killed you. Game over.",
        "keywords": ["ringwraiths", "knife", "horse"],
        "exit": True
    },

    "fire end": {
        "message": "The ringwraiths noticed the camp fire and raided your camp. They killed you and took the ring. Game over.",
        "keywords": ["fire", "raid", "hill"],
        "exit": True
    },

    "run away": {
        "message": "You were blocked by a bunch of orcs and they killed you in an instant. Game over.",
        "exit": True
    },

    "Saruman": {
        "message": "Once you hand over the ring, the wizard reveals himself as Saruman, who works with the ringwraiths. They get ahold of the ring and your mission has failed. Game over.",
        "keywords": ["wrong", "Saruman", "fail"],
        "exit": True
    },

    "Gollum": {
        "message": "Even though you brushed him off, he crawls faster than you can walk. He catches up and runs off with his precious ring. Your mission has failed. Game over.",
        "keywords": ["Gollum", "precious", "fire"],
        "exit": True
    },
}

game_state_key = "start"

while True:
    game_state = story[game_state_key]

    is_match = False
    while not is_match:
        sentence = text_model.make_sentence()
        random.shuffle(game_state["keywords"])
        for w in game_state["keywords"]:
            tb = TextBlob(sentence)
            if w in tb.words:
                is_match = True
    print(sentence)
    print(game_state["message"])
    if "exit" in game_state:
        exit()

    valid_input = False
    while not valid_input:
        choice = input("> ")
        if choice.lower() == "a":
            valid_input = True
            game_state_key = game_state["a"]
        elif choice.lower() == "b":
            valid_input = True
            game_state_key = game_state["b"]
        else:
            print("Error, please select ")
