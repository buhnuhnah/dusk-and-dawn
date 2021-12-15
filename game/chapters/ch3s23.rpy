label ch3_s2:
    scene park night with Fade(0.75, 0.5, 0.5)
    show bolt neutral at rightish
    show shadow neutral at leftish
    "I almost lose consciousness after that but then I no longer hear them behind us. It worked. But... where should we go?"
    "The only safe place I can think of now that is close enough to reach before we collapse is Aunt Matilda's house."
    "I hope Aunty won't ask too many questions when we arrive at her house bearing such wounds."
    "No matter. I will explain everything to her if I must. For now, the important thing is for us to be safe."
    b "We're going to... my Aunt's house... neither Dusk nor Dawn should have the information on where it is..."
    sh "Alright... sounds good..."
    "We are both so tired, we can barely speak. I walk, leaning on Samuel for support."
    scene black with Fade(1.0, 0.0, 0.0)
    am "Oh my God! What happened to you kids!"
    "Aunt Matilda's worried voice is the last thing I hear before I pass out on the floor of her living room."
    jump ch3_s3_1

label ch3_s3_1:
    scene aunt room day with Fade(0.75, 0.5, 0.5)
    show bolt neutral
    "I wake up feeling surprisingly well. I look myself over... my wounds are healed."
    "How much time has passed? I grab some of my clothes I left by Aunt Matilda's in case of a sleepover and go down to the living room."
    hide bolt neutral
    show rene neutral
    with dissolve
    show rene neutral at right with ease
    show shadow neutral at left with dissolve
    am "So you say your name is Samuel?"
    sh "...yes."
    am "Not very talkative, are you?"
    sh "I can't say I trust you."
    show rene happy
    r "You can trust her. She's my best friend."
    sh "She has healing-"
    am "Oh, Rene, you're up!"
    "Aunt Matilda interrupts what Samuel tried to say. But if I heard correctly it was something about healing... hmm..."
    "I sit down next to Samuel."
    show rene neutral
    r "We need to talk."
    am "Oh, sure! I love talking!"
    r "A serious talk is what I mean. I need to come clean with you, Aunty. Samuel and I are-"
    am "Supers."
    show shadow surprised
    show rene surprised
    sh "How did you know?!"
    r "Whoa...!"
    am "Well, where do I even begin..."
    am "First, you barged into my house in a state close to death... in what I can only describe as either superhero outfits or cosplay..."
    am "And then there is the fact that I, as a healer, can read other people's superpower signatures."
    am "So I know you've used your powers recently and what they are..."
    r "A healer?! Then that time I came to you with the wound on my arm..."
    am "That time and several times before, I healed you."
    show shadow neutral
    r "Oh!"
    am "I knew you have superpowers from the first time they manifested-"
    r "And you said nothing?!"
    am "You've never been particularly interested in using them. If I had known you joined a super team, I would have spoken to you earlier."
    am "We are both guilty of hiding information from each other, Rene."
    show rene sad
    r "Yes... I suppose you are right."
    am "So what superhero team did you join?"
    show rene neutral
    r "Dusk."
    am "Oh no... and you, Samuel?"
    sh "I'm Dawn."
    am "And yet here you are, together. I assume something went terribly wrong."
    "I tell her what happened that night."
    am "That's... very unpleasant to say the least."
    sh "How long have we been out of it?"
    am "For two days."
    show rene surprised
    r "Two days?!"
    am "Yes, you were near death when you came here."
    am "Samuel was in a better state but I had to wait several times for my healing power to recharge before I had healed you enough for you to wake up."
    am "Even with your accelerated healing, your bodies wouldn't be able to heal themselves in time before death."
    show rene neutral
    sh "We owe you our lives. Thank you."
    am "You've made a good choice in coming here."
    show rene happy
    r "This was the only safe place I could think of."
    am "I'm happy you consider my home safe."
    am "There's something I wish to tell you about Dusk and Dawn though."
    am "If you feel like you are ready to hear something that will change the way you see the world."
    show rene neutral
    r "That's... quite dramatic. But I'm ready."
    sh "Let's hear it."
    am "When I was younger, I was part of a super team too. It was called Daylight."
    show rene surprised
    r "You were?!"
    am "Yes, I wanted to use my powers to help others. Daylight was a much larger organisation than Dusk and Dawn respectively are."

menu:
    "Be surprised":
        r "Wait... you know Dusk and Dawn?!"
        am "Yes, I do. I was just getting to it. I know you're excited but could you let me speak, Rene?"
        show rene neutral
        r "Oh... I'm sorry."
        jump ch3_s3_2
    "Hold in your reaction and let Aunty speak":
        show rene neutral
        "I'm so curious about this, but I try not to show it. I don't want to interrupt her."
        jump ch3_s3_2

label ch3_s3_2:
    am "At one point Daylight split into two organizations: Dusk and Dawn. Both of those groups believe the other to be the evil one. Is that correct?"
    r "Well, yes, that's what I've been told all the time. That Dawn is evil and we need to save the world from them."
    sh "And we've heard of the ambitions of Dusk."
    sh "That they want to change the world to fit their perception of good and that they won't hesitate to destroy anyone or anything."

