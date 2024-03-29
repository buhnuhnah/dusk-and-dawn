label ch4_s1_1:
    scene warehouse outside
    hide rene onlayer mc
    show frostbite neutral at farleft
    show stoneman neutralfrown at leftish
    show bolt neutral at side onlayer mc
    show shadow neutral at farright
    show mia neutral at rightish
    with Fade(0.75, 0.5, 0.5)

    "A couple of us are uneasy as we head into the warehouse. No one speaks to each other, but we keep close."
    if bastion >= samuel:
        "I keep close to Bastion."
        "I catch a glimpse of his face - his attention is constantly focusing on every nook and cranny of this place."
        "His eyes are hard and I could tell his resolve is harder. He's putting on a brave face for all of us."
        "I wonder... if maybe he's scared too?"
        "Gah, I shouldn't get distracted..."
    else:
        "I stay close to Samuel."
        "I catch a glimpse of his face - his brows are drawn downwards, his eyes flitting back and forth like an animal on the hunt."
        "He is prepared. Unlike me. Here I am, being distracted by his beautiful eyes..."

    sh "Hey, anyone here?"
    "Nothing."
    f "Huh, looks like we got here first... do you see anything, Mia?"
    m "Uh-uh. I guess they're just running behin-- eep!"
    show shadow surprised
    show stoneman surprised
    show mia surprised
    show bolt surprised onlayer mc
    "We all turn to Mia-- but then our eyes stopped on Alicia."
    show frostbite surprised
    f "What's... going on?"
    sh "... stay still. Stay very still."
    "There was a red dot on Alicia's forehead. I've never seen Alicia go so quiet so fast."
    ma "Well well well, thought you could get the drop on us, hm?"
    hide frostbite
    hide stoneman
    hide mia
    hide shadow
    show magno happy at left
    show snapshot happy at right
    with dissolve
    "We turn to see Magno and Snapshot walk out of the shadows, side by side."
    "The pair of them looked so full of themselves-- as if they've just made the catch of the century."
    "Snapshot was holding a rifle, aiming it steadily at Alicia's head."
    b "P-Please don't shoot! We're just here to talk!"
    show snapshot neutral
    ma angry "Honestly! How FOOLISH do you think we could possibly be?! After everything you've pulled on us, dear Shadow... for what?!"
    ma "That {i}BITCH?!{/i}"
    show snapshot annoyed
    "Bastion takes a step forward, but is stopped at the sight of Snapshot cocking her rifle."
    show magno neutral
    sn happy "Ah ah ah, Rocky. One wrong move, and I put Frosty over here on ice..."
    ma "I don't see why you need to hesitate. Go ahead, Snapshot."
    sn annoyed "... don't tell me what to do."
    b "Wait wait wait! Just wait! Please hear us out! We're not your enemies!"
    sn neutral "Yeah? Well, you're as comfy as I'm allowing you to get. Go ahead, I'm lis--"
    ma angry "Bah! Snapshot, didn't I order you to fire?!"
    sn annoyed "And didn't I tell you to shove it up your ass? Come on, might as well hear them out."
    show bolt neutral onlayer mc
    b "Th-there's a group called Daylight! They've been responsible for all of our fighting."
    b "They keep setting us up to fight each other, and benefiting from it."
    b "The more we fight each other, the more the crystals in our uniform charge up! They're planning to use that energy to take over the world."
    show snapshot surprised
    "There's a look of thought on Snapshot's face. I watch as her finger slides off of the trigger."
    sn "Huh... and can I ask, where you got this information fro--"
    "Magno starts to levitate chains into the air."
    ma "Enough of your mindless PRATTER!"
    sn annoyed "Hey, we're talking here!"
    hide magno
    hide snapshot
    show frostbite surprised at center
    with dissolve
    "I see him swing wide with one of the chains, and I immediately move to teleport Alicia out of the way." with sshake
    f "Ahhhh! Damn it, I knew this was a bad idea!"
    hide frostbite
    show magno angry at left
    show stoneman angry at rightish
    show shadow angry at farright
    with dissolve
    "I look back to see Samuel and Bastion fighting Magno."
    "Snapshot, on the other hand, has her weapon pointed downward. She seems more annoyed than anything."
    "Everything's gone to hell in a handbasket real fast! Think Rene, thin-- huh?"
    show bolt surprised onlayer mc
    $renpy.sound.play("beep.mp3", loop=True, relative_volume=0.5)
    "In the midst of all the fighting, I hear something... is that a beeping sound? It's faint, and coming from one of the crates nearby..."

menu:
    "I need to go help the others!":
        # BAD END 6 : EXPLOSIVE FAREWELLS
        "I need to go help the others! If Magno kills anyone, then our plans to fight Daylight is going to end before it even begins!"
        show bolt angry onlayer mc
        "I rush into action, teleporting behind Magno and holding his arms behind his back."
        b "Stop!"
        ma "Gah! You... you BITCH!"
        play sound "<to 1.0>punch.mp3" volume 0.6
        queue sound "beep.mp3" loop volume 0.5
        "He's so much more powerful than I am. After he breaks free from my grip, he delivers a sharp backhand that knocks me down." with hit
        show shadow angry
        show stoneman angry
        "With his attention on me, Samuel and Bastion both rush up behind him, fists raised in the air."
        "The ensuing barrage is effective, he doesn't even see it coming. As they rain down blow after blow on him, I--"
        play sound "beep-raw.mp3" loop volume 0.1
        pause(1.0)
        play sound "explosion.mp3" volume 0.75
        scene black
        hide bolt onlayer mc
        with fade
        "..."
        "BAD END 6: EXPLOSIVE FAREWELLS"
        return
    "That's too suspicious not to check":
        jump ch4_s1_2

