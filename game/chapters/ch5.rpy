label endings:
    scene college classroom day with Fade(0.75, 0.5, 0.75)
    "Overtime, we slowly assimilated ourselves back to everyday life."
    "We all went back to school, but the topic of heroism became a touchy one."

    if murder and villain > 10:
        "Everyone had a lot of time to reflect. And that made it awkward between me and my former team..."
        "I'm guessing it's because I killed those guards."
    if bastion > 15:
        "No matter what though, we all made continued efforts to keep being friends with each other."
        "We met everyday, kept involved in each other's lives..."
        "But it all still {i}feels{/i} so different. So awkward that we won't talk about such a big part of our lives."

    "Anyway, I've been doing a lot of reflection myself. I've been thinking about if I want to continue bringing the fight to Daylight."
    "I feel like it's something I need to decide now. It's taking up so much space in my head that I get distracted during economics."
    "And... I need to figure out if I want to do it alone."
    "Not just the \"being a hero\" thing... everything else."
    "So much has happened. I've grown closer with a lot of people. People who I think I might want to share my life with."
    "I've been standing here for a good bit now, looking at my phone."
    "The name of the person I trust the most was sitting there, one tap away from what could potentially be the biggest change of our lives."

menu:
    "No. I shouldn't":
        jump rene_end
    "Let's meet":
        "I don't want to be alone in this."
        "After what feels like forever, I pound the message I want to send into my phone."
        "{i}\"Can we meet on the bridge?\"{/i}"
        if samuel > bastion:
            jump shadow_end
        else:
            jump bastion_end

# RENE ENDINGS
label rene_end:
    "I can't be so selfish. Especially now of all times..."
    "I need to make that decision for myself, no one else should be a factor into it."

    scene bridge with Fade(0.75, 0.5, 0.5)
    show rene neutral at center
    "There is something relaxing about looking out into the big blue."
    "The gentle tinge of saltwater teasing my nostrils does a lot to relax my nerves."
    "A nice cool breeze, pure silence..."
    "The perfect place to make a big decision."
    r "Deep breath, Rene."
    "In... and out."
    "..."
    "What do I want?"

menu:
    "I want to live peacefully":
        jump rene_peace
    "I have to be responsible":
        jump rene_fight

label rene_peace:
    "Why throw away everything I have? Good school, good friends..."
    "A life where the only thing I have to fight is taxes."
    "I've done my duty. Others will continue the fight for me. I'm not going to make a difference either way if I keep it up."
    "So instead of doing that, I'm going to make the only choice that really, truly matters."
    "..."
    "Hm... Aunt Matilda's casserole the other day was pretty great. I should learn how to make that."
    "The store isn't too far away. I'll stop by on the way home."
    "I should probably study too. Been a little distracted in class recently."
    "Yes, that sounds like a plan. A hot meal, a hot bath..."
    show rene happy
    "And a well deserved rest."
    scene black with Fade(0.75, 0.5, 0.75)
    "GOOD END 2: THE SIMPLER THINGS"
    return

label rene_fight:
    "I started it. It would be irresponsible for me to just abandon everything."
    "Besides, would Daylight actually let me lead a peaceful life? I better strike first."
    "And besides, it's not like I have to do it alone."
    "Mia's been telling everyone who matters about Daylight. Surely, I'll make some new friends down the road."
    "Fighting across the country... finishing what I started... it only feels right."
    if villain <= 15:
        jump rene_hero

menu:
    "And we'll do it the right way":
        jump rene_hero
    "And we'll do it my way.":
        jump rene_vigilante

label rene_hero:
    "I'm a hero. I was made to do this."
    "I've grown out of it recently, but I need to get back into it."
    "I think I'll start by going home, looking in the mirror, and saying..."
    show rene happy
    r "Bolt."
    "Bolt."
    show rene neutral
    "You'll learn to fear that name, Daylight."
    scene black with Fade(0.75, 0.5, 0.75)
    "GOOD END 3: BOLT"
    return

label rene_vigilante:
    "Not only that... but I'll do it my way."
    "No rules, no stupid moral codes. Just results. If anyone dares stand in my way..."
    show rene angry
    "Well, we'll see."
    "You'll learn to fear me, Daylight. Whether I'm Rene, or Bolt..."
    show rene neutral
    "I'm free. And I'm coming for you."
    scene black with Fade(0.75, 0.5, 0.75)
    "GOOD ENDING 4: BOLT, THE VIGILANTE"
    return

