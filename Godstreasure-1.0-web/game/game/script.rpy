define flagc =False
define flaga =False
define flagb =False
define flagd =False
define o = Character("oldman")
define xy = Character("You")
define m = Character("Mom")
define mm = Character("Mom")
define Kim = Character("Kindaichi", image="jintianyihead", color="#FFFF00")
define tc = Character("Teacher")
define xue = Character("Snow", image="xuehead", color="#CC33CC")
define lihua = Character("lily",image="lihua2head", color="#33CCCC")
define wumu = Character("Mr.Wood",image="wumuhead", color="#FF0000")
define hetian = Character("Hetian", image="hetianhead",color="#66CC99")
define x = Character("???",color="#CCCCCC")
define zion = Character("Zion",image="zionhead", color="#0000CC")
define juan = Character("Juan",image="juanhead", color="#CC0000")
define ch = Character("ChiFeng",image="chifenghead",color="#66CC99")
define reed = Character("Reed",image="Reedhead", color="#CC33CC")
define rv = Character("Raven",image="ravenhead", color="#0000CC")
define moon = Character("Moon",image="moonhead", color="#FFCCCC")
define gu = Character("village children",color="#CCCCCC")
define police = Character("Police officer",image="policemanhead",color="#CCCCCC")
define rf = Character("Raven's father",color="#CCCCCC")
define ott = Character("123",image="jin123head",color="#CCCCCC")
default points = 0
image side jintianyihead="jin.png"
image side jintianyihead ba="jin2.png"
image side jintianyihead cc="jin3head.png"
image side jintianyihead bz="jin4head.png"
image side xuehead="xue.png"
image side xuehead cf="xuehead3.png"
image side lihua2head="lihua2head.png"
image side hetianhead="hetianhead.png"
image side hetianhead yy="hetianhead2.png"
image side zionhead="zionhead2.png"
image side juanhead="juanhead.png"
image side chifenghead="chifenghead.png"
image side chifenghead nm="chifenghead2.png"
image side Reedhead="Reedhead.png"
image side Reedhead gb="Reedheadx.png"
image side moonhead="moonhead.png"
image side ravenhead="ravenhead.png"
image side wumuhead="wumuhead.png"
image side policemanhead="policemanhead.png"
image side jin123head="jin123head.png"

label start:
    play music "background.mp3"
    scene bg
    with pixellate
    $ Kim_point=0

    "With the sunset, an old man was wandering on the beach"
    "I've noticed him for some time"
    menu st:
        "Maybe it's time i went and saw him":
            "You walk slowly towards the old man"
            "You watch him closely"


        "go home for dinner":
            xy"(I heard that a psychopath had recently escaped from a mental hospital)"
            xy"(My god, it can't be this old man!!??)"
            xy"(aaaaaaaaaaaoooooooaaoiiiooooa)"
            xy"(I'd better go home for dinner.)"
            jump end1


    "There was an indescribable sadness in his eyes that was clearly contagious"
    "My curiosity impelled me to have a talk with the old man"
    "The old man looked at me, smiling without a word"
    o "Once upon a time there was a child named four lang, he buried the treasure and silently made a vow"
    o "He hoped that one day the people in pain and despair could use this treasure to move toward a new future"
    o "I see you as I saw myself, boy.Do you want to hear my story?"


menu:
    "I'd love to hear it":
        xy "I'd love to hear it"
        jump story1
    "Is he a psychopath?":
        xy "(Is he a psychopath?)"
        xy "(I'd better run!!!)"
    "Beat up this old headache full of nonsense":
        "You swing your fist at the old man"
        "You don't expect this old man to block your fist with his backhand"
        "Then he hits you to the ground with an uppercut"
        "You look at the old man with astonishment"
        "Your subconscious is telling you to run!!"
        "You escaped the beach as fast as you could"
label end1:
scene br1
with pixellate

"you hurried away from the old man. you were sure he was a psycho!"
xy "Why are there so many strange people now!!!"
return

label end3:
scene br1
with pixellate
"You were ruthlessly expelled from school"
Kim "Why !!!"
return

label story1:
"The old man gave me a cold look and patted me on the shoulder."
o "Fifty years ago........"
$renpy.movie_cutscene("op.avi")
scene school
with pixellate

stop music

"Class bell rings!!"
Kim ba"agghh"
show kim at left
with dissolve
Kim ba"Oh my god!!I have to hurry to class."
Kim ba"Or this will be the 21st time this month"
"Class bell rings again!!"
Kim ba"Don't rang again!"
Kim ba"Here I come, teacher!!!!"
"Kindaichi,with super reasoning ability and determination.But, each class grade is in pass line below.In other words, this person can do nothing but reason..."
"You can say that he is a man born to reason, or you can say that he is an idiot who can only reason..."

scene classroom2
with pixellate
show teacher at right
with dissolve
play music "notalone.mp3"
tc"Ahem, based on a fair, open, fair vote.I decided to make Snow the new monitor in this class."
tc"Please clap your hands!!"
show kim at left
with dissolve
Kim "(After being such a troublesome monitor, what does that guy plan to do?)"
tc"Ahem,then Snow, as the new monitor, what do you want to say to your classmates?"
show meixue
with dissolve
xue"Ok, although I have some shortcomings, but I will use their own efforts to give back to everyone!"
menu mnt:
    "Boring speech, anyone can say that.":
        Kim "Boring speech, anyone can say that."

        xue"Kindaichi,Can you respect me!!(shy)"
        Kim "Ha ha ha, you look so funny angry, ha ha ha ha ha!"
        tc"Ahem"
        tc"21 tardiness, plus one disruptive session.Kindaichi, please come to the principal's office today."
        Kim "ah........"
        "Kindaichi was expelled, the end of memory"
        jump end3

    "Silent applause.":
        Kim "(Although I think this guy is not a leader)"
        Kim "(But...I have a good relationship with her, is it possible to delete my attendance record??)"
        $ Kim_point +=5
        Kim "(Yeah!!!!)"


xue"Next, welcome the new students who will be transferred to our class this term!!"
"The crowd stared at the classroom door"
"A beautiful girl walked slowly from the door to the front of the platform"
"The crowd stared at the classroom door"
hide teacher
with fade
show lihua at right
lihua "Hi, I'm lily, a transfer student. Nice to meet you."
Kim "Wow, that's cute."
xue"......."
Kim "Wow, that's cute."
Kim "Snow White skin, standard figure, lovely voice, this is love..."
xue"......."
xue"hum"
xue"....."
scene classroom
with pixellate

