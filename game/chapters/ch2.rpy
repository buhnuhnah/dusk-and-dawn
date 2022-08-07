label ch2_s1:
    scene college classroom day
    show rene neutral at side onlayer mc
    with Fade(0.75, 0.5, 0.5)
    "The next day I feel a lot better, physically anyways."
    "I still have not reached a decision about whether my self-sacrificing behavior is a good thing or not."
    "Prof. Brown" "Rene, could you deliver those papers to Professor Smith in the Music department?"
    "That's the next building over on our campus."
    show rene happy onlayer mc
    r "Of course, Professor. Where can I find Professor Smith?"
    "My economics professor gives me the directions and I head to the Music department, a heroic quest to deliver some very important papers."
    scene college classroom day with fade
    "When I approach the classroom I can hear singing inside. Whoever's singing has a beautiful voice."
    s "*lyrics*"
    "He looks familiar but he's too far for me to tell for sure."
    show rene neutral onlayer mc
    "But man, this song is supposed to be a happy one. Why is he struggling to convey happiness so much?"
    "Prof. Smith" "Again, Samuel. This song is supposed to be about joy. Your singing is making me sad instead."
    "The professor agrees with me... I guess the student is called Samuel."
    "Samuel... Samuel... Do I know him?"
    "Maybe I should help him sing? I've got plenty of happiness. Maybe I could cheer him up..."

menu:
    "Sing with him":
        $ samuel += 5
        jump sing_ch2
    "Wait for them to finish":
        jump wait_ch2

label sing_ch2:
    show rene happy onlayer mc
    show samuel smirk at center with dissolve
    "I step inside the classroom and join Samuel in singing."
    r "*lyrics*"
    s "*lyrics*"
    "It worked! We finish the song together with smiles on our faces."
    show rene surprised onlayer mc
    "That smirk... oh my gosh, I do know him! Samuel is... Shadow! Woah!"
    s "Thank you!"
    "Prof. Smith" "...an unconventional way of solving the problem, but if it works, it works."
    jump ch2_s1_2

label wait_ch2:
    "I shouldn't interrupt. This Samuel might sound familiar, but I don't know him as far as I can tell."
    "It's almost hard to listen to though, he just makes the song sound sad."
    "When he finally finishes singing, I push open the door and make my presence known."
    show rene surprised
    show samuel neutral at center with dissolve
    "But as I step in closer I realise where I know Samuel from. Samuel is... Shadow! Woah!"
    jump ch2_s1_2

label ch2_s1_2:
    "Prof. Smith" "Who are you? Are you one of our students? I don't recognise you."
    show rene happy onlayer mc
    r "My name is Rene Garcia. I'm a student of economics, I just came from across the campus."
    show samuel surprised
    "At the sound of my voice, Shadow- Samuel freezes and looks at me wide-eyed."
    s "Bolt...?!"

menu:
    "Admit that you are Bolt":
        $ samuel += 5
        r "That's me, yes."
        jump ch2_s1_3
    "Deny it":
        $ hide_identity = True
        show rene neutral onlayer mc
        r "You must have me mistaken for someone else."
        show samuel angry
        s "Don't lie to me! I know it's you."
        jump ch2_s1_3

label ch2_s1_3:
    show samuel angry
    s "What are you doing here?!"
    "Prof. Smith" "Do you know each other?"
    show rene neutral onlayer mc
    r "We work... together."
    s "Don't approach me outside of work."
    show rene angry onlayer mc
    r "I'm not here because I'm stalking you or something. Professor Brown asked me to deliver those papers."
    "I hand the documents to Professor Smith."
    "Prof. Smith" "Ah, thank you."
    s "So the task is done. Leave."
    r "Why are you so rude?"
    s "Just leave. Now."
    r "Fine. I'm going, I'm going."
    hide samuel with dissolve
    "What the hell was that? Does he dislike the sight of me that much?"
    show rene neutral onlayer mc
    "Maybe I hurt him more than I thought two days ago... and that's why he's so upset with me..."
    show rene sad onlayer mc
    "Why does it hurt so much though? We're not even friends."
    if bastion >= 10:
        jump ch2_s1_b1
    else:
        jump ch2_s2

label ch2_s1_b1:
    "Ugh... i have to get my mind off of that."
    show rene neutral onlayer mc
    "By this point, class was over. I had decided to hang out with Dusk after classes in the park."
    "I wonder if I should head back and meet Bastion? Or maybe I should just head to the park..."
menu:
    "Head straight to the park":
        "We're going to the same place anyways, I'll just go ahead and get a head start. Give me some time to think..."
        jump ch2_s2
    "Check on Bastion":
        jump ch2_s1_b2

