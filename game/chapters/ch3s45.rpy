label ch3_s4_1:
    scene dusk base
    hide rene onlayer mc
    show bolt neutral at side onlayer mc
    show shadow neutral at center
    show mia sad at offscreenleft behind frostbite
    show frostbite annoyed at offscreenleft
    show stoneman neutralfrown at offscreenleft
    with Fade(0.75, 0.5, 0.5)

    "I entered through the doors of our base, Samuel wasn't too far behind. He kept a careful distance behind me."
    "The lights were on, so at least I knew someone was there."
    b "Hey, team?"
    "I call out."
    "..."
    sh "Hm... do you think they made it?"
    show bolt angry onlayer mc
    "Of course they did! Hey, gu--"

    if bastion <= 15:
        jump ch3_s4_shadow
    else:
        jump ch3_s4_bastion

label ch3_s4_shadow:
    play sound "<from 1.0>door-slam.mp3" volume 0.5
    show frostbite annoyed at leftish
    show mia sad at left behind frostbite
    show stoneman neutralfrown at center
    show shadow surprised at farright
    with ease
    show bolt surprised onlayer mc
    "All of a sudden, I hear the door shut behind us. I turn my back against Samuel to see--"
    st "Well well well, I was wondering."
    show bolt neutral onlayer mc
    show shadow neutral
    b "Bastion..."
    show stoneman angry
    st "I see you're with your new friend... should I give you two a moment?"
    show bolt sad onlayer mc
    b "Bastion, please, listen..."
    "I see Bastion's fist turn to stone."
    "Samuel presses his back against mine, and I avert my eyes for a second to see that Alicia was facing him frost forming at her fingertips."
    "And there's poor Mia behind her... she looks frightened."
    st "No, don't! I'm afraid I've already heard enough! I already understand what's happened!"
    b "Bastion!"
    st "You've abandoned all your morals! All your heroic virtues for... for this scoundrel!"
    st "You've killed! Abandoned your duty! All for what?"
    st "{i}Him?!{/i}"
    show bolt crying onlayer mc
    "I don't know what to say. Bastion's words hurt. As I'm choking on my words, Samuel walks in front of me."
    sh "Bastion."
    st "Shadow."
    sh "Please... listen to what we have to say. We're not here to harm you, I swear."
    f angry "And why should we listen to the words of a villain?"
    sh "It's funny you say that, actually. Heroes, Villains..."
    sh "There's none of that here now. It's us and them."
    show frostbite annoyed
    m surprised "Wait... what does that mean?"
    st "Explain yourselves while you have the chance."
    show bolt neutral onlayer mc
    "Samuel and I look at each other, and nod."
    "I start..."
    jump ch3_s5_1

label ch3_s4_bastion:
    "In that moment, I sense a presence, and whirl around immediately to see..."
    show mia surprised at left
    show frostbite surprised at leftish
    show stoneman surprised at center
    show shadow neutral at right
    with ease
    show bolt surprised onlayer mc
    st "Rene!"
    b "Bastion!"
    show stoneman happy
    show bolt happy onlayer mc
    "I run towards him and envelop him in an embrace. He hugs me back... though I don't realize just how tight he's hugging me."
    show bolt shy onlayer mc
    show frostbite happy
    show mia happy
    b "Ahhhhck... Bastiooon..."
    show stoneman surprised
    st "Oh! Oops! Sorry, I..."
    sh "Ahem."
    show stoneman neutralsmile
    show bolt neutral onlayer mc
    "Bastion let's me go, rubbing the back of his head out of embarrassment."
    "I turn around to see Samuel staring at us. Behind him was Alicia, arms sternly crossed over her chest."
    "And there was Mia next to her, sticking close to her."
    f "Good to see you back, Bolt."
    m "I'm glad to see you're back. After you disappeared at the warehouse, I..."
    show stoneman happy
    st "I told you. I told you she was going to be okay."
    "All of their heads immediately turn to Samuel."
    sh "... we have a lot to talk about, so you might want to sit down."
    "Samuel and I look at each other, and nod."
    "I start..."
    jump ch3_s5_1

label ch3_s5_1:
    scene dusk base
    show mia surprised at left
    show frostbite surprised at leftish
    show stoneman surprised at center
    show bolt neutral onlayer mc
    show shadow neutral at right
    with Fade(0.25, 0.5, 0.25)

    "..."
    "We explain everything. From why we kept fighting each other, to the existence of Daylight."
    show stoneman sad
    "As Samuel and I take turns explaining everything we heard from Aunt Matilda, looks of concern slowly spread on everyone's face."
    "But most of all, Bastion."
    show mia sad
    show frostbite sad
    "As we finish our explanation, a silence hangs over the room. And, all of a sudden, Bastion sinks to his knees."
    st "Rene, I..."
    if bastion < 15:
        jump ch3_s5_2
    else:
        jump ch3_s5_3

