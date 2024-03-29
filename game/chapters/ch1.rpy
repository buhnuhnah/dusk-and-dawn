label ch1:
    scene warehouse night
    show stoneman neutralsmile at center with dissolve
    st "Alright, Dusk, keep moving! We're almost at the warehouse!"
    show stoneman at offscreenleft with ease
    show bolt neutral onlayer mc at side with dissolve
    "Moonlight falls on the windowless building before us. The industrial area is dark at night, so unlike the rest of the city."
    "I suppose there is no point in lighting a building at night whose only purpose is to store items and datasticks."
    "There are no humans working here, except for the guards."
    "They are equipped with flashlights, making them easy targets. So they won't be working here very long."
    "I teleport behind the nearest guard. Even in the darkness, it's easy to guess where to strike."

menu:
    "Knock him out":
        $ bastion += 5
        jump knock_warehouse
    "Kill him":
        $ villain += 5
        jump kill_warehouse

label knock_warehouse:
    play sound "zap.mp3" volume 0.4
    "I give him a heart zap with the paralyzer. Just like that, he was out like a light." with flash
    "Chances are, he might wake up later and throw us for a loop. It's happened before. If this all comes back to bite us later..."
    show bolt surprised onlayer mc
    "In the middle of my thoughts, I feel a light tap on the shoulder."
    show stoneman happy at center with dissolve
    st "Good job, Rene! I know we're dealing with the same guards over and over again, but..."
    show bolt neutral onlayer mc
    st neutralsmile "The no-kill policy is one of the only things separating us from them. And you have to remember: these people have families too, y'know?"
    "He's right. These people are just working their jobs. After flashing me his dorky little smile, he turns."
    show stoneman at offscreenleft
    with ease
    jump warehouse

label kill_warehouse:
    $ murder = True
    "If I don't kill him here we'll have to fight him again on the next mission. It's been like that before and I'm sick and tired of it."
    show bolt angry onlayer mc
    play sound "slap.mp3" volume 0.8
    "I snap the man's neck." with sshake
    show frostbite surprised with dissolve
    f "Bolt!"
    show bolt neutral onlayer mc
    "Frostbite is shocked to see what I did."
    show frostbite angry
    f "What the hell are you doing?!"
    b "I'll explain myself later. Focus on the fight."
    hide frostbite with dissolve
    jump warehouse

label warehouse:
    hide bolt onlayer mc with dissolve
    "Guard 1" "What the fuck! Who's there?!"
    show bolt surprised onlayer mc at side with dissolve
    "His voice is too close for comfort. I whirl around but before I can react, I feel the coldness in the air."
    show frostbite neutral at center with dissolve
    "Frostbite is right by my side. She touches the guard and freezes his hand with her ice powers."

menu:
    "Knock him out":
        $ bastion += 5
        play sound "zap.mp3" volume 0.4
        "I zap him with my paralyser and he falls to the ground, unconscious." with flash
        hide frostbite with dissolve
        "I see Bastion take notice, and he flashes me a thumbs up."
        jump warehouse2
    "Kill him":
        $ murder = True
        $ villain += 5
        play sound "slap.mp3" volume 0.8
        if villain > 5:
            "I snap his neck too. I relish the feeling of his body going limp in my hands." with sshake
        else:
            $ spare1kill2 = True
            "I snap his neck. I relish the feeling of his body going limp in my hands." with sshake
        show frostbite sad with dissolve
        "Frostbite looks terrified and about to puke, but I just gesture for her to continue with the fight."
        hide frostbite with dissolve
        jump warehouse2

label warehouse2:
    hide bolt onlayer mc with dissolve
    "Guard 2" "It's Dusk, we are under attack!"
    show bolt neutral at side onlayer mc
    show stoneman neutralsmile at left
    show frostbite neutral at right
    with dissolve
    "Dusk - that's us. Three friends with special powers who formed a superhero team."
    show frostbite at center with ease
    show mia neutral at right with dissolve
    "And then there's Mia, our hacker."
    "Currently we are here to secure a package from this warehouse."
    "The building and the items stored inside are owned by the enemies of our organisation - Dawn."
    show stoneman happy
    st "Take this!"
    "With a smile on his face Stoneman, our leader, punches the last guard and knocks her unconscious." with sshake
    "He has the power to turn his skin to stone. It's hard to hurt him and his punch is powerful."

    if villain == 0:
        jump no_wkills
    else:
        jump wkills