"6：00 pm"
show lihua
with dissolve
lihua "Are you Mr. Kindaichi?"
Kim "how did you know my name?."
lihua "I heard your story from that man"
Kim "Which people?"
lihua "It doesn't matter. I heard you were a great high school detective."
lihua "I have a puzzle on my side. Can you solve it?"

menu dk:
    "of course":
        lihua "Well, as the man said"
        hide lihua
        with dissolve
        "Lily put a box in front of me with a combination lock on it."
        lihua "I have three pictures in my hand. This is a hint about the password. The password is four digits."
        lihua "Ready for the guessing game?"
        menu dr:
            "Let's start":
                show 1962
                with dissolve
                lihua "The first picture, the mysterious death of Marilyn Monroe in 1962"
                hide 1962
                with fade
                show 1963
                with dissolve
                lihua "The second picture is Nixon's assassination in 1963"
                hide 1963
                with fade
                show 1964
                with dissolve
                lihua "The third picture, the 1964 Tokyo Olympic and paralympic games"
                hide 1964
                with fade
                lihua "The password has nothing to do with these three pictures!"
                lihua "Do you know the password?"
                menu ds:
                    "A piece of cake":
                        jump cod1



                    "I'll think it over. You say it again":
                        jump dr



                    "Say it again please. I wasn't listening carefully":
                        lihua "......."
                        lihua "(What an idiot)"
                        $ Kim_point -=10
                        lihua "sure, I'd be happy to say it again."
                        lihua "I have three pictures in my hand. This is a hint about the password. The password is four digits."
                        lihua "Ready for the guessing game?"
                menu dm:
                    "Sorry, I still didn't catch what you were saying.":
                        lihua "......."
                        lihua "You let me down"
                        "Memory break, game over"
                        jump start



                    "I know":
                        jump dr


    "I can't":
        show lihua
        with dissolve
        lihua "??????"
        Kim "........"
        lihua "??????"
        Kim "........."
        lihua "You're so funny. I'll say it again. It's a simple game"
        Kim "(I really can't)"
        jump dk


    "Silently walk away":
        show lihua
        with dissolve
        lihua "Wait, what are you doing?"
        Kim "School's over. I'm going home"
        lihua "You're not interested in passwords?"
        Kim "bingo!!!"
        $ Kim_point -=20
        lihua "........."
        lihua "The password is 5987. Open it yourself.goodbye"
        Kim "goodbye"
        jump story5
menu cod1:
    "The first number is?"
    "1":
        lihua "wrong"
    "2":
        lihua "wrong"
    "3":
        lihua "wrong"
    "4":
        lihua "wrong"
    "5":
        $ flaga =True
        lihua "Bingo"
        $ Kim_point +=5

    "6":
        lihua "wrong"
    "7":
        lihua "wrong"
    "8":
        lihua "wrong"
    "9":
        lihua "wrong"
if flaga:
    jump cod2
else:
    jump cod1
menu cod2:
    "The second number is?"
    "1":
        lihua "wrong"
    "2":
        lihua "wrong"
    "3":
        lihua "wrong"
    "4":
        lihua "wrong"
    "5":
        lihua "wrong"
    "6":
        lihua "wrong"
    "7":
        lihua "wrong"
    "8":
        lihua "wrong"
    "9":
        $ flagb =True
        lihua "Bingo"
        $ Kim_point +=5

if flagb:
    jump cod3
else:
    jump cod2
menu cod3:
    "The Third number is?"
    "1":
        lihua "wrong"
    "2":
        lihua "wrong"
    "3":
        lihua "wrong"
    "4":
        lihua "wrong"
    "5":
        lihua "wrong"
    "6":
        lihua "wrong"
    "7":
        lihua "wrong"
    "8":
        $ flagc =True
        lihua "Bingo"
        $ Kim_point +=5

    "9":
        lihua "wrong"
if flagc:
    jump cod4
else:
    jump cod3
menu cod4:
    "The fourth number is?"
    "1":
        lihua "wrong"
    "2":
        lihua "wrong"
    "3":
        lihua "wrong"
    "4":
        lihua "wrong"
    "5":
        lihua "wrong"
    "6":
        lihua "wrong"
    "7":
        $ flagd =True
        lihua "Bingo"
        $ Kim_point +=5

    "8":
        lihua "wrong"
    "9":
        lihua "wrong"
if flagd:
    jump story4
else:
    jump cod4

label end2:
scene br1
with fade
"You suddenly open your eyes and find yourself in bed, everything is normal."
"Is it only a dream?But something seems wrong..."

return

label story4:
scene classroom
with dissolve
lihua "Wow, you are amazing"
"The detective points is [Kim_point] "
lihua "There's something important here. It's two invitations.For you and snow.So, bye!!"
Kim "Oh, wait a minute.Invitation to what??"
lihua "It's a secret"
Kim "What? It's so mysterious.Let me see!"
Kim "Well, if it's something bad, it's embarrassing."
Kim "Go home and see. Go home and see"
xue"what's that in your hand?Kindaichi!"
Kim "!!!!"
Kim "this is......"
xue"This box looks expensive!!"
Kim "hahaha,yeah.it is so expensive....."
xue"Lily didn't give it to you, did she??"
Kim "!!!!!!!!"
xue"I hit the nail on the head!"
Kim "Yeah, yeah?See you tomorrow, snow!(Run!!!!)"
xue"Give me stop!"
"Snow chased jintian a five street, two people because of physical exertion, temporarily stop."
jump story5

return

label story5:
scene scenestrat2
with pixellate
Kim "Stop chasing. Stop chasing.There are two invitations, one for you."
xue"Did lily give it to you?"
Kim "That's right. Do you want to see it now?"
xue"Well, I don't really trust you.kindaichi"
Kim "All right, all right.Wait a sec"

"The car horns honked"
x"Hey，kindaichi！"
Kim "Mr. Wood！"
"Your detective point is [Kim_point] now"

scene scenestart3
with pixellate

