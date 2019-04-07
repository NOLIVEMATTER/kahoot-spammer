# kahoot-spammer

--basic setup--

these files allow you to spam bots onto a kahoot game with two step authentification however they require some setup on your part

obviously the files with linux in the name are for linux and the ones with winodws in the name are for windows (idk why i had to specify)

you need chrome and the chrome webdriver installed on your computer 

I used selenium for this project so this means for windows you will have to specify webdriver executable path in the executablepath variable near the top of the file. For linux I assume you have installed the webdriver to the default location.

you will also need to specify a gamepin for the kahoot game

--general info--

this porject uses selenium for the web ineractions, sockets for the remote execution, and time to wait for the browser to load and was programmed in python 2.7

--what even is this--

These programs are not very good programs. I am well aware that there are probably better ways to do this, this is just a general proof of concept and I was bored so I made this

I dont know if I am the first person to implement a solution for this, and I doubt it and I am not claiming to be the first, however I havent seen any other github projects that allow bypass of the dual athuentification procedure for kahoot. I might just not have searched for very well.

this wont work for regular kahoot games just an fyi

--general concept--

the concept is to have several windows to try all diffrent combos for the kahoot two step authentification code, this way bots can still join the game even with two step 

--inspiration--

So after discovering that kahoot had implemented a dual authentification option to stop bots from joining games, I resolved to fix the issue and allow people to ruin learning expiriances once again.
