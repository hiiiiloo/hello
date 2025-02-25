from tkinter import Tk, Label, Button
from PIL import ImageGrab


def display_message(item):
    label_message.config(
        text=item,
        font=("courier", 13,"italic"),
        fg="black",
        bg="light grey",
        padx=20,
        pady=20,
    )

root = Tk()
root.title("Special Card")
root.geometry("500x400")
root.configure(bg="light grey")

title_label = Label(
    root,
    text="A special messages",
    font=("georgia", 20, "italic underline"),
    bg="light grey",
    fg="dark red"
)
title_label.pack(pady=10)

label_message = Label(
    root,
    text="kannaaaaaa click these messagesssssss",
    font=("tahoma", 15, "italic"),
    bg="light grey",
    fg="brown",
)
label_message.pack(pady=20)

messages = [
    """ith indallo kore ayi njn chyth kond irikkun.literally njn ith december ill start chythe ahh. ith egane ninak ayakkum ennu 
    ariyath kond njn ith igane vech kond irikkuva. and guess what njn kand pidich  egane link akkanam ennu.soooooooooo.......
    (these innu 25th feb add chythe ahh this starting sentences).
    you know ith kore avind enik indallo nallonam dheshayam varind ith kond. 
    but ith njn like ishttapett njn thanne oky chyam ennu vicharichitt chyune sooooooooooo not a big deal.
    i just like this soooo much, i mean this idea you know. 
    njn indallo ith card mathiri egane ayakkum ennokkey njn irunn nokki kond irikkuvarun. kore njn nokki korach njn google ill nokki pne 
    chatgpt ithe eduth chodich. 
    but ivar onnum parayune reethi enik manasillavanilla. pne njn yt ill nookii. enik oru kundham manasillavanilla. 
    like card ode ayakkan njn vicharikkumbol ath parayune code vechitt msg mathram 
    snd avunollu. ath kond enik full dheshyam vannath. and guess what njn ee code ith file ninak ayakkan povua 
    and ni egane ahh ennu vechal open chy ennu reethiyil. but you know i got it egane card ayakkan pattum ennu
    sooooooo yaaaaaaaayyyyyyyy.(ith njn ee file ode ayakkan povua ennu paranje enik full dheshyam vannuitt ahh ttoo.alter chythitt enik
    venakil ayakkam but i didnt. that teeth showing emojji.i just dont want to make any changes to these msgs thats why.)""",
    
    
    """i know ith full oru msg akkan pattum ennu. but ith alle oru resam. oro msg ni igane open chyum ath nokkum pne 
    ath read chyum full time waste avum because ithil njn specially onnum parayathilla. 
    ennum paranj ni ee full msg vayakathirunal. you know what i will do. njn mindulla athra thanne. 
    appo ni vivcharikkundavum ooo damnnn ennu. but njn ithil chelapol vallom 
    special paranjallooooooo. maybe njn paranj ennu irikkum ketto. anyways how is life going my babyyyyyy. 
    i know is going gooodddddd because im there naaaa right. what could possibly go wrong if im there. 
    nothing could ever. cause you know im damnnn special.(that smilling emoji). you could ask me later if you didnt get 
    which emoji is that okayyy. anywaysss,,,, you know that i love you sooooooo much right...
    like sooooooooooooo muchhhhhhhh. and you know i misssssssssss youuuuuuu sooooooo muchhhhhhhhh.......
    i know that im not easy to love. you know i have a huge cruch in you like sooooooo biggggggg.
    like a whale(that laughing emoji). and did i ever told you this i reallyyyyyyyyy like you smile.
    soooooooooooo muchhhhhhhh. like i get butterflies every thime you smile. yeaaaaaaa literally.
    and i could do anything to see you smile. thats why everytime when namal ahh jcb stop chyth ittekkune eduth 
    vech njn kore byeeee ennu parayune because when i say that you smile and i feel happyyyyyy at that time.""",
    
    
    """hi baby gurllllll,,,,,
    ippo time 10:20pm and ni vandi odikkuva.. njn paranjille orakkam varulla ennu that is because of this. 
    but i cannot say that. pne laptop ind ennu chodichath ith kond thanne ahhhh. actually i dont know why there 
    is 3 messages but yeaaaaa. and enik ninne vilikkanam enit samsarikkanam ennu okkey ind... ith indallo 
    enik whatsapp ill alland msg ayitt ayakkam ennu ik but enthooo egane chyan ayitt thonni. njn paranjille ith trial
    2 ahh ennu karanam njn 1st chythath full kolam ayi appo athi enik alternation varuthi kand pidich chyan 
    olle patience illarun soo i deleted that one and started new one. do you know the fun part ippo ithinthe name indalo
    trial2 ennu ahhhh. njn ith mattitt puthiye peru vechitt njn ith ninak ayakkummmmm.... 
    and kannaaaaa,you know njn ith kore nallu kond vichariche igane oru kazhyam chyanam ennu, but egane chyum ennu 
    i really dont know enitt ee edak njn njn reels kandond irunnapol you i got the idea you know enik entha ezuthande 
    ennu i dont know just kore kazhyam ind like i loveeeeeeee youuuuuuu sooooooo muchhhhhhhhhh
    guess what njn ith 1st chyth kond irunappol ni vilichh. 
    guess what ni entha paranje ennu red bull ine kurich pne kurkure vangiii pne 9 30 ikku ni vanillakil varan ennum 
    okkey paranj you know i really liked those letters your gifts soooooooooo muchhhhh i reallyyyyy lovedddddd ittttt 
    ath njn paranjillalooo ath enik entha parayande ennu ariyillarun just first time ahh enik agane letters 
    okkey kittune ath kond enth parayanam ennu ariyath kond ahh not because enik ath ishtapettilla. 
    i realllyy lovedddd ittttt pne indallo enik ni ahh letter ill oranathil my future wife ennu ezuthitt ille you know 
    i blushedddd sooooooooo muchhhhhhhhhh. ohhhhhhhh ith full enik ath kittiye ne kurich analo njn ezuthuneee you know 
    njn ninak njn igane kore indakki tarune ishttam ahh ennu okkey ni paranjille at that time i was and still ith ezuthune 
    time illumm i making something soooooo special njn tharum ath just oru kazhyam koode kittan ind ath kitti kazhinal enik 
    ath complete chyam. njn athinthe kore demo indakki noki ath that worked so yayyyyyyyyyy.(again that emoji) okayyyyyyyyyy.
    ith enik parayanam ennu indarunn. i reallyyyyyy loveeeeee how you make me feelllll lovedddddddd. 
    i know im not good at expressing my feelings. im sorry. i really dont like that me so much.
    im sorry if i accidentally hurt you in any way. whatever happens always remember that 
    i loveeeeee youuuuuuu soooooo muchhhhhhhhhh than i love myself. (that smilling emoji). okayyyyyyyyyyy. """
]


for idx, message in enumerate(messages, start=1):
    btn = Button(
        root,
        text=f"Message {idx}",
        command=lambda msg=message: display_message(msg),
        font=("trebuchet MS", 12),
        bg="grey",
        fg="silver",
        padx=10,
        pady=5
    )
    btn.pack(pady=5)



root.mainloop()