show kim at left
with dissolve
Kim "Mr. Wood！"
show wumu at right
with dissolve
Kim "So, lily gave me the invitation that you entrusted her with."
wumu"Yeah, long time no see, detective.You are my number one guest on this show!"
Kim "alright！"
wumu"I don't know if your reasoning has declined.kindaichi!!!"
Kim "It's okay, it's okay, don't try me out with some silly mystery games, okay?"
wumu"Please listen!!"
Kim "........"
xue"Hee Hee"
wumu"Mr Zhang was murdered, three servants A, B, C three people are A mastermind, by his hands to kill Mr Zhang, the other two are accomplices, responsible for the stolen property transfer."
wumu"The police questioned the three of them about who killed Mr. Zhang."
wumu "A said, I didn't kill Mr. Zhang, nor did I kill Mr. B. B says, I did not kill anyone. I didn not kill C. C said, I didn't kill him, and I don't know who killed him."
wumu "In fact, what each of them said was half true and half false.According to this characteristic, the police soon found out who killed Mr. Zhang.Do you know who the killer is?"
menu io:
    "A":
        wumu"Wrong, please be serious"
        $ Kim_point -=5
        jump io



    "B":
        wumu"How did you answer it so quickly!!!"
        $ Kim_point +=20
        Kim"........"
        Kim"First of all, what everyone says is half true and half false"
        Kim"C said I didn't kill him. I don't know who killed him.Three accomplices, it is certain that the first sentence he said is true and the second sentence is false, so the murderer is not C."
        Kim"From this judgment B said the latter sentence is true, so the first sentence is false, so, the murderer is B!!"
        "The detective points is [Kim_point] "

    "C":
        wumu"Wrong, please be serious"
        $ Kim_point -=5
        jump io
xue"So that's it"
wumu"Ok, let me get down to business."
wumu"This time we're going treasure hunting!Unearth the hidden treasures of the Christian church"
Kim"You must be talking in your sleep."
Kim"Detective is my specialty, but treasure hunting isn't"
wumu" that's too bad.This treasure is different"
wumu"I found out that year four lang in order to avoid the rebellion completely annihilated, the treasure hidden to tiancao island B or A island one of them."
wumu"The treasure specifically has 60 kilograms of gold crosses, there are more than 20 gold and silver candlesticks in the legend.And the sparkling jewel crown!!"
wumu"And all kinds of treasures worth billions of yen!!"

Kim"But with all these legends, there's no way to find out where the treasure is."
x"No, no, no, there's a big hint"
"Said a man named Hetian"
show hetian at left
with dissolve
hetian"In fact, this is probably what happened on tenkao A island 20 years after the Meiji restoration."
hetian"There were children playing on the rocks"
hetian"One of the children jumped onto a rock"
hetian"He stumbled upon a cave behind the shaky demonstration!"
hetian"There's something shiny inside"
hetian"They later found a large stone statue and a necklace for the virgin Mary."
hetian"On one end of the necklace was a golden cross of gold!!"
hetian"And then it would be years, and then there was a man who lived in Nagasaki"
hetian"By some means, the golden cross was obtained on tencaoa island."
hetian"He commissioned the jeweler to remake it into a gold ring"
hetian"But the jeweler said the gold had an iron core in the middle of the process"
hetian"He came across some words on the iron core"
hetian"He looked closer and saw that it was Deus"
"(Deus for god in Latin)"
hetian"It was marked with enigmatic words"
hide hetian at left
with fade
Kim cc"The treasures of Deus...!"
wumu"Deus is the god of the secret Christian church."
wumu"It basically says, bury or sink the treasure of the gods somewhere."
Kim"So, this riddle is a sign of the so-called hidden treasure!"
xue"Has anyone ever solved this puzzle?"
wumu"No, although many treasure hunters have challenged the puzzle to possible hiding places, none has succeeded."
Kim cc"Tiancao's treasure....."
stop music
jump story6

label story6:
scene sea
with pixellate
play music "EverybodyKnows.mp3"
"Ten days later"
hetian"this time we can invite all of you to explore the legendary treasure"
hetian"Thank you very much!"
scene board1
with pixellate
show hetian at left
with dissolve
hetian"So let's start with the sponsors"
hetian"I'm Hetian from the editorial department of modern weekly."
hide hetian at left
with fade
show wumu at left
with dissolve
wumu"I'm freelance reporter wood.I see, everyone is an acquaintance, there is no need to introduce it!"
x"You're still the same, wood"
x"We haven't seen each other for about a year since we excavated the treasure of mount li!!"
wumu"Mr. Zion, your rolex is diamond-encrusted!Since you've made such a fortune as an antique dealer, why are you looking for treasures?"
show zion at right
with dissolve
zion"This watch?This is a business prop.We're like the real estate guys.If it looks like you don't have any money, no one will cooperate with you."
zion"It is said that tiancao treasure has a dreamlike golden diamond."
zion"As an antique dealer, even if you don't do business, you should have a look and broaden your horizon."
juan"Well, there's no need to be so hypocritical.I see, because even if you did not find this treasure yourself, as an intermediary you can also earn a part of the fee!
You!"
juan"If I find it, I'm not going to sell it to a bum like you."
zion"Oh, miss Juan.You're not still thinking about what happened five years ago."
hide zion
with fade
hetian"All right, guys, can you just calm down!"
juan"Miss chifeng, why are you taking pictures?"
show chifeng
with dissolve
ch"I'm just doing my job"
ch"This is breaking news"
hide chifeng
with fade
Kim"Everybody seems to know each others"
wumu"After all, the world is so small, and the world of treasure hunting is even smaller"
wumu"Although this is my second designated treasure hunt"
wumu"But of the seven, including hetian, the list is almost exactly the same."
wumu"The name of the dropout from Tokyo university was reed"

reed"Huh, high school.Don't distract us from the treasure hunt!"

xue"What do you mean!"
wumu"Then there's Moon, an assistant professor of archaeology at the university"
show moon
with dissolve
"Moon glanced at wumu and gave a cold smile."
wumu"She's still like that, a defiant woman."
hide moon
with fade
show hetian at left
with dissolve
hetian"One more person?You can't miss the boat!!"
show wumu at right
with dissolve
wumu"Be patient, hetian"
wumu"If it hadn't been for that child, the treasure wouldn't have been found!"
Kim cc"The child??"
scene temple
with pixellate
"3 hours later"
Kim"Finally!!Arrive!!!"
x"I've been waiting for you long time"
show raven
with dissolve
wumu"This is raven, who will guide us on our trip.I had entrusted it to his father, but his father was hurt and couldn't come."
rv"Hi, I'm raven"
hide raven
with fade