label no_wkills:
    f annoyed "Aren't you a bit too happy about fighting?"
    show stoneman neutralsmile
    st "Oh, well... I just can't help it, y'know? I'm pretty good at the whole \"fighting evil\" thing!"
    st "Well, compared to everything else..."
    show bolt happy onlayer mc
    b happy "I see someone needs a boost to their ego!"
menu:
    "Say something nice to raise Stoneman's confidence":
        $ bastion += 5
        jump boost_ego
    "Say something funny to lighten the atmosphere":
        jump make_joke

label boost_ego:
    b "No worries, Stoneman! You are a capable person outside of fights too!"
    show stoneman shy
    st "Haha... wow, uh... thanks, Bolt! You know, you're not too bad yourself-"
    m annoyed "Enough with the flirting!"
    show bolt shy onlayer mc
    b "...flirting? I'm not...!"
    show stoneman neutralsmile
    show bolt neutral onlayer mc
    show mia neutral
    jump warehouse3

label make_joke:
    show bolt happy onlayer mc
    b "You should make a rock garden. So that you can grow {i}boulder{\i}!"
    f annoyed "Oh god why..."
    m annoyed "That wasn't funny at all..."
    show stoneman happy
    st "Haha! Oof... I felt that one..."
    b "Sorry guys!"
    show bolt neutral onlayer mc
    show stoneman neutralsmile
    show frostbite neutral
    show mia neutral
    jump warehouse3

label wkills:
    f sad "Bolt...she..."
    show bolt angry onlayer mc
    show frostbite surprised
    show stoneman surprised
    b "Later, Frostbite!"
    "I snap at her and she takes a step back."
    st "What is going on?"
    show bolt happy onlayer mc
    b "Nothing."
    show bolt neutral onlayer mc
    show stoneman neutralfrown
    show frostbite neutral
    jump warehouse3

label warehouse3:
    m neutral "Done! I've hacked and disabled their alarms."
    m "You should be able to open the doors without alerting their headquarters."
    show stoneman happy
    st "Good job, Mia! Thank you!"
    m "...don't worry about it... I'm just doing my job..."
    f annoyed "Let's continue with the mission! The sooner we can find the package, the less risk we run into Dawn."
    "Dawn is a supervillain team. Our enemies. There are three of them, and lately we've run into them way too often."
    "Unlike those guards they pose a real threat. I hate to admit it but their superpowers equal our own."
    show stoneman neutralfrown
    "We enter the building. Boxes are piled upon boxes all the way to the ceiling."
    show bolt surprised onlayer mc
    b "That's a lot of packages! How do we find the right one?"
    m "The measurements are 31 x 23 x 26 inches. Weight should be around 4 pounds..."
    show bolt neutral onlayer mc
    st worried "Most boxes here are around this size."
    f sad "The packages are marked by letters and numbers... do we know what signature we are looking for?"
    m "C15467YZ. I'll send it to your holo watches."
    b "Hopefully there is some pattern to the way things are organized here."
    st neutralsmile "Let's spread out. I'll take the right side, Bolt you take the left and Frostbite the back."
    f neutral "Alright."
    b "On it, leader."
    m "And I'll look for some sort of inventory document. There must be one. It will be classified for sure."
    m "Hopefully I can crack it quickly."
    st "Good luck everyone."
    hide stoneman
    hide frostbite
    hide mia
    with dissolve
    "I open the holo display of my watch. It glows a warm orange hue and shows the signature above my wrist."
    "Looking at it I compare it to the labels on the boxes, trying to find a pattern."

    "..."

    "It takes me a while but finally I figure out how the warehouse is organized. If I'm right the package is not on my side."
    show mia neutral at center with dissolve
    m "Found the inventory document. Now to crack this... I need some time."
    hide mia with dissolveRR
    "I turn to rejoin the others and to talk to them about the pattern I found."
    "Just then I hear the sounds of fighting from Frostbite's side of the warehouse."
    "I run there as quickly as I can. When I'm closer I realise what is going on immediately."
    "The red and black uniforms of Dawn flash before my eyes."
    "It's our enemies... why again? We were so quiet and efficient!"
    show stoneman at offscreenright
    show magno angry at left
    show frostbite hurt at right
    with dissolve
    ma "Take this, you bitch!"
    "The chains that Magno, the leader of Dawn, manipulates in the air hit Frostbite straight in the chest."
    "He manipulates gravity and for some reason he likes to fight with those clunky metal chains."
    f "Oof!" with sshake
    "Frostbite grabs her arm. She's hurt but it seems she can still fight. It's not that bad, at least we can heal quickly."
    show bolt surprised onlayer mc
    b "Frostbite!"
    "I run closer and phase the last stretch, appearing behind Magno. I jab him with my paralyser."
    show bolt angry onlayer mc
    play sound "woosh.mp3" volume 0.4
    "The chains try to wrap around me but I teleport again before I'm caught." with woosh
    show stoneman angry at center
    show snapshot at offscreenright
    hide magno
    hide frostbite
    with dissolve
    st "Dawn!"
    play sound "<from 1.0>gunshots.mp3" volume 0.8
    "Stoneman runs up to us but before he can join the fight, a spray of bullets hit in front of his feet."
    stop sound fadeout 1.0
    show stoneman surprised at left
    show snapshot happy at right
    with ease
    sn "I will be your opponent today!"
    "That's Snapshot, whose superpower is high accuracy. She shot the ground on purpose to stop Stoneman."
    "She could have hit him square in the chest if she wanted to."
    st determined "Very well."
    show bolt neutral onlayer mc
    "Both Magno and Snapshot are here, so that only leaves..."
    hide stoneman
    hide snapshot
    show shadow neutral at center
    with dissolve
    sh "Hello, Bolt."
    "I hear his voice behind me. Shadow. As usual he wanted to be unseen, hidden in the darkness. Even I didn't notice him."
