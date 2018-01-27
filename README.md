# BlockShell
A command line utility for learning Blockchain technical concepts likechaining, mining, proof of work etc.

<img src="https://image.ibb.co/mJFNGw/blockshell.gif">
<img src="https://preview.ibb.co/dhC7yb/Logomakr_5g_Ei_Dw.png" height="80">

## About
Anyone who wants to understand how blockchain technology works, then <b>BlockShell</b> should be a great start. Because I have created BlockShell keeping blockchain fundamentals in the center of development. With BlockShell you will actually create a tiny blockchain in your system where you can create blocks with data, explore blocks etc.

So, by using BlockShell anyone can learn following blockchain concepts,
* Block & Chaining
* Hashing
* Mining
* Proof of Work

## BlockShell Web Explorer
<p>BlockShell comes with built-in blockchain explorer by which you can actully see how blocks are mined and what is stored and where.</p>

Latest Mined Blocks             |  Block Details
:------------------------------:|:-------------------------:
![](https://preview.ibb.co/iZa5jG/Screen_Shot_2018_01_25_at_11_25_22_PM.png)  |  ![](https://preview.ibb.co/cDB0Jb/Screen_Shot_2018_01_25_at_11_25_35_PM.png)

## Installation
Step 1 - Create project directory
```
mkdir <project_name> && cd project_name
```

Step 2 - Create new virtual environment
```
virtualenv venv
```

Step 3 - Activate virtual environment
```
source venv/bin/activate
```

Step 4 - Clone this repo
```
git clone https://github.com/daxeel/blockshell.git
```

Step 5 - Change directory to cloned one
```
cd blockshell
```

Step 6 - Install blockshell
```
pip install --editable .
```

Step 7 - Try "blockshell" command and test installation!
```
blockshell
```

<b>Output in terminal after calling BlockShell command</b>
<img src="https://image.ibb.co/dRqGrw/Screen_Shot_2018_01_25_at_11_21_38_PM.png">

## Lanuch BlockShell Web
Step 1 - Start new terminal window, go to cloned directory

Step 2 - Start web.py
```
python web.py
```

Step 3 - Go to 127.0.0.1:5000 address in browser and boom!