label ch4_s1_2:
    show bolt neutral onlayer mc
    "All the times we've infiltrated this place, I've never heard a sound like that..."
    hide magno
    hide shadow
    hide stoneman
    show frostbite surprised at left
    show mia surprised at right
    with dissolve
    m "Rene? What are you doing?"
    f annoyed "Bastion needs backup! Come on!"
    b "No, just... give me a second!"
    "I quickly follow the sound of the beeping and find myself in front of a box."
    "It's very similar to the ones we've been sent to find everytime we come here. 31 x 23 x 26 inches..."
    "I open it and look inside. Sitting in the box was some kind of contraption."
    "It scared me at first because it straight up looks like a bomb."
    "Naked wires attached here and there, and there was this... crystal inside of it? It was glowing--"
    show bolt surprised onlayer mc
    show frostbite surprised
    b "{i}Ahhh!{/i}" with woosh
    "It's a bomb. {w}{i}It's a bomb.{w} It's a bomb.{/i}"
    f "Wh-what is it?"
    b "Bomb! There's a bomb in here!"
    hide frostbite
    hide mia
    show magno surprised at left
    show stoneman surprised at rightish
    show shadow surprised at farright
    with dissolve
    ma "Huh?!"
    "Magno, Samuel, and Bastion stop fighting as the mere mention of the word \"bomb\" overpowers any hostility we had towards each other."
    b "I need to do something! I need to do something!"

menu:
    "Alicia and Mia are here! we can deal with it here!":
        jump ch4_s1_3
    "Screw it. Take it and teleport far away!":
        # BAD END 7 : HEROIC SACRIFICE
        jump bad_end_7

label bad_end_7:
    show bolt neutral onlayer mc
    "Screw it. Who knows how close it is to blowing up?! I can't let anyone else get hurt. I need to go far!"
    "I pick it up, and ready myself..."
    sh "Rene, wait!"
    st "Don't!"
    hide stoneman
    hide shadow
    show frostbite annoyed at left
    show mia surprised at right
    with dissolve
    f "What are you doing?! Come on, hand that thing over!"
    m "Rene!"
    show bolt sad onlayer mc
    b "I have to guys... to keep everyone safe! Take care of Daylight for me"
    "Before anyone could reach me, I'm gone."

    scene park night
    show bolt hurt onlayer mc
    with Fade(0.25, 0.5, 0.25)

    "Huh... back here again. This is really the farthest I can go, huh...?"
    "I'm too tired to move."
    "... but at least everyone's going to be alright. It's sobering, actually."
    "The last thing I was going to see before I get obliterated is the brilliant glow of this crysta--"
    show bolt surprised onlayer mc
    "My eyes widen as I see a pair of boys running over to me, running from their mother to me."
    "The mom looked concerned, and the boys seemed curious."
    b "N-No! Don't come any clo--"
    play sound "beep-raw.mp3" loop volume 0.1
    pause(1.0)
    play sound "explosion.mp3" volume 0.75
    scene black
    hide bolt onlayer mc
    with fade
    "..."
    "BAD END 7: HEROIC SACRIFICE"
    return

