
define e = Character("？？？", color="#FFFF00")
define l = Character("刘备")
define ee = Character("曹安民", image="caoanmin_head",color="#FFFF00")
define c = Character("曹操")
define x = Character("夏侯元让")
define g = Character("关羽")
define y = Character("袁绍")
image head caoanmin_head="caoanmin_head.png"

label start:
    scene bg2
    with fade
    play music "herodawn.mp3"

    "话说天下大势，分久必合，合久必分。周朝末年，七国纷争，并入于秦"
    "到了秦朝灭亡前，楚汉纷争，又并入于汉"
    "汉朝自高祖刘邦，斩白蛇而起义，一统天下"
    "后来光武中兴，传至汉献帝，遂分为三国"
    scene backg
    with dissolve
    show caoanmin at left
    with dissolve



    e "你是何人"

    e "此处乃是我十八路诸侯会盟之地，闲杂人等，休得入内"

    e "否则休怪我刀剑无情"


    show liubei at right
    with dissolve

    l "在下乃中山靖王之后，汉景帝玄孙，刘备刘玄德是也 "
    l "不知尊驾如何称呼？ "

    ee "哼，我乃曹安民是也"

    ee "可曾听过"

    l "实不相瞒，未曾听过 "

    ee "混账，竟敢轻视本将军！来人，给我拿下"

    c "放肆！！！"



    ee "叔。。。不，将军"

    c "此人敢自称是汉氏后裔，那么必然是皇亲国戚，汝等浅薄小辈，怎敢如此无礼！"
    c "退下！"
    ee "是。。。"

    hide caoanmin
    hide caocao
    show caocao at left
    with dissolve
    with move

    c "小子浅薄，将军勿怪"
    c "将军刚才说自己乃是中山靖王之后？"
    l "回将军话，正是"
    c "嗯，仔细观来，阁下果然是仪表堂堂，气宇不凡啊，哈哈！"
    c "请问阁下尊姓大名，现居于何处？麾下兵马多少？"
    l "回将军话，在下刘备字玄德，先居无定所，只靠织席贩履为生"
    l "今日三人三骑愿杀国贼董卓，匡正天下！"
    c "！！！"

    show xiahoudun
    with dissolve

    x "织席贩履竟能说的如此从容，如此坦荡！此人不简单啊，孟德"
    c "。。。。是啊"
    c "想当年，王司徒宴上，何人瞧得起我曹操！"
    c "那些个乌合之众，只知哭哭啼啼，装腔作势"
    c "还说我是奸宦之后，董卓鹰犬，可笑可笑啊"
    c "今日见到将军，仿佛看到了我当日宴会上的样子啊"
    c "阁下泰然说出织席贩履之时，我着实吃了一惊啊！"
    l "哪里哪里，阁下可是曹孟德，曹将军？！"
    c "正是在下"
    l "将军只身刺董，名扬天下。乃大汉之忠臣也"
    l "刘某得见将军，真是三生有幸啊"
    c "哪里哪里，将军请"
    x "三位英雄，请！"

    hide caocao
    hide xiahoudun

    scene bgstart

    show guanyu at left
    with dissolve

    g "大哥，此人便是曹操？"
    l "是，此人胸怀大志，颇有抱负。但。。。"
    g "怎么了，大哥？"
    l "世人皆说，曹孟德，治世之能臣，乱世之奸雄。有如此人，不知对我大汉是幸还是不幸"
    g "大哥，乱世之中，当有兼并天下之志！"
    g "我并没觉得有何不妥，大哥也是一样的英雄应该也明白这个道理"
    l "。。。。是嘛，兼并天下啊。。。"
    g "正所谓，太平时杀一人，悔恨终生。战乱时，杀万人，天下称颂。此乃，霸。。"
    l "云长！一人也是人，万人也是人。杀一人是祸，杀万人亦是过。"
    l "我刘备决不辜负天下一个人。这天下，如果没有战乱，没有杀戮之声该有多好啊"
    g "。。。大哥，说得对。。。。。是我浅薄了。。"

    hide guanyu
    hide liubei

    show yuanshao at left
    with dissolve

    y "孟德！哎呀呀，孟德啊，我们千盼万盼可把你盼来了"
    y "当年洛阳一别，恍如隔世，恍如隔世啊，孟德！"

    show caocao at right
    c "这不是本初兄吗？如今你贵为十八路诸侯盟主，我还没想到是你。"
    c "气宇轩昂不减当年啊，本初兄"
    y "孟德！还不是因为你的举荐啊，哈哈哈"
    c "哈哈"
    y "孟德！尚未用过膳吧，来来来，你先入座"
    y "来人，给孟德上菜。"
    c "这么客气，弄得我都有点不认识你了"
    y "呵，哈哈，认识认识，你啊，总爱开这样的玩笑，一直没改。"
    y "你我情同手足，生死之交。如分彼此"
    c "这样啊，哈哈，那行吧"
    y "孟德，这三位是？也是你的战将吗？"
    c "嗯，那也不是。这三位刚才在门口与我的将士起了点摩擦。我看三人仪表不凡"
    c "想来都是末路英雄，"



    stop music

    return