label ch2_s1_b2:
    "I should find him. Maybe we could talk about some of the thoughts I've been having recently..."
    "I dunno. Just anything to occupy my mind so I don't think about Samuel."
    scene college classroom day
    hide rene onlayer mc
    show rene neutral at side onlayer mc
    with Fade(0.75, 0.5, 0.5)
    "I head back to the classroom after the bell's rung. Honestly, I'd be surprised if anyone was still in there."
    show bastion worried at center with dissolve
    "He's writing so furiously- I swear, if he was writing any faster, I'd start seeing smoke come up from the paper."
    show rene happy onlayer mc
    r "Bastion!"
    "...he doesn't respond? Not even a glance? He just keeps writing."
    show rene neutral onlayer mc
    r "Bastion?"
    "I walk up to him. He was paused in thought, absentmindedly drilling the eraser end of his pencil into his temple..."
    "I lean in front of him."
    r "Ba--"
    show bastion surprised
    show rene surprised onlayer mc
    ba "Uwaaaah!" with sshake
    "He flails in surprise, sending a flurry of papers into the air."
    r "W-woah!"
    ba "Rene?! Oh, I'm-- I'm sorry!"
    r "No, it's-- it's fine! Lemme just-- oof!"
    "As soon as I bend down to pick up some of the papers, my forehead collides with Bastion's."
    "Yeeowch! He's got a hard head!" with hit
    show bastion worried
    ba "O-oh my goodness-- Rene! Are you okay?!"
    show rene sad onlayer mc
    r "Yes! Yes I'm-- I'm {i}fine{/i}!"
    ba "Are you sure? I can get you to the infirma-"
    "He's more worried about me {i}now{/i} than when I was injured?!"
    show rene angry onlayer mc
    r "I said it's fiiiiine!"
    show rene neutral onlayer mc
    "What a {i}disaster{/i}."
    "After we both manage to gather the papers without getting a concussion, the two of us calm down."
    show bastion neutralfrown
    "Well... {i}I{/i} have. Bastion still seems a bit embarrassed."
    r "Bastion, are you okay?"
    ba "Yeah... my apologies, Rene. I was just... deep in thought."
    "Deep in thought? Hm..."

menu:
    "I shouldn't pry.":
        "A lot seems to be on his mind right now. Must be about school things..."
        jump ch2_s1_b4
    "Ask what's on his mind.":
        $ bastion += 5
        r "Well?"
        ba "Hm?"
        "I take a seat next to him. I guess he realizes what I'm about to say next, because he immediately looks sheepish."
        r "Well... what's on your mind?"
        ba shy "Oh, y-know..."
        "..."
        "......"
        "........."
        r "I... don't know? Actually?"
        ba "I meant uh... school things, y'know?"
        "Uh-uh, no. That's not it."
        show bastion neutralsmile
        ba "Like, for example, we just learned about collective decision making. I'm still thinking abo--"
        r "Is that what's really on your mind, Bastion?"
        show bastion neutralfrown
        "He sighs. He's not very good at covering it up."
        "It's strange. He's so confident whenever we're out on the field, but right now? He's a pale image of the confident leader I always see."
        ba sad "Maybe... not right now."
        r "...alright. But remember this..."
        "I give him a poke on his hard, vulnerable forehead."
        show rene happy onlayer mc
        r "We're a team!"
        show bastion shy
        "His cheeks flare, but he quickly saves face with that goofy grin I'm so familiar with."
        show bastion happy
        ba "Of course, of course! Haha, I can always rely on you, Rene!"
        show rene neutral onlayer mc
        "...huh, why do I feel so disappointed?"
        "Truth be told, I kinda enjoyed that shy face of his. It was kinda..."
        show rene surprised onlayer mc
        "Ah, what am I thinking?"
        jump ch2_s1_b4

label ch2_s1_b4:
    show bastion happy
    show rene neutral onlayer mc
    ba "Ahem. In whatever case... we should be heading to the park to meet the others, yes?"
    show rene happy onlayer mc
    r "Yes! Shall we?"
    ba "Let's not keep them waiting, then!"
    "And just like that, our spirits are high."
    "Bastion. He's not the most charismatic leader, but he makes up for it in spunk."
    "When he's around, I genuinely feel bolder around him."
    "...of should I say {i}boulder{/i}?"
    "Ahem. Anyways, since our spirits are high, maybe I can do something to lighten the mood a bit more?"
    "I feel like Bastion still hasn't shaken off that incident earlier..."