show kim at left
with dissolve
Kim"It's a historic site again. I go to these places every time.How boring. How to find treasure."
show juan at right
with dissolve
juan"I feel the same way, young man"
Kim"Well, you're a treasure hunter..."
juan"Miss Juan.This is my name."
juan"I've heard all about you, kindaichi"
juan"The high school student who once found the treasure of wiming island and became famous in the detective circle.But you don't look rich?"
Kim"Well, because in the end we didn't even get a penny."
juan"Guys,Come here."
juan"Think about it. Should we join forces"
Kim"ah???"
juan"Actually, based on what I know so far.I guess the treasure is around the zhengjue temple"
juan"If we can combine your intelligence with mine, we'll probably find the treasure first"
menu ib:
    "Yeah, great.You are a good judge of people":
        Kim"Yeah, great.You are a good judge of people"
        juan"Of course. After all, I'm an expert in the field of treasure hunting."
        $ Kim_point -=5
        Kim"hahaha"
        "The detective points is [Kim_point] "




    "Is it really that simple?":
        Kim cc"Is it really that simple?"
        $ Kim_point +=5
        juan"What do you mean?"
        Kim cc"Deus treasure, slowly sinking."
        Kim cc"I always felt that the truth could not be ascertained without unlocking the meaning of the inscription"
        juan"The secret of the inscription....."
        "The detective points is [Kim_point] "
hide juan at right
with fade
x"Okay,i catch you!kindaichi"
"You look in the direction of the voice and you see a familiar person"

Kim"Lily!!"
show lihua2 at right
with dissolve
lihua"Wow, so happy. kindaichi, you remember me!!!"
Kim"Of course! (this woman is so loud)"
xue"Are you the last person who didn't get on the boat?Lily?"
Kim"By the way, did you hear Mr. Wood say something about me?"
wumu"Kindaichi!Hey, Lily's here.Let me tell you something.The girl is a golden retriever and famous in the world of treasure hunting."
wumu"She may even be our secret weapon in the treasure hunt"
scene meeting1
with pixellate
Kim"That thing you're talking about, isn't it the one that uses the weird stick to find things"
lihua"Yeah, you're so smart.kindaichi"
lihua"You see, with this l-shaped stick, from hot springs, hoses, even gold.You can find anything."
xue"Is it really possible to find something like this?"
lihua"Oh, snow, what are you doing here?Looks like nothing?"
lihua"Oh, I see.Are you here to dig a hole?"
lihua"Laymen don't talk too much, okay?Lovely monitor!"
xue"What are you talking about!!"
wumu"Well, enough.We are partners."
wumu"Anyway, Lily.Please show us how to use this."
lihua"ok!"
xue"(damn girl)"
lihua"This thing was designed to look for underground water."
lihua"But everything has other USES."
hetian"By the way, lily is a treasure hunter from generation to generation.I received all kinds of training from an early age"
hetian"She is said to be even more accurate than a metal detector at detecting the material and quantity of items under the ground."
xue"Don't you think it's ridiculous, kindaichi?"
menu ic:
    "Yeah, that doesn't seem possible":
        Kim"Yeah, that doesn't seem possible"
        xue"you think so"
        $ Kim_point -=5
        Kim"en"
        "The detective points is [Kim_point] "

    "No, although it's my first time, too.But in theory it could.":
        Kim cc"No, although it's my first time, too.But in theory it could."
        $ Kim_point +=10
        xue"Well, all right......"
        lihua"Don't talk to the layman, will you?It would look stupid."
        xue"(This girl!!!!!)"
        "The detective points is [Kim_point] "
lihua"This is not a ridiculous thing.Not only did they look for mines during the Vietnam war, but many water utilities used them to look for run-down sewers."
wumu"That's interesting"
show moon
with dissolve
moon"you don't know anything about this, but you can write a treasure report, so ridiculous. Mr. Wood"
moon"It is said that this is a 16th century German, in order to find the mines, even by the national examination to confirm the use of this instrument qualification accurate technology"
hide moon
with fade
wumu"Professor Moon, you are as knowledgeable as you are temperamental"
"Suddenly the instruments in lily's hand crossed"
ch"!!!!!!!!!Did you find anything?"
zion"underground water!?"
lihua"No, not water.It must be metal"
"!!!!!!!!!"
"Mr. Reed turned to look for his equip"
lihua"Metal!!!must be mental!"
"Reed rushed over like mad"
"He pushed the crowd away with his shovel and began to dig frantically"
"Ms Juan and Mr Zion are digging hard"
xue"Kindaichi...Terrible, everyone's eyes have changed!!"
wumu"That's the magic of a treasure. It only takes one to dig it up and it could be worth 100 million yen"
wumu"It makes me want to try"
"What does Mr Zion's spade seem to touch"
"The three people threw shovels and began to dig with their hands."
wumu"Well, it's a very old currency!In terms of material, it's closer to the 18th century.But of little value"
scene xiaohai
with dissolve
gu"Oh, they're digging."
gu"are you looking for the treasure of Deus?"
gu"You'd better stop, or you'll be killed by the white-haired ghost"
gu"We won't care then"
gu"Come on, come on"
Kim cc"?????"
Kim cc"(feeling a sense of foreboding)"
Kim cc"(white-haired ghost.....)"
jump crime1

label crime1:
scene rvandjin
with pixellate
Kim"Hi, can I ask you something?"
rv"What is it?"
Kim"In zhengjue temple, what are those children talking about,the white-haired ghost?"
rv"That's just a rumor!"
Kim"Rumors?"
menu rumor:
    "Since it is hearsay, it must be false.Do not believe":
        Kim"Since it is hearsay, it must be false.thank you"
        rv"Don't ask anyone unless you have something to say, you idiot"
        $ Kim_point -=5
        Kim"......."
        "The detective points is [Kim_point] "

    "Rumors?What kind of rumor is it":
        Kim"Rumors?What kind of rumor is it"
        $ Kim_point +=10
        rv"There was once a man who claimed to be the heir of the great Deus, with a golden cross around his neck."
        scene ghost1
        with pixellate
        rv"Dig the area for treasure with a spade"
        scene ghost2
        with pixellate
        rv"On one occasion, however, the excavation collapsed."
        scene ghost3
        with pixellate
        rv"The hair of the last rescued man turned white with claustrophobic fear.And then he disappeared!"
        scene ghost4
        with pixellate
        rv"Later, it is said, the man turned into a white-haired ghost who chased down explorers seeking the treasure with a spade"
        Kim"The white-haired devil who kills treasure hunters!!."
        rv"To put it bluntly, I think this is a story that adults use to deceive children.Don't take it personally."
        "The detective points is [Kim_point] "

