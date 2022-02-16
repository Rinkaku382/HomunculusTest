
define slowfade = Fade(1.0, 0, 3.0)
define midfade = Fade(1.0, 0, 2.0)
define quickfade = Fade(1.0, 0, 1.0)
define slowerfade = Fade (3.0, 0, 3.0)
define slowdissolve = Dissolve(2.0)
define fadehold = Fade(3.0, 1.0, 3.0)

define config.hard_rollback_limit = 0
define config.menu_include_disabled = True
init:
    image movie = Movie(size=(1920, 1080), xpos=0, ypos=0, xanchor=0, yanchor=0)

$ renpy.music.set_volume(1.1, channel="music")

define i = Character("Isabelle", color="#c45151", what_xpos=255, what_ypos=-450, who_ypos=-550, who_xpos=-14)
define isa = Character("Isabelle", color="#c45151", what_xpos=1675, what_ypos=-450, who_ypos=-550, who_xpos=1400)
define h = Character("Her", color="#5d6f5c", what_xpos=255, what_ypos=-450, who_ypos=-550, who_xpos=12)
define y = Character("Yasu", color="#c6943d", what_xpos=1675, what_ypos=-450, who_ypos=-550, who_xpos=1420)
define c = Character("Claire", color="#5d6f5c", what_xpos=1675, what_ypos=-450, who_ypos=-550, who_xpos=1420)
define s = Character("Stefan", color="#c6943d", what_xpos=1675, what_ypos=-450, who_ypos=-550, who_xpos=1420)
define j = Character("Julie", color="#5d6f5c", what_xpos=1675, what_ypos=-450, who_ypos=-550, who_xpos=1420)
define k = Character("Kim", color="#c6943d", what_xpos=1675, what_ypos=-450, who_ypos=-550, who_xpos=1420)
define t = Character("Takeshi", color="#5d6f5c", what_xpos=1675, what_ypos=-450, who_ypos=-550, who_xpos=1420)
define h = Character("Her", color="#5d6f5c", what_xpos=255, what_ypos=-450, who_ypos=-550, who_xpos=12)
define her = Character("Her", color="#5d6f5c", what_xpos=1675, what_ypos=-450, who_ypos=-550, who_xpos=1425)
define r = Character("Remu", color="#5d6f5c", what_xpos=255, what_ypos=-450, who_ypos=-550, who_xpos=12)
define re = Character("Remu", color="#5d6f5c", what_xpos=1675, what_ypos=-450, who_ypos=-550, who_xpos=1405)

label start:
    $ yasu_comp = False
    $ claire_comp = False
    $ stefan_comp = False
    $ julie_comp = False
    $ kim_comp = False
    $ takeshi_comp = False
    $ stories_comp = 0
    scene black
    with slowfade
    scene diary
    with slowfade
    """
    Homunculus Hotel...

    A place in which\npeople find refuge from the world's dangers and uncertainties.

    They get here in order to find a place that could be safe,\none that could help them get better.

    That's why all the rooms are always occupied by someone.

    And you can see them, walking through the corridors\nor having a lonely breakfast.

    Passing by the courtyard...each of them alone.

    Why I came to this hotel...

    Well, because someone told me that\nthe rooms can show the guests' personal and intimate dreams.

    Dreams from the past.\nDreams of possible and multiple futures.\nDreams of fears or desired achievements.

    But it's not so simple to understand them, right?

    We can't always fully interpret our own dreams...

    And that's my job, helping others in understanding the dreams that their rooms show.

    The first day I spent here seems so far away, now.

    I entered as a guest, but then, since I\ncouldn't see anything in my room, I got employed as a helper.

    Maybe because of this job, mine has become a solitary existence.

    I get to talk with lots of people during the day,\nsince my schedule is filled with meetings.

    But then, in evenings such as this one,\nI find myself alone in my room.

    And, unable to resist to the forceful waves of memories,\nI just let myself go...

    And yearn for you,\nfor your company.
    """
    stop music fadeout(2)
    scene black
    with slowerfade
    play music "toherenevercome.ogg" fadein(2)
    $ renpy.pause(0.5)
    play movie "intro1.ogv" loop
    show movie with slowdissolve
    h """
    Isabelle...

    Isn't\nthis sky\nbeautiful?
    """
    isa """
    Hmmm\nit's ok,\nI guess.
    """
    h """
    You\ncan't see it,\nhuh?

    The shades\nof blue.

    The clouds\ngently floating.

    Oh,\nlook!

    There's\na butterfly flying\nover there!

    I envy them\na lot,\nyou know?

    I'd like to be\nas free\nas they are.

    Flying\nall around.

    Free to be\nas I am.

    Hmmm...

    When I\nlook around\nmyself...

    I realize that\nno one\nis free.

    We are\ncocoons\nwalking around.

    Unaware of\nwhat or who\nwe could be.

    We accept\nwhat is more\ncomfortable.

    And avoid\nour dreams.

    But it's not\nour fault.

    The world\nis changing\nfor the worst.

    And it builds\nmore and more\ntraps...

    To convince us\nthat a good wage\nis enough to\nbe happy.

    That a good job\ncan make us\nenjoy life.

    And,\nby believing\nthis lie,\nwe kill ourselves.

    This is\nthe true suicide,\nfor me.

    I wish\nwe could live\nthrough this sky,\nthrough our dreams.
    """
    stop music fadeout(2)
    jump segment1

######## START OF SEGMENT 1 #########################################################################################

label segment1:
    play music "intro.ogg" fadein(3)
    scene desk
    with slowdissolve
    stop movie
    """
    Oh...

    Our time together still appears so clear to me.

    When we met, when we were together, when we left each other.

    Those events still affect me.

    And, then, just when that sceneries look clearer,\nthey suddenly fade into this hotel room.

    Ironic, though...

    I've helped a lot of people,\nbut I'm totally unable to see my dream.

    I'm unable to help myself.

    And memories are now tormenting me.

    A torture that seems endless, in nights such as this...

    So I give up.

    Whenever I look at all these items in my room,\nI feel different moments coming up to me.

    They knock on my door,\nand I reject them.

    Because I fear that pain,\nthe pain of remembering.

    But...enough of that.

    I feel like I've been\nholding myself for too long, now.

    Tonight I just want to try and remember harder.

    I want to clearly focus on my past,\nand deeply explore it.

    Can thinking about the people I've met and helped help me?
    """
    jump deskscreenintro
label deskscreenintro:
    call screen deskintro
label flowerintro:
    """
    These flowers always reminds me that...

    We used to fill our home with them.

    And every morning, after breakfast, we tended to them.

    It's only because of you that\nI try to keep these alive so hard.

    And, somehow, that gives me strength.
    """
    jump deskscreenintro
label calendarintro:
    """
    Time passes.

    Days go by.

    Here, on this calendar, the appointments of last month are all marked.

    All these people...

    All their dreams...

    Marked on paper and into my memories, indelible.

    Yasu and Claire, on the first floor.

    Julie and Stefan, who occupy the second.

    Kim and Takeshi, on the third.

    Most of them have been my patients for a long time...

    While others have merely been a fleeting encounter.

    But regardless, they've all been very important to me.
    """
    jump deskscreenintro
label mugintro:
    """
    This mug is so old...

    It's one of the few things I managed to bring here with me.

    And it brings back the sweet memories of our breakfasts together.

    I miss those mornings so much...

    Sometimes I even childlishly ask myself:\nwill they ever come back?
    """
    jump deskscreenintro
label photosintro:
    """
    I used to make lots of photos, here in the hotel.

    Every time I look at them, I'm reminded of\nthe most beautiful moments and friends I have encountered here.

    Most of the people I took pictures of aren't here anymore.

    But they still smile so happily and live through these images.

    I guess this is what I've been searching through photography:\nto make people everlasting.

    Have I succeeded?\nI guess so.

    And maybe that's why I stopped.
    """
    jump deskscreenintro
label booksintro:
    if claire_comp == True:
        """
        All these books...

        I'll never grow a collection as huge as Claire's...\nbut it's nice to always remember that we shared an interest.

        I hope she's still reading, wherever she is now.
        """
        jump deskscreenintro
    if claire_comp == False:
        """
        Some books and graphic novels that I really care about.

        The hotel's delivery service is very useful, I'd say.

        Without it I would have died of boredom.

        All these books, words, thoughts remind me of...

        Claire.

        She used to read a lot, everyday,\nas she was working on her various projects.

        She was a hunter, constantly on the search for new ideas and images.

        Of all the memories I have of her,\nthere is one I hold dearly.

        The last morning I saw her.
        """
        jump day2
label lampintro:
    if yasu_comp == True:
        """
        This lamp always reminds me of Yasu's light.

        Not only the one in his room,\nbut also his inner light.

        We all have one, inside of us.

        For some it shines brighter,\nfor others it's dimmer.

        But that's what makes as humans.

        And his reflected the spirit of a wonderful human being.

        I truly hope he is with his wife, now...
        """
        jump deskscreenintro
    if yasu_comp == False:
        """
        Just a normal lamp,\n with the hotel's name written in gold on its base.

        Its light is perfect:\nnot too strong, and not too weak.

        It's soothing, warm, comforting.

        Now that I think about it...\nYasu, from the first floor, had the best light in the entire hotel.

        The vastness of the field...

        The sweet sound of the wind...

        And Yasu's gaze as he observed the horizon...
        """
        jump day1
label diaryintro:
    if claire_comp == False or yasu_comp == False:
        """
        It's too soon to write today's entry...
        """
        jump deskscreenintro
    if claire_comp == True and yasu_comp == True:
        """
        Do I really want to go to sleep already?
        """
        menu:
            "Yes.":
                scene diary
                with slowfade
                """
                Since I came here, each day has had the same routine...

                Wake up.

                Let the day flow.

                Get back to the room.

                But, now that I think about it...\nthings weren't any different before.

                Thanks to Yasu and Claire,though,\nI remembered that repetition can mean peace.

                A peaceful existence...

                One that doesn't look for the excitement of continuous events\nbut that enjoys the stillness of and dedication to personal thoughts and perseveration.

                When I think about my life before arriving in the hotel, or even my life as a whole...

                I realize how much all these elements have been estranged to me\nby a life wasted in honour of a business company that didn't reflect me.

                And now I'm welcoming them into the house that my mind is.

                And, once again, I lose myself into reveries about you...
                """
                stop music fadeout(2)
                scene black
                with slowerfade
                play music "toherenevercome.ogg" fadein(2)
                $ renpy.pause(0.5)
                play movie "intro1.ogv" loop
                show movie with slowdissolve
                isa """
                You\nknow\nwhat?
                """
                h "Hmm?"
                isa """
                I love\nhaving breakfast\nwith you.

                It feels so...\npeaceful,\nfor once."""
                h """
                What do you mean?
                """
                isa """
                Well,\nyou know...

                Lately\nit's been\npretty stressful.
                """
                play movie "intro2.ogv" loop
                show movie with dissolve
                h "Do you\nsay that\nbecause of me?"
                isa """
                No,\nit's just...

                You've been\nfeeling down\nand i'm worried\nfor you.
                """
                h """
                You\ndon't have\nto be.

                It's\nnot your fault\nafter all.

                I'm just...\nso tired.
                """
                scene intro3
                with slowdissolve
                stop movie
                isa "I know,\nbut you are\nso miserable..."
                h """
                Please\ndon't pity me.

                I get\nenough of that\nat work.
                """
                isa """
                Then maybe...

                You should\ndo something\ndifferent.
                """
                h """
                ...what?

                Is this\nwhat it's\nabout?
                """
                scene intro4
                with slowdissolve
                isa """
                I only want\nwhat's best\nfor you,\nyou know that.

                If your job\ndoesn't make you\nhappy,\nthen-
                """
                h """
                Enough.

                I know\nwhat this\nis about.

                After all,\nI don't pretend\nto be understood.
                """
                isa """
                No,\nI understand!

                You know\nI do!

                I\nlove you\nso much!
                """
                jump segment2
            "No.":
                "Maybe I'll take another look around."
                jump deskscreenintro

label day1:
    $ fly = False
    $ shame = False
    $ alone = False
    $ rest = False
    $ nopressure = False
    $ reading = False
    stop music fadeout(2)
    scene black
    with fade
    scene day1
    with slowfade
    $ renpy.pause(3)
    play music "day1.ogg" fadein(2)
    play movie "wakeup.ogv" loop
    show movie with slowdissolve
    """
    I wake up early in the morning with a strange headache,\nas always.

    Not the best way to start the day, I guess...

    The light that comes from the window is soft, pale,\nand my body finds it difficult to get up.

    But it has to.

    I have to.

    So I force myself...

    Lift my body up...

    Pass my hands on my face...

    And get mentally ready for this new day.
    """
    scene corridordog
    with slowfade
    stop movie
    $ dog = False
    $ pet = False
    """
    The first floor's corridor.

    It's been half a year since I started working here...

    I was worried,\nat first.

    The idea of an hotel that offers a support service to the guests still seems...

    Well, strange.

    But I grew confident with it.

    Both with the idea and the job itself.

    I just have to visit and then spend some time with some of them,\nnothing too stressing.

    So here I am now...
    """
    jump floor1_1
label floor1_1:
    if yasu_comp == False:
        call screen floor1_1
    if yasu_comp == True:
        stop music
        scene desk
        with slowfade
        play music "intro.ogg" fadein(3)
        $ renpy.pause(3)
        jump deskscreenintro
