
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

label start:
    $ yasu_comp = False
    $ claire_comp = False
    $ stefan_comp = False
    $ julie_comp = False
    $ kim_comp = False
    $ take_comp = False
    $ stories_comp = 0
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
    stop music fadeout(2)
    scene day0
    with slowfade
    $ renpy.pause(3)
    play music "intro.ogg" fadein(3)
    scene desk
    with slowdissolve
    """
    I still remember that time...

    It seems like ages ago, now.

    And yet, even though so much has happened...

    Those events still affect me.

    And, sometimes, that apartment fades into this hotel room.

    Since I came here, each day has had the same routine...

    Wake up.

    Let the day flow.

    Get back to the room.

    Now that I think about it...

    Things weren't any different before.

    For now, anyway, I just need to write down today's entry.

    And then go to bed.

    Just as usual.
    """
    jump deskscreenintro

label deskscreenintro:
    call screen deskintro

label flowerintro:
    """
    These flowers always make me remember...

    That's why I try to keep them alive so hard.
    """
    jump deskscreenintro
label calendarintro:
    if julie_comp == True:
        """
        Dear Julie...

        Time passes endlessly.

        Sometimes slowly, other times rapidly.

        And I often feel as if I can't keep track of it.

        I really hope you can, now.
        """
        jump deskscreenintro
    if julie_comp == False:
        """
        Time passes.

        Days go by.

        Here, on this calendar, the appointments of last month are all marked.

        All these people...

        All their dreams...

        Marked on paper and into my memories, indelible.

        And, among them, the images and words from Julie's room still clearly ring, heavy.

        Through her recalling her past life, I can still feel a light lingering accross the tunnel...
        """
        jump day3
label mugintro:
    """
    This mug...

    It's so old...

    And it brings back so many sweet memories.

    I miss them so much...
    """
    jump deskscreenintro
label photosintro:
    if stefan_comp == True:
        """
        Stefan...

        Even though he has always scared me...

        I still worry about him a lot.

        I hope everything is going good for him.
        """
        jump deskscreenintro
    if stefan_comp == False:
        """
        When I was still a guest here...

        I used to take many photos of the hotel and the guests.

        Many of them are not here anymore.

        And the others...

        Well, we are not so friendly anymore.

        Time passes and things change, right?

        This reminds me...

        A lot of time ago, Stefan was just like me.

        He wanted to listen to people.

        To know about their life.

        Even though he often said he didn't care about others...

        He spent a lot of time with some of the guests.

        Just...

        What happened then?
        """
        jump day4
label booksintro:
    if claire_comp == True:
        """
        All these books...

        I'll never grow a collection as huge as Claire's.

        But it's nice to always remember that we shared an interest.

        I hope she's still reading, wherever she is now.
        """
        jump deskscreenintro
    if claire_comp == False:
        """
        Some books and graphic novels I really care about.

        The hotel's delivery service is very useful, I'd say.

        Without it I would have died of boredom.

        This reminds me of...

        Claire.

        She used to read lots and lots of books, everyday, as she was working on her various projects.

        And if I close my eyes, I can still remember that morning...
        """
        jump day2
label lampintro:
    if yasu_comp == True:
        """
        This lamp always reminds me of Yasu's light, now.

        I wonder if he is with his wife, now...
        """
        jump deskscreenintro
    if yasu_comp == False:
        """
        Just a normal lamp.

        On the base the hotel's name is written in gold.

        Yasu, from the first floor, used to have the room with the best light in all the hotel.

        I still remember the vast field...

        The sweet sound of the wind...

        And Yasu's posure as he observed the horizon...
        """
        jump day1