label ch4_s1_3:
    "Aha, got it! I literally have the two most perfect people in the world here to deal with this!"
    "At least, I think so. My mind's kinda hard to hear over the beating of my heart...!"
    hide magno
    hide stoneman
    hide shadow
    show frostbite surprised at left
    show mia surprised at right
    with dissolve
    b "Alicia! Mia! I need you two over here!"
    f "Wh-What?!"
    m "M-M-Me?!"
    show bolt neutral onlayer mc
    b "Yes yes yes, now please! Alicia, I need you to freeze the bomb to stop it from exploding!"
    f "O-Okay!"
    "She almost trips over herself as she dashes over."
    "As soon as she lays eyes on the bomb, she takes hold of it. Urgency fueling her every movement."
    "A thick ice encases the device, but the crystal still shines brilliantly through it."
    f neutral "Got it!"
    b "Mia!"
    m "I...I..."
    "Mia looked so afraid. She's always preferred working in the background."
    "I almost completely forgot she's not used to the immense amount of danger we put ourselves in."
    m sad "I...I can't...!"
    "I walk over to her, and take her shaky hands in my own."
    b "Mia, please listen to me... you're the only one here who knows {i}anything{/i} about {i}anything{/i} with tech."
    b "We need you now more than over."
    b "I know it's scary, I know the pressure is on but... you need to be brave."
    m sad "...brave."
    show mia angry with dissolve
    "At that moment, I feel it. Her hands become steady. She peers up at the bomb, and she doesn't flinch."
    m "I need to be brave!"
    "She beelines towards Alicia and immediately starts tending to the device. Alicia stands there, frozen, keeping as still as she can."
    "Everyone watches, holding their breath, letting the master do her work."
    "I watch the entire time, not understanding a {i}single damn thing{/i}."
    "I can't even put into words just how little I understand. And I know everyone feels the same way."
    play sound "pop.mp3"
    show mia surprised
    "After a short moment, the device creaks open and Mia extracts the crystal from it."
    show frostbite neutral
    show bolt happy onlayer mc
    "A massive sigh of relief hits the room."
    m "I... I got it!"
    b "Great job, Mia! You're a hero!"
    f "Ahhh... I can finally put this down now, right?"
    ma "What is that?"
    show bolt neutral onlayer mc
    show mia neutral
    with None
    show magno surprised at leftish
    show snapshot neutral at farleft
    hide frostbite
    with dissolve
    "All eyes shot to Magno, who was standing in between everyone."
    "He was staring at the bomb with such intensity I was afraid he'd actually be able to detonate it."
    "I've never seen him so... calm?"
    m "It's a device whose sole purpose is to detonate when the energy core reaches a sufficient amount of po-"
    sn annoyed "It's a bomb."
    m "{i}Yes{/i}, it's a bomb..."
    b "But more importantly, this is what I was trying to tell you about!"
    b "The crystal inside of that bomb is the exact same one we have in our uniforms! The one that gathers power when we fight."
    ma "That means...!"
    show shadow neutral at right
    show stoneman neutralfrown at farright
    hide mia
    with dissolve
    sh "Look who's finally getting it. Yeah, that means your little stunt almost cost everything within a two mile radius."
    ma angry "PREPOSTEROUS! Me?! Making a mortal folly?!"
    sn "Does all that magnetism attract stupidity? Look what almost happened because you couldn't shut your mouth."
    ma "Don't you DARE talk to me that w-"
    sn neutral "{i}Anyway{/i}, we were in the middle of talking."
    show snapshot at leftish
    show magno at farleft
    with ease
    sn "You, they call you Bolt, right?"
    b "Feel free to call me Rene."
    sn "Well, look who's getting all buddy buddy already. I was gonna ask: Where did you get this information from? All this stuff about Daylight?"
    b "From my aunt. She's a super who had a leadership position in Daylight."
    sn "Ah, well, that's convenient. Alright. I think that's enough for me."
    show stoneman surprised
    st "Enough?"
    sn "Yeah. What else are you here for? You came here to convince us to join you, right? Common enemy and all that?"
    sn neutral "Well, I'm in. Truth be told, I've been thinking about how weird our repeat encounters are."
    sn "Plus, I don't appreciate getting almost turned into a formerly alive person."
    sn happy "I like to be the one doing that to other people."
    sn neutral "So, I'm feeling pretty spiteful. I'm in."
    sn "And since we're getting intimate here, just go ahead and call me Levina."
    show bolt surprised onlayer mc
    "Wow. Straight to the point with her."
    "Our heads turn over to Magno, who seems deeply angry. But not at Levina."
    "His eyes were shut, arms crossed tightly over his chest."
    show bolt neutral onlayer mc
    show stoneman neutralfrown
    b "What about you?"
    "My heart jumps as his eyes shoot open. Eyes that were full of anger."
    ma "I... will not be made a fool by anyone."
    ma "Daylight will regret the day they ever choose to {i}cross me{/i}."
    b "Does... does that mean you're in?"
    show snapshot at farleft behind magno
    show magno at leftish
    with ease
    show shadow angry
    show stoneman angry
    "In response, Magno walks over to me. He doesn't get close as Bastion and Samuel move right in front of me."
    "It was so strange. I could still feel his murderous intent. But for the first time, it wasn't aimed at any of us."
    ma "If you are working to ensure the complete, utter annihilation of Daylight, of the group that almost slayed all of us here today..."
    ma "Then our goals align."
    show shadow neutral
    show stoneman neutralfrown
    "Complete, utter annihilation is a... {i}strong{/i} set of words. But no one looks like they want to argue right now."
    "Almost as if everyone knows that correcting him would just be exhausting."
    "Plus, it looks like we're somehow on his good side. Let's keep it that way."
    show snapshot happy
    l "Look at that, Sam. The team's back together again. Isn't that nice? I almost didn't want to shoot you in your sad little face."
    show shadow smirk
    sh "Ha. Can't say I missed your company, but I can definitely say I'm glad I don't have to dodge bullets in the foreseeable future."
    show snapshot neutral
    l "Maybe I'll make you dance here and there. After all, you left me with Rustbucket over there."
    show frostbite surprised at offscreenright
    ma "Silence, bitch."
    hide snapshot
    hide magno
    with dissolve
    show shadow at left
    show stoneman at center
    show frostbite at farright behind stoneman
    with ease
    f "Is... is this supposed to be banter? How did any of you get along?!"
    show bolt happy onlayer mc
    "If I was more comfortable, I would've made a joke about how Magno's powers made him \"attractive\"."
    "...But that's a casket I'm not willing to crawl into right now."
    show bolt neutral onlayer mc
    show shadow neutral
    show frostbite neutral
    st "Chances are, since they set all of this up for us, they must already know that we know about the situation and what our intentions are."
    st "... which means I'm sure they'll take measures to act against us."
    show shadow neutral
    sh "There's only one place right now that's away from the eyes and ears of Daylight."
    "Oh, Aunty. I'm sorry that I keep bringing weirdos home..."
    show bolt happy onlayer mc
    b "And I know where it is! Follow me!"
    jump ch4_s2_1