label dog1:
    if dog == False:
        $ dog = True
        """
        The director's dog.

        Seems like she was waiting for me.

        Should I pet her?
        """
        menu:
            "Of course!":
                $ pet = True
                "She barks happily!"
            "Not now.":
                $ pet == False
                "She looks disappointed."
        jump floor1_1
    if dog == True and pet == True:
        """
        She barks happily again!
        """
        jump floor1_1
    if dog == True and pet == False:
        "What's done is done."
        jump floor1_1
label portrait1_1:
    """
    A portrait of the hotel's director.

    Always elegant,\nalways radiant.

    She's such a classy woman...

    I wonder how she does it!
    """
    jump floor1_1
label portrait2_1:
    """
    The director is so beautiful in this one!

    Every time I see her tender smile, I get reminded of what elegance is.

    To work and live like that, with elegance...

    I'm so envious.

    I would like to be like that.

    But I constantly feel like I'm too rough.

    But that's ok, I guess.

    In the end, we are who we are.

    And it's enough to be like that:\njust how we are.
    """
    jump floor1_1
label mirror1:
    """
    Me, myself and I.

    A beautiful person...

    Right?
    """
    jump floor1_1
label yasu1:
    if yasu_comp == True:
        """
        Yasu's session is finished.
        """
        jump floor1_1
    if yasu_comp == False:
        stop music fadeout(4)
        scene door101_1
        with slowfade
        $ renpy.pause(1)
        scene door101_2
        with dissolve
        $ renpy.pause(1)
        scene door101_3
        with dissolve
        $ renpy.pause(1)
        scene yasuframe
        with dissolve
        $ renpy.pause(0.5)
        play movie "yasu.ogv" loop
        show movie with slowdissolve
        play music "yasu.ogg" fadein(4)
        """
        As I open the door and enter,\nI find myself in Yasu's vast field.

        He is right there, next to me,\nlooking at the horizon.
        """
        i """
        Hello,\nMr. Yasu.
        """
        menu:
            "How are you today?":
                i "Is\neverything alright,\ntoday?"
                y "Well...\nI'm so-so,\nthanks."
        y """
        I feel a little\nmore tired than usual.

        Anyway...

        I was wondering if\nit was already\ntime for\nour meeting,\nMs. Isabelle.

        Thanks for\ncoming today.
        """
        i """
        There's no need\nto thank me.

        It's my job,\nafter all.
        """
        y """
        I know...

        But I still think\nI should thank you.
        """
        i """
        Don't worry about it,\nit's ok.

        Anyway,\nwhy are you so tired?
        """
        menu:
            "Still up all night?":
                i """
                Still\nup all night?

                Are you\nsleeping well\nlately?
                """
                y """
                Hmm...

                It seems\nI can't fall asleep.

                No matter\nhow hard I try.

                So I just stand here\ndoing...

                Well,\ndoing nothing.

                And the more\nI try to sleep...

                The more\nI can't.

                I realized,\nlately, that I do\nwant to sleep...

                But the scenery\nis too beautiful.
                """
            "What have you been up to?":
                i "What\nhave you been\nup to?"
                y """
                Oh,\njust the usual...

                I look\nat the field...

                And try to catch\nthe differences...

                Between now\nand yesterday.
                """
        y """
        Oh,\nthis reminds me...

        There was a sparrow,\nlast night.

        It was flying\nright above my head.

        And\nstrangely\nit never\nreached land...

        He just flew\nover my head\nfor a while.

        And then,\njust as it arrived,\nit disappeared.

        What could it mean?
        """
        menu:
            "Maybe you wish to fly away?":
                $ fly = True
                i "Maybe you\nwish to\nfly away?"
                y """
                Hmmm...

                Well,\nI can't say\nI never\nwished I could...

                But\nto dream about it\nseems...

                A little too specific.

                I don't think I've been\nmuch into that,\nlately.

                It's a dream\nfrom my past.

                From when\nI was still a child.

                And, you know...

                When you look\noutside a window\nat that age...

                You just wish\nyou could\nbe outside.

                Flying in the sky.

                But then\nwhen you get older...

                The earth becomes\nyour world.

                The soil\nis where you feel\nmore comfortable.

                And the sky\ngets distant.

                That's how\nI feel about it.

                This\nreminds me of\nmy childhood.

                So much time\nhas passed.

                I'm sixty,\nnow.

                And I have\nso many\nthing on my back...

                Projects,\npeople,\nfailures.

                But now,\nthis peace...

                Hmmm...

                I'll tell you\na little\nstory.

                When I was\nten years old\n...

                I usually\nplayed with some\nfriends from the\nstreet.

                We had\ndifferent ages,\nbackgrounds,\nfamilies.

                But still,\nwe were all\nclose friends.

                I still\ndon't know\nhow it was\npossible.

                Usually people,\nexpecially kids,\ncare a lot\nabout differences.

                If you have\nmore money\nthan me,\nI'm entitled to\nhate you.

                If you have\ndifferent skin\nthan me,\nI'm entitled to\nhate you.

                And if\nyou have someone\nwho loves you\nbut I don't...

                I'm even more\nentitled to\nhate you.

                That's how\nhumanity seems\nto work.

                Anyway,\nwe used to play\nall together.

                We shared\nour childhood\njust like that:\n playing.

                Our studies\nalways came\nafter.

                And we all\nhad different\ndreams.

                For some years\nI had the\ndream of flying.

                But...

                It was\nsomeone else\nwho pursued it.

                One of us\nwas a very\npoetic boy.

                He used\nto write\nshort poems,\nyou know?

                I always had\npure admiration\nfor him.

                I expressed\nmyself in\nother ways,\nbut...

                Poems\nattracted\nme.

                And his poems\nwere beautiful.

                But\nwhat I mean\nwhen I say...

                That he\npursued the\ndream of flying\nis...

                Well,\nI see flying\nas a way\nto escape.

                Escape from...

                I don't know,\nwhatever\nbad situation\nyou are in.

                And he\nmade it.

                By following\nhis love\nfor literature...

                He\nelevated himself\nabove\neveryone else.

                And so\nhe was able\nto escape.

                He became\na novelist.

                With\nhis novels\nhe tried to \nchange humanity.

                And I...

                Had nothing\nbut\nblind admiration.

                I\ntried to do\nthe same thing,\nbut...

                I guess\nI'll never know\nif I succeeded\nor not.

                But,\nyou know,\nit's ok.

                There are\nmany artists\nwho...

                Never saw\ntheir work\nbeing spread\naround the world.

                It's sad...

                But...

                Is the result\nmore important than\nthe fight itself,\nI wonder...
                """
                menu:
                    "Something tells me you succeeded.":
                        i """
                        Something\ntells me\nyou succeeded.

                        You are a\nstrongwilled and\ngood man.
                        """
                        y """
                        Who knows...

                        Our world\nis brutal,\nIsabelle.

                        No matter\nhow much\nyou fight.

                        No matter\nhow many tears\nyou shed.

                        The world\nwon't be gentle\nwith you.

                        But we\nstill have\nto fight.

                        Think about\nthis.

                        When\nyou are\na kid...

                        You spend\nall your time\nplaying.

                        Studying\ncomes after.

                        That's because\nyou only want\nto have fun.

                        But then you\ngrow up.

                        You have\nto study\nto get\ngood grades.

                        You need\ngood grades\nto find\na good job.

                        And\na good job\nto have\na good life.

                        It's a\ndamn struggle.

                        But it's also\nwhy we can't\ndream of flying.

                        We\ncan't aim\nfor the sky\nanymore.

                        We're too busy\nwatching\nthe ground under\nour feet.

                        We aim at\na comfortable\njob.

                        At\na happy family.

                        And at\na peaceful death.

                        During high-school,\nafter the lessons...

                        I used to see\na group of bankers.

                        Their backs\nwere\nso stooped...

                        And I\nunderstood that life\nis difficult\nfor everyone.

                        And\nit doesn't matter\nwhat you aim at.

                        You'll have\nto struggle\nin any case.
                        """
            "Are there thoughts that still haunt you?":
                $ shame = True
                i """
                Are there\nthoughts\nthat still haunt\nyou?
                """
                y """
                Sometimes\nI wonder...

                How is\nmy family doing?

                And what about\nmy friends?

                So much time\nhas passed,\nsince the last time\nI saw them all...

                It still feels selfish,\nto be here.

                And yet,\nI feel good.

                Like never before,\nyou know?

                Do you think...

                I should be ashamed\nfor feeling\nso happy here?
                """
                menu:
                    "Why should you?":
                        i """
                        Don't you think\nyou're exaggerating\nit a little?

                        Why\nshould you\nfeel ashamed?
                        """
                        y """
                        I got\nthe easy way out.

                        Out of the problems.

                        Of any\npainful situation\nthat life brings.

                        But not them.

                        They're still\nwhere I left them.

                        And...

                        It feels\nas if I ran away.
                        """
                        menu:
                            "Only you have the answer for that question.":
                                i """
                                Only you have\nthe answer for\nthat question.

                                Though I know\nhow difficult it\ncan be to\nunderstand that...
                                """
                                y "Probably, yeah..."
                            "It's not your fault for ending up in here.":
                                i """
                                It's not\nyour fault for\nending up\nin here.

                                It just\nhappens,\nwether we\nchoose it\nor not.
                                """
                                y """
                                I know, but...

                                Sometimes...

                                I wonder if things\ncould have been\ndifferent.
                                """
                        y """
                        Uhm...

                        ...

                        I'm trying to\nfocus on the shame\nI'm feeling.

                        To understand it.

                        To analyze it.

                        And yet,\nI still feel bad.

                        I still feel\nit's not right\nto be here.

                        Going away\nso abruptly...

                        Suddenly...

                        It feels\nlike a crime.

                        And I wonder...

                        Why do we all have\nto go like that?

                        It's unfair.

                        But the more\nI think about this...

                        The more this peace\nseems to affect me.

                        I remember...

                        My wife\nwas always\nvery quiet.

                        And she was\na painter.

                        She used to paint\nall day,\nevery day.

                        She said that\npainting all day\nmeans constantly\ngetting better.

                        And indeed\nshe got better\neach day.

                        In the beginning,\nshe worked\nin an office.

                        And meanwhile\nshe kept painting,\nevery evening.

                        She didn't accept\nany kind\nof advice.

                        And any kind\nof appreciation.

                        For her,\nnothing was ever\ngood enough.

                        She didn't want\nto be the best...

                        But she wanted\nto portray\nwhat she felt.

                        What\nshe couldn't express\nwith words.

                        And so,\nafter one year,\nshe\nabandoned her job.

                        People thought\nshe had gone mad.

                        Many of our friends\nasked me\nto talk to her.

                        Both our families\nwere worried\nand asked me\nto make her think\nabout it.

                        But I trusted her.

                        I knew\nshe\nwasn't stupid.

                        And she wasn't\ncrazy at all.

                        She\njust wanted\nto live freely.

                        And,\nafter some time,\nher paintings\nattracted many critics.

                        Her efforts paid out.

                        And people\nchanged their minds\nabout her.

                        She\nfound her peace.

                        And finally\nfound happiness.

                        Maybe\nshe passed through\nthe same sensations\nI'm having.

                        Maybe,\nif I looked better\nat her paintings\nI would have\nunderstood better.

                        We were happy,\nbut...

                        Now that I'm here\nI wonder\nwhat she's thinking.

                        If she\nmade some paintings\nabout me.

                        If I\nwill ever\nsee them.
                        """
                        menu:
                            "What kind of paintings she used to paint?":
                                i """
                                Oh,\nan artist!

                                And what kind\nof paintings\nshe used to\npaint?
                                """
                                y """
                                Sometimes\nabstracts.

                                Other times\nstill lives.

                                It depended\nby the feelings.

                                That's why\nI'm curious.

                                But,\nknowing her,\nI'm sure she just\npainted a hat.
                                """
            "It could mean that you feel alone.":
                $ alone = True
                i """
                Maybe...

                It means that\nyou feel\nalone?
                """
                y """
                Alone...?

                I can't say\nthis place is lively.

                But...

                In a way,\nI don't feel alone.

                There's peace\nin here.

                So I'm ok\nwith the loneliness.

                It's as if,\nfor the first time...

                I'm at peace\nwith the world.

                Have you ever\nfelt like that?
                """
                menu:
                    "Maybe sometime.":
                        i "Sometimes\nmaybe,\nyes."
                        y """
                        Well, in any case...

                        It's true\nthat I'm alone.

                        But it's also true\nthat you\ncome here often.

                        So you lift\nthat loneliness\na little.

                        This hotel makes\neveryone lonely.

                        Even when\nI go out\nfrom the room...

                        I find it\ndifficult to talk\nwith others.

                        If I meet\nanyone at all.

                        So I prefer\nto stay here...

                        By myself.

                        But I don't\nfeel bad.

                        It's so peaceful...
                        """
        y """
        Hmmm...

        How can I\nexplain it...

        Have you ever\nfelt like...

        Like you're\na floating weed?

        You know...

        Calmly floating\non a pond's\nsurface.
        """
        menu:
            "Often.":
                i """
                Yes...

                Very often.
                """
                y """
                You must have\nbeen very free,\nthen!

                That's good...
                """
                menu:
                    "Is it related to something?":
                        i "Is it related\nto something,\nanyway?"
                        y """
                        Nothing in particular,\nno.

                        It's just the way\nI'm feeling.

                        I'm starting\nto realize that...

                        All my life\nhas been\n just like that.

                        A floating weed...

                        Gently swept away\nby the current.
                        """
                    "Have you dreamt of floating weeds?":
                        i "...have you dreamt\nof floating weeds?"
                        y """
                        Oh,\nno!

                        Only the field,\nas usual.

                        But I got\nthis image\n in my mind.
                        """
            "What do you mean?":
                i """
                Im not sure\nI follow you...

                What\ndo you\nmean?
                """
                y """
                You see...

                I've been\nbetween freedom\nand slavery...

                For all my life.

                A slave,\nas I had to\nwork for a company.

                But free,\nas I could do what\nI wanted anyway.
                """
            "Never.":
                i """
                No,\nnever.

                I'm sorry.
                """
                y """
                Well,\nthat's a pity,\nbut...

                You know.

                Never\nsay\nnever.
                """
                menu:
                    "What's with the floating weeds?":
                        i """
                        But what's with\nthe floating weeds?

                        What\ndo they\nmean?
                        """
                        y """
                        Well...
                        """
                    "Is that how you feel today?":
                        i "Is that\nthe way\nyou're feeling?"
                        y """
                        Yes,\nlooks like it.

                        I'm starting\nto understand\nthis peacefulness.

                        And that's why\nthis image popped\ninto my mind.
                        """
        y """
        For me,\na floating weed is...

        Someone that\ncan live between\nfreedom and slavery.

        Peacefully.

        Someone\ntied to earth\nand yet\nfloating on water.
        """
        menu:
            "It's a very peaceful image, indeed.":
                i """
                Oh,\nI get it!

                It's a\nvery peaceful image,\nindeed.
                """
                y """
                Yes.

                And yet...

                Something\ntroubles me.
                """
            "Yet, you dream of a field...":
                i """
                Yet,\nyou dream of\na field...

                Do you think\nthese two things\nare connected?
                """
                y """
                Maybe...

                I still feel\nthe past.

                No matter\nhow much time\nI spend here...

                It still haunts me.
                """
        y """
        But the more\nI explore myself...

        The more\nthis sensation\nabandons me.
        """
        i """
        Maybe you only have to accept it...

        And let it go,\nso that peace\nmay come.
        """
        y """
        Yes.

        I'm now\nsure\nof this.

        It's...

        Strange.

        Thinking about\nall these memories...

        Made me\nfeel better.

        Way better,\nthanks to your help.

        The thoughts\nare\nslowly\ndisappearing.

        In the end...

        It's useless\nto feel bad.

        I can't turn\ntime back.

        So I might\nas well\nmove on.

        And find\nmy own\npeace.

        So...

        I think\nI'm ready.
        """
        scene yasu
        with slowdissolve
        stop movie
        menu:
            "Are you sure?":
                i """
                ...really?

                Are\nyou\nsure?
                """
                y """
                Yes.

                I\nfinally\nam.

                I want to\nmove beyond.

                You see?

                The field\nis still.

                No wind.

                Not today.
                """
                scene yasuend
                with slowdissolve
                y """
                I was just\nwaiting\nfor you.

                To say\ngoodbye\nproperly.

                To tell\nyou\nhow I feel.

                And to\nthank you\nonce again.

                So...

                Thank you,\nIsabelle.

                For all\nthe help.

                And...

                I hope you'll\nfind your dream\nsoon.
                """
        $ yasu_comp = True
        $ stories_comp += 1
        stop music fadeout(2)
        scene corridordog
        with slowerfade
        stop movie
        play music "day1.ogg" fadein(2)
        jump floor1_1
