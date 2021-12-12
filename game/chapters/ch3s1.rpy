label ch3_s1_1:
    scene warehouse night with Fade(0.75, 0.5, 0.5)
    show stoneman neutral at left
    show bolt neutral at right
    "Another night, another warehouse, another \"fetch\ quest\". This is getting so boring and repetitive."
    "What kind of heroes are we? Are we saving anyone?"
    "No, all we do is steal stuff from Dawn and fight them."
    if bastion >= 15:
        "Bastion should know this too, right?"
    f "Let's split up or we won't ever find the datastick!"
    st "Agreed. Such a small thing in such a big place. We'll never find it unless we comb through the whole building."
    "I'm a bit uneasy about this. This warehouse doesn't have an open layout like the others."
    "And it's much larger. We won't be in sight of each other and possibly not in hearing distance either."

menu:
    "Voice your concerns":
        b "I'm not sure it's a good idea to split up in this place..."
        f "Don't chicken out on us, Bolt."
        if bastion < 15:
            b "I'm not--"
            st "We have a mission to do. Let's get on it."
            show bolt surprised
            b "..."
            "They completely ignored me. Wow."
            jump ch3_s1_2
        else:
            b "I'm not."
            st "Bolt's right to be concerned. We just need to make sure we're careful going forward."
            "Careful? What happened to all that talk about putting your body on the line?"
            st "Everything is going to be okay. We just have to be quick about it."
            jump ch3_s1_2
    "Remain silent":
        "I don't say anything. They'll just think I'm scared. Hopefully nothing bad will happen."
        st "We have a mission to do. Let's get on it."
        jump ch3_s1_2

label ch3_s1_2:
    hide stoneman with dissolve
    show bolt at center with ease
    "As our leader commands, we split up and go into different areas of the warehouse."
    "I look carefully through all the boxes trying to find what we seek."
    "Why did we come here without knowing the exact location of this item?"
    "I keep getting this weird feeling that something is terribly wrong."
    ma "Hello, gorgeous!"
    "I flinch when I hear Magno’s voice behind me. I turn around."
    "He stands there, chains suspended in the air, flashing his teeth at me."
    "The wide smile doesn’t reach his eyes. I flinch. It’s so creepy."
    show bolt at right with ease
    show shadow at left with dissolve
    "I take my eyes off him and look to the right. Shadow is standing behind Magno."
    "He nods when he sees me, but then looks behind me and frowns when he realises I'm alone."
    b "What do you want, Magno?"
    ma "Oh, what's with the cold greeting! Aren't you happy to see me?"
    show bolt angry
    b "Why would I be?!"
    ma "Well, I'm always happy to see you."
    "A chain wraps around my waist from behind." with woosh
    "Wait! Where did that come from? Since when can he control two sets of chains?!"
    ma "And to catch the little birdie!"
    "The chain tightens around me as I try to wiggle out of it."
    ma "Ah-ah, not so fast!"
    sh "...you caught her. Let's tie her up and move on to the next one."
    ma "What? Where's the fun in that!"
    if murder:
        ma "The little bitch murdered our men!"
        sh "As we killed Dusk guards many times."
    ma "She thinks she's a hero. Well guess what, Bolt? It's time to stop playing around."
    "His other chain moves in and wraps around my throat. The metal moves like snakes and encloses around my whole body."
    "Then he tightens them."
    "It hurts. I would scream but I can't breathe."

    if bastion > 15:
        jump ch3_s1_bastion
    elif samuel > 15:
        jump ch3_s1_shadow
    else:
        # BAD END 1: ALONE AND FORGOTTEN
        show shadow sad
        show bolt sad
        "All I wanted was to be a hero. To save the world from Dawn."
        "But here I die in the warehouse alone and forgotten. My friends don't reach me in time and Samuel just stares sadly."
        "The world darkens as I suffocate."
        scene black with Fade(1.0, 0.0, 0.0)
        "BAD END 1: ALONE AND FORGOTTEN"
        return