label diaryintro:
    if stories_comp <= 5:
        """
        It's too soon to write today's entry...
        """
        jump deskscreenintro
    if stories_comp == 6:
        """
        Do I really want to go to sleep already?
        """
        menu:
            "Yes.":
                scene diary
                with slowfade
                """
                Here in the Homunculus Hotel,\npeople find refuge from the world's danger and uncertainties.

                They get here in order to find a place that could be safe.

                A place that could help them get better.

                That's why all the rooms are always occupied by someone.

                And you can see them...

                Walking through the corridors.

                Having a lonely breakfast.

                Passing by the courtyard...

                Each of them alone.

                The first day I spent here seems so far away, now.

                First a guest, and then a member of the staff.

                I think it's been three years.

                And I've been writing this diary only for the last two months.

                I came to this hotel...

                Well, because someone told me that\nthe rooms show the guests' personal and intimate dreams.

                Dreams from the past.

                Dreams of possible and multiple futures.

                Dreams of fears or desired achievements.

                But...

                Even after all the time I spent here...

                I'm still unable to see mine.
                """
                jump day1
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
    It's early in the morning.

    I wake up with a strange headache.

    Not the best way to start a day, I guess...

    The light that comes from the window is soft, pale.

    And my body finds it difficult to get up.

    But it has to.

    And so I force myself to lift my body...

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

    Silent and empty, as always.

    It's been a couple of months since I started working here.

    At first, I was worried.

    The idea of an hotel which offered a support service to the guests still seemed...

    Well, strange.

    But I got confident with it.

    Both with the idea and the job itself.

    I just have to visit some of them three\nor more times a week, depending by the guest.

    And then spend some time with them, nothing too stressing.

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
    """
    jump floor1_1
label portrait2_1:
    """
    The director is painted beautifully.
    """
    jump floor1_1
label mirror1:
    """
    Me, myself and I.
    """
    jump floor1_1
label yasu1:
    if yasu_comp == True:
        """
        Yasu's session is already finished.

        I should check out the other room.
        """
        jump floor1_1
    if yasu_comp == False:
        """
        Room 101.

        It's occupied by a man named Yasu.
        """
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
        As I open the door and enter, I find myself in a vast field.

        Yasu is right there, next to me, looking at the horizon.
        """
        i """
        Hello,\nMr. Yasu.
        """
        menu:
            "How are you today?":
                y "Oh, fine,\nthanks."
        y """
        Just...

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
                y """
                Hmm...

                It seems\nI can't fall asleep.

                No matter\nhow hard I try.

                So I just stand here\ndoing...

                Well,\ndoing nothing.

                And the more\nI try to sleep...

                The more\nI can't.

                I realized,\nlately that\nI want to sleep...

                But the scenery\nis too beautiful.
                """
            "What have you been up to?":
                y """
                Oh, the usual...

                I just look\nat the field...

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
                        ## Spostare questo pezzo come risposta al passaggio "It could mean that you feel alone."?
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

                        You'll have\nto struggle\nanyway.
                        """
            "Are there thoughts that still haunt you?":
                $ shame = True
                y """
                Sometimes\nI still wonder...

                How is\nmy family doing?

                And what about\nmy friends?

                So much time\nhas passed,\nsince the last time\nI saw them all...

                It still feels selfish,\nto be here.

                And yet, I feel good.

                Like never before,\nyou know?

                Do you think...

                I should be ashamed\nfor feeling\nso happy here?
                """
                menu:
                    "Why should you?":
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
                            "Only you have that answer for that question.":
                                y "Probably, yeah..."
                            "It's not your fault for ending up in here.":
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

                        And meanwhile\nshe painted,\nevery evening.

                        She didn't accept\nany kind\nof tip.

                        And any kind\nof appreciation.

                        For her,\nnothing was ever\nenough good.

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
                            "What kind of paintings she made?":
                                y """
                                Sometimes\nabstracts.

                                Other times\nstill lives.

                                It depended\nby the feelings.

                                That's why\nI'm curious.

                                But,\nknowing her,\nI'm sure she just\npainted a hat.
                                """
            "It could mean that you feel alone.":
                $ alone = True
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
                y """
                You must have\nbeen very free,\nthen!

                That's good...
                """
                menu:
                    "Is it related to something?":
                        y """
                        Nothing in particular,\nno.

                        It's just the way\nI'm feeling.

                        I'm starting\nto realize that...

                        All my life\nhas been\n just like that.

                        A floating weed...

                        Gently swept away\nby the current.
                        """
                    "Have you dreamt of floating weeds?":
                        y """
                        No.

                        Only the field,\nas usual.

                        But I got\nthis image\n in my mind.
                        """
            "What do you mean?":
                y """
                You see...

                I've been\nbetween freedom\nand slavery...

                For all my life.

                A slave,\nas I had to\nwork for a company.

                But free,\nas I could do what\nI wanted anyway.
                """
            "Never.":
                y """
                Well,\nthat's a pity,\nbut...

                You know.

                Never\nsay\nnever.
                """
                menu:
                    "What's with the floating weeds?":
                        y """
                        Well...
                        """
                    "Is that how you feel today?":
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
                y """
                Yes.

                And yet...

                Something\ntroubles me.
                """
            "Yet, you dream of a field...":
                menu:
                    "Any idea why?":
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
        menu:
            "Maybe you only have to accept it...":
                i "And let it go, so that peace may come."
                y """
                Yes.

                I'm now sure of this.
                """
        y"""
        It's...

        Strange.

        Thinking about\nall these memories...

        Made me\nfeel better.

        Way better,\nthanks to your help.

        The thoughts are\nslowly disappearing.

        In the end...

        It's useless\nto feel bad.

        I can't turn\ntime back.

        So I might\nas well\nmove on.

        And find my peace.

        So...

        I think\nI'm ready.
        """
        menu:
            "Are you sure?":
                y """
                Yes.

                I finally am.

                I want to\npass away.

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
        with slowfade
        stop movie
        play music "day1.ogg" fadein(2)
        jump floor1_1