label claire1:
    if claire_comp == True:
        """
        She's not here anymore...
        """
        jump floor1_1
    if claire_comp == False:
        """
        Room 102...

        It's occupied by Claire\nbut she's not here, now.

        Probably, she's wandering through the hotel,\ntalking with whoever she sees!
        """
        jump floor1_1

label day2:
    $ discover = False
    $ walone = False
    $ dream = False
    $ guests = False
    $ sdifferent = False
    stop music fadeout(2)
    scene black
    with fade
    #scene day2
    #with quickfade
    $ renpy.pause(3)
    play movie "breakfast.ogv" loop
    show movie with slowdissolve
    play music "day1.ogg" fadein(2)
    """
    Hmm...

    Today seems like it could be a good day.

    I woke up with your face in my mind, so I'm sure I dreamt of you.

    Well, I hope I did, actually.

    But anyway...

    I'm thinking of you, this morning.

    And when I think about you...

    I always feel a mixture of happiness and melancholy.

    And somehow the day feels less heavy.
    """
    scene corridor
    with slowfade
    stop movie
    """
    Today the first floor is empty.

    Usually the director's dog is here,\nbut maybe today she's with her.

    Also, no guests around.

    It's so lonesome...
    """
    jump floor1_2
label floor1_2:
    if claire_comp == False:
        call screen floor1_2
    if claire_comp == True:
        stop music
        scene desk
        with slowfade
        play music "intro.ogg" fadein(3)
        $ renpy.pause(3)
        jump deskscreenintro
label portrait1_2:
    """
    This portrait has been here since...

    Well, since forever.

    I still remember my surprise\nwhen I first saw it!

    For an instant...\nI fell in love with her.

    Well, maybe I still am a bit infatuated...?

    I mean...she's too beautiful!
    """
    jump floor1_2
label portrait2_2:
    """
    I remember who took this photo...

    Some years ago there was a famous photographer here in the hotel.

    And I also remember he had an affair with the director herself.

    Hmmm...

    I always had a strange interest in gossip.

    Too bad there's not much of it anymore.
    """
    jump floor1_2
label mirror2:
    """
    It's me!

    Wait, are those new wrinkles?

    Ugh.
    """
    jump floor1_2
label yasu2:
    if yasu_comp = True:
        "He's not here anymore..."
    if yasu_comp = False:
        """
        Room 101...

        It's occupied by Yasu.

        He's not here, now,\nhe's probably on his daily stroll around the hotel's courtyard.

        Sometimes the rooms are too much to bear,\nso guests try to take a pause from their dream.

        I really can't blame them.

        This job, after all, is for me a pause from my memories.
        """
        jump floor1_2
