label ch4_s3_bastion:
    ba "Here, I'm coming with you!"
    show bolt surprised
    r "Shouldn't you stay up here?"
    ba "Well, I certainly can't let you go alone."
    show bolt neutral
    r "I won't be alone, I'll be with Mag- ah... yeah. Right...."
    ba "Remember what your aunt said... there's bound to be some heavy resistance down there."
    ba "I want to lend my strength against whatever it is."
    ba "When we fight together as a team... as a duo... we're unstoppable."
    "Bastion... this boost in confidence is exactly what I needed."
    s "Hey, don't keep us waiting, yeah? Fighting robots is starting to drag."
    ba "We'll be back before you know it!"
    ba "..."
    ba "Samuel."
    s "Huh?"
    ba "You're a good man."
    s "... thanks."
    "They trade a nod of understanding with each other, before Bastion leads me down the stairs of the bunker."
    jump ch4_s4_bastion1

label ch4_s4_bastion1:
    scene warehouse night with Fade(0.75, 0.5, 0.5)
    show bolt neutral at left
    show stoneman neutral at right

    "It was a long descent. As the two of us rush down the stairs, I try to keep an eye out for Magno who's already moved ahead of us."
    ba "I wonder what he's trying to do, rushing ahead like that..."
    r "Whatever the reason, he should've waited for us."
    "It gets colder and darker the further we descend."
    "I have no idea how deep in the earth we are, but I understand now why they were so bold with their bomb."
    "As soon as our feet hit the ground, we are greeted with the source of the bright light."
    "A gigantic orange crystal, sitting at the other end of the room."
    "It's enormous, standing  from floor to ceiling. It looks alot like the crystal that was inside of the bomb."
    "The bomb that... I'm holding."
    "Besides the complicated looking technology surrounding it, consisting of a bunch of terminals, there's nothing else here."
    "It's just a big, plain room."
    "At least, I think it is... the crystal is the only source of dim light."
    ba "If a small crystal can cause a large explosion... I don't even want to imagine the destruction a crystal of this size could cause."
    "I gulp."
    r "That must be why they built this place so far underground..."
    ma "You two. Hurry up already."
    "The both of us were so enamored with the crystal, we didn't even notice Magno standing a few feet in front of us."
    "He's just facing the crystal, staring it down."
    "I swear, if I didn't know any better, I would've assumed he was trying to have a staring contest with the thing."
    r "Right... come on! Let's make this quick."
    "I move forward, bomb in hand. I whisper to myself the instructions on how to arm the bomb again..."
    "That's very important."
    "As soon as I step closer to the crystal..."
    play sound "crash.mp3"
    show bolt surprised
    show stoneman surprised
    r "Woah!" with hit
    # scene white
    show bolt surprised at rightish
    show stoneman surprised at leftish
    with ease
    "Bright, white light fills the room, as if someone just flipped the light switch on."
    "Bastion immediately pulls me back next to him and Magno."
    "Before us, on the opposite side of the room..."
    "A hulking behemoth of steel. Like one of those mechs you'd see in a show, or a video game."
    show bolt neutral
    show stoneman neutral
    "It's facing us. At least, I {i}think{/i} it is."
    "It doesn't have any eyes, but the dangerous looking drill it has in place of one of its hands is pointed right at us."
    "... and the large gun mounted on its right shoulder."
    ma "Hmph! What a spectacular creation! A shame that machines cannot be persuaded with human sentiments..."
    ma "... but I will make it bend all the same."
    "Magno steps forward confidently, and we watch. He begins to raise his hand."
    "I begin to feel a massive power building within Magno. I can tell he's going to give his all."
    ma "You had the gall to use me. To claim me as some pawn in your scheme."
    ma "Yet, when you decide to make an enemy out of me, you don't even grant me any proper opposition!"
    ma "It's clear to me that not only did you not pay attention... but you do not fear me! And I will personally seek to make amends of that fact!"
    ma "Witness, firsthand, my magnificent power!"
    "He brings his hands together in a crushing motion towards the giant robot."
    "..."
    "Nothing. The robot doesn't react."
    show bolt surprised
    ma "... what?"
    "He tries again, to no avail."
    show stoneman surprised
    ba "It's resisting Magno's powers?! They've prepared for us!"
    ma "... bastards! BASTARDS!"
    "The shoulder mounted gun whirls awake, and twists to face Magno. A red dot appeared directly on his chest."
    r "Aiden!"
    play sound "lazer.mp3"
    "I teleport directly towards him, just barely managing to knock him down a second before the gun fires." with hit
    ma "Gah! You..."
    show bolt neutral
    r "Listen! Right now, you need to hide!"
    ma "Me?! Hide! Y-"
    show bolt angry
    r "You're dead weight right now!"
    play sound "lazer.mp3"
    show bolt neutral
    "I didn't catch the twisted look on his face for long as I'm forced to teleport again." with woosh
    "If I hadn't, that bullet would've ended me instantly."
    show stoneman neutral
    "I look back to see the crater the bullet made in the wall- the shells this beast is firing are huge!"
    "Even Bastion's powers wouldn't be able to deflect those..."
    ba "Let's go, Rene! We  can defeat this together!"
    "Bastion hardens his skin and rushes towards the robot at an angle."
    r "Right!"
    "I run towards the robot from the other side, forcing it to focus on two different targets."