menu:
    "The team's waiting. Let's just go.":
        show rene neutral onlayer mc
        "The rest of Dusk is waiting for us. Let's just go ahead and meet them... killer jokes are better with a crowd anyways."
        jump ch2_s2
    "Let's make it light.":
        $ bastion += 5
        r "Then come on, ol' chap!"
        "I strike a goofy pose and offer an arm, smiling right at Bastion."
        "Bastion seems taken aback... but he's smiling."
        ba "Haha, what's gotten into you?"
        r "Don't take my chipper attitude for {i}granite{/i}, Bastion!"
        "{i}Oof{/i}, that one hurt {i}me{/i}. But... I can see that I got him. He can't help but laugh."
        ba "Ah, I see. Because... rocks."
        r "Mhm! And what better {i}rock{/i}star to share these {i}solid{/i} jokes with than you?"
        ba "Rene... I'm afraid your path in comedy has hit rock bottom."
        "{i}Hey.{/i}"
        r "I just hook my arm around his and pull him along. All while he's laughing."
        "For that moment, it looks like he's forgotten everything that was worrying him."
        "I'm glad I could help him forget whatever was on his mind, even for a moment."
        show rene neutral onlayer mc
        r "Hey, just curious... does your brain... become like, you know, {i}hard{/i} whenever you use your powers?"
        ba "Of course!"
        show rene surprised onlayer mc
        r "Wait, really?"
        ba "How else are my plans so {i}solid{/i}?"
        show rene happy onlayer mc
        r "Oh my goodness-- you're worse than me!"
        jump ch2_s2

label ch2_s2:
    scene park day
    hide rene onlayer mc
    show rene neutral at side onlayer mc
    show mia happy at left
    show alicia happy at center
    show bastion neutral at offscreenright
    with Fade(0.75, 0.5, 0.5)
    show bastion neutralsmile at right with ease
    m "And then Professor Miller said..."
    a "Really, I thought..."
    "I realise I’m not listening to the conversation at all."
    "The Dusk team: Bastion, Alicia, Mia and I decided to hang out together after school at the park."
    "It’s nice to spend time together outside of work…"
    show rene sad onlayer mc
    "But I can't focus. I keep thinking about Shadow's reaction to me discovering he's Samuel."
    "All this time he was living his life so close to me and I didn't realise. I feel weird about this."
    "He's right - it was easier when I saw everything as black and white."
    "But I can't anymore. Shadow is a real person trying to live his life, not just an anonymous enemy."
    if villain >= 10:
        "But after all, why can't it be? Knowing my enemies shouldn't necessarily interfere with the way I work."
    show bastion happy
    ba "...what do you think, Rene?"
    r "Uh I'm sorry. I wasn't listening."
    m sad "Is something wrong?"
    show bastion worried
    ba "Ever since you got injured in the fight, you've been out of it."
    a sad "Does it still hurt?"
    r "It does a bit. But it impacted me more mentally than I thought it would. I keep thinking - was it the right thing to do?"
    if bastion < 15:
        ba neutralsmile "We won thanks to you."
    else:
        ba neutralfrown "Uhm... of course. It was the right thing to do..."
        "Well, you don't look to sure about it."
    r "Did we really win? The mission, maybe. But the fight against Dawn? It seems never-ending. How long have we been fighting them now?"
    a neutral "Over a year."
    m neutral "It feels like much longer..."
    ba worried "Are you having second thoughts about being part of Dusk?"

menu:
    "Deny it. Of course you don't. You love your team.":
        show rene surprised onlayer mc
        r "No! I love Dusk. It's just that... lately we get called in so often to steal things from Dawn..."
        ba neutralsmile "...not steal, secure."
        jump ch2_s2_2
    "Admit that you do":
        $ villain += 10
        show rene neutral onlayer mc
        r "The thought of quitting the team did, in fact, cross my mind..."
        show bastion surprised
        show alicia surprised
        show mia surprised
        "They all look at me in shock."
        m "You can't be serious!"
        jump ch2_s2_2
    "Lie that you don't":
        $ villain +=5
        show rene surprised onlayer mc
        r "No, of course not. I love Dusk."
        show rene neutral onlayer mc
        "I don't but they won't see me admitting that."
        r "It's just that... lately we get called in so often to steal things from Dawn..."
        ba neutralfrown "...not steal, secure."
        jump ch2_s2_2

label ch2_s2_2:
    show rene sad onlayer mc
    r "Whatever. And somehow Dawn always knows we'll be there."
    a annoyed "Are you suggesting one of us is a traitor?"
    if villain >= 15:
        "She looks at me with suspicion in her eyes."
        show rene neutral onlayer mc
        r "Anything you want to say Alicia?"
        show alicia surprised
        "She shakes a bit but doesn't reply. She's terrified of me. How fun."
        jump ch2_s2_3
    else:
        show rene angry onlayer mc
        r "Of course not! I'm just saying it's weird and that's all."
        m neutral "It is weird, that's true..."
        show bastion sad
        ba "Maybe you're right."
        jump ch2_s2_3

label ch2_s2_3:
    show rene sad onlayer mc
    show bastion worried
    show alicia sad
    show mia sad
    "Silence falls as we all analyse the past year in our heads."
    "With the mood gone south, we all begin to head our separate ways. No one is in the mood to joke around like usual."
    "Something weird is going on. I can feel it."
    "I just hope we will survive it as a team."
    if bastion >= 15:
        "I noticed Bastion and his looks of doubt."
        "Not only that, but his looks of... worry? Whatever it is, he's being quiet about it..."
        "What are you thinking about?"
        "Are you having the same doubts as me?"
    jump ch2_s3