label claire2:
    if claire_comp == True:
        """
        Claire's session is finished.

        I should check the other door.
        """
        jump floor1_2
    if claire_comp == False:
        stop music fadeout(4)
        scene door102_1
        with slowfade
        $ renpy.pause(1)
        scene door102_2
        with dissolve
        $ renpy.pause(1)
        scene door102_3
        with dissolve
        $ renpy.pause(1)
        scene claireframe
        with dissolve
        $ renpy.pause(0.5)
        play movie "claire.ogv" loop
        show movie with slowdissolve
        play music "claire.ogg" fadein(4)
        """
        The film stocks, books and notebooks that fill Claire's room seem to be increased.

        Her room has never been orderly, but...

        Now it's worse than it ever was.
        """
        i """
        Good morning,\nClaire.
        """
        menu:
            "How are you today?":
                i """
                How are\nyou today?

                How is it\ngoing with\nthe project?
                """
                c """
                Oh, Isabelle...

                It's terrible...

                Terrible!!

                I can't work...

                I can't even\nwrite a single line...

                Look at this.

                I only wrote\nthe notes\nfor the scene.

                Not even\na description\nor a dialogue!

                I just wrote...

                'Maria's house,\ninterior - afternoon'\nbut then?

                What could\nhappen?

                I don't know!

                I can't concentrate\nat all...
                """
        menu:
            "Is something distracting you?":
                i """
                What's the\nmatter?

                Is something\ndistracting\nyou?
                """
                c """
                I don't know!

                Hmm, maybe...

                But I can't even\nunderstand what.
                """
            "You always work so much...":
                i """
                You always\nwork\nso much...

                Why don't you\nrest\na little?
                """
                c """
                I can't!

                Don't you\nunderstand?

                I'm in the middle\nof the project.

                I can't rest now!

                I'll rest\nwhen I'm dead!

                Oh...

                Well...
                """
        menu:
            "What about your dream, though?":
                i """
                What about\nyour dream,\nthough?

                Have you seen\nanything particular,\nlately?
                """
                c """
                Hmm.

                It's strange...

                I don't think\nI dreamed at all,\nlately.
                """
                i "You sure?"
                menu:
                    "It's ok if you don't want to talk about it, though.":
                        i """
                        You know I\ndon't want to\nintrude\ntoo much.

                        I'm\njust\nworried.

                        It's ok if\nyou don't want\nto talk about\nit,\nthough.
                        """
                        c """
                        I'm still not ready,\nsorry...

                        But please,\ncould you stay here?

                        I think\nI need\nsome company...
                        """
                    "You know the room doesn't lie.":
                        i """
                        You know\nthe room\ndoesn't\nlie.

                        So please,\njust talk\nabout it.
                        """
                        c """
                        Ok,\nfine...

                        I did,\nof course.

                        Nothing new though,\nreally.

                        Just the usual thing.

                        Tons of projects that\nneed to be started...

                        Or finished.

                        But this one...

                        It's killing me.
                        """
            "What are you up to, today?":
                i """
                So, what\nare you up to,\ntoday?

                Something\nexciting?
                """
                c """
                Nothing much.

                Just working\non a scene.

                Or at least\nI'm trying.
                """
                menu:
                    "Is it an important scene?":
                        i """
                        Is it\nan important\nscene?

                        And what's\nthe issue\nwith it?
                        """
                        c """
                        Yes, it is.

                        But...

                        Well, I can't seem\nto be able to\nclose it.

                        I keep\ngetting stuck.
                        """
                    "You never told me about the whole project, though!":
                        i """
                        You never\ntold me about\nthe whole project,\nthough!

                        What is it\nabout?
                        """
                        c """
                        Yes,\nI know...

                        But\nit's because...

                        Well,\nI'm still very unsure.
                        """
                        menu:
                            "What are you unsure about?":
                                i """
                                What are you\nunsure\nabout?

                                What\nworries\nyou?
                                """
                                c """
                                I just don't feel\nconfident enough.

                                I try to work\nand get stuck.

                                I try to distract myself\nand still think\nabout it.

                                I don't\nknow what to do\nanymore.
                                """
        c """
        ...

        Tell me,\nIsabelle...

        Have you ever\nfound yourself...

        Blocked?
        """
        menu:
            "What do you mean?":
                i "What\ndo you\nmean?"
                c """
                In your job.

                Like...

                No matter\nhow much you try,\nyou can't do it well.

                I don't know,\nI feel just like that...

                Blocked.

                What should I do?
                """
        menu:
            "You should take a pause and rest.":
                i """
                I think...

                You should\ntake a pause\nand rest.
                """
                $ rest = True
                c """
                It's difficult, but...

                I'll try, thanks.
                """
            "Don't pressure yourself too much.":
                i """
                Just...

                Don't pressure\nyourself\ntoo much.

                Life is\nalready heavy\nby itself...

                It gets worse\nif we're hard\nwith ourselves.
                """
                $ nopressure = True
                c """
                I know, but...

                I want to finish\nthis piece so much.

                Hmm...
                """
        c """
        I'm trying\neverything\nI can!

        I have even\nstarted reading\na new book!

        Have you ever read\nSoul Mountain?

        It's a novel\nwritten by\nGao Xingjian.

        I've known him\nfor years...

        And yet,\nI never read anything\nhe made until now.

        You know...

        The story\nof this character\ntravelling to \nfind himself...

        Somehow\nI can relate to him.

        I don't know\nhow to explain it...

        It's difficult\nto use words,\nbut...

        This novel\ntouches my heart.

        Here, let me\nread you\na passage...

        'Sitting at rest\nknow not to discuss\nthe shortcomings\nof other people'

        'Setting out\non a journey\nfully appreciate\nthe beauty of\nthe dragon river.'

        At some point,\nit also gave me\nsome ideas\nfor a passage!

        Do you want\nto hear what\nI wrote?
        """
        menu:
            "Yes, I'd be glad to!":
                i """
                Of course!

                I'd be\nglad.
                """
                c """
                Great!

                So...

                It's the scene where\nthe protagonist\nenters in\nthe dinner room.

                She looks around,\nstudies the people\nin the room...

                And as she realize\nthey all hate her,\nshe...

                Well,\nthat's all.

                For now,\nat least.

                I'm writing\nvery little,\nlately.
                """
            "I'm more interested in the process.":
                i """
                Hmm, no...

                I'm\nmore interested\nin the process.
                """
                c "The process?"
                i """
                Yes...

                How you're\ndeveloping\nthe project.
                """
                c """
                Hmmm...

                I don't make\nmuch planning,\nthese days.

                I just\nfollow\nmy thoughts.

                They're\nlike a stream.

                But, lately...

                It gets\ninterrupted\npretty often.

                And easily.
                """
        menu:
            "Has it ever happened before?":
                i """
                And...

                Has it\never happened\nbefore?
                """
                c """
                No.

                Well,\nto be honest...

                I don't remember\nthat well.

                Maybe it did.

                But that doesn't\nchange anything.

                I still don't know\nwhat to do.

                I can't help\nbut think that\nI can't make it.

                Not alone\nat least.
                """
                menu:
                    "So you think that with others you could?":
                        i """
                        Oh,\nwait!

                        So you think\nthat with others\nyou could?

                        Is this\nwhat you mean?
                        """
                        c """
                        Hmm...

                        I can't make\na movie by myself.

                        I need the\nhelp of others.

                        I need to\nwork with other\npeople.
                        """
                        menu:
                            "You could ask the other guests!":
                                $ guests = True
                                i """
                                But...

                                You could ask\nthe other\nguests!

                                What do you\nthink\nabout it?
                                """
                                c """
                                The other guests...

                                Well\nthat's not a bad idea!

                                You know,\nI...

                                I could try,\nyes!

                                Oh...

                                I don't remember\nif I already\ntold you this story,\nbut...

                                I want\nto tell you\nabout a friend\nof mine.

                                An\nold and dear\nfriend.

                                We knew each other\nso well...

                                We used to make\nvery personal movies\ntogether.

                                And struggled\nagainst\nproducers and labels.

                                Getting even a\nsmall amount\nof funds\nalways seemed\nimpossible.

                                At that time\nI had\nso many ideas...

                                As if\nhaving no money\nonly got me\nstronger.

                                I wanted to spit\non each producer's\nface.

                                To each 'no'\nI answered\nwith a curse.

                                I\ncouldn't care less\nabout\ntheir opinions.

                                About their\nmarket analysis.

                                About their\naudience.

                                They used to say...

                                'The public\nlikes this,\nso we need\nto make it.'

                                But...

                                I didn't like\nthe idea of being\nan\ninsincere director.

                                I wanted\nto be\nme.

                                So,\nwith this\nfriend of mine...

                                We made\nwhat\nwe wanted\nto make.

                                The length\ndidn't matter.

                                The format\ndidn't matter.

                                The genre\ndidn't matter.

                                And when we\ncouldn't find actors,\nwe played\nthe characters\nourselves.

                                We had\ntons and tons\nof projects.

                                My entire house\nwas filled\nwith screenplays.

                                I miss\nthat time\nso much...

                                Maybe\nwhat I miss\nis love?

                                Maybe\nit was love\nwhat inspired me...
                                """
                            "Why don't you make something different, then?":
                                $ sdifferent = True
                                i """
                                Why\ndon't you make\nsomething different,\nthen?

                                Like a novel,\nfor example.
                                """
                                c """
                                I don't know...

                                I made movies\nall my life.

                                I don't know\nif I'd be\ncapable.

                                And I think\nthat people should\nstick to\ntheir occupations.

                                If you're\na director\nyou direct.

                                If you're\na writer,\nyou write.

                                But\nmaybe...

                                Maybe it\ndoesn't have to\nbe like that.

                                I'll\nthink about it\nI guess...
                                """
                    "What's worrying you?":
                        i "What's\nworrying\nyou?"
                        c """
                        You know,\nIsabelle...

                        Projects used to\nmake me happy.

                        Being involved in\nsomething greater...

                        Seeing people\nsmile or cry...

                        In front of what\nI had created...

                        It all gives you\na different\nperspective\non things.

                        You even get\nto think\nyou have a gift.

                        Or that you matter\nand have a place\nin the world.

                        But now...

                        Now that I can't\nmake anything...

                        I wonder if\nI deserved\nthat place...

                        And also...

                        What's the point\nin working\non projects\nwithout a crew?

                        It just doesn't\nmake sense.
                        """
                        menu:
                            "Working alone could be an interesting challenge.":
                                i """
                                Well...

                                Working alone\ncould be an\ninteresting\nchallenge.

                                Don't\nyou\nthink?
                                """
                                c """
                                Well, yeah,\nmaybe it could...

                                But then,\nthis sense of\nloneliness\nwouldn't go away.

                                I miss the people\nI once worked with.

                                But,\nat the same time...

                                Yes,\nit could be\ninteresting.

                                As a\npersonal challenge,\nI mean.

                                But...

                                Do you think\nit would be useful?
                                """
                                menu:
                                    "It's up to you to discover that.":
                                        $ discover = True
                                        i "It's\nup to you to\ndiscover that."
                                        c """
                                        I don't know...

                                        I'm not sure\nif I want to take\na risk so big.

                                        I could feel worse\nthan before...
                                        """
                                        i """
                                        You only\nhave to\ntry.
                                        """
                                    "Why don't you try and see what happens?":
                                        $ walone = True
                                        i """
                                        Why don't you\ntry and see\nwhat happens?

                                        You\ncould have a\ngreat surprise!
                                        """
                                        c """
                                        Well,\nif you say so...

                                        I guess trying\nwon't hurt that much.
                                        """
                                    "I think you should confront your dream. ":
                                        $ dream = True
                                        i """
                                        I know it's\ndifficult,\nbut...

                                        I think you\nshould confront\nyour dream.
                                        """
                                        c """
                                        Isabelle,\nplease.

                                        I already told you\nI don't want to.

                                        So please,\ndon't talk about it.

                                        Anymore.
                                        """
                                        i "You're right,\nsorry."
        c """
        But\nanyway...

        You know...

        I'm sorry\nif I\ndon't talk about\nmy dreams...

        I have\na bad relationship\nwith them.

        Since\nI was little...

        I feared dreams.
        """
        menu:
            "Why?":
                i """
                Why?

                What is it\nthat frightens\nyou?
                """
                c """
                Hmm...

                Ever since\nI was born,\npeople used to say\nthat it's useless\nto chase dreams.

                That\nif you do that\nyou'll end up\nwith nothing.

                I tried\nto go\nagainst that.

                To chase mine,\neven though\nI wasn't sure.

                I made\nthe films\nI wanted to make.

                I forced myself\nto believe in them.

                But eventually...

                Everyone\nends up\nabandoning them.

                And I stopped\nchasing mine.

                I put\nmy abilities\ninto labels.

                I started\ntrusting\nproducers.

                I wasn't\nthe person\nI used to be\nanymore.

                I lost\nthe love\nof my life.

                And the job\nof my life.

                So,\nnow...

                Now\nI want to take\nthe old me\nback.

                That's why\nmaking this project\nis so important.

                And why\nnot being able\nto work\nhurts me.

                But...

                Well...

                I'm sorry,\nI know it's sad.

                I always\ntry to...\nsmile.

                But\nthe truth is\nthat I lost\nall my hope.
                """
                menu:
                    "You'll find it.":
                        i """
                        You'll\nfind it.

                        I'm\nsure\nof this.

                        And then\nyouìll be able\nto write\nagain.
                        """
                        c """
                        Thanks,\nIsabelle.

                        Really.
                        """
                    "I'm here for you.":
                        i """
                        I'm here\nfor you.

                        So please,\nstay\nstrong!
                        """
                        c """
                        Thanks,\nIsabelle.

                        Really.
                        """
        if discover == True:
            c """
            Well...

            I'm thinking.

            A lot...

            But I think\nI'll get there,\nyou know?

            Somehow,\nsomeday.

            Maybe\neven sooner\nthan I expect to!
            """
            i """
            I'm happy\nto know that.
            """
        if walone == True:
            c """
            Maybe\nI...

            I could get out early\nin the morning,\nwith only\none camera...

            And just film.

            It doesn't\nmatter what,\nyou know.

            Just film\neverything.

            And maybe\nI'll feel\ngood!

            I'll feel free.

            No schedule.

            No obligations.

            If I want to film\nthe landscape\noutside\nthe window...

            For four hours,\nI can!

            Without\ngiving a fuck,\nyou know.
            """
            i """
            I'm glad,\nClaire.

            It's so nice\nseeing\nyou smile.
            """
            c "Oh,\nthank you\nso much,\nIsabelle!"
        if dream == True:
            c """
            You know,\nfor all this time...

            I've been \navoiding\nmy dream.

            All this\nprojects...

            All this\nmaterial...

            I created\nproblems over\nproblems.

            For nothing.

            I don't have\na schedule,\nanymore.

            I don't have\nany obligations\nneither.

            And yet I let\nmy mind control\neverything.

            Without\nrealizing that\nthis was\nmy dream...

            The absence\nof obligations...

            And complete\nfreedom.
            """
            menu:
                "You can still work on it!":
                    i """
                    Yes!

                    You can\nstill work\non it!
                    """
                    c """
                    Y-yeah...

                    Maybe I can...

                    It will\ntake time,\nbut...

                    I'll be\nable to...

                    Or\nat least\nI\nhope.
                    """
        if guests == True:
            c """
            Hmmm...

            The movie...

            Envision\nthe movie...

            The places,\nthe characters,\nthe light.

            We used to\nlook out for light\ntogether...

            And that...

            I could\nfeel like that\nagain...?

            I could...\nat least try.

            Yes...

            Of course!

            Thank you,\nIsabelle.

            I'm so\nhappy!

            So, so happy!!
            """
        if sdifferent == True:
            c """
            You made me\nremember\nhow much I\nejoyed drawing...

            When I was young,\nyou know.

            So I thought...

            Well,\nwhy not start drawing\nagain?

            And so\nI will just\ntry...

            And finally\nfind some\nmotivation!
            """
        c """
        And...\nwell...
        """
        scene claireend
        with slowdissolve
        stop movie
        c """
        I took\nmy decision.

        And I feel\nit's time.

        I understood\nthat...

        Well,\nthese projects\nwill never\nend.

        As long as\nI go on\nthey'll just...

        Keep\npiling up.

        So...

        It's time\nto focus\non the last one.

        And say\ngoodbye.

        To them\nand to you.

        Thank you.

        You were the\nkindest person.

        I'll hold you\nin my heart.
        """
        $ claire_comp = True
        $ stories_comp += 1
        stop music fadeout(2)
        scene corridor
        with slowerfade
        stop movie
        play music "day1.ogg" fadein(2)
        jump floor1_2

######## START OF SEGMENT 2 #########################################################################################

label segment2:
    scene desknight
    with slowfade
    play music "intro.ogg" fadein(2)
    """
    At one point, we started arguing a lot.

    A struggle was hidden somewhere, everyday.

    There was not only one elefant in the room...

    They filled the whole apartment.

    It's true,\nI could not stand the idea of you doing that kind of job...

    Of you getting involved with different people each night.

    Of you risking your life like that,\njust for your freedom.

    I know you desired it more than anything else, but...\nwas that really worth it?

    Even now, it's difficult for me to think that you didn't suffer.

    But I'm left with no answers...

    I don't know how you truly felt.

    At our beginning together we used to talk a lot,\ndiscussing everything that happened between us.

    Then, through time, we stopped,\nas we got more and more involved with our own things.

    That makes me understand that time really changes people for the worst, sometimes.

    And now I can't do more than remembering and go on through the days.

    Without you...

    ...

    Well...

    Four last items.

    Four last memories.
    """
    jump deskscreen1
label deskscreen1:
    call screen desk1
label flower1:
    """
    Well watered today, too.

    Are you watering yours, I wonder?

    Or...do you even keep flowers, anymore?

    ...are you even still alive?

    Oh God, that's so sad...I can't...
    """
    jump deskscreen1
label calendar1:
    if julie_comp == True:
        """
        Dear Julie...

        Time passes endlessly.

        Sometimes slowly, other times too rapidly.

        And I often can't keep track of it.

        But I hope you can, now.
        """
        jump deskscreen1
    if julie_comp == False:
        """
        Each time I look at the appointments of the month,\nand the names written on the calendar...

        I think about their voices.

        What stories they have to tell,\nwhat lives I can see through their recallings.

        And, among them,\nthe images and words from Julie's first session still ring, heavy.

        Thanks to her discussing her past...\nI often see a light lingering accross the tunnel I'm walking through...
        """
        jump day3
label mug1:
    """
    This mug is so old...

    And every time I drink from it,\nit brings back so many sweet memories.

    Sometimes it's...

    Overwhelming.
    """
    jump deskscreen1
label photos1:
    if stefan_comp == True:
        """
        Stefan...

        Even though he has always scared me...

        I still worry about him a lot.

        I hope everything is going good for him.

        And that those eyes are now closed,\nat rest.
        """
        jump deskscreen1
    if stefan_comp == False:
        """
        When I was still a guest here...

        I used to take many photos of the hotel and the guests.

        Many of them have left the hotel.

        And the others...

        Well, we are not so friendly anymore.

        Time passes and things change, right?

        This reminds me...

        A lot of time ago, Stefan was just like me.

        He wanted to listen to people.

        To know about their life.

        Even though he often said he didn't care about others...

        He spent a lot of time with some of the guests.

        And when I think about him, the words from\none of our various sessions come to my mind.
        """
        jump day4
label books1:
    """
    All these books...

    I'll never grow a collection as huge as Claire's...\nbut it's nice to always remember that we shared an interest.

    I hope she's still reading, wherever she is now.
    """
    jump deskscreen1
label lamp1:
    """
    This lamp always reminds me of Yasu's light.

    Not only the one in his room,\nbut also his inner light.

    We all have one, inside of us.

    For some it shines brighter,\nfor others it's dimmer.

    But that's what makes as humans.

    And his reflected the spirit of a wonderful human being.

    I truly hope he is with his wife, now...
    """
    jump deskscreen1