menu:
    "Duck":
        jump duck
    "Phase away":
        $ samuel += 5
        jump phase

label duck:
    "His attacks are usually predictable. His strength lies in his ability to wrap shadows around himself and disappear from sight."
    play sound "<to 1.0>punch.mp3" volume 0.6
    "I hope for the best, quickly ducking as a fist flies a mere inch above my head."
    "But before I can react, I feel him kick my legs out from under me." with hit
    show shadow angry
    sh "What, not giving me a challenge today? Why are you not being serious?"
    show bolt happy onlayer mc
    b "That was a lucky shot!"
    jump warehouse4
label phase:
    play sound "woosh.mp3" volume 0.4
    "Expecting the blow I quickly phase out further away." with woosh
    "I whirl around and indeed Shadow is standing there, his fist where my head was a moment ago."
    show shadow happy
    sh "I see you are in top form."
    show bolt happy onlayer mc
    b "Always."
    jump warehouse4

label warehouse4:
    show bolt neutral onlayer mc
    "He is an opponent I enjoy fighting with. Both physically and with words."
    "Wait... why am I happy to see the enemy?"
    hide shadow with dissolve
    "Shadow hides in darkness again. Meanwhile Magno and Frostbite are fighting it out."
    show mia neutral at center with dissolve
    m "I know where the package is. It's not far away from Frostbite's location."
    "We all hear Mia's voice right in our ears through the communication devices."
    show stoneman neutralfrown at center
    hide mia
    with dissolve
    st "She can't secure it now that Dawn is here. We should abort the mission."
    b "No! I can cover Frostbite while she grabs the box!"
    show stoneman surprised
    st "Are you sure? It's dangerous!"
    b "It will be fine."
    show stoneman determined
    st "Ok, if you say so. Bolt, cover Frostbite. Frostbite, grab the package."
    hide stoneman
    with dissolve
    "We both confirm receiving orders. I phase in closer to Frostbite and try to get Magno's attention off her."
    show magno angry at left
    show frostbite neutral at right
    with dissolve
    play sound "zap.mp3" volume 0.4
    "I zap Magno with my paralyser and Frostbite starts running to acquire the box." with flash
    ma "Not so fast, you bitch!"
    show bolt angry onlayer mc
    b "Hey I'm right here! I'm the one you have to fight now!"
    show frostbite neutral at farright with ease
    show shadow neutral at rightish with dissolve
    "But as I see Frostbite find the right package and start pulling it out, Shadow appears behind her, ready to punch."
    play sound "woosh.mp3" volume 0.3
    "I teleport there as quickly as I can and zap him in the back. He turns around and throws a kick at me, which I dodge." with flash
    play sound "hit.mp3" volume 0.6
    "Only to get smashed hard in my kidney by Magno's chains." with hit
    show bolt surprised onlayer mc
    b "Ouch!"
    f surprised "I've got the package! I'm getting out of here, cover me!"
    "As Frostbite runs past Shadow she freezes his boots to the ground so he can't follow."
    hide frostbite with dissolve
    "Before I can phase out, Magno wraps his chains around me."
    "He tightens them to the point that I feel like they are going to crush my lungs."

    scene warehouse night
    show bolt hurt onlayer mc
    show shadow sad at right
    show magno angry at left
    with Fade(0.25, 0.5, 0.15)
    "One end of the chain is wrapped around my throat."
    "I can't use my powers while being in such close contact with the abilities of another super."
    "Snapshot is getting closer and closer to the door, not noticing what is going on. Stoneman is occupied too."
    "I can't breathe...!"
    scene warehouse night
    show shadow sad at right
    show magno angry at left
    with Fade(0.25, 0.5, 0.15)
    "I look through my teary eyes at Shadow. He's looking at me with determination and... pain..."
    "He breaks out of Frostbite's hold. Her powers grow weaker the further she is from the target and now she's almost at the door."
    show shadow angry
    sh "Stop it, Magno! You're killing her!"
    "He is... concerned about me? But... he's on the opposite side of the fight?"
    show shadow at right with ease
    show magno angry at left with dissolve
    ma "So what! The bitch can die for all I care! She is our enemy!"
    sh "Since when are we murderers?!"
    "They are fighting over me. But Magno does not loosen the chains and I start losing consciousness."
    play sound "<to 1.0>punch.mp3" volume 0.6
    "I can't believe it when I see Shadow punching Magno. The chains fall to the ground." with hit
    scene warehouse night with Fade(0.5, 0.5, 0.25)
    show stoneman surprised at center with dissolve
    st "Bolt!"
    "Stoneman's concerned face comes into my view. He takes me in his arms and starts running to the exit."
    scene black with fade
    "That's the last thing I remember before I passed out, exhausted."
    hide bolt onlayer mc

    scene dusk base
    show bastion neutralfrown at left
    show mia angry at center
    show alicia neutral at right
    show rene neutral at side onlayer mc
    with Fade(1.0, 1.0, 0.5)
    m "That was beyond stupid!"
    a "I have to agree with Mia."
    ba surprised "But the mission was a success."
    a annoyed "At what cost! Rene, she..."
    "I come to my senses to see the rest of my team arguing about me."
