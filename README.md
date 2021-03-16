# EPI Judge

## Beta 5

## Introduction

EPI Judge is meant to serve as a companion to our book Elements of Programming Interviews. Specifically, this project consists of the following:

- **Stub programs** for each problem in our book in Python
- **Test-cases** that cover common corner-case and performance bugs
- A **framework** for running these tests on your implementation on your machine

## Installation

Here's how to download the judge:

    $ git clone https://github.com/adnanaziz/EPIJudge.git
If you do not have `git`, here's a good [tutorial](https://www.atlassian.com/git/tutorials/install-git) on installing git itself.

## Running the judge using IDEs

Check out these one minute videos to see how easy it is to get started with the judge.

### Python

[PyCharm](https://youtu.be/ImD_iI-uGYo), [Eclipse](https://youtu.be/rZ1qqwEXwQY), [NetBeans](https://youtu.be/Z41jW1TyZwY)


## Running the judge from the command line

### Python

    $ python3 <program_name>.py


## FAQ

- How can I contact the authors? 

Please feel free to send us questions and feedback -  `adnan.aziz@gmail.com` and `tsung.hsien.lee@gmail.com`

- Help, my EPIJudge is not working, what should I do?

If you do have issues, e.g., with install or with buggy tests, feel free to reach out to us via email. Please be as detailed as you can: the ideal is if you can upload a screencast video of the issue to youtube; failing that, please upload screenshots.  The more detailed the description of the problem and your environment (OS, language version, IDE and version), the easier it’ll be for us to help you.

- I'm new to programming, and don't have any kind of development environment, what should I do?

The IntelliJ Integrated Development environments described above are best-in-class, and have free versions that will work fine for the EPI Judge. They do not include the compilers. You can get the Python development environment from [Python.org](https://www.python.org/downloads/). Google is a good resource for installation help.

- What compilers are supported for judge?
  - Python
    - **Python** 3.7 and newer


- What compilers are supported for solutions?
  - Python
    - **Python** 3.6 and newer 

Let us know if you managed to compile with an older version.

- What does the UI look like?

Take a look at this screenshot.

<img src="http://elementsofprogramminginterviews.com/img/judge-ide-example.png" width="600px"></img>

- How can I understand the test framework better?

The judge harness is fairly complex (but does not use nonstandard language features or libraries). You are welcome to study it, but we’d advise you against making changes to it (since it will lead to nasty merge conflicts when you update).

## Tracking your progress

The file [index.html](https://github.com/adnanaziz/EPIJudge/blob/master/index.html) in the root of this project tracks your progress through the problems. Specifically, there's an expanding tab for each chapter. Click on it, and you will see your progress, e.g., as below. This file gets updated each time you execute a program. You can **use this file to map book problems to stub programs**.

<img src="https://i.imgur.com/xjf7Z32.png" width="600px"></img>

## Acknowledgments

A big shout-out to the hundreds of users who tried out the release over the past couple of months. As always, we never fail to be impressed by the enthusiasm and commitment our readers have; it has served to bring out the best in us.
We all thank [Viacheslav Kroilov](https://github.com/metopa), for applying his exceptional software engineering skills to make EPI Judge a reality.
