# AirBnB clone - The console

In this project we will be building a clone of the famous AirBnB platform. The goal is to create a command line interface to serve as a command interpreter for our AirBnB objects, their abstactions and handling storage.

## Console Features

``` text

* Creating New Objects
* Retrieving Objects from Files
* Performing Operations on Objects
* Destroying Objects

```

To run the command interpreter:

``` bash

./console.py

```

## Execution

Your shell should work like this in interactive mode:

``` text

$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$

```

But also in non-interactive mode: (like the Shell project in C)

``` text

$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$

```

## Storage

To manage the classes and their data storage, we will use the Storage engine. The engine will utilize the FileStorage class, which will handle reading and writing objects to and from files on the system.