label ch2_s3:
    scene living room
    hide rene onlayer mc
    show rene neutral at side onlayer mc
    show aunt matilda happy at center
    with Fade(0.75, 0.5, 0.5)
    "In the evening I decide to visit my Aunt Matilda. The two of us have always had a close relationship."
    "Aside from my team members whom I've known for a year now, she is my closest friend."
    "While other friends entered my life and left it, she remained a pillar of stability."
    "There is a difference in ages of course. But Aunt Matilda feels 20 years younger than she is. She is my mother’s younger sister."
    "Always cheerful and kind, she has her own studio where she paints."
    "Her paintings hang in the city’s gallery and sell for piles of money."
    show aunt matilda surprised
    am "Hi, Rene! Oh, what happened to you?"
    "She notices the ugly bruise on my arm which refuses to fade. It changes color everyday and glares back as I glare at it."
    show rene happy onlayer mc
    r "It's nothing. I just bumped into my closet real hard."
    am angry "You're so clumsy. Show it to me."
    "She touches the bruise and tries to be gentle."
    show rene hurt onlayer mc
    r "Ouch!"
    "But it still hurts like a bitch."
    show aunt matilda neutral
    "Through the pain, I feel that Aunt Matilda's touch is cold and pleasant."
    "Suddenly the pain stops."
    show rene surprised onlayer mc
    r "...what?"
    show aunt matilda surprised
    am surprised "What's wrong?"
    r "It doesn't... hurt anymore..."
    show aunt matilda happy
    am happy "That's great!"
    show rene neutral onlayer mc
    r "...I suppose."
    "But why did it suddenly stop hurting? I look at it and the bruise is much less remarkable. Weird."
    am neutral "So... is there anything troubling you? You don't normally bump into furniture."
    show rene sad onlayer mc
    "I wish I could talk about my super life with her."
    "An outsider's perspective on what is happening would be so valuable, especially my Aunt's who I know deeply cares about me."
    am  "If you are not gonna say anything, I'm going to get angry!"

menu:
    "Say it's about a boy":
        $ samuel += 5
        jump boy_ch2
    "Say you quarreled with your friends":
        jump friends_ch2

label boy_ch2:
    show rene sad onlayer mc
    r "I... met a guy... and I'm having some trouble communicating with him."
    show aunt matilda happy
    am happy "Finally love troubles, oh my cute little Rene!"
    show rene shy onlayer mc
    r "No no no! Not that kind of trouble!"
    am "I thought you'd never find a boy you would be interested in."
    show aunt matilda neutral
    am neutral "As open as you are to meeting new people, you've never been interested in forming such a close attachment to anyone but your friends."
    r "I'm just... I have to know someone first before I'm attracted to them."
    am "Oh, I understand that. Don't worry. Do you want to talk about it?"
    show rene sad onlayer mc
    r "I'm sorry, Aunty. I would prefer not to."
    show aunt matilda happy
    am happy "Whenever you are ready then!"
    jump ch2_s3_2

label friends_ch2:
    show rene sad onlayer mc
    r "I had... a fight with my friends."
    show aunt matilda surprised
    am surprised "Oh no! With Alicia, Mia, and Bastion?"
    r "Yes... Bastion took my side, while the girls were against me."
    show aunt matilda neutral
    am neutral "Oh no, what divided you so?"
    r "Something I've done at work. But I can't tell you what."
    show aunt matilda sad
    am sad "I'm sorry to hear that but I understand."
    jump ch2_s3_2

label ch2_s3_2:
    show aunt matilda happy
    am happy "It seems to have been a hard week for you. How about we bake a cherry pie?"
    show rene happy onlayer mc
    r "Oh yes! My favourite cake is bound to cheer me up!"
    am "To the kitchen then!"
    "We spend some time baking a cake and talking about nothing important."
    "I feel relieved not having to think about my troubles for a few hours."
    jump ch2_s4