scene temple
with pixellate
"Near the zhengjue temple, miss Juan was digging the treasure alone when a figure approached her."
"(video)"
$renpy.movie_cutscene("firstdie.avi")

scene wenquan
with pixellate
xue"No one's morning spa is really good ah, do not worry about being loved to sleep in the golden field of a peep"
"(boys' bathroom)"
Kim"Hahaha, I knew snow would take a morning shower because she was worried about being peeked at by me, who likes to sleep late."
Kim"Ha, ha, ha"
Kim"Let me see her..."
xue"Uh-huh!The centipede!"
menu peeked:
    "Go to snow's girls' shower so you can get a peek!!Ha, ha, ha":
        Kim"Snow, I'm coming.Where? Where is the centipede?I'll kill it for you."
        $ Kim_point -=5
        Kim"......."
        Kim"(peeking at snow's chest)"
        "The detective points is [Kim_point] "

    "Pretend you didn't hear and keep peeping":
        Kim"You're not that gullible trying to fool me"
        Kim"I'm an anti-sleuthing detective.Do you think this will get me through?"
        $ Kim_point +=5
        xue"Help!Disgusting!"
        xue"Help!!!!!"
        Kim"......."
        Kim cc"I'd better go and see what happens."
        "The detective points is [Kim_point] "
"(video)"
$renpy.movie_cutscene("firstdie2.avi")




scene wenquan
with pixellate

"The local police came to investigate the murder"
show policeman at left
with dissolve
police"The victim was Juan, 36, a professional treasure hunter"
police"The victim suffered a fractured skull and a concussion.It's not clear what the weapon was, though.But seems to have been hit on the head with a blunt object like a spade"
police"What was puzzling, then, was the sign of the cross on the dead man's chest and the quantity of white hair in the hot spring"
"Shutter sound"
police"No photos!!"
show chifeng2 at right
with dissolve
ch"Don't get in my way. This is big news. Do you want to interfere with a journalist's right to report the news?"
police"You're obstructing the police!!"
hide chifeng2 at right
with fade
show hetian at right
with dissolve
hetian yy"I'm sorry. I'm sorry.This woman is such a bull in a China shop."
hetian yy "After all, Mr. Policeman, this has nothing to do with our trip!"
hide hetian at right
with fade
police"Well, everything of value from the victim's room, including lipstick, was taken."
police"It must have been an accidental robbery"
police"I think the victim must have arrived at the open spring at midnight"
police"She witnessed the robber's crime and was killed by the robber"
police"The robbers stole the keys from the dressing room and broke into the house.Then he took the victim's luxuries."
hide policeman at left
with fade
menu policecome:
    "Reasonable":
        show kim at left
        with dissolve
        Kim"(Well, that makes some sense.The logic is right.But the killer can just run away)"
        Kim"(Then why make so many white hairs and crosses on the chest)"
        $ Kim_point -=5
        Kim"(I'm afraid it's not that simple...)"
        Kim"(Is the legend true)"
        "The detective points is [Kim_point] "

    "Wait!!!":

        Kim bz"I don't think so"
        show policeman at right
        with dissolve
        police"What?Are you questioning me?The kid!!!!"
        Kim bz"If it's a home invasion, why cross your chest with lipstick?And lots of white hair in the bathhouse."
        Kim bz"How do you explain all this?"
        $ Kim_point +=5
        police"......."
        Kim"And look, there's some dark dirt under miss Juan's fingernails."
        police"What does this show??"
        Kim bz"Juan's in the shower, but it's like digging in the dirt.It was early in the evening that everyone dug up the treasure around the temple.The big probability is not the soil"
        police"yes"
        Kim cc"Where did miss Juan sneak out again in the middle of the night to dig for treasure?"
        police"Uh huh"
        Kim"Then while she was digging for the treasure, she was attacked by the murderer."
        police"That makes sense"
        police"......."
        police"What are you talking about here, kid? I'm a cop.Who are you to reason here!!"
        Kim bz"Hehe, it is no wonder that you are the kind of policeman who can only hang around in such a small place all his life.What I said was true, but you were angry with me"
        Kim cc"any man can be a policeman"
        xue"I feel Kindachi, your attitude also has a little problem"
        hide policeman at right
        with fade
        "The detective points is [Kim_point] "
scene room3
with pixellate
reed gb "Ah, ah, the lost property that the policeman said the murdered woman had lost must be the treasure we were looking for!
It must be, it must be
Damn it!!"

"Reed rummaged and rummaged"
"Doesn't look like anything of value"
reed gb "Impossible!!"
zion "Well, this bag has a double bottom"
"!!!!!!!!!"
wumu "Ah, this feels like a map
There are some marks on it"
zion"Triangular pool and kantaro cliff
Is there a secret?"
scene zhaodongxi
with pixellate
moon"Wait a minute. The triangle of the triangle pool, that's what the inscription says"
reed gb "!!!!!!!!!May be!"
moon"For Christianity, the number 3 represents the trinity of father, son and spirit!Three is an extremely important number
So in some archaeological sources the saints sometimes deliberately rewrote it as 3 instead
So the triangle might have been what they called the sacred pond"
wumu "Yeah, that's it"
"......."
moon"Well, there's no point in talking to people like you"
wumu "There are many important things in the world that are not in books!"
reed gb "But you see these two places in the map so far away, how to find the treasure ah!!"
ch"well.."
Kim"Could it be a bearing or something?"
wumu "What does this mean, Kindachi"
Kim"In war games, isn't it often said to find the enemy at twelve o 'clock?"
reed gb "I see, if so.So two and five!"
rv"It was in the cave once found guanyin place"
hetian"In order to get to where the treasure might be buried tomorrow morning.Let's change to another place today"
"OK!!"
stop music