label claire1:
    """
    Room 102.

    It's occupied by a woman named Claire.
    """
    jump floor1_1
    return

label day2:
    $ discover = False
    $ walone = False
    $ dream = False
    $ guests = False
    $ sdifferent = False
    stop music fadeout(2)
    scene black
    with fade
    scene day2
    with quickfade
    $ renpy.pause(3)
    play movie "breakfast.ogv" loop
    show movie with slowdissolve
    play music "day2.ogg" fadein(2)
    """
    Today seems like it could be a good day.

    I woke up with your face in my mind and I was smiling while sleeping.

    Or at least I guess I was.

    Well, I hope I was, actually.

    But anyway...

    I'm thinking of you, this morning.

    And when I think about you...

    There's always a mixture of happiness and melancholy.

    But the day feels less heavy.
    """
    scene corridor
    with slowfade
    stop movie
    """
    Today it's the turn of the first floor again.

    So, room 101 and 102 and then the appointments for this week are almost over.
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
    It's me.

    Wait, are those new wrinkles?

    Ugh.
    """
    jump floor1_2
label yasu2:
    """
    Room 101.

    It's occupied by a man named Yasu.
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
                c """
                I don't know!

                Hmm, maybe...

                But I can't even\nunderstand what.
                """
            "You always work so much...":
                menu:
                    "Why don't you rest a little?":
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
                i "Have you seen\nanything particular,\nlately?"
                c """
                Hmm.

                It's strange...

                I don't think\nI dreamed at all,\nlately.
                """
                menu:
                    "You sure?":
                        menu:
                            "It's ok if you don't want to talk about it, though.":
                                c """
                                I'm still not ready,\nsorry...

                                But please,\ncould you stay here?

                                I think\nI need\nsome company...
                                """
                            "You know the room doesn't lie.":
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
                c """
                Nothing much.

                Just working\non a scene.

                Or at least\nI'm trying.
                """
                menu:
                    "Is it an important scene?":
                        c """
                        Yes, it is.

                        But...

                        Well, I can't seem\nto be able to\nclose it.

                        I keep\ngetting stuck.
                        """
                    "You never told me about the whole project, though!":
                        c """
                        Yes,\nI know...

                        But\nit's because...

                        Well,\nI'm still very unsure.
                        """
                        menu:
                            "What are you unsure about?":
                                c """
                                I just don't feel\nconfident enough.

                                I try to work\nand get stuck.

                                I try to distract myself\nand still think\nabout it.

                                I don't\nknow what to do\nanymore.
                                """
        c """
        Tell me,\nIsabelle...

        Have you ever\nfound yourself...

        Blocked?
        """
        menu:
            "What do you mean?":
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
                $ rest = True
                c """
                It's difficult, but...

                I'll try, thanks.
                """
            "Don't pressure yourself too much.":
                $ nopressure = True
                c """
                I know, but...

                I want to finish\nthis piece so much.

                Hmm...
                """
        c """
        All's fine.

        I started reading\na new book!

        Have you ever read\nSoul Mountain?

        It's a novel\nwritten by\nGao Xingjian.

        I've known him\nfor years...

        And yet,\nI never read anything\nhe made until now.

        You know...

        The story\nof this character\ntravelling to \nfind himself...

        Somehow\nI can relate to him.

        I don't know\nhow to explain...

        It's difficult\nto use words,\nbut...

        This novel\ntouches my heart.

        Here, let me\nread you\na passage...

        'Sitting at rest\nknow not to discuss\nthe shortcomings\nof other people'

        'Setting out\non a journey\nfully appreciate\nthe beauty of\nthe dragon river.'

        At some point,\nit also gave me\nsome ideas\nfor a passage!

        Do you want\nto hear what\nI wrote?
        """
        menu:
            "Yes, I'd be glad to.":
                c """
                Great!

                So...

                It's the scene where\nthe protagonist\nenters in\nthe dinner room.

                She looks around,\nstudies the people\nin the room...

                And as she realize\nthey all hate her,\nshe...

                Well,\nthat's all.

                For now,\nat least.

                I'm writing very little,\nlately.
                """
            "I'm more interested in the process.":
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
                        c """
                        Hmm...

                        I can't make\na movie by myself.

                        I need the\nhelp of others.

                        I need to\nwork with other\npeople.
                        """
                        menu:
                            "You could ask the other guests!":
                                $ guests = True
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

                                That\nwe used to make\nvery personal movies\ntogether.

                                We struggled\nagainst\nproducers and labels.

                                Getting even a\nsmall amount\nof funds\nalways seemed\nimpossible.

                                At that time\nI had\nso many ideas...

                                As if\nhaving no money\nonly got me\nstronger.

                                I wanted to spit\non each producer's\nface.

                                To each 'no'\nI answered\nwith a curse.

                                I\ncouldn't care less\nabout\ntheir opinions.

                                About\ntheir market analysis.

                                About\ntheir ideas\nof the public.

                                They used to say...

                                'The public\nlikes this,\nso we need\nto make it.'

                                But\nthe truth\nis that...

                                The public likes\nwhat you give them.

                                There's no need\nto try to\nplease them.

                                There's no need\nto be obedient\npuppies.

                                And\nI didn't like\nthe idea of being\nan\ninsincere director.

                                I wanted\nto be\nme.

                                So,\nwith this\nfriend of mine...

                                We made\nwhat\nwe wanted\nto make.

                                The length\ndidn't matter.

                                The format\ndidn't matter.

                                The genre\ndidn't matter.

                                And when we\ncouldn't find actors,\nwe played\nthe characters.

                                We had\ntons and tons\nof projects.

                                My entire house\nwas filled\nwith screenplays.

                                I miss\nthat time\nso much...

                                Maybe\nwhat I miss\nis love?

                                Maybe\nit was love\nwhat inspired me...
                                """
                            "Why don't you make something different, then?":
                                menu:
                                    "Like a novel, for example.":
                                        $ sdifferent = True
                                        c """
                                        I don't know...

                                        I made movies\nall my life.

                                        I don't know\nif I'd be\ncapable.

                                        Gues I'll\nthink about it.
                                        """
                    "What's worrying you?":
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
                                        c """
                                        Well,\nif you say so...

                                        I guess trying\nwon't hurt that much.
                                        """
                                    "I think you should confront your dream. ":
                                        $ dream = True
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
                c """
                Hmm.

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
                    "You'll find it again.":
                        c """
                        Thanks,\nIsabelle.

                        Really.

                        Oh, wait!

                        I think\nwe passed\nour session's\nending!

                        I'm\nso sorry...
                        """
                    "I'm here for you.":
                        c """
                        Thanks,\nIsabelle.

                        Really.

                        Oh, wait!

                        I think\nwe passed\nour session's\nending!

                        I'm\nso sorry...
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
            It's been some days,\nnow...

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
                    c """
                    Y-yeah...

                    Maybe I can...

                    It will\ntake time,\nbut...

                    I'll be\nable to...

                    Or\nat least\nI\nhope.
                    """
        if guests == True:
            c """
            Oh,\nwell...

            The movie...

            Envision\nthe movie...

            The places,\nthe characters,\nthe light.

            We used to\nlook out for light\ntogether...

            And that...

            I could\nfeel like that\nagain...?

            I could...\nat least try.

            Yes...

            Of course!

            Thankyou,\nIsabelle.

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
        But...

        You know...
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

        It's time\nto say\ngoodbye.

        To them\nand to you.

        Thank you.

        You were the\nkindest person.

        I'll hold you\nin my heart.
        """
        $ claire_comp = True
        $ stories_comp += 1
        stop music fadeout(2)
        scene corridor
        with slowfade
        stop movie
        play music "day2.ogg" fadein(2)
        jump floor1_2