menu:
    "Remind them it was your idea":
        jump my_idea
    "Snap at Alicia":
        jump snap_alicia

label my_idea:
    show bastion neutralfrown
    r "Guys... it was my idea."
    a "Not your brightest moment."
    ba angry "Come on now, Alicia. Don't talk down to her. She knows we have her back."
    jump scene2
label snap_alicia:
    show rene angry onlayer mc
    r "At least I'm brave enough to do my job, Alicia."
    a "Your job isn't to die."
    ba neutralfrown "Calm down, you two."
    jump scene2

label scene2:
    show rene neutral onlayer mc
    show bastion neutralfrown
    r "As Bastion said, it made the mission a success. I can take a bit of pain for the team."
    show rene hurt onlayer mc
    "But man, does my whole body hurt. Ouch."
    show rene neutral onlayer mc
    a "No one asked you go to that far, you self-sacrificing idiot!"
    show rene angry onlayer mc
    r "What did you say?!"
    show bastion angry
    ba "Alicia! We should praise Rene for thinking seriously about the mission, not calling her names!"
    r "You're just jealous that it was my idea that made this whole mission a success."
    a angry "What?! Are you out of your mind?!"
    m surprised "Bastion, you don't seriously believe this is okay...?"
    ba worried "No, what Magno did to her is not okay. But... it's all part of the job. We're heroes. This is the price we pay to keep everyone safe."
    show rene neutral onlayer mc
    a "I can't believe it!"
    m "What kind of friend are you?!"
    r "Folks, I really am fine..."
    a "Don't lie to us!"
    r "...well I will be tomorrow."
    ba angry "Hey, there are things expected of us. Certain things we have to uphold, for the good of everyone."
    ba "If we fall short, who knows how many innocent people will get hurt?"
    ba "As leader, I have to make sure we meet these expectations. Because of Rene, we provided."
    ba "Because of the sacrifices we make, people are safe. This discussion is over."
    show rene happy onlayer mc
    r "As long as we win, it doesn't matter if I get a bit hurt. It's my own decision to act this way. Please respect it."
    m annoyed "Oh God, why..."
    a annoyed "This is unbelievable..."
    ba neutralsmile "Thank you, Rene."
    r "No problem at all!"

    if villain == 0:
        jump end_scene2
    else:
        a sad "There's one more thing we have to talk about..."
        show bastion surprised
        show mia surprised
        show rene neutral onlayer mc
        a "Why did you kill today, Rene?"
        ba "What?! Kill?!"