label ch2_s4:
    scene warehouse outside
    hide rene onlayer mc
    show stoneman neutralfrown at center
    show bolt neutral at side onlayer mc
    with Fade(0.75, 0.5, 0.5)

    "Another mission to fetch a package, another Dawn warehouse. Those places all look the same to me."
    st worried "Why are they sending us on another similar quest? And so soon? Bolt is still not fully healed..."
    show bolt surprised onlayer mc
    b "Actually I am. Don't know how but I am."
    "I looked over my wounds yesterday evening and surprisingly they were all healed."
    "I have no idea what caused this sudden acceleration but it happened."
    show bolt neutral onlayer mc
    b "Let's get this over and done with quickly."
    show stoneman neutralfrown
    "This time it's just the two of us. The higher-ups decided a smaller team would be sufficient."
    "I just hope we don't run into Dawn."
    "It's the same routine as last time. We dispatch the guards and enter the warehouse. We split and look for the right box."
    if villain >= 20:
        "This time around I don't kill but only becuase I don't want to antagonise my teammate."
    "Just what is in those boxes that is so important to the higher-ups?"
    "This time around 10 minutes pass before things start to go south."
    show stoneman surprised at leftish with ease
    show bolt surprised onlayer mc
    show shadow neutral at rightish with dissolve
    "Suddenly Shadow appears behind Stoneman and kicks his feet from under him. Stoneman goes down but rolls over and stands up quickly."
    show stoneman angry
    st "I see you've arrived!"
    "I look around to see if I can spot the other Dawn members coming."
    "But it's quiet. Shadow slips into the darkness and reappears a distance away."
    b "Did you come alone today?"
    sh "...yes."
    "Huh. That's surprising."
    "Maybe this is just a diversion then and the others are attacking a Dusk warehouse as we speak? It's happened before."
    show bolt neutral onlayer mc
    b "Stoneman, we should leave quickly."
    st neutralfrown "Not before we complete the mission."
    show shadow angry
    "Stoneman runs up to Shadow and throws a punch, but Shadow blocks him and slips away."
    show stoneman angry
    st "Bolt, don't just stand there! Help me!"
    "Stoneman and Shadow, fighting each other..."
    show bolt sad onlayer mc
    "This is the last situation I wanted to find myself in."
    show bolt neutral onlayer mc
    "I should help Stoneman so that we can complete our mission. But I don't want to fight Shadow..."
    "I don't feel comfortable with the idea anymore and after our arguement... I don't want to worsen our relations."
    show bolt surprised onlayer mc
    "Wait, what am I thinking? Shadow is our enemy. Why did seeing him live a normal life affect me so much?"
    st "Bolt! What are you doing?!"
    "Shadow and Stoneman are fighting but no side is winning. What should I do?"
menu:
    "Look for the package in the meantime":
        $ samuel += 10
        $ ch2choice = "LOOK"
        jump look_ch2
    "Fight Shadow with Stoneman":
        $ bastion += 5
        $ ch2choice = "FIGHT"
        jump fight_ch2
    "Refuse to take action.":
        $ samuel += 10
        $ villain += 5
        $ bastion -= 5
        $ ch2choice = "REFUSE"
        jump refuse_ch2
label look_ch2:
    show bolt neutral onlayer mc
    "I can't force myself to participate in the fight but I'm still on a mission and I need to do my job."
    b "I'll look for the box! Keep him occupied!"
    if bastion < 15:
        st "What?! I gave you a direct order as a leader!"
    else:
        show stoneman surprised
        st "What...? Re- Bolt! Please help!"
        b "...sorry, I can't."
    show shadow neutral
    "Shadow looks at me for a moment with a look in his eyes that I can't decipher. I don't wait to watch the fight."
    show stoneman angry
    "I spend the next few minutes looking for the package, while Stoneman and Shadow fight it out."
    show shadow smirk
    "I can feel Stoneman's anger radiating and Shadow has his characteristic smirk."
    st "What's so funny?!"
    sh "Nothing. Nothing at all."
    hide shadow with dissolve
    show stoneman at center with ease
    "Eventually I find the box, take it and run to the exit. Bastion follows me soon after. He looks very tired and pissed."
    show bolt sad onlayer mc
    b "Stoneman..."
    if bastion < 15:
        jump ch2_s5
    else:
        jump ch2_s5_b1

label fight_ch2:
    show bolt neutral onlayer mc
    "Forget my weird feelings. I have to help my friend, Stoneman. I will figure out my emotions later."
    show shadow sad
    "I join the fight and together Stoneman and I quickly overpower Shadow."
    "I see the disappointment on Shadow's face. It hurts to see him this way."
    show bolt sad onlayer mc
    "I don't know what to think anymore. We are enemies. I'm doing my job. It should feel right but it just doesn't."
    hide shadow with dissolve
    show stoneman neutralfrown at center with ease
    "Eventually Shadow retreats and we find the package."
    show bolt happy onlayer mc
    b "Good job today, Stoneman."
    "I smile at Stoneman, but he looks... troubled."
    show bolt neutral onlayer mc
    b "Why are you..."
    if bastion < 15:
        jump ch2_s5
    else:
        jump ch2_s5_b1