label diary1:
    if stefan_comp == False or julie_comp == False:
        """
        It's too soon to write today's entry...
        """
        jump deskscreen1
    if stefan_comp == True and julie_comp == True:
        """
        Do I really want to go to sleep already?
        """
        menu:
            "Yes.":
                scene diary
                with slowfade
                """
                I'm not used to question myself,\nthat's why Stefan always scared me so much.

                I couldn't stand his questions, or anything he had to say to me.

                I've always knew that what he said was the truth,\nthat's why I didn't want to listen.

                That's the same you did:\ntelling me the truth about the world.

                But it pointed out all my mistakes, constantly.

                Talking with Julie was more pleasant, but still...

                Nonetheless, it was difficult.

                I now realize that as she confronted her memories, I confronted mine.

                And all my questions were not for her, but for myself.

                Still...I can't help but being scared by her, too.

                By the intentions behind her words.

                By the possibilities that hid in her past.

                By what she decided to tell me and what she didn't say.

                Maybe, both with Stefan and Julie,\nwhat isn't said is worst than what has been said.
                """
                play music "toherenevercome.ogg" fadein(2)
                $ renpy.pause(0.5)
                play movie "intro2.ogv" loop
                show movie with dissolve
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
                h """
                It's...

                It's not\nfor money...

                You really\ncan't\nunderstand.
                """
                stop music fadeout(3)
                scene desk
                with slowfade
                stop movie
                jump segment3
            "No.":
                "Maybe I'll take another look around."
                jump deskscreen1

label day3:
    $ cat = False
    $ cat_pet = False
    stop music fadeout(2)
    scene black
    with fade
    scene day1
    with quickfade
    $ renpy.pause(3)
    play music "day2.ogg" fadein(2)
    play movie "smoking.ogv" loop
    show movie with slowdissolve
    """
    Sometimes I observe the hotel's courtyard.

    It's almost empty, in the early mornings...

    And the soft breeze that caresses me helps me concentrate.

    And get mentally ready for the day.

    It's in moments like these that I can think more straightly.

    In which I don't lose myself through memories.

    And in which I miss you the most.
    """
    scene corridorf2
    with slowfade
    stop movie
    """
    And here I am.

    The second floor.

    The light here is always so smooth...

    So calming.

    Ironic, since the rooms are mostly the emotionally heaviest of all the hotel.
    """
    jump floor2_1
label floor2_1:
    if julie_comp == False:
        call screen floor2_1
    if julie_comp == True:
        stop music
        scene desknight
        with slowfade
        play music "intro.ogg" fadein(3)
        $ renpy.pause(3)
        jump deskscreen1
label cat1:
    if cat == False:
        $ cat = True
        """
        I often encounter this cat, when I come here...

        The director told me he has no owner.

        So I often wonder where he comes from?

        Should I pet him?
        """
        menu:
            "Of course!":
                $ cat_pet = True
                "He has scratched me!"
            "Not now.":
                $ cat_pet = False
                "He seems happy I didn't approach him..."
        jump floor2_1
    if cat == True and cat_pet == True:
        """
        He scratched me again!
        """
        jump floor2_1
    if cat == True and cat_pet == False:
        "Maybe it's better to leave him alone..."
        jump floor2_1
label clock1:
    """
    This clock is as old as this place.

    I always have the impression that I could break it just by touching it.

    ...

    ...And sometimes I'm tempted to do it.

    Maybe another time, though.
    """
    jump floor2_1
label breakfast1:
    """
    ...

    Why did someone left here an entire breakfast?

    And for two?

    Hmmm...
    """
    jump floor2_1
label julie1:
    if julie_comp == True:
        """
        Julie's session is finished.
        """
        jump floor2_1
    if julie_comp == False:
        """
        Room 203.

        Until some weeks ago it was occupied by a young man.

        It has been vacant for some time and, then, Julie arrived.
        """
        stop music fadeout(4)
        scene door203_1
        with slowfade
        $ renpy.pause(1)
        scene door203_2
        with dissolve
        $ renpy.pause(1)
        scene door203_3
        with dissolve
        $ renpy.pause(1)
        scene julieframe
        with dissolve
        $ renpy.pause(0.5)
        play movie "julie.ogv" loop
        show movie with slowdissolve
        play music "julie.ogg" fadein(4)
        """
        As I enter Julie's room...

        I find myself in what appears to be a real nightmare.

        Are all these...her?

        I recognize the true one, though.

        Her expression tells it all, really.

        Rapidly, I sit next to her...
        """
        i "Good morning,\nJulie."
        menu:
            "How are you today?":
                j """
                Hi,\nIsabelle...!

                Hahah.

                Uhmm...

                What am I\nsupposed to\nsay?

                Hah...
                """
                menu:
                    "Nothing, if you don't feel like it.":
                        j """
                        Thanks,\nI would really\nprefer that.

                        ...haha.

                        Sorry,\nit's nothing\npersonal.

                        But...

                        After all,\nI almost don't\nknow you.
                        """
                        i "No problem,\nit's ok."
                        j "Maybe we could\nget to know\neach other\nbetter?"
                        i """
                        Of course!

                        I would\nlove to.
                        """
                        j """
                        Great!

                        Hah...\nha.
                        """
                    "Just how you're feeling now.":
                        j """
                        Uhmmm...\nyeah.

                        But...

                        How can I\nsay this...
                        """
                        i "Go on,\ndon't worry."
                        j """
                        I barely\nknow you.

                        I,\nlike,\nonly know\nyour name.

                        And you're\nhere\nfor work.

                        So it's\nawkward.

                        No offense\nmeant,\nof course.

                        Hahah.
                        """
                        i """
                        None taken.

                        Does\nthis situation\nmakes you\nuncomfortable?
                        """
                        j """
                        Humm...

                        A little.

                        Yes.

                        Sorry.
                        """
                        i """
                        Don't worry!

                        Let's try\ntalking a little,\nok?
                        """
                        j "Ok...\nheh."
        j """
        So, hahah.

        What exactly\nshould we\ntalk about?

        Like...

        My past?

        How\nI'm feeling\nnow?
        """
        i """
        Of whatever\nyou want!

        But usually\nI start from\nchildhood...

        And then\nmove on\nto now.
        """
        j """
        Uhm, ok...

        Where\ndo I\nstart...

        I've\nalways been an\nonly child.

        My parents\nwere very kind\nbut also\nstrict.

        You know,\nthey cared\na lot about\ngrades and such...

        Oh\nand people's\nimpressions.

        A classic,\nright?

        But well,\nthat's how\nthey were.

        Everything\nwas about\ngood grades\nand\nnice smiles.

        You know...

        All work\nand\nno play...
        """
        i """
        May I ask\nyou...
        """
        menu:
            "How was your life before the Hotel?":
                j """
                My life\nbefore...

                I worked\nin a...wonderful\noffice.

                Had a\n...wonderful\nhusband.

                In a\n...wonderful\ncity.
                """
                i "Uh, all very...\nwonderful!"
                j """
                Yes...

                Right?

                I have\nalways\nwondered...

                How did I\nget there?

                You know,\none moment\nbefore\neverything\nwas average.

                And then...

                One moment\nlater\neverything\nwas...wonderful.
                """
                menu:
                    "Were you happy?":
                        j """
                        ...\nyeah...

                        Of course\nI was.

                        Hahahhh.
                        """
                        i "...now you\ndon't seem\nso sure."
                        j """
                        It's just\nthat...

                        Well,\nhappiness is\nsubjective.

                        Your happiness\nmay not coincide\nwith mine.

                        And...

                        Well,\nit's like\nmoney.

                        You know,\nyou spend your\nwhole life,\nand then...

                        Things\njust\nend.

                        And\nthe people around you\njust get three days\nof mourning.

                        Your funeral\nends.

                        Then all the\ninheritance affair...

                        And life\neventually\nmoves on\nfor everyone.

                        And you\nfind yourself\nin a strange\nhotel.

                        And you're\nonce again\nalone.

                        That's why I'm\nnot sure if\nI'm happy,\nnow.
                        """
                    "What had happened?":
                        j """
                        It's\nstrange...

                        I try to\nremember,\nbut...

                        I can't.

                        Hahah.

                        Funny,\nright?

                        When we try\nto remember\nthe most important\nthings...

                        We\njust\ncan't.

                        And all\nthere is\nare the most\nstupid things.

                        But maybe\nit's just how\nlife is.

                        Thing\nsimply\nhappen.

                        Without\nany reason.

                        Without\nany meaning.

                        They\nhappen.

                        And\nthat's\nall.

                        That's how\nyou end up\nwhere you are.

                        At one point\nyou wake up\nand realize...

                        'Oh,\nI'm here!'
                        """
                j """
                Uhmm...

                It's difficult\nfor me,\nyou know?

                I'm not\nso used to\ntaking decisions.

                Usually...

                I just do\nwhat others tell me\nto do.
                """
                i "Can I\nask you\nwhy?"
                j """
                H...hah.

                I...

                I\ndon't\nknow.

                Usually,\npeople tell me\nwhat I should\nor should not do...

                And I follow\ntheir advices.

                It's nothing particularly\nstrange...

                Or is it?
                """
                i """
                It depends on\nhow you feel\nabout it.

                Does it make you\nfeel\nbad?
                """
                j """
                Well...

                Sometimes,\nyes.

                It's suffocating.

                I find myself\nliving a life\nthat isn't mine...

                Talking with people\nI don't\nlove...

                Doing things\nI don't\nunderstand.

                But...

                Always with\na smile\non my face.

                Heh.
                """
                menu:
                    "What does smiling means to you?":
                        j """
                        ...

                        I think...

                        I think that\nsmiling to others\nmakes them feel\nloved.

                        Or appreciated.

                        It makes people\nfeel happier,\nin a way.

                        Hahah...\nhahh.

                        And...

                        When I smile\nI can\nendure things\nmore easily.

                        If I stop\nsmiling...

                        Then everything\nloses colour.

                        And nothing\nmakes sense\nanymore.

                        No matter\nhow much\nI may suffer...

                        Smiling\nmakes life\nsofter.
                        """
                    "Do you think this relates to your dream?":
                        j """
                        ...

                        It could,\nyes...

                        But I can't\nunderstand how.

                        I mean...

                        I used\nto smile\na lot...

                        And\nloved cinema,\nbut...

                        What\ncould this\nmean?

                        I really\ndon't get it.

                        I'm\nscared.
                        """
            "What do you think about your room, then?":
                j """
                ...

                Well...

                It\nmakes me\nanxious.

                And nervous.

                Hahah.

                Sorry,\nI try to laught,\nbut it's\ndifficult.
                """
                i "Don't worry,\nyou don't\nhave to\nforce yourself."
                j """
                Yeah,\nsure.

                Anyway,\n all these\nme...

                Remind me of\na bad period\nof my life...

                You know,\nIsabelle...

                I lived a\npretty lonely\nlife.

                I mean...

                It was\na...\nwonderful one.

                Nothing\nreally bad\never happened.

                Yet I\ncan't help but\nwonder...

                Was it really\nmine?

                Or was it\nsomeone else's\nlife?

                Following other's\norders,\ndesires,\nadvices...

                Yes,\nI had\na...wonderful husband,\nbut...

                Does that matter\nwhen you can\nbarely kiss him?

                Yes,\nwe had\na wonderful house,\nbut...

                Does that matter\nwhen you can\nbarely touch it?

                Work...

                Work,\nwork,\nwork.

                Only work.

                All the day,\nevery day.

                A repetition of...

                Work,\nearn money,\nspend them.

                We wanted\ntwo children,\nyou know?

                But\nhow could I\ngive birth\nin such a world?

                There's too much\nhate\nall around.

                Too much\ndivision.

                Too much\nloneliness and\nabandonment.

                Life was\nbarely tolerable\nfor me...

                How could I\never possibly\nbring a new life\nto a place like this?

                So\nI had to\nrefuse...

                And he\nabandoned me\nfor\nsomeone else.

                And I accepted it.

                With\na sweet smile\non my lips.

                I hate\nmyself\nfor that.

                I hate\nthese stupid\nsmiles.

                How can\npeople like me\nconfront life\nin such a way?

                How can we\njust accept?

                What was\nwrong\nwith me\nat that time?

                Maybe...

                These other me\nare all the times\nI betrayed myself?

                All the times\nI smiled?

                And...\nwhat should I\ndo now?
                """
                menu:
                    "Learn from all that and keep walking.":
                        scene julieend
                        with slowdissolve
                        stop movie
                        j """
                        Uhmm...

                        Is that\nthe right thing\nto do?

                        Hmmm...

                        I wonder...

                        Maybe\nyou are right.

                        I should\nlook at my past\nanalitically...

                        Study it...

                        Understand\nmy errors...

                        And then\ngo on\nwith my life.

                        But is it\nreally possible?

                        Can\nI\ndo it?

                        Do I\nhave\nthat strength?

                        But,\nI could try,\nat least.
                        """
                    "You should understand the dream, then yourself.":
                        scene julieend
                        with slowdissolve
                        stop movie
                        j """
                        The dream...

                        Myself...

                        These two things\nstill look so\nseparated\nto me.

                        I really\ncan't grasp\nthe idea.

                        Tell me,\nIsabelle,\nhow do you?

                        Isn't it\ndifficult\nfor you too?
                        """
                        i """
                        In the beginning\nit was,\nbut...

                        Well,\nI can't see\nmy dream.

                        That's why\nI can do\nthis job.

                        I will stay\nin this place\nas long as\nI can't see it.

                        So I have to\nmake myself useful,\nsomehow.
                        """
                        j """
                        Oh...

                        Maybe I shouldn't\nsay that,\nbut...

                        That\nsounds like\na prison.
                        """
        i """
        Julie...

        This hotel\nis not\nagainst you.

        Even if\nsometimes\nit may seem so...

        It exists\nfor you.

        For\nme.

        For everyone\nthat inhabits\nthe rooms.

        And this dream,\nyour dream...

        For how\nterrifying,\nor dark\nit may be...

        Is here\nto help you\nunderstand yourself.

        Change\nyourself.

        Believe in\nyourself.

        That's what\ndreams\ndo.
        """
        $ julie_comp = True
        $ stories_comp += 1
        stop music fadeout(2)
        scene corridorf2
        with slowfade
        stop movie
        play music "day2.ogg" fadein(2)
        jump floor2_1