menu:
    "Let Bastion lead!":
        r "I'm following your lead, Bastion!"
        ba "Right! Follow-up after me!"
        "The gun aims at Bastion and fires off a couple of rounds."
        "He's nimble enough to not get hit directly, but there's a couple of close calls."
        "As he gets closer, the robot is forced to ready its drill. It begins to spin, making this loud, constant, terrible sound."
        "Bastion doesn't even flinch."
        "As the robot thrusts its drill at Bastion, he leaps up over the drill and runs up the robot's arm."
        play sound "<from 10.0>metal-hit.mp3"
        "And with a giant leap, Bastion sends his fast crashing right into the head of the robot." with woosh
        stop sound fadeout 2.0
        "There was no way I was going to look cooler than that. I didn't even have a chance."
        "Bastion lands on the ground next to the robot. As it reels, Bastion takes hold of one of its arms and yanks it down, forcing it to kneel."
        ba "I've staggered it!"
        "Here goes nothing...!"
        jump ch4_s4_bastion2
    "I'll take the lead!":
        r "Follow my lead!"
        ba "I'm with you!"
        "The gun aims towards me, but I'm ready for it. The moment I see the light of the red laser, I teleport."
        "I repeated this, dodging shell after shell. It was a perfect distraction to keep the heat off of Bastion."
        play sound "<from 10.0>metal-hit.mp3"
        "He takes advantage of the ploy, rushing up underneath the robot and smashing his fist into one of its legs." with woosh
        stop sound fadeout 2.0
        "Even with the gift of steel limbs, it still couldn't hold its balance."
        "Bastion grabs one of its arms and yanks it down into a kneeling position."
        ba "I have it, Rene!"
        "Here goes nothing...!"
        jump ch4_s4_bastion2