label refuse_ch2:
    show bolt surprised onlayer mc
    "I can't do anything. I just don't know what I should do. I'm so confused."
    if bastion < 15:
        show stoneman angry
        st "Bolt, for fuck's sake!"
    else:
        show stoneman angry
        st "Tch... just... nevermind! I... I got this!"
    show shadow smirk
    "Shadow has his characteristic smirk on his face. He's pleased with my decision."
    show bolt sad onlayer mc
    "I mean, I'm not fighting the enemy, I'm not doing my job, I feel so stupid. But I can't move."
    hide shadow with dissolve
    show stoneman at center with ease
    "Eventually Stoneman overpowers Shadow and Shadow retreats from the fight. We find the package."
    b "I'm sorry, Stoneman."
    if bastion < 15:
        st "Not now. We'll talk in the compound."
        jump ch2_s5
    else:
        st "Bolt... we'll talk later."
        jump ch2_s5_b1

label ch2_s5:
    scene dusk base
    show frostbite neutral at farleft
    show stoneman angry at center
    show mia neutral at right
    show bolt neutral at side onlayer mc
    with Fade(0.75, 0.5, 0.5)

    if ch2choice == "LOOK":
        st "And she refused to fight Shadow! Disobeyed my order!"
        "The whole Dusk team is gathered in our secret base and Bastion is voicing his displeasure with my actions during the mission."
        show bolt angry onlayer mc
        b "But I still furthered our mission objective. Which was not to fight Dawn but to look for the package!"
    elif ch2choice == "FIGHT":
        st "And she was hesitant to fight Shadow! Almost disobeyed my order!"
        "The whole Dusk team is gathered in our secret base and Bastion is voicing his displeasure with my actions during the mission."
        show bolt angry onlayer mc
        b "But in the end I didn't! I fought him alongside you!"
    else:
        st "And she refused to fight Shadow! Disobeyed my order!"
        "The whole Dusk team is gathered in our secret base and Bastion is voicing his displeasure with my actions during the mission."
        show bolt sad onlayer mc
        b "..."
        st "You won't even say anything to defend yourself?!"

menu:
    "Apologize":
        $ villain -= 5
        show bolt sad onlayer mc
        b "I'm sorry..."
        st "At least you feel guilty about it..."
        jump ch2_s5_2
    "Stay silent":
        $ bastion -= 5
        show bolt neutral onlayer mc
        b "..."
        st "Unbelievable."
        jump ch2_s5_2

label ch2_s5_2:
    show stoneman angry
    st "Still, I gave you my order and you disrespected me!"
    show bolt angry onlayer mc
    b surprised "Ah, so this is about your feelings now?"
    m "Folks, calm down...!"
    st "You mean your feelings! Exactly what is your relationship with Shadow?"
    b "What are you implying?"
    st "Nothing. I can see there's something going between you. Has been for a while."
    st "You just enjoy each other's company too much and avoid fighting."
    b "What?! That's ridiculous! There is nothing between us. You're just imagining things!"
    f "Actually, I agree with Stoneman. The way you behave around Shadow is not normal for enemies..."
    b "Not you too?! Leave me alone! I will feel and do what I want!"
    hide stoneman
    hide frostbite
    hide mia
    with dissolve
    "Angry, I stomp out of the room, slamming the door behind me."
    "What is with them?! There is nothing special between me and Shadow..."
    jump ch2_s6

label ch2_s5_b1:
    scene dusk base
    show frostbite neutral at farleft
    show mia neutral at right
    show stoneman sad at center
    show bolt sad at side onlayer mc
    with Fade(0.75, 0.5, 0.5)

    if ch2choice == "LOOK":
        st "I'm just... trying to understand. I needed your help, Bolt. And instead, you just..."
        "The whole Dusk team is gathered in our secret base, and Bastion is quietly voicing his displeasure over my actions during the mission."
        b "I furthered our mission objective, didn't I? We were looking for a package, not fighting Dawn!"
    elif ch2choice == "FIGHT":
        st "Bolt, you... I noticed that you hesitated."
        "The whole Dusk team is gathered in our secret base, and Bastion is quietly voicing his displeasure over my actions during the mission."
        b "..."
    else:
        st "Bolt, I needed your help! What happened?"
        "The whole Dusk team is gathered in our secret base, and Bastion is quietly voicing his displeasure over my actions during the mission."
        b "..."

menu:
    "Apologize":
        $ villain -= 5
        b "I'm sorry..."
        st "...I'm just... trying to understand. That's all."
        jump ch2_s5_b2
    "Stay silent":
        $ bastion -= 5
        show bolt neutral onlayer mc
        b "..."
        st "Bolt, we're a team. I need to be sure that we're on the same side. I need to completely understand where your head's at..."
        jump ch2_s5_b2

