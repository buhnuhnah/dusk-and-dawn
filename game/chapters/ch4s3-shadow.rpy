label ch4_s3_shadow:
    hide frostbite
    hide mia
    show shadow neutral
    with dissolve
    s "You're not going alone."
    r "I won't be alone, I'll be with Mag--"
    "I stop."
    s "There's going to be something big guarding that crystal, no doubt. I'm going to make sure you do what you have to do without getting hurt."
    show shadow smirk
    s "When you and I work together, I know we can do amazing things."
    show bolt shy onlayer mc
    "Samuel... ugh. Aren't you the charmer?"
    show bolt neutral onlayer mc
    show shadow at left with ease
    show stoneman angry at right with dissolve
    ba "Go, you two! We have everything covered up here!"
    show shadow neutral
    s "We'll be back before you know it."
    show stoneman neutralsmile
    ba "And Samuel?"
    s "Huh?"
    ba "...thank you."
    s "..."
    "They trade a nod of understanding with each other, before Samuel places his hand on the small of my back."
    "We both descend through the bunker doors."
    jump ch4_s4_shadow1

label ch4_s4_shadow1:
    scene black
    hide bolt
    show bolt neutral at side onlayer mc
    show shadow neutral at center
    with Fade(0.75, 0.5, 0.5)

    "It's a long descent. As the two of us rushed down the stairs, I tried to keep an eye out for Magno, who's already moved ahead of us."
    s "You know... he was always sort of a glory hog."
    r "Oh yeah? Huh. Never would've guessed."
    "It gets colder and darker the further we descend."
    "I have no idea how deep in the earth we are, but I understand now why they were so bold with their bomb."
    "As soon as our feet hit the ground, we are greeted with the source of the bright light."
    show shadow at right with ease
    scene crystal
    hide bolt
    show bolt surprised at side onlayer mc
    show shadow neutral at right
    with dissolve
    "A gigantic orange crystal, sitting at the other end of the room."
    "It's enormous, standing  from floor to ceiling. It looks alot like the crystal that was inside of the bomb."
    "The bomb that... I'm holding."
    show bolt neutral onlayer mc
    "Besides the complicated looking technology surrounding it, consisting of a bunch of terminals, there's nothing else here."
    "It's just a big, plain room."
    "At least, I think it is... the crystal is the only source of dim light."
    s "... so, the bomb you're holding. If a crystal of that size can level a large building..."
    "I gulp."
    r "That must be why they built this place so far underground..."
    show magno neutral at left with dissolve
    ma "You two. Hurry up already."
    "The both of us are so enamored with the crystal, we completely forgot about Magno."
    "He's just standing, facing the crystal, staring it down. It's like he's committed to not blinking."
    r "Right... come on! Let's make this quick."
    "I move forward, bomb in hand. I start to whisper all of the instructions on how to arm the bomb again... and how to set the timer."
    "That's very important."
    "As soon as I step closer to the crystal..."
    play sound "crash.mp3"
    r "Woah!" with sshake
    scene crystal white
    show bolt surprised onlayer mc
    show shadow surprised at right
    show magno surprised at left
    with dissolve
    "Bright, white light fills the room, as if someone just flipped the light switch on."
    show shadow angry
    "Samuel immediately pulls me back next to him and Magno."
    "Before us, on the opposite side of the room..."
    show shadow neutral
    show magno neutral
    show crystal behind shadow with dissolve
    "A hulking behemoth of steel. Like one of those mechs you'd see in a show, or a video game."
    "It's facing us. At least, I {i}think{/i} it is."
    show bolt neutral onlayer mc
    "It doesn't have any eyes, but the dangerous looking drill it has in place of one of its hands is pointed right at us."
    "... and the large gun mounted on its right shoulder."
    ma "Hmph! What a spectacular creation! A shame that machines cannot be persuaded with human sentiments..."
    ma happy "... but I will make it bend all the same."
    "Magno steps forward confidently, and we watch. He begins to raise his hand."
    "I begin to feel a massive power building within Magno. I can tell he's going to give his all."
    ma angry "You had the gall to use me. To claim me as some pawn in your scheme."
    ma "Yet, when you decide to make an enemy out of me, you don't even grant me any proper opposition!"
    ma "It's clear to me that not only did you not pay attention... but you do not fear me! And I will personally seek to make amends of that fact!"
    ma "Witness, firsthand, my magnificent power!"
    "He brings his hands together in a crushing motion towards the giant robot."
    "..."
    "Nothing. The robot doesn't react."
    ma surprised"... what?"
    "He tries again, to no avail."
    show shadow surprised
    s "Did they... make this one so it's resistant to Magno's powers?!"
    ma angry "... bastards! BASTARDS!"
    "The shoulder mounted gun whirls awake, and twists to face Magno. A red dot appears directly on his chest."
    show bolt surprised onlayer mc
    r "Aiden!"
    play sound  "lazer.mp3"
    "I teleport directly towards him, just barely managing to knock him down a second before the gun fires." with hit
    ma "Gah! You..."
    show bolt angry onlayer mc
    r "Listen! Right now, you need to hide!"
    ma "Me?! Hide! Y-"
    r "You're dead weight right now!"
    play sound "lazer.mp3"
    hide magno with dissolve
    show shadow neutral at center with ease
    "I didn't catch the twisted look on his face for long as I'm forced to teleport again. If I hadn't, that bullet would've ended me instantly." with woosh
    show bolt surprised onlayer mc
    "I look back to see the crater the bullet made in the wall- the shells this beast is firing are huge!"
    show shadow smirk
    s "Guess it's just you and me, huh? Bet you're glad I came down here!"
    show shadow angry
    "Samuel rushes towards the robot at an angle, ready to dodge at a moment's notice."
    show bolt neutral onlayer mc
    r "Yeah, guess you can say that!"
    show bolt angry onlayer mc
    "I run towards the robot from the other side, forcing it to focus on two different targets."