# SHADOW ENDINGS
label shadow_end:
    scene bridge with Fade(0.75, 0.5, 0.75)
    show rene neutral at center

    "I watch the clock on my phone intently as it moves past our agreed meeting time."
    "The view here is beautiful but I can't help but feel a {i}little{/i} frustrated."
    show rene angry
    r "Ugh..."
    show rene sad
    r "There's no way he'd forget, right?"
    show rene neutral
    "Almost as if the world was listening, I spot him walking my way."
    show rene neutral at right with move
    show samuel neutral at left with dissolve
    "He waves to me, unaware of the stress he's caused."
    show rene happy
    r "Hey, Sam."
    s "... you're not mad that I'm a minute late, are you?"
    show rene surprised
    "Crap. He could really tell?"
    show rene neutral
    s "Relax these, will you?"
    "He points at his own eyebrows."
    show samuel happy
    s "You'd be surprised how much they give away."
    "In a panic, I cover my eyebrows, which only seems to {i}amuse{/i} him."
    show rene angry
    r "Ugh, nevermind!"
    s "Alright, alright. I'm done, I'm done."
    "You don't {i}look{/i} done with that... smile on your face!"
    show rene neutral
    show samuel neutral
    "The two of us lean on the railing against the bridge, looking out towards the vast blue ahead of us."
    "It's nice sharing this with someone else."
    s "The view is beautiful..."
    r "... no, don't. Let me guess--"
    show samuel happy
    s "... like you."
    show rene happy
    r "Oh, couldn't see {i}that{/i} coming!"
    "Okay, I didn't mind the cheesy flirting as much now."
    r "Sam Sam Sam... you're gonna have to find much better ways to surprise m- mph!"
    "I guess, in that moment, Samuel decided to surprise me."
    show rene surprised
    "He pounces, stealing my lips away, his pressed against mine."
    show rene happy
    "Samuel was so hot against me, I felt myself melting into him, becoming one with him."
    "We've harmonized before, but not like this."
    "He puts his hands on the sides of my face to hold me where he wants me."
    "Once he's sure I'm not going to go away, his hands move up my face and he begins to twirl my locks."
    "Caught in the moment, I forget everything else, even my own name."
    s "How's that?"
    "He lets me breathe a moment."
    r "... eh, it was... alright? I'd give it a seven out of ten at best."
    "My words make him hungry, but he relents."
    "We spend some time with each other on the bridge. Just the two of us."
    "I can tell he was just waiting for me to get past all of this cheap fluff. He knew there was something more pressing on my mind."
    "I mean, why did I choose someplace dramatic like a bridge on some random afternoon?"
    "The sun's setting, as though the world's telling me I'm taking too long. This is it, now or never."
    "I take a deep breath. Samuel takes that as a sign and stands straight up, ready to receive me."
    "I need to choose my words carefully..."
menu:
    "Let's live together. As us.":
        # GOOD END 5: OUT OF THE SHADOWS
        jump shadow_date
    "Let's work together. As heroes.":
        # GOOD END 6: WHAT MATTERS TO US"
        jump shadow_work

label shadow_date:
    show rene neutral
    r "Samuel, you can say that a lot's happened between us."
    show samuel neutral
    s "Oh yeah? I... {i}guess{/i} you could say that, huh?"
    "Sarcastic jerk."
    r "I just want to ask..."
    show rene happy
    r "Do you want to date?"
    show samuel happy
    "He smiles, and gives his answer in the form of taking my hands."
    s "Of course."
    "My heart's fluttering in my chest, I'm so happy to hear him say it. Our complete acceptance of each other."
    "I lean in and touch foreheads with him."
    s "I'll let you pick the first date spot."
    r "How about dinner at my place?"
    s "Oh, spicy."
    r "The {i}dinner{/i} will be."
    show samuel neutral
    s "... actually, can I take you somewhere?"
    show rene surprised
    r "I thought you wanted {i}me{/i} to pick the spot?"
    s "Yeah, for the date. This isn't a date. I want you to meet someone close to me."
    show samuel happy
    s "My little brother. If we're going to be together... well, me and my brother are a package deal."
    s "You have to take care of him too, you know."
    show rene happy
    r "Ha, you sound like that's going to be a deal breaker for me! Take me to meet the little squirt."
    "With that said and done..."
    "I follow Samuel."
    scene black with Fade(0.75, 0.5, 0.75)
    "GOOD END 5: OUT OF THE SHADOWS"
    return