label ch3_s1_bastion:
    show stoneman angry at offscreenright
    "Magno approaches me, a look of elation on his face. He's really enjoying it."
    "His chains tighten around me even more and he suspends me in the air."
    play sound "slap.mp3" volume 0.8
    "Then he slaps me hard across the face." with hit
    show stoneman angry at center with ease
    show bolt surprised
    st "Get off of her, damn it!"
    "The next thing I see is Stoneman leaping through the air towards Magno. Before Magno can react, Bastion leans his head back..."
    play sound "hit.mp3" volume 0.6
    "... and gives Magno the most devastating headbutt I've ever seen. The impact was sickening." with hit
    "The chains drop from me as Magno reels from the headbutt, and I fall to the floor."
    show bolt neutral
    "I'm trying desperately to catch my breath. I'm crying and wheezing. Not the image of a hero, but who cares."
    "I almost died...for real!"
    st "Gah!"
    "I raise my head to see Stoneman drop to the floor. Magno was approaching him."
    ma "Impressive use of your head, you son of a bitch... now how about I rip it off?"
    show bolt surprised
    "He's going to kill Stoneman...!"

menu:
    "Help him":
        jump ch3_s1_bastion2
    "Run away":
        # BAD END 4: COWARD'S DEATH
        "I... I have to get the others!"
        play sound "<from 1.0>gunshots.mp3" volume 0.6
        show bolt neutral
        show stoneman surprised
        show shadow sad
        "I don't make it very far though, before I hear the sound of a gunshot." with hit
        "At the same time I feel excruciating pain in my chest. I look down to see... blood."
        "I cough up red and fall to the floor."
        "The last thing I see is Snapshots smiling face. She was my killer."
        "And the last thing I hear is Bastion calling out for my name."
        show stoneman sad
        st "R... Ren--"
        play sound "gunshot.mp3"
        scene black with Fade(0.5, 0.0, 0.5)
        "BAD END 4: COWARD'S DEATH"
        return

label ch3_s1_bastion2:
    show bolt angry
    "I am thrown into a fury I've never felt before. I unleash a twister of uncoordinated punches and kicks on Magno." with hit
    "I {i}have{/i} to defeat him, or else Bastion and I will die."
    ma "You traitor! You bitch!"
    "Magno throws me off him and kicks Bastion in the stomach."
    ma "Ow-- you fucker!" with woosh
    "Magno winces-- Bastion hardened himself to soften the blow."
    play sound "<to 1.0>punch.mp3" volume 0.6
    "Bastion immediately takes advantage of the situation, and throws a hard right hook at Magno."with woosh
    "It connects cleanly, sending Magno reeling back."
    st "That'll shut you up!"
    play sound "<from 1.0>gunshots.mp3" volume 0.6
    "A spray of bullets hit Stoneman! Thankfully, his skin was already stonelike... if he was normal, that would've killed him!"
    st "Tch... Snapshot."
    show shadow sad
    "I look up to see Snapshot smiling wickedly, guns pointed at us. And I see Samuel nearby, watching as the action goes on..."
    sn "Hey, girlie... whispers told me that you started to care for a certain someone..."
    b "What are yo--"
    show bolt surprised
    "My eyes widen as I see her pointing one of her guns at Samuel. Her own teammate."
    st "Nngh...! No!"
    "Bastion...!"
    "Even though Shadow was the enemy, I watched Stoneman bull charge towards Snapshot."
    "Snapshot smiles smugly at this. Her bait was taken."
    "She aims her guns forward and unloads on Stoneman, her bullets chipping away at his stone skin."
    play sound "<from 1.0>gunshots.mp3" volume 0.6
    b "S-Stoneman!"
    show stoneman neutral
    st "W-Worry about getting your friend to safety!"
    hide stoneman with dissolve
    show bolt sad at rightish
    show shadow sad at leftish
    with ease
    "Running out of options, I come up to Shadow and grab him by the shoulders."
    b "Samuel, do you trust me?"
    show shadow neutral
    sh "Yes, I do."
    "There is only one thing I can think of and it's risky."
    "I can take the longest leap I've ever done with my powers. Straight outside the warehouse. And then we'll make a run for it."