label ch2_s5_b2:
    show stoneman neutralfrown
    st "All that being said, I have to ask..."
    st "Bolt, what's your relationship with Shadow?"
    show bolt neutral onlayer mc
    "My eye twitches."
    show bolt angry onlayer mc
    show mia surprised
    show frostbite surprised
    show stoneman surprised
    b "Just {i}what{/i} exactly are you implying?"
    m "Uh oh."
    show mia neutral
    show frostbite neutral
    st "No! It's just... I noticed that the two of you have been talking it up and avoiding conflict with each other!"
    show stoneman neutralfrown
    st "Remember: we're {i}enemies{/i}. If there's anything between the two of you... we, your teammates, should know."
    b "What?! That's ridiculous! There's nothing between us. You're just imagining things!"
    f "Actually, I agree with Stoneman. The way you behave around Shadow is not normal for enemies..."
    b "Not you too?! Leave me alone! I will feel and do what I want!"
    hide stoneman
    hide frostbite
    hide mia
    with dissolve
    "Angry, I stomp out of the room, slamming the door behind me."
    "What is with them?! There's nothing special between me and Shadow..."
    jump ch2_s6

label ch2_s6:
    scene park night
    hide bolt onlayer mc
    show rene neutral at side onlayer mc
    with Fade(0.75, 0.5, 0.5)
    "I need some fresh air so on my way back home I take the longer route through the park. The main alleys are well-lit."
    "It's well past 3 am, so there's nobody here... or so I thought but now I hear singing."
    show samuel sad at center with dissolve
    s "*lyrics*"
    show rene surprised onlayer mc
    "It's a sad song about loss and loneliness. And I recognise the voice. It's Shadow... Samuel singing."
    show rene sad onlayer mc
    "I feel like this song suits him more than the one we sang at his class... but..."
    "That's not a very nice thought, is it? That loneliness and sadness suit someone."
    s "*lyrics*"
    "Come to think of it, he always has this aura of melancholy around him. It feels as if he cannot allow himself to be happy."
    show rene sad onlayer mc
    r "*lyrics*"
    show samuel neutral
    "I know the song so I join in. I... really think Samuel needs a friend. He notices my presence and smiles a sad smile."

menu:
    "Admit that you want to become closer to Samuel":
        $ samuel += 5
        $ villain += 5
        "And I... yes, I would like to be his friend. Not his enemy or a stranger..."
        show rene neutral onlayer mc
        "I cannot deny that I've always felt a sense of connection with him and I want to pursue it."
        jump ch2_s7
    "Samuel is your enemy. It's not appropriate to befriend him.":
        "No, this is wrong! Samuel is my enemy, why would I try to be closer to him? So what if I feel a connection to him?"
        "I should squash those feelings while I still can, not pursue them."
        "I finish the song."
        "Not giving Samuel the chance to say anything, I phase out and then start walking quickly in the direction of home."
        show rene neutral onlayer mc
        "I will not be confused anymore."
        jump ch3_s1_1

label ch2_s7:
    show samuel smirk
    s "...thank you... for joining me."
    show rene happy onlayer mc
    r "No problem. I hope my butting in didn't destroy your mood."
    show samuel surprised
    s "What? No! I like singing with others. Especially if they sing well."
    r "Thank you for saying that. From a professional, that means a lot."
    show samuel smirk
    s "Where did you learn to sing?"
    r "I did church choir as a kid. Other than the basics I picked up there, I'm self-taught."
    show samuel neutral
    s "I see... Can I ask you something, why didn't you pursue it professionally? You have a good voice and you like it... right?"
    show rene surprised onlayer mc
    r "I... never thought I was good enough to do it for a living... I guess I lacked the confidence to do it?"
    show samuel smirk
    s "Lack confidence? You? Really?"
    show rene happy onlayer mc
    "I laugh at that."
    r "Even I have moments where I don't believe in myself. Despite how I act, I don't believe I'm invincible."
    s "I believe I've been deceived."
    r "I’m sorry to hurt you. Besides the fact that I never thought I could sing professionally, I also really like numbers."
    r "I’m happy with my choice of major and excited to graduate and work using my skills."
    show samuel neutral
    s "Your major is something related to numbers?"
    r "Economics."
    show samuel smirk
    s "Huh... so you {i}are{/i} smarter than I thought..."
    show rene angry onlayer mc
    r "Hey!"
    show samuel happy
    s "Confident, beautiful, smart, and has a good singing voice... what can you not do... Rene?"
    show rene surprised onlayer mc
    "Wait... he thinks so highly of me... more importantly \"beautiful\"? Does that not count as flirting?"
menu:
    "Flirt back":
        $ samuel += 5
        jump flirt_ch2
    "Ignore that part":
        jump ignore_ch2

label flirt_ch2:
    show rene happy onlayer mc
    r "You're not so bad yourself, handsome!"
    show samuel smirk
    s "I see... so you like my looks."
    r "Well, I like your singing voice too and I like how being around you brings out my competitive side."
    r "Be it an argument or a fight, I'm never bored."
    s "I get where you're coming from. I feel the same."
    show rene surprised onlayer mc
    "Oh..."
    "I meant- I... wanted to be friends... I didn't uh-"
    "Time for a strategic retreat. Let's change the subject!"
    show rene sad onlayer mc
    r "On the topic of our bickering, I'm sorry about what I said that day in my room."
    jump ch2_s7_2