label ch4_s2_1:
    scene living room
    hide bolt
    show bolt neutral at side onlayer mc
    show aunt matilda neutral at farleft
    show stoneman neutralfrown at rightish
    show shadow neutral at  farright
    with Fade(0.75, 0.5, 0.5)

    "That night had to be one of the weirdest nights of my life."
    "The entire night I was completely surrounded by supers. And that includes my {i}aunt{/i}, of all people."
    "What is it they say? Extraordinary times call for... strange bedfellows? I {i}have{/i} to be remembering that wrong..."
    "It's been a very long night."
    "Anyway, as soon as we stepped into Aunty's place, the seven of us gathered in the living room and got right into the thick of it."
    "Aunty explained everything to the people not in the know."
    "I couldn't help but focus on, well, {i}everything{/i}."
    "My team has never been to Aunty's place before. Now here they are, all at once. So there's that."
    "Progressing up the chain, we have Levina, who was lugging around a huge arsenal. Pistols and rifles and submachine guns, {i}oh my!{/i}"
    "Aunty didn't seem to mind that there was a pile of bullets sitting on the coffee table, or a rifle sitting on the recliner where a person should be."
    "Oh, also, the bomb we disarmed? It was sitting on the living room table."
    "But hey, if she's not offended, who am I to say anything?"
    "And then at the very top, we have Aid-- {i}Magno{/i}."
    "On the way back, it's been established that he doesn't... like us using his name too much."
    "He also keeps calling all of us by our hero names, so obviously, we've been meshing together pretty well."
    "Anyways."
    "Aunty explained everything and took every question that came her way."
    "By the end of that, there was little confusion on who the enemy was, and who we should be trusting."
    s "Alright. Now that all that is out the way, I guess the next question is..."
    s "Where do we even begin?"
    hide shadow
    hide stoneman
    show snapshot neutral at rightish
    show magno neutral at farright
    with dissolve
    ma "We should first inquire about the headquarters of these particular people... if the woman even knows."
    show aunt matilda happy
    am "Ha! A pleasant one, isn't he?"
    l "Don't mind him. So, got any idea where these people are?"
    show aunt matilda neutral
    am "Of course I do. With all that technology they haul everywhere, they're not exactly pick up and go."
    ma angry "Then tel--"
    hide magno
    hide snapshot
    show mia neutral at rightish
    show stoneman neutralfrown at farright
    with dissolve
    m "Miss Matilda. If that's the case, can you share that information with us?"
    am "... yes yes, in due time."
    ba "If I may ask, why the hesitation, miss?"
    am "I'm just in thought is all, dear. Hm... I really put you all on a dangerous path, haven't I?"
    r "And you'll feel responsible if we get hurt?"
    show aunt matilda happy
    am "Look at you, all sharp!"
    show aunt matilda neutral
    r "I know you're worried, Aunty, but... you know about the dangers of this life better than anyone."
    r "And in whatever case, we {i}have{/i} to do thi--"
    am "Yes, yes, dear... I know. I know."
    "She indulges in a bit of tea before taking a deep breath."
    am "Their headquarters are located... below Dawn's warehouse."
    show bolt surprised onlayer mc
    show stoneman surprised
    show mia surprised
    r "What?!"
    "There wasn't a single person who wasn't confused in that room."
    ba "But... there was a bomb there that was set to explode! Wouldn't they have been caught in the blast zone?"
    am "In their little bunker where all of them are safe and snug? No explosion is going to get through those doors, dearie."
    show bolt neutral onlayer mc
    hide mia
    hide stoneman
    show magno surprised at rightish
    show frostbite surprised:
        xalign 1.1
    ma "Those rats! They were right beneath our noses the entire time!"
    a "How would we go about finding the entrance to that place?"
    show mia neutral at offscreenright
    am "Hm... does anyone have a map of the place?"
    hide magno with dissolve
    show frostbite at right
    show mia neutral at farright
    with ease
    m "I do- on my laptop. I'm really familiar with the place in and out since we've been there so many times."
    m "I have access to the alarms, their security cameras..."
    am "Oh, you and I will talk dear. I can point everything out to you so you can help your friends later."
    am "The entrance should be located within the main warehouse area. The door {i}must{/i} be opened remotely."
    am "I was gonna see if I could pull some old tricks and favors to get you all into there but... well, looks like you already have everything you need!"
    show frostbite happy
    show bolt happy onlayer mc
    "Mia shies away from everyone's looking at her. Me though? I was looking at her with pride, and so was Alicia and Bastion."
    show bolt neutral onlayer mc with None
    hide frostbite
    hide mia
    show shadow neutral at farright
    show stoneman surprised at rightish
    with dissolve
    s "Any idea on who we should be expecting? Any insights to the superpowers of the people in there?"
    am "That... I actually can't confidently speak on."
    am "I actually wouldn't be too surprised if there wasn't anyone there to greet you."
    show stoneman surprised
    ba "Huh? But they should certainly be expecting us."
    am "Not some{i}one{/i} per se... some{i}thing{/i}. Last time I was around, the boys were putting together all sorts of junk and making them work."
    show stoneman neutralfrown
    s "So... we should be expecting a robot?"
    am "You should be expecting heavy resistance. They'd want to keep their precious Daylight Core safe."
    hide stoneman
    hide shadow
    show snapshot neutral at rightish
    show magno neutral at farright
    with dissolve
    l "Apparently not enough to stick their own necks out though. Do you know why?"
    am "When I left, they were already spread pretty thin as is. And chances are, they've only increased their business load..."
    am "I'm not saying it's not a guarantee, but when your scope involves the world, you can let some small things slip through the cracks."
    ma happy "Hahaha... either way, it's perfect for me! Robot or man will be CRUSHED underneath my power!"
    show frostbite neutral at right
    show mia neutral at farright
    hide magno
    hide snapshot
    with dissolve
    a "Alright, we get in, do everything we have to do..."
    a "Our goal is destroying the crystal.  What do we use to do th-"
    "Fingers point at the disarmed bomb that was sitting on the table literally in front of us."
    show frostbite surprised
    a "Oh."
    "After discussing it further, the plan was set. It was a very straightforward one."
    "Go in. Fight. Blow up their Daylight Core. Get out."
    "I didn't know what to think about what would happen afterwards. If there even {i}was{/i} going to be an afterwards."
    "We all spend the time getting rid of the crystals inside of our uniforms in private."
    "Aunt Matilda was helping set Mia up to get us inside their bunker."
    "It was so quiet the entire time. Everyone was so focused."

    if samuel > bastion:
        jump ch4_s2_shadow
    else:
        jump ch4_s2_bastion

label ch4_s2_shadow:
    scene living room
    hide bolt
    show shadow smirk at center
    show bolt neutral at side onlayer mc
    with Fade(0.75, 0.5, 0.5)

    "Sometime during, out of the blue, Samuel pokes my cheek."
    show bolt surprised onlayer mc
    r "A-Ah! Hey!"
    s "Hey yourself, gorgeous."
    "Wh-What the heck?! NOW, OF ALL TIMES?!"
    s "Haha... just wanted to see your reaction. Figured you could do with a little loosening up."
    show bolt neutral onlayer mc
    r "Gee, {i}thanks.{/i}"
    show shadow neutral
    s "I can see that you're nervous. And I can't really blame you. We're walking into some dangerous territory here."
    show shadow smirk
    s "I just wanted to make sure you know... I've got your back, okay?"
    show bolt happy onlayer mc
    r "... thanks, Sammy."
    show shadow surprised
    s "Sammy? Huh. That's new."
    "I hug him."
    show shadow happy
    "At that moment, I didn't want to stop hugging him."
    "We sit there in silence for a good bit of time before he eventually starts to pull away."
    show shadow neutral
    s "... we have things to do."
    show bolt neutral onlayer mc
    r "We do."
    show shadow smirk
    s "... but imagine what our celebration is going to look like."
    show bolt surprised onlayer mc
    r "H-huh?"
    show bolt shy onlayer mc
    hide shadow with dissolve
    "Samuel turns away, taking his smirk with him. {i}Ugh{/i}. Why does he pride himself on embarrassing me?!"
    "... and why do I enjoy it so much?"
    "Anyway..."
    jump ch4_s2_2