menu:
    "Admit it":
        $ bastion -= 5
        jump admit
    "Lie that you didn't":
        jump lie

label admit:
    show rene neutral onlayer mc
    r "It's true. I killed."
    ba "But... why...?"

menu:
    "Explain the reason":
        jump explain
    "You don't have to explain yourself to them":
        if spare1kill2 == True:
            $ bastion -= 10
        else:
            $ bastion -= 5
        jump dont_explain

label explain:
    r "Because we have to fight the same guards over and over again. I wanted to hurt Dawn more than usual."
    "And I enjoyed it. But I won't admit that. They would never understand."
    show bastion angry
    if spare1kill2 == True:
        ba "How could you...? Even after everything I said... Rene! Why?!"
    else:
        ba "That's beyond stupid! Those are human lives you are playing with, Rene!"
    show rene angry onlayer mc
    r "I don't expect you to understand!"
    r "I'm leaving."
    jump end_scene2
label dont_explain:
    show rene angry onlayer mc
    r "I don't have to explain myself to you! My reasons are my own!"
    show bastion angry
    if spare1kill2 == True:
        ba "What?! Rene, after everything I said?! How could you! I thought you were... I thought..."
        r "...you wouldn't understand anyway."
        show bastion neutralfrown
        ba "...you're right. I don't plan on making it a habit to understand and sympathize with murderers."
        ba angry "I hope you feel proud of yourself, Rene. You just betrayed everything we stood for."
    else:
        ba "What?! We're a team! You could at least try to act like you are a part of it!"
        r "You wouldn't understand anyway!"
        ba "You are right. You don't have to explain yourself because no matter the reason... You're a murder now!"
    r "I'm leaving."
    jump end_scene2

label lie:
    show rene angry onlayer mc
    r "She's lying! I would never do something like that!"
    a surprised "But... you did it in front of me. Why are you lying?"
    show bastion neutralfrown
    ba "That's quite an accusation, Alicia. I don't believe Rene would kill anyone..."
    a angry "But she did! She snapped a guard's neck in front of me with her own hands!"
    if villain > 5:
        a "And then did it again!"
    r "I did not!"
    ba "I... don't know what to say..."
    r "I'm leaving."
    jump end_scene2

label end_scene2:
    show rene hurt onlayer mc
    "I get up and wince. I think I need to take a cab home. I can't walk in this state."
    show rene neutral onlayer mc
    "I'd never admit to how much it hurts. But it feels like I got run over by a truck."
    "I can't go to the hospital as a super. Our powers are a secret from the rest of society. I can't risk being found out."
    "I guess I should just sleep it off."
    jump scene3

label scene3:
    scene bedroom
    show rene neutral at side onlayer mc
    with Fade(0.25, 1.0, 0.25)
    "As soon as I get home I sneak past my parents and collapse on my bed without even changing clothes and fall asleep."
    show rene hurt onlayer mc
    "I will regret this tomorrow."
    "My dreams are restless. I keep replaying what happened at the warehouse. Magno's eyes staring, that intent to kill, it haunts me."
    show rene sad onlayer mc
    "I noticed how unstable he is but I never thought he would go so far. I have to be careful around him from now on."

    if villain != 0:
        jump villain_dream
    else:
        jump scene3_2

label villain_dream:
    scene warehouse outside
    hide rene onlayer mc
    show bolt neutral at side onlayer mc
    with Fade(0.75, 0.5, 0.25)
    "In my dreams I kill the guard again and again. And I feel..."
menu:
    "Guilty":
        $ villain = 0
        show bolt sad onlayer mc
        "I regret what I did today. What has gotten into me? Not only did I kill, I also got into a fight with my friends. This is not me."
        "I'm not this person... or am I?"
        scene bedroom
        show rene neutral at side onlayer mc
        hide bolt onlayer mc
        with fade
        jump scene3_2
    "Empowered":
        $ villain += 5
        show bolt happy onlayer mc
        "I feel elated. The strong will rule over the weak. I've proved today that I'm the strong one."
        show bolt neutral onlayer mc
        "And... I want to do it again. I'm finally being true to myself."
        jump scene3_2

label scene3_2:
    if bastion >= 10:
        jump scene3_2a
    else:
        jump scene3_2b