menu:
    "Make a leap of faith":
        jump ch3_s1_bastion3
    "It's too risk. What if we disintegrate?":
        # BAD END 5: SHOT DOWN
        "No, I can't. It's too risky. What if we disintegrate at the molecular level. I've never leapt that far."
        b "No, I can't do it. Get up. Let's try to take them down."
        sh "Alrigh--"
        play sound "gunshot.mp3"
        show bolt surprised
        show shadow surprised
        "Samuel crumples to the ground. A large hole pierced through the middle of his chest."
        b "Samuel!"
        show stoneman at offscreenright
        "I look to see Snapshot, one gun pointed at me, smirking at me. Because I screamed, Bastion whips his head over to me in concern."
        show stoneman surprised at right with ease
        st "R...Rene! What happ--"
        play sound "gunshot.mp3"
        "Bastion is silenced. The stone on his body gave way under all the bullets, leaving his skin underneath."
        "I was the final distraction needed for Snapshot to end him."
        show bolt sad
        "I fall to my knees."
        "Samuel and Bastion... because of my indecision..."
        sn "You should've left when you had the chance, girly."
        play sound "gunshot.mp3"
        "Then there's another gunshot. It was an act of mercy, really. Stopping me from thinking too hard about what I've done." with hit
        scene black with Fade(1.0, 0.0, 0.0)
        "I didn't even get to think if I deserved it."
        "BAD END 5: SHOT DOWN"
        return

label ch3_s1_bastion3:
    show bolt neutral
    "There is no other choice. I need to try to teleport. Not only further away but with two people."
    ma "Fight me, you bitch!"
    "I tune Magno out and focus on my powers."
    "I feel the vortex pulling at me, the world in between reality and dreams which I briefly enter."
    "Then I reappear... outside the warehouse."
    b "Samuel, are you alright?!"
    "I look down at Samuel, then pat down his body."
    show shadow happy
    sh "I'm fine. When did you get so touchy-feely?"
    show bolt angry
    b "Not now, you idiot! I need to check if anything's disintegrated!"
    sh "I assure you everything is in the right place.Or do you want me to undress to see for sure?"
    "I realise he's flirting with me."

menu:
    "Flirt back":
        $ samuel += 5
        show bolt happy
        b "Save that offer for later. We gotta get out of here."
        "My answer surprises him but he quickly regains his composure and smiles back."
        jump ch3_s1_bastion4
    "Get angry at him":
        b "Stop being inappropriate, you idiot!"
        show shadow neutral
        sh "Fine... fine... I just wanted to lighten the mood."
        "Maybe I shouldn't have snapped at him like that but it's really annoying. This is not the time or place for such conversations."
        jump ch3_s1_bastion4

label ch3_s1_bastion4:
    show bolt neutral
    show shadow neutral
    "I grab Samuel by the hand and we run. Behind us I hear the door open. Magno is persuing us."
    "But... I don't see Bastion. The gunshots seemed to have stopped too."
    "He... he gave me an order. And that order right now is to help Samuel."
    "I phase once more when we get to the park in hopes of losing them."
    jump ch3_s2

label ch3_s1_shadow:
    "Magno approaches me, a look of elation on his face. He's really enjoying it."
    "His chains tighten around me even more and he suspends me in the air."
    play sound "slap.mp3" volume 0.8
    "Then he slaps me hard across the face." with hit
    show shadow angry
    sh "Leave her alone, Magno!"
    "Shadow throws himself at Magno and starts beating him up with his fists."
    "The chains drop from me, Magno's concentration broken. I fall to the floor."
    "I'm trying desperately to catch my breath. I'm crying and making strange wheezing sounds. Not the image of a hero but who cares."
    "What the fuck! I almost died here! For real!"
    sh "Ouch!"
    show bolt surprised
    "I raise my head to see Shadow drop to the floor."