menu:
    "Agree with Samuel":
        $ villain += 5
        jump ch3_s3_agree
    "Deny it":
        jump ch3_s3_deny

label ch3_s3_agree:
    r "What you say might be true, Samuel. The team and I suspected something weird was going on."
    if villain >= 20:
        sh "And your actions prove Dusk is not so crystal-clear too."
        am "What actions?"
        show rene happy
        r "Ah... it's nothing important, Aunty!"
        "I kick Samuel in the shin but he just smirks in response."
        "How dare he try to tell my Aunt of all people I killed someone? Last thing I need is for her to hate me."
    jump ch3_s3_3

label ch3_s3_deny:
    show rene angry
    r "That's not true!"
    sh "Your team's actions so far would prove otherwise."
    sh "Do you even know what it is you've been stealing from our warehouses?"
    show rene sad
    r "...No."
    sh "Figured. It was supplies we meant to distribute to the poor of our city."
menu:
    "Believe him":
        $ samuel += 5
        show rene surprised
        r "Oh no! But why would Dusk... want to prevent you from doing good?"
        sh "I don't know. But I'm glad you believe me."
        r "Well... of course I do!"
        show rene neutral
        "We look each other in the eyes in silence."
        jump ch3_s3_3
    "Deny the fact that Dusk would ever do something like that":
        show rene angry
        r "I don't believe you! Dusk would never do something like that!"
        show shadow sad
        sh "After everything you still don't trust me, huh..."
        "He looks so hurt by my words. But how can I believe something so outrageous?"
        show rene neutral
        show shadow neutral
        jump ch3_s3_3

label ch3_s3_3:
    "Aunt Matilda clears her throat."
    am "About that. When Daylight split into Dusk and Dawn it was a decision on the higher-ups' part."
    am "It was not due to infighting. To be precise - infighting is what they wanted to cause."
    am "Each time a member of Dusk fights a member of Dawn while wearing their superhero outfit, you power up a crystal embedded in your clothes."
    am "That crystal transmits this energy to the Daylight Core in Daylight's headquarters."
    am "The leaders want to use this power to take over the city... and later the whole state."
    show rene surprised
    show shadow surprised
    r "What?! They want to take over the world?!"
    am "Eventually, yes."
    sh "So that's why there were so many pointless fights lately."
    show rene neutral
    r "Yes, we noticed that too."
    show shadow neutral
    am "The more you fight, the stronger Daylight becomes."
    b "Could that be why they didn't reign in Magno's murderous intent?"
    am "Probably. You getting beat up so badly has served them well in terms of the amount of power gathered."
    sh "And if they suspected that Rene and I might have noticed something strange about our organisations..."
    am "Then it's not surprising they wanted to get rid of you."
    am "And that they have done it in a way in which they could gain the most from your deaths."
    show rene surprised
    r "Oh my God! That's crazy!"
    am "It is a lot to take in."
    am "One more thing. I had a leadership position at Daylight. I left when they made this decision, not wanting to take part in it."
    am "This house is a sanctuary, protected from their eyes by multiple barriers. Whenever you need a safe haven, you can come here."
    show rene happy
    r "Thank you, Aunty."
    show shadow happy
    sh "Yes, thank you, Matilda."
    am "Oh my... all I ever wanted is to help people... now I can again, I'm so happy! Don't worry about anything!"
    "She looks dazzled by Samuel's smile. Funny."

    if samuel >= 20:
        "So I'm not the only one attracted to that smile. It must run in the family."
        "I chuckle and they both look at me strangely."
        sh "What's so funny?"
        b "Nothing! Nothing at all~!"
        sh "Well, I'm glad you can still smile given the circumstances."

    show rene neutral
    r "Thank you for all the information, Aunty. Now we need to figure out what our next step will be."
    am "I will leave you to it then. It's time to make lunch anyway."
    "Aunt Matilda leaves us and soon we hear music playing from the kitchen and the sound of pots and pans."
    "Aunty sings a happy song. She shouldn't be able to hear us talking."
    show shadow neutral
    sh "Your Aunt... she's-"
    show rene happy
    r "Amazing? Ha! I know."
    sh "Ahem, anyway..."
    sh "We have quite the path ahead of us, don't we?"
    show rene neutral
    "It's just the two of us now. As everything slows down, the situation really starts to sink in for me."
    "Gosh... this is all so crazy."
    "Never had it crossed my mind that there was something bigger than the both of us, using us. Pitting us against each other."
    "An organization bent on taking over the world... using our powers."
    "What do we even do about this?"
    if samuel >= 20 and villain >= 25:
        jump ch3_s3_villain
    else:
        jump ch3_s3_4