label ch3_s5_2:
    st "I'm sorry. I'm so sorry..."
    b "Bastion..."
    st "All this time, I've just kept pushing you. Encouraging you to make sacrifice after sacrifice."
    st "I'm... an idiot. I should've known. And even after pushing you, the way I treated you after everything..."
    show stoneman angry
    st "How could I not see all of the pressure I was putting on you?!"
    st "All of the harm it was doing? And not only to you, but to all of us..."
menu:
    "Apology accepted":
        b "Apology accepted."
        show stoneman sad
        "Finally... it was so satisfying hearing him apologize after everything he's put me through."
        show shadow smirk
        sh "Heh."
        st "How do I make it up to you?"
        "I walk up to Bastion and pull him to his feet."
        b "If you're going to be a damn leader, we're going to need you on your feet. We still have a lot to do."
        b "So, make it up to me by helping us take out Daylight, yeah?"
        show stoneman neutralfrown
        st "..."
        jump ch3_s5_4
    "It's not your fault":
        show bolt sad onlayer mc
        b "It's not your fault, Bastion."
        show stoneman surprised
        st "Huh?"
        show bolt neutral onlayer mc
        b "How could you have known about what they were doing? They fooled all of us. Don't beat yourself up over it."
        show stoneman sad
        st "But... what if any of you died?"
        b "Well, none of us did. Because in the end, we have a good leader, and that's what counts."
        b "Now, are you going to continue moping, or are you going to help us out?"
        show stoneman neutralfrown
        st "..."
        jump ch3_s5_4

label ch3_s5_3:
    show stoneman sad
    st "I've failed you..."
    show bolt surprised onlayer mc
    b "Bastion?"
    st "I kept pushing you... I encouraged you for being self-sacrificing over... over what?"
    show bolt sad onlayer mc
    st angry "Taking away supplies that would've been gifted to the needy? I thought we were the heroes!"
    st sad "I couldn't stop thinking about it the next day. About why they kept pushing us... if only I figured it out sooner."
    st "All the pressure I put on you, all the harm I've done... I could've stopped all of that, Rene!"
    st "If I lost you... I..."
    b "..."
menu:
    "Hug him":
        $ bastion += 5
        show bolt neutral onlayer mc
        "I sink down to his level, and take him in a hug."
        "In front of the team and Samuel, we share a quiet moment together."
        st "... I don't know what I would do, Rene."
        show bolt happy onlayer mc
        b "Then don't lose me, knucklehead. I'm hard to miss."
        "I place my forehead against his, and smile. It was time for me to pay my debt."
        "It was time for him to borrow my confidence."
        show stoneman shy with dissolve
        "His deep frown slowly curls into a smile. That damn, goofy smile."
        st "I like you, Rene. I..."
        st happy "I want to protect you."
        show bolt surprised onlayer mc
        b "E-Eh?"
        "Where did this dork get this confidence from all of a sudden?! Oh gosh, did I give him too much of my confidence?"
        show bolt shy onlayer mc
        show mia happy
        show frostbite happy
        "I can feel my cheeks starting to flare up, and-- and he's laughing at me?!"
        jump ch3_s5_4
    "Help him up":
        "I walk up to him and offer a hand. He slowly looks up to me with a small shimmer in his eyes."
        show bolt happy onlayer mc
        b "Come on, Stoneman. You can't lead all of us from down there."
        "I don't wait for him to take my hand-- instead, I reach down and take his, lifting him up to his feet."
        "I try to pull my hand away, but he holds onto it. He squeezes it with a gentleness I've never felt from him before."
        st "... I don't know what I would do if I lost you Rene."
        "In response, I just chuckle."
        b "It's kinda hard to lose me, you dork."
        show stoneman shy with dissolve
        "His frown was already curling into that smile. That damn, goofy smile."
        st "I like you, Rene. I..."
        st happy "I want to protect you."
        show bolt surprised onlayer mc
        b "E-Eh?"
        "Where did this dork get this confidence from all of a sudden?! Oh gosh, did I give him too much of my confidence?"
        show bolt shy onlayer mc
        show mia happy
        show frostbite happy
        "I can feel my cheeks starting to flare up, and-- and he's laughing at me?!"
        jump ch3_s5_4