menu:
    "Let Samuel lead!":
        r "I'm following whatever you do, Samuel!"
        show shadow smirk
        s "Then try not to stare! Ha!"
        show shadow angry
        play sound "shadow.mp3" volume 0.8
        "Shadow uses the shadows the machine was casting to send tendrils out of it, slamming it into various parts." with sshake
        "The tendrils wrap around the machine, contricting it."
        jump ch4_s4_shadow2
    "I'll take the lead!":
        r "Follow my lead!"
        show shadow smirk
        s "Heh, I'll try not to get distracted."
        "Really?"
        show shadow neutral
        "The gun aims towards me, but I'm ready for it. Everytime it even dares to shoot at me, I teleport a short distance."
        "I was dodging shell after shell, keeping the attention of the gun off of Samuel. It was a perfect distraction."
        show shadow angry
        play sound "shadow.mp3" volume 0.8
        "Samuel eventually follows up, using the shadows that the machine casted to create tendrils." with sshake
        "The tendrils wrapped around the machine, constricting it."
        jump ch4_s4_shadow2

label ch4_s4_shadow2:
    "I use this distraction to teleport myself onto the machine's shoulders, and immediately start looking for any weaknesses."
    "I know it's silly, but this thing is a machine! It can be shut off, right?"
    r "Just... keep it up! I'm sure I can find a-"
    "All of a sudden, an insanely bright light fills my vision."
    show crystal white behind shadow with dissolve
    show bolt surprised onlayer mc
    show shadow hurt
    r "Ah!"
    s "Tch...!"
    "My eyes adjust just barely to see that the robot was the one emitting this bright light."
    "Wait a second, if it's filling the room with bright light, that means... Samuel's powers are useless!"
    r "Samuel! They're prepared for you! You need to-"
    show bolt hurt onlayer mc
    "I wasn't allowed to finish my sentence as the air left my lungs." with woosh
    "In my moment of distraction, the hand clamps itself around me, holding me in a vice grip."
    "I can't breathe."
    show shadow angry
    s "R-Rene! Are you okay?! I can't see y-"
    play sound "lazer.mp3"
    "..." with hit
    hide shadow with dissolve
    "The sudden silence draws my attention."
    "I can't breathe. My ribs are seconds away from becoming dust, but somehow, that isn't the first thing on my mind."
    "I see Samuel on the ground, next to a large crater. He isn't moving."
    "I try to teleport, but..."
    "Of course, they were prepared for me too. I don't know how they did it, but my powers aren't working."
    "I want to scream, to kick, to be filled with an insane amount of power to turn this situation around."
    show bolt sad onlayer mc
    "But I can't do anything."
    show bolt crying onlayer mc
    "All I can do is shed a tear."
    "I've never felt so afraid, so powerless."
    "The robot holds me closer, and I hear the horrifying sound of the drill as it begins to rev up."
    "It aims it towards me, and inches it closer."
    show bolt hurt onlayer mc
    "My vision is already fading to black. It's either going to crush me to death, or..."
    scene black
    hide bolt onlayer mc
    with Fade(0.75, 0.0, 0.0)
    "..."
    "What a way to go out. I-"
    scene crystal white
    show bolt surprised at side onlayer mc
    with fade
    r "*gasp!*"
    "All of a sudden, I draw breath. I feel my body begin to loosen up, but it's still holding me."
    "The spinning drill, mere inches away from my body,  it's stopped."
    "It just... stopped trying to kill me?"
    "That's when it hit me."
    r "M...Mia!"
    "The red dot on the gun's blinking. I think that was her way of telling me..."
    "... to turn it against the robot."
    show bolt hurt onlayer mc
    "I squirm out of the grip, mustering all the strength I can. I can barely touch the tip of the shoulder mounted gun."
    show bolt angry onlayer mc
    "I take a deep breath, lurch forward, and give it a huge smack to the side. The gun turns to point directly towards the robot's head."
    "And in that instant..."
    play sound "lazer.mp3"
    "The robot's head acquires a new,  large hole." with hit
    "The steel behemoth crumbles to the ground in a mix of sparks and smoke, taking me with it." with woosh
    show bolt neutral onlayer mc
    "It was down."
    "Mia saved my life... again."
    show bolt surprised onlayer mc
    r "Samuel!"
    "I scramble to Samuel, who hasn't moved."
    "I shouldn't be moving so fast at this rate because of my injuries, but I don't care."
    show bolt sad onlayer mc
    r "Samuel...?"
    "I kneel next to him, taking his head in my hands."
    show bolt crying onlayer mc
    r "Samuel, please... please don't go..."
    "No, please. Not him. Not now. Not when we're so close."
    "A tear leaves my eye, falling onto his face."
    show shadow smirk with dissolve
    s "Hm... I guess I'm supposed to wake up now, huh?"
    show bolt surprised onlayer mc
    r "Huh?!"
    s "It's a thing in movies, when the person cries on-"
    show bolt angry onlayer mc
    "I drop him."
    show shadow hurt
    play sound "<to 1.0>punch.mp3" volume 0.6
    s "Ow. Hey, I wasn't finished..." with sshake
    r "... jerk!"
    show shadow happy
    s "Hehe... hey. Let's finish the job already."
    show bolt sad onlayer mc
    r "Are you okay, at least?"
    show shadow neutral
    s "That bullet almost hit me... I guess it landed close enough to really hurt."
    s "Go ahead and set the bomb, alright? I'll focus on getting myself to my feet here..."
    show bolt neutral onlayer mc
    r "I'll get this thing set, then help you up... I'll be back!"
    "There is nothing standing between us and our goal now."
    "The hard part is finally over."
    hide shadow with dissolve
    "I walk away from Samuel, and towards the crystal, bomb in hand-"
    show magno neutral with dissolve
    ma "Wait."
    show bolt surprised onlayer mc
    r "Wait?"
    ma "I believe it's to our benefit that we keep this crystal intact."
    r "Huh?! What are you talking about?!"
    ma angry "Fools... making me feel {i}powerless{/i}. I'll show them. I'll make them rue the day."
    "He was almost mumbling to himself darkly. It was almost like I wasn't even there."
    show bolt sad onlayer mc
    r "Aiden... it's over. With this, we can stop Daylight from-"
    ma neutral "From taking over the state, right? Such a crystal can hold such power?"
    ma "I see now what must happen... I must learn how to use their technology. To use it for my own good."
    show bolt surprised onlayer mc
    ma angry "Don't you see?! This is destiny! This is {i}mine to use! Mine to conquer with! {i}I'LL MAKE THEM REGRET THE DAY THEY EVER CROSS ME!{/i}"
    r "..."
    show bolt sad onlayer mc
    r "Aiden-"
    ma "Call me that again, and I'll make God weep when he hears what I've done to you."
    ma neutral "There is a change of plans. The crystal will not be destroyed. Now leave, Bolt. I will spare you from my future conquests."
    ma "And consider that the kindest thing I will ever do. Especially to someone who has referred to me as {i}dead weight.{/i}"
    show bolt neutral onlayer mc
    r "... no. No, I can't let you do this."
    ma angry "Then die."
    play sound "hit.mp3"
    show bolt hurt onlayer mc
    "In an instant, metal strikes me across the head. A scattered chunk of metal from the inside of the robot." with sshake
    "I'm instantly floored and dazed- and I'm too weak to do anything."
    ma "I offer you mercy, and you take it... for granted? You take anything I do FOR YOU GRANTED?"
    "Magno raises his hand, and a large chunk of metal levitates high above me."
    ma "Don't bother haunting me, bitch."
    show bolt hurt onlayer mc
    "I... I can't move. My brain is giving the commands, but my body isn't listening."
    show shadow at offscreenright
    "Was this... really it?"
    show shadow angry at center with ease
    hide magno with dissolve
    s "NO!"
    show shadow hurt
    play sound "metal-crash.mp3" volume 0.3
    show bolt surprised onlayer mc
    "All of a sudden, I feel something pressing against me. A familiar warmth." with hit
    hide shadow with dissolve
    "Samuel used his body to shield me from the attack."
    "Now he lays on top of me... unconscious."
    show bolt sad onlayer mc
    r "Samuel..."
    show magno angry with dissolve
    ma "Very well then. By my generosity, I will send you off with a companion! Thank me in hell-"
    play sound "gunshot.mp3"
    show bolt surprised onlayer mc
    show magno surprised
    ma "..." with woosh
    "Magno looks down to see his chest bleeding. Bleeding from the hole that was just placed into it."
    ma "You..."
    show magno at left with ease
    show snapshot neutral at right with dissolve
    l "Bitch? Is that what you're going to say?"
    show snapshot annoyed
    l "Geez, for someone with a fancy vocabulary... your insults really get stale."
    "Magno looks up to Levina, shocked."
    ma angry "You dare..."
    play sound "<from 1.0>gunshots.mp3" volume 0.6
    show magno surprised
    show snapshot neutral
    "Levina fires off a stream of bullets at Magno, each one creating different wounds in his chest." with hit
    "Magno stood no chance. His look was one of fury, but I can tell his body couldn't take Levina's assault."
    "Reduced to being on his knees, he's forced to look up to Levina. The look on his face- the anger. The defeat. The {i}betrayal.{/i}"
    ma "Snap...shot... you wi-"
    play sound "gunshot.mp3"
    "One bullet placed between his eyes." with hit
    hide magno with dissolve
    "Aiden crumples to the ground, lifeless." with woosh
    show snapshot happy at center with ease
    l "I've always wanted to do that, ever since we started working together. I thought about doing it when he was sleeping, but..."
    l "For someone who tries to get the last word all the time, it's a lot more satisfying when you rob him of it."
    l "It's {i}especially{/i} satisfying looking him in the eye as he took it all in."
    "..."
    show bolt neutral onlayer mc
    "Levina walks across the room towards us, taking hold of the bomb in my hand. I hold onto it, not wanting to give it over."
    l "... hey, we came here to do something. If you're not going to do it, then I'm going to."
    show bolt surprised onlayer mc
    r "You'll...?"
    show snapshot happy
    l "I've always wanted to blow something up. Besides, you look like you need a good rest. You {i}and{/i} your boyfriend."
    l "So... why don't you leave this to me and go join your friends at your Aunt's place?"
    l "They left already, and I have a feeling they're dying to see you."
    r "What about you...?"
    show snapshot neutral
    l "Eh... chances are, you'll probably never see me again. Sorry, I'm a little too old for your group."
    l "None of your business, anyway. Come on, hand it over."
    "She gives a light tug, and takes the bomb away from me."
    "It still doesn't {i}feel{/i} right but... I could tell she's telling the truth."
    show bolt neutral onlayer mc
    "I can't fully understand her, no matter how hard I try..."
    l "Alright, I just press this button and... set the timer..."
    r "Actually, you..."
    "I give a quick explanation."
    l "Ah, alright, phew. Woulda blown myself up. Thanks."
    "What a... weird exchange."
    l "Now, get yourself out of here, because I'm not going to carry you out."
    r "... thank you..."
    show snapshot happy
    l "You know? It's been a pleasure. You weren't half boring to work with. So, thanks. And you're welcome."
    show snapshot neutral
    l "Alright, I'm serious. Get outta here. Shoo."
    "I... nod."
    "If it wasn't for Levina, Samuel and I would've been dead."
    "I'll admit, she confuses me but... I'm thankful that she was on our side. It'd be interesting if we met again."
    "I wrap my arms around the unconscious Samuel, close my eyes..."
    "... and think of Aunty's place."
    jump ch4_s5_1