scene senlin
with pixellate

Kim cc"raven's father said to be a famous treasure hunter."
rv".......yes"
wumu"(cigarette)"
wumu"If possible, could you meet with him and ask him two questions?I'll do an interview, too."
rv"Ah, but...'"
wumu"It would be confusing to go all together?"
wumu"Then I will go with kimada and snow.Is that convenient for you?Our information will be kept confidential"
rv"If so, of course"
scene jiazhongtan
with pixellate

wumu"Excuse me, Sir, what kind of person was your master, Mr. Zangyuan qingzheng?"
rf"My teacher, he preferred to mine for information."
rf"In fact, he also dug up a lot of treasure in this way.
Look at this, everybody"
rf"This is the family tree of my teacher, Mr. Zang yuan
Why is his genealogy in your hands"
rf"Because this is a decryption competition, the treasure hunter qing zheng master let his descendants launch a decryption competition
It was said that he would give the treasure in his hands to the one who solved the secret"
rf"As a result, neither I, then the teacher's best pupil, nor any other family member was able to solve the puzzle
The teacher also entrusted this to me, although now I still do not know the final answer"
rv"......"
wumu"!!!!He Is  the father of the famous entrepreneur Mr John"
rf"You are clever, yes"
rf"Mr John alone inherited the 200 billion yen fortune discovered by master qingzheng"
xue"But aren't these four also Mr. John's brothers and sisters?Did they get nothing?"
rf"Yes, although it's a little sad to say
After my master died, there was a big fight between the brothers over the inheritance"
rf"With the exception of John, who was young at the time, everyone else was killed in the slaughter"
rf"It's kind of tragic. Treasure, have let a person crazy, unscrupulous temptation.Although the young me also is same, keen to seek treasure.But I'm too old for treasure now.This treasure is best if no one finds it."
Kim bz"....."
scene evening2
with pixellate

wumu"What a sad story..."
xue"Brothers kill each other for money"
wumu"......."
wumu"Goodbye and don't oversleep tomorrow.kindaichi
(wumu leaves)"
Kim"Yes, Sir!!(smile)"
xue"Can i ask you a question,Kindachi?"
Kim cc"Huh?"
xue"What is the secret hidden in that genealogy?"
Kim"Ah, that.Probably have something in common"
xue"In common?"
Kim bz"Aren't you sure?Snow, the name in the genealogy..."
"There was a noise in the grass"
xue cf "Look, Kindachi.There's something moving over there!Awful."
Kim bz"Probably a leopard cat or a rat
If you're so scared, would you like to sleep with me tonight?(smile)"
xue cf "Rolled away!I will not sleep with someone like you who writes porn on your face!!Goodbye!!!!!
(snow closes the door)"
Kim"Well, I have to go back to my room and sleep too!
Oops, the shoelace is loose!"

menu destiny1:
    "Tie your shoes":
        "(video)"
        $renpy.movie_cutscene("youdie.avi")
        "You were attacked by white - haired ghosts. You're dead"
        jump start

    "Do not tie your shoes":
        "(video)"
        $renpy.movie_cutscene("nodie.avi")

Kim"!!!!!!!!!Is there really a ghost with white hair?"

scene senlin
with pixellate
"In the morning"
reed"Well, I'll be right out.I need to check out"
ch"Photography is a job that really needs strength, just a night off to start"
ch"!Work hard today, too!"
moon"Well, look around"
xue"Kindachi!!Get up!!"
Kim cc"?I told you to wait a minute.I was scared to death yesterday!!"
wumu"........."
hetian"Sorry, I got up a little late.I'm changing my clothes.Wait, I'm sorry.(calling)"
hetian"Oh, you said everyone checked out?"
hetian"Finished...Mr. Wood must scold me!"
xue"you said the white - haired ghost attacked you last night!?"
Kim bz"Yeah, he almost killed me with his shovel!"
xue"Easy for you to say!"
xue"Mr. Wood, let's call it quits on this trip.It's too dangerous!"
wumu"That's impossible. Everyone's in high spirits right now.And in Juan's case, the police are treating it as a robbery"
xue"Kindachi..."
Kim bz"No, I'm staying.Something's wrong with me. I always think Juan's case must be more than a simple robbery."
Kim cc"And yesterday's white hair ghost, I think I need to find out."
Kim"There must be some truth behind all this that we don't know
Is that right, Mr. Wood"
wumu"........(pause)"
Kim bz"Mr. Wood, you and the other treasure hunters acted strangely when they heard about the gray-haired ghost.
Have you known anything before"
wumu"........"
Kim cc"Tell me, what happened to you"
wumu"........"
wumu"It was a treasure hunt, the one Mr. Zion was talking about.In addition to this time, there was another member.That man's name is Nagasaki.
The man was buried under the rock because of the collapse.We couldn't get to the rescue team in time.So the people who were there did their best to dig him out."
wumu"However, Nagasaki was confirmed dead.
The problem is the way he died.Even now, it's chilling.The guy's hair is all white because of the claustrophobia.It looked like a white-haired devil."
wumu"We had a hard time getting his body down the mountain because it was raining hard.Together we decided to bury him on the spot."
wumu"As we prepared to bury him, moon quietly placed the cross on his chest.Then a bolt of lightning fell and struck the cross pendant.The lightning left a mark of the cross on Nagasaki's chest.But at the time, there was something even more frightening."
wumu"Before the burial, I personally closed my eyes for Nagasaki.But after being struck by lightning, he seemed to come back to life!Terrible!!"
wumu"So when Juan was killed, you're probably thinking about what happened that day.All this, we fear, is the revenge of Nagasaki!"
"A person came panting"
lihua"I overslept. Sorry."
Kim bz"lily, you surprised me when you suddenly came over here."
scene senlin
with pixellate