label shadow_work:
    show rene neutral
    r "Samuel... there's a lot out there that needs to be done."
    show samuel neutral
    s "I... guess you can say that."
    r "Daylight's still out there. I mean, you and I,  we started all of this. Shouldn't we be the ones to-"
    show samuel sad
    s "I can't."
    show rene surprised
    r "Huh?!"
    "He answered so {i}quickly{/i} and confidently."
    s "Remember? I have a brother who needs me."
    show samuel neutral
    s "What kind of person would I be if I abandoned my sick brother to go fight a bunch of old people across the country?"
    show rene neutral
    "He's right. His brother is the most important person in the world to him. Why didn't I think of that?"
    "Did I ruin everything?"
    s "I know you've been thinking really hard on it. Everything's been a blur for the past few days for you, huh?"
    s "Can I offer you an alternative?"
    show rene surprised
    r "An alternative?"
    show samuel happy
    s "I'm always down to do some good. But I'd like to do it my way."
    s "You want to team up with me, right? But instead of dealing with all of that Daylight nonsense, how about we do something more... worthy?"
    r "Worthy?"
    show samuel neutral
    s "... let's stick to our community. Let's commit to a place that matters to us- that we can actually make an impact."
    show samuel happy
    s "All of the people we care about are here. Why go anywhere else? Let's be the protectors of this place."
    "I... found nothing wrong with what he was saying."
    show rene neutral
    "Leave the hero stuff to the big heroes. Why should we feel responsible?"
    show rene happy
    "Just stick close..."
    show samuel surprised
    s "Mmmph...! Hey! You can't steal my moves!"
    r "Hmhm!"
    "... to what matters."
    scene black with Fade(0.75, 0.5, 0.75)
    "GOOD END 6: WHAT MATTERS TO US"
    return

label bastion_end:
    scene bridge with Fade(0.75, 0.5, 0.75)
    show rene neutral at center

    "It's ten minutes before our agreed meetup time. I kept trying to run the script in my head, but I just can't nail anything down...!"
    "Gah, {i}this{/i} is why theatre students have my complete, utter respect."
    "Ten minutes. Just ten minutes left to get the courage to ask the questions I want to ask. That should be plenty of time to-"
    show rene surprised
    r "Oh no!"
    "The world could've told me \"I hate you\" in literally any other way. It could've blown up the sun or- or put me in some prank show!"
    "But {i}no{/i}. There he was. Walking towards me."
    show rene neutral
    "Maybe he hasn't seen me yet. Maybe I could still hide-"
    show rene neutral at right with move
    show bastion happy at left with dissolve
    ba "Rene!"
    "{i}Rene, you fool.{/i}"
    show rene happy
    r "Hello, Bastion! H-How are you?"
    show bastion neutral
    ba "I'm... fine?"
    "Oh no. He sees through my flimsy disguise."
    show rene shy
    r "And... How about you? Are you okay? I mean, good? I mean, of course you're both of them, I meant as in, like..."
    show bastion happy
    ba "This is a gorgeous view."
    "He's looking away from my stammering, taking in the beautiful view of the vast blue before us."
    show rene happy
    "At that moment, I remember who I'm with."
    "And I've never felt so calm so fast."
    "We speak at length. About... well, anything and everything that passes our minds."
    "He talked to me about a start up charity that wants to supply games and toys to therapy facilities and hospitals."
    "I talked about the high score I got in a rhythm game the other day."
    "No matter where our minds wander, the other follows it. I feel like we could talk forever."
    "That, combined with the beautiful view of the ocean... it's like we're in a constant state of reverie."
    show bastion neutral
    ba "... it feels crazy."
    show rene neutral
    r "What does?"
    ba "We were suiting up and acting like heroes a short time ago."
    ba "Now... I argue that we could convince ourselves that it was all some strange dream."
    show rene sad
    r "... yeah."
    ba "Oh, sorry. I shouldn't have brought that up..."
    r "It's just... I've been thinking alot about you. Ever since that incident with Magno."
    r "Before that, you told me not to risk myself, even for the greater good. And then you jump in between me and Magno..."
    ba "That was..."
    show bastion sad
    ba "Pretty selfish of me, wasn't it?"
    show rene surprised
    "{i}Selfish?{/i}"
    "I remember something. He called himself selfish one time when he was talking about me."
    r "What do you mean by that?"
    show bastion neutral
    ba "... I like you alot, Rene. My feelings for you have been guiding some of the things I've said to you... some of the things I do."
    ba "I didn't want you to put yourself at risk because I didn't want to see you hurt."
    ba "I didn't throw myself in front of Magno for the greater good."
    ba "I did it because I wanted to preserve you. So you could continue being in my future."
    r "..."
    show bastion shy
    ba "I'm sorry if I ever worried you, Rene. I'll go ahead an-"
    show rene neutral
    r "You think you can just say all that mushy stuff and leave? Uh-uh."
    show rene happy
    r "I asked to meet you here so I could ask you a big question. I haven't asked it yet, you dork."
    show bastion surprised
    ba "Oh?"
    show rene neutral
    r "But before that, promise me... no matter what happens between the two of us... from here on out, we give equally to each other."
    show bastion happy
    ba "Haha... I don't see any reason to decline here."
    "There it is."
    "That dorky smile."
    "I watch Bastion as he sorta... fidgets in place. Leaning forward, leaning back."
    r "Are you... okay?"
    show bastion shy
    ba "I... I want to do something, but... I'm afraid it's... quite risky..."
    show rene happy
    r "... here, let me help."
    "I clutch his collar, pull him in-"
    show bastion surprised
    "And plant a kiss right on his lips."
    show bastion shy
    "He makes that cute blushing face he does when he's embarrassed, but he doesn't let me admire it for long."
    "Instead, he's only emboldened by me."
    show bastion happy
    ba "I love you."
    "He says this as he presses his lips against mine, breathing love into my body."
    "Our foreheads touching, I get a fantastic view of his clumsy smile and the glisten in his eyes."
    "It was set."
    r "I love you too."
    r "Equally."
    "{i}Wink.{/i}"
    ba "Rene... I'm glad."
    "It's starting to get dark."
    show rene neutral
    r "Bastion... about the thing I wanted to ask you."
    show bastion neutral
    ba "Yes?"

