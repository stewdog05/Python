import webbrowser as wb
import pyautogui as pg
import time as t
points = 0
show = pg.prompt("What is your favorite show ?")
if show == "Hannah Montana":
    pg.alert("BESTTT OF BOTH WORLDS")
    points += 10
    wb.open("https://www.youtube.com/watch?v=t93u0qg5q_M")
    t.sleep(6)
elif show == "Sponge Bob":
    pg.alert("I can't hear YOUUUUUUU")
    points += 15
    wb.open ("https://www.youtube.com/watch?v=MlnDf3e3PQ0")
    t.sleep(6)
elif show ==  "Full House":
    pg.alert("U got it dudeeee")
    points += 5
    wb.open ("https://www.youtube.com/watch?v=U-PhFzLWVt0")
    t.sleep(6)
elif show == "Bubble Guppies":
    pg.alert("cooooolio!")
    points += 10
    t.sleep(6)
elif show == "My Little Pony":
    pg.alert("PONYSSS")
    points += 20
    wb.open ("https://www.youtube.com/watch?v=T0d_8NV1Hew")
    t.sleep(6)
else:
    pg.alert("Hm")
    points -= 3
    wb.open ("https://www.youtube.com/watch?v=_RXo5XDkEJM")
    t.sleep(6)
food = pg.prompt ("What is your favortie food ?")
if food == "Pasta":
    pg.alert("NOOODLESSS")
    points += 10
    wb.open ("https://www.youtube.com/watch?v=BTs5FS66IUI")
    t.sleep(6)
elif food == "Llama":
    pg.alert("mm fur")
    points += 100
    wb.open ("https://www.youtube.com/watch?v=3U8pAM4VXvI")
    t.sleep(6)
elif food ==  "Steak":
    pg.alert("fancy shmancy")
    points += 10
    wb.open ("https://www.youtube.com/watch?v=I4Q3YDezqcM")
    t.sleep(6)
elif food == "Pizza":
    pg.alert("Italiano!")
    points += 10
    t.sleep(6)
elif food == "Cous cous":
    pg.alert("Cous cous yum")
    points += 20
    wb.open ("https://www.youtube.com/watch?v=snLsmEn1NUA")
    t.sleep(6)
else:
    pg.alert("Okayyy")
    points -= 2
    wb.open ("https://www.youtube.com/watch?v=-Y8VMW_KXoo")
    t.sleep(6)
name = pg.prompt ("What is your name ?")
if name == "Larrabee":
    pg.alert("yikes")
    points -= 55000000000000000000
    wb.open ("https://www.youtube.com/watch?v=eDU0CTDMk2g")
    t.sleep(6)
elif name == "Winnie":
    pg.alert("you wish you were stewart")
    points -= 4500000
    wb.open ("https://www.youtube.com/watch?v=3U8pAM4VXvI")
    t.sleep(6)
elif name ==  "Bridget":
    pg.alert("Well Bridget, your not a kool kat")
    points -= 400000
    wb.open ("https://www.youtube.com/watch?v=-Y8VMW_KXoo")
    t.sleep(6)
elif name == "Bob":
    pg.alert("Bob the builder!")
    points += 100
    t.sleep(6)
elif name == "Fraser":
    pg.alert("hm")
    points -= 20
    t.sleep(6)
else:
    pg.alert("Yikes ur not a kool kat")
    points -= 200
    wb.open ("https://www.youtube.com/watch?v=-Y8VMW_KXoo")
    t.sleep(6)
sport = pg.prompt (" What is your favorite sport?")
if sport == "Lacrosse":
    pg.alert("dope")
    points += 40
    wb.open ("https://www.youtube.com/watch?v=eHIxdnc_yCE")
    t.sleep(6)
elif sport == "Field Hockey":
    pg.alert("knarly")
    points += 40
    t.sleep(6)
    wb.open ("https://www.youtube.com/watch?v=PUCgC_TukKg")
elif sport == "Ice Hockey":
    pg.alert("brrrrr")
    points += 30
    wb.open ("https://www.youtube.com/watch?v=jUP0j0u-G-s")
    t.sleep(6)
elif sport == "Tennis":
    pg.alert("MINE! YOURS!")
    points += 10
    t.sleep(6)
    wb.open ("https://www.youtube.com/watch?v=drOzZ2hYFHI")
elif sport == "Soccer":
    pg.alert("FAST FEET! GO! GO! GO!")
    points += 10
    t.sleep(6)
elif sport == "Zorbing":
    pg.alert("ZORBBBBBBBBBBB")
    points += 200
    wb.open ("https://www.youtube.com/watch?v=NpOc0yqrmxI")
    t.sleep(6)
else:
    pg.alert("Strange choice")
    points -=1
    t.sleep(6)
color = pg.prompt ( "What is your favorite color?")
if color == "Blue":
    pg.alert("Like the ocean")
    points += 30
    wb.open ("https://www.youtube.com/watch?v=I6ILheTtuq4")
    t.sleep(6)
elif color == "Red":
    pg.alert("Red antssssss")
    points +=5
    wb.open ("https://www.youtube.com/watch?v=sMfkODJw30M")
    t.sleep(6)
elif color == "Yellow":
    pg.alert("Like sunflowers")
    points += 20
    wb.open ("https://www.youtube.com/watch?v=HcUsAV06uLs")
    t.sleep(6)
elif color == "Green":
    pg.alert("Are you a planter or somethinggg")
    points += 10
    wb.open ("https://www.youtube.com/watch?v=4Dr1mvtUIwI")
    t.sleep(6)
elif color == "Purple":
    pg.alert("I love lavender")
    points += 30
    wb.open ("https://www.youtube.com/watch?v=dkcICPEQVaY")
    t.sleep(6)
elif color == "Pink":
    pg.alert("PINKALISHISH")
    points += -10
    wb.open ("https://www.youtube.com/watch?v=bDlroFGK5Sg")
    t.sleep(6)
else:
    pg.alert("Coolio")
    points -= 1

pg.alert(points)