label scene3_2a:
    scene warehouse outside
    hide rene onlayer mc
    show bolt neutral at side onlayer mc
    show magno happy at center
    show stoneman angry at offscreenright
    with Fade(0.75, 0.5, 0.25)
    "In my dreams, I'm facing down Magno again at the warehouse. His chains lash out at me, and as I brace myself, suddenly..."
    show bolt surprised onlayer mc
    show stoneman angry at rightish
    show magno at leftish
    with ease
    "Bastion!"
    hide magno with dissolve
    show stoneman at center with ease
    play sound "hit.mp3" volume 0.6
    b "Stoneman!" with hit
    "He crumbles to the ground, but I manage to catch him."
    show stoneman neutralsmile
    st "Bolt... are you okay?"

menu:
    "Why did you do that?!":
        show bolt angry onlayer mc
        b "Why did you do that?! I... I could've teleported..."
        st "You're safe, aren't you...? If you'd have gotten hurt, I..."
        b "We're supers, Stoneman! I would've... I would've been able to take it! Why did you feel the need to do that?!"
        st "As long as I can use my body to keep others safe..."
        show bolt neutral onlayer mc
        "Wait, all that self-sacrificing talk earlier..."
        show bolt angry onlayer mc
        "Does he think this is good?! Me watching him take a beating for me like this?!"
        jump scene3_2a_end
    "Yes... thanks to you.":
        show bolt surprised onlayer mc
        b "Bastion I... yes. I'm fine, thanks to you..."
        st "That's good... I'm glad that you're safe..."
        b "But... but you didn't have to! I..."
        st "I had to. For the mission..."
        "For the mission..."
        show bolt sad onlayer mc
        "He took that for me... because he thinks it's a good thing?"
        jump scene3_2a_end
label scene3_2a_end:
    show stoneman neutralfrown
    st "Sorry Rene, I have to... rest my eyes..."
    hide stoneman with Dissolve(1.0)
    "He begins to fade in my arms. I clutch him close."
    show bolt surprised onlayer mc
    b "Wait! Bastion, I'll get you to safety!"
    hide stoneman with dissolve
    show bolt sad onlayer mc
    "No no no no no... not like this! This is reminding me too much of Mar--"
    jump scene3_2b

label scene3_2b:
    scene bedroom
    show rene neutral at side onlayer mc
    hide bolt onlayer mc
    with fade
    play sound "<to 0.6>glass-knocking.mp3"
    "Suddenly I wake up. It sounded like something collided with the window. What's going on? This is the upper floor."
    "It is painful to move around but I get up and approach the window. I pull the curtain away and..."
    show rene surprised onlayer mc
    show shadow neutral at center with dissolve
    "Shadow!"
    "I see him on the other side of the glass door on my balcony. Did he climb the tree next to the house?"
    "But more importantly what is he doing here? We're enemies! If someone sees us together!"
menu:
    "Open the window":
        $ samuel += 5
        show rene neutral onlayer mc
        "I stop hesitating and open the door."
        jump scene3_3
    "Hesitate":
        show rene neutral onlayer mc
        "No, he's my enemy. I shouldn't be letting him into my home."
        show rene surprised onlayer mc
        "Before I reach out to close the curtain, Shadow pulls the window open. Damn, I really should remember to lock this thing."
        jump scene3_3

label scene3_3:
    show rene surprised onlayer mc
    b "What are you doing here?!"
    show shadow smirk
    sh "Nice to see you too."
    show rene neutral onlayer mc
    "He looks past me at my room. I stop blocking his way and move to the side. We may as well sit down and talk like civilized people."
    "Or at least I sit down because standing is making me tired..."
    b "So... why are you here? How do you know where I live?"
    show shadow worried
    sh "I came to check up on you."
    show rene happy onlayer mc
    b "What?! Were you worried about me or something?"
    sh "Yes..."
    show rene surprised onlayer mc
    b "Why?! We're enemies. You shouldn't be here or... care about my wellbeing..."
    sh "I will be the one to decide whom I care about."
    sh "And regardless of who you are to me, you are part of my life and I don't enjoy seeing the people around me get hurt."
    b "Wow... that's... very nice of you..."
    show rene neutral onlayer mc
    "That's impossible. There has to be something more to this."
    "Sure, I enjoy our bickering and we are rarely the ones to fight against each other."
    "Of the whole Dawn team I could say Shadow is the one that is the nicest, but... he's still a villain."
    show shadow sad
    sh "You don't believe me."
menu:
    "Admit it":
        $ samuel += 5
        jump admit_ch1
    "Lie to him":
        jump lie_ch1