label stefan1:
    """
    Room 204...

    Just looking at it makes me anxious.
    """
    jump floor2_1

label day4:
    $ cat2 = False
    $ cat_pet2 = False
    stop music fadeout(2)
    scene black
    with slowfade
    scene day1
    with quickfade
    $ renpy.pause(3)
    play music "day2.ogg" fadein(2)
    play movie "listening.ogv" loop
    show movie with slowdissolve
    """
    Sometimes, just as soon as I wake up, I listen to something.

    Books aren't the only thing that guests can receive\nfrom the mail service here in the hotel.

    So I bought some albums.

    And, believe it or not...

    I almost always listen to 'our' album.

    Heh.

    ...

    I guess Julie already had an impact on me.
    """
    scene corridorf2_2
    with slowfade
    stop movie
    """
    Ok.

    Today there's only one session with Stefan

    Huh.

    Good luck to me.
    """
    jump floor2_2
label floor2_2:
    if stefan_comp == False:
        call screen floor2_2
    if stefan_comp == True:
        stop music
        scene desknight
        with slowfade
        play music "intro.ogg" fadein(3)
        $ renpy.pause(3)
        jump deskscreen1
label cat2:
    if cat2 == False:
        $ cat2 = True
        """
        Ok...

        Today is another day.

        Should I pet him?
        """
        menu:
            "Of course!":
                $ cat_pet2 = True
                "He has scratched me today too!"
            "Not now.":
                $ cat_pet2 = False
                "Once again, he seems happy I didn't approach him..."
        jump floor2_2
    if cat2 == True and cat_pet2 == True:
        """
        He scratched me again!

        Hm.
        """
        jump floor2_2
    if cat2 == True and cat_pet2 == False:
        "Maybe it's better to leave him alone..."
        jump floor2_2
label clock2:
    """
    Is this the day I'll touch this clock and break it?

    Hmmmmm...

    Maybe.

    Or maybe not.
    """
    jump floor2_2
label breakfast2:
    """
    ...

    Someone left here an entire breakfast.

    Again.

    And for two.

    Again.

    Hmmm...

    This is getting suspicious.
    """
    jump floor2_2
label julie2:
    """
    Not today, unfortunately.
    """
    jump floor2_2
label stefan2:
    """
    Room 204...

    Just looking at it makes me anxious.
    """
    stop music fadeout(4)
    scene door204_1
    with slowfade
    $ renpy.pause(1)
    scene door204_2
    with dissolve
    $ renpy.pause(1)
    scene door204_3
    with dissolve
    $ renpy.pause(1)
    scene stefanframe
    with dissolve
    $ renpy.pause(0.5)
    play movie "stefan.ogv" loop
    show movie with slowdissolve
    play music "stefan.ogg" fadein(4)
    """
    As usual, he's looking into the mirror.

    And, as always, I wait for him to talk.

    Whenever he's ready.

    But...

    It's strange.

    Today something feels different...
    """
    s """
    Welcome back,\nIsabelle.

    How\nare you doing\ntoday?
    """
    menu:
        "Still sleepy. And you?":
            s """
            And you're\nsupposed\nto help\nwhile sleepy?

            Hmm.

            Anyway, today's\na bad day,\nas usual.

            I feel\nlike I have\nno energies.

            Don't\nknow\nwhy.
            """
        "Very happy, and you?":
            s """
            Happy,\nhuh?

            I can\nread you\nlike an open\nbook.

            And you're\nnot happy.

            But\nit's ok if\nyou want to\nfake it.

            It's not\nmy business.

            Knowing\nthat you're sad\ndoesn't satisfy\nme.

            I'm not\na horrible\nperson.

            Even\nif you think\nI am.

            I just question\nwhat you\nbelieve in.

            But,\nyou know...
            """
        "I don't trust you. What's happening?":
            s """
            You don't\nneed to.

            I don't\nwant to\nharm you,\nIsabelle.

            You know\nI don't.

            And you know\nI don't\nplay games.

            But...
            """
    s """
    ...

    How much\ndo you plan\non staying here,\ntoday?
    """
    menu:
        "All the time necessary.":
            s """
            Lucky me.
            """
        "Am I disturbing you?":
            s """
            Hm,\nwhatever.
            """
    s "Just don't\ndistract me\nfrom the mirror."
    i "Have you seen\nsomething new\nin it?"
    s """
    Always\nstraight\nto the point.

    Huh?

    Sometimes\nI forget\nthat's why\nyou are here.

    Just\nto know\nabout me.

    How\nI feel.

    How\nI think.

    And if\nyou can\ncontrol me.

    What is it\nthat brought\nyou here?

    Some kind\nof advertisement?

    A friend\ntold you about\nthis place?

    Or some vip\nsaid they've\nbeen here?

    Was it\nthe possibility to\nmake choices\nand influence\nother people?

    Is that\nhow you think\nabout the world?

    And how\nyou act?

    Do you\nlet yourself\nbe controlled\nby others?

    Is that why\nyou want to\ncontrol things?

    Or guide them\ntowards\nwhere you want.

    Or\nwhere others\nwant.

    And as always,\nyou expect to\ndo the same\nwith me.
    """
    menu:
        "It's just my work.":
            s """
            Just...

            Your...

            Work.

            Three words\nare enough\nfor an absolute\ntruth.

            Controlling others\nwhile\nbeing controlled...

            Is this\nwhat your work\nis about?

            For you,\nknowing that you\nhave to listen\nto others\nand guide them\nis enough.

            Right?

            And I imagine\nyou want me\nto shut up.

            But\nyou know\nI won't.

            Because\nthis is my time\nand I can do...

            Whatever\nI want\nwith it.

            I am\ncontrolling you.

            I decide\nwhat to tell\nyou.

            Depending on\nyour question\nI choose how\nto answer.

            If I\nfeel like it,\nI might tell you\na story.

            If I don't,\nI might just\nplay with you.

            So...

            You think that\nyour questions\ncontrol me,\nbut it's the opposite.
            """
        "Do you plan on going on for much longer?":
            s """
            Hmm.

            So you\nare sincere,\nsometimes.

            That's nice\nto know.

            You should\ndo that\nmore often.

            Free yourself\nfrom the burden\nof your mask.

            It must be hard\nto smile\nall the time.

            To be\nfake happy\nevery day.

            So...

            Just\nlet yourself\ngo.

            You remind me\nof someone\nI once knew.

            A brilliant,\nsuccesful,\nyoung\nman.

            Always\nsmiling.

            Always\nplaying a part.

            Like a\nskillfull actor.

            I worked\non some\nsoundtracks\nfor him.

            Not\nas many as\nI would have\nliked to,\nbut...

            I enjoyed\nmaking them.

            Especially\nbecause...

            It meant\ngetting to know\nhim.

            He was\nconstantly annihilated\nby his life.

            By\nthe sadness\nhe had.

            By\nhis eternal\nloneliness.

            And yet\nhe was always\nsmiling.

            Always\nlistening.

            Always\nhelping others.

            Even though\nno one\nwas there\nto help him.

            Of course\nhe worked with\na lot of\npeople.

            But that's\nnot what\nhe needed.

            He needed\na deeper kind\nof help.

            More\npersonal.

            Something\nno one wanted\nto give him.

            Thanks to him\nI understood\nthat...

            Those who\nseem to be\nthoughtless...

            Are\nthe ones who\nsuffer more than\nany other.

            Isn't it\nthe same\nfor you?
            """
            i "..."
    s """
    Hmm,\nyou know...

    I've\nrealized something,\nlately.

    We are\nnot humans\nanymore,\nIsabelle.

    So...

    We\nmay just\nmove on.

    And\nnot care about\nhuman things\nanymore.

    Let's just\ngive up\nart, meaning,\npurpose, satisfaction.

    Let's just\ntoss away\npersonality, individuality,\nlove, feelings.

    And let's embrace\nmoney, work,\ntechnology, property.

    Let's live to get\na new nice house,\na new super car,\na new bank account.

    Let's work\nand be just that:\nour job.

    Not humans,\nbut a lable.

    We are\nwalking lables.

    We are\nmusicians, concept artists,\nlwyers, accountants,\ncashiers, street cleaners.

    All this\njust to avoid\nbeing homeless.

    All this\nsadness and unsatisfaction\nonly to not\nstop walking.

    So yeah,\nlet's stop pretending\nbeing humans\nanymore.
    """
    menu:
        "What about these eyes, then?":
            s """
            They\nare only\nmemories.

            Nothing\nmore.

            Memories\nI try to avoid\nby looking through\nthe mirror.
            """
            i "They seem\nto haunt you."
            s "Sometimes."
            menu:
                "Any idea why?":
                    s"""
                    If you think\nit's some trauma\nfrom my childhood...

                    Or other\nbullshit\nlike that...

                    I'm sorry\nto disappoint\nyou.
                    """
                    i "Then what\nis it?"
                    scene stefanend
                    with slowdissolve
                    stop movie
                    s """
                    ...

                    Some\ntime\nago...

                    'Before',\nI should\nsay.

                    I was\na different\nperson.

                    As you\nalready know,\nI was a musician.

                    Admired\nby fans.

                    By critics,\ndepending\non the trends.

                    Or by\nother musicians.

                    Yet,\nI wasn't\nso much in love\nwith people.

                    I didn't look\nat anyone\nwith...

                    Interest.

                    I was\nclosed\ninto myself.

                    I wanted to\nexplore myself.

                    That's when\nthe eyes appeared\nin my dreams.

                    At first\nthere were\nonly two...

                    Then they\nstarted multiplying,\nday by day.

                    And now\nthat I'm here...

                    They're\nall around\nme.

                    Does\nthis story\nsatisfies you?
                    """
                    menu:
                        "What are they looking for?":
                            s """
                            ...

                            For\nthe humanity\nleft in me.

                            I\nguess.
                            """
                        "What are you looking for?":
                            s """
                            For myself...

                            I\nguess.

                            Whatever that\nmeans...

                            With\nor without\nhumanity.
                            """
        "What makes you think we're not humans anymore?":
            s """
            Hmm,\nwell...

            Let's put\neverything\non the table.

            You've seen\nmany people\npass away.

            And\nI heard about\nYasu and Claire.

            You know,\nby now,\nwhat I'm\ntalking about.

            We won't\nstay here\nforever.

            Because\nwe're all\nrunning out\nof time.

            The problem\nis...

            Will we\nresolve ourselves\nbefore\nthat time comes?

            You\nunderstand this well,\ndon't you?
            """
            menu:
                "I don't know what you're talking about...":
                    scene stefanend
                    with slowdissolve
                    stop movie
                    s """
                    You don't?

                    So,\nwhat was\nthat girl's\nname...
                    """
                    i """
                    Stop!

                    Please...
                    """
                    s """
                    I know\nit hurts,\nIsabelle.

                    I know\nhow difficult\nit is.

                    How tedious\nit is.

                    And how much\nit destroys\nyou.

                    But\nwe don't have\nthe time\nto cry.

                    We don't have\nthe time\nto be sad.

                    We have built\nthe world\nas it is today.

                    And these\nare its rules.

                    And this hotel\nis no\ndifferent.

                    When we\ncome here,\nwe think\nwe'll have all\nthe time we need.

                    We think\nour rooms\nwill help us.

                    That we\nwill understand\nourselves.

                    Or\nfind peace.

                    But\nall we find\nis this pain.

                    And\njust like\nout there...

                    We don't have\nall the time\nwe want\nto resolve it.
                    """
                "I do...in a way.":
                    scene stefanend
                    with slowdissolve
                    stop movie
                    s """
                    It's not the same\nfor everyone.

                    But\nyou feel\nit.

                    That pain\nthat won't\ngo away.

                    The pain\nthat haunts you\nevery night.

                    That\ntorments you\nin your sleep.

                    That reminds you\nof painful\nmemories.

                    And makes\nyou feel\nalone.

                    That pain\nwill follow us\nuntil\nthe very end.

                    And I'm afraid\nthis hotel can't\navoid that.
                    """
    $ stefan_comp = True
    $ stories_comp += 1
    stop music fadeout(2)
    scene corridor
    with slowfade
    stop movie
    play music "day2.ogg" fadein(2)
    jump floor2_2

######## START OF SEGMENT 3 #########################################################################################

label segment3:
    scene deskdawn
    with slowfade
    play music "intro.ogg" fadein(2)
    """
    Then, we left each other, like many do at some point.

    Things start, and then end.

    Stories have a conclusion, and obviously an ending too.

    This is what I've tried telling myself for a lot of time.

    But now...

    Now it's too difficult.

    Too heavy.

    I can help others in sustaining themselves and be better,\nbut I really can't help myself.
    """
    jump deskscreen2
label deskscreen2:
    call screen desk2
