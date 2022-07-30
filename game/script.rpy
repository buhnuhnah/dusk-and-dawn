#SPRITE POSITIONS
transform left:
    xalign 0.15
transform right:
    xalign 0.85
transform leftish:
    xalign 0.35
transform rightish:
    xalign 0.65
transform farleft:
    xalign 0.05
transform farright:
    xalign 0.95
transform flip:
    xzoom -1.0
transform side:
    xalign 0.05
    yalign 1.0

#CHARACTER DEFINITIONS
define ba = Character("Bastion")
define st = Character("Stoneman", image='stoneman')

define a = Character("Alicia")
define f = Character("Frostbite")

define r = Character("Rene")
define b = Character("Bolt", image="bolt")

define m = Character("Mia")

define s = Character("Samuel")
define sh = Character("Shadow")

define ma = Character("Magno")
define sn = Character("Snapshot")
define l = Character("Levina")

define am = Character("Aunt Matilda")

# IMAGES

# plays in ch 4 when the alarm gets tripped
# ANA CHANGE THIS TO INCLUDE THE FULL PATH ONCE YOU GET REAL WAREHOUSE
image warehouse alarm:
    "warehouse_red.png" with dissolve
    pause 0.5
    "warehouse.png" with dissolve
    pause 1.0
    repeat

init python:
    config.searchpath.extend(["game/audio", "game/images/backgrounds"])
    dice = renpy.random.randint(2,8)*0.1
    renpy.add_layer('mc', above='overlay')

    # POINT TRACKERS
    villain = 0
    samuel = 0
    bastion = 0

    # STORY TRACKERS
    murder = False          # true if you kill any guards
    spare1kill2 = False     # true if you spare guard 1 and kill guard 2 in ch 1
    hide_identity = False   # true if you tell samuel you're not bolt in ch 2
    ch2choice = "EMPTY"     # holds what choice you made in ch 2: ("LOOK", "FIGHT", or "REFUSE")

    # SHAKE EFFECT
    import math

    class Shaker(object):
        anchors = {
            'top' : 0.0,
            'center' : 0.5,
            'bottom' : 1.0,
            'left' : 0.0,
            'right' : 1.0
            }
        def __init__(self, start, child, dist):
            if start is None:
                start = child.get_placement()
            self.start = [self.anchors.get(i,i) for i in start] # central position
            self.dist = dist                                    # max distance from start in pixels
            self.child = child
        def __call__(self, t, sizes):
            # turns float to int
            def fti(x, r):
                if x is None:
                    x = 0
                if isinstance(x, float):
                    return int(x * r)
                else:
                    return x
            xpos, ypos, xanchor, yanchor = [fti(a,b) for a,b in zip(self.start, sizes)]
            xpos = xpos - xanchor
            ypos = ypos - yanchor
            nx = xpos + (1.0-t) * self.dist * (renpy.random.random()*2-1)
            ny = ypos + (1.0-t) * self.dist * (renpy.random.random()*2-1)
            return (int(nx), int(ny), 0, 0)
    def _Shake(start, time, child=None, dist=100.0, **properties):
        move = Shaker(start, child, dist=dist)
        return renpy.display.layout.Motion(move, time, child, add_sizes=True, **properties)
    Shake = renpy.curry(_Shake)

    # Shake(position, duration, max distance
    sshake = Shake((0, 0, 0, 0), 0.5, dist=15)      # for getting hit
    woosh = Shake((0, 0, 0, 0), 0.5, dist=5)        # for almost getting hit

    # FLASH EFFECTS
    flash = Fade(0.1, 0.0, 0.25, color="#fff")
    hit = ComposeTransition(sshake, after=flash)

label start:
    # DEBUGGING
    screen debug():
        frame:
            xalign 0.1 ypos 50
            hbox:
                spacing 50
                vbox:
                    text "Villain Points"
                    text "[villain]"
                    textbutton "Add" action SetVariable("villain", villain+5)
                    textbutton "Remove" action SetVariable("villain", villain-5)
                vbox:
                    text "Samuel Points"
                    text "[samuel]"
                    textbutton "Add" action SetVariable("samuel", samuel+5)
                    textbutton "Remove" action SetVariable("samuel", samuel-5)
                vbox:
                    text "Bastion Points"
                    text "[bastion]"
                    textbutton "Add" action SetVariable("bastion", bastion+5)
                    textbutton "Remove" action SetVariable("bastion", bastion-5)

    # HIDE THIS FOR FINAL PRODUCT
    show screen debug

    jump ch1