label admit_ch1:
    b "No, I don't. You and I are not friends and never can be."
    if murder:
        jump admit_ch1a
    else:
        show shadow neutral
        sh "I supposed it's easier for you to see everything as black and white."
        sh "Then you can fight against us with no worry that you are doing something wrong."
        show rene angry onlayer mc
        b "Of course I'm doing nothing wrong by fighting you!"
        sh "Feel free to keep telling yourself that."
        jump scene3_4

label admit_ch1a:
    show shadow smirk
    sh "Oh really now? I heard what you did today."
    show rene neutral onlayer mc
    b "Which part do you mean...?"
    sh "The killing part. I never thought you had it in you. It goes against everything Dusk believes in."
    "Well until today, I didn't think I had it in me either. But I won't admit that."
menu:
    "Say you'll never do it again.":
        show rene sad onlayer mc
        b "I regret it... I deeply regret it. You won't see me ever doing it again."
        show shadow neutral
        sh "Hmm... I see."
        jump scene3_4
    "Admit that you liked it and will do it again":
        $ villain += 5
        show rene happy onlayer mc
        b "Yes, I liked it and I would do it again."
        show shadow smirk
        sh "Well, it does give you a boost. Just don't get too addicted to the feeling."
        sh "Only kill when you have something to gain from it, not for pleasure. Else you will lose yourself entirely...like someone else I know."
        sh "I would hate for that to happen to you."
        show rene neutral onlayer mc
        "Whom is he referring to?"
        show shadow neutral
        sh "But if you're thinking of switching sides - don't do it."
        show rene surprised onlayer mc
        b "What? Why?"
        sh "Because it's not any better on the Dawn side either."
        sh "Yes, we are more lenient on the killing part, but there are so many rules holding one back from reaching one's true potential."
        b "I see. Do you want to leave?"
        show shadow smirk
        sh "And go where? For now I need the organisation and it needs me. We have a strained relationship but it's not bad enough to leave."
        jump scene3_4

label lie_ch1:
    show rene neutral onlayer mc
    b "No, I believe you."
    show shadow neutral
    sh "You're lying."
    show rene surprised onlayer mc
    b "I'm..."
    sh "I wish you would at least feel comfortable enough with me to say the truth."
    b "That's... I'm sorry..."
    sh "Don't worry about it."
    jump scene3_4

label scene3_4:
    show shadow neutral
    sh "It doesn't change the fact that I care about your wellbeing."
    show rene surprised onlayer mc
    b "I... I'm not sure what to say..."
    sh "Just promise me you won't risk your life like that ever again."
    b "What?! Who are you to tell me what to do?!"
    show shadow surprised
    sh "No need to react so..."
    show rene angry onlayer mc
    b "Now I know why you are here! Dawn doesn't want to lose against Dusk so they delegated you to mess with my head!"
    b "But you know what? My resolve is not so easily swayed! I don't mind getting hurt if we win against you villains!"
    show shadow sad
    sh "Rene... that's not a good way of thinking..."
    if villain >= 15:
        show rene angry onlayer mc
        b "Maybe our fights are just a game to you, but I want to win against you! For my own sake if not anyone else's!"
        show shadow smirk
        sh "So competitive... ha..."
        jump scene3_4a
    else:
        show rene angry onlayer mc
        b "Maybe our fights are just a game to you, but I'm serious about saving the world from you guys!"
        show shadow smirk
        sh "Saving the world... ha..."
        jump scene3_4a

label scene3_4a:
    show rene angry onlayer mc
    b "Laugh all you want! Now get out!"
    show shadow sad
    sh "If that's what you wish."
    hide shadow with dissolve
    "He leaves through the window. I fall back on the bed and start to cry."
    show rene sad onlayer mc
    "Why did I get so angry? What if he and my friends are right? What if I'm wrong?"
    "But Bastion stood by the decision..."
    "I'm so confused."
    "Eventually I cry myself to sleep."
    jump scene4

