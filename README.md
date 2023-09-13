[Python REPL reference](https://realpython.com/python-repl/)
## What is Python REPL?

The Python interpreter allows for what’s known as an interactive REPL
(Read-Eval-Print Loop), or shell, which

**R**eads a piece of code

**E**valuates it, and then

**P**rints the result to the console in a

**L**oop

The **Python interpreter** can execute Python code in two modes:

**Script**, or program

**Interactive**, or REPL



The main difference between a module and a script is that modules are meant to be imported, while scripts are made to be directly executed.


## Interactive mode

When you run the **Python interpreter** in **interactive mode**, you open an interactive shell, also known as an **interactive** or a **REPL session**.
In this shell, your **keyboard is the input** source, and your **screen is the output** destination.

## Why Use a Python REPL?

As a Python programmer, you’ll spend considerable time in interactive mode.

Explore and learn Python syntax

Try out and prove ideas, concepts, and implementations

## Starting and Ending REPL Interactive Sessions

1. Running the python Command
Open command-line window.
Run `python` without any arg.
It shows current `Python` version and `platform` you are running the interpreter.

The second line shows a message with commands that you can run to get additional information about Python in general.

The last line is `primary prompt ` of a standard Python interactive session or shell.

The interpreter also has a `secondary prompt` represented by three dots (...).

```
>>> number = 42

>>> assert isinstance(number, int) and number > 0, \
...     f"number greater than 0 expected, got: {number}"

```

2. Passing Command-Line Options to the python Command
-  `-i` flag option makes the interpreter enter the interactive mode after running a script
- `-c` option executing a piece of code
- `-m` creating virtual environment

```
C:\>python -c "print('Hello word')"
```

```
C:\REPL>python -i sample.py
```

Check the current global variables in your script.
```
globals()
```

Inspect the stack trace when your program raises an exception.

Call `mean()` with an empty list as an argument.
```
mean([])
```

In this case, the function fails with a `ZeroDivisionError` because calling `len()` with an empty list returns `0`.

## Task 1 Script mode
In Python interpreter:

Execute **script** `sample.py` in Python interpreter.

Write your own script,
execute the function `random` from `random` **module**, print the ranodm number to the screen.




- `-b` option when you’re running code that compares `bytes` objects

Run python with the -b option and without.
```
>>> my_str = "Welcome to Python"
>>> bytes_str = b"Hello"
>>> my_str == bytes_str
```


Understanding `bytes`. Check it on your name.
```
bytes_str = b"Hello"
>>> for byte in bytes_str:
...     print(byte,end='')
...     print('\n')
```
Python `bytes()` function is used to convert an object to an `immutable`(cannot be modified) byte object of the given `size and data`. The Python bytes() function returns a byte's object, which is an immutable series of integer numbers ranging from `0 to 256`.

3. Exiting the Current Python REPL Session
- quit()
- exit()
- Ctrl+Z and then Enter on Windows systems
- Ctrl+D on Unix systems, such as Linux or macOS


These key combinations represent the end-of-file character `(EOF)` in the corresponding OS.

Both functions allow you to exit the current session by implicitly raising a `SystemExit` exception.


They allow you to exit the current interactive session because the interpreter runs in a special file called __main__, as you can confirm by inspecting the __name__ attribute:
```
>>> __name__
```

All the Python code in an interactive session will be contained in the __main__ file, which runs until an EOF character is read.


This means that when the interpreter finds this character, it immediately terminates the current REPL session.

## Running Code in a REPL Session

1. Simple statement

When the REPL’s primary prompt `(>>>)` appears on your screen, type in the following expressions, pressing the Enter key after each of them:

```
>>> 5 - 2
3

>>> sum([1, 2, 3, 4])
10

>>> 42 > 7
True

>>> number = 42

>>> 7 / 0
```


While running these examples,
note how after executing each expression, the interpreter loops back to the primary prompt (>>>), which lets you introduce a new expression.
Now you’ve seen the REPL cycle in action. The Python interpreter has `read` your expressions, `executed` them, and `printed` their corresponding result to finally `loop` back to the primary prompt.



2. Compund statements
Conditionals, loops, and with statements

```
>>> number = -42
```

```
if number < 0:
    print("negative")
elif number > 0:
    print("positive")
else:
    print("equal to 0")
```

When it comes to entering indented code blocks, keep in mind that the standard REPL `doesn’t support auto-indentation`:

3. Dealing With Explicit and Implicit Line Continuations

`Explicitly join` multiple physical lines into a `single logical line` using the `backslash (\)` character

```
>>> number = 42

>>> assert isinstance(number, int) and number > 0, \
...     f"number greater than 0 expected, got: {number}"

```

Once you open a bracket, such as [], (), or {}, and press Enter, you get the REPL’s secondary prompt. This is known as `implicit line joining`.

4. Printing vs Evaluating

The interpreter doesn’t display anything for `statements that don’t generate return values.`

```
>>> numbers = [2, 4, 1, 3]

>>> numbers.sort()
>>> numbers.append(5)
```

Because these method calls don’t issue any output to the screen, it may seem that they didn’t perform any real action. However, they did.

```
>>> print(numbers.append(6))
```

5. Flagging and understanding errors

When an error occurs in a REPL session, the interpreter automatically prints the corresponding error message and traceback. Then, it loops back to the REPL’s primary prompt.

Explore the follwoing errors:

```
>>> greeting = "Hello, World!
>>> 42 / 0
>>> 42 / 0

```

6. Using the _ Special Variable

```
>>> 42 < 7
>>> _
```

7. Reloading imported modules

```
>>> import greeting

>>> greeting.greet()
'Hello, World!'
>>> greeting.greet("Pythonista")
```

## TASK 2 implement additional functionality and test it.

Now say that you want to add a new argument to your function. The argument will be a `Boolean flag` that allows printing the `greeting message in uppercase letters`.


**Handle the list of names instead of str.**

```
>>> import importlib
>>> importlib.reload(greeting)
```