label ch4_s2_bastion:
    scene living room
    hide bolt onlayer mc
    show bolt neutral at side onlayer mc
    with Fade(0.75, 0.5, 0.5)

    show stoneman neutralsmile at center with dissolve
    ba "Rene?"
    show bolt surprised onlayer mc
    r "Oh, Bastion!"
    "I was so caught up in my thoughts, I hadn't noticed Bastion standing right in front of me."
    show stoneman neutralfrown
    ba "... a lot on your mind, huh?"
    show bolt happy onlayer mc
    r "Haha, what gave it away? Was it the everything?"
    show stoneman happy
    "We both share a laugh. Despite the situation we were marching ourselves into, we still manage to laugh with each other."
    show bolt neutral onlayer mc
    r "Did you get your crystal out of your uni--"
    show bolt surprised onlayer mc
    show stoneman neutralsmile
    "Out of the blue, a warmth encompasses my hand."
    ba "..."
    r "..."
    "Bastion gently squeezes my hand."
    ba "I know everything is scary right now. You have every right to be nervous."
    show bolt sad onlayer mc
    r "Bastion... yo-"
    show stoneman sad
    ba "I'm nervous too. I think... I'm the most nervous I've ever been."
    show bolt surprised onlayer mc
    "I look at him in shock. I never would've thought he would just... confess something like that to me."
    "This is our {i}leader{/i}, after all."
    show bolt sad onlayer mc
    "But I understand why. After the revelation earlier, after Bastion found out that he was pushing us for the wrong reasons..."
    "I grab his other hand, just so he's not the only one giving confidence here."
    show bolt happy onlayer mc
    r "Everything's going to be okay."
    show stoneman neutralfrown
    ba "... Rene, please. Please swear to me that you won't push yourself past your limits and get yourself hurt."
    show bolt surprised onlayer mc
    show stoneman sad
    ba "Even if it's for the greater good."
    r "Bastion..."
    "After saying that, he looks almost guilty."
    show bolt neutral onlayer mc
    r "... that won't have to happen. For either of us."
    show bolt happy onlayer mc
    r "Because we're going to go into this with equal effort."
    r "None of us will have to do any of that self-sacrificing nonsense if we have each other's backs, right?"
    show stoneman neutralfrown
    r "You believe in my ability to get things done, right?"
    r "Well, I believe in you in the same way. And that's the only reason why I'm not a nervous wreck right now!"
    show stoneman neutralsmile with dissolve
    "My words are magic, I can see Bastion's doubts just melting away."
    "I was so nervous before, but after saying that... heh, I really rubbed off on myself!"
    "It was something that I needed to hear too. Huh, I didn't know I had it in me!"
    show stoneman happy
    ba "Ha... look at me. I didn't mean for that sorry display, Rene. {i}I{/i} should be the one encouraging {i}you{/i}."
    show stoneman shy
    ba "I guess all of that earlier came from a place of... selfishness?"
    show bolt neutral onlayer mc
    r "Selfishness?"
    show stoneman shy
    ba "Ah... I'm not making sense, am I? I'm sorry, I really shouldn't be dropping this all on yo--"
    show bolt happy onlayer mc
    r "I like you too, Bastion."
    show stoneman surprised
    "He stops. No blushing, no rambling."
    show stoneman happy
    "Just a self-assured, dorky smile. I respond with giving one of my own."
    ba "... well then, shall we?"
    r "We shall!"
    jump ch4_s2_2