label scene4:
    scene college classroom day
    hide rene onlayer mc
    show rene neutral onlayer mc
    with Fade(0.25, 0.5, 0.25)
    "The next day my body is in a much better state, though I've got colorful bruises all over."
    show rene hurt onlayer mc
    "Stubborn as I am, I decide not to acknowledge the soreness and go to class..."
    "Now it's midday and I regret that decision wholeheartedly."
    r "Ouch..."
    "It hurts to sit on a bruised butt after all."
    show bastion worried at center with dissolve
    ba "Are you ok? Maybe you should go home?"
    show rene happy onlayer mc
    r "I'm fine, it's not so bad."
    ba "Hm... alright. Just make sure to look after yourself, okay?"
    show rene neutral onlayer mc
    show bastion neutralsmile
    "Bastion and I are both economics students. We both keep good grades because we picked our field of studies well."
    "It's something we both enjoy, though I do look forward to graduating and to start working."
    "But with Dusk as well as studies, my double life hasn't left me much time for a normal part-time job."
    "The lecture starts, but I can't focus to save my life. My thoughts stray to Shadow's weird visit yesterday."
    show rene sad onlayer mc
    "I wonder if I was too hard on him."
    "He came to me worried after all… and what if it was genuine? I accused him of trying to manipulate me without proof."
    "Yes, I'm a person who often acts impulsively and without thinking. But I'm also capable of self-reflection..."
    "I guess I should do that later."
    "Maybe I should apologise the next time I see him?"
    "But... apologise to my enemy?"
    "Are we really enemies? He did save me after all."
    "And we rarely exchange any real punches, we often just engage each other and try to see who can catch whom."
    "I hate to call it a game when what we are doing is serious... but it is something I enjoy."
    "And what he said about promising not to act reckless..."
    "I'm not sure how I feel about my decision to grab the package despite everything yesterday."
    "Bastion backed me, but the others pointed out that it wasn't a good thing to do."
    "What if I am wrong in believing that it was worth getting hurt over the box..."
    "I don't even know what's in this package and I receive no bonus for performance on those missions."
    "Yes, I get a salary for being a superhero, it is a job after all. It's a good thing to do but it's still work."
    show rene surprised onlayer mc
    "A note lands in front of me."
    show bastion happy
    "I look to my right at Bastion and he points to it with his pen."
    "\"Try to be less obvious about not paying attention to the class\" it says."
    show rene neutral onlayer mc
    "Crap. I was indeed quite deep in thought."
    "Back to class it is then. Better focus before the teacher catches me. I don't need more trouble in my life."
    jump scene5

label scene5:
    scene black with Fade(0.5, 0.0, 0.25)
    "I spend the rest of the day reflecting about what happened yesterday."
    scene park day memory with fade
    "At one point I rememeber a memory from my childhood."
    "I was 8 years old then and I was playing in the park with my 6 year old brother, Marcus."
    hide rene onlayer mc with dissolve
    "Marcus" "Rene, Rene! Catch me if you can!"
    r "Of course I can! Just watch me!"
    "I run up to Marcus as quickly as I can. But he is too far ahead of me."
    "He sends me a big smile and starts climbing a tree. When I reach him, he is already high up."
    "I don't climb after him. I've got a terrible fear of heights and just looking at him sitting on that branch makes me nauseous."
    "Why is he doing this if he knows that I don't like it? Probably to annoy me."
    r "Marcus! Come down!"
    "Marcus" "No, you come up! Or are you too scared?"
    "Normally Marcus is able to bait me into doing anything he wants. Any challenge, I will accept."
    "I'm overly competitive, I know. But not this. I'd rather die than climb that tree."
    "Marcus" "I knew it! Scaredy cat!"
    r "Hmpf! This is not fun. I'm leaving."
    "I stomp away from the tree."
    "Suddenly I hear a scream and when I turn around I see Marcus falling."
    "This is when I phase for the first time. One moment I'm here, the other under Marcus."
    "It's dizzying. I want to throw up. And the pain... ouch..." with hit
    r "Marcus, are you alright?!"
    "Marcus" "Yes... yes... what about you, sis?"
    "He landed on me, so I cushioned his fall."
    "But as he rolls off me to the side I notice that I can't quite move my right arm. The arm he landed on."
    "I start crying and so does Marcus."
    "Soon our parents find us. My arm is broken and I'm taken to the hospital."
    "My super powers are still weak so it takes me a few months to recover."
    "Since then, I've always thought that it doesn't matter if I get hurt, What matters is that everyone lives and we succeed."
    if villain != 0:
        "Well... almost everyone."
    if bastion >= 10:
        "That's how it should be... right, Bastion?"
    "I applied this logic to everything in life. Everything is a challenge to me."
    "This has its upsides, but it can be... self destructive too."
    "And yesterday I was so self-destructive that even Shadow, an enemy, noticed and he decided it was worth talking about."
    "Did I go too far?"
    jump ch2_s1