label ch3_s3_villain:
    show shadow neutral
    sh "If I may make a suggestion..."
    show shadow happy
    sh "Why don't we just leave all of this behind?"
    show rene surprised
    r "What do you mean, leaving everything behind?!"
    sh "Think about it. Neither Dusk or Dawn are good organisations. You and I know this now."
    sh "Why don't we use the powers we've been given to do our own good?"
    sh "No masters, no one to tell us what to do. We choose what's good, and what's not."
    sh "If killing someone is for the greater good, it should be done."
    sh "If they are more valuable to us alive, they should live. Simple as that."
    r "Well, it makes sense to me. But... what exactly do you want to do?"
    sh "Start our own duo. Just us. Doing what we think is right."
    r "Wow... that's... I didn't expect...."
    sh "I really like you, Rene. If there's anyone I could choose to team up with, it would be you."

menu:
    "I like that":
        # GOOD END 1: VILLAIN AT HEART
        jump ch3_s3_villain2
    "We can't just abandon this!":
        jump ch3_s3_villain3

label ch3_s3_villain2:
    show rene happy
    "How can I resist those words?"
    r "I'd be happy to join you in this!"
    sh "Excellent."
    # CG 1: THE BOLT/SHADOW DUO BACK TO BACK
    scene cg1_villain_heart with Fade(0.5, 0.0, 0.5)
    "This marks the start of our duo. We decided to leave the whole Dusk and Dawn problem behind."
    "Of course the two organisations hunt us relentlessly."
    "But instead of stealing items from warehouses and fighting against each other, we spend time actually helping people."
    "I lost my friends, leaving them behind."
    "But were they really my friends? Or just people I fought alongside because I had to?"
    "Samuel left his colleagues behind too. That made us grow closer together."
    "The important thing is that we have each other and I'm happy. I'm doing what I always wanted to do."
    "I wish I wasn't haunted by it all, but you can't have everything."
    "GOOD END 1: VILLAIN AT HEART"
    return
label ch3_s3_villain3:
    show rene neutral
    r "Samuel, I... we can't. Not now, at least."
    r "Not while our two teams are fighting each other. Not while Daylight plans to take over the world."
    show shadow neutral
    "He's hurt, but I'm firm in this decision."
    sh "You're right... that might have been hasty on my part."
    show shadow happy
    sh "But... I want you to sincerely think about it."
    show rene angry
    r "Gah... where is your mind right now?!"
    sh "I dunno. Maybe we can explore it?"
    "... unbelievable!"
    jump ch3_s3_4

label ch3_s3_4:
    if bastion >= 15:
        show shadow neutral
        sh "You probably want to rush in there soon, huh?"
        show rene surprised
        r "Huh? What makes you think that?"
        sh "Well, your friend Bastion is out there. I can tell you care for him..."
        sh "... and that he cares for you."
        show rene shy
        "I feel my cheeks flush. I mean, yeah, we care for each other... but that's because we're a team."
        "Right?"
        sh "The fact that you're thinking about it..."
        if bastion > samuel:
            show shadow neutral
            sh "Heh. So much for all of that flirting."
        show rene angry
        r "What does that mean?!"
        show shadow neutral
        sh "Nothing. I just wanna know what's on your mind right now. Considering our... current predicament."

    show rene neutral
    r "Right now, we need to think about what to do next. And I think I have an idea..."
    show shadow neutral
    sh "And that is?"
    r "Daylight. We can't let them go through with their plans. Not with so many innocent lives at stake here."
    r "Not with my friends out there..."
    sh "..."
    "He looks thoughtful for a moment. For a second, I straight up think that he's going to leave me on my own."
    sh "Ha, when you get all fired up like that..."
    show shadow happy
    sh "I can't help but feel the same way. I {i}could{/i} disappear but..."
    sh "I think I'm feeling a little spiteful."
    show rene happy
    r "Samuel..."
    "I'm glad."
    "I'm glad I'm not alone in this."
    show shadow neutral
    sh "Hey, come back to Earth. We can talk big as much as we want, but I'd like to have a plan before we head out."
    show rene happy
    "A thought immediately comes to mind."
    r "Let's go to my team's secret base."
    "It's been two days, after all. They must be worried sick for me."
    if bastion > 15:
        "And... everything that's happened with Bastion... I need to make sure."
    sh "Ah... and?"
    show rene neutral
    r "We'll gather the group together. Tell them about everything we've just learned."
    r "We can stop this fighting, and focus on what matters. All of us."
    "He seems like... he's doubting something. And I already have an idea where his head's at."
    r "I want you to be with me, please. It'll help a lot if you're there..."
    sh "... I'll follow. But the moment your friends try anything, I-"
    r "They won't. Not with me there."
    "Slowly, I see the doubt melt from his face."
    sh "... alright. Sounds good."
    r "Getting them on board is the most important step of the plan. Without them, we don't stand a chance."
    r "After that, we can come back here-- away from the eyes of Daylight."
    "We both give a nod to each other, and I start to lead the way."
    "Lead the way... towards what could be the biggest fight of all of our lives."
    jump ch3_s4_1