reed"Slow, too slow!"
hetian"I'm sorry I'm late."
reed"Hetian, you're ten minutes late"
hetian yy"I'm sorry, it was really my fault"
zion"So, is everyone here?"
rv"Well, photographer chifeng isn't here"
reed"Damn it. Do we have to wait?"
moon"That's odd. Chifeng is usually the first to arrive"
hetian yy"The phone is temporarily unavailable"
reed"She also has the map we gave out yesterday, and there's almost only one road!You don't get lost!Are you sure everyone has checked out?
Uh huh"
lihua"Use my equipment to find her!"
Kim"Can I find that with your device?"
lihua"........."
xue"......."
Kim"........."
lihua"Probably not, so let's find it together!After all, cameras are made of metal."
reed"Damn it. Waste of time"
rv"Chifeng!"
"Lily feels that her instrument is responding. Following the instrument, she walks into a piece of grass."
moon"Look, camera!"
zion"This is chifeng's camera!"
Kim"Is it..."
Kim"!!!!"
Kim"Mr. Hetian, please continue to call miss chifeng"
Kim"!!!!!!!!!"
"The crowd followed the ringing of the telephone"

"(video)"
$renpy.movie_cutscene("crime2.avi")

scene senlin
with pixellate
play music "EverybodyKnows.mp3"
Kim"Don't move, guys"

menu sr2:
    "To examine the body of the victim":
        "Found!A quick-drying marker with traces of use"
        "Found!There was no apparent damage to property"
        "Found!There were signs of blunt force trauma to the back of the head"
        $ Kim_point +=10
        "Found!The map"
        "Found!The victim was probably dead within an hour or two"
        "The weapon was a spade, and the cross on the chest was drawn with all the quick-dry marks of the victim"
        "So it's not a curse"
        "The killer is in these people!!"

    "Go back to our room and search for evidence":
        ".........."
        $ Kim_point -=5
Kim"Go back to our room and search for evidence"

scene muwu
with pixellate

"Now it's detective 1 to detective 1. The detective can question the suspect individually"
menu sr:
    "Ask Reed":
        reed"Damn it, do you suspect me?Are you a qualified detective or not"
        reed"I checked out at 6:30 this morning and called the front desk"
        reed"I was already at the meeting place around 6:50!"
        reed"I'm just looking for treasure, not murder"
        reed"If you're a detective, find a way to clear me of suspicion.Damn boy!!!!"
        jump sr
    "Ask Raven":
        rv".........."
        Kim"Do you have anything to say?"
        Kim"I will arrive about the same time as you"
        rv"Well, because I came straight from home"
        Kim"Can anyone prove that to you?"
        rv"As I was going out, I got a call from Mr. Wood."
        rv"I asked my father, who was watching TV, what time it was"
        rv"He said the exact time is 6:30, I think I should go out, too"
        rv"So I got to the rendezvous point around 7 o 'clock"
        Kim bz"Well, I don't think you're lying. Mr. Wood also told me about it"
        Kim"How long does it take from your home to the meeting place?"
        rv"Thirty minutes is enough"
        Kim bz"What about cycling and motoring?"
        rv"No, all the way from my house to the meeting place is a rugged mountain road that is inaccessible to vehicles"
        rv"By the way, the roads you walk on are also full of stone steps, and this terrain is impossible to drive through"
        jump sr
    "Ask Moon":
        moon"I left the hotel, I think it was around 6:40"
        moon"And I got to the meeting place at about 7 o 'clock"
        moon"Mr. Reed had arrived by then"
        moon"He felt a little anxious. Maybe he thought we were too slow"
        jump sr
    "Ask Hetian":
        hetian"I was the last one to arrive at the rendezvous because I did oversleep."
        hetian"So the time I left the hotel.I think it was in the first 10 minutes of assembly time"
        jump sr
    "Ask Zion":
        zion"I lost time trying to fix my hair"
        zion"It's a little late for leaving the hotel"
        zion"I should have arrived at the destination at 7:05"
        jump sr
    "Ask lily":
        lihua"Kindachi, are you doubting me?I'm so sad."
        lihua"I was late. I really went to bed late. I got up too late"
        lihua"So I left the hotel a little late"
        jump sr
    "Okay,finished.Take a coffee break":
        jump endpart1
label endpart1:
scene room4
with pixellate

"The phone ringing"
Kim bz"Hello, this is Kindachi.Who are you calling, please?"
x"Kindachi, you liar.Sneaked out, even without my sister!"
Kim bz"Ah, 123"
Kim bz"Excuse me, 123. Because this case is not suitable for you."
ott"How do you say"
Kim"I'm telling you, there's a ghost in my adventure"
ott"!!!!!!!!!!Ghosts..."
Kim"Ah, the white-haired ghost.Special in the night operation, with a spade attack innocent passers-by killing demons!!"
ott"Well, I don't have to explore, you know.I'm busy, so hang up."
Kim cc"Ha-ha-ha, little fool."

scene coffeebar
with pixellate


Kim bz"Have some coffee and dessert. That's great"
xue"This cup has handles on both sides. It's really cute"
wumu "It's true. It's rare."
scene bashou
with pixellate
Kim cc"Why is my cup the only one missing a handle"
lihua"Really?"
rv"Sorry, this cup has only one handle"
rv"Although the design is the same, the cup with two handles broke three in one fell swoop yesterday"
zion"Ah, yes"
xue"Because the cups are exactly the same design.So I take it for granted that this cup also has two handles!"
moon"Isn't it? Think it's a set of cups that makes you think that way?"
scene linggan
with pixellate
Kim"!!!!"
reed"What's the matter, Kindachi"
Kim"Isn't it? I see.I've figured it out. A psychological hoax by the real murderer!"


scene room4
with pixellate
"evening"
"phone ring"
Kim bz"What!It's you again, 123."
ott"Big liar!!"
ott"Because of you I made a big mistake at school!!"
Kim cc"Ah, 123 when did I lie to you?"
ott"Didn't you say there were white hairs in the area where you were investigating the case?"
ott"There is a child in our class who transferred from the place you mentioned three months ago."
ott"But he said there was no such rumor"
scene linggan
with pixellate
Kim"!!!!!!!!!!"
Kim"It turned out that this is also the murderer set the heart of fraud"
Kim"By the way, 123. You entrust uncle to investigate something."
ott"Oh, what is it?"

scene room3
with pixellate
zion"I hear you already know how the killer. did it?"
Kim"Well, before I point out the killer, there's one thing I have to say.Motive of the murderer"
wumu"?The killer's motive?"
Kim"The high probability is to revenge for the previous expedition's Nagasaki"
Kim"This is misleading.The killer deliberately made us think it was revenge for the death of Nagasaki"
Kim"In fact, when we first got to the island, we entered the psychological trap set by the killer. So did the white-haired devil mentioned by the kids."
rv"The rumor was also designed by the killer??"
rv"But, Mr. Kindachi.The rumour was circulated long before the performance began"