label ch3_s5_4:
    show shadow neutral
    sh "If I can cut in here...what's everyone thinking?"
    show bolt neutral onlayer mc
    show stoneman neutralfrown
    show frostbite annoyed
    show mia neutral
    f "It all just sounds so insane. Who told you this again? Your aunt?"
    b "Yes... she had a leading role in Daylight, but left. She's a super, and she can tell if others are supers too."
    f "Huh. Just seems a little... convenient, is all."
    b "I know it all sounds {i}insane{/i} but... Aunty wouldn't lie to me."
    m "It'd be quite the thing to lie about... the better question is, what do we do with this information?"
    m "If everything she says is true..."
    f "Then we have quite the opponent ahead of us."
    b "That's why me and Samuel are gathering everyone together."
    b "Aunt Matilda's place should be safe from the supervision of Daylight. We should actually get there as soon as possible."
    show bolt happy onlayer mc
    b "We could talk to her and really pin down a plan of attack!"
    show bolt neutral onlayer mc
    f angry "{i}What{/i} plan of attack?! It's obvious that we've just been pawns for them. Do you really think we stand a chance?!"
    "Bastion steps up between everyone. He has a brave look on his face."
    st neutralsmile "Daylight has benefited from our struggles. And now they're planning to use it to take over the world."
    st "All this time, we've been playing into their hands. Now... it's our chance."
    m surprised "Our chance to do what?"
    st "To be heroes."
    show frostbite neutral
    show shadow smirk
    sh "Well, someone lit a fire under this guy.."
    st "I'm willing to put my all into stopping Daylight. It's the least I could do."
    f annoyed "{i}sigh{/i} ... I still think the odds are stacked against us."
    m neutral "Uhm... if I could make a suggestion..."
    st "Hm? What is it, Mia?"
    show shadow surprised
    show frostbite surprised
    show stoneman surprised
    show bolt surprised onlayer mc
    m "What if we told Magno and Snapshot about this?"
    f angry "Those complete psychos?! Uh-uh, no way."
    show shadow angry
    sh "Hey, they're just as much heroes as you are..."
    show shadow neutral
    show stoneman neutralfrown
    show bolt sad onlayer mc
    sh "Which, in hindsight, isn't really saying much."
    f "I really can't believe you're calling someone like {i}Magno{/i} a hero..."
    show bolt neutral onlayer mc
    m "We can't deny that they're very powerful. They would be great to have on our side."
    m "And... I don't think it's a stretch to get them to fight Daylight. They've been used too, after all."
    "We all look to Samuel."
    sh "... it's a risk."
    show bolt happy onlayer mc
    b "The more, the merrier, right?"
    show bolt neutral onlayer mc
    sh "Keep in mind, there's a chance of them trying to {i}lessen{/i} our numbers."
    sh "I mean, yes. They'd be great to have on our side, but Aiden and Levina are... passionate people."
    f surprised "Magno's name is {i}Aiden{/i}?"
    m happy "... Levina's a very pretty name..."
    show frostbite neutral
    show mia neutral
    sh "Yeah, if you want to get whipped and shot at, feel free to tell them that."
    st neutralsmile "Well, we have to try, no? Their powers would be invaluable."
    f "I wonder... how would we even go about... talking to them?"
    "We all look at Samuel. Again."
    sh sad "{i}sigh{/i}... I can set up a meeting and ask for a cease fire. If any of you  pray - pray that they'll honor it."
    show shadow neutral
    "Samuel takes a moment to text on his phone. Mia tries to sneak a look, but shrinks away once she's spotted."
    b "What's the verdict?"
    show mia happy
    sh "... they'll meet us at Dawn's Warehouse."
    st "Alright! We should hurry. The quicker we get everyone to Rene's Aunt's place, the quicker we can plan."
    f annoyed "Why do I have a bad feeling about this...?"
    m happy "Don't worry everyone. Even though I don't have any powers... I'll see this through to the end with all of you!"
    show bolt happy onlayer mc
    b "Mia!"
    st "And team... let's be careful out there, yeah? No unnecessary sacrifices."
    st "That includes you, Samuel."
    show shadow smirk
    sh "Feh... like I'd do that for any of you."
    show shadow neutral
    show bolt happy onlayer mc
    sh "Enough talk. Let's mosey."
    f surprised "... let's {i}mosey{/i}? Did he really just say that?"
    "With my team now on board, we head over to the Dawn warehouse to see if we can complete the unity of Dusk and Dawn."
    show bolt neutral onlayer mc
    "... I hope it goes well."
    jump ch4_s1_1