label day3:
    $ cat = False
    $ cat_pet = False
    stop music fadeout(2)
    scene black
    with fade
    scene day1
    with quickfade
    $ renpy.pause(3)
    play music "day1.ogg" fadein(2)
    play movie "smoking.ogv" loop
    show movie with slowdissolve
    """
    Sometimes I observe the hotel's courtyard.

    It's almost empty, in the morning...

    And the soft breeze that caresses me, helps me concentrate.

    And get ready for the day.

    It's in moments like these that I can think more straightly.

    In which I don't lose myself through memories.

    And in which I miss you the most.
    """
    scene corridorf2
    with slowfade
    stop movie
    """
    And here I am.

    The second floor, finally.

    I'm almost halfway through the month, now.

    But I can't stop worrying.

    I almost don't know Julie, yet.

    Will it go well?
    """
    jump floor2_1
label floor2_1:
    if julie_comp == False:
        call screen floor2_1
    if julie_comp == True:
        stop music
        scene desk
        with slowfade
        play music "intro.ogg" fadein(3)
        $ renpy.pause(3)
        jump deskscreenintro
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

        I should check on Stefan.
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
        As I stumble into Julie's room...

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
        i """
        So...

        May I ask\nyou...
        """
        menu:
            "How was your life before the Hotel?":
                j """
                My life\nbefore...

                Well,\njust normal,\nI guess.

                I worked\nin a wonderful\noffice.

                Had\na wonderful\nhusband.

                In\na wonderful\ncity.
                """
                i "Uh, all very...\nwonderful!"
                j """
                Right?

                I\nalways\nwondered...

                How did I\nget there?

                You know,\none moment\nbefore\neverything\nwas average.

                And then...

                One moment\nlater\neverything\nwas wonderful!
                """
                menu:
                    "I imagine you were very happy!":
                        j """
                        Yeah...

                        Of course\nI was.
                        """
                        i "...now you\ndon't seem\nso sure."
                        j """
                        It's just\nthat...

                        You know,\nyou spend your\nwhole life,\nand then...

                        Things\njust\nend.

                        And you\nfind yourself\nin a strange\nhotel.

                        And you're\nonce again\nalone.

                        Not sure if\nI'm happy,\nnow.
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
                        """
            "What do you think about your room?":
                j """
                ...

                Well...

                I think you\ncould imagine\nby yourself,\nbut...

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

                And I don't\nwant to\nremember it.
                """
                i "Ok, then,\nlet's not talk\nabout it."
                j "Thanks.\nHeh."
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
        Ok.

        Childhood's ok.

        So,\nyou want me\nto tell you\nabout it,\nright?
        """
        i "If you\nfeel\nlike it."
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

        Uhmm...

        Sorry,\nI...

        I think\nthat's been\na lot\nfor today,\nalready.

        Would you mind\nif we continue\nanother day?

        I'm...

        Tired.

        Hahah...
        """
        i """
        No problem\nat all.

        See you\nnext time,\nJulie.
        """
        j "Ok, bye.\nHah."
        $ julie_comp = True
        $ stories_comp += 1
        stop music fadeout(2)
        scene corridorf2
        with slowfade
        stop movie
        play music "day1.ogg" fadein(2)
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
    with fade
    scene day1
    with quickfade
    $ renpy.pause(3)
    play music "day3.ogg" fadein(2)
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
    scene corridorf2
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
        scene desk
        with slowfade
        play music "intro.ogg" fadein(3)
        $ renpy.pause(3)
        jump deskscreenintro
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
    Today something feels different...
    """
    s """
    Welcome back,\nIsabelle.

    How\nare you doing\ntoday?
    """
    menu:
        "I feel relaxed.":
            s """
            Being\nrelaxed...

            Or\nbeing\nstressed.

            Such\nstrange\nconcepts.

            They don't belong\nto me,\nanymore.

            And\nI don't belong\nto them,\nanymore.
            """
        "Sad. Happy now?":
            s """
            No.

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
    I\nrealized something,\nlately.

    We are\nnot humans\nanymore,\nIsabelle.

    So...

    We\nmay just\nmove on.

    And\nnot care about\nhuman things.
    """
    menu:
        "What about these eyes, then?":
            s """
            They\nare only\nmemories.

            Nothing\nmore.

            Memories\nI try to avoid\nby looking through\nthe mirror.
            """
            i "They seems\nto haunt you."
            s "Sometimes."
            menu:
                "Any idea why?":
                    s"""
                    If you think\nit's some trauma\nfrom my childhood...

                    Or other\nbullshit\nlike that...

                    I'm sorry\nto disappoint\nyou.

                    I already\ntold you that\nmany times.
                    """
                    i "Then what\nis it?"
                    s """
                    ...

                    Some\ntime\nago...

                    'Before',\nI should\nsay.

                    I was\na different\nperson.

                    As you\nalready know,\nI was a musician.

                    Admired\nby fans.

                    At times\nby critics.

                    And by\nother musicians.

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
                            """
                        "What are you looking for?":
                            s """
                            For myself...

                            I guess.
                            """
        "What makes you think we're not humans?":
            s """
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

                    How tedius\nit is.

                    And how much\nit destroys\nyou.

                    But\nwe don't have\nthe time\nto cry.

                    We don't have\nthe time\nto be sad.

                    When we\ncome here,\nwe think\nwe'll have all\nthe time we need.

                    We think\nour rooms\nwill help us.

                    That we\nwill understand\nourselves.

                    Or\nfind peace.

                    But\nall we find\nis this pain.

                    And\njust like\nout there...

                    We don't have\nall the time\nwe want\nto resolve it.
                    """
                "I do...in a way.":
                    s """
                    I know,\nit's not the same\nfor everyone.

                    But\nyou feel\nit.

                    That pain\nthat won't\ngo away.

                    The pain\nthat haunts you\nevery night.

                    That\ntorments you\nin your sleep.

                    That reminds you\nof painful\nmemories.

                    And makes\nyou feel\nalone.

                    That pain\nwill follow us\nuntil\nthe very end.

                    And I'm afraid\nthis hotel can't\navoid that.
                    """
    s """
    Well.

    I think\nI talked enough,\nfor today.

    Will I\nsee you\ntomorrow?
    """
    i """
    Yes...

    See you\ntomorrow.
    """
    $ stefan_comp = True
    $ stories_comp += 1
    stop music fadeout(2)
    scene corridor
    with slowfade
    stop movie
    play music "day3.ogg" fadein(2)
    jump floor2_2