"Well?It doesn't seem to be specific..."
Kim"Yeah, normally this kind of scary stuff makes people think it's a long time ago"
Kim"But that white-haired ghost rumor didn't exist three months ago.This is what my sister asked the classmate who transferred to Tokyo three months ago."
Kim"The murderer made preparations in advance for the murder"
Kim"He came to this place many times.Every time he met a child, he mentioned the story to people"
wumu "But why did the killer do it?"
Kim "Is to die because of the accident of Mr. Nagasaki and white ghost hearsay bound together, create a white ghost revenge, or the murderer for the death of the dragon and the illusion of revenge."
Kim"Because of the cause of Nagasaki, the suspect will be locked in the internal personnel."
Kim"Then the murderer just made white hair ghost hearsay in advance, built the atmosphere of a kind of stranger to commit murder."
Kim"The murderer's aim was to seize Mr. John's property"
hetian yy"I'm sorry to interrupt.Although John died of an acute illness, he had nothing to do with the person who died."
"Kindachi brings out the qingzheng family roster, which he borrowed from Raven's father.The puzzles in the family book answer Mr Hetian's question."
Kim"Because qingzheng's family totem is a moon.The name of each person in the family register bears the character of a month"
Kim"And in this case, the names of the two people who died are the same, with the moon.They are all descended from Mr. John, and they don't know it."
Kim"Mr. John is trying to prevent a repeat of the old sibling rivalry over property.The children were deliberately placed in foster homes."
Kim"I have also been confirmed through the Tokyo police about this."
Kim"And the real motive of this case is to monopolize this estate!!"



Kim"Yesterday I actually set up a trap for the killer with my watch"
Kim"First, I asked Mr. Wood to return to the hotel yesterday.Set Ms. Chifeng's alarm clock for 15 minutes."
Kim"Similarly, I did the same thing with my suspect's watch"
Kim"And then after the crime, I deliberately told people that the conclusive evidence was still in the hotel"
Kim"Hearing that, the killer will find the right time to return to the hotel and destroy the evidence"
Kim"That is, the murderer came to this hotel as soon as he heard me!Set the alarm clock in your room 15 minutes ahead of your watch"
Kim"As you can see, the alarm clock says 5 a.m., but the real time is 8:45"
Kim"Now the man wearing the same watch as the alarm clock is the murderer"
"With jintian's hint, raven grabs the watch of the person next to him and sees that the murderer is hetian!!"
Kim"In fact, John had a third child, and that child had died"
Kim"And that person was Mr. Hetian's wife"
Kim"Mr. Hetian himself would certainly not be able to claim the estate, but if all of John's children died.Then John's granddaughter, hetian's daughter, becomes the only legal heir."
hetian yy"But I was the last one to go. Chifeng left the hotel a long time ago.There was no way I could kill chifeng by bypassing anyone who had started before me, because there was only one road to the rendezvous."
Kim"Because you let her get to you, you used the human imagination to create a subtle psychological trick"
Kim"Success made miss chifeng, who started 20 minutes earlier"
Kim"Mr. Hetian used a crime method called space exchange"
Kim"It's like when I go to a cup with two handles in a coffee shop"
Kim"I wouldn't hesitate to think that my quilt had a handle that didn't exist"



Kim"Using a similar method, you can see clearly on the map that there is only one way to the gathering place"
Kim"But if you leave some charred marks on the map like this, the broken roads will connect themselves"
Kim"If so, people will take this shortcut"
Kim"You set Mr Reed's watch five minutes ahead of time, who has a habit of arriving ten minutes before the assembly time.Let him arrive 15 minutes early."
Kim"Same with miss Moon.Instead of adjusting the alarm clock in the room, hetian adjusted everyone's watch"
Kim"While everyone because of the fear of white hair ghost bathing, homeopathy will other people's watches to adjust the time"
Kim"Next, they use their watches.Adjust the alarm clock in a strange room"
Kim"After that, follow the plan.Reed, chifeng, and moon left the hotel every five minutes"
Kim"So miss chifeng went the wrong way and had to return"
Kim"So, leave the house 10 minutes early, but miss chifeng will be the last to walk because she wasted time taking unnecessary walks"
Kim"That's how the killer changed the order.Successfully manufactured an alibi"
Kim"The only person who could do this was Mr. Hetian, the last one to leave the hotel"
hetian"I was wronged!!!!!"
"At this time, jin tian turned on the TV.Mr Hetian heard reports this morning that the John group had declared bankruptcy."
"Hetian was stunned"
wumu "The treasure you targeted is gone"
wumu "You can kill for a treasure. Don't you think about other people's lives?You scum!I'm gonna hit you with my fist!!"
hetian yy"Kill me, kill me, anybody can do it!!!"
hetian yy"I can't kill myself, please........."



hetian yy"I can't kill myself. If I kill myself, my daughter won't get the insurance"
hetian yy"My daughter is seriously ill and the medical bill is 80 million yen"
hetian yy"In order to save my child, I bought myself a high insurance, I tried to die countless times, but never succeeded"
hetian yy"Later, I learned from my father-in-law that my wife was John's child"
hetian yy"But there was more than one heir to John's family, and other competitors"
hetian yy"At that moment, I was determined to get my inheritance at all costs"
hetian yy"So I arranged this treasure hunt, and I planned to kill all the other heirs"
hetian yy"Please, kill me.Save my daughter"
Kim"I understand how you feel about trying to save your daughter.But you put things on that can't be weighed on the same scale."
hetian yy"Why!Why!Why!!!!!Daughter, I'm sorry."
hetian yy"I'm sorry........"
"......."

scene jail
with pixellate

"Ten days later"
"In the cell..."
hetian yy"I've told you everything I need to tell you. Let's get this executed!I don't want to live alone after my daughter dies"
police"Don't give up on yourself. Maybe your daughter won't die so easily"
police"It is said that one person gave her a treasure of tian-zheng-ling gold award on Christmas Eve."
police"The treasure was sold at today's auction for the treatment of your daughter."
police"Your daughter was saved..."
hetian yy".........."
hetian yy"......."
hetian yy"Is there really a god in the world"
hetian yy"Thanks,God"

"(video)"
stop music
$renpy.movie_cutscene("end.avi")

return
