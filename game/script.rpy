# The script for a simple Ren'Py game.
# You can learn more about Ren'Py at https://www.renpy.org/

define p = Character("[player_name]")
define piffi = Character("Piffi")
define kee = Character("Kee")
define boop = Character("Boop")
define chase = Character("Chase")
define nief = Character("Nief")
define dev = Character("HitRecord")

# Image definitions
image bg discord_server = "images/discord_server.png"
image bg introductions_channel = "images/introductions_channel.png"
image bg voice_chat = "images/voice_chat.png"
image bg movie_night = "images/movie_night.png"
image bg dm_chat = "images/dm_chat.png"

# Blurred background images
image bg discord_server_blurred = im.Blur("images/discord_server.png", 10)
image bg introductions_channel_blurred = im.Blur("images/introductions_channel.png", 10)
image bg voice_chat_blurred = im.Blur("images/voice_chat.png", 10)
image bg movie_night_blurred = im.Blur("images/movie_night.png", 10)
image bg dm_chat_blurred = im.Blur("images/dm_chat.png", 10)

# Character images
image piffi = "images/piffi.png"
image kee = "images/kee.png"
image boop = "images/boop.png"
image chase = "images/chase.png"
image nief = "images/nief.png"

# Transforms
transform fit_screen:
    xysize (config.screen_width, config.screen_height)

transform center:
    xpos 0.5
    xanchor 0.5

transform big_center:
    xpos 0.5
    xanchor 0.5
    ypos 0.5
    yanchor 0.5
    xsize 1.2
    ysize 1.2

# The game starts here.
label start:

    play music "dokidoki.mp3" fadein 1.0 loop

    # Player name input
    $ player_name = renpy.input("What is your name?")
    $ player_name = player_name.strip() or "Player"

    show bg discord_server_blurred at fit_screen

    p "Wow, this server is really active. I should introduce myself."

    p "Hey everyone! I’m new here. Excited to join the community!"

    show piffi at big_center
    piffi "Welcome, [player_name]! I’m Piffi, one of the admins here. Feel free to ask if you have any questions."

    hide piffi
    menu:
        "Check out the #introductions channel":
            jump introductions_channel
        "Join the voice chat now":
            jump voice_chat

label introductions_channel:

    show bg introductions_channel_blurred at fit_screen

    p "Hi everyone! I’m [player_name], and I love gaming and coding."

    show kee at big_center
    kee "Hey [player_name], welcome! I’m Kee, another admin here. Nice to meet you!"

    hide kee
    show boop at big_center
    boop "Hi [player_name]! What games do you play?"

    p "I play a bit of everything, but I’m really into RPGs and strategy games."

    hide boop
    show chase at big_center
    chase "Nice to meet you, [player_name]. I'm Chase. Looking forward to seeing you around!"

    hide chase
    show nief at big_center
    nief "Welcome, [player_name]. I'm Nief. Don't get the wrong idea, I'm just being polite."

    hide nief

    jump voice_chat

label voice_chat:

    show bg voice_chat_blurred at fit_screen

    show piffi at big_center
    piffi "Oh hey, [player_name]! Glad you could join us."

    hide piffi
    show kee at big_center
    kee "Hey [player_name]! It's great to have you here."

    hide kee
    show boop at big_center
    boop "Hi [player_name]! We were just talking about the upcoming server event."

    hide boop
    show chase at big_center
    chase "Welcome, [player_name]! Any suggestions for the movie night this weekend?"

    menu:
        "Suggest a popular movie":
            p "How about a popular movie?"
            chase "That sounds like a great idea! Everyone loves a classic."
        "Suggest a niche indie film":
            p "How about a niche indie film?"
            chase "Interesting choice! It’ll be something new for everyone to experience."

    hide chase
    show nief at big_center
    nief "Glad you could join us, [player_name]. This is going to be a fun event. Not that I care or anything."

    hide nief

    jump end_scene1

label end_scene1:

    show bg discord_server_blurred at fit_screen

    "Later that evening, Piffi sends a private message."

    p "Hey Piffi! Yeah, everyone’s been really welcoming. Thanks for checking in."

    show piffi at big_center
    piffi "No problem! I wanted to personally make sure you’re feeling at home here."

    menu:
        "Thank Piffi for being so considerate":
            p "That’s really considerate of you, Piffi. Thanks!"
            piffi "You’re welcome! I always try to make sure everyone feels welcome here."
        "Ask Piffi more about themselves":
            p "So, Piffi, tell me more about yourself. How long have you been an admin here?"
            piffi "I’ve been an admin for about a year now. It’s been a lot of fun, and I’ve met some amazing people."
            p "That’s awesome! What do you enjoy most about being an admin?"
            piffi "I love organizing events and creating a positive community atmosphere."

    hide piffi

    jump server_event

label server_event:

    show bg movie_night_blurred at fit_screen

    show piffi at big_center
    piffi "Alright everyone, thanks for joining movie night! We’ve got a great lineup tonight."

    p "This is going to be great. Thanks for organizing this, Piffi."

    piffi "My pleasure, [player_name]! Let’s get started."

    hide piffi

    "The movie night goes smoothly, and everyone has a great time."

    jump confession

label confession:

    show bg dm_chat_blurred at fit_screen

    "After the movie night, Piffi sends another private message."

    show piffi at big_center
    piffi "Hey [player_name], did you enjoy the movie night?"

    p "It was fantastic, Piffi. You did a great job organizing it."

    piffi "Thanks! I'm glad you had fun. Actually, there's something I've been meaning to tell you."

    menu:
        "Ask Piffi what’s on their mind":
            p "What’s on your mind, Piffi?"
            piffi "Well, I’ve really enjoyed getting to know you, [player_name]. I think you’re amazing."
        "Confess that you’ve developed feelings for Piffi":
            p "Actually, Piffi, I’ve developed feelings for you. I really enjoy talking to you."
            piffi "[player_name], I feel the same way. I’m really glad you said that."

    show nief at big_center
    nief "Hold on a second, Piffi. [player_name], you can't just come in here and take Piffi away. Not that I care or anything, but... I've loved Piffi for a long time."

    p "Nief, I didn't know you felt that way, but I genuinely have feelings for Piffi."

    nief "It's not like I like you or anything! But... I guess if Piffi likes you, I can't do anything about it."

    piffi "Nief, you're a wonderful friend and I appreciate your feelings, but my heart belongs to [player_name]. I hope you can understand."

    nief "Fine! But if you hurt Piffi, I'll never forgive you!"

    hide nief

    p "Piffi, I promise to always cherish you and make you happy."

    piffi "I know you will, [player_name]. I'm looking forward to our future together."

    "The game ends with a romantic moment between Piffi and the player, setting the stage for future interactions and deepening their relationship."

    hide piffi

    jump ending

label ending:
    show bg discord_server_blurred at fit_screen

    dev "Hi there!"

    dev "Thanks for playing this game. I made it while half-asleep, so I hope you enjoyed it."

    dev "A special thanks to Nief for the dating sim idea. Without you, this wouldn't have been possible!"

    dev "Thanks for playing! Now enjoy a surprise video."

    stop music fadeout 1.0
    $ renpy.movie_cutscene("images/rick_roll.webm", delay=2, loops=0, stop_music=True)

    return