label ch4_s2_2:
    scene living room
    hide bolt
    show bolt neutral at side onlayer mc

    "Everyone was ready. We were as prepared as we were ever going to be."
    show mia neutral at right
    show aunt matilda happy at left
    with dissolve
    "Mia was the last to join us, fresh off of a debriefing with Aunt Matilda."
    am "She takes good notes, this one! I really don't want to understate it. She {i}may{/i} just have ended up saving your lives."
    show bolt happy onlayer mc
    r "I always knew you secretly had a superpower, Mia!"
    m surprised "Note taking? Not the most extravagant super power, but I enjoy it...!"
    hide mia
    hide aunt matilda
    show snapshot surprised at left
    show stoneman neutralsmile at right
    with dissolve
    l "Huh, maybe that's why we haven't won after all this time. Should we have gotten ourselves a cute little hack girl that could disarm bombs?"
    ba "Try as you may... I doubt any of them could be as great as Mia."
    l "Eh, money can buy a lot of things."
    show bolt neutral onlayer mc
    "That was coming from the person who was the most decked out in gear."
    "A superpower that lets you never miss must be {i}expensive{/i} for upkeep."
    hide snapshot
    hide stoneman
    show magno angry at left
    show shadow neutral at right
    with dissolve
    ma "I am getting impatient. Shall we proceed?"
    s "Slow your roll. Rushing into this when some of the team might not be ready is going to be a recipe for disaster."
    ma "We are wasting time!"
    hide magno
    hide shadow
    show frostbite annoyed at left
    show mia annoyed at right
    with dissolve
    a "You're wasting our air, but we're not complaining about it..."
    show bolt angry onlayer mc
    r "Hey hey hey! Come on, let's not fall apart right now! Not before the biggest fight of our lives!"
    show bolt happy onlayer mc
    r "You know what this group needs right now! Some good pep! How about a good chant and a huddle!"
    "I place my hand out in front of me."
    show frostbite surprised
    show mia neutral
    a "... seriously? How could you be acting like this right now?"
    "Mia places her hand on top of mine, followed by Bastion and Levina, who seems wildly amused with everything right now."
    show frostbite neutral
    "Alicia rolls her eyes, but succumbs to us very shortly afterwards."
    "The peer pressure is also too strong for Samuel, who tries to act cool by putting his hand {i}underneath{/i} mine."
    show mia annoyed
    "Magno, to the surprise of no one, doesn't care too much about this show."
    m "You know, Magno, you cou-"
    hide frostbite
    hide mia
    show snapshot neutral at center
    with dissolve
    l "Shhh. It's not worth it."
    hide snapshot
    show aunt matilda neutral at center
    with dissolve
    "Another hand reaches into the pile- Aunt Matilda's."
    show aunt matilda surprised
    am "Why are you all looking at me like that? I'm part of this too!"
    s "Alright, well, we all have our hand in. What are we chanting?"
    show bolt surprised onlayer mc
    "Oh crap, that's right. Uh..."
    hide aunt matilda
    show shadow neutral at left
    show stoneman neutralsmile at right
    with dissolve
    s "Smooth plan."
    show bolt shy onlayer mc
    r "Hey, shush! I'm thinking!"
    ba "Maybe... heroes?"
    show bolt neutral onlayer mc
    hide stoneman
    show frostbite sad at right
    with dissolve
    a "That doesn't... feel right at the very moment."
    s "Villain hunters?"
    show frostbite neutral
    a "Uh-uh. Doesn't feel right either."
    hide shadow
    show snapshot happy at left
    with dissolve
    l "Suicide squad."
    show frostbite annoyed
    a "AbsoLUTEly not!"
    hide snapshot
    show mia neutral at left
    with dissolve
    show frostbite neutral
    m "If I may make a suggestion... since we're going up against an organization called Daylight..."
    m "Why don't we call ourselves Nightfall?"
    "That makes an immediate impression on everyone."
    "It seems to strike a chord-- I even catch Magno sticking out his bottom lip and nodding to it."
    show bolt happy onlayer mc
    r "Nightfall it is? Ready everyone? One... two..."
    show frostbite annoyed
    a "Hold on! Let Mia countdown! It was her idea!"
    show bolt shy onlayer mc
    r "Oh! Right, right. Mia, if you would please..."
    show bolt happy onlayer mc
    show mia happy
    m "With pleasure. Ahem..."
    m "One... two... three!"
    show frostbite happy
    "Nightfall!"
    "And just like that..."
    "We plunged ourselves into what was going to be the longest part of this night."
    show bolt neutral onlayer mc
    "What could potentially be our final one."
    jump ch4_s3_1

