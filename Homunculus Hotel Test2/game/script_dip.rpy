
define slowfade = Fade(1.0, 0, 3.0)
define quickfade = Fade(1.0, 0, 1.0)
define slowerfade = Fade (3.0, 0, 3.0)
define slowdissolve = Dissolve(2.0)
define fadehold = Fade(3.0, 1.0, 3.0)

#define config.hard_rollback_limit = 0
define config.menu_include_disabled = True
init:
    image movie = Movie(size=(1920, 1080), xpos=0, ypos=0, xanchor=0, yanchor=0)

$ renpy.music.set_volume(0.2, channel="music")

define i = Character("Isabelle", color="#c45151", what_xpos=255, what_ypos=-450, who_ypos=-550, who_xpos=-14)
define isa = Character("Isabelle", color="#c45151", what_xpos=1675, what_ypos=-450, who_ypos=-550, who_xpos=1405)
define h = Character("Her", color="#5d6f5c", what_xpos=255, what_ypos=-450, who_ypos=-550, who_xpos=12)
define her = Character("Her", color="#5d6f5c", what_xpos=1675, what_ypos=-450, who_ypos=-550, who_xpos=1425)
define r = Character("Remu", color="#5d6f5c", what_xpos=255, what_ypos=-450, who_ypos=-550, who_xpos=12)
define re = Character("Remu", color="#5d6f5c", what_xpos=1675, what_ypos=-450, who_ypos=-550, who_xpos=1405)