label ignore_ch2:
    show rene neutral onlayer mc
    "I want to be friends with Samuel so it's better if I don't acknowledge that part."
    "Besides he could have just meant he finds me aesthetically pleasing. Don't jump to conclusions, Rene!"
    "I should just change the subject."
    show rene sad onlayer mc
    r "There's something I wanted to talk about. I need to apologise for what I said that day in my room."
    jump ch2_s7_2

label ch2_s7_2:
    show samuel neutral
    s "...hm? No offense was taken. It's your choice how you take on the words of others and how you feel."
    r "But I accused you of having ulterior motives... while you were just worried about me, weren't you?"
    s "I was."
    r "But if you were not angry about that day, why did you lash out at me in the classroom?"
    if hide_identity:
        s "Because you lied to me about your identity."
        show rene neutral onlayer mc
        r "No. It was even before that!"
    s "...well..."
    show rene neutral onlayer mc
    "I see he's uncomfortable. Should I push for an answer?"

menu:
    "Wait for his answer. You need know.":
        $ samuel += 5
        "I really need to know what that was all about. Otherwise I don't feel like we can move on and improve our relationship."
        r "I'm waiting."
        jump ch2_s7_3
    "Drop the subject.":
        "I won't push for an answer if he doesn't want to give one."
        show rene happy onlayer mc
        r "Don't worry about it, Samuel. You don't have to tell me if you don't want to."
        show samuel neutral
        s "I'm just worried about how you would take my answer. But I'll give it to you. You deserve it."
        jump ch2_s7_3

label ch2_s7_3:
    show samuel neutral
    s "...Uh well, I was scared about how that would change our relationship."
    s " Knowing each other in real life... talking normally... singing together..."
    show rene surprised onlayer mc
    r "Ah, so we're worried about the same thing."
    show rene sad onlayer mc
    r "We're supposed to be enemies... a hero and a villain..."
    s "A hero and a villain? Which is which though?"
    show rene surprised onlayer mc
    r "That's-"
    s "Not as obvious as you think it is. You are as much a villain to me as I am to you."
    s "I would not work for Dawn if I didn't think it was the right side..."
    r "I didn't think-"
    s "You thought I was evil, did you not? Guess what - there are very few truly evil people in the world."
    s "But I guess I might as well be, isn't it that most evil people believe they’re in the right too."
    show samuel smirk
    s "It's up to you to decide how you see me."
    s "I'd just ask you to judge me based on my actions, not based off of any ideas others put in your pretty little head."
    "There is so much truth to what he is saying. I always believed Dusk and Dawn are polar opposites, pure good and pure evil…"
    show rene sad onlayer mc
    "But what if I was wrong?"
    "Even if the organisations are right and wrong, the people can have their own set of morals."
    if bastion >= 15:
        "If I told Bastion... I wonder how it would change his outlook."
    show rene neutral onlayer mc
    r "Why did you join Dawn in the first place?"
    show samuel neutral
    s "I... honestly? I need the money for something. They offered a good sum."
    r "Ahh, I see. So it's not about saving the world for you?"
    show samuel smirk
    s "I don't have such dreams, no. My dream is to be recognised for my singing. This is just a job for me."
menu:
    "Ask why he needed the money":
        $ samuel += 5
        jump ask_ch2
    "This is too private to ask. Don't.":
        "This is way too private to ask. I don't know him well enough to pry into his life like that."
        jump ch2_s7_4

label ask_ch2:
    "I need to know more about him. It's a bit of a private subject but he can always refuse to answer if he doesn't want to."
    r "If I may ask... why'd you need money so badly?"
    show samuel sad
    s "Well... I'm the only one who takes care of my brother."
    s "He's sick. I need money for his treatment and enough for us to be able to live somewhat comfortably..."
    s "I still wanted to pursue music and this was the only way I saw it could be possible."
    show rene surprised onlayer mc
    r "Ahh...I'm sorry for prying into your private life!"
    show samuel neutral
    s "Don't worry about it. I wanted to tell you."
    show rene sad onlayer mc
    "This is why he always seem so sad..."
    "Taking care of a sick loved one must be hard, especially if you are as young as we are and studying while also being supers."
    show rene happy onlayer mc
    r "You're a strong person."
    s "I'm not."
    r "You are! I really believe that!"
    show samuel smirk
    s "...thank you."
    jump ch2_s7_4

label ch2_s7_4:
    show rene happy onlayer mc
    show samuel smirk
    "We talk a bit more about our daily lives. Eventually I yawn. It's late and I'm tired."
    "We have a day off college tomorrow but it would still be good to go to sleep before morning comes."
    "We say our goodbyes and part ways. I feel giddy thanks to talking to him. I really enjoyed our time together."
    jump ch3_s1_1