label ch4_s4_bastion2:
    "I teleport myself onto the machine's shoulders, and immediately start looking for any weaknesses."
    "I know it's silly, but this thing is a machine! It can be shut off, right?"
    r "Just... keep it up! I'm sure I can find a-"
    "All of a sudden, a foul smelling mist expels from the robot. It forces me to cover my mouth almost instantly."
    "Ugh, I can still smell it! It smells like something from chemistry class..."
    show stoneman surprised
    ba "Wh-what the..."
    show bolt surprised
    r "...!"
    "I peer down to see Bastion reeling."
    "He was looking at his hands- at the expanding patches of his own flesh as the stone parts of his body melt away."
    "He's reverting back to his normal self! Whatever this mist is, it's rendering him useless!"
    r "Bastion! They put some kind of chemical in the mist! You need to-"
    "I wasn't allowed to finish my sentence as the air left my lungs."
    "In my moment of distraction, the hand clamps itself around me, holding me in a vice grip."
    "I can't breathe."
    show stoneman angry
    ba "N-No...! Rene! Don't worry, I-"
    play sound "woosh.mp3" volume 0.1
    queue sound "crash.mp3" volume 1.0
    "The next thing I see is Bastion flying across the room. With its foot now free, the robot kicked Bastion as hard as it could."
    hide stoneman
    show bolt at center with ease
    "I can't breathe. My ribs are seconds away from becoming dust, but somehow, that isn't the first thing on my mind."
    "Bastion lands on the ground rolling. And then he stops moving."
    "I try to teleport, but..."
    "Of course, they were prepared for me too. I don't know how they did it, but my powers aren't working."
    "I want to scream, to kick, to be filled with an insane amount of power to turn this situation around."
    "But I can't do anything."
    show bolt sad
    "All I can do is shed a tear."
    "I've never felt so afraid, so powerless."
    "The robot holds me closer, and I hear the horrifying sound of the drill as it begins to rev up."
    "It aims it towards me, and inches it closer."
    show bolt neutral
    "My vision is already fading to black. It's either going to crush me to death, or..."
    scene black with Fade(0.75, 0.0, 0.0)
    "..."
    "What a way to go out. I-"
    scene warehouse with fade
    show bolt surprised
    r "*gasp!*"
    "All of a sudden, I draw breath. I feel my body begin to loosen up, but it's still holding me."
    "The spinning drill, mere inches away from my body,  it's stopped."
    "It just... stopped trying to kill me?"
    "That's when it hit me."
    r "M...Mia!"
    "The red dot on the gun's blinking. I think that was her way of telling me..."
    "... to turn it against the robot."
    show bolt neutral
    "I squirm out of the grip, mustering all the strength I can. I can barely touch the tip of the shoulder mounted gun."
    "I take a deep breath, lurch forward, and give it a huge smack to the side. The gun turns to point directly towards the robot's head."
    "And in that instant..."
    play sound "lazer.mp3"
    "The robot's head acquires a new, large hole."
    "The steel behemoth crumbles to the ground in a mix of sparks and smoke, taking me with it." with hit
    "It was down."
    "Mia saved my life... again."
    show bolt surprised
    r "Bastion!"
    show bolt neutral at rightish with move
    show stoneman neutral at leftish with dissolve
    "I scramble to Bastion, who still hasn't moved."
    "I shouldn't be moving so fast with these injuries, but I don't care."
    show bolt sad
    r "Bastion...?"
    "I kneel next to him, taking his head in my hands."
    r "Bastion, please... say something..."
    "No, please. Not him. Not now. Not when we're so close."
    "A tear leaves my eye, falling onto his face."
    ba "... something..."
    show bolt surprised
    r "Huh?!"
    "Bastion turns to me in my hands, looking up to me with a tired smile."
    ba "Sorry, I know I was supposed to say something other than... \"something\". I'm not very creative..."
    show stoneman happy
    ba "Fantastic job as always, Rene."
    show bolt happy
    "I hug him, and he hugs me back."
    ba "Ow..."
    r "Oh, it's just a hug. Don't be a baby."
    "I let him down gently. It's clear that he's pretty hurt."
    show bolt neutral
    r "How are you feeling?"
    show stoneman neutral
    ba "I'm hurt, but... I know I'll feel better once we complete our objective."
    ba "I just need a moment to get on my feet..."
    r "No, you sit there and rest."
    show bolt happy
    r "I'll get this thing set up and we'll be out of here lickety split."
    ba "Rene..."
    show bolt neutral
    r "The hard part's done! Just let me take care of the rest, okay? I'll be back."
    "He nods. He knows better than to argue right now."
    "There's nothing standing between us and our goal now."
    "The hard part is over."
    hide stoneman with dissolve
    show bolt at center with move
    "I walk away from Bastion, and towards the crystal, bomb in hand--"
    ma "Wait."
    show bolt surprised
    r "Wait?"
    ma "I believe it's to our benefit that we keep this crystal intact."
    r "Huh?! What are you talking about?!"
    ma "Fools... making me feel {i}powerless{/i}. I'll show them. I'll make them rue the day."
    "He was almost mumbling to himself darkly. It was almost like I wasn't even there."
    show bolt neutral
    r "Aiden... it's over. With this, we can stop Daylight from-"
    ma "From taking over the state, right? Such a crystal can hold such power?"
    ma "I see now what must happen... I must learn how to use their technology. To use it for my own good."
    ma "Don't you see?! This is destiny! This is {i}mine{/i} to use! Mine to conquer with! {i}I'LL MAKE THEM REGRET THE DAY THEY EVER CROSS ME!{/i}"
    r "..."
    r "Aiden-"
    ma "Call me that again, and I'll make God weep when he hears what I've done to you."
    ma "There is a change of plans. The crystal will not be destroyed. Now leave, Bolt. I will spare you from my future conquests."
    ma "And consider that the kindest thing I will ever do. Especially to someone who has referred to me as {i}dead weight{/i}."
    r "... no. No, I can't let you do this."
    ma "Then die."
    play sound "hit.mp3" volume 0.6
    "In an instant, metal strikes me across the head. A scattered chunk of metal from the inside of the robot." with hit
    "I'm instantly floored and dazed- and I'm too weak to do anything."
    ma "I offer you mercy, and you take it... for granted? You take anything I do FOR YOU GRANTED?"
    "Magno raises his hand, and a large chunk of metal levitates high above me."
    ma "Don't bother haunting me, bitch."
    "I... I can't move. My brain is giving the commands, but my body isn't listening."
    show stoneman angry at offscreenright
    "Was this... really it?"
    show stoneman angry at leftish
    show bolt surprised at rightish
    with ease
    ba "NO!"
    show stoneman neutral
    play sound "metal-crash.mp3" volume 0.3
    "Bastion leaps into view, covering me with his body. I don't get to object as the chunk smashes directly into him." with hit
    "His body becomes terrifyingly still on top of me."
    show bolt sad
    r "Bastion...!"
    ma "...very well then. Let this be my last generous act. I will send you off into the afterlife with a companion! Thank me in hell-"
    play sound "gunshot.mp3"
    show bolt surprised
    ma "..." with woosh
    "Magno looks down to see his chest bleeding. Bleeding from the hole that was just placed into it."
    ma "You..."
    l "Bitch? Is that what you're going to say?"
    l "Geez, for someone with a fancy vocabulary... your insults really get stale."
    "Magno looks up to Levina, shocked."
    ma "You dare..."
    play sound "<from 1.0>gunshots.mp3" volume 0.6
    "Levina fires off a stream of bullets at Magno, each one creating different wounds in his chest."
    "Magno stood no chance. His look was one of fury, but I can tell his body couldn't take Levina's assault."
    "Reduced to being on his knees, he's forced to look up to Levina. The look on his face- the anger. The defeat. The {i}betrayal.{/i}"
    ma "Snap...shot... you wi-"
    play sound "gunshot.mp3"
    "One bullet placed between his eyes." with hit
    "Aiden crumples to the ground, lifeless."
    l "I've always wanted to do that, ever since we started working together. I thought about doing it when he was sleeping, but..."
    l "I didn't want to just rob him of his final {i}breath{/i}, but his final {i}words{/i}."
    l "I wanted him to look me in the eye and have no question on who was responsible for the worst part of his life."
    "..."
    "It was chilling, how she was just so... nonchalant about it. There was no sentiment about it."
    "Just a cold blooded kill."
    show bolt neutral
    "Levina walks across the room towards us, taking hold of the bomb in my hand. I hold onto it, not wanting to give it over."
    l "... hey, we came here to do something. If you're not going to do it, then I'm going to."
    r "You'll...?"
    l "I've always wanted to blow something up. Besides, you look like you need a good rest. You {i}and{/i} your boyfriend."
    l "So... why don't you leave this to me and go join your friends at your Aunt's place?"
    l "They left already, and I have a feeling they're dying to see you."
    r "What about you...?"
    l "Eh... chances are, you'll probably never see me again. Sorry, I'm a little too old for your group."
    l "None of your business, anyway. Come on, hand it over."
    "She gives a light tug, and takes the bomb away from me."
    "It still doesn't {i}feel{/i} right but... I could tell she's telling the truth."
    "I can't fully understand her, no matter how hard I try..."
    l "Alright, I just press this button and... set the timer..."
    r "Actually, you..."
    "I give a quick explanation."
    l "Ah, alright, phew. Woulda blown myself up. Thanks."
    "What a... weird exchange."
    l "Now, get yourself out of here, because I'm not going to carry you out."
    r "... thank you..."
    l "You know? It's been a pleasure. You weren't half boring to work with. So, thanks. And you're welcome."
    l "Alright, I'm serious. Get outta here. Shoo."
    "I... nod."
    "If it wasn't for Levina, Bastion and I would've been dead."
    "I'll admit, she confuses me but... I'm thankful that she was on our side. It'd be interesting if we met again."
    "I wrap my arms around the unconscious Bastion, close my eyes..."
    "... and think of Aunty's place."
    jump ch4_s5_1