label ch4_s3_1:
    scene park night
    hide bolt
    show bolt neutral at side onlayer mc
    with Fade(0.75, 0.0, 0.0)
    "We left the house with our heads held high."
    "It was no secret that everyone was feeling either nervous, uncertain or extremely murderous."
    "But we kept walking forward."
    "You can think that's because we had no other choice, that it was either fight or die..."
    "But that couldn't be further from the truth."
    "In this long night, where long time enemies made alliances, ate crackers and drank juice together and made a plan against an unknown enemy..."
    "None of us fell into deep despair."
    "We're all motivated. Motivated by each other. Motivated by a single cause."
    "When you feel that way with a lot of people, you feel like nothing in the world can stop you."
    "Yes. This. This is something that we {i}want{/i} to do."
    "Either to protect each other, for the fun of it, for revenge... we all want to do it."
    "We had so many choices, and the one we all chose is what has us all marching together right now."
    "Marching as {i}Nightfall{/i}."

    scene warehouse inside
    show bolt neutral at side onlayer mc
    with Fade(0.75, 0.5, 0.5)

    "There it is. Where the source of all our problems lies."
    "And where it's going to be buried."
    "The team entrusted me with the bomb because of my abilities."
    "It only made me a little scared to have something in my hand that could destroy everything and everyone I love in a second."
    "But I understand."
    show mia neutral at center with dissolve
    m "There it is..."
    "Mia looks down at her laptop, which has an impressively detailed map of the warehouse on the screen."
    m "The entrance should be in the main warehouse area, where we all met each other last time."
    show mia at right with ease
    show snapshot neutral at left with dissolve
    l "Are those little dots us?"
    m "Mhm. Turns out, there's a very complex security system here that I never had access to."
    m "It was very well hidden... we can thank your Aunt for this, Rene."
    show bolt happy onlayer mc
    r "Yeeeah. She's pretty awesome, isn't sh-"
    play sound "ping.mp3" loop
    show bolt surprised onlayer mc
    show mia surprised with None
    show snapshot surprised
    show frostbite surprised at rightish behind mia with dissolve
    a "What... is that?"
    "I immediately held the bomb in front of me-- but the sound wasn't coming from that. Phew."
    stop sound
    "Instead, the sound was coming from Mia's laptop."
    m "There's... uhm...!"
    show snapshot neutral
    l "Party time."
    "On her laptop, multiple tiny dots appeared on the screen."
    show frostbite annoyed
    "It looked like an army of ants marching, all pouring down to where we were on the map."
    play sound "gunshot.mp3"
    show bolt surprised onlayer mc
    show frostbite surprised
    "A gunshot goes off. We all look up to see Levina with her rifle out. Past the smoking barrel of her gun, on the ground, was a person."
    "... not a person, actually. It was a white and yellow... robot?"
    "Electricity arced outside of the massive hole Levina just blew inside of it."
    show snapshot happy
    l "Well, thank god I brought my armor piercing bullets."
    show snapshot neutral
    l "Actually, how about we go about thanking me?"
    show bolt neutral onlayer mc
    show frostbite annoyed
    show mia neutral
    "The doors to the warehouse open, and a formation of robots begin to file out towards us."
    "Not only from the warehouse- to the left and right of it. Above it, on the roofs. All around."
    hide snapshot
    hide frostbite
    hide mia
    show shadow smirk at left
    show stoneman neutralsmile at right
    with dissolve
    s "Heh. Looks like they're throwing the kitchen sink at us too."
    ba "No matter what, that's not going to stop us!"
    ba "Everyone, remember what we talked about. We're going to go in with a tight formation around Rene and Mia-"
    ma "BAH! They send ROBOTS after ME?! A master of magnetism?! What an insult! An affront to my splendid power!"
    "Magno raises his hand, floating a dozen or so robots into the air, and sends them crashing into each other."
    show stoneman surprised
    ba "Magno! Remember the pla-"
    show shadow angry
    s "Hey, this is a good thing. They're all robots. Let's just get going!"
    show stoneman neutralsmile
    ba "Right... come on everyone!"
    hide stoneman
    hide shadow
    show frostbite annoyed at center
    with dissolve
    a "Rene, Mia, stay behind us!"
    hide frostbite with dissolve
    "The tide of robotic soldiers continues, but with our combined might, we carve our way through."
    show mia sad at center with dissolve
    "Mia is being protected from the danger because... well."
    hide mia with dissolve
    "And I have to be guarded in the middle as I cradle the bomb like a baby in my arms."
    show bolt hurt onlayer mc
    "I don't wanna know what happens if I move it around {i}too much{/i}."
    play sound "<from 10.0>metal-hit.mp3"
    pause(1.5)
    stop sound fadeout 4.0
    show bolt neutral onlayer mc
    show stoneman angry at center with dissolve
    "Bastion... or should I say, Stoneman, uppercuts the head off of an approaching robot."
    "Another gives him a harsh whack to the face, but he doesn't feel anything." with sshake
    "He headbutts the robot square against the head, sending it spiraling to the ground."
    play sound "shadow.mp3" volume 0.8
    show stoneman at left with ease
    show shadow angry at right with dissolve
    "Shadow manipulates the darkness of the night around him into tendrils, and impales a slew of robots like a skewer." with woosh
    "If I didn't know any better, I'd say the two of them have been working together for years."
    "The way they move in tandem, pushing us forward into hostile territory..."
    play sound "<from 1.0>gunshots.mp3" volume 0.6
    hide shadow
    hide stoneman
    show snapshot annoyed at center
    with dissolve
    "Levina is as vicious as ever, letting loose an onslaught of gunfire on anything that comes within sight." with sshake
    "From the outside it looks like she's firing wildly, but in reality, every bullet was finding their mark."
    "In the midst of all of this, I spot some robots on the roof."
    show bolt surprised onlayer mc
    "It looked like they were carrying... weaponry! Are those... missile launchers?!"
    r "O-Oh no! Everyone, look ou-"
    play sound "<to 1.0>gunshot.mp3"
    queue sound "explosion.mp3" volume 0.5
    show snapshot neutral
    "Before I even finish my sentence, Levina aims a gun up there and, without hesitation, fires a bullet." with sshake
    "The bullet must've hit one of the rockets."
    show bolt neutral onlayer mc
    l "I was already handling it."
    hide snapshot
    show frostbite surprised at center
    with dissolve
    a "Look out!"
    show bolt surprised onlayer mc
    "As soon as I look, I see a robot lunging wildly at Mia."
    show frostbite at right with ease
    show mia surprised at left with dissolve
    m "Eep!"
    play sound "freeze.mp3" volume 0.3
    show frostbite angry
    "Alicia is quick on her feet, placing her hand on the robot and freezing it before it could throw a punch."
    play sound "shatter.mp3" volume 0.3
    show bolt angry onlayer mc
    "I follow up with a kick, shattering it completely." with woosh
    m "Th-thank you!"
    show frostbite neutral
    a "Good job, Bol- Rene!"
    show bolt happy onlayer mc
    r "Not too shabby yourself, Ali!"
    show mia neutral
    "We pave our way forward. Anything that dares stand in our way is left utterly destroyed."
    "We are a machine. A... machine destroying machine!"
    "Guided by Mia, we all make our way into the warehouse."
    "The resistance doesn't let up. When one goes down, it feels like two replace them."
    "We're here where it all started. Inside of the warehouse."
    "But instead of us being pitted against each other... well, it really does feel like it was us against the world."
    m "The entrance should be below here! Give me a moment to open it!"
    "I look around. How can there be an underground entrance {i}anywhere{/i} in here?"
    "The minute it takes Mia to figure everything out is maybe the most hectic minute of our lives. Everything is so fast, so {i}visceral{/i}."
    hide mia
    hide frostbite
    with dissolve
    show bolt angry onlayer mc
    "The constant sound of gunfire, large hunks of metal being levitated and tossed around, circuits and sparks scattering everywhere." with sshake
    show bolt neutral onlayer mc
    "When the minute's up, it feels like everything suddenly grinds to a halt."
    "There is a moment where everyone just stands still, no more robots in sight."
    show frostbite hurt with dissolve
    a "{i}Huff{/i}... {i}huff{/i}... is it over?"
    hide frostbite
    show snapshot neutral
    with dissolve
    l "I wouldn't count on it. Where are we with the hacking stuff?"
    hide snapshot
    show mia neutral
    with dissolve
    m "It's almost done... in the meantime... I just figured out that these robots are being remote controlled..."
    hide mia
    show magno angry
    with dissolve
    ma "Bah! Cowards!"
    hide magno
    show stoneman neutralfrown
    with dissolve
    ba "Wait, Mia. Does that mean it's possible you can--"
    play music "alarm.mp3" volume 0.2 loop
    play sound "machinery.mp3"
    show warehouse alarm
    show bolt surprised onlayer mc
    show stoneman surprised
    "The ground shakes as a red alarm light sweeps the room."
    "We all gather together, watching the floor open up in front of us."
    "A small bunker with strong looking reinforced doors slowly lifts itself out of the ground and presents itself to us."
    "The whirring of machinery, the red alarm light... it really does feel like the buildup to a game's final boss."
    stop music fadeout 5.0
    r "So, this is what they've been hiding under our noses the entire time..."
    hide stoneman
    show shadow neutral
    with dissolve
    s "Huh... can't say I'm not impressed."
    s "The end... is right past there."
    show mia neutral
    hide shadow
    with dissolve
    m "I'm going to need another minute on the door. Matilda said I shou-"
    play sound "<from 3.5>machinery.mp3"
    show bolt surprised onlayer mc
    show magno angry at offscreenright
    m surprised "Ah!"
    show magno angry at center with ease
    hide mia with dissolve
    ma "No need to wait! I'll just rip the damn doors off myself!"
    "The doors slowly begin to fold into themselves."
    show bolt neutral onlayer mc
    "After a couple of mighty yanks, the doors are ripped off their hinges, Magno suspending them in the air."
    hide magno
    show snapshot happy
    with dissolve
    l "Well, that's one way to do it. Well then, Rene. The floor's all you-"
    play sound "metal-crash.mp3" volume 0.5
    "Magno sends the massive steel doors flying over our heads without warning."
    hide snapshot
    show frostbite surprised
    with dissolve
    a "Woah! H-Hey!"
    "Before we could ask why, we received our answer."
    "Multiple robots were crushed underneath the door, but that wasn't enough to deter the others from approaching us." with sshake
    show bolt hurt onlayer mc
    show frostbite annoyed
    "A second wave. And we're all already so tired."
    hide frostbite
    show snapshot happy
    with dissolve
    l "Ha... I could do this all day."
    show bolt neutral onlayer mc
    r "Alright, everyone! I should start going in and set the bom-"
    "I whip my head over to the bunker entrance to see that Magno is already going down the stairs."
    show bolt angry onlayer mc
    r "Hey!"
    show snapshot neutral
    l "Hey kid, go do your job. We'll stay up here and do our best to hold them off."
    show bolt neutral onlayer mc
    hide snapshot
    show frostbite happy at right
    show mia neutral at left
    with dissolve
    a "Yeah. Go do what we came here to do, Rene!"
    m "You don't have to worry about us... I think if I have a minute, I could do something about these remote controls..."
    "I nod. There wasn't any time to argue. It was do or die. I turn to the bunker, and take a deep breath."
    if samuel > bastion:
        jump ch4_s3_shadow
    else:
        jump ch4_s3_bastion