label flower2:
    if kim_comp == True:
        """
        Is it possible to see someone's face when we look at a certain flower?

        Because that's what happens when I look at them, now.

        I think about you, thanks to Kim's teaching.

        Love truly is absolute, and never passes.

        It may look towards someone else,\nbut if we were particularly fond of someone, we will always keep a fragment of that love with us.
        """
        jump deskscreen2
    if kim_comp == False:
        """
        Fresh like a blooming flower, so was Kim.

        Tormented by love, just like me.

        Hoping for a better future...not so much like me.
        """
        jump day6
label calendar2:
    """
    Dear Julie...

    Time passes endlessly.

    Sometimes slowly, other times too rapidly.

    And I often can't keep track of it.

    But I hope you can, now.
    """
    jump deskscreen2
label mug2:
    if takeshi_comp == True:
        """
        To be in love with our dreams...

        To talk about them feverishly...

        Thanks to you, Takeshi, I learned how important this is.

        And now that I've remembered, I look at this mug very differently.
        """
        jump deskscreen2
    if takeshi_comp == False:
        """
        This mug always gets boiling hot when I pour something into it.

        It seems like a magic.

        A terrible one.

        But it's just like Takeshi was...

        Cold when empty, and boiling hot when he discussed his desires.
        """
        jump day5
label photos2:
    """
    Stefan...

    Even though he has always scared me...

    I still worry about him a lot.

    I hope everything is going good for him.
    """
    jump deskscreen2
label books2:
    """
    All these books...

    I'll never grow a collection as huge as Claire's.

    But it's nice to always remember that we shared an interest.

    I hope that, wherever she is, she's still reading.
    """
    jump deskscreen2
label lamp2:
    """
    This lamp always reminds me of Yasu's light.

    I wonder if he is with his wife, now...
    """
    jump deskscreen2
label diary2:
    if kim_comp == False or takeshi_comp == False:
        """
        It's too soon to write today's entry...
        """
        jump deskscreen2
    if kim_comp == True and takeshi_comp == True:
        """
        Do I really want to go to sleep already?
        """
        menu:
            "Yes.":
                scene diary
                with slowfade
                """
                And this closes off the round of memories that came to my mind...

                All these scenes, all these words...

                They echo through my mind as painful stabs at my soul.

                When I see or think about all these people, it's too hard to sit still\nthings are too passionate, times are too real.

                I feel it in the hotel's corridors...\nthe people breathing without hope, going through the motions.

                The focus get cleared then the light turn sharp,\ntears burn my eyes, and the mind grows weary.

                How much time has passed since my first day here?

                How many days have passed since the last time I saw you?

                And how many since the first time we ever spoke?

                Should I still think about you?

                Should I forget about you?

                How is it that I can tell others to move on,\nbut I can't do that to myself?

                I realize only know that I can give strength to others,\nbut I'm powerless when it comes down to me.

                I can't love myself, like many others of my generation.

                I can't find the energy to uplift myself from\nthe thoughts, the preoccupations, the fears.

                The only thing I can do is losing myself into my own self.

                And hope...

                Hope to move on.

                But also hope to see you.

                To talk with you...

                At least one last time...I'm powerless\neven if it means to only dream about it.
                """
                stop music fadeout(2)
                jump ending
            "No.":
                "Maybe I'll take another look around."
                jump deskscreen2

label day5:
    stop music fadeout(2)
    scene black
    with slowfade
    scene day1
    with quickfade
    $ renpy.pause(3)
    play music "day3.ogg" fadein(2)
    play movie "breakfast.ogv" loop
    show movie with slowdissolve
    """
    A calm day.

    While looking outside the window,\nlosing myself in the endlessness of the hotel all around...

    I feel a strange heaviness inside of me.

    And I can't go on eating.
    """
    scene corridorf3_1
    with slowfade
    stop movie
    """
    The third floor...

    The most empty of all.

    Something that, strangely, reflects the minimalism of Kim and Takeshi.
    """
    jump floor3_1
label floor3_1:
    if takeshi_comp == False:
        call screen floor3_1
    if takeshi_comp == True:
        stop music
        scene deskdawn
        with slowfade
        play music "intro.ogg" fadein(3)
        $ renpy.pause(3)
        jump deskscreen2
label jacket1:
    """
    Takeshi's jacket.

    I don't know why, but he never keeps it into his room.

    He always prefers to leave it outside.
    """
    jump floor3_1
label painting1:
    """
    There was a painting here, once...

    A big painting of the director's lover.

    One of the many, anyway.

    But she toss it away some years ago.

    Or, at least, that's what the rumors say.
    """
    jump floor3_1
label plant1:
    """
    It's strangely dry...

    Someone should definitely water it.
    """
    jump floor3_1
label takeshi1:
    if takeshi_comp == True:
        """
        Takeshi's session is finished.

        I should check on Kim.
        """
        jump floor3_1
    if takeshi_comp == False:
        """
        Room 305...Takeshi's room.

        It always feels a bit cold from outside.
        """
        stop music fadeout(4)
        scene door305_1
        with slowfade
        $ renpy.pause(1)
        scene door305_2
        with dissolve
        $ renpy.pause(1)
        scene door305_3
        with dissolve
        $ renpy.pause(1)
        scene takeshiframe
        with dissolve
        $ renpy.pause(0.5)
        play movie "takeshi.ogv" loop
        show movie with slowdissolve
        play music "takeshi.ogg" fadein(4)
        """
        To burn with desire...

        To burn with desire,\nbut in a cold and windy world.

        To gently fall on the ground like snowflake,\nunique in a vast group and yet seemingly identical.

        It has always been strange to talk with Takeshi and to describe him,\nbecause my words never seemed enough.

        Somehow, he constantly managed to\nescape from my grasp.

        I've never been able to entirely capture the image of him.
        """
        i "Hello Takeshi..."
        menu:
            "What's on your mind today?":
                t """
                I've been\nthinking\nand observing,\nas usual.

                Today\nthe snow fell\nmore ferociously.

                It seems\nthe dream\nis changing.

                Which means that\nI am.

                And the world is,\ntoo,\nalongside me.

                It's a strange\nsensation.

                This snow\nis warmer.
                """
                menu:
                    "Warmer? How so?":
                        t """
                        It's quite\ndifficult to\ndescribe...

                        I don't know\nif I can find\nthe right words.

                        But what\nI mean\nis...

                        This snow\nis burning\nme.

                        Burning me\nwith the desire\nto act.

                        I feel like\nthis world\nis a prison.

                        I wander through\nthis endless land...

                        And struggle\nto not lose\nmyself.

                        And the\nonly way\nis through act.

                        But\nwhat kind\nof act?

                        And then...\nwhat is\nan act?

                        What does it\nmean\nto act?
                        """
                    "How do you know the world is changing?":
                        t """
                        The world\nconstantly changes,\nIsabelle.

                        At each second passing,\nwe experience\na reality that\nis different from\nthe previous one.

                        This snow\nis different\nfrom the one\nthat fell\nbefore.

                        The universe\nchanges,\nevolves.

                        It's a sham\nthat we don't realize\nthis while living.

                        Everyday\nwe walk through\nour cities...

                        Unaware of\nour own\ninner changes.

                        We don't have\ntime\nto think about it.

                        Not\nanymore.

                        We have to\nwork.

                        We have to\nconstantly run.

                        We are\nbombarded with images,\nsounds,\nthoughts.

                        Everything\ngrows faster\nday by day.

                        This is part\nof the change\ntoo.

                        To the point where\nwe can't think\nabout ourselves.
                        """
        t """
        I'm sorry...

        As always,\nI'm losing myself\nthrough my preoccupations.
        """
        i """
        Don't worry\nabout that.

        It's my job\nto listen\nto you.
        """
        t """
        That's true...

        But one\nmust never\nlose their\nfocus.

        In general,\nI mean.

        Both in\neveryday life\nand\nwhile deeply thinking.

        We must\npay attention\nand be focused.
        """
        i"And you\nfeel like you're\nnot focused?"
        t """
        Sometimes\nI am...\nother times\nI'm not.

        My mind\nwanders.

        And I\nlose myself\nhalfway\nthrough the thoughts.

        Through\nthe feelings.

        Through\nthe sensations.

        And when\nI start wandering\neverything becomes\none.

        There's no\ndistinction\nanymore.

        All things\nare the\nsame thing.
        """
        menu:
            "How does that make you feel?":
                t """
                ...Scared.

                Losing myself\nis like\nlosing touch\nwith reality.

                Nothing\nis the same\nanymore.

                Nothing\nmakes me feel\nanything.

                I become like\nthis snow...

                Cold\nand silent.

                Oh, and\nyou know...

                I still hope\nto find something\nin here.

                Can you\nbelieve that?
                """
                menu:
                    "What might you find?":
                        t """
                        Among all the\nspectres I catch\na glimpse of...

                        I sometimes\nwish to see\nit.

                        My future.

                        Right among\nthis land.

                        But the\nonly thing that\ngreets me is\nthat tree.

                        From time\nto time,\nI pass\nnear it.

                        And that's when\nI understand\nI'm walking\nin circle.

                        But I can't\nstop at all.

                        I can't help\nbut follow\nthe world's pace.

                        Even though\nI don't want\nto.
                        """
                    "Do you think there's a meaning behind that hope?":
                        t """
                        Yes,\nI thought a lot\nabout it.

                        I have no\nclear\nanswers,\nbut...

                        Maybe\nit's the desire\nto stop walking.

                        To be able\nto not move\nanymore.

                        To not follow\nthe world's pace...

                        And follow\nmine.

                        I feel\nthere's too much\nspeed\naround me.

                        Too much\nnoise.

                        Too much\nsnow.
                        """
            "What happens then?":
                t """
                I just\nwalk.

                Walk\nand think.

                And as I walk\nI see spectres\nfrom the everyday world.

                They\nfleetingly appear\naround me.

                Sending me\ntheir doomed\nmessages.

                And I flee\nfrom them.

                Or at least\nI try.

                They are\nsilhouettes\non the verge\nof suicide.

                Children\nnot endorsed by\ntheir loved ones.

                Artists\nexploited by\ntheir audience.

                Employees\nforced into a job\nthey hate\njust to survive.

                People\nwith no way\nto survive the\neveryday.

                People\nwho stopped.

                People\nwho couldn't follow\nthe world's\ngrowing speed.

                All this\nis the image of\ntoday's world.

                And it\npains me.

                And if\nI stopped...

                It would be\nthe end\nof me.

                I would become\na spectre\namong them.

                So there ain't\nno way\nI can stop\nwalking.

                No matter what\nhappens.

                No matter\nwhat it means\nto keep walking...

                I can't\nafford\nto stop.

                Even though\nI would\nlike to.
                """
        i "But the snow\nis turning\nwarmer, right?"
        t """
        Yes.

        Slowly...

        But\nit's happening\nfor sure.

        And maybe\none day it will\nslow down.

        And I too\nwill be able to\nchange pace.

        In the end,\nmy struggle\nis a clash\nof ideals.

        To keep\non walking,\nfollowing the\ngrowing speed\nof the world?

        To stop\nand fall victim\nof the world's\napathy?
        """
        menu:
            "When did you started walking?":
                t """
                When\nI was\nstill a child.

                But...

                I think\nit's the same\nfor everyone.

                Especially nowadays,\nit's impossible\nto not walk.

                To not\nmove,\nsomehow.

                We all\nhave to.

                The world\nforces us.

                We are\nforced to\nsurvive.

                We are\nforced to\nwork.

                We are\nforced to\nmake money.

                And so\nwe are\nforced to\nwalk.

                There's not much\nwe can do\nabout it.

                That's\nthe sad truth\nabout us.

                From\nthe moment\nwe are born...

                We are\nbound to\nwalk\nand suffer.

                Well,\nmaybe we won't\nsuffer...

                But for sure\nwe will be\nforced\nto never stop.

                We won't be\nable to get\nsome rest.

                We won't\nhave\nthe time.

                Because\nin modern world\nstopping means\nto lose time.

                And\nif we lose time\nno one\nwill remember us.

                No one will\ncare\nabout us.

                And we\nwon't be able\nto start walking\nagain.

                Various things\nmay happen...

                People we love\nmay die...

                We may lose\nour way...

                We may lose\nourselves...

                And yet,\nwe won't be able\nto stop.

                This\nhurts\nme.

                It's\nunjust.
                """

        scene takeshiend
        with slowdissolve
        stop movie
        """
        But\nyou are\nright.

        The snow\nis getting\nwarmer and warmer.

        The world\nstill constantly\nrotates.

        The universe\ncontinues to\nchange.

        And we\nstill\nmove on.

        My\nown\ndesire...

        To follow\nmy own\npace.

        To follow\nmy own\nthoughts.

        To not\nlose\nmyself.

        To be\nfocused.

        It\nmay be\npossible.
        """
        $ takeshi_comp = True
        $ stories_comp += 1
        stop music fadeout(2)
        scene corridorf3_1
        with slowfade
        play music "day3.ogg" fadein(2)
        jump floor3_1
label kim1:
    """
    Today Kim isn't in her room.
    """
    jump floor3_1

label day6:
    stop music fadeout(2)
    scene black
    with slowfade
    scene day1
    with quickfade
    $ renpy.pause(3)
    play music "day3.ogg" fadein(2)
    play movie "wakeup.ogv" loop
    show movie with slowdissolve
    """
    Sometimes, I wake up with only one thought in my mind...

    Work is a pain, and it's sad that we can't just wake up and live.

    It's sad that life itself, for how hard it is at times, can't be seen as a job itself.

    And that I have to wake up, go out and confront a work schedule.

    What are we becoming?
    """
    scene corridorf3_2
    with slowfade
    stop movie
    """
    A silent day on the third floor.

    Just as usual, I should say.
    """
    jump floor3_2