label intro:
    stop music fadeout(2)
    scene black
    with slowfade
    scene intro0
    with slowfade
    play music "toherenevercome.ogg" fadein(2)
    $ renpy.pause(0.5)
    play movie "intro1.ogv" loop
    show movie with slowdissolve
    isa """
    It's always\nso beautiful...
    """
    h "What?"
    isa "Having\nbreakfast\nwith you."
    h """
    Yes...

    I...

    I think so\ntoo.

    It\nreally\nis...
    """
    play movie "intro2.ogv" loop
    show movie with dissolve
    isa """
    So...

    Do you\nfeel better\ntoday?

    Has it\npassed\nalready?
    """
    scene intro3
    with slowdissolve
    stop movie
    h """
    Hmm...

    Not so great,\nI guess.

    It doesn't\njust pass.

    Sadness\ndoesn't go\naway easily.
    """
    isa "I'm very\nsorry..."

    h """
    Sorry?

    Why...?

    It's not\nyour fault.
    """
    isa """
    Yes,\nbut...
    """
    h """
    It's not\nyour fault.

    So don't be\nsorry.

    Really.

    It's not\nabout\nyou.

    Don't have\npity\nfor me.

    It just\nmakes me\nfeel worse...

    And\nI am\ntired of it.

    I feel\nlike nobody's\npraying\nfor me...

    I\njust need you\nto care.

    Not to\nfeel sorry.
    """
    scene intro4
    with slowdissolve
    isa """
    But...

    I do care!

    And\nyou know\nthat!

    And I thought\nI did\nenough to\nshow it...
    """
    h """
    Huh...

    You know...

    Caring\nis something\nyou need to do\nconsistently.

    Not\nsometimes.

    Not only\nin the morning.

    Just asking\nhow I feel\ndoesn't mean\nyou really care.

    Otherwise\nit would be\ntoo easy.

    The truth is\nthat you\ndespise me.

    I see it\nwhen I\nget back\nfrom work.

    You\nhate\nwhat I do,\ndon't you?

    And to me\nthat means\nyou\nhate\nme.
    """
    isa """
    What...?

    That's\nnot\ntrue!

    I\ndon't\nhate\nyou!

    I'm\nin love\nwith you...
    """
    h """
    In love...

    I wish\nwe knew\nwhat it means\nto be in love.

    But\nI think\nwe actually\ndon't.

    At all.
    """
    stop music fadeout(2)
    scene black
    with slowfade
    scene intermission1
    with slowfade
    play music "toherenevercome.ogg" fadein(2)
    $ renpy.pause(0.5)
    play movie "intro1.ogv" loop
    show movie with slowdissolve
    h """
    You know...

    I like\nour kitchen.

    From here\nwe can see\nthe stars fading\nat morning.
    """
    isa """
    You're\nright.

    It really is\nbeautiful.
    """
    play movie "intro2.ogv" loop
    show movie with dissolve
    isa """
    Listen,\nI...

    I dreamt of you,\nlast night.

    And when\nI woke up...

    I wished\nyou were there\nwith me.
    """
    h "You know\nthat I\nfinish late..."
    isa """
    Yes,\nI know...

    And it's nice\nthat you're able\nto come home\nbefore I wake up...

    But,\ncan't you\nreally stop?

    It\nworries\nme.
    """
    h "You know\nI can't."
    isa """
    But...

    Why not?

    I don't\nunderstand.
    """
    scene intro3
    with slowdissolve
    stop movie
    h """
    We talked\nabout this.

    I like\nmy job.

    And\nI don't want\nto quit.
    """
    isa """
    You think\nit's ok to...

    Just\nleave me alone\nhere?

    While you're\nout there\nwith...

    Strangers.

    Just because\nit's your job?
    """
    h """
    Why do you\ncare so much?

    It's just\na job.
    """
    isa """
    It's\ndangerous.

    It's\ndegrading.

    And I\ndon't want you\nto do it.
    """
    h """
    Well,\nit's not about\nwhat you want.

    It's\nthe only thing\nI have\nfor myself.

    And\nI like it.
    """
    scene intro4
    with slowdissolve
    isa """
    If that's\nthe only thing\nyou have...

    Then why\nare you\nstill here?
    """
    stop music fadeout(2)
    scene black
    with slowfade
    scene intermission2
    with slowfade
    play music "toherenevercome.ogg" fadein(2)
    $ renpy.pause(0.5)
    play movie "intro2.ogv" loop
    show movie with slowdissolve
    h """
    Listen,\nIsabelle.

    I thought\nabout it,\nand...

    I think\nit's better if\nwe break up.
    """
    isa "Yeah,\nI figured\nas much..."
    h """
    I'm sorry,\nbut\nI cant go on\nlike this.

    It's...
    """
    isa "Is it\nabout\nyour job?"
    scene intro3
    with slowdissolve
    stop movie
    h """
    Partly.

    You know\nhow important it is,\nfor me.
    """
    isa """
    Yeah,\nsure.

    It's more\nimportant than me,\nI know.
    """
    h """
    Why do you\nalways have\nto compare it\nto yourself?

    This thing\nis not\nabout\nyou.

    I told you\na billion times.
    """
    isa """
    How can it\nnot be about\nme too?

    Do you know\nhow it feels?

    How it\nfeels to...

    Know you're\nout with\nsomeone else.

    For money.

    Every night.

    And\nI'm here,\nalone.

    I don't care\nif it's\njust a job.

    I just\ndon't want to\nfeel like this\nanymore.

    So yeah,\ndo whatever\nyou want.

    Just\nleave me\nalone.
    """
    stop music fadeout(2)
    scene black
    with slowfade
    scene ending
    with slowfade
    scene remufullui
    with slowfade
    i """
    Is that...

    Y-you...?
    """
    her """
    Yes.

    It's,\nuhm...

    It's been\na longtime?
    """
    i """
    A longtime?

    A...

    You\ndisappeared.

    You\nabandoned\nme.

    You...
    """
    her """
    I know...

    And\nI'm\nsorry.

    But you\nmust understand\nthat...

    Well.

    I'm\nsuffocating.
    """
    scene remunotebook
    with slowdissolve
    her """
    You always\nbuilt up\nall these\nwalls...

    It was impossible\nfor me\nto really get\nin touch with you.
    """
    i "So\nit's always\nmy fault..."
    her """
    No...

    It's just\nwho you are.

    And I've\nnever\naccepted it.

    I just stared\nwhile you were\nalways writing\non your notebook.

    It was\nour fault.
    """
    scene remunoui
    with slowdissolve
    her """
    I\nmissed\nyou,\nfor all\nthis time.

    While\nI was\naway...

    I always thought\nabout\nyou.

    And I\nwanted to...

    ...
    """
    scene remugetup1
    with slowdissolve
    $ renpy.pause(2)
    scene remugetup2
    with slowdissolve
    $ renpy.pause(2)
    scene hug1
    with slowdissolve
    $ renpy.pause(2)
    scene hug2
    with slowdissolve
    $ renpy.pause(2)
    scene hug3b
    with slowdissolve
    $ renpy.pause(2)
    scene hug3
    with slowdissolve
    her "I\nmissed\nthis."
    i """
    I...

    I\ndon't know\nwhat to\nsay...

    Remu,\nI...

    So\nmuch time\nhas passed.
    """
    re """
    Do you\nreally care\nabout time?

    We can\nrewrite it.

    We can\ngo back.

    At least in\nhere...

    In\nyour\ndreams.
    """
    scene hug4
    with slowdissolve
    i """
    In my\ndreams...
    """
    scene hug5
    with slowdissolve
    i """
    I\nalways see\nyou.
    """
    scene hug7
    with slowdissolve
    re """
    I know...

    But\nI am here\nnow.
    """
    i """
    Where\nhave you\nbeen?

    I\nmissed\nyou.
    """
    stop music fadeout (2)
    re """
    I won't\ngo\nanywhere.

    Anymore...
    """
    play sound "ending.ogg" fadein(2)
    #scene school1b
    #with slowdissolve
    $ renpy.pause(2)
    scene school1
    with slowdissolve
    i """
    You told me\nthe same thing\nthat time...

    Remember?
    """
    re """
    Yes...

    School was\nalmost\nover.

    It was\na hot summer...

    And we\nwere together.
    """
    i "As usual..."
    re """
    Yes,\nas usual.
    """
    scene school2
    with slowdissolve
    i """
    At\nthat\ntime...

    We knew\neach other\nsince the\nyear before.

    We\nalready were\nbest friends.

    Together\nagainst\nthe world.
    """
    scene school3
    with slowdissolve
    re """
    I\nalways thought\nyou had...

    Something\nspecial\nwithin you.

    And,\nback then...

    Your smile\nmade me\nso happy...

    Every day\nI went to school\njust because\nof that.

    You were\nmy reason\nto live.

    I don't\nsay that\nlightly...

    Without\nyou...

    Nothing\nwould have had\nsense.

    And\nthat day...
    """
    scene school4
    with slowdissolve
    re "All these\nfeelings..."
    scene school5
    with slowdissolve
    re "Suddenly\naccumulated."
    i """
    I still\nremember...

    You\nmoved toward\nthe door...

    Then\nstopped.
    """
    scene remu1
    with slowdissolve
    i "And\nslowly..."
    scene remu2
    with slowdissolve
    i "You turned\ntoward me."
    show remu3:
        yalign 0.0
    with slowdissolve
    $ renpy.pause(2)
    show remu3:
        subpixel True
        yalign 0.0
        linear 6.0 yalign 1.0
    $ renpy.pause(6)
    show remu3b:
        yalign 1.0
    with slowdissolve
    i """
    You\nsmiled back\nat me.

    And that became\nthe most\nbeautiful day\nof my life.
    """
    scene isabelle1
    with slowdissolve
    re "You couldn't\nbelieve it,\nhuh?"
    i """
    For\nsomeone\nlike me...

    To be\nloved\nby you...

    I\nreally couldn't,\nyeah.
    """
    i """
    Even when\nyou got away...

    I just\nstood there.

    I don't know\nwhy I've never\ntold you that.

    But...

    Do you think\nour destiny was\nalready set?
    """
    scene love1
    with slowdissolve
    i """
    I've always known\nyou coldn't\nlove me\ncompletely.

    I knew\nyour voice\nwasn't happy.

    But sad,\nevery night.

    And that\nthose\ntears...

    Meant\nyou didn't feel\nthat much.
    """
    scene love2
    with slowdissolve
    i """
    I knew\nyour work\nwas important.

    And that you\npoured\nall yourself\ninto it.

    To me,\nthat couldn't\nmake sense,\nthough.

    And I\nalways thought...

    I\nwas\nmiserable.

    Just like\nyour clients.

    I felt\nterrible.

    And\nin the end...

    I couldn't\nlove you\nlike\nI should have.
    """
    scene love3
    with slowdissolve
    re """
    People\nalways think\nthat...

    People\nlike me\nare\nunhappy.

    I knew you\nthought that,\ntoo.

    Many times\nI tried\nto talk...

    To\nexpress\nmy feelings.

    But you\ncouldn't\nlisten.

    You\ndidn't\nwant to.

    So\nI ran\naway.

    And\ndecided that\nit was you\nwho disappeared.

    Just to\nnot\nsuffer.
    """
    show remu3:
        yalign 1.0
    with slowdissolve
    $ renpy.pause(2)
    show remu3:
        subpixel True
        yalign 1.0
        linear 6.0 yalign 0.0
    $ renpy.pause(6)
    scene remu2b
    with slowdissolve
    $ renpy.pause(2)
    scene remu1b
    with slowdissolve
    $ renpy.pause(2)
    scene morning1
    with slowdissolve
    i "I dreamt\nthat morning..."
    scene morning2
    with slowdissolve
    i "Ever\nsince..."
    scene morning3
    with slowdissolve
    i "The morning\nyou\ntold\nme..."
    scene morning4
    with slowdissolve
    i "How much\nunsatisfied\nyou were."
    scene morning5
    with slowdissolve
    i "And how\nselfish\nI was."
    re "I know..."
    show morning6a:
        yalign 1.0
    with slowdissolve
    re "But\nin\nhere..."
    show morning6:
        yalign 1.0
    with slowdissolve
    show morning6:
        subpixel True
        yalign 1.0
        linear 6.0 yalign 0.0
    $ renpy.pause(6)
    show morning6b:
        yalign 0.0
    with slowdissolve
    re "We can\ngo back."
    scene credits
    with slowdissolve
    $ renpy.pause(30)
    stop sound fadeout(4)
    scene black
    with slowfade
    return