label ch4_s5_1:
    scene black
    hide bolt onlayer mc
    with Fade(0.75, 0.5, 0.5)
    "..."
    "It's been a few days."
    "After teleporting, everything just went straight to black."
    scene living room
    show bolt neutral at side onlayer mc
    with Fade(0.0, 0.0, 1.0)
    show mia happy at farleft
    show frostbite happy:
        xalign 1.2
    show shadow smirk at left
    show stoneman happy at right
    show aunt matilda happy at center
    "I woke up on my aunt's couch as she was tending to me."
    "As soon as I opened my eyes, I was descended upon by the smiling faces of all of my friends."
    show bolt surprised onlayer mc
    "My return to consciousness was accompanied by celebratory shouts and woops."
    "It was a little mean to me personally, they didn't even let me get my strength back so I could yell with them..."
    show bolt happy onlayer mc

    if samuel > bastion:
        "Aunty, Alicia, Mia, Bastion..."
        "And Samuel. He was trying to hide the fact that he was seriously hurt behind all that coolness... but I could tell."
        "But what matters the most is that he was okay. We were okay. The two of us."
    else:
        "Aunty, Alicia, Mia, Samuel..."
        "And Bastion, who was doing everything he can to look like he wasn't hurt. But I could tell he was putting on a brave face."
        show bolt sad onlayer mc
        "You idiot... What happened to all of that talk about not being self-sacrificing?"
        show bolt happy onlayer mc
        "But what matters most now is that he's okay. We were okay. The two of us."

    "The sight of all of them together is so comforting... but I couldn't help but divide my attention between them and the sun outside."
    "I forgot how nice it looked. At that moment, I wanted to bathe in its warmth more than anything."
    show bolt neutral onlayer mc
    "But that can wait."
    "The operation was a success. Mia had been keeping tabs on the energy register in the warehouse, and there was nothing to report."
    "A large explosion had taken place, which the police were looking into."
    "Levina had kept her promise."
    "I tell them everything that happened."
    show frostbite surprised
    show mia surprised
    show shadow neutral
    show stoneman neutralfrown
    show aunt matilda sad
    "What we saw when we went down there, the giant robot that stood in our way, about Magno and Levina. Everything."
    "Everyone seemed to be confused by Levina, some of them were horrified with what she'd done."
    "Everyone except Samuel, who had a quiet understanding."
    hide aunt matilda
    hide shadow
    hide stoneman
    hide frostbite
    hide mia
    with dissolve
    "We spend the next few days healing and laying low."
    "We keep our eyes on the media, trying to discern if anyone was getting close to discovering our identity..."
    "No, they weren't able to find anything besides some charred bits of robots."
    show aunt matilda neutral at left
    show mia neutral at right
    hide bolt onlayer mc
    show rene neutral  at side onlayer mc
    with dissolve
    "One day, Aunt Matilda and Mia gather everyone in the living room. The two of them had been researching for a few days."
    show rene sad onlayer mc
    "They inform us of more crystals. The huge ones, like the one we saw underground. How many there are."
    "One for each state. This was a worldwide operation."
    "We may have stopped Daylight here... but this was a minor hindrance more than anything."
    "We don't even bring up the discussion of if we want to continue this fight against them or not. Everyone was tired of fighting."
    "Some of us wanted to go back to college and revert to a nice, quiet life."
    show rene neutral onlayer mc
    "Mia made it her mission at that time to alert other superhero groups to the efforts of Daylight, so that eased the pressure on us."
    "We don't {i}have{/i} to act. We don't {i}have{/i} to be the ones to chase after Daylight."
    show rene sad onlayer mc
    "I mean, what difference would we make? If you really break us down. you'd realize..."
    show rene neutral onlayer mc
    "... we're just a bunch of people who want to live happily."
    jump endings