label floor3_2:
    if kim_comp == False:
        call screen floor3_2
    if kim_comp == True:
        stop music
        scene deskdawn
        with slowfade
        play music "intro.ogg" fadein(3)
        $ renpy.pause(3)
        jump deskscreen2
label jacket2:
    """
    Takeshi's jacket.

    I wonder...

    How much time has passed since the last time I saw him wearing it?

    We use to keep things, and then forget about them...

    Or, maybe, there is a purpose in not using them.

    Is this thought stupid?

    Who knows...
    """
    jump floor3_2
label painting2:
    """
    I wonder where this paiting is now...

    I tried asking it to the director, but she never answered.

    Could it bring back a painful memory?
    """
    jump floor3_2
label plant2:
    """
    This plant is very dry, usually...

    But today it seems someone has exaggerated with the water!
    """
    jump floor3_2
label letter:
    """
    A page torn from a notebook...

    It says:

    'I loved, I lost, I abandoned.'

    'Time won't bring back my past, only my memories and dreams will.'

    'And it's up to me to forget, or to move on.'

    'Living is only up to me.'
    """
    jump floor3_2
label takeshi2:
    """
    Not today, unfortunately.
    """
    jump floor3_2
label kim2:
    stop music fadeout(4)
    scene door306_1
    with slowfade
    $ renpy.pause(1)
    scene door306_2
    with dissolve
    $ renpy.pause(1)
    scene door306_3
    with dissolve
    $ renpy.pause(1)
    scene kimframe
    with dissolve
    $ renpy.pause(0.5)
    play movie "kim.ogv" loop
    show movie with slowdissolve
    play music "kim.ogg" fadein(4)
    """
    Whenever I entered Kim's room...

    I found her longing for her past,\nas I am.

    And I envied her a lot...\nsince she was able to still see her lover through the dream.
    """
    k """
    Oh!

    Hi,\nIsabelle...
    """
    i "Hi, Kim."
    menu:
        "How are you feeling?":
            k """
            Uhmm...

            It's strange.

            I feel like\na broken\nrecord.

            As if\nI'm divided\nbetween different\ntunes...

            that go on\nseparately.

            Totally detached\nand yet\nclose\nto each other.

            There's noise\nall around.

            And then\nmusic.

            And noise\nagain.

            And\nI\njust...
            """
            i "What is it?"
            k """
            The usual,\nIsabelle...

            I'm\nwondering.
            """
    menu:
        "...about him?":
            k """
            Well, no...

            Not today,\nat least.

            But,\nnow that you\nmention him...

            Sometime I\nstill wonder\nwhat he's doing.

            You know,\nlike...

            Where\nis he\nnow?

            What\nis he\ndoing?

            While I'm\nhere...

            How\nis he\nfeeling?
            """
            menu:
                "Do you ever find an answer?":
                    k """
                    No...

                    Obviously\nnot.

                    Those are\nunanswerable questions.

                    I will\nnever know,\nprobably.

                    And I\ntry to think\nit's ok.

                    I try to\nconvince myself.

                    Sometimes it's\na whole job\nby itself,\nyou know?

                    Forcing yourself\nto do something...

                    To believe\nin something...

                    Some people\ndo that\nall their life.

                    But to me\nit's impossible.

                    It's not\nwho I am.

                    And not who\nI've always been,\neither.

                    I can't help\nbut asking\nhow can others\ndo that?

                    How is it\npossible?

                    Forcing\nan idea\nover yourself...

                    It's unbearable.
                    """
                "How does that make you feel?":
                    k """
                    Well...

                    It's interesting,\nat times.

                    Not everytime,\nbut sometimes.

                    Because\nI can imagine\ninfinite possibilities.

                    I picture them\nin my mind...

                    I visualize\nthe colours.

                    The rooms he\nmoves through.

                    The various looks\nin his eyes.

                    The words\nhe says.

                    And everything\nbecomes more beautiful\nthan reality itself.

                    In these moments\nI understand what\nlove is about.

                    To find someone\ndear\nto you...

                    And be interested\nin their existence.

                    In what they could\ndo or be or say\nwhen you're not\nwith them.

                    With who\nthey could become\nin the future.

                    Or even\nwho they will be\nwhen you'll be\nmeeting them\nin a few hours.

                    And I realize\nthese thoughts can\nbecome stories.

                    But...
                    """
                    i "But...?"
                    k """
                    Well...

                    Is it\nright to\ndo so?

                    Is it right\nto put\nsomeon's life\ninto words?

                    Do I\nhave the rght\nto break\nsomeone's secrets?
                    """
                    menu:
                        "Don't novelists write about other people?":
                            k """
                            Yeah,\nmaybe...

                            But\nI\ndon't.

                            I prefer\nto write\nabout me.

                            It's\nmore\nsimple.

                            More\nsincere.

                            To write about\nothers means to\ninvade other\npeople's space.

                            I can't\nwrite about\nsomeone\nwithout their\npermission...

                            It's like\nmurdering them,\nto me.

                            There's something\nawfully cruel\nin doing that.

                            As if\nit is a\nprofanation.
                            """
        "...about your novel?":
            k """
            Well...

            I'm\ntrying to.

            It just\nkeeps on\ndeveloping\nby itself.

            Whenever I\nsit at the desk\nthe words just\ncome to me.

            I\naccept\nthem.

            I\nleave\nthe door\nopen.

            And\nthey\ncome in.
            """
            menu:
                "Tell me about what you wrote today.":
                    k """
                    Three monks\nare walking\nthrough the fog.

                    Slowly.

                    Silently.

                    Then,\nsomeone emerges\nin front\nof them.

                    As they\nlook at\nthis person...

                    They feel\nas if\nheaven is,\nsuddenly,\nin front of\ntheir faces.

                    Someone\nso pure...

                    So beautiful...

                    Not in\na physical\nway.

                    But in\na pure,\nspiritual\none.

                    Someone that\nshines\nthrough the fog.

                    And who\nlooks at them\nwith a thin\ntired\nsmile.
                    """
                    menu:
                        "Is it...him?":
                            k """
                            ...no.

                            I can't\nwrite about\nhim...

                            I may\nput some detail\nhere and there...

                            Or hint\nat him.

                            But I can't\nwrite about\nhim.

                            I can only\nwrite about\nmyself.

                            What I\nhave\ninside of me.

                            What I feel\nfor him...

                            It's an\nentirely\ndifferent thing.

                            It comes from\nboth outside\nand inside\nof me.

                            It's a part\nof my feelings\nand yet it's\ndetached.

                            Like this ghost\nlingering beside\nme.
                            """
                "And how is it developing?":
                    k """
                    Hmmm...

                    It's coming along\nwell,\nI guess.

                    I feel like\nI'm halfway\nthrough.

                    And...\nit's strange.

                    It's like\nI'm coming to\nunderstand\nsomething.

                    Something\nburied\ndeep\nwithin me.

                    The more\nI write,\nthe more\nI feel...

                    Lonely.

                    Like,\neternally\nlonely.

                    And this loneliness\nis not only\nmine...

                    It's the\nhuman condition.

                    We are born\nalone...

                    We will die\nalone.

                    As\nsingluar\nindividuals.

                    Hoping to\nfind someone\nwho will erase\nthis feeling.

                    That will\ncaress us\nwhen we feel bad.

                    That will\nkiss us\nwhen we are sad.

                    That will\nlove us\nwhen we won't.

                    And\nbecause of this\nI think that...
                    """
    k """
    Something's\nbroken\ninside of me.

    Half of\nmy heart\nfeels anxious.

    The other half\nlongs for him.

    And I can't\ndecide\nwhich part I\nshould follow.

    Should I\nsurrender\nto love?

    Or\nshould I\naim to\nmyself?

    Am I\nthis feeling\nitself?

    Or am I\nonly me?

    It's so\ndifficult to\nunderstand...

    The notes in my head\nkeep reapiting\nthemselves.

    Broken.

    Redundant.

    And his caresses\nare both a curse\nand a blessing.

    Mostly\nbecause...

    It's not\nhim.
    """
    scene kimend
    with slowdissolve
    stop movie
    """
    But only a\nshade\nof my memories\nof him.

    As I remember\nhis touch\nover my skin...

    Or his eyes\nglancing at\nme...

    Or the curtains\nslowly moving\nnext to us...

    I feel\nalive\nonce again.

    But this...

    This is\nonly\na dream.
    """
    $ kim_comp = True
    $ stories_comp += 1
    stop music fadeout(2)
    scene corridorf3_2
    with slowfade
    play music "day3.ogg" fadein(2)
    jump floor3_2

######## ENDING #########################################################################################

label ending:
    scene black
    with slowfade
    scene ending
    with slowfade
    play music "toherenevercome.ogg" fadein(2)
    $ renpy.pause(0.5)
    scene 1
    with slowfade
    her "Isabelle..."
    i """
    Huh...?

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

    Sorry,\nI'm suffocating.
    """
    scene 2
    with slowdissolve
    her """
    Oh,\nthat's better,\nnow.

    You always\nbuilt up\nall these\nwalls...

    It was impossible\nfor me\nto really get\nin touch with you.
    """
    i "So\nit's always\nmy fault..."
    her """
    No...

    It's just\nwho you are.

    And you must\nunderstand that\nI've never\naccepted it.

    Just like you\nnever accepted\nme.

    I just stared\nwhile you were\nalways writing\non your notebook.

    It was\nour\nfault.

    But now...

    Let's just\ntalk about it.

    Let's confront\nthis elephant\nin the room.

    Let's put\neverything\non the table.

    Ok?
    """
    scene 3
    with slowdissolve
    her """
    I\nmissed\nyou,\nfor all\nthis time.

    While\nI was\naway...

    I always thought\nabout\nyou.

    And I\nwanted to...

    ...
    """
    scene 4
    with slowdissolve
    $ renpy.pause(2)
    scene 5
    with slowdissolve
    $ renpy.pause(2)
    scene 6
    with slowdissolve
    $ renpy.pause(2)
    scene 7
    with slowdissolve
    $ renpy.pause(2)
    scene 8
    with slowdissolve
    $ renpy.pause(2)
    scene 9
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
    scene 10
    with slowdissolve
    i """
    In my\ndreams...

    I\nalways see\nyou.
    """
    scene 11
    with slowdissolve
    re """
    I know...

    But\nI am here\nnow.
    """
    i """
    Where\nhave you\nbeen?

    I\nmissed\nyou.
    """
    stop music fadeout (10)
    re """
    I won't\ngo\nanywhere.

    Anymore...
    """
    play sound "ending.ogg" fadein(2)
    scene 12
    with slowdissolve
    $ renpy.pause(2)
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
    scene 13
    with slowdissolve
    i """
    At\nthat\ntime...

    Everithing was\nsimpler\nback then.

    We just\nhad to study.

    Life was\nway far away\nfrom us.

    We knew\neach other\nsince the\nyear before.

    We\nalready were\nclose.
    """
    scene 14
    with slowdissolve
    re """
    I\nalways thought\nyou had...

    Something\nspecial\nwithin you.

    And,\nback then...

    Your smile\nmade me\nso happy...

    Every day\nI went to school\njust thanks\nof that.

    You were\nmy reason\nto live.

    I don't\nsay that\nlightly...

    Without\nyou...

    Nothing\nwould have had\nsense.

    And\nthat day...
    """
    scene 15
    with slowdissolve
    re "All these\nfeelings..."
    scene 16
    with slowdissolve
    re "Suddenly\naccumulated."
    i """
    I still\nremember...

    You\nmoved toward\nthe door...

    Then\nstopped.
    """
    scene 17a
    with slowdissolve
    i "And\nslowly..."
    scene 18a
    with slowdissolve
    i "You turned\ntoward me."
    show 19b:
        yalign 0.0
    with slowdissolve
    $ renpy.pause(2)
    show 19b:
        subpixel True
        yalign 0.0
        linear 6.0 yalign 1.0
    $ renpy.pause(8)
    show 19a:
        yalign 1.0
    with slowdissolve
    i """
    You\nsmiled back\nat me.
    """
    scene 20
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
    scene 21
    with slowdissolve
    i """
    Maybe\nit was...

    I've always known\nyou coldn't\nlove me\ncompletely.

    I knew\nyour moans\nweren't happy.

    But sad,\nevery night.

    And that\nthose\ntears...

    Meant\nyou weren't feeling\nthat much.
    """
    play movie "22.ogv" loop
    show movie with slowdissolve
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
    re """
    People\nalways think\nthat...

    People like me\nare unhappy.

    I knew you\nthought that,\ntoo.

    Many times\nI tried\nto talk...

    To\nexpress\nmy feelings.

    But you\nwouldn't\nlisten.

    So\nI ran\naway.

    And\ndecided that\nit was you\nwho abandoned me.

    Just to\nnot\nsuffer.
    """
    show 19b:
        yalign 1.0
    with slowdissolve
    stop movie
    $ renpy.pause(2)
    show 19b:
        subpixel True
        yalign 1.0
        linear 6.0 yalign 0.0
    $ renpy.pause(6)
    scene 18b
    with slowdissolve
    $ renpy.pause(2)
    scene 17b
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
    scene 24
    with slowdissolve
    i "How much\nunsatisfied\nyou were."
    scene 25
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