menu:
    "Let's live together. As us.":
        jump bastion_date
    "Let's work together. As heroes.":
        jump bastion_work

label bastion_date:
    show rene happy
    r "I think I know the answer already, but... how about we start dating?"
    show bastion happy
    ba "Haha... we've already got quite the lead on our future, don't we?"
    ba "I would love nothing more, Rene. Of course."
    "We squeeze each other's hands, reciprocating each other's love and warmth in equal measure."
    "We've overcome so much together. Fought so hard to get where we are."
    "Maybe it's selfish to think that I deserve a reward, but when the reward is me getting to spend the time with the man I adore..."
    "Well, I don't even think about it."
    ba "Are you free now... {i}milady{/i}?"
    r "Hahahahaha! No-- nonononono... I will {i}not{/i} be able to take you seriously if you start saying that."
    ba "Haha, who knows? Maybe you'll get used to it."
    show bastion shy
    ba "... maybe before me..."
    r "Yeah yeah, don't count on it, rockstar..."
    r "But to answer your earlier question... yes, I'm free."
    show bastion happy
    "I'm free now more than ever."
    ba "In that case, shall we head over to my place?"
    r "Lead the way!"
    "With that said and done, Bastion pulls me along..."
    "And I follow his lead."
    scene black with Fade(0.75, 0.5, 0.75)
    "GOOD END 7: A SAFE BASTION"
    return

label bastion_work:
    show rene neutral
    r "I know this might be... a bit too soon, but."
    r "I've been thinking about taking the fight to Daylight."
    show bastion neutral
    r "I know I have the option to leave this all behind, but... don't you think since I started it, it's my responsibility?"
    ba "..."
    ba "You don't have to feel like it's your responsibility, Rene. {i}No one{/i} should feel like saving the world is their responsibility."
    ba "The only reason why you should do it... is because you {i}want{/i} to."
    r "..."
    "Maybe it wasn't the answer I wanted but... maybe it was the answer I needed."
    ba "Is that what you want, Rene?"
    r "... yes. Even if I don't feel responsible, I can't let these people run free and do whatever they want."
    "All this time, I kept convincing myself that I {i}should{/i}."
    "When in reality, it's because my convictions are too strong, too firm to let me sit on the side."
    "I'm a hero through and through."
    "I have someone to thank for that."
    ba "If you're that firm... then I'm coming with you."
    "That throws me for a loop. Is he doing it because he wants to, or because he feels like he has to because we're a couple now?"
    "I felt bad. I didn't want t-"
    ba "And it's because I want to."
    "He places a finger beneath my chin and raises my eyes to meet his. His eyes are filled with undoubtable resolution."
    "When Bastion is sure of something... it's really a sight to behold."
    show rene happy
    r "... let's work together. As heroes."
    show bastion happy
    "A daring smile sprawls across his face."
    ba "Together, Bolt..."
    r "We're unstoppable!"
    "For us, it was another day."
    "For Daylight, the sun was starting to set."
    scene black with Fade(0.75, 0.5, 0.75)
    "GOOD END 8: HEROES AT HEART"
    return