menu:
    "Help him":
        # sfx: gunshot
        jump ch3_s1_shadow2
    "Run away":
        # BAD END 2: SHOT TO DEATH
        play sound "gunshot.mp3"
        "I don't make it very far though, before I hear the sound of a gunshot. At the same time I feel an excruciating pain in my chest." with hit
        "I look down to see... a wound in my chest. There is so much blood."
        "I cough up red and fall to the floor."
        "The last thing I see is Snapshot's smiling face. She was my killer."
        scene black with Fade(1.0, 0.0, 0.0)
        "BAD END 2: SHOT TO DEATH"
        return

label ch3_s1_shadow2:
    show bolt angry
    "I don't know what I'm doing when I throw myself at Magno and beat him with my fists. My movements are so desperate and uncoordinated." with hit
    "I just {i}have{/i} to defeat him, or else Shadow and I will die."
    ma "You traitor! You bitch!"
    "Magno throws me off him and kicks Shadow in the stomach." with woosh
    "Running out of options, I come up to Shadow and grab him by the shoulders."
    show bolt sad at rightish
    show shadow at leftish
    with ease
    b "Samuel, do you trust me?"
    show shadow neutral
    sh "Yes, I do."
    "There is only one thing I can think of and it's risky. I could take the longest leap I ever did with my powers."
    "Straight outside the warehouse. And then we'll take a run for it."

menu:
    "Take a leap of faith":
        jump ch3_s1_shadow3
    "It's too risky. What if we disintegrate?":
        # BAD END 3: DYING TOGETHER
        "No, I can't. It's too risky. What if we disintegrate at the molecular level? I've never leapt that far."
        show bolt sad
        b "No, I can't do it. Get up. Let's try to take him down."
        sh "Alright."
        show bolt neutral
        "We take another attempt at fighting Magno. But just as we think we almost have him-"
        play sound "gunshot.mp3"
        "I hear a gunshot and feel excruciating pain. I look down to see a wound in my chest. There is so much blood." with hit
        show shadow surprised
        sh "Rene!"
        "Magno and Shapshot laugh."
        play sound "gunshot.mp3"
        "Then there's another gunshot. Samuel's dead eyes are the last thing I see before I slip into darkness."
        scene black with Fade(1.0, 0.0, 0.0)
        "BAD END 3: DYING TOGETHER"
        return

label ch3_s1_shadow3:
    "There is no other choice. I need to try to teleport. Not only further away but with two people."
    ma "Fight me, you bitch!"
    "I tune Magno out and focus on my powers."
    "I feel the vortex pulling at me, the world in between reality and dreams which I briefly enter."
    "Then I reappear... outside the warehouse."
    show bolt neutral
    b "Samuel, are you alright?!"
    "I look down at Samuel then pat down his body."
    show shadow happy
    sh "I'm fine. When did you get so touchy-feely?"
    show bolt angry
    b "Not now, you idiot! I need to check if anything's disintegrated!"
    sh "I assure you everything is in the right place. Or do you want me to undress to see for sure?"
    "I realise he is flirting with me."

menu:
    "Flirt back":
        $ samuel += 5
        show bolt happy
        b "Save that offer for later. We gotta get out of here."
        show shadow surprised
        "My answer surprises him but he quickly regains his composure and smiles back."
        show shadow neutral
        "I grab Samuel by the hand and we run. Behind us I hear the door open. They are persuing us."
        "I phase once more when we get to the park in hopes of losing them."
        jump ch3_s2
    "Get angry at him":
        b "Stop being inappropriate, you idiot!"
        show shadow neutral
        sh "Fine... fine... I just wanted to lighten the mood."
        "Maybe I shouldn't have snapped at him like that but it's really annoying. This is no time and place for such conversations."
        "I grab Samuel by the hand and we run. Behind us I hear the door open. They are persuing us."
        "I phase once more when we get to the park in hopes of losing them."
        jump ch3_s2
