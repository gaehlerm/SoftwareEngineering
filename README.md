# 1. Introduction to software engineering

Copyright Marco Gähler, all rights reserved.

Please give me feedback on the book. Either as a merge request or by email, marco.gaehler@gmx.ch

This is a book about software engineering, similar to Clean Code by Robert Martin. So far it is only a rough draft. There is still a lot to write. Especially some chapters feel like they were too short. Anyone who feels like it may help improving this book. Just create an MR. And my English could be better...

The first half of the books seems more or less ok, the second half needs some serious reworking.

Things to write:
-	If anyone is an expert on Copilot and has ideas how to integrate it into this book, let me know.
-	What is architecture? Or leave this chapter away all together? Read book "Fundamentals of Software Architecture"?
-	Domain driven design -> reread the book. What in the book is about DDD and what are other topics like destillation? DDD distilled may help to get the essence.
-	Write some more about everything. Some chapters are really short.
-	Restructure and sort the chapters somehow.
-	Some simple example on refactoring (what technique exactly? Converting a function into a class?)
-	Design patterns -> write short explanations to all of them? Or leave this chapter away completely.
-	How to work with existing code? If the code is not as nice as explained here. Read WELC again.
-	How to organize software projects
-	Mention combinatorial explosion somewhere?


# 2. Table of content

// figure out how to sort the different chapters and sections

- [1. Introduction to software engineering](#1-introduction-to-software-engineering)
- [2. Table of content](#2-table-of-content)
- [3. Preface](#3-preface)
- [4. Introduction](#4-introduction)
	- [The Life of a Software Engineer](#the-life-of-a-software-engineer)
- [5. Single responsibility principle](#5-single-responsibility-principle)
	- [Do not Repeat Yourself](#do-not-repeat-yourself)
	- [Advantages of the SRP](#advantages-of-the-srp)
		- [Understanding](#understanding)
		- [Naming](#naming)
		- [Duplication](#duplication)
		- [Testing](#testing)
		- [Bugs](#bugs)
		- [Bug fixing](#bug-fixing)
	- [Example](#example)
	- [Orthogonality](#orthogonality)
		- [Advantages of orthogonal systems](#advantages-of-orthogonal-systems)
	- [Copilot](#copilot)
	- [Exercises](#exercises)
- [6. Levels of abstraction](#6-levels-of-abstraction)
	- [Real world example](#real-world-example)
	- [Programming Example](#programming-example)
	- [The onion layers](#the-onion-layers)
		- [3rd party libraries](#3rd-party-libraries)
		- [Infrasturcture code](#infrasturcture-code)
		- [The domain level](#the-domain-level)
		- [The application level](#the-application-level)
		- [API](#api)
		- [GUI and acceptance tests](#gui-and-acceptance-tests)
		- [Summary](#summary)
	- [Dependency tree](#dependency-tree)
	- [Exercises](#exercises-1)
- [7. Interfaces](#7-interfaces)
	- [Real world interfaces](#real-world-interfaces)
	- [Code interfaces](#code-interfaces)
	- [APIs](#apis)
		- [Adding more functionality](#adding-more-functionality)
		- [Semantic Versioning](#semantic-versioning)
	- [Conclusion](#conclusion)
- [8. Functions](#8-functions)
	- [Do one thing only](#do-one-thing-only)
	- [Temporal coupling](#temporal-coupling)
	- [Number of arguments](#number-of-arguments)
		- [Copilot](#copilot-1)
	- [Output arguments](#output-arguments)
	- [Return values](#return-values)
	- [Copilot](#copilot-2)
- [9. Classes](#9-classes)
	- [Data classes and structs](#data-classes-and-structs)
	- [Private or Public](#private-or-public)
	- [Functions and Methods](#functions-and-methods)
	- [Different kind of classes](#different-kind-of-classes)
		- [Data class](#data-class)
		- [Pure method classes](#pure-method-classes)
		- [Delegating class](#delegating-class)
		- [Worker class](#worker-class)
		- [Pure Abstract Base Class](#pure-abstract-base-class)
		- [Implementation class](#implementation-class)
		- [Inheritance classes](#inheritance-classes)
		- [General recommendations](#general-recommendations)
	- [Constant Class instances](#constant-class-instances)
		- [Mixing const and non-const objects](#mixing-const-and-non-const-objects)
	- [Free Function vs. Method](#free-function-vs-method)
	- [Constructors](#constructors)
	- [Getter and setter functions](#getter-and-setter-functions)
		- [Data classes](#data-classes)
		- [Worker classes](#worker-classes)
		- [Delegating classes](#delegating-classes)
		- [Other points of consideration](#other-points-of-consideration)
	- [Lose and strong coupling](#lose-and-strong-coupling)
		- [Coupling and Cohesion](#coupling-and-cohesion)
		- [Worker classes](#worker-classes-1)
		- [Other class types](#other-class-types)
		- [Inheritance](#inheritance)
	- [Static expression](#static-expression)
	- [Drawbacks of classes](#drawbacks-of-classes)
	- [Example](#example-1)
	- [Conclusions](#conclusions)
	- [Copilot](#copilot-3)
	- [Exercises](#exercises-2)
- [Inheritance](#inheritance-1)
	- [Drawbacks of Inheritance](#drawbacks-of-inheritance)
		- [Tight Coupling](#tight-coupling)
		- [Error prone](#error-prone)
		- [Obscure code](#obscure-code)
		- [Implementation](#implementation)
		- [Overriden baseclass functions](#overriden-baseclass-functions)
	- [Advantages of Inheritance](#advantages-of-inheritance)
		- [Code reuse](#code-reuse)
	- [Interfaces](#interfaces)
	- [Conclusions](#conclusions-1)
- [10. Testing](#10-testing)
	- [A short story about tests](#a-short-story-about-tests)
	- [Test examples](#test-examples)
		- [When, what and how](#when-what-and-how)
	- [General thoughts about tests](#general-thoughts-about-tests)
		- [Double Entry Book Keeping](#double-entry-book-keeping)
		- [Understand what you do](#understand-what-you-do)
		- [A few general tips](#a-few-general-tips)
		- [Quality of test code](#quality-of-test-code)
	- [Number of test cases](#number-of-test-cases)
	- [Parts of a test](#parts-of-a-test)
		- [Setup and Teardown](#setup-and-teardown)
		- [Helper functions](#helper-functions)
		- [Test body](#test-body)
	- [Problematic tests](#problematic-tests)
		- [Dependent tests](#dependent-tests)
		- [Flaky tests](#flaky-tests)
		- [Britle tests](#britle-tests)
		- [Random numbers](#random-numbers)
	- [When what and how](#when-what-and-how-1)
		- [When to run tests](#when-to-run-tests)
		- [The Beyonce rule](#the-beyonce-rule)
		- [Mocking and Stubs](#mocking-and-stubs)
	- [Untestable behavior](#untestable-behavior)
- [11. Types of tests](#11-types-of-tests)
	- [Unit tests](#unit-tests)
		- [Testing files](#testing-files)
		- [Testing classes](#testing-classes)
		- [Copilot](#copilot-4)
	- [Integration tests](#integration-tests)
	- [End-to-End tests](#end-to-end-tests)
	- [The testing pyramid](#the-testing-pyramid)
	- [Exercises](#exercises-3)
- [12. Writing good Code with Tests](#12-writing-good-code-with-tests)
	- [Unit tests](#unit-tests-1)
	- [Component tests](#component-tests)
	- [Testing existing code](#testing-existing-code)
	- [Asserts](#asserts)
	- [Test Driven Development](#test-driven-development)
		- [Importance of TDD](#importance-of-tdd)
		- [Example](#example-2)
	- [Fakes and Mocks](#fakes-and-mocks)
		- [Mocking](#mocking)
		- [Faking](#faking)
		- [Dependency injection](#dependency-injection)
		- [Copilot](#copilot-5)
- [13. Refactoring](#13-refactoring)
	- [There will be change](#there-will-be-change)
	- [Keeping code in shape](#keeping-code-in-shape)
		- [Refactoring and automated test](#refactoring-and-automated-test)
		- [Keep refactorings small](#keep-refactorings-small)
	- [Levels of Refactoring](#levels-of-refactoring)
		- [Refactoring is dynamic](#refactoring-is-dynamic)
		- [The circle of doom](#the-circle-of-doom)
	- [When to Refactor](#when-to-refactor)
	- [Refactoring process](#refactoring-process)
	- [Refactoring techniques](#refactoring-techniques)
		- [Renaming](#renaming)
		- [Extract function](#extract-function)
		- [Scratch refactoring \[Feathers p. 212\]](#scratch-refactoring-feathers-p-212)
	- [Real life refactoring](#real-life-refactoring)
		- [Seams](#seams)
		- [Sketches](#sketches)
	- [Copilot](#copilot-6)
	- [Exercises](#exercises-4)
- [14. Understandable code](#14-understandable-code)
	- [Exercises](#exercises-5)
- [15. Programming languages](#15-programming-languages)
	- [Existing programming languages](#existing-programming-languages)
	- [Code examples](#code-examples)
	- [Python](#python)
		- [Type hints](#type-hints)
		- [Slots](#slots)
	- [Abstract base classes](#abstract-base-classes)
	- [C++](#c)
		- [Pointers and arrays](#pointers-and-arrays)
			- [Smart pointers](#smart-pointers)
			- [Vectors](#vectors)
		- [Pass by reference](#pass-by-reference)
		- [Classes](#classes)
		- [Structs](#structs)
	- [Copilot](#copilot-7)
	- [Exercises](#exercises-6)
- [16. Bugs, Errors, Exceptions](#16-bugs-errors-exceptions)
	- [Syntax Errors](#syntax-errors)
	- [Bugs](#bugs-1)
		- [Cost of Bugs](#cost-of-bugs)
		- [Debugging](#debugging)
		- [Copilot](#copilot-8)
	- [Exceptions](#exceptions)
		- [Wrapping exceptions](#wrapping-exceptions)
		- [Exceptions and goto](#exceptions-and-goto)
- [18. Programming Paradigms](#18-programming-paradigms)
	- [Object Oriented programming](#object-oriented-programming)
	- [Procedural programming](#procedural-programming)
	- [Functional programming](#functional-programming)
	- [Conclusions](#conclusions-2)
	- [Copilot](#copilot-9)
- [19. Design patterns](#19-design-patterns)
	- [Factories](#factories)
	- [Visitor](#visitor)
		- [Implementation](#implementation-1)
	- [Strategy pattern](#strategy-pattern)
	- [Façade](#façade)
	- [Adapter](#adapter)
	- [Template](#template)
	- [Flyweight](#flyweight)
	- [Observer](#observer)
	- [Copilot](#copilot-10)
- [20. Decoupling](#20-decoupling)
	- [Exercises](#exercises-7)
- [21. Physical laws of code](#21-physical-laws-of-code)
	- [Entropy](#entropy)
	- [Correlation](#correlation)
- [22. Software Architecture](#22-software-architecture)
	- [About Architecture](#about-architecture)
		- [Coupling](#coupling)
- [23. Solid principles](#23-solid-principles)
	- [Single Responsibility Principle](#single-responsibility-principle)
	- [Open Closed Principle](#open-closed-principle)
	- [Liskov Substitution Principle](#liskov-substitution-principle)
	- [Interface Segregation Principle](#interface-segregation-principle)
	- [Dependency Inversion Principle](#dependency-inversion-principle)
		- [Example](#example-3)
		- [Pimpl](#pimpl)
	- [Summary](#summary-1)
	- [Exercises](#exercises-8)
- [24. Datatypes](#24-datatypes)
	- [Lists](#lists)
	- [Enums](#enums)
	- [Booleans](#booleans)
		- [Switch statements](#switch-statements)
	- [Strings](#strings)
		- [Boolean logic](#boolean-logic)
		- [Natural Language](#natural-language)
	- [Dicts](#dicts)
	- [Trees](#trees)
	- [Pointers](#pointers)
- [25. Variable Properties](#25-variable-properties)
	- [Compile-time constant](#compile-time-constant)
	- [Constant](#constant)
	- [Mutable](#mutable)
	- [Member variables](#member-variables)
	- [Static Variables](#static-variables)
	- [Dynamic Variables](#dynamic-variables)
	- [Global Variables](#global-variables)
	- [Variable comparison](#variable-comparison)
- [26. Naming](#26-naming)
	- [Copilot](#copilot-11)
	- [Exercise](#exercise)
- [28. Complexity](#28-complexity)
	- [Complexity of code](#complexity-of-code)
	- [Estimating complexity](#estimating-complexity)
	- [Single line complexity](#single-line-complexity)
	- [Back magic code](#back-magic-code)
- [29. Data files](#29-data-files)
	- [CSV](#csv)
		- [Copilot](#copilot-12)
	- [Json](#json)
		- [Copilot](#copilot-13)
	- [XML](#xml)
		- [Copilot](#copilot-14)
	- [TOML](#toml)
	- [YAML](#yaml)
	- [HDF5](#hdf5)
		- [Copilot](#copilot-15)
	- [Databases](#databases)
	- [Custom file format](#custom-file-format)
	- [Exercise](#exercise-1)
- [30. Setting up a project](#30-setting-up-a-project)
	- [Project folder](#project-folder)
	- [Exercise](#exercise-2)
- [31. Performance Optimization](#31-performance-optimization)
	- [Exercise](#exercise-3)
- [32. Comments](#32-comments)
	- [Bad comments](#bad-comments)
		- [Commented out code](#commented-out-code)
		- [TODO comments](#todo-comments)
	- [Useful comments](#useful-comments)
		- [Docstring](#docstring)
	- [Summary](#summary-2)
	- [Copilot](#copilot-16)
	- [Exercises](#exercises-9)
- [33. Logging](#33-logging)
	- [Exercises](#exercises-10)
- [34. Tools](#34-tools)
	- [Version control software](#version-control-software)
		- [Git, everywhere git](#git-everywhere-git)
		- [Copilot](#copilot-17)
	- [Command line](#command-line)
		- [Copilot](#copilot-18)
	- [IDE](#ide)
	- [Continuous Integration](#continuous-integration)
	- [Debugger](#debugger)
	- [Profiler](#profiler)
	- [Formatter](#formatter)
	- [Code quality checker](#code-quality-checker)
	- [Pip, cmake](#pip-cmake)
	- [Ticketing system](#ticketing-system)
	- [Wiki](#wiki)
	- [Docstring](#docstring-1)
	- [Exercises](#exercises-11)
- [35. Domain Driven Design](#35-domain-driven-design)
	- [Ubiquitous Language](#ubiquitous-language)
	- [Describing a model](#describing-a-model)
	- [Implementing a Model](#implementing-a-model)
	- [Maintaining the model WIP](#maintaining-the-model-wip)
		- [Unified model](#unified-model)
		- [Separate ways](#separate-ways)
		- [Conformist](#conformist)
		- [Developer Client relationship](#developer-client-relationship)
	- [Refactoring toward deeper insight](#refactoring-toward-deeper-insight)
	- [Entities, value objects, aggregates, … WIP](#entities-value-objects-aggregates--wip)
	- [Domain level, old text](#domain-level-old-text)
	- [Exercises](#exercises-12)
- [36. Good code](#36-good-code)
- [37. 3rd party software](#37-3rd-party-software)
- [38. Dependencies](#38-dependencies)
	- [Circular dependencies](#circular-dependencies)
		- [Example](#example-4)
- [39. Working in teams](#39-working-in-teams)
	- [Team structure](#team-structure)
		- [The bus factor](#the-bus-factor)
	- [Developers work](#developers-work)
	- [Communication](#communication)
	- [Working with humans](#working-with-humans)
	- [Working with customers](#working-with-customers)
- [40. Code review](#40-code-review)
	- [Drawbacks](#drawbacks)
- [41. Working with existing projects](#41-working-with-existing-projects)
- [42. Planning](#42-planning)
	- [Planning code # move elsewhere? Rename section?](#planning-code--move-elsewhere-rename-section)
- [43. Agile](#43-agile)
	- [Agile values](#agile-values)
	- [Work planning](#work-planning)
	- [QA](#qa)
	- [The Iron Cross](#the-iron-cross)
		- [Good](#good)
		- [Fast](#fast)
		- [Cheap](#cheap)
		- [Done](#done)
	- [Sprints](#sprints)
	- [The end of the project](#the-end-of-the-project)
	- [Becoming agile](#becoming-agile)
	- [Agile = Courage + Feedback + Simplicity + Communication](#agile--courage--feedback--simplicity--communication)
		- [Courage](#courage)
- [44. Continuous integration](#44-continuous-integration)
- [45. Hiring and getting hired](#45-hiring-and-getting-hired)
	- [Hiring](#hiring)
	- [Getting hired](#getting-hired)
- [46. Work ethics](#46-work-ethics)
- [47. Examples](#47-examples)
	- [Apple pie](#apple-pie)
		- [User story](#user-story)
		- [Implementation](#implementation-2)
	- [Paint](#paint)
- [More Copilot](#more-copilot)
- [48. Further reading](#48-further-reading)
- [49. Outlook](#49-outlook)
- [Abbreviations](#abbreviations)


# 3. Preface
"I have been consistently disappointed by the quality of CS graduates. It’s not that the graduates aren’t bright or talented, it’s just that they haven’t been taught what programming is really all about." - Robert C. Martin

In 2007 I had my first semester at university. It was the first time I learned programming. We learned C++ and I found it very confusing. Especially things like plain old arrays, pointers, the const expression, etc. I somehow struggled understanding these things. They just felt wrong. There were so many open questions about how to write the code properly and I didn’t know where to get good advice. I passed the exam, but I was somehow dissatisfied.

Three years later I took a course on computational physics. There I had to write slightly bigger programs. It worked, but I struggled a lot. The code was dreadful and I knew it. But I didn't know how to make it better. Changing things was hard and I learned how to use a debugger. I still have all my university files around, but I didn’t dare to look at this code ever since. Already thinking about it makes me shudder.

After my studies I wanted to improve my programming skills and bout the book “Effective modern C++” by Scott Meyers. A good book. But not for me at the time back then. It deals with a lot of details of C++ and I understood barely a thing because I was missing the background.

Another few years later I decided to give it another shot with programming. I found a company that was searching for people with programming and physics knowledge. So, I fought I might have a chance, despite my poor programming skills. At the job interview I was asked a few very technical (and in hindsight fairly useless) C++ questions and I could answer most of them. I got the job.

In the beginning a struggled a little. I was overwhelmed by the amount of code, I didn’t know what IDE to use and the make build I used was flawed. You name it. Still, I good some very good feedback by my boss. A few months later I had my first big feature implemented. It also had automated tests and the code was much cleaner than comparable features. Another month later I implemented my second feature. Everyone in the company expected this to be very difficult, but I found a neat way to implement it.

My boss wrote most of the code and the success of the company was based to a fair amount on his efforts. He knew everything, but I hardly ever understood what he was talking about. It was all too difficult. 

Around that time the company hired some more software developers. Especially one of them made a huge impression on me. I could ask him almost anything and he was able to give me a simple answer. He knew the concepts that our code was based on which allowed him to understand the fundamental structure in our code and sort out all the rest. But it was also the way he worked. He wrote small functions covered with automated tests. He was also refactoring the code. One Monday morning he came to the office. He made a gigantic merge request and made the comment “I fell into a shit hole”. He opened my eyes. He made me realize the way he works was so much better. So much more structured. This was engineering. Software engineering.

There is so much I learned in the few years since my friend fell into the shit hole. And the basic principles are so easy to learn. This book is what this book is about. No fancy code. But fundamental principles. It gives you an overview of the most important topics such that you don’t get overwhelmed by all the possibilities a programmer has. It also contains a lot of real-world examples that don’t use any code at all. I want to explain principles that are very general and don’t need any code to explain. In fact, software engineering is with some respects very similar to other engineering jobs. Therefore, a car or a computer are frequently better examples than some fancy code you struggle understanding.

I’m not a great software engineer, not at all. And my English is fairly lousy. But maybe this is a good thing when writing a book. It will be easy to understand and I tried to keep all chapters down to the point and easy to understand. It keeps the book short and motivates you to read it all, because everything I wrote is important. At least that's what I think.

I'm not god and this is not the holy bible. This book tries to help you with your programming problems, but it doesn't contain the absolute truth. Probably there are hardly any absolute truths in programming, there are only trade offs. I hope that the recommendations I give in this book help you write better code. And if you regard this book as important enough to make a youtube video about it and critisize some parts of it, even better. 

This book is only a step in your career. Now you have to get out into the real world. Get a job. Write code and learn how to apply the principles you learned here. It is hard, this will take your whole life. Others have the same problems. Talk to them, improve your solutions, get smarter. Become a real software engineer.

Enjoy my book and good luck with your career.

# 4. Introduction

"If I had an hour to solve a problem I'd spend 55 minutes thinking about the problem and 5 minutes thinking about solutions." – Albert Einstein

In this chapter we want to look at how code should look like. What kind of rules there are to judge the quality of code and some of my personal recommendations what kind of features of your programming language you should, or rather shouldn’t, use. In my opinion there are plenty of things, especially in object oriented (OO) programming that are only used due to historic reasons. In reality they are only leading to bad code and should be abandoned. In fact, pretty much everything else than plain classes should be taken with care in OO programming.

But OO programming is by far not the most important topic in this book. No matter how good or bad your usage of OO features, you can write good or bad code independently. There are more important things to learn throughout this book. Most notably the Single Responsibility Principle (SRP), basics on interfaces, testing and naming. Furthermore, there are several chapters on how to work with code that has not been written up to current standards and how to collaborate with other programmers. Topics which are highly important but are frequently neglected in books on software development.

This book contains very little code. It’s more about concepts or software engineering, rather than difficult examples. Still, some of the concepts are easier to understand with a few lines of code. As the programming languages I chose mostly python and a some C++. Not because these languages would be better than for example JavaScript, but rather because these are the languages I know.

This book tries to give clear answers to simple problems. I also try giving answers to hard problems, but these are, as in other books, usually fairly vague. The only thing that really helps against hard problems is a lot of experience. It would take too much explanations or code to explain all the details. I can only try to lay out all the different arguments for some tradeoffs and then you have to do all the reasoning by yourself. This is why software engineering is hard. There are just too many problems without any clear solutions. And you have to solve them all by yourself.

This book is about engineering, not about a scientific approach. Thus there is no absolute truth. I rather give some general advice. For this reason, there are only few references for specific topics. Many chapters are my personal summary about some other more specialized book, thus I mention what book I was reading as a foundation for the corresponding chapter.

## The Life of a Software Engineer

I know you want me to get started and show you some fancy code examples. And I’m sorry to tell you that this is not happening. We don’t even know yet what this book should be about. Of course, you want to become a great software engineer get a job at google earn a lot of money and life a happy life. But this is all so vague. We have to sit down and analyze the situation. I even found moral support from a fellow physicist.

Let me start with a very blunt question: What do you think does a software engineer do?

“He writes code” may be your first response.

“He engineers software” is a very smart one.

Indeed, these answers contain some truth. But writing code covers only a tiny fraction of your future working day. One thing you will do is the same as we do right now: you analyze a problem and try to figure out what to do next. 

Your boss will not let you write code for a month just for the sake of writing code. You will be spending quite a lot of time in meetings and talking to other people about figuring out what you should do exactly. What your customers want. 

The first rule of software engineering

**We write code in order to create value for our customers.**

If you don’t like meetings nor customers you can stay at home and write whatever code you like. But unless you are a genius, chances are very low anyone will pay you for that. It is more rewarding to write mediocre code that’s being used rather than writing brilliant code no one cares about.

Besides the meetings, you will of course spend a fair amount of time with your precious code. But I have to disappoint you once again. It will be like in a marriage. You spend most time on cleaning up code or discussing things with your colleagues. The part that’s really fun covers only a small fraction of it. The following plot with highly unscientific numbers sums it up nicely.

<img src=images/programmerActivity.png width="400">

You certainly have to look twice to grasp the meaning of this plot. You will spend only 5% of the time implementing new features! 5%! Not including all the meetings that you have to visit as well. Of course, these numbers are only a very rough estimate. They depend on many factors. If you work on a new project there is no refactoring (code clean up) required yet and there is less code for you to read. Ultimately, you’ll spend more time coding. In a very big project, it takes more time to implement changes. It can take a year until you are fully productive in a big project! But the company is already earning money with this code for a long time, so adding new features is not that important anymore. Either way, I will continue the discussion with the value from the plot.

The most obvious and undeniable conclusion we can draw from the plot is that software engineering is not about writing code. It’s about reading code! If you can reduce the time required to read code by half you save more time than you spend writing code in total. By a lot. 

The second rule of software engineering:

**We write code that is easy to understand.**

Good code is not fancy, good code is not complex and it’s not necessarily short. Good code is simple. It is as simple as it gets. Reading good code is not like reading Shakespeare. It’s ... it’s rather like watching Donald Trump... Knowing only 1000 different words is great if you are a politician. Everyone understands him. Even as people are tired, they like watching him on TV. I’m sometimes embarrassed because of my lousy English. But writing these lines is really cheering me up. Most people reading this book are not native English speakers neither and therefore my somewhat limited language may actually help with that respect. It makes it easier to understand. And with code it’s fairly similar. Simple code is good because it's easy to understand.

Good code uses only the bare minimum of syntax that a programming language offers. It is great if you don’t know a programming language too well. You don’t fall into the trap of using fancy but useless features. Don’t learn programming languages. Learn programming. Unless you work for google on some other company working on highly specialized code, you will never need all the gimmicks some programming languages offer.

// somehow I'm not happy with the transition here. Is there some other way to change the topic?

Of course, we are not politicians. We are software engineers. What we write has to be absolutely correct. Unlike politicians, we have responsibility. If we make mistakes, air planes may crash. People may die!

Urm... let me rephrase that as well... 

Unlike politicians, we have honor. We don’t want to be responsible for people to die. We want to write code that is impeccable. We want to be absolutely certain that there are no bugs. We constantly check our code is correct. We test our code. We let our computers test our code. We write code that tests our code!

The third rule of software engineering

**We write automated tests that cover all our code.**

Now let’s go back to our lovely plot. There is one more huge chunk of work. Changing existing code. Also known as refactoring. Yes, as astonishing as it sounds you have to clean up your code just the same way as you have to clean up your kitchen. The importance of refactoring cannot be understated. It helps you keeping the logic of the code under control by sorting things out. All the time, over and over again. Without refactoring your code quite quickly becomes such a huge mess, you will barely be able to make any changes. And there will be a million places where bugs can hide.

The fourth rule of software engineering

**We constantly clean up our code.**

Now you know what the life of a programmer will look like. Now you know what to look out for. Now we can do what you wanted me to half an hour ago. I can explain to you the fundamental principles how to write good code.

These four rules will accompany us throughout our book.

//make a list of the 4 rules in a box

// The fundamentals

# 5. Single responsibility principle 

Every object does exactly one thing. Everything is done by exactly one object.

There are different definitions of the Single Responsability Principle (SRP). I don’t think the differences between them really matter. It is much more important that you get the idea behind it.

The SRP is probably one of the most important topics in this book and in all of software development. It says that every piece of code should have exactly one task. It is the foundation to write readable code.

## Do not Repeat Yourself

// DRY does not always have to be obeyed that stricty. Repeat yourself until it is clear what the acronym should be.

You should not copy paste code. This violates the Do not Repeat Yourself (DRY) principle, unless you immediately remove the duplication. As you have duplicated code, something is not done by exactly one object but rather by two. Instead write a function and use the function from now on. This covers most cases violating the SRP.

The DRY principle also applies to processes like building your project. If you have to repeat your steps there is something wrong. Instead you should automate the whole process. 
//97-things-every-programmer-should-know chapter 63

// See 97-things-every-programmer-should-know chapter 42. The build should be one step running through without any warnings or errors. Warnings are unnecessary mental work. Even if ignored. Clean them up immediately. -> where did I write something similar before? -> chapter automatization?

The other cases are code that emerged as a duplication over time. Frequently, one piece of logic is needed at several different places and due to the lack of knowledge is reimplemented several times. This kind of duplication has to be refactored out relentlessly.

// remark that switch case statements are a frequent source of SRP violation.

## Advantages of the SRP

The importance of the SRP cannot be overstated. It alone makes your code an order of magnitude better when applied properly or worse when ignored. And it is fairly simple to learn. There are dozens of reasons why this is the case. Here are the most important ones.

### Understanding
A function or class that implements exactly one thing will always be quite easy to understand. It all follows the same logic and there will be no unexpected behavior. Additionally, the code for a certain problem will be short as it focuses only on its core. All other duties are resolved elsewhere.

### Naming
Giving names to objects is one of the hardest tasks of a programmer and can be extremely frustrating. Names are always either too long or not expressive enough. This is an indication you might have violated the SRP. If an object obeys the SRP, it does one thing. And naming an object that does only one thing is usually not that hard.

### Duplication
Every bit of logic is taken care of in exactly one place in your code. You have no code duplication. You are not allowed to copy paste any code. Do not Repeat Yourself. DRY. However, this does not only apply to copy paste code. It can also be that there are two pieces of code quite far apart in the code doing very similar things. Every time you see redundant code you should immediately start refactoring. The most common issue in code duplication is several programmers developing the same piece of logic. This can lead to huge amounts of code duplication without anyone ever copy pasting anything.

### Testing
Writing unit tests becomes fairly simple as well. A class obeying the SRP is not so big, setting it up is probably not a big deal, nor is understanding the logic behind it. You know exactly what the idea of the class is and finding the important parts to test becomes easy. Just look at the few public functions. And as the class is simple, you will be immediately able to tell what the expected output of the function will be.

### Bugs
As the purpose of each class becomes clearer, it will be easier to structure the logic of your problem. You will only write code that makes sense. You will create way less bugs. And it’s very hard for those bugs to hide. Frequently you know right away why a bug showed up. It is immediately apparent which part of the code is responsible for the behavior of the bug.

### Bug fixing
Tracking down bugs will be much easier. You can fairly well understand what each class should do and therefore find unexpected behavior much quicker. However, fixing a bug becomes harder at first sight. You are not anymore allowed to randomly add and if statement in your code. This would violate the SRP and is bad code. Instead you have to find a proper solution. Which usually turns out easier than applying some ugly hot fix. And especially it really fixes the bug once and for all.

## Example
Let's have a look at a very short example. Even though it is only 5 lines long, it violates the SRP. Can you figure out why?

```py
def print_body():
	# print something

def print_page():
	print("author: Marco")
	print("*************")
	print_body()
	print("copyright my company")
	print("page number 1/1")
```
The problem are the different levels of abstraction. Printing a string is clearly a lower level of abstraction than calling a function which probably prints a string as well. There should either be only print statements or function calls within a piece of code. Thus there are 2 possibilities. We can either unroll the `print_body` function if it's fairly short or write functions for the other print statements. The later is probably the prefered solution as it's fairly easy to create these functions.

```py
def print_header():
	print("author: Marco")
	print("*************")
	
def print_body():
	# print something

def print_footer():
	print("copyright my company")
	print("page number 1/1")

def print_page():
	print_header()
	print_body()
	print_footer()
```

Now all of the code looks very uniform. This is an indication that the SRP is now fulfilled.

Admitedly I was a little bit picky here. But I can't make much more convoluted examples in a book.

## Orthogonality

Orthogonality is a mathematical definition. It states that two objects are under a right angle in the current coordinate system. The first part of this sentence may seem intuitive, but the part about the coordinate system...? Let me show you a brief example that everybody knows.

// TODO search images without copy right
<div class="row">
    <img src ="images/water_valve2.jpg" alt="retro water tab"width="247">
    <img src ="images/water_valve1.jpg" alt="new water tab" width="200">
</div> 

On the left-hand side, we have old school water tabs. The user has 2 degrees of freedom. One for the amount of cold water and one for the amount of warm water. However, this is not what the user generally wants. It turns out, the user wants to be able to control the 2 degrees of freedom differently. He wants to control the total amount of water along with the temperature of the water. The orthogonal solution from the user perspective is shown on the right-hand side. The solution on the left-hand side is outdated. It is orthogonal in the engineers coordinate system but nowadays we have higher requirements and are not satisfied with the engineers’ solution anymore. We expect this coordinate transformation into the users coordinate system to be done inside the water tab.

In software engineering we encounter exactly the same phenomenon. We have a downstream person (user) and an upstream person (developer). Both want to deal with orthogonal data, but they may be working in separate coordinate systems. Now it is always the upstream persons job to transform the output to make the data orthogonal in the downstream persons coordinate system. This is similar to other cases where it is always the upstream persons duty to make the downstream persons life as comfortable as possible by converting the data handed over.

It may not always be that obvious how the downstream would like the interface to look like. When in doubt, the upstream should return the data in the most general representation. Make sure there are no implementation details leak into the interface, even tough this is easier said than done. This has the highest chances to be orthogonal from the user point of view.

Frequently you cannot choose how the data looks like you work with. For example, if it originates from a third-party library. And the data at hand really does not fit to the algorithm you want to use for your specific problem. In this case you should first orthogonalize the input data before continuing. Separating the orthogonalization and algorithm steps is much simpler than running an algorithm on a dataset that is not optimally set up to start with. 

A common example is the coordinate transformation between spherical (r $\phi$ $\theta$) and Cartesian (x y z) coordinates. Some problems are easier to solve in one coordinate system, others are more easily solved in the other coordinate system. In most cases it’s best to first convert the data into the appropriate coordinate system, rather than adapting the algorithm. This keeps the algorithm and the coordinate transformation apart, in accordance with the single responsibility principle.

### Advantages of orthogonal systems

Working in an orthogonal system has many advantages:
-	Errors just propagate straight through the system and are easy to find. They don’t spread out.
-	Fixing these bugs is easier as the system is less fragile.
-	It is easier to write tests for an orthogonal system.
-	It decouples the code as the transformation acts as an adapter.

// figure out what else to write. Maybe add some examples.

## Copilot

// Is there some way to refactor code towards the SRP using Copilot?

## Exercises

Make an example where the SRP is violated and the code should be refactored.

Create a non-orthogonal system that the reader should orthongonalize.

# 6. Levels of abstraction

"You can solve every problem with another level of indirection." – Andrew Konig

"Except for the problem of too many levels of indirection." – my hero

Levels of abstraction is an extremely important concept in software engineering. Yet it doesn’t get the amount of attention it would deserve. It applies to so many things around us, but so few people know about it. It’s about taking a few objects and creating a new object out of it with completely different properties. Something completely new emerges.

## Real world example

You take a CPU, a mainboard, RAM, an SSD and a power supply. Some of the most complex objects human kind had ever created. From some of them you might have a rough idea what they do, and maybe even how they work. When you assemble these parts, it becomes mind boggling. So many extremely complex objects. And now we combine them. How is this going to end up? Surprisingly simple. You sit in front of it every day. It’s a computer. And all your questions are gone. It’s a higher level of abstraction and it’s fairly simple to use. As I write this book I only care about the text software that I use. I don’t care about the operating system (OS). I don’t care about the computer that’s standing on the floor. I don’t care about the CPU inside. I don’t care about the billions of transistors inside and I don’t care about the quantum mechanical effects the transistors are based on. My text software depends on all these things but I don’t have to know anything about them. All these things were abstracted away by the next higher level. The text processing programm emerged from combinind all these imensly complex objects.

One can also look at the problem bottom up. Quantum mechanics does not know anything about transistors. Transistors don’t know anything about CPUs. CPUs don’t know anything about computers, computers don’t know anything about the OS and the OS doesn’t know anything about my text software. Some things like the quantum mechanics are just there. We can’t change them, but we can use it and create other objects. Other things like the transistors are designed to operate inside a CPU. We can design transistors that meet the extremely stringent requirements to operate inside a CPU. Yet you could take a CPU, break out a transistor and use it on its own. It’s just a transistor. Albeit an extremely small one. You would need an electron microscope to do something with it. The OS supplies an interface on which the text processing software is running, but the OS doesn't care too much about the text processing software.

Another example is a company. Every company has a job hierarchy. Even if some modern companies try to keep it flat, some kind of hierarchy is still around. Every level of this hierarchy has a different task. The lowest level are the factory workers. They do the actual work. However, the other levels are also required. The department head has to make sure all his employees are happy, or at least that they do their job. And as you go further up the hirarchy, the work is more about strategy of the company. It involves more politics and HR. This is the natural way companies are organized. Big companies won’t work in any other way. The CEO cannot manage all 10’000 employees by himself, nor can he know every detail of every processes within the company. He needs this job hierarchy. He has to delegate his work and let others take care of the time-consuming details. He needs these levels of abstraction. Self organizing companies without a hierarchy frequently don't work out very well.

You create a level of abstraction every time you combine some existing objects. The new level has a higher level than the previous ones. It may have completely different properties than the lower levels. In theory the higher level combines the complexity of all the underlying objects but if the higher-level object is well designed you don’t care anymore about the lower level objects at all. Just like it's very hard to calculate the quantum mechanical properties of a simple molecule, yet you can take a statistical average and make very accurate predictions on a combustion engine or the aerodynamics of an airplane.

Creating good levels of abstraction is probably the most important task in software engineering. This is the very heart that allows us humans to understand and tackle such extremely complex tasks. You have break them up into smaller and smaller blocks that you can understand.

## Programming Example

C++ is a fairly low-level programming language. Its widespread usage has mostly historical reasons. There are a lot of things that newer programming languages do better. But it’s the same as always. The code is working and it will not be replaced because of some smaller inconveniences in the programming language. About a decade ago, some of the most fundamental issues were removed with the release of the C++11 standard.

C++ uses old school arrays. These are commands to allocate memory in order to store some objects. If the programmer doesn’t know how many objects there will be, he has to use the famous new and delete commands in order to allocate memory on the heap. These commands are extremely error prone. They were extremely hard to use. If you forgot to use delete in a corner case, the software was leaking memory and you had to restart it every few days or so.

```C++
int * arr = new int[10];
arr[0] = 42;
// etc.
delete[] arr;
```

One of the main reasons Java got so popular was the garbage collector. It took care of all the deleting. Without a doubt a tremendous improvement at the time.

Though it turns out there exists also a solution with pure C++ code. There is a quite simple pattern that ensures you to always call new and delete as the correct time. You create a class that calls new inside the constructor and delete in the destructor. No matter what you do, every object in C++ is guaranteed to call its constructor when creating and the destructor deleting the object. The constructor and destructor are both called exactly once. Always. So if we call new inside the constructor and delete inside the destructor, they are both guaranteed to be called exactly once. The allocated memory is guaranteed to be freed again. Finally, you can safely use C++ without facing the danger of memory leaks.

Here is a very simplified version how the fundamental idea of the vector class looks like. Our custom vectorClass contains an array and manages its size. This takes a little bit of logic, but in the end the user doesn't have to know anything about the array inside the vector class anymore.

```C++
// basic idea from https://www.geeksforgeeks.org/how-to-implement-our-own-vector-class-in-c/
class vectorClass {
private:
    int* arr;
	int capacity;
    int current;
public:
    vectorClass()
    {
        arr = new int[1];
		capacity = 1;
        current = 0;
	}
	~vectorClass()
    {
        delete [] arr;
    }
	void push(int data)
    {
		// at some point the size of the array is smaller than the size required. Then it's time to allocate more space
        if (current == capacity) {
            int* temp = new int[2 * capacity];
		}
		// etc.
	}
}
```

This idea how to simplify the usage of arrays changed C++. One of the biggest problems was gone. The user friendliness improved a lot. This pattern is used everywhere by everyone and has been calles Resource Acquisition Is Intialization (RAII) by Scott Myers //see Effective Modern C++

If there is a code pattern that everyone uses it becomes part of the programming language. The vector class was born. It’s a higher-level object based on the array. It hides all the nasty work with new and delete and comes with an easy to use interface and all the important functionality one would expect. The only price to pay is a tiny bit of performance due to the internal implementation details. This loss of performance is so small, you won’t be able to measure it in any ordinary software. 

Vectors are a higher level of abstraction than arrays. They are easier to use and simply better than arrays. Don’t ever bother using old school arrays. Don’t waste time learning more about arrays. I told you everything you have to know.

## The onion layers

//create a Figure with levels of abstraction. Levels: Infrastructure – Domain level – application level – API – acceptance tests/GUI

// where did I get these layers from? And I think I have to look at this again. Most graphics I found have the domain level in the center.

In your code you will also have different levels of abstraction. These can be compared to the layers of an onion. Thus it is also called the onion architecture. The outer layer always depends on the interface of the inner layer.

The innermost layer is the Domain Model. It is the heart of your software. The Domain Model cannot be bought anywhere, it is unique to your problem. It solves the complexity of your busines. It doesn't know anything about the outer layers. 

// TODO search images without copy right, sort the layers differently
<div class="row">
    <img src ="images/onion_layers.webp" alt="Example onion layers of a project"width="247">
</div> 

### 3rd party libraries

The lowest, inner most level is the programming language and 3rd party libraries. You can’t change those unless you replace them. Changing code in a 3rd party library may be possible in some cases, but I highly discourage you from doing that. Unless you take the library into your own code base and treat it the same way as all your other code. Generally, this is an extremely bad idea as it involves a huge amount of work. The only reasonable approach is writing the authors of the library and offering help to get your suggestion implemented.

### Infrasturcture code

One layer above the programming language and the 3rd party libraries we have our own low-level infrastructure code. These are generally all your basic datatypes and all the input/output (IO) code. All the technical details the user will never see. The user will not even know about. He can only guess how this code could be implemented, though in good code he will not have any clue how it's actually done.

### The domain level

//add something about domain levels. Write more exactly what the differences between the domain level and high level code are.

Then there is the domain level. This is the core of your application (though it is not the core of the onion!). It contains all the business logic of your software. This is where all the complexity of your software lies. It takes understanding of the business to understand this code here. The domain model converts the computer language from the infrastructure into a human readable language. The interface of the domain level reads almost like normal text. Every business person should be able to understand this text.

The domain level is the part that is hard to develop and you can't buy elsewhere. You have to do it yourself. Because this is what you will earn money with.

### The application level

The next level is the application level code. Here the code follows pretty much the same logic as the problem we are solving. Variables and functions have the same names as the sales person uses. It also follows the same logic. If a marketing person looks at the application level code, he should be able to understand what is going on and possibly also spot potential errors.

### API

One level higher is the API. This defines the interface between our code and the user. It’s a wrapper around the high-level code. It offers all the functionality the user would expect in an easy to use form.

### GUI and acceptance tests

On the highest level are the GUI and the acceptance tests, both at the same level. If you ever have a GUI make sure its code is completely decoupled from the rest of the code. The only interaction should be through your API. The same holds for the acceptance tests. It is so much easier writing on the API than testing a GUI. You should only test GUIs if you absolutely have to because, for whatever reason, they contain too much logic. Tough this is a clear indication of very bad sign.

### Summary

As a summary I want to emphasize again the tremendous importance of abstraction levels. Different abstraction levels are the only reason we are able to understand highly complex systems. And it’s your job to define the abstraction levels for your code. Good luck!

## Dependency tree

// I think this is somehow redundant with the explanation of the DIP?

Between classes as well as between files there are dependencies. The high-level object always depends on objects in the same level or on lower-level objects. In math we call this kind of structure a tree, or more accurately a directed acyclic graph. This graph has the additional property that there should never be any bidirectional connections, i.e., there should never be any cyclic dependencies. Diamond like shapes are fine as long as there is a unique direction of the dependencies.

//add a graph with dependencies, explain the levels of abstraction better

// abstract vs concrete code -> see Clean Architecture?

## Exercises

Sort the following function calls by their level of abstraction, starting with the highest:
- main()
- look_up_flight()
- select_flight_from()
- plan_voyage()
- book_flight()

# 7. Interfaces

“Make interfaces easy to use correctly and hard to use incorrectly" - Scott Meyers, The fundamental rule of interfaces

Interfaces go hand in hand with levels of abstraction. Each level of abstraction has two interfaces. One to the low-level side, another one towards the high-level side.

In this chapter we learn that interfaces exist not only in software but also in the real world. And we can learn a great deal from them. An interface is always the connection between a developer and a user. It is defined by the developer, but it should be designed from a user perspective. Because the developer has to implement it only once while the users might have to interact with the interface millions of times. Thus it pays off to design an interface properly.

## Real world interfaces

Functions, classes, libraries and also complete software or smartphone apps have an interface. Even technical objects like plugs have an interface. The technical details may vary quite a lot but the basic principles are very similar.

“Plugs”, you may laugh. Yes, even plugs. Electric plugs in America look different than the European ones. It is impossible to plug in an American plug into a European plug and vice versa. This is due to historical reasons, but at the same time also a safety measure. It prevents you from connecting your American 110V device into a European 230V plug causing damage. It’s fail-save. Though pretty much all devices can deal with both voltages by now.

An example of bad design is the USB 2 port. The USB stick looks symmetric on the outside but in reality, it is not. Someone once said you always needed 3 attempts to plug in a USB 2 cable. The first time would have been right but you didn’t manage, the second time was the wrong way around and the third time you managed. USB 3 has a much more user-friendly design. You can plug it in either way. The technicians implemented a technical solution to enable this. The two devices involved have to negotiate between each other how to use the different lanes of the cable. This is some extra work for the engineers, but once solved it is a very convenient solution for the users.

Another example are water tabs for showers, as already explained in the chapter on orthogonality. There are 2 tubes for cold and hot water where the plumber attached one valve each. This was a pain to use. It took quite a while to set the temperature correctly and once you changed the amount of water, the whole procedure started again. This was the engineer friendly solution, not the user friendly one. This was a bad interface. 

The new handles allow you to choose the amount of water and the temperature separately. This might be technically a little bit more complicated to implement but it’s so much more convenient to use. 

Notice how both solutions have 2 degrees of freedom. A mathematician would call this a coordinate transformation. With the old valve you and all other users had to do this transformation yourselves. With the new valve this is solved mechanically once and for all. 

I hope these simple examples gave you an idea what good interfaces are about. If you design an interface, you should always know your customers. What do they do? How do they think? How are they going to use your product? This is of utmost importance. A good interface is user centric. It represents the way the user thinks and hides all the technical details.

Car engines are operating best around roughly 2000-3000rpm. At lower rotations the engine could not operate properly, running it faster makes it inefficient. This problem is mitigated by the gear box that allows your car to operate at a wide range of velocities.

Now there used to be a minor problem about the gear boxes. They were not user friendly. The user had to manually change the gear using a clutch. Most car drivers get the hang out of it quickly, but it is certainly not user friendly. Most car drivers only want to get to work, the restaurant, etc. They only want to set the speed of the car. They do not want to care about neither the gear box nor the clutch in their car!

Now there is a well-known solution: automatic gears. A car can drive at any pace of choice and the automatic gear box will select the most suitable gear. Problem solved. You pay a little fee for the automatic gear but you’ll never have to think about it again. Now we only have to wait for self-driving cars in order to remove the steering wheel and the speed bar all together.

## Code interfaces

Once again, understanding interfaces in general will allow you to write much better code. It’s just the same as in the examples above. Try to follow the same principles. Figuring out what the user really wants, makes writing a well-designed interface quite easy. Writing some user code examples will help you a lot.

Always define an interface from the user perspective. What is it a user wants? How does he want to use your code? These are the important questions to ask. 

An interface that is designed from the engineers point of view is usually no good. It is designed from the wrong point of view. An engineers interface is easy to implement but not that easy to use as engineers look at what they have and lack the visions of what they could have. Thus, they miss the point of a good interface. An engineers interface is like an old Nokia phone. It's shape and functionality is mostly given by the engineers. They gave the designers strict limitations on what they could do. Meanwhile a good interface is more like an iPhone. Here is was the other way around. Designers told the engineers what they had to do and the solution was a phone with an easy to use interface.

Interfaces are everywhere. Every function or class has an external interface and uses several interfaces from other functions or classes. This is why understanding good interface design is paramount. Especially with classes it is hard to define a good interface that let's the user do what he wants without exposing too much of the internals of the class. But also with functions one has to consider how the function arguments should be ordered.

// Big data structures take more time to build up but at the same time they are used longer. Having small data structures around for a long time is a sign for bad code. -> bundle your data into some bigger objects.

// is there something else left to write here? It feels very short. Figure out a good example?

## APIs

"With a sufficient number of users of an API, it does not matter what you promise in the contract: all observable behaviors of your system will be depended on by somebody." - Hyrums law

The Application Programable Interface (API) is an extremely important part of your software. It is the public interface of your software. It is what everyone sees from the outside. Everything we discussed in the interface section matters here as well, but in an API, it is really important to get everything right. Having a bad API will cost you a lot of money. People won’t buy your product if the user experience is bad. They rather go to the company next door and buy their software. "They support even emojis!" Yes, sadly enough, supporting emojis is important nowadays for business reasons.

That was no joke by the way. Apple once had an important security fix in their latest update. They add new emojis to the update as emojis are the better motivation to install an update than a security fix.

APIs are an extremely difficult topic. Not so much for technical reasons, but rather because you deal with users outside the company. They use your code hidden underneath the API. Every change you make in your code could potentially lead to a bug in your client’s code. Even fixing a small bug in your own code. When maintaining an API, you have exactly one task: Never ever break your clients code! Now you might think this is doable. But I can promise, you will get nightmares.

You are always allowed to add new functionality as long as you don’t change the functionality implemented with the old syntax. The old code is guaranteed to run exactly the same way it did before, but you can use some new functionality as well. Vice versa you are never allowed to change or delete existing functionality. This would lead to compilation errors or, even worse, bugs in the user code. And that’s when customers go rampage. "Up to now the code worked and all of a sudden it fails. What the **** did you do?" If you don’t understand this harsh reaction, you never had a work colleague breaking your code once in a while. You would feel exactly the same.

### Adding more functionality

You want to add a new option to one of your API functions, but there is a lot of customer code out there. This code doesn’t use this new option so far and won’t use it in the future. How can you add this option without breaking this old user code?

The answer are default arguments. The current behavior is set to be the default and after the update, the user can select an alternative option inside the function call. This works in all modern programming languages. You don’t even need an if statement.

Removing functionality on the other hand is really hard. This inevitably changes the behavior of existing functionality. You are not allowed to do so except under very special circumstances, as explained in the next section.

### Semantic Versioning

APIs have version number. These are 2 or 3 numbers separated by dots. For example, "3.11.2", the latest python version at the time of writing. "3" is the major version, "11" is the minor version and "2" is the trace. The last is generally used only in bigger projects. 

Every time you make a new release you increase the version number. 
- For bug fixes or internal improvements, you increase the trace number. This is for all kind of changes the user shouldn’t notice or probably doesn't care about. The user should be able to increase to a higher trace version without any issues.
- The minor version number is increased for new features. The changes explained so far still backward compatible as they don’t change any existing functionality. 
- The really big disaster starts with major version changes. Sometimes this is required and it is dreadful. You might think that it’s not so much effort for the customers to change some code. "HA!" Think again. To migrate most of the python code to the major version 3 took 20 years and only a few years ago the support of python 2 was stopped. The transition was pretty much a nightmare because a lot of libraries available were not yet updated. Users simply don't have time to update their code to a new major version of your library. So if you don't want to lose them, you should make damn sure you don't break the old interface.

Usually companies support many API versions simultaneously. They know their users need time to adapt to the new version. And some users will never adapt at all. They are forced to support the old API versions for many more years, even though there would be a better API available.

// ## Copilot

// Copilot is generally not to good with writing interfaces. Instead you should do this yourself and let copilot fill in the gaps. -> remove comment?

## Conclusion

Interfaces should always be designed from a user point of view. This makes them much better as user friendlines is the main goal of any interface.

APIs are extremely delicate. You have to get it right on the first attempt. You really have to reconsider every change you make several times. And don’t make any breaking changes unless it’s absolutely necessary.

Defining interfaces should generally not be done by Copilot. Rather this is a task that should be done by the programmer. Copilot is better with writing the implementation of a function or class, depending on the interface provided.

# 8. Functions

"Functions should do one thing. They should do it well. And they should do it only." - Robert C. Martin

// Further Reading: Clean Code, chapter 3, Robert C. Martin

Functions are, along with classes, the backbone of modern OO software. People just don’t care about functions too much as they are fairly simple to use and there are only very few things to take care off. Still, there is quite a lot to know about functions as well. We'll learn that functions have to follow the SRP and that they shouldn't have any side effects.

Throughout this book, we’ll distinguish between functions and methods as most authors do so. Even though I would personally like to call them both just functions as they are pretty much the same, just in a slightly different context. Most things I write about functions apply to methods as well as they are in many respects very similar. The class variables and the slightly different context are not a fundamental difference. Class variables are just about the same as mutable output arguments. Therefore, I generally won’t mention the differences between functions and methods.

## Do one thing only

Due to the single responsibility principle, functions may cover only one level of abstraction. Therefore, they should be very short (preferably less than ten lines) and have as few levels of indentation as possible. Having nested if/else, while or for loops would also violate the SRP. This reduces the amount of logic you can pack into a single function and makes it easy to name and understand. At the same time, it takes getting used to the formatting of such code. Almost all code is written at the first level of indentation.

Naming becomes comparably easy if you follow these rules. The function body is one level of abstraction lower than the function name. The name is a summary of what is going on inside the function. There should never be any unexpected behavior inside a function that could confuse the reader of the code. There should not be any hidden behavior inside a function.

```py
counter = 0
def log_in(email_address):
	counter +=1
	check(email_address)
```

This function clearly has a side effect. It says nothing about a hidden counter, thus this is hidden behavior that is not mentioned in the function name and thus should be avoided. Additionally, side effects may lead to temporal coupling as the order of calling functions with side effects matter.

Side effects also become a real problem when testing code. When calling the above function `log_in` twice, the value of `counter` will be different every time. This will make the tests very brittle because temporal coupling.

## Temporal coupling

Temporal coupling is if you can do things in the wrong order. Sometimes the code enforces the right order, sometimes it doesn't. Most notably, temporal order is not enforced by classes. Class methods can usually be called in any order. There is nothing enforcing the correct order. Let me make a brief example:

```Py
class Shopping():
	def get_money(self, amount):
		self.money = amount
	def create_shopping_list(self, shopping_list):
		self.shopping_list = shopping_list
	def go_shopping():
		# use the shopping_list and money
```
Apparently you have to get money and create a shopping list before you go shopping. The correct usage of this class is as follows:

```py
shopping = Shopping()
shopping.get_money(50)
shopping.create_shopping_list(["apple", "banana"])
shopping.go_shopping()
```

This sequence of function calls is given by the natural order of the shopping process. First you need money and a shopping lst, before you go shopping. However, this order is not enforced by the code. One could also swap two of the function calls as follows:

```py
shopping = Shopping()
shopping.get_money(50)
shopping.go_shopping()
shopping.create_shopping_list(["apple", "banana"])
```

Now you go shopping before creating a shopping list. In fact, the call of `create_shopping_list` is probably superfluous because the shopping list might not be used anymore. Instead you go shopping with a shopping list that is empty or not existant.

This is one of the drawbacks of OO code. Methods change the state of the object. Thus it is very hard to enforce that the methods get called in the correct order. 

It is one of the advantages of procedural code that such issues are less likely to occure. Code doesn't always have to be OO. Sometimes other paradigms yield better code.

```Py
money = get_money(50)
shopping_list = create_shopping_list(["apple", "banana"])
go_shopping(money, shopping_list)
```

In this case it is physically impossible to go shopping without having a shopping list.

```Py
money = get_money(50)
go_shopping(money, shopping_list)
shopping_list = create_shopping_list(["apple", "banana"])
```

After swaping the last two lines, this code cannot be executed anymore as the variable `shopping_list` is not initialized. When executing the code above you will get an error, `NameError: name 'shopping_list' is not defined`. This prevents you from calling the functions in the wrong order.

Long story short: make sure your functions never have side effects. Functions and methods should only have an effect on the class instance or, if necessary, to mutable arguments.

// how to make these steps work with copilot?

## Number of arguments
As for the length of the function, the number of arguments should be as small as possible as well. This simplifies the function a lot. 

Now there are very few functions with zero arguments. These are the easiest, they always behave the same way. There’s not much to test. The more function arguments a function has, the more functionality it can contain. Yet at the same time the more complex it will become.

Try to have at most 3 function arguments. This shouldn’t be a big burden. A plumber manages to carry all his stuff with only two hands, thanks to the invention of the tool box. Why shouldn't we be able to juggle everything within 3 arguments? We can use our equivalent to a toolbox: the dataclass (python) or struct (C++). If you don’t know how to pack all the variables you need into three struct objects, it’s time you reconsider the function design.

In classes the number of arguments issue becomes even worse. Methods can access additionally all the class variables. The equation is very simple,

`Total variables = function arguments + class variables`

Global variables should not be used, so we neglected those. Still, with having function arguments and class variables at the same time, it is very easy to exceed the recommended amount of 3 variables.

A method might access only a few of the class variables. However, one does not know until one has read all of the method and sub-methods involved. Furthermore, one has to check whether a method changes the class variables or not, except if it uses the C++ const expression. It is recommended to use methods with only one or maybe two arguments to keep the complexity as low as possible.

Following the SRP, functions can only be either a query or a command //https://en.wikipedia.org/wiki/Command%E2%80%93query_separation, but never both at the time. The code does not become more readable when violating this rule. In the best case you gain one line of code because you don't have to make an additional check. But at the same time you make the code more confusing as two responsibilities are much harder to deal with than only one. And potentially saving one line of code is not worth violating the SRP. A common anti pattern with that respect is returning a boolean flag on a set command.

```py
if set_node("money", 50):
	go_shopping(); 
```
Here the `set_node` function does two things at a time which certainly doesn't help with understanding the code.

### Copilot

// Is there a way so sort input variables into an array?

## Output arguments

A very vexing thing are functions altering the value of the input arguments. This is also a very common source for bugs as it is something quite unexpected. Now, once again, in C++ one can make this understood with the type of the argument. One can pass the argument by reference, which renders it modifiable. However, in other languages, this has to be clear from the context of the function.

Unexpected changes of values of a function argument are very hard to keep track of. For this reason, a function should always modify at most the first argument. Modifying two arguments violates the SRP and is even more confusing. I hope it is clear to you what kind of responsibility you have when writing functions that alter values of function arguments. If you change the value of an argument, it has to be the most important argument. It’s kind of an input and output argument at the same time. So, it has to be special.

Output arguments can be compared to class instance objects. They are essentially both function arguments that may change their values, just that the class instance is obviously a very special variable. The function acting on these variables may change the value of the output argument or the class instance and thus may have side effects. This is in either case sometimes required, but at the same time undesired behavior as it is hard to keep track of.

## Return values

Return values are in my opinion very normal, yet many OO programmers tend to dislike them. They work only with their class methods which only manipulate the existing class instance. In my opinion, return values have the very distinct advantage that their intention is clearer. It states: this is a new value. Compared to: This function may or may not change the first input value. Or, this method might change a variable of the class instance. And once again, keep in mind the SRP. A function may only have either a return value or an output argument but never both at the same time.

Return values are very central in functional programming. There you are not allowed to change existing objects. So you don't have the issue of output arguments changing their values. And the work around are return values. They have the advantage that it's obviously a new object with new properties. Each state the code is in, there is a different set of variables. You'll never have to track what state a variable is in because it is unique.

As a summary I’d like to emphasize that you should take care of the length of a function as well as the number of arguments. This is especially the case for methods and functions that change the value of an input argument.

## Copilot

Copilot is, just as with any piece of comparably simple code, fairly good at writing new functions from scratch. The following code needed only very little guidance. The usage of dependency injection with the `condition` argument was also a suggestion by Copilot.

```py
books = [
    {'title': 'The Alchemist', 'author': 'Paulo Coelho', 'price': 10.2},
    {'title': 'The Prophet', 'author': 'Kahlil Gibran', 'price': 12.3},
    {'title': 'The Little Prince', 'author': 'Antoine de Saint-Exupery', 'price': 8.5}
]

def print_books_where(condition):
    for book in books:
        if condition(book):
            print(book['title'], book['author'], book['price'])

def author_is(author):
    return lambda book: book['author'] == author

print_books_where(author_is('Paulo Coelho'))
```

# 9. Classes

"Q: What did the Java code say to the C code? A: You’ve got no class." - HampusMa on devrant.com

// Break up this chapter? It's quite long...

Classes are undoubtadly one of the backbones of modern code. Unless you are one of the few functional programmers, chances are high that you use them every day. Therefore, it is time we have an in depth discussion about them. 

This book is not about explaining what classes are exactly. This you have to learn else where. Instead this chapter is about how classes should be used. How one can distinguish different kind of classes, depending on the functions and variables they use. We'll try to understand when a function or variable should be public or private and I'll explain why I think plain getter and setter functions should generally be avoided.

## Data classes and structs


The C programming language was specified well before object-oriented programming was developed. It doesn’t support classes. But it has something very similar: structs. It is about the same as a dataclass in python. A struct is a user defined object that contains all kind of different variables. It is also possible to nest structs into each other. Structs are extremely useful as they allow us to store different data together inside a single object. It’s like a toolbox. In theory you may also store functions within a struct, though this is generally not done, at least not in C++. For storing functions, we have classes.

An example of a dataclass:
```py
import dataclasses

@dataclasses.dataclass
class Person:
    name: str
    age: int
    city: str

p = Person('John', 30, 'New York')
```

Nowadays structs or dataclasses are not that much used anymore. Especially the java community seems to avoid such kind of objects at all cost. Though there is absolutely nothing wrong about structs. In fact, structs are really helpful. Code without structs is like a plumber without a toolbox. It helps you sort your stuff.

Classes are pretty much the same as structs. Besides some technical details, the only real difference are the encapsulation of variables and functions and the introduction of inheritance. You can decide for each one of the variables or method to be public (accessible to the outside) or private (usable only within a class). This makes classes strictly more powerful than structs. 

But more powerful is not always better. A gun is more powerful than a knife, but at the same time it is also more dangerous. You can easily shoot yourself into the foot. So actually, it’s not the best idea to own a gun because the danger may be bigger than the advantages. With great power comes great responsibility!

## Private or Public

If you are not so used to working with classes, this may be very confusing. Why would you like to make anything private at all? Isn’t it easier to make everything public?

Indeed, this is a very important question. Even extremely important. Once you are able to create a class and decide right away which members should be private or public you are already a fairly good programmer. To make it short, it has to do with power once more. Never give the users more power than necessary.

Let’s figure out why there should be private variables and functions at all. We need something where you face only the surface of it and you only have very few ways to interact with it. It’s not hard to find an example. This description holds for almost everything around you. For example, your car. It is a highly complex object. It contains an engine, breaks and tons of other parts. You don’t even want to know. You only want it to drive. You need the speed bar, the brake pedal and the steering wheel. 

You have this absolutely massive object and you can essentially do only three things with it: increase the velocity, reduce the velocity and change the direction of the car. And miraculously that’s all you need. As long as your car is running you don’t care about anything else. I correct myself: you don’t want to know about anything else. Everything else works automatically. It’s like magic. You don’t want to tweak the fuel pump, change some engine settings or fiddle around with the steering wheel servo control. It works and it’s fine. You don’t want to deal with the internals of the car. You don’t even want to be able to take care of these parts. These are private parts of the car and are not to be touched by you. Only a mechanic should be able to maintain them.

There is one very simple rule of thumb which parts of a class should be public or private. If a class has no functions, it’s a struct and all variables should be public. Otherwise as few functions as possible should be public and all variables are private. But we’ll look at this rule in more detail in the next sections.

## Functions and Methods

Functions inside classes are also referred to as methods. Mostly by the Java people. Usually the notation of a function in this book is meant for both, free functions and methods. The difference between them is fairly small and it will be noticed if it really makes a difference. In C++ you can define functions and static methods in a way that you cannot even tell the difference when calling them. Static methods and free functions inside a namespace are indistinguishable in C++.

## Different kind of classes

// make some examples

I like to broadly categorize classes by the number of variables and the complexity of the functions they contain. Making sure that your classes are fitting into one of these categories is helpful for fulfilling the SRP.

### Data class

The data class has no member functions and therefore all variables are public. It has no functionality by itself but it’s great for storing data. As mentioned in the previous section, it’s like a tool box and the variables are tools in there. If a data class has too many (at most around eight) variables, split up the data class into sub-classes. This improves the general overview in the toolbox.

### Pure method classes

A class may have no member variables at all. It contains only of public methods. In java and C#, writing such kind of classes is required as every function has to be implemented within a class. In other programming languages however, there is not much need for pure method classes. In C++ and python you can define the corresponding functions free standing instead.

```py
class Math:
	def sin(angle):
		return 0

	def cos(angle):
		return 1
```

### Delegating class

The delegating class is a mixture of the struct and the function class. It contains private variables and public functions. Calls to one of these functions are all delegated to one of the member variables. It’s similar to a car. It consists of many comlex parts that each has its own functionality. Setting the temperature will just pass the corresponding command to the AC. Any other part of the car doesn’t have to know anything about the temperature or its control at all.

```py
class Car:
	def __init__(self, engine):
		self._engine = engine
		# ...
	
	def set_velocity(new_velocity):
		self._engine.set_velocity(new_velocity)

	def change_direction(direction):
		self._steering_servo.set_direction(direction)
	
	# ...
```

### Worker class

Worker classes are doing the hard work in your code and they are the most commonly used. Some people may say these are the only real classes. At least most of the design rules for classes apply only to worker classes. Worker classes have very few private variables, some rather complicated private methods and a few public methods. Worker classes are the only type of classes with private methods. Other classes don't have complicated methods to hide, other classes hide only variables. 

This means that worker classes are the only classes that do really complicated things that have to be hidden from the other programmers or users. At the same time, worker classes are extremely dangerous. You can easily hide too much complexity within a single worker class, such that no one will ever be able to understand it. You have to make absolutely sure that your worker classes are small and well tested. In fact, a worker class isn’t that different from a function where the function arguments correspond to the member variables. Therefore a worker class shouldn’t have more than 3 member variables and about 100 lines of code, depending on the general complexity of the class. Consider also using functions instead of a worker class. Functions have to explicitly pass around the variables which might make the code easier to understand and test.

As a general rule of thumb one can say that a worker class has become too complex if you struggle writing tests for it. This is a clear indication that it's time to break up the class into smaller pieces. For more details see the chapter on testing.

### Pure Abstract Base Class

The pure abstract base class has a different name in every programming language. In Java it's called an interface. This class type defines only the interface (shape) of a class. It doesn't contain an actual implementation. It contains only public method declarations and no variables. Variables are a hidden detail that should not be defined in an interface. One has to write classes that inherit from this abstract base class in order to implement it. In python and other dynamically typed languages you don’t need any interfaces, but it makes the code easier to understand. In C++ and Java, it is very important to use interfaces in order to break the code into pieces, to reduce compile time and allow run time polymorphism.

In python a class has to inherit from `ABC` in order to be an abstract base class. The methods are all `abstractmethod` and they don't have any implementation.

```py
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod 
    def feed(self):
        pass
```

An alternative to abstract base classes in Python are protocols. // Differences protocols <-> ABC?

### Implementation class

This class inherits from a pure abstract base class and implements it. As the base class, it contains only public functions but no variables. Therefore the complexity of interface implementation classes is very low.

```py
class Sheep(Animal):
    def feed(self):
        print("Feeding a sheep with grass.") 
```

### Inheritance classes

Inheritance classes are usually delegating classes. They can be worker classes as well, though this is not recommnded due to the complexity of the resulting class. However, as I mentioned before, I generally do not recommend using inheritance, except for defining interfaces. Anything you want to do using inheritance can be done using composition as well. And keeping your fingers off inheritance will possibly save you quite some trouble. I read many books and there are many refactoring techniques and similar that work perfectly well, except for inheritance. The main problem is usually overriding base class functions that can cause all kind of issues. Furthermore, you don’t really gain anything by using inheritance.

Here is one of the issues of using inheritance.

```py
class Animal():
    def feed(self):
        print("Feeding meat.")

class Sheep(Animal):
    def feed(self):
        print("Feeding grass.") 
```

Writing such code at first seems attractive. You don't have to redefine the `feed` function for animals eating meat. It's already there. But saving lines of code is no merit for code quality. Stability is. And this code here is not stable. It is brittle. A single typo can create a hard-to-track bug. Let's assume you define a method `fed` inside `Sheep` instead of `feed`. Then the sheep will most likely be fed with meat. 

In the case above using an abstract base class, this kind of bug is not possible. The code is much more stable. The following code return an error message before executing it because `Lion` does not implement the `feed` function.

```py
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod 
    def feed(self):
        pass

class Lion(Animal):
    def fed(self):
        print("Feeding meat.")

if __name__ == "__main__":
    lion = Lion()
    lion.feed()
```

This error prevents you from creating a bug that might be very hard to track down and cost you a lot of time. Instead you immediately get a message that you there is something wrong with your code.

### General recommendations

It is recommended sticking to the class types mentioned above. It may be convenient to add a method to a data class or a variable to a pure function class. However this will quite certainly make the code worse as it violates the single responsibility principle.

The most common error is mixing the worker class and the delegating class. You can easily end up with a fairly complex function within a delegation class using a lot of member variables. This is bad by design as the delegation class is fairly high level of abstraction, meanwhile the worker class is by design a low-level object. Mixing different levels of abstraction is a really bad thing to do. Refactor the complex part into a separate class or function and call it from the delegating class. This should do the job.

## Constant Class instances

// move const part of the description elsewhere?

In C++ you can enforce an object to remain the same for as long as it exists, using the const keyword at the time of creation. In Python you cannot enforce it, you can only use the all uppercase notation to hint that a variable should not be changed. The usage of const is easy, even though it might be a little confusing at the beginning. Everything that should never be changed should be made constant and can be defined so at the time of creation. You create an object and it will remain the same until you throw it away. This makes life of a programmer much easier and prevents abuse of variables. This has once again to do with power. Life becomes easier if you don't have the power to change an object that should not be changed. It prevents you from making a mistake by changing the object.

But things are not always that easy. You might have cases where all properties are const except one. Or is it? Let’s look at an example. 

We have a bottle. It has a color, size and material. They are all fixed when the bottle is created. In our code that would be the constructor. These properties can never ever be changed. You could only replace the bottle with a different one. An instance of the bottle class should be made constant.

```py
from dataclasses import dataclass

@dataclass
class Bottle:
	color: str
	size: float
	material: str

if __name__ == "__main__":
	BOTTLE = Bottle()
```

Note that color and material should probably not be a string, but rather a `Color` or `Material` enumeration, respectively. We just use strings here for the sake of simplicity.

### Mixing const and non-const objects

So far so good. We created a bottle that is contsant. But having an empty bottle is fairly useless. You want to use it. You fill water into the bottle and drink it later on. This is a really simple example but, in our code, it leads to very fundamental questions. We have a constant bottle with a not constant amount of water in it. How are we solving this problem?

The first attempt is removing the constness and adding the amount of water to the class variables. This is a dreadful idea. Now anyone could change the color of the bottle. Do never remove a const'nes from an object that is constant.

We make all variables private and write getters for them. The amount of water can be changed with the functions fill and release. This is better, yet somehow it still feels wrong. I have a grudge against getter and setter functions as explained further below.

A completely different idea is keeping the amount of water separate from the bottle. We create a new class `WaterBottle` that contains a constant `Bottle` and a variable amount of `Water`. This also prevents the `bottle` class from getting any bigger and it keeps some structure in the code.

```py
from dataclasses import dataclass

@dataclass
class WaterBottle:
	BOTTLE: Bottle
	amount_of_water: float

@dataclass
class Bottle:
	color: str
	size: float
	material: str
```

This is just one example how one can deal with const objects. One always has to consider whether an object or only parts of it should be constant. Such considerations are important as const'nes is an important property of variables. You shouldn't consider const'nes as restricting you, but rather that it fixes some behavior.

## Free Function vs. Method

// This text here is redundant (where? output arguments?), tough I quite like it. What to do…?

There are two ways to change the value of an object by a function. Either pass a mutable object as an output argument or the object is a class instance and the function a method acting on it. The two cases look like this:

```py
a.b() vs. b(a)
```

In both cases, this might change the value of a. However, there are some differences. `b(a)` can access only the public variables and functions of a. If a has a public variable c, then we can write `b(a.c)`, which makes even more clear what part of a is to be changed. While in `a.b()` there is no way telling which variables in `a` are going to be changed by `b`. You can only hope the author did well obey the SRP and give `b()` a more meaningful name that allows to understand easily which variables of a are going to be changed. Or `a` has to be a struct, such that the method is called by `a.c.b()`. 

From the code point of view, both functions do roughly the same and there is no clear advantage for one or the other. However the class method call, `a.b()` is frequently more readable than `b(a)` as we'll see in a second. Simply because of the way our natural language is structured.

It happens you write a function that uses one or more public methods of a class. Apparently, your new function is related to the class, but at the same time you could also write it as an independent function. Now what should you do?

Generally, it’s better to define it as a free function. It keeps the class smaller and less complex. The price of the function is lower if it’s outside the class. But as always there might be a tradeoff. For example, you have a class behaving like a list and you want to implement a function `contains`. It returns true if the list contains the function argument and false otherwise. You are tempted to implement it as a member function. But you can easily implement it as a free function as well. This would generally be preferred. We have the following two options:

```Py
# Free function:
if contains(names, “Donald”):
   print(“Make America great again”)
# Or method:
if names.contains(“Barak”):
   print(“Yes we can”)
```

In this case I certainly prefer the second option from the readability point of view. It’s so much clearer. It reads like an English sentence. From code point of view, I prefer the first option using the free function. This is one of the cases where the principles explained in this book will not give you a definite answer how to deal with this problem. It can only give you some arguments for one solution or the other. You’ll eventually have to make a judgment call by yourself. If you find some good arguments for and against both solutions, you are a good programmer. Once you manage to make the right decision, you are a great programmer.

In software engineering there are always so many things to consider. This was just another example. Probably there are more arguments for one or the other solution that I missed. They might make the whole discussion obsolete. Let me know if you found such a solution, I’d be curious.


## Constructors

// need examples, etc.

Constructors are very special methods. The constructor is called once every time an object is created. This has severe consequences that many software developers are not aware of. Most notably, writing tests can become nearly impossible if the constructor contains too much logic or has side effects. The author of some code might have assumed that there will be only one class instance and planned accordingly. This might be true in his particular part of the code he wrote. However, his assumption might break down when writing unit tests. There you have to be able to create many objects without any interactions between them, otherwise your tests become very fragile.

Thus, make sure the usage of a constructor is always fool proof. A constructor should be as simple as possible. Everything a constructor does, for example allocating memory or opening a file, has to be undone by the destructor. This constructor/destructor pair is the only way to guarantee that all effects of the constructor are undone. This also means that you shouldn't define a counter in the constructor.

The following code creates a counter for the class instances. It looks neat. However, it will be barely possible to test this counter. Every time you add an additional test case, the counter values will change. And once you change the order in which the tests are executed, your tests will break.

```py
from itertools import count

class Obj(object):
	_ids = count(0)

	def __init__(self):
		self.id = next(self._ids)
```

You will witness what I said here once you write a complicated constructor and try to write unit tests for it.

## Getter and setter functions

In Java, it is common practice to define a class and make all its variables private. The developer clicks a button in the IDE and public getter and setter methods are automatically generated. For each private variable, it creates a setter and getter methods to access and change it. This is extremely wide spread and in my opinion a very bad habit.

Here we distinguish here between two relevant types of classes. 

### Data classes

In data classes all variables are public. Everyone can work with the variables directly. There is no need for setter or getter functions. The Java people claim that this was bad because you had to decouple everything. They were decoupling the implementation of the class (the variable) from the interface (the getter and setter). Well, yes, they do decouple them. But they might have never really thought about the outcome. They decouple in a strictly worse manner than just giving raw access to the class variables.

Let me make an example. We have again the class bottle:
```Py
class Bottle
   def get_size(self):
       return self._size
   def set_size(self, size):
       self._size = size
```

This time it has getter and setter functions for the size. This is perfectly viable code. But this fails due to the real-world restrictions. You cannot change the size of a bottle. Once a bottle is created in the factory the size is fixed. And it can never be changed again. This is equivalent to setting the size in the constructor. There cannot be any `set_size` function to change the size of an existing bottle. Never. It is physically impossible. Vice versa there is no need to create a bottle if you don’t know it’s size. This doesn't make sense. Once the bottle is created by its constructor, it immediately becomes a constant object where no variables may, or can, be changed anymore. There is no more need for a getter function. Just access the class variable directly. You can’t make any mistakes now.

```Py
class Bottle
	def __init__(self, size):
		self.SIZE = size

BOTTLE = Bottle()
print(BOTTLE.SIZE)
```

Another point of using getters and setters was decoupling. You want to rename `size` into `volume`. It’s easy to do, there are only 3 places where size is used. Replace them with `volume` and you’re done.

```Py
class Bottle
    def get_size(self):
		return self.volume
    def set_size(self, size):
		self.volume = size
```

See the problem? You didn’t improve anything at all. Everyone still uses the get_size function which returns a volume. This will cause a hell lot of confusion. You would have to rename the getter and setter function as well. It decoupled the code only in theory. Writing getters and setters is only useful if the value returned by the getter is the result of a calculation, lifting the code on a higher level of abstraction. But then it’s not a pure getter function anymore...

Having accessor methods to class variables only makes sense if it lifts the code to a higher level of abstraction. Then you really gain something. And it is really a form of decoupling. But this is not possible in data classes as there is no abstraction around that could be decoupled.

### Worker classes

The other case are mostly the "normal" worker classes. It is very well possible to have getter and setter functions here. But if they refer directly to a variable within the same class it is a hint that your class design may be bad. Access functions should shift you to a higher level of abstraction while the plain getter and setter functions here do nothing with that respect. Instead they have to access or change data that is located in a nested data structure. They just make it more convenient to get there.

But again, the member variables of a worker class should be private because they should not be accessed from the outside. They should neither be accessed through raw setter or getter functions. Member variables in a worker class should be hidden deep inside the class and used only by the methods of the corresponding class. These variables can be considered as intermediate results of internal calculations. They are not intended to be public. Neither directly, nor via accessor methods. Thus there is no reason to write getter or setter methods in worker classes.

### Delegating classes

The only class type that has something similar to plain getter and setter methods are the delegating classes. But also here, you should not write them. Getters and setters already contradict the name of these classes. Getters and setters are accessor functions and not delegators. Accessors don't increase the level of abstraction meanwhile this is exactly the idea of a delegating class.

One example of a delegating class is a car. You can change the temperature, possibly by calling a `set` function. But this is no fundamental property that had been set in the production line of the car. It’s just an environment parameter that is controlled by the air conditioning and a temperature sensor.

```Py
class Car:
	# contains an object air_conditioning
	def set_temperature(temperature):
		self.air_conditioning.set_temperature(temperature)
```

The car class is only delegating the `set_temperature` function call to the `air_conditioning`. And also, the `air_conditioning` does not have a temperature variable. It has only a temperature sensor that measures the temperature along with its possibility to change the temperature.

This might be only one example, but there aren’t any other variables in the car where you can use a get or set call directly. It doesn’t improve the code if you write a `get_air_conditioing` function.

I hope I managed to convince you not to write bare getter and setter functions to member variables. Especially not to all of them.

### Other points of consideration

One of the few advantages a getter and setter function have compared to dealing with a raw member variable is tracking the value and access points of the variable. While this can easily be done in the debugger with getter and setter functions, it is almost impossible to do something similar for a plain variable. On the other hand, using a debugger is a strong sign that the code is bad and not covered well with unit tests. 

Generally I don't regard this reason as sufficient to write setter and getter functions. As I hope I don’t have to get to use a debugger at all, I omit writing getters and setters in structs and work with the plain variable.

## Lose and strong coupling


### Coupling and Cohesion

A well-known rule says: "Classes should have high cohesion within themselves and low coupling between each other." (Robert C. Martin) If you don’t understand these expressions, we could rewrite it to: “There should be a lot of interaction between methods and variables within a class and little interaction between classes.” This is indeed a very important rule. However, as most rules in software engineering, it has to be taken with a grain of salt.

The amount of cohesion within a class may differ a lot, depending on the type of class. The cohesion within a worker class is certainly much higher than within a data class. In a worker class, there is a significant amount of work required to change its structure. In a data class, there is barely any cohesion between the member variables. Also the delegating classes have fairly little cohesion. Yet there is nothing wrong about these types of classes. In fact, they are very useful to structure your objects, etc.

### Worker classes

The rule above defined by Robert C. Martin was meant for the worker classes. Worker classes are a very common source for bad code as they tend to become way too complex. When breaking them into smaller pieces, this rule is very useful. It gives you a hint how to break them into pieces preferably. Cluster your methods and variables into small groups. There should be a lot of interaction within the groups and little interaction between the groups. Possibly you also have to rewrite a few methods before breaking the class into pieces. It will be worth the effort. If you manage to do this, it will certainly make your code easier to understand. And you have become a much better software engineer.

// create such a plot. There is a similar one in one of the books, but I don't remember where.

// see fundamentals of software architecture p. 43, LCOM metric.

Unfortunately it is very difficult to make an example here of such a complicated class. Thus I can only explain here in rough terms how you could break such a complicated class into pieces.

Classes have low coupling if the number of interaction points between different classes is comparably low. Ideally, every class does its work and then hands it over to the next one, like in a rally race. The interface of every class would consist of only one function. High coupling on the other hand is like two classes playing ping-pong. The classes all have a big interface containing many functions and which call each other several times in a specific order. This quickly becomes terribly complex. The absolutely worst case is two classes calling each other recursively. I could hardly imagine any worse code than that! This is about the strongest coupling there is. Neither of the two classes can be changed without changing the other one as well. Such code is solid as a rock.

I hope from this description you already understand that strong coupling makes the code very difficult to understand. Additionally, it also makes it brittle, which isn’t any better. It becomes increasingly hard to make any changes. Implementing new features will take a long time and fixing bugs is hard because it is not clear what each class is supposed to do exactly. Having strongly coupled code can become a nightmare.

There always has to be some amount of coupling. Code cannot exist without it. But the amount of coupling between classes should be kept as low as possible. Additionally there are techniques to decouple your code. Writing an adapter between two classes for instance can give you more flexibility.

### Other class types

Maybe you realized by now why this rule about high cohesion does not apply to all kind of classes. A pure data class has no cohesion at all. It takes no effort at all to split a data class. You may split it however you like. A delegating class has very little cohesion. Yet these classes are extremely valuable as they allow you to structure your code. This rule about cohesion mostly applies to worker classes, meanwhile data classes are a lose bunch of variables without any cohesion. They are grouped together solely because it makes the code easier to understand and deal with.

### Inheritance

Coupling is one of the reasons why I recommend not to use inheritance. Inheritance is among the strongest coupling we have available in software development. The derived class inherits all the implementations of the base class functions. Vice versa, the behavior of the base class functions may change if some function calls get overridden by the derived class. Inheritance obfuscates the code and getting rid of inheritance at a later point can be almost impossible.

## Static expression

Static methods are another thing that I discourage using. It’s not super bad, yet it’s another of these misguided object-oriented things. Isn’t it strange: you write a class with all kind of member variables, then there is one static method that doesn’t need any of these variables but it is still within the class? Didn’t we say, we wanted to keep classes as small? It should have high cohesion? A static method has about as little cohesion as the variable in a data class. Zero.

I fully understand that there are programming languages where functions have to remain within a class and static functions are the only way to write “free” functions. But in all other languages I recommend not to use static methods as it doesn’t add any additional functionality nor does it improve the code. In C++ you can mimic a static function using a namespace. The resulting function call will be undistinguishable. At the same time you can split up a namespace over many files, as done for the `std::` namespace.

As we are talking about static, we can also discuss static variables as used for instance in C++. Static variables are similar to singletons and you’ll have a hard time testing classes containing static variables. Do not use singletons and do not use static variables. As soon as you start writing unit tests for static variables you'll see why I discourage using static variables.

## Drawbacks of classes

Classes are very often abused for writing bad code without the programmers realizing it. They just think it would be normal. The most common problem is that classes become too big. It’s just too convenient to write everything inside a single class. You have all the member variables around and it’s so easy to work this way. In some cases, I had the feeling that the authors of some code wanted to write all code inside a single class. This is extremely problematic. If a single class covers the whole code, then the member variables become ... global variables! The whole code becomes a big ball of mud. // https://de.wikipedia.org/wiki/Big_Ball_of_Mud

But also for slightly smaller classes, member variables are an issue. If a global variable is like placing a bag on a public square, a class variable is like a bag in the entrance of a huge building. Here you have some ways to protect the bag, like installing surveillance cameras. But it’s still a dangerous game to play. Be careful with class variables. Or even worse, inherited variables. Keep your classes small in order to limit the scope of your class variables.

If you write a class where all function implementations consist of a single line (delegating class) or you have no functions at all (data class), the number of class variables is not too critical. If you have more than about 6 to 8 member variables you should consider sorting them in sub classes. However, as soon as you have to write complex functions you have to be extremely careful as things might get out of hand otherwise. The combination of complex functions and many member variables lets the complexity skyrocket. Keep the number of variables at one or two when dealing with complex functions, as recommended in the section on worker classes. Or even better, replace the class with a few functions if you find a reasonable way to get rid of all member variables.

It’s a good rule of thumb to say that the class design is probably ok as long as writing unit tests works out fine. And you don’t feel the urge to test private functions because class implementation is too complex. Make classes as small as possible, yet still convenient to work with.

## Example
// TODO, I don’t know yet exactly if/how to write this example. What is exactly my point?

I would like to discuss an example. Many people completely misunderstand what belongs into a class. 

// I think this belongs elsewhere: Once again, I’d like to mention the rules of software engineering. We write code that generates values for our customers and we write code that is easy to understand. We don’t write code that mimics the whole world. It’s more like a cartoon. It’s minimalistic.

// Apple pie example? Or do we have another example? And is it about what we need or what belongs into a class or outside?

Let’s take the example of an apple pie. It has a lot of different properties and I’d like to show you how to deal with some of them.

Here is a list of properties the pie has: Sweetness, weight, price, baking grade, ingredients

Now some of these properties are really the properties of a single pie. The baking_grade for example. One pie may be burned while another one is baked perfectly. Other properties are more about apple pies in general. The price is something the sales department of the bakery cares about, while the ingredients are used by the bakers. These are not intrinsic properties of the pie and can be stored elsewhere. For example, in a dict. We could also define a variable apple_pie_price, but storing all prices in a single data structure is way more convenient. The only drawback is that the apple_pie object needs to have a variable `name="apple_pie"`. A small price to pay.

// what do I want to say with this code here?

```Py
class Sweetness(Enum):
	too_sweet = auto()
	just_fine = auto()

class BakingGrade(Enum):
	burned = auto()
	well_done = auto()

def bake_apple_pie(ingredients, baking_temperature):
	weight = sum([ingredient.weight for ingredient in ingredients])
	if ingredients["sugar"] / weight > 0.2:
		sweetness = Sweetness.too_sweet
	else:
		sweetness = Sweetness.just_fine
	name = "apple_pie"
	if baking_temperature > 220.:
		baking_grade = BakingGrade.burned
		name = "burned_apple_pie"
	else:
		baking_grade = BakingGrade.well_done
	return ApplePie(weight, sweetness, baking_grade, name)

@dataclass
class ApplePie:
	weight: float
	sweetness: Sweetness
	baking_grade: BakingGrade
	name: str

prices = {"apple_pie": 25, "burned_apple_pie": 15} 
ingredients = {"apple_pie" : {"apple": 0.3, "flour": 0.3, "eggs": 0.1, "sugar": 0.1}}

burned_apple_pie = bake_apple_pie(ingredients=ingredients["apple_pie"], baking_temperature=225.)
```

Now the code can be used as follows:
```py
ordered_dish = "apple_pie"
ingredients = get_ingredients(ingredients[ordered_dish])
dish = 
```

## Conclusions

I think we can agree on the fact that OO programming is important and everyone should know about it. It has advantages, but at the same time classes are a very common source for bad code. Classes have a tendency of growing and becoming a big ball of mud. Many people simply don't know that this is an issue. As a rule of thumb we can say that your class design is fine as long as wirting tests is not an issue.

Follow the rule “use composition, not inheritance” and don’t use friend classes and other curious OO constructs if these exist in your programming language. Inheritance introduces very strong coupling which should be avoided at all cost.

Many guidelines on how to write classes are defined for worker classes. For example the rule that classes should have high cohesion. It seems like most people overlooked the other kind of classes. A data class has no cohesion at all but it a perfectly viable object.

Prefer free functions over methods. It improves clarity which variables may be changed. Though sometimes methods may make the code more intuitive to read and are thus prefered.

## Copilot

Just as with functions, Copilot can write classes from scratch as well. Here I wrote only the first half of the first line of the comments, the rest is a suggestion by copilot.

```py
# wirte a class Person with attributes name and age
# and a method get_name that returns the name
# and a method get_age that returns the age
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
```
The code is, though very simple, correct. It only misses the pythonic notation with the leading underscore to make `name` and `age` private. However, I generally don't like the code here as I explained in the section on getters and setters. Instead of this class here, we could also write a dataclass.

Generally it's better to start writing some code that you want instead of writing comments.  Here I started writing `class` as I was not satisfied with the suggestion. The result is a suggestion for a class without getter and setters.


## Exercises

The following class is too big. Refactor it such that you get several smaller classes.

This class is a mixture of a delegating class and a worker class. Convert it into a delegating class by moving the complex code into a dedicated function. 
// create such a class

# Inheritance

"Favor composition over inheritance" - Basic rule of class design

Or my version of this rule: "Use composition, not inheritance"

Inheritance is considered to be one of the integral parts of OO programming and certainly one of the most widely used. Inheritance is often said to be an “is a” relationship. A sheep is an animal. Therefore, the sheep class has to inherit from the animal class. But as always, there is more to it.

## Drawbacks of Inheritance

Inheritance comes along with quite some issues and should thus be avoided if possible. Modern languages like Go and Rust don't even support inheritance anymore.

### Tight Coupling

The most obvious problem here is that we may create very long inheritance chains. I once read an article about some code having 10 levels of inheritance. It turned out to be absolutely disastrous. There is barely any stronger coupling between code than in inheritance. It was impossible to apply any changes or to remove all the inheritance. This inheritance structure was like a tree whose roots were entangling all the code around it. The code lost all his fluffiness and became solid as a rock. 

One of the main problems here is that all inheritance levels have access to the base level variables. The variables and methods are not sorted. They are just there. Meanwhile with composition, you only have to consider the variables inside the class. This makes it much clearer where a variable comes from and probably prevents you from accessing objects several layers deep in the hierarchy, unless you really want to do so. Therefore one can say that composition properly implements encapsulation while inheritance doesn't.

Furthermore, I regard the common usage of inheritance as an old dogma. It is your job to write code that’s easy to understand. Don’t let yourself get bothered by someone saying that a sheep is an animal and you should therefore use inheritance. It will quite certainly not improve the code and you can end the discussion. You are probably developing a model of a sheep that doesn’t need to know about animals. You have to be pragmatic. If a sheep doesn't have to know about the Animal class, then there is no reason why it should inherit from it.

### Error prone

There are several other issues with inheritance. This is already clear due to the fact that Michael Feathers wrote in his book Working Effectively with Legacy Code several examples that he wanted to refactor. In about half of them there were problems with inherited or global variables or overridden methods. It’s just so easy to create bugs with inheritance. One misspelled function will not override the base class function and thus creating a bug. You can delete a derived class function and the code still compiles due to the base class function. Meanwhile without inheritance you would get a compiler error.

Though it has to be said, that with the `override` keyword or attribute, this problem has been resolved in some programming languages as C++ and Java. Still, I would recommend not to use inheritance and always use `override` in case you do have to use inheritance to prevent nasty bugs.

### Obscure code

Additionally, there is the problem with variables inherited from the base class. These are almost as bad as global variables. One doesn’t know where they come from. Imagine a variable you get from 10 levels of inheritance. And there are dozens of methods that can alter them. This is absolutely terrifying. For this reason it is generally not recommended to nest inheritance. And honestly, I don't see at all, why inheritance should be used, other than for defining interfaces. Code reuse can be better implemented using composition or functions.

### Implementation

The implementation of inheritance can be complex task, depending on the programming language. There are many things that the compilers in the early days were not able to deal with. The danger was very high that a programmer created very subtle bugs. Even today it is still difficult to use inheritance correctly in some programming languages. Implementing inheritance in C++ requires quite some knowledge and care to prevent bugs. It is fragile. Avoid fragile code. If you follow my advice not to use inheritance you won’t have to bother with such technicalities.

// add a plot of the diamond problem below

When using multiple inheritance, there is the additional diamond problem. Let's say, we have a base class `A`. `B` and `C` inherit from `A`. So far so good. Now there is the class `D` inheriting from `B` and `C`. Classes `A`, `B` and `C` all have a function `f` implemented. Which function `f` should `D` use?

This leads to all kind of nasty ambiguities which functions should be used. For this reason, some languagues like Java don't support multiple inheritance. And while I regard single inheritance as a bad practice, multiple inheritance should certainly be avoided.

### Overriden baseclass functions

Inheritance is difficult to implement properly. Especially when dealing with constructors and overridden functions, there is quite something you have to know about v-tables and other technicalities. Chances for creating errors are significant. This can be avoided by not using inheritance. Inheritacne is simply too error prone. Though this is better in python than in C++.

Sometimes inheritance can be extremely confusing. Let's take the following example:

```py
class Animal(): 
    def feed(self):
        print(f"eating {self.get_food()}")

    def get_food(self):
        return "grass"

class Lion(Animal):
    def get_food(self):
        return "meat"

if __name__ == "__main__":
    lion = Lion()
    lion.feed()
```

Is the lion now eating grass or meat? Of course it's eating meat. But using overriden functions in the base class can quickly become confusing. This is the simplest version of the Yo-yo problem where the programmer has switch between reading code of the base class and the derived class in oder to understand the code. The derived class not only depends on the base class, it's also the other way around. We break the encapsulation of the base class and introduce a mutual dependency. This is so confusing, it is dreadful. Please don't write such code.

Of course, this can be avoided using the final keyword in some programming languages. But it is just another example, why in my opinion inheritance should be avoided. As I said, there is just too much that can go wrong with inheritance.

In inheritance, the derived class inherits all the functions from the base class. This might be more than what is actually required. The interface of the derived class is bigger than it has to be. This is bad as it violates the Interface Segregation Principle, see chapter on SOLID principles. Having to write tests for unused functions in the interface is only one of the problems.

## Advantages of Inheritance

There are quite few advantages and none of them justify using inheritance.

### Code reuse

The biggest advantage of inheritance is certainly code reuse. You may define a function in a base class and reues it in several derived classes. This saves you from repeating yourself. 

On the other hand, you can usually also use composition or write functions with the corresponding functionality and reuse them. In most cases this works out just fine as well.

## Interfaces

In C++, you have to use inheritance for defining interfaces. There’s no way around it. It's an old language. Just make sure the base class is purely abstract, use smart pointers and don’t use inheritance anywhere else. This way you should be save. When I write that you shouldn’t use inheritance, this is the one and only exception.

## Conclusions

You don’t gain much by using inheritance. Using composition is in most cases a perfectly viable alternative. If your code looks messy as you start using composition instead of inheritance you probably wrote messy code all along. You just didn’t see it because the inheritance was hiding it. Which is another bad thing.

There are also some more esoteric things, for example friend classes. At first sight, friend classes look like a good idea as it makes writing code easier. However, on the long term this has similar issues as making private variables public. In most cases it results in bad code that is not properly encapsulated. Just ignore friend classes and similar things and never look back. There are very few cases where friend classes are really useful. // cite https://google.github.io/styleguide/cppguide.html#Friends . Write your code in the most common way possible and only consider something else if it really improves your code.


# 10. Testing

// if you don't use tdd: insert errors into the production code to test the tests. https://github.com/97-things/97-things-every-programmer-should-know/tree/master/en/thing_95

Software Engineering:

"Data structures + algorithms = software" Adapted from Bertrand Mayer

Abstractions + testing = engineering

It may sound surprising to you, but proper testing is an absolutely essential step towards writing better code. It forces you to write better code. In fact, this was the first chapter that I wrote for this book.

In this chapter, we learn why tests are so important, how to write them and what to look out for when writing tests.

## A short story about tests

In the early days of software engineering, people wrote code and packaged it into the software they were selling. Before the release, the whole company had to drop all its work for 2 weeks and manually check that all the features were implemented correctly. The software developers had to spend night shifts to fix the bugs ASAP because otherwise the release of the software would be delayed.

But that's not the end of it. Of course, the company wants to make more money. They add some small features to this huge software and sell it again. But here comes the problem: before they can release the software and make a lot of money, they have to do the quality assurance all over again. And all the code that was changed since the last check has to be tested. ALL the code has to be tested because developers changed also code used by old features. Once again, the whole company freezes for 2 weeks.

Obviously, this is highly frustrating. Every release, you have to test a feature that didn't change at all, yet the team could have introduced some bugs. Every release you waste 2 weeks of your time to do the same boring repetitive task. Every release, the company spends millions to test things that were already tested several times before. And even worse. As the software grows, the number of bugs increases. Some of them even slip through the expensive testing. And the release gets delayed as the bugs become harder and harder to fix. It's a nightmare.

After another terrible release, the company is at the verge of collapsing. The CEO comes to the development team. His tie is hanging lose and he looks really tired. Apparently, it's been days since he slept for the last time. And he says “Guys, it cannot go on like this. These tests are killing us. We need the following: Here is a screen. At any time during the development I want here a list with all the features that are currently not working according to specification. If everything works, it should be green. If you make this work, I’ll pay you one Billion.”

Silence in the room. One Billion??? You may laugh. But there are more than enough companies that would actually pay this amount. It’s an enormous amount, but at the same time the efforts required are incredible. There are millions of lines of code and tens of thousands of features. It’s hard to find anyone in the company who knows what the specifications are. It will take years to get these automated tests working and maybe the company will be bankrupt before you finish.

On the other hand, the benefits for the company would be worth this amount. At first you might think “ah, spend one billion for saving 2 weeks of testing??”. But there is so much more to it.

1.	You can release anytime the screen is green. If the team works well, you can release every day (“nightly build”)
1.	If a customer needs a feature urgently, you can quickly implement it and send him the nightly build.
1.	There are less bugs as automated tests are more reliable than manual testing.

And that’s only the marketing side of it. At least as important is the developers’ side of this screen. So far you were always afraid that you would break some feature when changing code. A feature was working so far but all of a sudden, it’s broken. Nobody realized when it happened. You’ll spend the rest of your work life in constant fear. This is worse than the zombie apocalypse. There is nothing that can make you feel save again. You are never going to touch a single line of code again unless you really have to, as you are afraid of breaking something.

But now, all of a sudden... magic! You know if you accidentally broke a feature. The screen tells you everything is alright! Your paranoia starts to fade. You gain confidence again in your code. In your abilities. In yourself! You can start replacing all this old ugly code that had been sewn together like a Frankenstein monster. Things that were welded together by force because the author didn’t dare to rewrite the existing code to make a clean solution possible. Suddenly things look fine again.

You go to your CEO, give him a hug and a box of chocolate. You thank him for saving your career and you pay him back the billion.

I must admit that at times I exaggerated a little to make a point. But the exaggeration is smaller than you think. The importance of writing automated tests cannot be overestimated. They are no guarantees to make your software project a success. But I can tell you that projects without automated tests are doomed and will fail sooner rather than later.

I hope this is enough motivation to make you read through this chapter and really try to write tests by yourself. As always, it’s not easy at the beginning. Ask the internet and others for advice and you’ll get a fairly good idea how to write them.

## Test examples

Here is a small real-world example how a test works. 

1.	Make sure the coffee machine is clean, has coffee, water and electricity.
Press the coffee button.
Wait until the coffee has finished.
1.	Taste the coffee. If you like it, the test passes. Otherwise it fails.
1.	Throw away the cup and the remaining coffee.

This is it. Tests always consist of a few instructions that should be easy to understand. The result of the test can take up only two values. It passed (you like the coffee) or it failed (you didn’t like it). If it failed, you should call the technician to fix it. Or you write a script that calls the technician automatically.

Tests consist of three stages that are run on a test bench.

1.	Setup: make everything ready for the test
1.	Execution: check the requirements are fulfilled
1.	Tear-down: clean up everything used for the test

Structure of a Software test

In software we do the same. In every programming language, there is one major testing library. They all do pretty much the same. The python testing library is called pytest.

```Python
# inside vector.py
class Vector:
	def __init__(self,x,y):
		self.x = x
		self.y = y
	def distance_to(self, other):
		return ((self.x-other.x)**2)**0.5

# inside test_vector.py
from vector import *
import math

def test_distance(self):
	v1 = Vector(0,0)
	v2 = Vector(1,1)
	assert math.isclose(v1.distance_to(v2), 1.4142, rel_tol=1e-3)
```

We can run the test in the command line with
```sh
pytest
```

The output is this:
```sh
E    assert False
E     +  where False = <built-in function isclose>(1.0, 1.4142, rel_tol=0.001)
```

Apparently I made a mistake in the implementation. The correct implementation of the `distance to` function would be

```py
	def distance_to(self, other):
		return ((self.x-other.x)**2 + (self.y-other.y)**2)**0.5
```

Now the test passes.

As you can see it’s pretty simple to write a test. Not only in python. There are testing libraries for all major prorgramming languages. And from the testing library point of view you won’t have to learn much more than what I explained here for quite a while.

Once again, the difficulty lies not in the usability of the testing framework. The much harder questions are what, when and how you should test. Let’s have a look at the code and try to understand.

### When, what and how
// rename this section. The title is redundant with another section

Our class vector contains the member function `distance_to`. It is part of the interface of the class and therefore has to be tested. This is the price you pay for public functions. Or rather: It’s a small fraction of the price you pay for having public functions. Keep functions private if possible. Private functions give you much more degrees of freedom as you are allowed to change them at will. For pubilc functions you have to stick to the behavior that you guaranteed by the interface. Avoid changing existing interfaces, it's a lot of work.

Inside the test_vector.py file we write the test case. Before you miss it, I’d like the emphasize the very first line. We want to test the `Vector` class. We have to import the corresponding file.

Next, we define the test case. Every test case gets a name. This name will show up in the test report if this test fails. It is good practice to give the test case a name which explains fairly well what it tests. These names may be up to one line long if needed. You don’t use these names anywhere else so it doesn’t hurt having very long test names.

Inside the test we start with the setup part. In order to test the distance_to function we need two vector objects `v1` and `v2`. In the next line we calculate the distance between `v1` and `v2`.

Now comes the execution of the test. We check if the result of the test is correct.


## General thoughts about tests

A lot of people think that the only reason for writing tests is finding bugs. They couldn't be further from the truth. Of course this is one of the reasons why we write tests, but the other reason is probably even more important: Tests enable us to fixate the behavior of the code.

### Double Entry Book Keeping

Robert C. Martin compared programming with tests to double entry book keeping //Clean Craftsman. I really like this comparison. In both cases you have two independent truths (creditor and debitor, or code and tests, respectively) that have to yield the same result. Once both truths yield equal results, it is highly likely that this result is correct. Because it is unlikely that the same mistake was made for both code and tests when implementing both of them independently.

Having two absolute truths allows you to play around with one of them. You still have something to check that the final result is correct. This allows you to refactor the code while leaving the tests as they are. Or you may change the tests while leaving the code as is. The other, untouched, component always works as a ground truth that you can compare your changes with. This allows you to refactor your code without having to be afraid that your code might break.

### Understand what you do

There are a lot of things to consider when writing tests. The example above was very simple. In real code you have to deal with much more complex objects. With many more arguments. But all together it comes down to one point: Do you really understand what you want to test? If no, there is no need to start writing a test. It would never work. It would be a waste of time. Rewrite your code to make it simpler or get someone to help you understand the problem you should solve.

### A few general tips

Make sure all the tests pass. Tests that don't pass are worthless. Even worse, they are a nuisance. When you run the tests, failing tests will confuse you. They will confuse you're coworkers. Everyone will waste time trying to fix the failing test. There is only one single solution to prevent this: all tests have to pass. Thus make sure your CI enforces that all tests pass.

In the setup part it is very common to have helper functions that create all the objects needed. These are normal python functions that return the desired objects. You might even have a util file for all the tests. It contains some fairly static objects you might need in a lot of different tests.

There are also some things to watch out for in the execution part of the test. The first mistake almost everyone made was checking two floating point numbers for equality. Due to rounding errors this will probably fail. There are dedicated approximative checks you should use instead. As the `isclose` function used in the example above.

Then it is common to miss some of the if-else branches. These are very important to test as most bugs usually hide in conditional statements. Make sure that you cover all cases, if necessary using a code coverage tool.

Similarly you have to make sure your tests cover all the corner cases. This is one of the reasons why the tests should be written by the same person as the actual code was.

You should make sure that you always change only either the code or the tests if you refactor code. This is the only way you can be sure that the changes are correct. If code and tests have to be changed at once, the changes should be straight forward.

### Quality of test code

Tests are somewhat special, but ultimately, they are still code. Probably the test code is longer than the actual production code that you work with in a serious project. Thinking about it, it becomes apparent that when writing tests, some coding guidelines have to be followed as well.

With tests it's even more important that the code is easy to understand than with normal code. It can't be too easy. You are even allowed to repeat yourself, at least a little. Or as Jay Fields //Working Effectively with Unit Tests   put it: "when writing tests you should prefer DAMP (Descriptive And Maintainable Procedures) to DRY."

Still, you should value the SRP. The code in tests should be clear to the reader. Do so by refactoring it as you would with any other code. Keep the functions short, find appropriate names and remove excessive duplication. These things frequently get overlooked when writing tests. Even tough the requirements on test code are somewhat different than for production code.

// add some examples on good unit tests? or how to refactor not so good unit tests?

## Number of test cases

Probably the hardest decision is what values you want to do in your tests. Writing one test case for a function is much better than nothing. But maybe you just got lucky and your code works exactly for this one number? For a single argument function, I recommend testing all possible corner cases and about two other values. As you wrote the function, you will know the corner cases. Division by zero, passing an empty array as a function argument, the file used does not exist, etc.

For functions with many variables it becomes very tricky to write tests. If you have 3 arguments and for each one you would like test 3 values you end up with `3^3 = 27` test cases. This is quite a lot. Now you really have to make sure you understand what you are doing. There might be cases where the variables don’t interact with each other. They are independent. This gives you the following options.

Now if you see that they are all independent, you may test them independently. The number of tests reduces to about 3 for each variable, thus `3*3 = 9` test cases. This sounds much more reasonable. 

Usually the variables are not independent, or at least it's not so clear how they interact. And it’s not feasible to write 27 test cases. Just do your best instead. Try to test all corner cases and add a few random ones. If the function consists of well written code that doesn’t look like hiding bugs deliberately, you should be pretty much fine. And even more important: try to keep the number of arguments low.

I'd like to state again that it is important to really know what a function does. As I already wrote several times you have to test the corner cases. And you only know them if you know the code. You won’t find them by chance. Nor can you figure out if some variables are independent of each other or not. This is just one of the reasons why you have to write tests right along with the actual code. If someone else has to write the tests for your code, he’s missing this very crucial information and either has to read and understand all the code or just guess what it does. Both cases are suboptimal.

You may also have structured objects as an input or output of a function. This can become worse than having three variables by orders of magnitude. The structured objects may have a thousand fields, for example elements in a list. Everything we discussed so far becomes peanuts. But we can still achieve reasonable test coverage if we try. First of all, all elements in a list have to be treated equally. This is a fundamental property when dealing with lists. It allows you to write tests for a fairly short list and deal with only one element of it. All the other elements will behave the same. The only corner case you'll have to take care of is the empty list.

But also in large structured objects the complexity is usually managable. Most of the entries are usually fairly independent and can be tested accordingly. Most of the entries from a large structured object are probably not even needed inside a function as the object is fairly generic. Again, it all comes down to the programmer knowing the relationship between different objects. Which parts of the object are really used inside the function? Write one generic test with default values for every part of the object. Then write also tests for some specific values of the object. Though again, here you'll have to figure out which are the important values. 

## Parts of a test

A test generally constists of 3 stages. 

The first stage is the setup. It creates all the required objects for the test. Usually these are all the variables. For componentss and integration tests, this may also be copying or creating files or even databases.

The second stage is the execution of the test. Here you run the function you want to test and check that the result is as expected.

The third stage is the teardown. It cleans up all the files you created during the setup and execution stage of the test.

### Setup and Teardown

Setup and teardown are the functions automatically called at the beginning and the end of a test, respectively. This is ensured by the testing framework. Though most of the time they are not needed. The setup can also be replaced by a few helper functions. There is absolutely nothing wrong with that. And at the end of the test, the interpreter or compiler cleans up all the variables as they go out of scope. 

So in most cases and especially in unit tests, there is no need for a teardown function. However, if your tests use text files, databases or something else that is presistant, things become tricky. Your tests might need temporary files, change values in databases, have network connections, etc. It becomes messy. You need a fool proof way that your file handling always works. This is where setup and teardown really come into play.

For the file creation there is not that much that can go wrong. You create it from code or copy it from another location. This is to be implemented in the setup part of the test or using some function. The tricky part is deleting the files in the end. It may sound very simple to delete a file at the end of the test, but if the test fails, the test aborts. A normal function call for deleting the file will never be executed. There will be a mess of undeleted files. This may impact future runs of the tests and they become flaky. This problem can be solved by implementing the teardown function that is guaranteed to be always executed, no matter the result of the test. This is where the dedicated teardown function comes into play. It is guaranteed to be executed, even if there is some error occuring inside the test. Only in very serious cases like a segmentation fault, the teardown may not be executed. 

Anyway, try to write tests that don’t need files or IO. It makes things much easier. Especially in unit tests you won't have to deal with setup and teardown if you don't want to bother with it.

// write a code example?

### Helper functions

A test is also a programming object. Accordingly, it has to follow the basic rules, for example the SRP. Each test has exactly one purpose. It tests exactly one function. Testing many functions inside a single test is bad practice. Write helper functions for the setup of a test and then writing an additional test case will be simple. You may even use copy paste in tests if it makes it more readable! Having many smaller tests forces you to structure them better and improves the overall overview.

//make an example how the test can look much smoother with helper functions

### Test body

// what to write here? Are there some best practices? Make some examples.

## Problematic tests

Just as with normal code, the design of tests can be problematic.

### Dependent tests

It will happen frequently that you have a test that can only work if another test works. They are coupled. For example, you have a function that writes a file. You write a test that calls this function and checks the existence of the file. Next you write a function that reads this file. In the test you will first call the function to create the file and then call the function to read it. Now these two tests are related. They both fail if the first test fails. If the code fails to write a file it won't be possible to read it. This kind of dependency is bad design and violates the SRP. For one failing feature only one test should fail. This makes it much clearer where the error comes from. Having 50 failing tests at once is really annoying. 

Unfortunately having all the tests completely separated is a very hard, if not an impossible task. There is always some correlation between failing tests. In python tests can be made depending on each other with the `@pytest.mark.dependency` attribute. This allows us to skip tests that would certainly fail under the current circumstances.

```py
@pytest.mark.dependency()
def test_a():
    assert False

# skip test_b if test_a fails
@pytest.mark.dependency(depends=["test_a"])
def test_b():
    pass
```

As in this example `test_a` is always going to fail, `test_b` will never be executed. The execution of `test_b` depends on the fact that `test_a` passed.

### Flaky tests

Tests that do not always return the same result are called flaky. This is extremely bad. Try to avoid flaky tests at all costs. It won't take much effort to rerun the tests. The main problem is rather that it destroys the confidence of the team into the test suite. You will never know if a test is failing due to your changes in the code or because for example the network is down. At times rerunning a test might help, but this is only a superficial fix. The only real solution is writing fail save tests. Make sure for example that the network connection is checked before running a test. All tests relying on the network connection will have a dependency on this check. This reduces the flakiness by orders of magnitude. And it is good practice to design your tests such that flakiness cannot occur. Especially unit tests should never be flaky. A test only becomes flaky if some part of the code under test is flaky and this should never be the case for unit tests. Thus avoid testing any input/output (IO) for unit tests and reduce it as much as possible for other tests.

### Britle tests

Tests that are over specified are called brittle. They break when changing the code in seeminly unrelated places. One example is testing a json file for formatting, even though the contents of the json file does not depend on the formatting. The formatting does not matter. It does not change any of the values in the file. Instead testing the formatting is just a waste. Even worse, it is a needless liability because it tests something that should not be tested. Instead use a json library to get only the actual values stored in the file and compare those. This is what we are really interessted in. Never use any string operations when reading a json file. This is the very definition of brittle code!

Another example of brittle tests are tests for methods that should be private but are made public in order to test them. When refactoring such a function, the tests should not break because it shouldn't be part of the public interface. But the opposite is true. Refactoring the internals of the surrounding class will inevitably break the test. Even though the public interface is undisturbed. This is the very definition of brittle. Instead the tests should be written using only the public interface of the class. Then a test breaks only if the interface is changed inadvertently. And that's when the test should really break.

### Random numbers

If you ever use random numbers in your code, you might get stuck with your tests. You think. Because how can you test something that’s random? Well, you can. Your random numbers are usually not really random. Your computer fakes them. It uses an algorithm to create numbers that look random, but it's still creating numbers in a deterministic order. Always use exactly the same random number algorithm and seed to get reproducible results for every test case. Only use real random numbers once you ship your software.

## When what and how

### When to run tests

It is very important that tests are run automatically. This is the only way to ensure that they are always run when necessarily. When they are run exactly, however, depends on the kind of test.

Unit tests are fasts. Each one of them takes only milliseconds to run. All together they shouldn't take more than a few seconds. Split them up in subgroups if your program becomes too big and it takes more than a few seconds to run them all.

Code is only allowed to be merged into master if the unit tests all pass. This means that every programmer has to run the unit tests before creating a merge request (MR) just as he has to make sure the whole projects compiles. It is mandatory to fix code that broke unit tests, otherwise it won't be merged.

Now let me repeat: It is mandatory that all unit tests pass before an MR can be merged into master. This is a rule that should be automated. Set up the Continuous Integration (CI) accordingly. It should check the unit tests just the same as it checks the formating of the code and the compilation. This is just another mandatory requirement inside the MR. This is the only way to ensure that the unit tests are guaranteed to pass all the time.

With End-to-End (E2E) tests it becomes a little bit trickier. E2E tests are slow and can't just be run in or before every MR. Therefore you can't guarantee that all E2E tests pass all the time. Instead you have to set up the CI to run the acceptance tests overnight ("nightly build"). And if a test fails, it should send an email to all the developers who changed something the last day that the tests fail. The team then has to sit together and figure out why this is the case. In most cases it is fairly obvious why and it won't take much time to figure out who broke the test and how.

### The Beyonce rule

A common question is "what to test?". A very simple answer is everything. This is certainly a correct answer, though you cannot always test everything equaly extensive. Instead, at google they came up with the Beyonce rule. // Software Engeneering at google 
She sings in her song "If you like it shoulda put a ~~ring~~ *test* on it."

### Mocking and Stubs

// See chapter 13 of Software Engineering at google. Mocking seems great at first sight but it's not.

// is using DI and faking better?

Mocking is commonly used in integration tests if you don't want to test the interaction of the object under test with another object. For instance if the other object is a physical device, connects to the internet, etc. All kind of things that are slow or could fail. Things you don't want to test because they are flaky. In short: IO. Instead you want to simulate the device under test, the internet connection or the database.

At first, mocking sounds great. Just simulate the database and everything is great. However mocking turned out to have severe drawbacks. Most of all, mocking makes the tests rigid. You will spend a lot of time writing a mock for a database, but you will never reach the complete behavior. Thus if you add more functionality to your code, you always have to update your mock as well. This takes significant efforts.

Generally it is recommended to use Dependency Injection (DI) instead of mocking. This forces you to write interfaces instead of just mocking a few functions. Anything you want to mock might be changed in the future. And if you want to change it in the future it is good to stay flexible using a slim interface. This is what DI forces you to do.

// write some examples

## Untestable behavior

As software engineers, we want to automate everything, tests included. However, this is not always possible. There are still things that we can barely automate. One example are image processing algorithms. How much can you compress an image such that it still looks good? This is very hard to tell with an automated test and is better judged by humans. Also if you run some complex simulation, like the aerodynamics of an airplane, you cannot write a test to check that your simulation yields the correct result. Simply because you don't know the correct result. You can only judge from your experience that the result makes sense. There are still things that are better tested by humans than computers.


# 11. Types of tests

There are different types of tests, depending on their scope. There are several different categories of tests. Though for the sake of simplicity I'd like to reduce it to only 3 different types.
- Unit tests test the behavior of individual functions and classes.
- Component tests test the interplay of many functions. Typically they test the functionality of libaries.
- End-to-end (E2E) or acceptance tests test the behavior of the complete software.

As we will see, each of these categories has its right to exist as they cover different parts of the code.

// small tests are the foundation of the testing pyramid. They can be executed quickly. Meanwhile going towards bigger tests,they take longer to execute and are testing the interaction of components, rather than individual components themselves. Bigger tests might also be written in a different programming language than the underlying code. 

## Unit tests

A lot of programmers work as follows. They write a function and have to figure out if it works correctly. In order to do so, they use print statements. They run the code and check if the results are correct.
```Py
def square(x):
	if x == 2:
		x = 3
	return x**2
print(square(1))
print(square(2))
print(square(5))
```

This works. They will find the bug in this case. People worked like this for decades. But it’s absolutely terrible. The print statements will be deleted once the code works. The checks will be thrown away and no one knows anymore what the code is really supposed to do. Whether it still works. When changing the function, you have to test it all over again. Everything. Every time. By hand! This is a typical example of procedural DRY that should be optimized away. And the solution are unit tests.

Unit tests cover small pieces of code. Usually they test a public method or a standalone functions. In the example above, they would check everything that is checked using print statements.

It may sound surprising, but unit tests are even more important than E2E tests. This is because they can give you precise information about what piece of your code contains a bug, meanwhile E2E tests can only tell you that something is wrong within the whole code base. Therefore, having your whole code covered with unit tests will have a similar, though not the same, effect as having E2E tests. But with the advantage that you'll know exactly where some error occured. The drawback being that unit tests do not test if these building blocks are connected correctly.

### Testing files

Most of the time, unit tests only need a setup and an execution phase. There is no tear down required as unit tests don’t interact with any files or databases that you would have to delete in the end.

"Why...? How? No files? No database?"

Yes, good point. Somewhere in the code you might have to interact with the file system. Reading a file is 1 line of code. You read it into a string and you can forget about the file. The following function does the job. Instead of writing tests for `share_values()` we can write tests for `extract_share_values()` and pass it a string that looks like the content of the file. Such that we don’t have to deal with the filesystem anymore.

```Py
def share_values(filename):
	share_value_file = read_share_values(filename)
	share_values = extract_share_values(share_value_file)
	return share_values
```

This is similar to the GUI case for acceptance tests. You pack everything you don’t want to test into a small layer that is unlikely to fail and the remaining test becomes much smoother. In this case this small layer is the function `read_share_values` which reads the file into a string.

The same holds for database access. You put all the code that requires DB access into a few simple functions that you are not going to write unit tests for but you make sure you test everything else.

An even better approach is using dependency injection as explained in the next chapter but for the moment we’ll leave it with the small wrapper function.

### Testing classes

Writing unit tests for classes is probably the most important part of this chapter. This is not only because of the prevalence of classes, but also because classes tend to become messy without any unit tests.

First of all, classes tend to become too big. They have too many member variables and comlicated private methods. Both will make it very hard to write unit tests. Member variables share the same issues as function arguments do. They increase the dimensionality of the problem under test. This leads to many more possible test cases than should be required for good class design.

Furthermore, there is the issue of how to deal with private methods in big classes. Because apparently, the testing framework doesn’t have access to private functions. No one has, except for the class itself. A first attempt is making the private functions public. This, however, is not recommended. You should not make functions public, only in order to test them. This will lead to crippled code with too many public functions, which is the exact opposite of encapsulation. Therefore, unit tests should only test the public interface of a class. If you are tempted to test also some private functions, you should resist. This is a clear sign that your private functions are too complex. Make this private function a class on its own with a public interface that you can test.

Classes that are hard to instantiate are another problem. For example, if the constructor has side effects that are not guaranteed to be undone, as opening a file, incrementing a counter, etc. In the real code, it may be guaranteed that all the required conditions are met to never run into troubles. When running unit tests however, these guarantees may be broken in some cases, leading to undesired behavior. For these reasons, the constructors should be small and not execute any fancy operations.

As a summary one can say two things about classes and tests:
-	Classes should be small and contain few member variables
-	The constructors should be small and not rely on any fancy logic

Both these rules are implied by the topics we covered so far. But now we have a reason why we absolutely have to obey them. The unit tests force us to do so.

### Copilot

Copilot can be a significant help when writing unit tests. I wrote a function to convert literal numbers into roman numbers and created a unit test file. Copilot started implementing the unit tests right away and without further instructions.

```py
from refactoring import roman_number

def test_roman_number():
    assert roman_number(1) == 'I'
    assert roman_number(2) == 'II'
    assert roman_number(3) == 'III'
	# ... and tests up to number 42
```

However there are two minor things that I'd like to have improved. First of all there should be preferably only one assert per test. Here we have 42 of them.

Second the test is testing things that were not even implemented in the code. The roman number function was only implemented for values up to a value of 3. So it seems as if Copilot somehow guessed what kind of tests were needed but did not check what is actually implemented.

The code above can be refactored using a dict,

```py
    # refactor this code to use a dictionary
    dictionary = {1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V'}
    for key in dictionary.keys():
        assert roman_number(key) == dictionary[key]
```
Looking at the code it is not quite clear if this is an improvement over the original code. We have removed some redundancy and use only one assert. On the other hand the redundancy was not that bad and the old code was very easy to understand, which is maybe even more important than removing the repeating code. This is a decision that takes human judgement and I'm still not sure which one is the better solution.

// Person example from https://youtu.be/IavOJI5OV7g?t=588 ?

## Integration tests

// what else to write here?

Integration tests are somewhat smaller than E2E tests. They only test one part of the whole software. A single library for instance. The public interface of the library under test is not connected to other libraries, but rather to fake or mock objects. See section Mocking and Stubs in the previous chapter. Mocks allow a library to be tested allone, without creating an end-to-end test.

Integration tests, at its own right, are just as important as acceptance tests. Integration tests are different from acceptance tests as they can use fakes and stubs to mimic the behavior of collaborating objects.


## End-to-End tests

// end-to-end tests vs. acceptance tests?

End-to-End (E2E) tests do what most people would intuitively expect from a test. Some marketing person orders a new feature. He tells you exactly what this feature should do and gives you some examples. The feature is complete once these examples can be executed with your software. As you don’t want to end up in the same situation as in the story above, you write automated tests that cover the examples. This is a fairly good guarantee that the feature is still working, even if someone was working on the underlying code.

If you publish some code examples as a documentation of your API, you should write an end-to-end test for every single one of them. There’s nothing more embarrassing than failing examples in your documentation.

E2E tests are user centered. The user doesn’t know anything about the internals of the code. He has only the interfaces you give him: GUI, API, joystick, microphone, etc. And this is all he cares about. He wants to watch a YouTube video. He wants high image quality and a fast response time. He doesn’t care what kind of fancy algorithms the thousands of google employees developed.

Sounds good. But at the same time, it seems extremely difficult to write these tests? Testing a GUI or the input of a microphone sounds pretty hard. 

True. But under a few conditions the effort becomes fairly reasonable. Most importantly, you need to have well-structured code. As shown in figure // layers of software...? the GUI is an abstraction level higher than the API. The GUI code consists only of some html and CSS code, images, buttons and graphs. These things are hard to test automatically, but they contain no logic that is likely to contain bugs. Every mouse click is a function call to the underlying API. If the GUI looks fine, it quite certainly is fine. // use the expression used by Robert C Martin??

Testing on the API level is in comparably easy. Translate the button clicks from the examples into function calls. Check that the result is as expected and you’re done. In practice you have to deal with potentially huge files and databases that you have to check. This can become quite tedious and slow. The fiels first have to be created. Either from code or by copying them from another location. The result of comparing big files may also be not too helpful. One option for improving the performance is comparing hash values instead of comparing complete files. 

E2E tests are important, but they cannot tell you where an error comes from. E2E tests are quite frequently highly correlated. A single bug can cause many tests to fail. It is important to combine them with unit tests. 

One last question you might ask: “And what should I do if the GUI code contains a lot of logic? How do I test directly on the GUI?” I’m very sorry to say, you have some serious problems. This was possibly the worst mistake ever and now you pay a huge price for it. There is no reasonable way to test your code. Good luck!


## The testing pyramid

We've defined here 3 categories of tests. From the fine grained unit tests up to the very coarse end-to-end tests. As a rule of thumb one can say that the testing suite of any programm should consist of a lot of small grained and few coarse tests.

Unit tests are the foundation of the testing pyramid. They are generally the most useful as they check each part individually and can return a detailed feedback if something is broken. They are like testing the individual parts of a car radio before assembling it. Unit tests prevent the usage of faulty parts. Roughly estimated 80% of all tests should be unit tests. //quote software engineering at google. 

Integration tests are the second level of the pyramid. They are like assembling the radio with the already controlled parts. Integration tests are coarser than unit tests and can't locate errors as precisely. But they are still usefull to check the functionality of the radio. About 15% of all tests are integration tests.

The E2E tests should only check that the installation of the radio in the car worked out as expected. Turning it on once should be completely sufficient as there is not much more that can still go wrong.

E2E tests are the least common. They are very valueable to check that a program really works. There are always some things that can go wrong, even if all unit tests pass. However the feedback you get from an E2E test is very limited. It will mostly tell you that something is off, but you'll spend a lot of time debugging the cause of this issue. On the other hand you don't need too many E2E tests. If you have good test coverage with your unit and integration tests, chances are low that you'll have a lot of failing E2E tests. Once you know that the engine, the gear box and the breaks of a car work and are playing together correctly, there is not much left to test on the completely assembled car. Only about 5% of all tests are end-to-end tests.

// get an image without copy right

<img src=images/testing_pyramid.jpg width="300">

## Exercises

Write some tests to existing code

Refactor tests

...?


# 12. Writing good Code with Tests

"Programmer: A machine that turns coffee into code." – Anonymous

// https://www.testim.io/blog/test-automation-benefits/

## Unit tests 

Unit tests make sure your code is correct on the small-scale level. You don’t have to check manually anymore if the results of a function or class are correct. But this is only half the reason why they are so important. The other half might be a little bit unexpected for you: unit tests force you to write good code. When writing unit tests, you realize right away if you code is good or bad. If it’s hard to extract the filesystem part of the code, you know there is some flaw in your code and you should redesign it.

During the setup phase of the code, you have to create all the objects required. If this becomes more tedious than you would expect it to be, your data may be spread in places where it doesn’t belong. This is a very strong indication that the design of your code is bad and should be reworked.

In good code, all the relevant data is easily accessible and constructing it manually for a test case is not harder than you would expect it to be. Preferably you have one big object with fairly static information that you can reuse in all tests and one small dynamic object that is different in every test.

If you write a test you have to know the expected outcome of the function call. If you struggle for the simplest cases, chances are high your function is too complex. It should be simplified. Rewrite the code until you can explain to your colleagues what it actually does. Until you can write a unit test. Otherwise you’ll run into huge problems down the bumpy road.

You will be running the unit tests all the time. After every function you defined, after every successful compilation and after every coffee you drink. It gives you a constant feedback whether everything is fine or you just broke something. This is invaluable. The only price you pay is the execution time of the unit tests. Keep them small and fast. A single unit test may never take more than 1ms. You’ll be running hundreds if not thousands of tests, so execution time is crucial.

// move this test elsewhere? the print statements were made in the chapter before.

Let’s go back to the example code from section //...

```py
print(square(1))
print(square(2))
print(square(5))
```

There are just a few simple steps required to create a unit test out of that code.

```py
def test_squares():
	assert f(1) == 1
	assert f(2) == 4
    assert f(5) == 25
```

Finally, I would like to emphasize once again the importance of this chapter. Learn how to write proper unit tests. Read this chapter again or, even better, search for more elaborated examples. There are thousands out there. And most importantly, once again, write tests yourself and discuss the design questions with your friends. This is how you’ll really make progress.

## Component tests

Component tests cover everything between unit and acceptance tests. Usually the interplay between a few classes or a complete library. If the library becomes an external interface, you could move the according component tests in to the acceptance tests.

All together the boarder of component tests is not so well defined. Feel free so write some if you really feel like it, but generally having good unit and acceptance tests should be sufficient.

## Testing existing code

It happens frequently that you’ll be writing tests for existing code. This is much harder than writing tests along with new code, as it is very hard to figure out the weaknesses and the logic behind existing code. Usually, there are corner cases that are really hard to find. Additionally it might be hard to set up all the tests as there are no interfaces and objects are hard to create. Writing tests for existing code can be really difficult.

Many people misunderstand the idea behind testing existing code. It is not so much about finding bugs in the existing code. Rather it’s about writing an automated documentation of what the code does at the moment. And yes, you read correctly: What it does at the moment. Even if you find some bugs you should not fix them right away as users might rely on this buggy behavior. As Hyrums law  states, "With a sufficient number of users of an API, it does not matter what you promise in the contract: all observable behaviours of your system will be depended on by somebody." Or to put it a bluntly: If you have enough users, some will certainly rely on buggy behavior of your API. // Hyrums law is already mentioned elsewhere

As you write tests, always make sure they fail when you expect them to. It already happened to me several times that such checks prevented me from hours of frustrating bug fixing. Usually, due to some build problems where I tested the wrong binary, but sometimes also because I simply didn’t understand the logic behind the existing code and I didn’t realize something was already implemented.

So far, I recommended not to test private methods as it breaks the encapsulation. Instead you were supposed to refactor the class and extract the private function into a new class on its own. With existing code you have to be a little bit more pragmatic. You can’t just take any code and refactor it as you like. This will certainly introduce bugs. Making these private methods public is indeed the only way how you can test the class. Once the class is refactored, make sure the initial method becomes private again.

Apparently this way of working is a hack that shouldn’t be applied unless necessary. And it also makes apparent how important it is to write tests right away and to keep constantly refactoring before the problem goes out of control.

//more about testing existing code in Refactoring? See Michael Feathers book. 

## Asserts

There were times when people thought writing assert commands in to the production code was a good idea. There are even famous books favoring this approach. This is so terribly wrong! 

The most obvious reason is that using asserts inside production code is a violation of the SRP. You are writing tests inside production code. I guess today everyone agrees that tests and production code should be in different files, possibly even in completely different folders.

Secondly your production code is not made to run automated test cases. Asserts are only executed if you run the software you create. It will highlight you any violations of the assertions along the way, but this is not something that can be automated. It can be used at most like something of an emergency light. You’d rather focus on writing better tests instead.

## Test Driven Development

So far, we wrote tests to check if our code works correctly. We wrote them once we were done with the code. But there is nothing wrong with writing the tests upfront. It is called Test Driven Development (TDD). In fact, I recommend using TDD in general. It forces you to think more about what you want to do. You have to figure out how the test should look like beforehand. Once the test is written you need to think about how to implement the feature. The importance of the test cannot be understated. It helps you understand what you really have to do. The test forces you to structure your code accordingly, which is a really good thing. You have to define the interface of a class before writing its implementation. TDD forces you to decouple the code as your tests force you to.

In software development it may happen frequently that you have some model in mind that is supposed to solve your problem. But it turns out to be too complex and somehow you don’t manage to get it working. This might be a case of YAGNI (You Aren’t Going to Need It). // citation  Chances are you’ll never need this complex structure. Instead you can write test cases for what you really need and make sure they all pass. Everything else you can take care of later on once you know it’s really needed. On a code level, YAGNI can be prevented by writing the tests first. If you don't need a piece of code to make the tests pass, just don't wirte it. Even if you really think that it would be important, beautiful and possibly even fun to write this piece of code. It's not needed now and maybe it never will be.

Maybe you do not fully understand yet how this is really going to work. Don’t worry. You should maybe first get some experience with normal tests. At least if you don’t immediately see how a test should look like. Or if you don’t know how the final interface of the code will look like. Yes, there are several things about TDD that seem a little odd and it takes time getting used to it. But it is worth the effort. Keep trying it once in a while and start using TDD more and more often.

You write one test for the feature you want to implement or the bug you want to fix. I repeat, one and only one test. In case you have acceptance and unit tests (I hope so), you may have one open test case for each of them. If both tests pass you can take a day off.

Just kidding. If a test passes for unknown reason this is a serious issue that you have to investigate. Maybe a feature is already implemented, maybe your test is not testing what it should. 

Otherwise you start implementing. Figure out why the test fails. For new features it’s usually very obvious. What the test is testing is not yet implemented. Write enough code until the test passes. No less and no more. You don’t have to write great code in this step. Just make sure you understand it well enough until the test passes.

Once the test passes you might have to refactor to get the code back into shape. You already wrote all the required test cases as a safety net. And then you are allowed to write the next test case until you are done with the feature and the acceptance test passes as well.

There is a general pattern how you write code in TDD and its quite simple.

1. Write a failing test.
2. Write code until the test passes.
3. Refactor if needed.

These three steps you have to repeat over and over again until you are done with your ticket.

Also, with TDD you have to do some bigger refactoring once in a while. This is inevitable and has to be taken into consideration. 

### Importance of TDD

As we learned in the chapter on interfaces, they should always be defined from the user perspective. With TDD you are taking the user perspective of your code. When writing a test, you are a user of the corresponding code. Therefore writing your tests before the code forces the code to adapt the code to the test. This is a good thing. It forces the code to adapt to the user and therefore its interface becomes more user friendly.

### Example

Let's write a program that converts arabic numbers (the once we use) into roman numbers. Let's write a first test case.

```py
# inside test_roman_numbers.py
from roman_numbers import *

def test_one():
    assert roman_numbers(1) == "I"
```

If we run the test, it fails as expected. But we can make it pass easily.

```py
# inside roman_numbers.py
def roman_numbers(_):
	return "I"
```

As there is nothing to refactor, we can continue with the second test.

```py
def test_two():
    assert roman_numbers(2) == "II"
```

```py
def roman_numbers(n):
	if n == 1:
		return "I"
	else:
		return "II"
```

Now the code started to become ugly. But at least for the time being we leave it as is.


```py
def test_three():
    assert roman_numbers(3) == "III"
```

```py
def roman_numbers(n):
	if n == 1:
		return "I"
	elif n == 2:
		return "II"
	else:
		return "III"
```

Now we have to refactor, otherwise this if else statement will take over. The new version of the code might look like this:

```py
def roman_numbers(n):
	return n*"I"
```

Let's add a fourth test:


```py
def test_four():
    assert roman_numbers(4) == "IV"
```

We don't know how to deal with numbers > 4, so we may return any value we want.

```py
def roman_numbers(n):
	if n >= 4:
		return "IV"
	return n*"I"
```

```py
def test_five():
    assert roman_numbers(5) == "V"
```

```py
def roman_numbers(n):
	if n >= 5:
		return "V"
	elif n == 4:
		return "IV"
	return n*"I"
```

Two tests later we are again at the point where we have to refactor. This time we have to think a little harder how the logic of the function really works.

```py
def roman_numbers(n):
	num = ""
	while n >= 5:
		num += "V"
		n -= 5
	while n >= 4:
		num += "IV"
		n -= 4
	while n >= 1:
		num += "I"
		n -= 1
	return num
```

In a second refactoring step we wrap the whole while loops into a single for loop.

```py
def roman_numbers(n):
	num = ""
	arabic_to_roman = {5:"V", 4:"IV", 1:"I"}
	for arabic in arabic_to_roman:
		while n >= arabic:
			n -= arabic
			num += arabic_to_roman[arabic]
	return num
```

Supporting bigger numbers can be done by prepending them to the `arabic_to_roman` dict. Note that I used a dict instead of a list of lists. This is because as I mentioned in chapter //?? that list elements should all be treated equally. Thus having a list `[[5, "V"], [4, "IV"], [1, "I"]]` would violate this principle.


## Fakes and Mocks

There are many cases where you have to write a test but the code you want to test contains something you don’t want to test. Like a database or an internet connection. You want to have a fake database that returns the value you expect and will never fail. The solution is writing a database on your own. Not a complete one. One that does only what you really need for this test case. It implements every function you call and returns some values that you want. You may have to implement quite some logic into the fake database to implement the desired behavior, depending on how complex your test cases should be. Maybe you need different fake databases for different tests. You might need a dedicated database that throws an exception in some special case.

In general, there are two ways to use a set-up database. Faking and mocking.

### Mocking

The first one is to use an existing database and change some of its behavior using a mocking framework. In the following example we mock the result when reading a csv file. In python this is easily done using the Mock library.

```py
from important_stuff import *

from unittest.mock import Mock

def test_mock_important_stuff():
	# Override the `read_csv` function defined in important_stuff.py and simply return some values.
    read_csv = Mock(return_value=([7], [8], [9]))

    assert read_csv("unexisting_file.csv") == ([7], [8], [9])
```

### Faking

A fake is a working version of the object you want to replace, albeit it's a simplified version. For example your fake csv reader does not read a file from the disk, but just returns a string stored in the code. For running tests this is usually good enough without having the drawback of dealing with the file system, where your original data could easily be deleted or messed with by anyone else.

Faking is usually closely related to dependency injection. For this reason these things are both explained at the same time in the next section.

### Dependency injection

In this case you create a new object from scratch, which pretends to read a csv file. But in reality it just returns a bunch of predefined numbers. This works if the `CsvReader` object implements a `Reader` interface and an instance of the `CsvReader` is handed over as a function argument. Then one can replace this function argument with an instance of a `MockReader`.  As python uses duck typing, one can also omit the definition of the interface. The whole code would look roughly as follows:

```py
from abc import ABC

class Reader(ABC):
	def read_file(file_name):
		pass

class CsvReader(Reader):
	def read_file(file_name):
		data = []
		# implement reading a csv file, see chapter on data files
		return data

class FakeReader(Reader):
	def read_file(file_name="not_needed"):
		return [1,2,3]

def get_data(reader):
	return reader.read_file("top_secret.csv")

if __name__ == "__main__":
	real_data = get_data(CsvReader())
	fake_data = get_data(FakeReader())
```

Using DI is generally a very recommended practice and should always be used when dealing with IO. For the very simple reason that you can very easily replace the code that you inject with something else. In the example above it would be fairly easy to write a `SqlReader`  that gets the data from a database instead a csv file. 

These `Reader` objects should be instantiated as soon as possible. Usually this is possible at the point where the type of reader is selected at a fairly high level of abstraction. The only drawback of DI is, that this object has to be passed through the whole stack down to the point where the database is actually used. On the other hand, this would have to be done with a string if DI was not used. Which certainly isn't any better. It just delays the selection process.

```py
filename = ...
if reder_type == "fake":
	reader = FakeReader(filename)
else:
	reader = CsvReader(filename)
reader.read_file(filename)
```

Delaying this decision would be a bad idea. Switch case selections should be resolved as soon as possible. There will be one place in your code where the user (or you) selects the kind of database he wants to use. Create the corresponding reder object right away. Dependency injection is the way to do it and it prevents you from writing really bad code.

Now don’t worry if you haven’t understood everything. I just explained very briefly dependency injection, faking, mocking etc., which are all fairly advanced topics. I just hope you got some of the basic ideas I tried to explain here. They can be useful and the ideas behind them are very important. In fact, these ideas are that important that you’re going to see them again in the section on the strategy design pattern. // or should I remove the design patterns?

As always, many books only focus on OO programming. They only explain dependency injection for classes. However, having classes is not a strict requirement for dependency injection. You can also pass different functions as function arguments in those programming languages supporting function pointers or duck typing. This has the advantage that you don’t have to deal with base classes and so on. It’s just not used that often because usually you want to inject complicated objects and function pointers can only be used for simple objects. Though generally I would recommend using dependency injection instead of using function objects. Simply because it can be used in all major programming languages the same way and you don’t have to learn anything additional right now.

//here I have to write about spys, mocks, fakes, stubs, etc! See clean craftmanship, p.118

So far for the technical implementation and the introduction to mocking. But the real problem is only to come once again. The question is how and what to test. Apparently, it’s no solution to write a complete database simulation every time it is needed. This is not only a hell lot of work. It also makes the code rigid. // and now what...?


### Copilot

Copilot knows about dependency injection as well. Again I had to write only about half of the comment in order to get a reasonable suggestion.

```py
# write a class person with attributes name and age
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

def print_name():
    person = Person('John', 30)
    print(person.name)

# use dependency injection to print the name of the person
def print_name(person=Person('John', 30)):
    print(person.name)
```

# 13. Refactoring
“If you wait until you can make a complete justification for a change, you’ve waited too long.” – Eric Evans

Refactoring is the art of changing existing code without altering its functionality. 

## There will be change

If code lives long enough (which is usually sooner rather than later), it will have to adapt to change. The build system might change, the database might change, and you'll have to adapt yourself to the new environment. This is almost inevitable. Only if you write extremely low level code with hardly any dependencies you might be save. Or you write mobile apps that are guaranteed to last only 1 or 2 years. Thus you have no choice but to adapt to the changing environment. Your code has to stay flexible. You have to keep it in shape. Make sure you can react to change.


## Keeping code in shape

// first refactor the core, refactor subsidiary code only when needed. It is important to focus on some parts. Refactoring the whole code is a tremendous amount of work. Make supporting code to be generic.

// The behavior of the software may not be changed or the users stop using it.

Even without external changes it is important to refactor your code once in a while. We have to face the sad that fact that our perfect code deteriorates over time. Every line of code you add is a possible source for deteriorating the code quality. You may add duplication, increase the class size or disrupt the order of logic in your code. Brief, the code becomes dirty and you have to clean it up. Sometimes it is also compared to entropy, the physical law of disorder //Thomas & Hunt. Fighting entropy is hard. It takes a lot of efforts. // see section on entropy

Refactoring is just like cleaning up your kitchen. Every time you cook something you have dirty dishes. But unlike for the kitchen you cannot hire a cleaning lady to clean up your code. She wouldn’t know what to do. You have to clean up your code by yourself. You have to refactor it. Continuously. You will be spending more time refactoring than writing new code. And as the code becomes older it only gets worse. That’s the faith of a software engineer.

I guess everybody reading (or writing) this book knows some of the problems why code rots. The very first example is copy paste code. This should be banned altogether. Instead of rewriting a function to fit its new needs, one just copies it and changes a line or two in its new location. Another issue is adding more and more features to an existing class. Also the features that you add are in hindsigth at the wrong place in your code and have to be moved to the correct location. These are some of the reasons why code rots and needs regular refactoring.

### Refactoring and automated test

Refactoring means to change the code without changing its functionality. This is what people didn’t do in very old code. They were afraid that they would change functionality. They would introduce bugs. It's like they didn’t clean up the kitchen because they were afraid, they might break something. And they didn’t see the reason why they should have cleaned up the kitchen. They only had a nagging feeling that something is wrong, but they couldn’t say what exactly. Long story short, the next person had to cook in a dirty kitchen. And at some point, there were so many dirty dishes in the kitchen they didn’t even see the bugs anymore that could hide underneath each and every dirty plate. People using the kitchen were afraid of introducing bugs when refactoring but now they were left with bugs anyway. They didn’t clean up the kitchen nor refactor the code. They started adding many more bugs further down the road, because the whole code base became so messy.

I really hope you understand that not refactoring is not an option. A cook has to clean up the kitchen continuously just as you have to refactor your code. All the time. Refactoring is an integral part of your job, not just an optional feature. Therefore, we have to take you your fear from refactoring, your fear from introducing bugs. You need a safety net. Something that automatically tells you when you introduced a bug... You need... automated tests! Unit tests, end-to-end tests, whatever. Just make sure your tests cover pretty much all the functionality of the code you want to refactor. There are tools to highlight the lines of your code covered by tests. Or you can also change one line of code and see whether one of the tests fails, though this is not a very productive solution.

If you are confident about the test coverage you can do pretty much anything you want. Whatever code you don’t like, just throw it out and rewrite it from scratch. Or use a third-party library. As long as the tests pass you are fine.

### Keep refactorings small

Most refactoring is fairly small. Renaming a variable. Breaking up a class into two new classes. Removing duplicate code. Extracting functions. The biggest mistake one can make with refactoring is waiting for too long. If you have the gut feeling your fundamental data structure could be an obstacle you should act right away. Discuss with your work colleagues whether this is really the correct choice and what other options you would have. Peripheral code can still be refactored later on. But if the core of your code is rotten you will have a big issue fixing it. And it will only get worse if you don't act quickly.

Probably you do some smaller refactorings quite often. But not really in a structured manner. You refactor as soon as there is some code you don’t like. This is honorable. But there is a very simple workflow that I can recommend to everyone. It’s: write code – test – refactor. For every feature you implement you should follow this pattern. Or even better, you can also write the tests before the code, as explained in the chapter on Test Driven Development. This pattern is great because you can really do one thing at the time. You can write mediocre code to start with. Maybe you don’t know yet how a variable should be named or you tend once again to write a class that is too big. Maybe there’s even duplicated code. Certainly, it would be better to write perfect code right from the beginning. But you’re not perfect.

Then you write the tests. Some tests may fail as you’re not so perfect code contains bugs. You fix the bugs and the code becomes even more ugly. Even if you had written sublime code to begin with, due to the inevitable bug fixes you would still have to refactor at some point. This is something that was missed by the waterfall development. You never write perfect code to start with. It always takes some refactoring in order to get there.

Finally, you refactor. You look at all the code that you wrote since you refactored the last time. Possibly also at code that existed for a long time and could be merged with your new code because it’s very similar. The code will probably look more complicated than you would expect it to be. You try to rethink the logic of the problem you just solved. Can you change the algorithm somehow that you can drop all the if statements for the corner cases? Or do you have to sort the data differently to make the code better?

There are hundreds of things you could do for improving the quality of the code. Look at the code and figure out what the most important things are you want to change. Try to write good code and follow your gut feeling. But make sure you also get some real work done between the refactoring sessions.

## Levels of Refactoring

Maybe you came up with a simple question: On what level should you refactor? Should you refactor only the small things, or should you dig down to the core of your software?

Let me make another small example. You like cooking and you are going to build a house. You make sure in the kitchen is ample space for all your equipment. You are very pleased. Yet dishes get dirty you still have to clean up the kitchen every day. Otherwise you’d be in no time left with a huge mess. This corresponds to the everyday refactoring of a software engineer. Make sure you remove code duplication, name all variables properly and clean up everything along the way you don’t like.

Once in a while you buy an additional kitchen device and over time you start running out of space. You have to sort out all the old devices you don’t need anymore, and make use of your Tetris skills to fit everything back into the shelves. This is an intermediate refactoring.

At some point you buy another machine and you realize there is not enough space anymore for your equipment anymore. There is only one solution. You need a bigger kitchen. You have to plan how much additional space you need for the next few years and either tear out some walls or expand your house. Now this will be a very demanding and expensive refactoring.

I hope you got the memo. Small refactoring should be done all the time. Every few lines of code. The costs are low and it keeps your work space clean. Intermediate refactoring costs more and effects a fair amount of your code base. It should be discussed with your work colleagues during the coffee break and may be done together. Big refactoring is really labor expensive. It’s done only every few months and takes good planning and dedicated meetings as there is a lot at stake.

### Refactoring is dynamic

Also consider that waterfall refactoring is bound to fail just as most waterfall projects are. Refactoring is concrete. Just as normal coding, it consists of a learning process. It’s a feedback loop. It usually has to be done incrementally and endless planning sessions are a waste of time. Every couple of lines you write you learn so many new things that require you to adapt the refactoring plans. Possibly you even have to drop these grand plans all together because you realize they just won’t work. And software engineering is concrete. You can have as many beautiful plans as you want. If they don’t work out, they are worthless.

You have to face the facts. Waterfall refactoring is not working out. Instead you have to follow the actual dynamics of making changes, learning more about your code and adapting your future changes. These three steps are the only way how refactoring is done. 

// Make circle graphic: changes to be made, make changes, more changes to be made

### The circle of doom

There is something very mean about refactoring. Refactoring good code is easier than refactoring bad code. For instance, working with code containing global variables, many dependencies, etc. is always a pain, no matter if you are writing new code, tests or doing some refactoring. In all cases you have to understand what the code really does. For writing new code and tests, this is bad enough. But with refactoring is becomes a nightmare because you have a circle of doom. You start postponing your refactoring because it’s hard to understand bad code. But over time, this will only make it worse and worse and worse. Until you reach the point where refactoring is essentially impossible and you are paralyzed. You’d have to refactor your code because it’s bad, but you can't because it's gotten too bad to make it better.

Don’t slack off refactoring. You’d pay the price rather sooner than later. Make sure you always keep the code in shape, this makes your life much easier.

// The behavior of the software may not be changed. Even if it’s a bug, you should rethink fixing it as the users may rely on that bug.

// section on text book refactoring -> write something about Michael Feathers book. Or the few pages of Uncle Bob.

## When to Refactor

// some parts of the text here are redundant.

It is generally a good idea to do refactoring. Most developers do rather too little refactoring than too much. Still, there are some general recommendations when to refactor or not.

Every few lines of code you wrote, you should consider refactoring them. It is not always necessary, tough it is by far the best moment. You still know what you just programmed and you might have an idea what there is left to improve. Additionally, you are always working on a tidy workplace which increases your productivity. Code that’s well taken care of is much easier to modify.

As already mentioned above, you should always refactor the code you just wrote. This is the number one rule. Furthermore, you should stick to the boy scout rule: Leave the camp ground tidier than you found it. Always refactor a little bit more than you should have. This helps fighting the code entropy. This rule is also known as the boys scout rule.

Refactor when you found a bug. Don’t just add a patch that might resolve the issue superficially. Search for the real source of the problem. Then consider if there is some redundant code that might need fixing, or better refactoring, as well. Find a good fix for the bug, possibly including some refactoring.

If you add a feature, it may not really fit into the code. Most likely, because the code has not been cleaned up, or the other authors simply didn’t know how the code should look like. But now, as you’re adding this new feature, you’re smarter. You might have an idea how the code should really look like for the feature to fit in. Now don’t squeeze the feature into the existing code base. Refactor instead and make sure the new feature fits in smoothly. Altogether, this is less work. And especially the code will ultimately be in a much better condition.

Also, during code review you can do refactoring. Team up with the author of the code and do some pair programming. This is much more motivating than a normal review as there is better knowledge exchange and the output of the review is significantly increased.

Generally, you should refactor code that you work with. In some cases, you may refactor code that you just walked by, but this should not be the rule. If there is no reason for you to touch that code at the time being, you shouldn’t refactor it. It is important in software engineering to know when to postpone some work and this is one of the cases. If no one works with a piece of code at the moment, there is no need to refactor right now.

// is this redundant?

Once in a while, you have to do a bigger refactoring. One that you don’t just do between writing a few lines of code, but it will take considerable efforts to get it done. You should probably discuss this topic with your work colleagues, opposite to the smaller refactorings that you just do by yourself.

Most important of all, it is your code. You are responsible. You are the one to decide it’s time for a refactoring. Don’t ask your boss for permission to refactor. Just do it.

## Refactoring process

Refactoring follows a similar process that I also use when writing this book here. I first started with writing down the basic ideas. Some rough drafts of what I wanted to have in this book. Then I was reading the text over and over again and reworked it several times, removing redundant parts and adding some more explanations where needed. Every time I started to understand my text better and could further improve it. Until I was roughly at the point where the text said what I wanted it to. Until I had put all my knowledge from my head into the text and sorted it out into a human readable piece of text. Or as Ward Cunningham had put it: “By refactoring I move the understanding from my head into the code.”

// add the graph from p.193, DDD. Refactoring is no linear process.

Refactoring, just as writing code, is a highly non-linear process. It cannot be planned too well because it is a creative process. And knowledge gains may come out of the blue. All of a sudden you understand the problem much better and the code can be improved accordingly.

## Refactoring techniques

The techniques explained here mostly require an existing set of automated tests as changes to the code may introduce bugs otherwise. Refactoring can be done also without tests, though in most cases, it is a very dangerous game to play. Even if some techniques seem save to be applied without tests, there is always some latent danger of breaking the code in some way. Especially if you have gobal variables or overriden functions it becomes tricky. Refactoring code in compiled languages is a little bit easier as the compiler does valuable checking of names, functions, types, etc.

There is a plethora of concrete refactoring techniques to be applied in specific cases. I will only briefly explain some of them. Most originate from the book Refactoring of Martin Fowler //Refactoring, Addison Wesley, 2019.

// add or remove some techniques?

### Renaming

Even though renaming does not change the shape of the code, it should be done extremely often. Finding good names is one of the hardest tasks in programming. There are some general rules how to do it, yet still it’s not easy at all. This leads to the fact, that there are many objects with suboptimal names. And as you write some code, it may happen that you spot something you just happen to know a better name. Then rename this object. This is the only way names get better over time. Don’t assume the author of the code knew it better. You have much more information now at hand that simplifies finding a good name.

### Extract function

If I have a function or method that is too long or not cohesive enough, I can replace some of the code with a newly created function. This is one of the most important refactoring techniques as too long functions are an extremely prevalent phenomenon and this is the main mechanism to get it under control. If there are not too many variables involved, the technique is fairly simple. The biggest difficulty is finding good names for the newly created functions.

Let's say we have this very simple code here. We already saw that this is violating the SRP as printing a string and calling a function are two different levels of abstraction.
```py
print("author: Marco Gähler")
print("********************")
print_content()

def print_content():
	# print some stuff
```

The solution is taking the explicit print statements into a function and call this function instead.

```py
print_header()
print_content()

def print_header():
	print("author: Marco Gähler")
	print("********************")

def print_content():
	# print some stuff
```

For once you are allowed to use copy paste in order to create the new function as the old code will be deleted anyway.

There is really not that much more to know about extracting functions than what I just showed here. It is really a simple refactoring technique, yet it is very important. This is probably the most used refactoring technique.

Inlining functions is the opposite and used rarely. Take a function call and replace it with the function body. Apparently, this makes the surrounding function longer as soon as the copied function body has more than one line. This is generally not desirable. Inlining functions only makes sense for one- or maybe two-line long functions, or if you are planning to refactor the surrounding function and you are planning to split up the old function.


### Scratch refactoring [Feathers p. 212] 

Scratch refactoring is not about improving code, it is only about getting an idea how the code could look like. Just refactor as you like and don’t care about bugs or similar issues. Figure out how the code should look like in a dream world.

Once you’re done refactoring, discard everything and do a normal refactoring, trying to apply the ideas you just got. Pay attention you don’t just lightly reimplement what you did before, you might have missed some technical details why the solution from the scratch refactoring might not work out the way you did it.

## Real life refactoring
// Stuff here is from Feathers book. Read it again and add some more stuff here.

In real life, your start getting afraid of the code changes you make in a refactoring. There’s just too much that can break without any test telling you. This is apparently a really bad thing. No one likes to life in fear. In your own code you can prevent this situation by meticulously testing all the code you write, but if you work on an existing project, you will have to face the demons. 

Refactoring untested code is usually a very hard task, there are whole books about it. And if the code is already pretty bad, refactoring becomes even harder. The most common issues on the macro level are
1.	No tests
2.	Obscure code
3.	No time

And on the micro level we have a few more indications that things will get tough:
1.	No interfaces
2.	Functions with side effects and global variables
3.	Huge classes and functions
4.	Objects hard to construct 
5.	Inheritance

Let’s say you want to break a class into pieces, but it's really big. It has no tests and you are uncertain of the side effects it might have. This is bad as functional changes introduced are bugs. The only way to prevent these changes is having plenty of tests.

### Seams

Now writing tests would be a very noble thing to do, but it is not always so easy. As I explained before, how easily you can write tests depends highly on the quality of your code. In order to write tests, you need something you can get a hold on. Michael Feathers calls this a “seam”. “A seam is a place where you can alter behavior in your program without editing in that place.” //WELC Thus, you can edit it elsewhere, in the so-called enabling point.

There are several different ways to implement seams. The best seams are interfaces and dependency injection. They are very easy to deal with and resemble normal code. Just create a new implementation of the interface or inject it and you are done.

Some of the seams explained in WELC change the behavior on the compiler level, either by the linker or the preprocessor. Needless to say, that implementing such kind of fancy seams is a fairly desperate measure. Such techniques resemble strongly black magic and should be avoided.

The most common seam is simply function arguments. It is not mentioned in WELC and the following code is just a strictly worse version of using dependency injection, but it is still a seam. 
```py
def f(debug):
	if(debug):
		# ...
	else:
		# ...
```
Passing a Boolean as done above is bad design. It is much better making the choice earlier on and passing on an object as explained in the chapter on dependency injection.

Usually just passing a number or a string is not sufficient for implementing a seam as changing their values does not alter the behavior of the function significantly. It only yields a different result.

However, the piece of code you hold in your hands between two seams may be way too big and you have no idea what you should test exactly. In the extreme case the only tests you can write are system tests. And if you don’t have any useful API you might be completely screwed.

### Sketches

Making sketches and diagramms may help you finding ways to refactor your code. This doesn’t have to be UML diagrams. It can be anything that helps you understand your code. Some kind of temporal behavior or what Feathers called a “scratch refactoring”. Basically, a draft code that shows how the final code could roughly look like without considering all the details that make real refactoring so hard. These are all tools that help you understand your code better and make it easier to write the actual refactoring code.

// Add the temporal graph from Evans?

## Copilot

It seems as if Copilot sometimes struggles with refactoring code. At times it doesn't find a reasonable refactoring suggestion. Though with playing around a little and giving Copilot some hints, it works out quite well. Here is an example:

```py
def roman_number(number):
    if number == 1:
        return 'I'
    elif number == 2:
        return 'II'
    elif number == 3:
        return 'III'
    # elif number == 4:
    #     return 'IV'
    # elif number == 5:
    #     return 'V'
```
Having only the first 3 cases and asking Copilot to refactor this code, it makes the following suggestion:
```py
    # refactor this code to use a dictionary instead of if/elif/else
	return {1: 'I', 2: 'II', 3: 'III'}.get(n, 'Invalid number')
```
This works out but it's not quite what I wanted. After commenting out the case for 4 and 5 and explicitly asking for a while loop, the code looks as follows:
```py
    # refactor this code using a while loop
    roman = ''
    while number > 0:
        if number >= 5:
            roman += 'V'
            number -= 5
        elif number >= 4:
            roman += 'IV'
            number -= 4
        elif number >= 1:
            roman += 'I'
            number -= 1
```
This is pretty much what I wanted, except that one could use a dict with number-roman number pairs. Asking explicitly for using a dict, the code looks pretty much how I wanted it to be. 

```py
    # refactor this code using a dictionary
    roman = ''
    roman_map = {1: 'I', 4: 'IV', 5: 'V'}
    while number > 0:
        for key in sorted(roman_map.keys(), reverse=True):
            if number >= key:
                roman += roman_map[key]
                number -= key
                break
	return roman
```

This code can be further refactored with the following command:
```py
    # refactor this code using a for loop
    roman = ''
    roman_map = {1: 'I', 4: 'IV', 5: 'V'}
    for key in sorted(roman_map.keys(), reverse=True):
        while number >= key:
            roman += roman_map[key]
            number -= key
	return roman
```

It seems as if Copilot worked best for refactoring if one gives it some step by step instructions.


// how does Copilot do with refactoring some more difficult problems?

## Exercises

// get some convoluted pieces of code and let the reader refactor them. How should he be guided by copilot? I really don't know. 

# 14. Understandable code

“Any fool can write code that a computer can understand. A good programmer writes code a human can understand.” – Martin Fowler

// This chapter is somehow not up to the point...

As we have discussed, good code is easy to understand. But what makes code easy or hard to understand? A computer understands anything, he doesn’t care. As long as the syntax is correct. And if there is a bug, the computer just executes it. But we don’t care about the computer. This book is about humans. We have to ask ourselves, when does a human understand something? Or what do humans struggle with?

Humans are fundamentally different than computers. We can do incredible things, yet at the same time we have severe weaknesses. The evolution adapted us to our environment. We were made to life in the forest, hunt animals and socialize with our clan. We needed good eyes to see our prey, get an understanding of the terrain and the direction of the wind and we had to know our hunting party. These things require a lot of intuition and approximate thinking. These are things computers or robots struggle with. Though they improve thanks to the emergence of artificial intelligence.

Something humans are not good at is very obvious. Math. We are bad at math. It’s so simple and logical. Yet it took me 12 years of school to calculate a differential. And I was comparably good! Humans are not made to think logically. We are guided by instincts and approximate thinking.

You can play terrible tricks with humans as we all follow the same laws of psychology. Even experts fall for such tricks. We can only mitigate our weaknesses by accepting them.

On the other hand, we are amazing at understanding complex processes by creating an abstract model of a process and analyzing different parts of it. We know a lot of different things and we can have an abstract imagination what would happen if we combine many of them. 

We are also pretty good in communicating with others. Using the natural language. We are able to explain fairly difficult things and others understand us. Just as you (hopefully) understand what I write here.

We are terrible at math and we can be extremely easily fooled. On the other hand, we are fairly good at understanding general objects, behavior and language. As long as they are not too complex. We can explain these things in English or any other language you wish. We can combine some of these semi complex objects into a new object, which... is still only semi complex. You can still describe what it does. 

This is how we are able to create extremely complex objects. We have to break them down into small parts that we understand very well and them build them together like Lego. Every time we assemble a few pieces we create something new that we give a name for and are able to explain to other humans what this thing does.

Most people driving a car have a fair idea how it works. It has an engine, wheels, breaks, a steering wheel, etc. We can mentally break down a car into smaller objects that we still understand roughly. Now if the car has a technical problem, we can probably guess quite well, which of all these parts broke.

So far, every programmer that told me he was working on a really complex problem simply wrote bad code. They all failed to break the problem into small pieces and reassemble them again. Or rather they didn’t realize they should do so and wrote spaghetti code instead. The code became so complicated they were barely able to add any new features. If something is complex you absolutely have to break it down. As long as someone can explain to you in words how something works, you can also write understandable code.

You should never underestimate the complexity you can create with bad code. If you write a thousand lines of unstructured spaghetti code, it might cost millions to rewrite it.

This whole book is about how to write low complexity code. The sections on the Single Responsibility Principle, naming and levels of abstraction are probably the most fundamental ones.

## Exercises

// ...? Write some very general question as done in the Pragmatic Programmer.

# 15. Programming languages

“I think I’m a much better programmer now than I used to be, even though I know less about the details in each programming language I work in.” – Michael Feathers, Working Effectively with Legacy Code, p.311

A very frequent question from beginners is “which programming language should I learn”. Some may have read somewhere that programming language A is better than language B for some very obscure reason. The very simple answer is: It doesn't matter too much. Most of the Object Oriented languages are similar enough and the different programming philosophies don't matter too much. A lot of the low level C++ features for instance can be wrapped into a higher level object, making it an intermediate level language. However it's still not such a high level language as Python.

I really want to emphasize that you shouldn’t learn a programming language in too much detail. Reading a small book about the language you want to use is certainly a good start. A small book, not a big one. The rest you can search in the internet as you need some specific syntax along the way. Google and Stackoverflow are a better help than your vague three-year-old memory. It is much more important that you learn how to program in general. To understand the general concepts. The concepts are easier to understand and more powerful than some syntax. Syntax you can easily look up, meanwhile concepts you have to understand.

But as you asked for a programming language, I would briefly like to give my point of view. Though it is highly biased. I know C++ and python and a little bit about Java and JavaScript due to the programming books that I read. If you work in a field where one specific programming language is used, you should certainly learn that one. Even if it’s just Matlab.

As I am a scientist, I would recommend python as a first programming language. Javascript is a viable alternative for non-scientists. They are both scripting languages that don’t need a compiler and are fairly easy to get started. As they use duck typing, you don’t need inheritance to define an interface. Any two objects that have the same interface can be exchanged in the code. And there is no need to learn anything about pointers or memory allocation like in the old days.

I would not recommend learning Java or C++ as a first programming language, even though I use some C++ code in this book. C++ and Java are too complicated and it takes much more time understanding the language itself. The C++ examples throughout this book are only to explain things you don't have to care about in Python. Instead you should learn how to apply the principles taught in this book and elsewhere to improve your code. Of course, later on in your career it makes sense to learn many more languages. Java and C++ are still among the most widely used. Not because they are better, but simply because there are so many old projects around. 

C++ and Java are static typed, have to be compiled, use inheritance to define interfaces and in C++ you have to deal with pointers. Learning new languages will show you other ways of thinking about some problems. Changing from Python to C++ you'll have to learn quite some basics of software development. It opens up more job opportunities as well. But it’s nothing you need to know when you just start programming.

## Existing programming languages

Programming languages and APIs share the same difficulties. It would be easy to create a new programming language that is clearly better than an existing one. But there are millions of programmers that already use the current languages and their code is worth billions. You cannot update such quantities of code only because there are a few new features that make the code a little bit shinier or more performant. Instead, there are thousands of developers making suggestions how the current programming languages could be improved without breaking compatibility. A team of experts will debate about all kind of possible issues before a new feature or internal change will be accepted into the standard of a programming language.

For example: In C++ there is the boost library. Pretty much everyone programming C++ knows it. It is certainly the most commonly used third party library and has a high-quality standard. The boost library contains hundreds of very important libraries that are not part of the C++ standard library. Usually new features are first implemented and tested as a boost library. Only once a new feature has been used and tested by the community for a few years, it might be accepted into the C++ standard library. This is how the smart pointers and the filesystem library made their way into the standard.

## Code examples

There are quite few code examples in this book. Most concepts that I explain here can be explained with real world examples. And I want to teach you concepts, not syntax. In some cases I will still use code examples, but the code should be really simple. The code examples are mostly written in Python and sometimes in C++ if needed to explain some low level feature. It’s not a deliberate choice to use Python and C++, it’s just the programming languages that I know. I’ll try to explain the examples such that you can roughly understand them, even if you don’t know the according programming language too well. I promise that the syntax will be very simple to understand. It requires only the very basics of the corresponding programming language.

## Python
// Do I need the opinion of some expert?

Even though Python is a fairly easy programming language to learn, there are some things that are some language specific things worth learning.

### Type hints

// https://youtu.be/dgBCEB2jVU0

Python is dynamically typed. At first, this seems like a great thing. You don't have to write the types and a function can be called by many different argument types. But it also comes along with its drawbacks. Types are an important part of the information of arguments and return values. With types, you know what kind of operations you are allowed to perform, or what the expected outcome of an operation will be. For example the `+` operator does something quite different with floats than with strings. So at times, it would be useful to know the type of a variable.

While it is not possible to enforce types in Python, and according to Guido van Rossum it will never be as it's not pythonic, it is possible to write type hints. A simple `: int` following a function argument to indicate that it should be an integer.

Here is an example using type hints:
```py
def digits_of(number: str) -> list[int]:
	return [int(d) for d in number]
```
But as I said, this is not enforcing that the argument of `digits_of` is a string. You could also pass a list of floats instead and have a perfectly valid result. It's just that this was apparently not intended by the author of the code.

I generally recommend using type hints as it makes the code much more readable. Even if it moves the syntax a fair amount closer to C++. C++ is not such a bad programming language after all. It's just a little bit old fashioned.

### Slots

// https://youtu.be/Fot3_9eDmOs

Python is a very dynamic language. It allows you to do things that wouldn't be possible in other languages. For instance, you may add fields to a predefined class as such:
```py
class Apple:
	def __init__(self, price: float, weight: float):
		self.price = price
		self.weight = weight

apple = Apple(1.0, 0.5)
apple.hi = "hi"
```

Adding this member variable `hi` to an existing class instance wouldn't be possible in hardly any other language. And this for good reasons. It's generally not good coding practice to do such things. For example you could accidentally misspell something like `apple.pice = 2.50` and python doesn't complain. Rather, it creates a new member variable `pice` and assigns it a value of `2.50`.

This issue can be prevented by using slots. 
```py
class Apple:
	__slots__ = "price", "weight"

	def __init__(self, price: float, weight: float):
		self.price = price
		self.weight = weight
```
Slots fixes the available member variables. In this case, there are only the variables `price` and `weight` allowed. (Accidentally) adding other member variables to the `Apple` class is not possible.

## Abstract base classes

Though it is not required, I still recommend using abstract base classes (ABC), as done throughout this book. It makes the code slightly more readable as it defines the structure of the interface you are going to use and implement.

## C++

C++ has some particularities like pointers, arrays, a preprocessor and header files that make the language somewhat special. Thus I'd like to explain some of the things where C++ tics while other programming languages tac.

C++ has been developed by Bjarne Stroustrup and published in the 80ies. He took the existing C programming language and added object orientation to it, along with some other things. So yes, it is a very old language, but it is still around and will accompany us for several more decades. Thanks to the constant development of the language, it has overcome many of the ancient problems that it brought along. At the same time, C++ is a very good example to learn a lot about programming languages and how they evolved. As I used C++ in some of the examples here, I’m going to explain here some of the particularities of this programming language.

### Pointers and arrays

Pointers point to an address on the heap. The place where the dynamically allocated variables live. Pointers are used to access complex objects that should not be passed around as a whole due to performance issues. However, dealing with raw pointers can lead to all kind of errors, memory leaks, and even worse, undefined behavior.

Along with pointers go arrays. They are a continuous piece of memory that the user has to manage on his own. He has to allocate them manually and delete the memory at the end of its life time.

```C++
#include <iostream>
// create an array with length defined at runtime
int length;
std::cin >> length;
// allocate memory with new[]
int * dice_rolled = new data_type[length];
// do something with the array
// delete the memory with delete[]
delete[] dice_rolled;
```

Pointers and arrays are barely used anymore on a daily basis. In most cases, they are taken care off by the modern C++ data formats like vectors. Vectors are a high-level object that offer about the same functionality as arrays, but it is much more user friendly as it’s almost impossible to introduce any errors. More details about vectors and arrays are given in the chapter on Levels of Abstraction.

#### Smart pointers

Smart pointers, `std::unique_ptr` and `std::shared_ptr`, are the replacement for the plain old pointers. Smart pointers are a higher-level implementation. It has things built in like reference counting and they know when to go out of scope. There are still some things to know like for example weak pointers, but these are mostly details that you don’t have to care about in the beginning.

There are libraries that require plain old pointers as function arguments. This is no reason to use plain old pointers all throughout the code. Instead you can convert the smart pointer into a pointer using the `get()` function.

```C++
auto foo = std::make_unique<Foo>();
some_old_C_library(foo.get());
```

#### Vectors

Similar to the issue with smart pointer, there are libraries that require plain old arrays instead of vectors. This, however, is no reason to use arrays throughout your code. Instead you can use vectors as usual and convert them to arrays using the `data()` function as needed.

```C++
std::vector<int> vec {1,2,3,4};
some_old_C_library(vec.data(), vec.size());
```

### Pass by reference

In order for an object to be mutable, it can be either passed by pointer or by reference. Passing by pointer is outdated. Objects should always be passed by reference. If it is passed by const reference it cannot be modified. Passing by const reference is very frequently required as passing by value creates a copy of the object and requires a lot of memory.

### Classes

C++ was one of the first mainstream programming languages to support classes, inheritance, etc. Probably it became so wide spread because most things worked out pretty well, except some details about multiple inheritance. #source? But as I told you not to use inheritance, you don’t have to worry about such details.

There is one thing however that was done better in other languages, in Java for instance. In Java, defining an interface is actually called this way, while in C++ one has to define an abstract base class. This is the only kind of inheritance that I recommend using. Remember when I say you shouldn’t use inheritance: the whole thing with abstract base classes should be named differently and is not affected by this rule.

### Structs

Structs are similar to classes, however all members are public. In general, structs are used to store different data types, though in theory they could also contain functions. The last is only forbidden by general agreement.

Structs are generally very useful objects, as explained in the section on classes. It’s a pity struct like objects are barely used in Java and some other languages. In Java a struct can be defined as a normal class containing only variables without any getter nor setter functions. Though as far as I know, this is not too common.

For more intormation about C++ I can recommend the google C++ style guide, https://google.github.io/styleguide/cppguide.html

## Copilot

Copilot can be used to translate between different programming languages. Here is a very simple example to show the capabilities of copilot. Though I don't know how difficult code snippets copilot can translate.

```C++
#include <iostream>

for (int i = 0; i < 10; i++) {
    std::cout << i << std::endl;
}
```

```py
for i in range(10):
    print(i)
```

## Exercises

- Learn some new programming languages. Write a program to read a simple comma separated value (CSV) file and save the values in a list/vector/array/... for at least 5 different programming languages.
- ...

# 16. Bugs, Errors, Exceptions

"It’s not a bug; it’s an undocumented feature." - Anonymous

Even if you write absolutely amazing code, some things will still go wrong. Some of these things are no problem at all, while others can be absolutely deadly. Literally. Problems are less critical if you find them early on and they are immediately recognizable. If your compiler finds an error the cost are barely worth mentioning. Triage the source of it an fix it. However if your software is already in production, the consts are significant.

I would briefly like to go through the different cases.

## Syntax Errors

Syntax errors happens to anyone, even the most experienced programmers. It’s normal and not a problem at all. You are not even able to run the code in this state. Fix it and try to improve your knowledge on the programming language you use. Syntax errors are the best example how problems don't cause any harm if they are caught early on. In compiled languages, the compiler will find the syntax error, in Python the parser checks the corectnes of the syntax.

At the beginning of our programming careers, we were all bothered by the compiler errors. We were happy once there were no more errors. Our programming skills were just too low to realize that the compiler was helping us. It is a good thing we got compiler errors because this might have saved us from creating serious bugs.

## Bugs

A lot of people underestimate the problem of bugs. They are easy to ignore because they don’t show up too often and maybe they are not too bad. Just some glitches. But this is exactly why bugs are so catastrophic. You don’t necessarily know something went wrong. You might have an idea something is off, but you are not sure. Or you don’t know at all. This is the absolute worst case that can happen in your code. You think everything is alright but in fact, it is not. Your hard disk got deleted, a bank lost a million, an airplane crashed. Anything is possible. Bugs are the absolutely worst thing that can happen to your code. Sure, most bugs are not that terrible. But don’t take them lightly.

### Cost of Bugs

The cost of bugs is gigantic. It may take hours, if not days to track down a bug. And in bad code it's frequently not clear how it should be fixed. Furthermore the cost of bugs increases exponentially over time. This is due to the growth and the additional complexity of the code. // SE at google, p.207

I hope you got the memo. In a small project, you can do pretty much anything you want. But you have to make sure you don’t create bugs. Write good code and make sure it’s well covered by tests. This is the only way to keep the number of bugs low and stay as far away as possible from the exponential growth of the cost they cause.

### Debugging

Debugging is the process of finding bugs. If you spend too much time debugging it’s a clear indication that your code quality is bad. You don't know what you are doing and you lack tests. Even with good code quality some bugs are inevitable. But at least it is usually fairly obvious where a bug is trying to hide.

In order to find out what some existing, badly tested piece of code is doing, I generally recommend using the debugger. Even though the knowledge gain has to be taken with a grain of salt. The results of the debugger are only a snapshot from which you try to extrapolate general behavior. Debuggers are by now quite simple to use and in most cases clearly superior to print statements. Writing tests or refactoring the code would of course be better options, but these take a lot of time.

### Copilot

// copilot is able to detect at least some beyond the array size errors

Copilot is able to find some bugs. Though I expect it to find only minor bugs, this is already a real feat. For example take the following code snippet,

```py
    roman_map = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X'}
    roman = ''
    for key in sorted(roman_map.keys(), reverse=True):
        while number > key:
            roman += roman_map[key]
            number -= key
    return roman
```
Here I introduced a bug as the code should be `while number >= key:`. The bug was easily found by Copilot labs fix bug function. Highlight all code shown here and click "fix bug". 

Once again, there is the question wether this bug was fixed because copilot know the code pattern or because it really "understands" what it does. The code has already been created by copilot itself.

## Exceptions

// throw exceptions only for the exceptional case. Exceptions are expensive as they do stack unwinding, etc. Only throw exceptions for the really exceptional cases. In C++ they have soon std::expected instead.

Exceptions happen in cases where the software is supposed to do something but it can’t. Or if the software knows that it shouldn’t do something. Some examples are writing files if there is not enough disk space left or a division by zero occurs. Though some programming languages can return infinity. There are not too many things in every day programming where an exception might occur. Mostly input/output (IO). Yet they have to be taken care of. The user has to be noticed to fix the problem.

User input should always be validated right away. Are all values correct? When writing and supporting your own code this is not a big deal, but users need human readable feedback. A "division by 0" error message is of no use when the input file has 10 variables that are all 0. Check the sensitive values and return a useful message instead. "Invalid input: price cannot be 0", makes it much easier to track down the source of the problem. Check the values that are sensitive and return an appropriate error message right away. If there is some invalid state, you should throw an exception as early as possible.

In case of connection problems or missing disk space, the user needs a corresponding error message to be able to resolve the issue. “no network connection available”, “not enough disk space”, etc.

### Wrapping exceptions

You don’t want exceptions to leave your code. This will crash the software. It is not a big deal for a small standalone project as it possibly should be terminated anyway. But in serious software development you cannot allow this to happen. It is recommended to define your own error types. Put a try catch block around the whole code to catch your custom exceptions. Custom exceptions mean that the user did something wrong. Add another try catch block around the whole program in order to catch all exceptions. These are unexpected errors, bugs. Write a different error message and kindly ask the user to contact your support as this is a programming error.

Raise exceptions right away if the program goes into an invalid state and return a message to the user what went wrong. It is not worth trying to deal with a semi invalid state, this is not worth the effort. Exceptions originating not from faulty user input should result in a message to send a bug report.
```Python
if __name__ == “__main__”:
try:
    main()
except CustomException:
	# You defined this exception, so you know what went wrong.
	# Return some error message how to resolve the issue
except:
	# You don't know what went wrong. The user should send in a bug report.
```

Try except blocks have some similarity to if else or switch case blocks. They are all susceptible to bad code, especially to violating the SRP. Therefore, apply the same rule to try except blocks as to if else blocks. There should be only one line of code within each option, usually a function call or a simple error message. Furthermore, try except blocks should be the only thing within a function. The single responsability of this function is managing the try catch block.

One common pattern is catching and reraising exceptions. This allows you to add additional information, depending on the type of exception. This is not worth the effort. This additional information is not really helpful to the user. Instead you should define a custom exception type and print an according message when catching it.

Make sure your unit tests check the exceptions as well, exceptions are part of the code specification. However, in some cases it is impossible to write a unit test. For example, you should never read in a file in a unit test. Instead you should use dependency injection to inject a file object throwing an exception. We go into more details in the section on dependency injection. 

### Exceptions and goto

By the way, you might have heard of the goto statement that was widely used until about 1970. Dijkstra wrote the famous paper “Goto considered harmful”. As always there was a lot of truth behind his argument but there are cases where Goto statements are a legitimate choice. The Linux kernel is written in C which doesn’t have exceptions and thus the Linux kernel uses Goto statements instead. The goto is called when an error occurs and redirects the code to the catch block. Thus, goto statements are not all that bad, they were only used in a bad manner as you can write terrible spaghetti code using goto statements.


# 18. Programming Paradigms

//remove this chapter? I don’t have much to say here, even though I’d like to. See clean Architecture (?)

## Object Oriented programming

Object Oriented (OO) programming started in the 80ies. It peaked with the still very wide spread languages C++ and Java. Somehow the whole software developer community became absolutely ecstatic about it. OO programming is great. It makes everything so easy. It is the natural representation of things. It will save the world!!!

It still amazes me how some half-baked promises can cause such dynamics in a group of highly intelligent people. Come up with some buzz words and the crowd does the rest. Even in times before social media. The only explanation I have is that the software engineers were all sitting in their basement and missed everything else out there. They had to create their own hype instead.

Well, now let’s be serious. As always, the truth lies somewhere in the middle. Yes, OO programming makes things easier. But it did not save the world. And most things that were developed along with OO programming are outright garbage. Without the hype around OO programming, these things would never have been able to get widespread usage. People stopped thinking critically and just started using all kind of OO features that turned out to lead to terrible code.

Don’t use any other OO feature than plain classes and abstract base classes or interfaces.

//write more about OO programming? And how does the linux kernel keep the compilation times under control? Libraries and pimpl?

## Procedural programming

While OO programming is mostly based on classes, class instances and methods, procedural programming depends mostly on functions and logical operations. In procedural programming, functions are more important than data types. Though, contrary to functional programming, you are allowed to have hidden states and use output arguments. This simplifies writing code at times but the code created this way is harder to understand due to the additional complexity.

## Functional programming

Functional programming is the way to programm using only functions. No classes, no mutable variables. This is a very strong restriction to the programmer and makes programming more difficult. On the other hand, it has also its advantages. You don't have to pay attention on things like mutable variables. Functions don't have side effects. The only thing that they change is the return value. Furthermore the return value of the functions only depend on its arguments. These are called pure functions.

Having only pure functions has several advantages. First of all it is generally recommended to use only pure functions where ever possible. Also in OO programming. Pure functions are much easier to deal with than functions depending on some kind of state. They are also much easier to test. You will never have the issue that you don't know how to test a pure function. Call the function with some different arguments and check that the return value is correct. It won't get any easier.

Due to the pure functions, functional code is generally easier to understand than, say, procedural code. This is because functional programming depends only on states that are easy to understand.

In many programming languages you can mimic functional programming to some degree by using only pure functions. And I highly recommend doing so. Using only functional programming, however, is quite tedious to get started with, but it's certainly worth the effort to get a new view on how programming can be done.

## Conclusions

All different programming paradigms have its advantages and drawbacks. Statements like "You have to use OO programming because it mimics the real world" are certainly outdated. It is best to be acquainted with all different paradigms in order to be flexible and adapt your style to the current needs. The times where you were supposed to write only procedural or OO code are over. If you are flexible, you can write better code.

## Copilot
Here is an example where copilot went haywire. I wanted it to create code like `a = [i for i in range(10)]`, but somehow this didn't work out. The output is certainly wrong.
```py
a = []
for i in range(10):
    a.append(i)

#rewrite the code above using functional programming paradigm

# Path: code_examples/softare_paradigms.py
a = []
for i in range(10):
    if i % 2 == 0:
        a.append(i)
```
When explicitly asking for a list comprehension, it works out.
```py
# rewrite the code above using list comprehension
a = [i for i in range(10)]
```

# 19. Design patterns

// not sure yet what I should write about design patterns.

// visit the youtube videos of Derek Banas, https://youtu.be/vNHpsC5ng_E

There is a famous book called design patterns [Gamma et al., 1995]. It describes ways how classes can be used to interact with each other and form new patterns. It certainly is a tremendously important book in the history of software engineering, but as with many books on OO programming, it turns out to be slightly outdated. Here I’d like to give a brief overview over the most important design patterns. Some more design patterns are explained scattered throughout the rest of the book.

One drawback is that you might start over engineering your code when using too many design pattern. You don't need a design pattern to cover every corner case. You don't have to make everything generic. It's more of an 80-20 phenomenon where 20% of all the design patterns cover 80% of all the code. // https://youtu.be/BPSuWUXyA58

## Factories

// Don't write code like this. The car calls the factory to create a part of the car. Instead you should call the engine and build up the car from it.

A factory is used if the construction of an object becomes too complex to handle in a constructor. Instead you want to have a dedicated object or function to take care of it's construction.

```py
class Car():
	def __init__(self, brand, model, has_AC):
		if brand == "mycar" and model == "123":
			self.engine = # ...


class CarFactory():
	def create_car(self, brand, model, has_AC):
		self.engine = self.create_engine(brand, model)
		self.AC = self.create_AC(has_AC)
		
```

// when to really use a factory? Polymorphism? when an object becomes too complex to create it by the constructor

There are different kind of factories. These are objects that create other objects. It makes sense to set up a factory if the output object is fairly complex. Setting up such an object within the constructor would clutter the class. It wouldn’t obey the single responsibility theorem anymore. I would like to highlight as well that a factory does not have to be a class. It can be a simple function as well.

## Visitor

Let's say you write a compiler and you have an Abstract Syntax Tree (AST). This tree represents the code that is to be compiled. Each node in the tree is of a certain kind. For example + is converted into an "add" node having two children.

Now you could write all the steps of the compiler, like the loop processor for example, into the nodes themselves. This, however, would result in code that is poorly structured. Changes usually involve compilation steps as the loop processor mentioned above. This would involve changing all node types at once and spreads all the related code across the whole code base.

Instead one can use the visitor pattern. This allows to add functionality to an existing class. In this way, the loop processor can be written as a single class, that acts on all the different nodes.

### Implementation

// not yet completed.

```py
from abc import ABC

for node in nodes:
    node.accept(visitor)

class City:
    def accept(visitor):
        visitor.do_for_city(this)

class Visitor(ABC):
	def do_for_city(city):
		pass

class Tourist(Visitor):
	def do_for_city(city):
		print("visiting city")

class SalesPerson(Visitor):
	def do_for_city(city):
		print("Meeting clients")
```

## Strategy pattern
//need to add some more text

The strategy pattern is basically the same as dependency injection. Once again, it’s worth to remark that the strategy pattern can be used with functions as well as classes.

## Façade

## Adapter

## Template

## Flyweight

## Observer

//etc. ...

## Copilot

Copilot knows quite well about design patterns. The bigger challange is explaining to copilot what you actually want to do. Here is the example of a factory created by a single comment and very little help to get the code started.
```py
# write a factory that creates a logistics object that implements a road logistics or sea logistics
def create_logistics(type):
    if type == 'road':
        return RoadLogistics()
    elif type == 'sea':
        return SeaLogistics()
    else:
        raise ValueError(f'Invalid logistics type: {type}')
    
class Logistics:
    def plan_delivery(self):
        raise NotImplementedError('Subclasses must implement plan_delivery')

class RoadLogistics(Logistics):
    def plan_delivery(self):
        print('Plan road delivery')

class SeaLogistics(Logistics):
    def plan_delivery(self):
        print('Plan sea delivery')
```

# 20. Decoupling
// Maybe look at Fowlers book refactoring again. There might be some advice.

// add some more text from the pragmatic programmer

Coupling is a very essential part of software engineering. Without coupling, it wouldn't be possible to write code. Coupling is the glue that sticks everything together. But too much glue is bad as everything becomes sticky. In bad code, everything depends on each other. Every module or file imports dozens of other files. This is really bad because if you want to change one file, you might have to change a whole dozen. Instead you have to make sure that the coupling is as low as possible. This keeps the code soft and flexible.

This is one of the reasons why global variables and inheritance are not recommended. Global variables are the worst as they instantly glue the whole code together. It’s like importing something everywhere. This is absolutely deadly. Don’t use global variables.

Inheritance is not quite as bad, but almost. Everything that depends on a derived class automatically also depends on its base class. You are not only coupling the derived class to the base class, but also the other way around. You can barely change one without changing the other. This is not how flexible code is supposed to be. Don’t use inheritance.

// A service locator is an intermediate object that knows about more or less everything. If you want something, ask the service locator. This is an anti pattern.
instead of asking what you want, you go to the service locator and reach through the service locator.
https://youtu.be/RlfLCWKxHJ0 video on service locators
Only ask for things you directly need

// Null paranoia: You don't have to check everything for not being null. Only check this if needed. There are cases where null is a perfectly viable option.

One common rule on coupling is the law of Demeter. Though it's not a very strict law. Martin Fowler called it "The occasionally useful suggestion of Demeter" // Refactoring p.192. More formally, the Law of Demeter for functions requires that a method `m` of an object `o` may only invoke the methods of the following kinds of objects: // https://en.wikipedia.org/wiki/Law_of_Demeter, https://www2.ccs.neu.edu/research/demeter/demeter-method/LawOfDemeter/paper-boy/demeter.pdf
- `o` itself;
- `m`'s parameters;
- any objects instantiated within `m`;
- `o`'s attributes;

The idea is to avoid so called train wrecks where you start chaining methods to achieve something. For instance you shouldn't write code as
```py
car.get_engine().turn_on()
```
Instead the `car` object should take over such function calls. Write a function inside the `Car` class `turn_on_engine()`,
```py
car.turn_on_engine()
```
Though as I already said before, this is only a vague recommendation and not a strict law. Don't become over enthusiastic about it. 

## Exercises

// Compare 2 different versions of some code and let the reader figure out why one is more coupled than the other.

# 21. Physical laws of code

"I think you should always bear in mind that entropy is not on your side." - Elon Musk

## Entropy

Entropy is the physical law of disorder. It says that disorder is always going to increase. Fighting entropy is a lot of work. It is like you cleaning up your room every week. If you don’t do it, your room will become dirty and you don’t find your stuff anymore.

In software engineering we have a very similar phenomenon and it has very severe consequences. As we write code, there is more and more disorder created. On the one hand, this is very natural as a growing code base automatically attracts more disorder. There is simply more stuff around that you have to take care of. On the other hand, this disorder is also man made. The entropy only grows significantly if you allow it to. You have to fight entropy in your code the same way you fight entropy in your bedroom. You have to clean up regularly. You have to sort all your belongings. You have to throw away stuff that you don’t really need or is duplicated. This will take time and effort. But such is life. You don’t get a well payed job in IT without doing the dirty part as well.

// This text is somehow duplicated with the beginning of Refactoring


## Correlation

// don't mix good and bad stuff. Then everything becomes bad.

Similar things belong together. It sounds fairly trivial and it is extremely helpful when designing code. And it’s true for pretty any aspect in programming. Not only code objects, but also abstract concepts. 

There is a market for food and further down the road there is a store selling electronics. Each kind of store has its own domain. If you find a market store selling apples, chances are high the next store sells apples as well. It is just normal that similar things align together. The same holds for code. Functions are bundled together by their functionality, as are classes. This makes them easier to find if you search for some specific functionality. At the same time, they should also have the same level of abstraction. The main function, for example, consists only of a few high-level function calls. No string manipulations or other low-level stuff. These low-level functions are buried somewhere in a deeper level of abstraction.

Once you start thinking about this rule, you will automatically structure your code in a much better way. It becomes so much tidier. It will feel more natural and it doesn’t need too much work to make it better.


# 22. Software Architecture

"The perfect kind of architecture decision is the one which never has to be made" ― Robert C. Martin

// Rethink this chapter. I state that architecture is everything, but at the same time only write about libraries. This chapter somehow needs serious rework to be done.

// where to write about stability of code? see clean architecture and 97-things-every-programmer-should-know chapter 74

## About Architecture

An Architect designs a house from the bigger picture down to the tiny details. But designing is not all he does. He also visits the construction site at least once a week to check the progress made, discuss possible issues with the construction workers, etc. An architect is responsible for everything, including all the small details.

In software development, the word architect seems to be used a little carelessly. Frequently people use it only for the high-level designer of an application. The architect designs whatever he feels like and leaves the rest of the work to the development team. Of course, this is bound to end up in trouble.

In the following I’ll follow the notation of Robert C. Martin what architecture should be. Architecture should be everything. From the high-level design all the way down to the tiny details. If you were hoping to get here some general advice how to design the high-level part of your software, I’ll have to disappoint you. It’s more about the general picture.

Good architecture takes time. It takes time to think about the structure of the code, time to clean up leftovers and time to write tests. But what if you have to be faster and start sacrificing quality of your architecture? It will take time to understand the code, time to change the code, time to explain your new colleague how everything works. Brief, you don’t gain anything. On the opposite, you will be much slower on the long run. Even under the pressure from the marketing and sales department, don’t let the quality of the architecture down. It will never pay off. Quick and dirty does not exist. There’s only slow and dirty.

One of the main jobs of a software architect is defining the building blocks (libraries) and interfaces of the whole software. Some of the interfaces may be only partial interfaces, meaning that it’s like an interface within a library. It fulfills all the requirements for a real interface and the library could easily be broken into two pieces at this point.

A partial interface has the advantage of needing only a limited amount of maintenance for versioning, etc. On the other hand, there is the danger that the interface gets lost over time as programmers start working around it.

It’s the architects’ job to figure out in the beginning where are what kind of interfaces required. He has to foresee the future. The YAGNI principle therefore doesn’t always hold for an architect. Because what if it turns out that we really needed that interface?

// write something about structuring classes into a library.

// Pretty much anything that holds for classes also holds for modules/libraries. Increase cohesion within a library and reduce coupling between libraries.

// One shouldn’t just cut the code horizontally or vertically. One should do both.

// Should we mention Uncle bob’s principles how modules should be structured?

//I think there is some more to mention from clean Architecture.
Separate Libraries

In every bigger code base, you’ll have to work with several libraries. Some of them are developed internally, others are 3rd party libraries. There are many things to consider when making such choices. The very first question is: do you need another library? Or can you implement the required functionality within an existing library? There are some mechanisms that favor smaller or bigger libraries. 
s
// These rules were for domain models and not for libraries. Move it to the according location. Instead add the rules from Clean Architecutre.

Reasons favoring bigger libraries are:
-	Flow between user tasks is smoother when more is handled with a unified model
-	If is easier to understand one coherent model than two distinct ones plus mapping between them
-	Translation between two models can be difficult
-	Shared language fosters clear team communication
Reasons favoring smaller libraries are:
-	Communication overhead between developers is reduced.
-	Continuous Integration is easier with smaller teams and code bases
-	Larger contexts may call for more versatile abstract models, requiring skills that are in short supply.

These advantages for either sides lead to tradeoffs in library sizes. Generally, it is favorable to create a dedicated library if there is a corresponding opportunity.

### Coupling

Interestingly, all the explanations made here about coupling and cohesion are also valid for libraries. You should pay attention that libraries are not becoming too large and rigid. You don’t gain a price for writing the biggest library in the company. One library that covers every object there is around. It just won’t work! An apple can have a color, a flavor and a price. There can be three different libraries graphical rendering, food and shopping. Each one uses exactly one property and it makes no sense to mix them up. Keep them separate and write glue code between the libraries if needed. That’s the only way to go. Just trust me. Don’t write a monolith software that should mimic the whole world. It won’t work.

# 23. Solid principles 
// Source: https://youtu.be/pTB30aXS77U, https://youtu.be/9ch7tZN4jeI and Clean Architecture

The solid principles were named by Robert C. Martin. SOLID is named after 5 general rules how to write code. These are:
1.	Single Responsibility Principle (SRP)
2.	Open closed principle
3.	Liskov substitution principle
4.	Interface segregation 
5.	Dependency Inversion

These 5 very general rules describe mostly how classes should be structured and connected with each other. Obeying them helps a lot with the design of the code. Interestingly enough, most people agree on the fact that these pirnciples are very important, but there is no exact common agreement how these principles should be applied nor what they mean exactly.

These principles hold for compiled languages as Java and C++. Python users have to know only the first two principles, the other three are nice to know but there are ways around them.

## Single Responsibility Principle

The SRP has already been explained at the very beginning of this book due to its high importance.

## Open Closed Principle

The Open Closed Principle (OCP) was first mentioned by Bertrand Meyer in 1988. It says that an object should be open for extension and closed for modification. The original version states that one should use inheritance to achieve this goal. This is an unfortunate choice. Robert C. Martin and others suggest using interfaces instead. Interfaces allow you to add as many implementations as you want at comparably low cost, while it is fairly expensive to change the interface itself. Each class implementing that interface would have to be changed as well.

Our code should be stable with respect to extensions later on, but not to changes. If the requirements change, we have to change our code as will. This is inevitable. But we shouldn't have to change our code if someone else wants to change his code. Thus the solution is to use abstractions at potential abstraction points. This allows the user of our code to extend it without us having to change anything in our code.

Let's make a small example. We have a class containing some postal codes of Swiss cities. If we want to add an additional city, we'd have to add an additional function to this class. The class `City` is not closed for modification. We have to modify it every time we add another city. This class is not obeying the OCP.

```py
class City:
	def zurich_postal_code(self):
		return 8000
	def bern_postal_code(self):
		return 3000

def print_all_postal_codes():
	city = City()
	print(city.zurich_postal_code())
	print(city.bern_postal_code())
```
If the user of this code wants to add another city, we have to do this within our own code inside the class `City`. This is the oposite of what the OCP says.

Instead we can create an interface city and implement it for every city we are interessted in. If we are interessted in adding an additional city, we don't have to change any existing class or interface. Instead we can create a new class to extend the implementation of the city interface. Like this it follows the open closed principle.

```py
from abc import ABC, abstractmethod

class City(ABC):
	@abstractmethod
	def postal_code(self):
		pass

class Zurich(City):
	def postal_code(self):
		return 8000

class Bern(City):
	def postal_code(self):
		return 3000

zurich = Zurich()
bern = Bern()

cities = [zurich, bern]

for city in cities:
	print(city.postal_code)
```

Now this code on the other hand fulfills the OCP. If the user wants to add another city, he can create as many additional cities as he wants and we don't have to care about it. The base class `City` defines the interface and that's enough for us to work with any class the user adds.

## Liskov Substitution Principle

// see https://youtu.be/pTB30aXS77U

Implementation of interfaces shouldn't blindly follow the "is a" principle. This is only a rule of thumb and not sufficient. Instead the implementations really have to share the same interface.

For example credit cards and paypal should not implement the same payment system interface, even though they are both payment methods. The credit card requires a card number, while paypal requires an email address. This leads to the situation where you don't know what the payment interface should take as an input argument.

```py
class Payment:
	def make_payment(amount, card_number_or_email_address)
```

This logical contradiction about what the second argument should be (email address or card number) is a violation of the Liskov substitution principle. Credit card payments and Paypal payments should not implement the same interface.

##  Interface Segregation Principle

The Interface Segregation Principle (ISP) is like the SRP for interfaces. Interfaces should be split up into many small parts. This is important in order to keep the coupling low. You don't want to import and compile a huge library only because you need one small feature of it. If there are some logical blocks within a library that are separate, make sure that they are made available separately.

Here the file A does not follow the ISP. It does 2 independent things. Most other code needs only one of these functions. They are independent. Thus, they should be in different files. 

Now in Python this is not such a big deal as you can import each function individually and even if you import the whole file A it's not a big deal. In C++ on the other hand, this is really a no no. In C++ you always include a whole header file at once and you'll have to compile everything that comes with it. There might be a hefty price to pay if the file A would be too big.
```py
# file A
def function_1():
	return 1

def function_2():
	return 2
```

// add graphs on the file dependencies below

The solution is to split up the file A into two subfiles A1 and A2. The goal is to find a way to do this, such that most of the other files use only one of the newly created files A1 and A2. The amount of code that they import is reduced roughly by half. This can be repeated until it is no longer possible to reduce the amount of code imported. At this point you finished the segregation of the file A.

```py
# file A1
def function_1():
	return 1

# file A2
def function_2():
	return 2
```

A common example is defining an enum inside a class, while other parts of the code might need access to this enum as well. This other part of the code has to import the complete class containing the enum, even though it doesn’t care about anything else than this simple enum. This other code import much more code than it would have to. And the solution is pretty simple. One can just extract the enum from the class and have it stand alone. Then it fulfills the ISP.

```py
# inside ImportantStuff.py
from enum import Enum

class BigClass:
    class Color(Enum):
        RED = 1
        GREEN = 2
        BLUE = 3
	# and much more code

# inside SomeOtherFile.py
from ImportantStuff import BigClass

c = BigClass()
color = c.Color.BLUE
```

Here we first need a class instance of `BigClass` because the enum is hidden inside of the class definition. This could be avoided by moving the enum outside the class. This would reduce the coupling of the code as the user code depended only on the enum and not on the whole class around it.

## Dependency Inversion Principle

Dependency Inversion Principle (DIP) is a technique used in languages as C++ and Java to reduce the compilation times considerably. The files in your project include each other and form a tree with the main function at its root. The so-called dependency tree. The leaves of the tree are low level functions of your code and other libraries, as we have learned in the chapter on levels of abstraction. The main function is the root.

// add a graph for the dependency tree

For interpreted languages like python the dependency inversion principle is not so important. This is mainly a technique to break compilation dependencies which don’t exist for interpreted languages. Though it's still good to know this principle as a python user as it is very fundamental.

The first time you compile your code, the whole code base (the whole tree) has to be compiled. This can easily take minutes, maybe even hours. The resulting files carry a time stamp. If you recompile your code later on, only the files that changed since the last compilation have to be recompiled. For small changes, this reduces the time required for compilation to a few seconds. However, there is a serious problem. As you change a file, you also affect all files that include this file, directly or indirectly. Everything in the branch of the tree up to the main function. A small change in a library file can cause huge parts of the code to recompile. For everyone working on the project. This is why software developers have so much time to spend in front of the coffee machine, waiting for their code to compile.

We first have to understand the source of this problem. As I mentioned before, it has to do with the `includes` (or `imports`). The main file includes all the other files. It is the root of the dependency tree. If one file changes, main changes as well as main directly or indirectly includes all other files of the project. Therefore, the main file has to be recompiled as well. It’s like a hard link.

Instead we want a soft link. Main should depend only on the public interface of a library, not its implementation. Such that main won’t be affected by internal changes of the code within a library. If I change a file in a library, I want to recompile only the library itself. I want to cut off this library branch from the dependency tree and deal with it independently. Main shouldn’t know about anything going on within this branch. Main shouldn't have to recompile if the code within this branch changes.

This is where dependency inversion comes into play. It does exactly what I just described. It breaks a branch off of the dependency tree and instead couples it loosely by the interface of the branch. You can do that by defining an abstract base class (interface in Java) that defines the shape of the interface. The file containing this interface doesn’t have any dependencies. It’s on the lowest level of the dependency tree. Or at least in something like a local minimum. The old interface code of the library inherits from this interface. It implements it. As main uses this library, at first is has only the information of the interface. Everything else is hidden as it’s not included. Unless you change the interface, changing code inside the library will not cause anything else to recompile. 

### Example

```C++
#include <iostream.h>

class Nothing{
	void do_nothing() {}
};

int main(){
	auto nothing = Nothing()
	nothing.do_nothing();
}
```

Now `main` depends on the `Nothing` class and everything that's inside it. Instead we can define an interface for `Nothing` and break this dependency.

```C++
// inside NothingBase.hpp
class NothingBase{
public:
	virtual void do_nothing() = 0;
};

// inside Nothing.hpp
#include "NothingBase.hpp"

class Nothing : public NothingBase {
public:
	void do_nothing() override {}
};

// inside main.cpp
#include "NothingBase.hpp
int main(){
	auto nothing = std::make_unique<Nothing>();
	nothing->do_nothing();
}
```

Now `main` depends only on the interface of `NothingBase`, not on the implementation defined in `Nothing`. Changing `Nothing` does not change `main`. Therefore, `main` does not need to be recompiled if `Nothing` changes! `main` and `Nothing` are only connected together by the linker. The linker will make sure the main function calls the correct implementation of this library.

// dependency tree graphs

### Pimpl

// reference to meyers book. or skip this part?

In case you've ever heared of the pimpl (pointer to implementation) idiom, it has the same goal. It achieves it by using pointers instead of abstract base classes or interfaces. There’s no need to use it. Defining interfaces is the strictly better option than using pimpl.

## Summary

I think this was the longest section in this book where I explain technical details for C++ that Python users don’t necessarily need. At the same time, I’d like to emphasize that this section was very important for the C++ and Java programmers. Both, for the quality of the code, and also for understanding how the whole concepts of includes, compiler and linker work.

## Exercises

For each principle create an example where it's violated and let the user correct it.



# 24. Datatypes

// what is the definition of data types and variable types?

// primitive obsession -> David Sackstein Cppcon 2022

There are hundreds of built-in datatypes. But again, I recommend not to use too many of them. Types by themselves are not improving your code. Only use other built-in types than mentioned here if you think it does so.

At the same time it has to be said that using custom types (classes) is highly recommended. For example you should always use a class `Money` when appropriate and not use floating point numbers. Using custom types makes the code more readable and easier to write. It prevents you from primitive obsession.

"Primitive obsession is a code smell in which primitive data is used excessively to represent data models." This is a very common phenomenon. Integer values are used as time, even though the there would be a time class in pretty much every programming language. Or strings are used to store all kind of information as we'll see an example further below.

Here is a list of datatypes that I generally use. They are called differently in most languages. I write the Python name and in brackets the C++ name: floats, ints, lists (vectors), enums, Booleans, strings, dicts (maps), trees, classes, (pointers).

I give you some explanations on all these types except floats, ints and classes. I simply don’t have anything to write about floats and ints. Except that I never use unsigned ints, as recommended by the google style guide. Classes are discussed in their own section.

## Lists

Lists are the work horse in programming. Whenever you deal with several values that should all be treated in the same way, they belong into a list. I would like to emphasize: to be treated the same way. If you do something with a list you should always iterate through all elements and do the same thing for all of them. If you somehow need just one value from a list, chances are high you shouldn’t use a list.

Here is an example how not to do it:
```py
fruits = [‘apple’, 1.5, 3.1, ‘banana’, 0.8, 2.1]
```

I deliberately made this code so terrible for you to understand. Strings and number cannot be equal objects so they may never be inside the same list side by side. In C++ this kind of list isn’t even possible. At least not without visiting a highly advanced course in C++ black magic. In Python on the other hand, this is syntactically correct code and it is frequently tempting to write such a list. Please resist this temptation!

The second problem is that we don’t know what these numbers mean. There is no reasonable name for this list that explains everything. This list violates the single responsibility principle all by itself. 

And third code based on this data structure will inevitably become brittle. It’s screaming for bugs. You can do pretty much everything wrong and I promise you will.

Apparently 3 values inside this list always belong together. In C++ we would create a struct for it, in Python we use a data class.

In Python the code should be rewritten to something like this:

```py
@dataclass
class ShoppingItem:
    name: str
    weight: float
    price: float

apples = ShoppingItem(name='apple', weight=1.5, price=3.1)
bananas = ShoppingItem(name='banana', weight=0.8, price=2.1)

shopping_list = [apples, bananas]
```

Now the code is much longer, but it is also much better. All the elements inside the list are equal. If you do something you can just iterate over all elements. The data structure now is also pretty save. Correlated data is all stored together. It is almost impossible to mix up the weight of the apple and the banana. And it’s also pretty hard now to make an error when creating the list.

We can summarize: Lists are very common. They should always contain objects of equal meaning. If you want to make a list with groups of objects you should create a class for these groups and make a list of these class instances. If you want to access a single object from a list, chances are high that your code is bad.

## Enums

Enums are something many software developers don’t know. You don’t need it. But they should know it, as enums make the code much better. There are several different ways to write code without using enums. They are all bad.

```py
# 1. boolean:
is_blue = True

# 2. string:
favorite_color = “blue”

# 3. integer:
favorite_color = 7

# 4. class instance:
class Blue:
	pass

favorite_color = Blue()

# 5. enum:
from enum import Enum
class Color(Enum):
	BLUE = 1

favorite_color = Color::BLUE
```

The first four options all have some severe drawbacks.

The first one is dead ugly. What does `is_blue = False` mean? Is it red? Invisible? Undefined? There are simply too many different options that can confuse the developer. Use booleans cautiously.

The second one looks reasonable but it’s easy to introduce bugs. If you write `“blu”` instead of `“blue”` you have a bug. Without you noticing neither that you have a bug nor where the error comes from. Do never make string comparisons except when parsing a string.

Sometimes such kind of objects are also called “string typed”. Strings are being abused for storing all kind of different data that it shouldn’t be used for.

Third option: 7? A color? No. Please, don’t do this to me. This is an example of a magic number and should be avoided. Unless this is a well-known international color standard. For example the RGB standard, `blue = [0,0,255]`.

Fourth option: For once using types is not the best option. It can be checked using `isinstance(blue, Blue)`, but this is tedious and not possible in C++ for example. For once using classes does not offer any advantages, only drawbacks.

Fifth option: The best solution is certainly using an enum. It looks slightly odd because of the `Color::` prefix and there is no way to change this. However, this code it is really solid and fool proof. If you write `Color::BLU` you will get an error because you quite certainly didn’t define a color `BLU`. You get a compile time error in C++ and a runtime error in python. Both is infinitely better than having a bug. Enums are great. Use them where ever you define a selection from a limited amount of options.

Enums can only be used if you know all possible options when writing the code. If the user can somehow define custom options, you have to use string comparison. Though cases where you really have to make string comparisons are rare.

## Booleans

// stay pragmatic. Once in a while an if statement is not too bad. This is more of a general advice.

“Have a seat my son. There is something very important that I have to tell you. If you hear it for the first time it may be very shocking. But it has to be said: Booleans are evil.”

“What? But … how …? This can’t be. Booleans are only a theoretical construct. It’s everywhere. The whole binary system consists of Booleans. What do you mean?”

“Yes of course you are right. Let me explain. It’s somehow like alcohol. Alcohol does not do any harm if it’s inside a bottle. You can drink it and have a great time, maybe the best time of your life. But at the same time, it can make you cause a car accident, make you start a pub brawl. Humans can’t deal with alcohol. This is why some people say that alcohol is evil. There is a very similar problem with Booleans. Booleans can be used for great things. But at the same time Booleans will make you create bugs. Humans can’t deal with Booleans. They just mix it up way too often. And even worse than Booleans are if statements. But ok, maybe we should not call them evil, but dangerous.”

I may be exaggerating slightly. But it’s true. Humans cannot deal with Booleans and if statements. Accept your faith and learn dealing with it.
-	Good code design leads to few if statements.
-	Resolve if statements as early as possible on the lowest level of abstraction. Don’t pass Booleans as function arguments.
-	Consider using enums instead.
-	Never nest if statements. Having too many levels of indentation are a sign for bad code.
-	Make sure your unit tests cover all branches of if else statements.
-	You can use polymorphism to prevent if statements.
-	Don’t use old-school C++ or java iterators. Looping over iterators requires comparisons. Range-based loops are much safer.
-	Replace switch case iterations by polymorphism. Resolve the conversion from the switch statement to the polymorphic types as soon as possible.

### Switch statements

In case you have a switch statement, you should replace it with polymorphism. The only place where switch statements (or nested if else) is allowed is at the creation of the polymorphic objects.

This is how the code should not look like. Even though it's short and looks neat.
```py
def get_post_code(town_name)
	match town_name:
		case “Zurich”:
			return 8000
		case “Bern”:
			return 3000

get_post_code("Zurich")
```

But as you'll learn in a second, you should never use strings unless you have to. Instead each town should be an object containing a corresponding function. Note that for this simple example at dict would suffice as well.

```py
class Zurich:
	def postcode():
		return 8000
class Bern:
	def postcode():
		return 3000

def cerate_town(town_name):
	match town_name:
		case “Zurich”:
			return Zurich
		case “Bern”:
			return Bern

town = create_town(“Zurich”)
town.postcode()
```

Now this looks all quite verbose but this code will be hidden at a low level of abstraction. `create_town` will be called where you get the `town_name` and then the match case (switch case in most other programming languages) will be resolved once and for all.

A small side remark: In this case, it would be worth having a dict instead of the match case. This would also allow us to read all the town name to post code conversion from a file. // when is it not better to have a dict?

## Strings

“You should never use two different languages in a single file. English is also a language” // ?

After pointers and Booleans, strings are probably the third most dangerous data type. Many programmers check 2 strings for equality. One of them is written in plain text in the code. A twenty-character long string. If a single character is wrong you have a bug and there is no way the computer is able to know and warn you. Of course, you can make this kind of code work. But it is extremely brittle. You should eliminate such risk whenever possible. As we’ve already seen you should always consider using enums if you want to do string comparison.

### Boolean logic

Some people even start to encode all kind of logic into strings. This is dreadful. At times this is also called "stringly typed" to highlight that there should be proper types used instead of strings. // see also "primitive obsession"

This example I found in book Clean Code on p.128 where Robert C. Martin (aka. Uncle Bob) did some refactoring on a unit test. It's a book I can highly recommend. But here Uncle Bob somehow went haywire. What he explained all made sense, but he somehow missed that one should never write code like that. 

He encoded five boolean states `{heater_state, blower_state, cooler_state, hi_temp_alarm, low_temp_alarm}` into a single string `“hbCHl”`, where each of the characters was encoding weather is was too hot or not, too cold or not, etc. Capital letters mean `true`, lower case letters mean `false`. It’s such a beautiful example of what kind of logic can be implemented in strings. At least it would be if it wasn’t that outrageous what he did here. Do never use strings to encode some other king of value. To make matters worse, the letter `“h”` is even used twice. Like this the code becomes extra brittle.

The resulting unit tests Uncle Bob wrote are kind of nice at first sight. But it takes some knowledge to understand what these 5 characters are supposed to mean. Without appropriate background knowledge it is not possible to understand the meaning of this string. And the order of the characters inside this string are somewhat arbitrary.

Now let’s look how we could make things better. We have 5 states that can all be true or false. Writing a list with 5 Booleans is probably the first thought, something like `water_state = [False, False, True, True, False]`. This is better than the string logic, but it still needs some serious reworking. Elements in an array should all be treated equally. But here you will probably need only one element at the time, `needs_hot_water != water_state[0]`. This `[0]` is a clear indication that we should not use an array.

A better solution is using a dataclass that stores 5 different variables. One Boolean replacing each character in the string above.

```py
from dataclasses import dataclass

@dataclass
class WaterState{
	heater_state: bool
	blower_state: bool
	cooler_state: bool
	high_temp_alert: bool
	low_temp_alert: bool
}
```

// do we need this second enum??? I'm not sure anymore if it increases readability.

Still, this is not yet optimal. What does `heater_state = true` or `= false` mean? Let's define an enum instead.

```py
from enum import Enum
from dataclasses import dataclass

class State(Enum):
	on = True # use 1 and 2 instead of True and False?
	off = False

@dataclass
class WaterState:
	heater_state: State
	blower_state: State
	cooler_state: State
	hi_temp_alert: State
	low_temp_alert: State
```

Now the `heater_state` can be `on` or `off`. This is much more intuitive to read.

Once one found this solution it looks so natural. This code is so much more readable than the encoded string that is absolutely worth the additional effort it takes to write this struct and the enum. Remember that we always code for readability and not for fewest lines of code.

The code using this dataclass is super simple. Opposite to the string solution there is no logic, comparison or anything similar required. It is simply obvious how to use it.

```py
if water_state.high_temp_alert == State.On:
	print(“Attention: the water is too hot”)
```

### Natural Language

Serious software products are available in many different countries. They have to be available in many languages. But you don’t want the translator to writen his text into your code nor does the translator want to deal with your code. He wants only the text the user can see. He wants the text in a dedicated text file. There is no arguing with that. Thus it is your job to extract all the human readable text from your code. Instead the code should get all the human readable text from this file. On start-up you read the text file and assign the different pieces to the corresponding variables. Selecting a different language is as little work as selecting a different file. Now, of course, this is in theory.

Ultimately you are left with barely any strings at all. Only when reading or writing a file you briefly have to deal with strings. At least in theory. For small projects it is not always worth the effort.

## Dicts

You run your code and check the values of your variables. In one case you have the first line, in another case you have the second line. When should you use which one?

```py
a = 0
b = 1
```

```py
vars = {‘a’ : 0, ‘b’ : 1}
```

These two lines do something very similar. They both assign the value 0 to a and value 1 to b. Yet there is a fundamental difference. In the first line the programmer knows that he needs variables a and b as he writes the code. In the second case, we have a dynamic data structure. Maybe the programmer knew that there will be ‘a’ and ‘b’ used as keys. Maybe he didn’t and these dict entries were generated by some user input.

If the developer knows all the variables that he needs, he should use normal variables. If they originate from somewhere else, a text file for example, he has to use a dynamic data structure like a dict. At first this may sound all a little confusing. But think about cooking recipes. You might know a few recipes that you define in your code and the name of the recipe is the name of the variable. Or you can write a parser that reads them from a cookbook into a dictionary. Here you have to use some kind of dynamic data structure. A dict is more appropriate than a list as you can use the name of the recipe as a key.

Dict are closely related to json and XML files. Json and XML are pretty much the same as a nested dict converted into a string. If you ever have to read in some json files, the resulting data structure will be nested dict that you might convert further into nested classe instances.

## Trees

It is not too often that I had to create a tree myself, yet I was working on a tree structure for a good part of my programming life. Trees are an extremely important data structure. As soon as you work with a recursive data structure you absolutely have to implement a tree. This allows you to use many standard algorithms that are very efficient. If you implement your own algorithms, make sure they are recursive and write automated tests for the corner cases.

## Pointers

C++ used pointers everywhere. Pointers were used to point to a certain location of your memory and access the corresponding value. Pointers are still used to implement polymorphism. Pointers are by far the most dangerous objects in the programming world. With pointers, pretty much anything can go wrong. Fortunately, they are barely needed these days. Vectors and other modern features have pretty much all functionality implemented that pointers were used for. The only remnant are interfaces where pointers are still needed for technical reasons. Use pointers only there and use the modern smart pointers (unique pointer, shared pointer) and you will be fine. Be happy if you use python and you don’t have to care at all.

# 25. Variable Properties

Once again, things only got stated with the introduction to the data types. The hard part is not choosing a data type, but figuring out how to deal with them. How to make them interact with each other. Here one can easily create a huge mess if things are not considered properly. And even experienced programmers do not always know how to structure them properly. Because it is hard. And I’m trying to explain to you at least some very fundamental ideas to look out for.

The most common way to structure data is having nested classes where one class contains instances of other classes. There’s certainly nothing wrong with that, but sometimes there are better solutions.

// add reference, …? 

Variables do not only have a type, but they can also have additional properties that we want to look at in this chapter. They can be compile-time constant, constant, mutable, member, static, dynamic or global. And possibly many more. All these variables have a different scope in which they can be accessed and altered. As always in programming, it is very convenient when you can access a variable all the time, like a global variable, for instance. At the same time, this is very prone to create bad code. Therefore, you should always choose a variable type that is just modifiable enough to work with but doesn’t give you any more accessibility permissions than that.

## Compile-time constant

Compile-time constants are the least powerful. They are known at the time you write the code and will never change their value. In python there is no way to enforce constness. But it is generally agreed upon that variables written in all upper case are constant and may not be changed, `PI=3.14`. In C++ there is the `const` keyword that enforces constness of a variable. `const double pi=3.14`. Now it is not possible anymore to change the variable `pi` or the compiler returns an error. Keep these constants somewhere separated and don’t clutter your code. Otherwise there is nothing you can do wrong with them.

In C++ there is also the `constexpr` key word to indicate that an expression can be evaluated at compile time.

## Constant

Compared to compile-time constants, constants do not know its values at the time of compilation. They will be assigned at runtime upon creation of the object.

Once created you can pass and copy them around as much as you please. You are always guaranteed to deal with the correct object. You can even make a constant global and not suffer from the main issues of global variables. Though it is still recommended to pass them around as function arguments instead.

## Mutable

In many ways, mutable variables can be compared to class instances. They are both very powerful, yet at the same time they are tricky to deal with as they may change their values. This can easily lead to bugs. On the other hand, writing code without mutable variables (nor class instances) is very hard. If you want to know how hard exactly, try functional programming. The problem of mutable variables is the mutability. They may change their values, even if they are just an argument of a function. This makes keeping track of their value so hard.

One option is to work more with unmutable objects. For example you can replace the following code,

```py
prime_numbers = [11, 3, 7, 5, 2]
prime_numbers.sort()
```

with something that does not change the list. Instead it can return a new list.

```py
prime_numbers = [11, 3, 7, 5, 2]
sorted_prime_numbers = sorted(prime_numbers)
```

It is hard to give a general recommendation to one of these solutions, though the second one does have its merits. There is the rule of thumb that objects should not be reused because it violates partially the SRP. This is partially the case here as the `prime_numbers` list changes its properties. Additionally working with mutable objects is a common source of bugs. Using the second version of the code does not mutate anything. It resembles rather functional programming.

On the other hand, the second solution may be a performance bottle neck as it needs more memory. This may be a problem for large lists.

## Member variables

Member variable is by far the most common property of a variable. Yet there is a lot that can go wrong as well, as member variables are at the same time mutable variables. Most things you have to know are explained in the section on classes. As long as your class design is alright (classes should be small!) and the methods are well designed (no side unexpected side effects), you are mostly fine with using member variables. Though you have to be carefull with them.

Member variables have pretty much the same problem as global variables, just in a somewhat limited scope. This is one reason why classes have to be small. 

Passing output arguments to functions makes the code obscure as well. The best solution would be passing around only immutable variables as done in functional programming. However, it would also be too difficult to code this way. This is how functional programming works, but it is not too wide spread, even though it exists longer than OO programming. OO seems to be in the sweet spot between accessability and privacy of variables and functions. But you always have to be aware of this and make sure you keep the balance and it doesn't tip over to the accessability side. Keep your classes small and make everything privat that can be.

## Static Variables

Static variables are member variables that share the same value over all class instances. Let’s briefly figure out when to use them. 

If a static variable is const, one could also create a free const variable outside the class instead. Except if this is not allowed to do so, as in Java, for instance.

If a static variable is not const, it is probably used to change the value of the variable in all class instances at once. This is dark magic! This is dreadful!! Do never use dark magic. Do never use non-constant static variables. 

And if you don't beleave me, try to write unit tests for a class containing static variables. You won't be able to change the order of the tests because they might break. This is absolutely brittle.

## Dynamic Variables

Dynamic variables are the main reason why I was writing this chapter. With dynamic variables I mean mostly entries of dictionaries. Pseudo variables that can be created at run time. An extremely powerful tool, yet one, that requires some understanding about when to use it. Read chapter Datatypes for more information about dicts.

## Global Variables

You might have heard about global variables. They are bad and you should never use them. This is indeed true. Let me make an everyday example to show you why this is the case. 

Let’s say you have to give a bag to a friend. But you are not able to meet. Now your solution is you place it in the middle of a public square and he can pick it up later on. Are you now thinking ...? No! NO! Don’t even think about it! There is NO WAY this is ever going to work. Everyone around can mess with the integrity of the bag. And they will. Believe me, they certainly will. This is the problem with global variables. Millions have tried this attempt before you, millions have failed. No one found a solution how to safely work with global variables. Do NEVER use global variables. If you think using a global variable is the only way to solve your problems you need someone to review your code and fix some fundamental issues. Using global variables is only going to make things worse.

Of course, it’s slightly different if the bag weights 1000 tons and no one can move it. Not even Superman. Nor your friend. This is not a variable anymore. This is a constant. You define it once and it will never change. But even here it is considered bad practice to make it global. Pass them around as function arguments in order to make the dependencies apparent.

Now as you already realized, global variables are bad because everyone can change their value. You cannot rely on them. You never know if someone messes with its integrity. This makes code also incredibly hard to understand, because the work flow becomes extremely entangled. All of a sudden you have temporal coupling between different function calls if they change this variable. You have to follow every trace where the variable could be changed. This is the very definition of spaghetti code. 

## Variable comparison

// call it differently than effects? Rewrite this section. It's confusing.

I’d like to briefly sort different kind of variables by the amount of effects they may have, starting with the least side effects. Having many effects of course makes it easier to program as you can do pretty much wahtever you want, but at the same time makes it extremely hard to keep everything under control. It’s best to choose variables with the least possible effects that let's you still implement what you want.

Here is a rough list how variable types are sorted by the amount of effects they have, starting with the least.

Immutable object < mutable object < class variable < inherited variable < singleton < global variable

There is certainly nothing wrong with immutable objects. We just can’t do it without them. It's just that they can't do much. They are just there and do nothing. They can only be used within the current scope and when passed as a function argument their value can't be changed. If you like working only with immutable objects, I can recommend you functional programming.

With mutable objects you have to be careful because it may be unexpected that a function call changes the value of an argument. Make sure you only change the first argument of a function call, otherwise things can become very confusing. This is no strict law, but more of a convention. Changing more than one argument by a function call is also a violation of the SRP and should be avoided.

Class variables are already quite tricky to deal with. There are just too many ways they can mess up the work flow and cause side effects. They may be used, of course, but I give some lengthy explanations in the chapter on classes, what things have to be considered to prevent you from causing chaos. Class variables and mutable objects both offer the option of changing an object. At the same time, this is also exactly the reason why they are hard to deal with. Furthermore, class variables are accessible in a potentially much bigger scope, within the whole class. This is fine for small classes, but one of the reasons why classes should not be too big.

Inherited variables are even worse than class variables. You don’t see at first sight where an inherited variable is defined. It’s like getting a couple of tools and you don’t know where they come from nor where they belong to. Compared to composition giving you one ordered tool box to deal with. Thus, inherited variables make the code strictly harder to understand. And there’s no apparent reason why one should use inheritance. And no, the few words saved are no reason. Number of words used is not a merit for the quality of code. Readability is. And readability is certainly better with composition than with inheritance. This is certainly one of the reasons why it's better not to use inheritance at all.

// why not to use the singleton: 97-things-every-programmer-should-know chapter 73

A Singleton is a class that can have at most one instance. If you create objects of this class in several locations, they all share the same class instance. There are very few cases where singletons are really useful. This is mostly the case for connections. It allows several pieces of your code to share the same connection to your database, webserver, mobile phone, etc. If you have few communication calls and few relatively big data sets this is not required. You wouldn’t gain much with the singleton pattern. Every class or library can connect to the database if it needs some data and disconnect in the end. However singletons are commonly abused to act as a global variable. And this is really bad. For this reason it is generally discouraged to use singletons. // performance??

Long story short: Never use global variables, not even global constants. Use singletons only for connections if setting up a new connection may be costly. And I recommend not to use inherited variables.

With mutable and class variables one has to always pay attention. Especially with bad code these variables may further add to the general confusion.

Immutable variables are always safe to use, yet at the same time they are not always that useful as their capabilities are fairly limited.



//where to move this text here? Somewhere to class functions? Or remove it completely?

Sometimes the member function thoughts even work in unexpected places. Let’s say you have the following Java code //example from working effectively with legacy code, p. 273

```Java
outputstream.write("header"); 
writeField(outputstream, body);

void writeField(Outputstream outputStream, Sting field){
    outputstream.write(field.getBytes());
    outputstream.write(0x00);
}
```

where outputstream is a built-in object in Java, thus we can’t add any member functions. Write takes a string and writes it to the output. For the bodies, the string has to be modified.

Here Feathers could have modified the string within its own function and keep the code much more readable.

```Java
outputstream.write("header"); 
outputstream.write(field(body))

string field(body){
    return (body + '0').getBytes();
}
```

Now this is just a little example in between how constantly considering how functions can be defined in different ways might make the code smoother. It is more readable and we don’t have to pass the mutable outputstream object.


# 26. Naming

"And you will know, my name is the Lord!” – Samel L. Jackson, Pulp fiction

How long does a football game take? This is a very inocent looking question, yet people might not agree to an answer. In Europe most people would say 90 minutes while in the United States, 60 minutes is the common answer. The reason for these different answers is very simple: names. There are two different sports that have the same name. This might cause some confusion.

The example was cute. You may get a laugh when mixing them up but it doesn’t cause any harm. With city names it already gets a little trickier. If you miss a job interview because you drove to the wrong end of your country it gets painful. For the police and health care system it becomes even worse. As soon as there are other people around who have the same name as you do it may get dangerous. If your namesake is a highly dangerous criminal, the cops may become really rough because they are confused. Even in Europe. Also in a hospital there are issues with using names as an identifier and so far there is no unique solution how to solve it.

All these things happen for only one reason. Name collisions. Different objects having the same name. Names are everything. No matter what you look at, you can name it. A computer, desk, printer, etc. This is the very foundation of our natural language. Of every language. Including programming languages. In a programming language we define things by giving them a name. Every variable, function or class has a name.

Choosing good names is paramount in programming. You certainly don’t want to run into name collisions as explained above. It would cause a lot of confusion and could be the source for many errors to come. But there is much more to consider when defining the name of an object. We are humans and we have to be able to read and understand the code. This would not be possible if we used randomly generated names. We need names that give us an idea what an object is and what properties it has. This is the only way we can create a picture in our mind what the code roughly does. It requires everyone working on the project to know what all these expressions mean. What kind of properties they have? We have to be like lawyers. The law defines every crime as exactly as possible and gives it a unique name. This is what we need.

Coming up with your own names is everything but easy. Especially new programmers really struggle finding good names. There are just too many possibilities how you can name an object. But there are some rules you can follow and at least some of the names are quite easy to find. Meanwhile for other variables even experienced programmers have to take a deep think. In fact, naming takes up a quite big fraction of our programming time. We do it very often and there is often no obvious solution, there might be only some vague recommendations. Or as Michael Feathers put it in his book "Working Effectively with Legacy Code":

“When naming a class, think about the methods that will eventually reside in. The name should be good, but it doesn’t have to be perfect.” Feathers p.340 

Here are some rules to follow when naming things:

1.	Names should be short yet clear. There is a constant trade-off on the length of a name. Short names may be unclear, yet long names may be a sign that the object is hard to describe. It should possibly be reworked. On the other hand, long names are not as bad as unclear names. When in doubt choose a longer name.
2.	Classes and functions obeying the single responsibility principle are comparably easy to name. Vice versa, if it’s hard to find a good name, reconsider whether the object follows the SRP and consider rewriting it accordingly.
3.	Never use plain values in your code. Always create a variable instead. Plain values are called magic numbers because no one can tell what its meaning is. And magic is having a negative meaning here. `Set_color(7)`. What does `7` mean?
4.	High level objects have short names as they describe very general things. Low level objects have long names as they are very specific.
5.	Well defined levels of abstraction result in clearly defined and unique properties. This helps finding a name. At the same time, functions and classes are required to be on a single level of abstraction in order to fulfill the SRP.
6.	Name collisions may happen once in a while. Consider refactoring one or both variables. They might do very similar things and should be refactored into one object. Otherwise you should be able to find clearly distinguishable names.
7.	Name collisions between different libraries are common and nothing to worry about. Use the namespace prefixes to distinguish them.
8.	Use names from the domain model if possible. Make sure your object in the code and the real object have very similar properties. You should be able to talk to a domain expert about the code and he should be understanding at least some of your problems. If he doesn’t understand you, you probably came up with names or a model that does not exist in reality.
9.	Objects have names that are simple to distinguish. Use normal English words everybody knows and don’t use abbreviations unless you use them in your spoke language. Differences in the names should be as early as possible.
10.	You may tweak the language a little and ignore grammar rules at times. If you have many fish, you may call them fishs or fishes to highlight the plural. Being able to understand the meaning of the code is importanter than the usage of proper English. Natural languages have some deficiencies when it comes to explaining things in an unambiguous way.
11.	Avoid “if”, “and” or “or” in the names of your variables. These neat little words are tempting to use, yet they are a clear sign to a violation of the SRP.
12.	If a variable is used all over the code, name it carefully. Possibly use a name from the domain level. If a variable is used only for about 5 lines, even i, j or k are fine.
13.	The name of a function should tell you exactly what it does. There shouldn’t be unexpected behavior hidden in the code. For example, it shouldn’t interact with global states, which is anyway a bad thing to do.
14.	snake_case notation is easier to read than camelCase. Use snake_case notation for variables and functions, camelCase for class definitions and file names. Though it is more important to stick to the rules used in an ongoing project than comming up with your own notation rules.

## Copilot

Naming is one of the hardest tasks in programming and Copilot is a great help. One thing one can do is writing some code and then let copilot find appropriate names for you.
```py
def print_states(states): 
    for a in states:
        print(a)
```
Here `a` is clearly not an appropriate name. Writing a comment to copilot to search for a better name works out pretty well.
```py
	for a in states:
    # find a better name for this variable
```
Though Copilot needs some help to get started and I had to write the beginning `for` in order to get the following suggestion:
```py
	for state in states:
    	print(state)
```
This is pretty much what was expected. The same works out for function names as well.
```py
def some_fancy_function_name(b,c):
    return b+c
```
```py
# suggest a better function name
def add(b,c):
    return b+c
```


## Exercise

Try to find better names for the following code:
// get the bowling code from clean craftsman?

# 28. Complexity

“I choose a lazy person to do a hard job. Because a lazy person will find an easy way to do it.” – Bill Gates

## Complexity of code

As we are writing software, we have to deal with two different complexities. The complexity of the problem we want to solve and the complexity of your code. As the code covers all the features of the real problem, the complexity of the code will always be at least as high as the complexity of the actual problem. This also becomes apparent as one product manager creates more than enough work for several programmers.

The goal of the software is to keep the complexity as low as possible. Close to the complexity of the real problem. If possible equal to the real problem. It should mimic the real problem 1 to 1. Unfortunately, this will never happen. There is always some overhead when programming. Not only boiler plate code, but there is also conceptual overhead. How should you map a real problem 1 to 1 into code? How should, say, an apple ever become code? This is where object-oriented programming came up. It claimed to be the natural representation of things. Because you could write a class `Apple` and this would solve all our problems. But it did not. We still don’t know how this apple should interact with all other objects in our code. We don’t even know how this apple class should really look like!

I cannot deny that OO programming makes some things easier and having an `Apple` class is a good start. But it doesn’t explain all the logic to you. You have to figure it out yourself. You have to try and explain what the apple really does. Maybe even write it down. Talk to other people, experts. It takes time to build up that knowledge what is important and how everything is connected. This is a fundamental requirement for writing good code with little complexity.

As a next step, you have to get an idea how you can convert all this knowledge into code. Take all the objects involved and connect them in different ways. Change the order of statements and how data is passed between the objects. When done correctly, you’ll end up with code that resembles very much the explanation of the experts in the domain. The objects have the same properties, the functions do the same things and you use the same names. Your code feels like a 1 to 1 mapping of the real problem. Eric Evans called this a domain model [Domain-driven design book]. Handle it with care. The domain model is very precious and you can easily destroy it by adding code that doesn’t fit into the model.

Having a domain model is a great asset. It forces you to understand the problem really well and write the core of your code first. At the same time, it prevents you from getting lost in low level details at the beginning of the development.

## Estimating complexity

Estimating complexity of a task is extremely difficult. Not only from a technical point of view, but also due to pressure from management.

Project Manager: Can you give me an estimate of the time necessary to develop feature xyz?

Programmer: One month.

Project Manager: That's far too long! We've only got one week.

Programmer: I need at least three.

Project Manager: I can give you two at most.

Programmer: Deal!

// source https://github.com/97-things/97-things-every-programmer-should-know/tree/master/en/thing_50

In many cases the complexity of a task is extremely hard to estimate. Some developers might have an idea what to do, others don’t. But nobody really knows exactly. And everyone is a little bit scared of that task. Nobody knows for sure how to break the complete problem down into smaller pieces. Yes, the conditions for this case were deliberately chosen to be rough. Such that you are forced to rethink everything you did so far. 

Probably everyone could have come up with a neat solution for solving the problem, but not with the existing code base. Instead you have to consider what you really need and what parts are already implemented in the code. This case is extremely common. Pretty much everything was already implemented in the code, but nobody saw it. For many tickets it is very clear where and how to write the code. But in the other cases you really have to take your problem and the code into pieces and consider if these things can be sorted differently. Sometimes you find a very simple solution. // rewrite this section, it doesn’t make sense. add example?

## Single line complexity

A frequent topic is the amount of logic in a single line of code. There are very different opinions. On one side we have Linus Thorwalds. In the Linux kernel the maximum line length is 80 characters, using the C programming language. It is absolutely impossible to write more than one or maybe two operations on a single line of code. Try it yourself. It is really worth wirting such code once in a while. You will learn quite something about how code can look like.

On the other end of the spectrum are some python programmers. It seems like adding as much logic as possible on a single line would be a sport. Very honestly, I think this is a pretty bad habit. You don’t gain anything by saving lines of code. At the same time every single line becomes increasingly convoluted. You won’t understand it anymore. And it's thus banned by the google style guide. // https://google.github.io/styleguide/pyguide.html section 2.7

Now this is still one of the more readable inline list initializations. But it is banned by the google style guide as it contains two variables.

```py
[[[0] * (i + j) for i in range(2)] for j in range(3)]
```

## Back magic code

Your code will contain some complexity. There’s no doubt about it. The only question is how to deal with it. One point is that you have to be honest. Some programmers try to hide complex code using all kind of black magic. This may work at times, but the code will be cursed. You can keep working on the code, but once in a while you see this black magic and you’ll become petrified. Your only thought will be: “I hope I’ll never have to touch this.”

It is much better to be honest. The problem is complex and we break down the complexity until we have some pieces that we can solve. Do not hide the complexity, make it apparent.


# 29. Data files

There are several file formats to save data or use them as an interface. A lot of people apparently don’t even know the most important once of them so I would like to give you a very short introduction.

The file formats that I used so far are CSV, json, XML, hdf5 and databases. Along with some custom file formats.

## CSV
// move the code examples into an exercise?

Comma Spaced Values (CSV) is probably the simplest file format. You save numbers and separate them by commas or whatever other character you feel like. But this is also one of the weaknesses of CSV. In some (natural) languages, the comma character is used for the floating point separator (exact name??). Thus you cannot use comma for separating different values as well. This overload of the comma character would cause serious problems.

CSV is no file standard so you can do anything you want. And that’s at the same time the down side of it. People do whatever they want and for every file you have to write a new bit of code to read out the data. Saving auxiliary data is pretty much impossible in CSV files. CSV saves only plain, unstructured lists.

Long story short: CSV is the file format everyone uses who doesn’t know anything better.

Here is some example code how to read a CSV file:

```py
def read_csv(filename):
    with open(filename) as file:
        x = []
        y = []
        for line in file:
            if line.startswith("#"):
                continue
			variables = line.split(",")
            x.append(float(variables[0]))
            y.append(float(variables[1]))
    return (x, y)
```

### Copilot

Copilot seems to be getting along with csv files quite well. Though I would have expected the data to be saved in columns instead of rows. But as I already said, there is no real standard for CSV files, thus such things have to be specified to Copilot.
```py
x = [1,2,3,4]
y = [5,6,7,8]
# write x and y to a csv file called 'data.csv'
```
This prompts the following code:
```py
import csv
with open('data.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(x)
    writer.writerow(y)
```

## Json

The JavaScript Object Notation (json) file format is clearly the best file format for everyday purposes. It is very simple to use. It can save any data structure you want and is extremely wide spread and thus supported. There are libraries to automate the parsing of json files for all major programming languages. The output data structure is a mixture of nested maps and arrays. It won’t get any easier to read a file into data.

Once you use json on a more serious project, you might want to use a schema to check the files for correctness. You may use different schemas for different versions of your interface. And before I let you write schemas by hand, there are tools around to do it. You only have to make sure your json file contains all possible fields in order to get a complete schema.

Thanks to schemas, json is also a meta language. It is possible to define a general pattern of how the json file should look like. This defines a standard which enables easy file exchange between different projects.

The following code creates a json file:
```py
import json

def write_json(filename, data):
    with open(filename, 'w') as f:
        f.write(json.dumps(data, indent=4))

if __name__ == "__main__":
    data = {'x': [1,2,3], 'y':[4,5,6]}
    write_json("temp.json", data)
```

Meanwhile this code here reads out the data.
```py
import json

def read_json(filename):
    with open(filename) as f:
        return json.load(f)

if __name__ == "__main__":
	data = read_json("temp.json")
    print(data['x']) # prints [1,2,3]
    print(data['y']) # prints [4,5,6]
```
As you can see, working with json files is much easier and less error prone than working with CSV files. The underlying data structure is a dict, which is a pretty bullet proof way to work with data. There is hardly a way to introduce unnoticed bugs.

### Copilot
Reading and writing json files using Copilot works out pretty well. Upon writing the following code
```py
a = [1,2,3]
b = [4,5,6]
# write a and b to a json file called 'data.json'
```
Copilot makes the following suggestion:
```py
import json
with open('data.json', 'w') as f:
    json.dump({'a':a, 'b':b}, f)
```
Also when reading a json file, the suggesiton of Copilot is quite sound. Following the comment
```py
# read the json file into a and b
```
Copilot makes the following suggestion:
```py
with open('data.json', 'r') as f:
    data = json.load(f)
    a = data['a']
    b = data['b']
```
Thus one can say that Copilot allows us to save some time writing code and saving brain memory when working with json files.

## XML

The eXtensible Markup Language (XML) is very similar to json. It’s a bit older than json and it doesn’t support arrays as nicely as json. Otherwise there are only minor differences between the two formats. One thing people might miss in json is the possibility to add comments. On the other hand, json is generally considered to be more easily readable. Other than that, there are only minor diffirences like the XML supporting comments and namespaces.

Generally I prefer json over XML. If I have to read out an XML file, I use tools that convert the data structure into the json object and work with it the way I’m used to. Like this I don't have to learn something new.

The following code converts an XML file into a json object:
```py
import json
import xmltodict

with open("data.xml") as xml_file:
    data_dict = xmltodict.parse(xml_file.read())
    json_data = json.dumps(data_dict)
```
Writing XML files is rather tedious as well. Here I recommend as well to work with json data and convert it to XML just before writing.
```py
import json
import xmltodict
json_string="""{"employee": {"name": "John Doe", "age": "35", "job": {"title": "Software Engineer"}}}
"""
python_dict=json.loads(json_string)
with open("person.xml", 'w') as file:
	xmltodict.unparse(python_dict, output=file)
```

### Copilot
Copilot struggles a lot when dealing with XML files. It seems as if it didn't know the xml libraries that would simplify it's life. Instead it assembles strings into an XML file by itself which results in very brittle code that is very hard to read.
```py
x = [1,2,3]
y = [4,5,6]
# write x and y to an xml file called 'data.xml'
```
This code worked out without any problems for json files, but for XML the result at the time of writing was dissatisfactory. The suggestion of Copilot is:
```py
with open('data.xml', 'w') as f:
    f.write('<data>\n')
    for i in range(len(x)):
        f.write(f'\t<x>{x[i]}</x>\n')
        f.write(f'\t<y>{y[i]}</y>\n')
    f.write('</data>')
```
Now this does the job, but this is certainly now how an XML file is supposed to be created. Reading XML files is even worse.
```py
x = []
y = []
# read the xml file into x and y
```
The code Copilot suggests is extremely brittle and doesn't even work in my case. Somehow Copilot doesn't seem to know about XML libraries that would simplify its life a lot.
```py
with open('data.xml', 'r') as f:
    for line in f:
        if '<x>' in line:
            x.append(int(line[3:-5]))
        elif '<y>' in line:
            y.append(int(line[3:-5]))
```

## TOML


## YAML


## HDF5

HDF5 is the most common binary file format. It is designed to deal with terabytes of data and optimized for high throughput. Pretty much all research facilities and companies dealing with huge amounts of data use this file format. It supports structured and auxiliary data. For looking at the data you either have to use the HDF5 library in your programming language of choice or download the free GUI software. Use HDF5 if you want to save several gigabytes of numeric data.

Working with HDF5 is in my opinion a tad less intuitive as working with json files. This is because HDF5 uses datasets that have to be created instead of just accepting a dict.

The following code saves a list of values inside an HDF5 file.

```py
import h5py

with h5py.File("temp.hdf5", "w") as f:
    dset = f.create_dataset("x", data=[1, 2, 3])
```

Reading a file returns an HDF5 file object. It may be a little intimidating at first, but it is fairly easy to work with. With many respects, it behaves similar to a dictionary.
```py
import h5py

with h5py.File('temp.hdf5', 'r') as f:
    print(list(f.keys()))
    print(list(f['x']))

```

As HDF5 is a binary format you cannot look at the data using a text editor. Instead you have to use the HDFview software, https://www.hdfgroup.org/downloads/hdfview/

### Copilot

Copilot seems to be getting along quite well with HDF5. On the following code snippet:
```py
x = [1,2,3,4]
# write x to an hdf5 file called 'data.hdf5'
```
Copilot correctly complements it to
```py
with h5py.File('data.hdf5', 'w') as f:
    f.create_dataset('x', data=x)
```
Also reading out data from an HDF5 file is no problem.
```py
# read the hdf5 file into x
```
```py
with h5py.File('data.hdf5', 'r') as f:
    x = list(f['x'])
```

## Databases

Databases (DB) are used for big amount of data that you want to analyze but doesn’t fit into memory. Databases have a whole lot of different functionality that improves searching and manipulating data within the database. There are several vendors and different technologies. 

I never really cared much about DBs and I'd like to teach you other things instead. So you better get your information elsewhere. I only know that proprietary DBs can be extremely expensive and it’s important to write your code such that you can easily replace the DB by another one, or you’ll be stuck paying hefty annual fees.

## Custom file format

Similar to the CSV file you can also define your own file format for other things than only numbers. You can define your own file with structured data. You can even define your own programming language like structured text within your custom file format. You can do pretty much anything in your like. You are a free person. Just don’t expect to be paid for such a waste of time. If you want to be a serious software engineer you have to gain value for the customer. You have to use json or write a library for a normal programming language. There’s no reason to define custom file formats.

## Exercise

// Create an exercise where the user has to save some data by himself and remove the examples in the code? But somehow I don't like removing the examples in the code.

# 30. Setting up a project

"If it's your job to eat a frog, it's best to do it in the morning. And If it's your job to eat two frogs, it's best to eat the biggest one first.", Mark Twain

// https://youtu.be/LfIPVIsH4ZU

Many students start with writing code when they have some task to do. And they postpone the whole infrastructure work for as long as they can. They keep compiling code with the command line for as long as they can. They don't use git. And they certainly don't use a Continuous Integration (CI) tool. This is dreadful. Set up these things right at the beginning of the project. 

Yes, it will take some time to get started. And yes, it's a painful process if you are not used to it. But it is worth it. The very first reason why it is worth it is DRY. If you have to type in the compilation command to the terminal over and over again, you are repeating yourself time and time again. This is going to slow down the development process. This is way worse than spending the same amount of time at the beginning of the process because it interrupts your thoughts.

For small projects, setting up git and a proper build tool need barely any time. Already after the first time introducing some hard to track down bug you'll be glad having version control and being able to simply revert your last changes. Same for the build process. Typing in a long command not only takes time, it is also brittle. It is too easy to make a typo and screw up the build process in some unforseen way that introduces hard to understand behavior.

Similarly for CI. It will take some time setting it up. But you will save a lot of time later on because you can be sure that the tests you wrote (and I really hope you have tests) always run. The code commited to master has been compiled and the tests pass without any errors.

So yes, setting up the infrastructure of a project may need some time. But it is certainly time well spent. There are so many advantages having a properly set up infrastructure:
- You anyway have to learn how to use git, cmake and all the other tools. So it's good practice to get started with them as soon as possible.
- You will save a lot of time down the road. This will outweight the time needed now to set everything up.
- Having properly set up tools makes it easier for new team members to get started. They only have to clone the repo and run the build tool and they can get started.

## Project folder
// Add a plot with the folder structure

Code is a collection of text files. One question is: how do you deal with them?

The very first thing is the length of each file. Try to keep them short. About 100 lines per file would be great, a few hundred are kind of acceptable. Having many fairly small files improves the overview. Generally, one file contains either a class or a bunch of similar functions. Classes that have more than 1000 lines should have been broken into pieces a long time ago. For this reason, files should never have more than 1000 lines. In fact, files should usually be much smaller than this.

The way to arrange the files in folders depends on the programming language. The code is located inside the src folder, sorted by further subfolders if necessary. Generally, each subfolder corresponds to a library of the project. Make sure there is only your own code and, depending on the programming language, your tests in there. Nothing else. Do never ever allow any auto generated files inside of the src folder. Or at least make sure they all get cleaned up immediately. Auto generated files should never make it into the master branch!

Generated files generally belong into the build folder. Like this cleaning up the build is quite simple. Just delete the folder and all build files are gone. It also makes version control fairly simple. Add the build folder to the .gitignore file to make sure that generated files never make it into the version control.

Acceptance tests should also remain outside of the src folder as these tests are quite independent of the code. They only use the public API. I would keep them in a separate folder next to src, usually within the same git project. You may also have them outside of the repository or even hand over the responsibility to the sales team if everyone agrees.

The path where the unit tests reside differs, depending on the programming language. There are languages where the unit tests are in a separate folder alongside the src and acceptance tests, for example in C++. In other languages, as python for example, the unit tests are written right next to the corresponding source file. This is necessary as in python it's very tedious to import files from a parent folder.

3rd party libraries belong into the lib folder. They are not part of the git project. They are too big and none of your business. You need some other way to manage them. If you use few libraries just manage them manually. In python use pip and the requirements.txt file.

There are some additional files in a project.

1.	Custom scripts for installation and build of the project. Getting the project, downloading the 3rd party libraries, building it and running the tests should all require only one single command.
1.	The readme.md file shown on the front page of the git project. It usually contains installation instructions and a short description of the project.
1.	.gitignore is related with git. It lists all files and folders to be ignored by git. For example, auto generated files or files too big to be managed by git.
1.	Some formatting, code quality checking and other files.

There are a few pitfalls how to arrange the files and folder of your project. But as long as you follow the general best advice you should be fine. Consult the wisdom of the internet for your programming language.

## Exercise

Figure out what kind of hidden files (starting with a `.`) your toools support and what is their purpose.

// git: .gitinore
// various .env
// ...


# 31. Performance Optimization

“Premature optimization is the root of all evil” - Donald Knuth

One of the most overestimated topics in programming is performance. This has historic reasons. Computers used to be extremely slow and expensive. Thus, it was worth spending a lot of time improving every bit of your algorithm. Back in the days, low level languages like Fortran or even Assembler allowed you to do so. But the performance of computers had been growing exponentially for the last 50 years while the prices dropped as well. Modern programming languages like python are not focusing on performance anymore. But rather on usability. Simply because it is more important to write readable code, rather than fast code.

As we have learned the main goals of a software engineer are creating value for the customer, writing code that is easy to understand, correct and well covered with tests. Performance is not a main goal. It is hardly ever an issue if the code is not optimized for performance. Hardly anyone cares about optimization anymore.

Let’s say you start writing one of the few applications that you assume needs performance. You’re a bit lost at which point in time you should start optimizing the code. Right from the beginning? Should you plan your algorithms such that they will be faster? How should you proceed?

First of all, it is not recommended to optimize the code at all. In fact, it is best to ignore the performance topic for the time being. Write your code with the usual test – code – refactor work cycles. The result will be code that is, at least in theory, modular, stable, easy to understand and well tested. Code that meets all your requirements, except for performance. 

Is this really the case, that performance was an issue? You had this feeling that you had to write highly optimized code. But you didn’t know for sure. And now is the time to test your assumption. If you have to run your code only once and it takes 2 days, run it over the weekend. Spending hours for optimization would be wasted time.

If your code takes an hour to run and you use it every day it is worth getting a profiler to check the bottle necks of your code. Pretty much all code that you’ll ever see has very few bottle necks. Usually it’s some fancy calculation on a huge data structure that scales worse than O(N\*log(N)). This is going to be the one and only point where you’ll have to optimize. As you have written great code, it is very easy to find this bottle neck using a profiler. For example, it turns out to be custom written Fourier transformation operating on a list with 10’000 elements. So, as you start reading through that code, you realize that the algorithm you have implemented scales with N^2. Such bad scaling is usually inacceptable. You ask the internet for advice. You find Fourier transform libraries that scale with N*log(N). As your code is well structured you can just remove your own Fourier transform function call, tweak your data structure a little and use the library you found. Now your code runs within seconds. Done. 

Finally, there are indeed some cases where you have to plan the software from scratch and focus on optimization. But these are very rare. These are mostly simulation software, games, websites containing a lot of data, or infrastructure code for huge server farms where not only performance but also energy consumption it a major concern. If the code can be parallelized it will become much more complicated as this is an additional complexity when designing data structures and algorithms. As a very rough rule of thumb, it takes twice the amount of time to write parallel code compared to linear code. There is a lot to learn if you want to write high performance code. But you won’t be alone. You’ll be working in a team where every single team member knows way more about parallel programming than I do.

There are many small things you can do for optimizing your code like manual loop unrolling. Keep your hands away! The performance gains are negligible. And if you are working with a compiled language, the compiler can optimize such things much better than you do. Only improve major algorithms. Especially those that scale better.

## Exercise

// Take code with one or two slow algorithms. The user should use the profiler to find the bottle necks and then improve the performance.

// The user should write a pairlist algorithm (or FFT or something else) and in a second step write a more optimized version.

# 32. Comments

"Code is like humor. When you have to explain it, it’s bad." – Cory House

Comments are a very double-edged sword. While they may be useful at times, they are also a liability. You always have to make sure you keep them up to date as you have to any piece of documentation. Additionally comments tend to be a remedy to fix bad code. And this is certainly not what comments are supposed to do.

## Bad comments

“Comments? Don’t.”

“Why?”

```py
def add(a,b):
	# This function returns the sum of the two arguments
	return a + b
```

Of course, I exaggerated in this example. I just wanted to make a point. But there are programmers who think that this comment here is justified. 

I do not share this opinion at all. In my opinion this comment is just useless. Read the function name. It explains exactly what the function does. And if you are not sure take a look at the implementation. This is exactly what makes code good. You read a function name and you know what it does. Good code is self-documenting. There is barely any need for additional comments. This comment here is a violation of the SRP.

“Yes, but it’s only one line of comment. It can’t hurt us.”, you might say. 

“NO!”

Sorry, I just lost my temper. I shouldn’t be so harsh with you. Many experienced programmers don’t know, so why should you? I have to tell you that you are wrong. You can’t believe how wrong you are. Maybe I haven’t made myself clear enough before. This comment is an absolutely useless liability. It claims something that will not always be true. The code will change as code always does. But the comment may be forgotten. Unlike function definitions, you can’t enforce that a comment stays at its correct location. You will end up having a comment that is plain wrong. It will confuse everyone who works on this code. It will cause bugs.

Not convinced? You think you won’t have these issues because you work carefully? 

“Ha ha. NO!“

Now you’re certainly wrong this time. By now you should know better. This is exactly what I’m trying to teach you throughout this book. You are human. Every human makes mistakes. I make mistakes, you make mistakes. It’s inevitable. Accept your faith and deal with it. Code is good if you can make only few mistakes. Removing useless comments is a must. They are an unnecesary source for bugs.

You want to become a software engineer. So stop using the English language and start reading code instead. The code contains the absolute truth. Not the comment.

### Commented out code

Another thing you might have seem somewhere is commented out code. Someone was developing a feature. Maybe he was replacing some code and wasn’t sure how to implement the new version. So, he commented out the old code and started implementing. He somehow didn’t understand all the details but at some point, everything seemed to work. He knew that he was more guessing that writing structured code. He knew his work was really bad. Therefore, he decided to leave the old code in the repo and just commented it out, right beside the new code.

Commenting out code is absolutely dreadful. This is one of the candidates for the worst programming practices. What are you supposed to do with commented out code? Everybody reads it. Nobody knows how to deal with it. It’s just causing confusion and wastes everybody’s time. If we only had a tool to browse the history of the code... Something like git...

Never use comments (or dead code) for that purpose. You have my permission to delete any commented-out code that you ever see. You may show this book as a proof if needed.

### TODO comments

Another bad habit is TODO comments. When you implement a feature, you are responsible that the implementation is ready to be merged into master. It’s ready to be merged when there is nothing important to be done anymore that would justify a TODO comment. Make sure you never merge any TODOs into master. They only cause confusion and there is never time to do them. You will never implement a feature without ticket and for refactoring you don’t need a TODO as a justification. Therefore again: make sure you never merge any TODO comments into master.

At the same time it is fine if you use TODO comments during the development of a feature. It might help you to organize your work. Just make sure to remove all the TODO comments before merging your changes into master.

## Useful comments

So much about why not to use comments. Now let’s talk about the cases where using comments is fully legitimate.

I have explained that you should not use comments for anything that could (or should) be explained by the code itself. Vice versa this means that comments are allowed to explain things you cannot express in code. For example, you can add links to the source of a code fragment, library or the explanation of an algorithm. It may also be useful to use comments on the interface of a library or API used be the documentation software. And of course comments are used at the beginning of the file for the boilerplate copyright statement.

### Docstring

You may use docstring tools, like sphynx in python, for automatically generated documentation. However, docstrings should only be used as an external documentation. Never use docstrings for internal purpose. Why should you read a docstring docummentation if you can read the source code and all its comments?

#should I add some more points when comments are allowed?

## Summary

Use comments only for things that cannot be made apparent by the code itself, yet you think it’s still very important.

## Copilot

Copilot is not yet able to write really useful comments. The following comment was created by the document function of Copilot Labs.

```py
def roman_number(number):
    # The roman_map dictionary is a lookup table that maps numbers to
    # roman numerals. It is used by the to_roman function to convert
    # numbers into roman numerals.
    roman_map = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X'}
    roman = ''
    for key in sorted(roman_map.keys(), reverse=True):
        while number >= key:
            roman += roman_map[key]
            number -= key
    return roman
```

## Exercises

// Create some code with comments and ask the user how to improve it.
// take them from clean code?

# 33. Logging

The basic idea of logging is to have a feedback what kind of steps your software executed. It might help you finding bugs. Now this sounds great, but in reality, there are several things to consider.

The most obvious drawback is that logging needs time to be implemented. It’s not a huge amount, yet it may add up.

Logging is usually not needed. Most code is deterministic. You run the same code twice it will do the exact same thing, down to some rounding errors. You don’t need the logs. Run the code with the same settings as the user did and inspect your code using a debugger.

If you struggle finding your bugs, you should rather improve the quality of your code. Simplify its structure and write unit tests. You will have less bugs and they are easier to find.

At the same time there are some cases where you can consider using a logger.

For non-deterministic software it may be useful. For example, if you have several programs that communicate asynchronously with each other, as in microservices. All kind of conditions may occur that you didn’t think of. Depending on the temporal order of the messages being sent. A logger may help you to trace back the source of a bug.

In a GUI the logger could store all the actions performed by the user. This may also be helpful if the user finds a bug.

And finally, a logger may be helpful for the user to send in auto created error reports if something went wrong. He can just click a button to send in an error report with all relevant data and doesn’t have to bother writing such a report by himself. This may be very useful as errors are almost inevitable and the users are a very helpful group to test your software. As long as the bugs are not too subtle or too serious.

## Exercises



# 34. Tools

There is a fair amount of software that is supposed to help you writing more or better software. Here is a short list of the most important classes of tools I worked with so far:

Version control software (VCS), Command line, Continuous Integration (CI), Integrated Development Editor (IDE), debugger, profiler, formatter, code quality checker, ticketing system, Wiki, pip (python), build tools, docstring, docker and possibly many more.

I have to admit that the list is pretty scrambled. We have some specific software products but also software types. This is because for some problems almost all software companies use the same product while for other tasks you can choose between a broad range of products. In most cases it is best to use what your work colleagues use as well. Then they can help you out if you are stuck somewhere.

## Version control software 

Git is certainly the very first program to mention here. Git is everywhere. It’s the Version Control Software (VCS) that Linus Thorwalds programmed because all the alternatives were too slow for managing the Linux kernel or had other drawbacks like bugs or licencins issues // citation wikepedia?. Git is clearly superior to most other version control software and there is no reason to learn anything else. Git is a de facto industry standard.

The original Git software is a console application but there is also proprietary software with a GUI.

I recommend learning the classic (command line) git. Start learning it as soon as possible. Every programmer has to be able to work with it. The only difference between companies is the way how they use git exactly.

### Git, everywhere git

Git should not only be used for bare code. Git can also be used on any text file that you have. The build files should certainly be version controlled. But also other pure text files are worth controlling with git. For example if you do research and have some files with measurement results. This could also be version controlled. The price you pay is negligible compared to what you gain by controlling all your files with git.

Or if you wirte a book like this one. It is writen in Markdown and version controlled with git. This makes it easy to cooperate with reviewers and at the same time I always have a safety net when I screwed up some of my text.

### Copilot

// is here the location to write about Merge (Pull) Requests? Seems like Copilot can help here as well, https://youtu.be/8_0DJ9FOlOM?t=559

## Command line

The most common command line software is the shell used on Unix systems. However, the Windows based PowerShell is a viable alternative. For many purposes python or other scripting languages can be used.

The command line is the swiss military knife of software development. It is the glue that connects all the different tools together. It enables us to automate all the build processes. For this reason, the command line tools are generally to be preferred over GUI based tools. GUI based tools are great for getting started with some smaller projects, however you’ll quickly reach some limits as they don’t scale up on bigger projects.

The shell is an extremely powerful and versatile tool for executing other programs and running scripts for running all kind of commands dealing with configuration settings, the filesystem, networking, etc. I it certainly worth learning at least some of the basic functionality once you have the opportunity of automating a shell process.

### Copilot

// Copilot for CLI might change how we use the command line (and all its programs with it). Now you no longer have to use google to find the syntax, but you can use Copilot CLI instead. https://youtu.be/8_0DJ9FOlOM?t=787 https://youtu.be/pw0SH7AHIFI -> how does this work exactly?

```sh
git? how do I update the message of my last commit
```
This returns the command `git commit --amend` along with a detailed explanation. The command can also be executed right away. Furthermore the `Revision` prompt allows you to ask for specific changes to the suggestion made.

## IDE

The Integrated Development Environment (IDE) is a class of software used for writing code. Like Microsoft Word adapted for programmers. There are dozens of different IDEs available, both proprietary and freely available. I never cared about the IDEs. I just use what my work colleagues showed me. I don’t think it’s worth spending too much time here by yourself so I recommend you to do the same as I did.

In all up to date IDEs, there are plug ins for most of the tools mentioned above. Ask your work colleague which ones you need. Spend a few hours with him to get an idea what they are used for. This is not wasted time. You also learn something about the code during that time.

It is worthwhile learning some of the shortcuts in your IDE that allow you to modify code in different files faster. This is useful as it improves your work flow. But don’t overdo it at the beginning, you may be wasting too much time here. You can still learn more once you know how your personal work flow looks like. And if you really like to push the shortcuts to the limit, you’ll have to learn the VIM text editor which is operated by keyboard only.

## Continuous Integration

"Continuous integration (CI) is the practice of merging all developers' working copies to a shared mainline several times a day." // https://en.wikipedia.org/wiki/Continuous_integration
This typically means checking in the latests changes of the code, compiling it if required, running all the tests and building the final artifact.

There are several different suppliers for Continuous Integration (CI) software. I don’t know the precise differences and probably you won’t have to neither. You don’t need this if you work alone and in any serious software company this choice is made by others.

At the time of writing, Jenkins is the most commmonly used CI software.

## Debugger

Probably everybody knows what debugging is. Because it is about the first thing you learn at programming: The code doesn't work and I don't understand what it does. Let's walk through it and see what my variables do. For example using print statements. But there is a better way than using print statements. The Debugger.

Every programming language has its own debuggers and IDEs usually support a debugger plugin for most major programming languages. It is useful to know some of the basic functionality of a debugger. Mostly setting break points, navigating through the code and looking at the stack trace. But generally, it’s a sign of bad code if you have to use a debugger too often. Write small classes and functions where you can tell exactly what they should do. Along with plenty of unit tests. Depending on the error you should be able to pin point the source to a certain class or area of the code without using a debugger. Anyway. Feel free to use a debugger, for example if you work with legacy code. But always keep the code quality high and make sure you don’t need the debugger at all.

## Profiler

A profiler lets you check the time required for executing each part of the code. Depending what kind of programming you do, chances are high you will never need one. Only run the profiler if the program is slower than it should be. Thus, this is not a software you have to get acquainted with at the very beginning of your programming career.

## Formatter

Pretty much all companies have a fixed ruleset how code should be formatted. Some teams can debate for days about tiny details. If you start at a company let someone set up the formatter for you. But don’t start endless discussions about the formatting details. Having the formatter set up properly will save you some pain afterwards. If the formatter follows the wrong rule set you will have formatting changes in your merge requests. Which is absolutely terrible, because it’s hiding the real changes. The formatter may change thousands of lines in a single MR and you don’t care about it. Real code changes are short but you have to check them meticulously. Put both kind of changes into a single MR and you are done for. Making an MR becomes impossible.

If you work with old code that was formatted with an out dated ruleset, you have to run the formatter and create an MR before you start writing code. Or at least the formatting needs to be in a separate commit, though a separate, dedicated MR is to be preferred. If you change the formatting rule set, run the formatter on all code and create a dedicated MR.

There are also some companies using custom formatting where every employee can use any formatting style he wants. Once he creates an MR, the official formatter runs on the code before merging it into master.

Personally, I don’t care too much about the formatting style. If I have a choice, I use the default formatting with a tab width of 4 and a line length of 100. This is a reasonable compromise. Linus Thorwalds (the guy from Git) has a very strict opinion on that topic. It you write code for the Linux kernel you have to use a tab width of 8 and a line length of 80. Try writing code like that. You have to write extremely well to make all the code fit reasonably into this pattern. That’s exactly why he’s come up with this rule.

## Code quality checker

There are different programs available that check your code on the most common quality issues. I don’t know too much about them but it’s certainly worth a try. One example is the test coverage tool. Tough this metric shouldn’t be abused as a business metric. Use it to check that you have (almost) all code covered by your unit tests.

If you use C++ or another compiled language, your most important quality checker tool is the compiler. Enable the “treat warnings as errors” setting for all different groups of warnings. You may find it annoying in the beginning but you get used to it and it will make your code better and prevent bugs. Because why should you search for bugs yourself if the compiler can do the job?

## Pip, cmake

Some people may argue pip and cmake don’t belong into this list. Of course, they are right.

Pip is the Python package management software. As a python developer it’s mandatory to know pip. It’s very easy to use. The command line pip install numpy will install the numpy library. Done.
Cmake is the most commonly used build tool for C++. Meson is a more modern alternative you can use for new projects. Make is outdated. And don’t ever use the Visual Studio build.

## Ticketing system

Jira is the most commonly used ticketing system and has little to do with code. It is very easy to use and most of the work in Jira will be done by the manager writing the tickets.
This ticketing software is also helpful when managing a one-man project as it helps organizing the work. And it doesn’t even have to be a software project. You can also use it for all other kind of projects. 
If you don’t work for a company there are also free alternatives. But I’ve never used them.

## Wiki

Most companies use confluence as the knowledge base. Like Jira this is an industry standard. Write general thoughts here. However, things will go out of date quickly so be careful.

You may also write some high-level documentation of your code. But don’t go too much into details. Low level details change too often and will get outdated.

Again, there are free alternatives around, though you are unlikely to see any alternatives in professional environments.

## Docstring

The docstring software auto creates a documentation depending on the comments in the code. It sounds like a nice idea, though it should be used scarcely. There is very little use of using docstrings for internal documentation. Instead it should be used only to document external APIs.

Every programming language has one docstring tool. For python it’s sphynx, for C++ it’s doxygen.

## Exercises

Get acquainted with Git and some other tools mentioned here.

# 35. Domain Driven Design

This chapter is highly influenced by Eric Evans book Domain-Driven Design. The book covers mostly conceptual topics like the domain model. This, along with the “Ubiquitous language” (Evans) it forms the heart of that book and this chapter.

## Ubiquitous Language

There are very few topics that are described mathematically. Most notably finance, physics and engineering. Most other topics are described by the natural language. This is a huge issue as it is hard to bake such a topic into code. It takes a lot of effort to understand the topic well enough to be able to implement it reasonably well. Especially it takes a lot of talking to domain experts about the topic. Only through these discussions you can learn how their model is built up. It is of utmost importance that the development teams learns the language used by the domain experts use among each other. A domain expert has to be able to follow the general discussions between developers. He has to be able to tell when something is off as there is something that doesn’t make sense to him. For instance if the developers mix up the usage of atoms and molucules in a chemistry simulation. This common language between developers and domain experts was named “Ubiquitous language” by Eric Evans.

Developing this Ubiquitous language is of utmost importance for the whole project. Only a well-developed shared language between the developers and the domain experts allows high level discussions about the domain. It takes a lot of effort to develop such a language. Developers and domain experts have to remain continuously in touch and keep refining the use of their language and improve the model that is based on this language. Play around with this language. Try to change the words. Try to build new phrases. This is an important part of the ubiquitous language. You have to develop the language like children learn to speak a natural language. Find easier, better, ways to say what you want to say. Use the insight gained this way to improve the domain-model.

## Describing a model

The domain-model is a high-level concept which has to be described. This can be done in several different ways. The most obvious description are UML diagrams. These are commonly used to show the relationship between different classes. However, UML diagrams are not always the ideal choice for describing code. UML has several deficiencies.

First, it supports only a somewhat limited amount of interactions between classes or class instances. There are frequently better ways to describe code than a class diagram. Maybe a piece of text will do, or a diagram that shows some temporal dependency of some process. It does not really matter how you represent the domain-model, as long as you understand it.

Second, one should always consider that UML diagrams should remain small. There are development teams that printed out their whole code base as a UML diagram, but this is pretty useless. There are way too many objects with interactions between each other as if this graph could be useful. There were attempts to create a UML like programming language and they all failed for a reason. Graphical programming simply isn’t any better than textual programming. Furthermore, a lot of information will get lost during the creation of the diagram. UML is not a complete programming language and it will never be. Keep UML diagrams small.

Instead you can use any kind of document you like. Frequently it is better to create some sort of temporal order that describes a process than a class diagram. Or you create a diagram with class objects. After all it's called Object Oriented programming, not Class Oriented programming.

As with all documents, the documentation of the domain core should be either kept up to date or archived. There is the danger that the documentation and the code diverge over time. Documentation has similar drawbacks as described in the chapter on comments. It takes a lot of efforts to keep a documentation up to date.

## Implementing a Model

There are cases where you can’t implement a model you developed. It would be simply too complex. This is a clear sign that your model is not optimal. A domain expert is able to explain it, so you should be able to implement it. In theory, the complexity of the domain-model should not exceed the complexity of the problem it tries to implement. This is the optimal case where a developer can explain the code to the domain expert and they would simply talk about the very same thing. In this case, the development of the code would feel very easy as everything just falls into place.

In reality, finding this optimal model is a really hard process. Most likely you’ll end up in an iterative loop switching between coding and modeling until you have a breakthrough when you suddenly realize how the optimal model should look like.

Decouple the domain-model code from your other code. This is important to keep the domain code clean and slim. Violating this rule would also be a violation of the SRP as the domain-model is located on a different abstraction level than, say, the database code. The domain model contains the actual conceptual complexity of the final software and thus it should not be cluttered with non-model related things.

## Maintaining the model WIP

It takes a lot of communication within the team to keep the model consistent. This cannot always be guaranteed and the model may diverge in different directions. Forcing the model to remain consistent may be a solution, but there are other ways to deal with this problem.

The thoughts made here are also to a large extent valid when dealing with any kind of library.

### Unified model

The attempt to keep the model unified is the most obvious one. Though it is hard to keep up the required level of communication to maintain this state. A good way to enforce this communication is continuous integration. This forces the team to merge often and early and therefore differences between the model and the actual code become apparent very early. The single … gets for the required communication a unified model that has less complexity than two different models.

### Separate ways

Sometimes the overhead of keeping models together simply becomes too big and it turns out that it is no longer useful to work together. It is no longer worth the effort. There is only very little overlap between the two models and cutting them apart is not such a big deal.

### Conformist

### Developer Client relationship

The model is split into two parts and one development team is relying on the model of the other team. If the upstream team (developer) is willing to cooperate (for financial or political reasons), the two teams can go into a developer client relationship where the downstream team (client) can order features that the upstream team will implement. 

## Refactoring toward deeper insight

#figure out what to write here exactly
This section is named after a chapter in the book Domain-Driven Design, p.322. It deals with a high-level point of view on refactoring, the domain level to be more precise.
-	The design does not express the team’s current understanding of the domain;
-	Important concepts are implicit in the design, though they should be explicit
-	Important parts of the design can be made suppler

However, all the time you have to stay in close contact with a domain expert. Under no circumstances you should make changes that contradict what he says.

## Entities, value objects, aggregates, … WIP

Entities are unique objects. Their lifetime typically spans over most of the code lifetime and they have unique properties and typically an ID. A very simple example are humans. Every human is unique and there are attempts to give every human some kind of ID. Though this is harder than it sounds. Obviously, names are not appropriate as a unique identifier. The social security number is used in some places, but not everyone has one and there is nothing comparable in many other countries. For many websites, the email-address is used, at times also the phone number. #what else to write about entities?

Value objects are pretty much the opposite of entities. Value objects are only defined by their properties. They don’t have any unique ID. One example are apples in the super market. They might look slightly different, but all together they are indistinguishable. The only interesting traits are the flavor and the price of an apple. Other than that, they can be replaced at any time.

Aggregates are a combination of several other objects. For example, a car is an aggregate. #what is the aggregate and what is the entity here? Ddd p.150?

Aggregates typically consist of one entity taking care of many value objects. 

## Domain level, old text

#get some more from the DDD book? It feels incomplete.
The Domain Level is an expression used by Eric Evans in his book Domain-Driven Design. The Domain Level and especially the Domain Core are the heart of the software. It represents the central part of your code. That part that you actually make money with. It may be fairly small, yet it covers much of the overall complexity of your code. The complexity of the business it represents. Frequently, the domain level is unique, you cannot buy this part of the software anywhere else. You have to develop it yourself for your business. Exactly this makes it so special and valuable.

While the UI and all the infrastructure code are usually fairly generic, the domain level consists of highly specialized code. Both, from the complexity and from the business rules point of view. It thus requires the best and most experienced programmers to implement and improve the domain level. This is an apparent contradiction to the rule that any programmer should be able to implement any open ticket around. Apparently, this means that extra care has to be taken with the team. The domain level developers have to stay and work on the domain level and not wander off, dealing with some database nuisances.

The domain level is the heart of your software. Its architecture influences all the other levels of the code. This means, that extra care has to be taken here as well. It takes the most experienced and capable programmers in the team to make design decisions here. Bad decisions here can be costly.

The domain level tends to grow over time. This should be prevented as code in the domain level needs to fulfill extra stringent requirements and is more costly. One of the reasons is that more and more peripheral code creeps into the domain level. Make sure that at all times, the domain level remains slim.

// example stolen from DDD p.68

You might be a little confused now about the domain level. Let me make a brief example (stolen from Domain-Driven Design).

Let’s assume you have a shipping company. You make money by transporting cargo from one harbor to another. Your software can do the following things:
1.	Draw a widget on the screen.
1.	Query the database for all the possible cities.
1.	Interpret the user’s input and validate it.
1.	Associate the selected harbor with the cargo.
1.	Commit the change to the database.

These are all more or less important commands, yet only one of them is in the domain level. 1 is in the GUI level. 2 and 5 deal with the database. This is infrastructure level. 3 is in the application level. Only 4 is located in the domain level as it deals with the heart of the business.

#The domain model is the interface between programmers and the domain experts. Both have to understand what is going on. The domain model connects code and the real world. A domain model doesn’t have to be as realistic as possible. It has to fit the purpose.

A project faces serious issues when its language is fractured. Programmers won’t be able to talk to the domain experts anymore as misunderstandings will pop up everywhere. Learn the language like toddlers.

High level concepts follow the domain language, low level concepts follow the general programming patterns. On the intermediate level you have to manage to make a connection between the two.

Coding is research. Figure out how to implement the domain knowledge of the experts. Draw diagrams if needed to understand the problem and convert the knowledge into code. But don’t plan too much ahead. Diagrams tend to get outdated.

Make code explicit

See DDD p.205

Explicit logic is much easier to understand than implicit logic. The logic is usually only implicitly known, but the logic in the code has to be explicit.

#write some examples here?

## Exercises

Take Robert Martin's bowling example and let the user programm it?

# 36. Good code

This is an attempt to distille a list of rules that allow you to judge the quality of code.

Here are some signs for good code:

By definition good code is easy to understand. Also, for new software developers in the team. Even marketing people may understand some of your technical discussions as you use the same domain language.

Good code is well tested. It has both, unit and acceptance tests. Especially a good coverage with unit tests is paramount, as it forces you to write good code. Yet at the same time, unit tests are strongly reducing the number of errors in your code.

Pretty much all your code follows the single responsibility principle. Functions, classes, modules. Everything. This makes the code much easier to understand and also naming becomes simpler, names should be short, yet concise.

Do not repeat yourself. There is no copy paste code around. But also avoid conceptual code duplication. Code duplication is terrible as you never know if making a single change is enough, or if it has to be implemented in several other locations. This leads to bugs and high maintenance costs very quickly.

Classes should have high internal cohesion. They should have strong coupling between the variables and methods and weak coupling to other classes. Due to constant refactoring classes tend to lose cohesion. Then they have to be broken up into several smaller classes.

It feels easy to add features and change code. Thanks to the test coverage you have a safety net and well-structured code makes it apparent where new features belong.

A function name tells you what it does, there is no surprising behavior. The same holds for classes and variables. Functions have no side effects.

There are no magic numbers. Assign the magic number to a variable with an appropriate name and the code becomes much clearer to understand.

Define variables right where they are used. Always assign them a value right away.

Create objects always at once. Creating only part of an object because not all required information is around is the code equivalent of a supply chain issue. This can become very confusing. An object should be completely created, or not existing at all. Throw exceptions if objects cannot be created at once.

Write short functions (~< 10 lines) and classes (~< 100 lines). These are very rough estimates and depend on a lot of factors. Usually their length is limited by the SRP and the level of abstraction. Complicated functions and classes have to be short or their complexity might get out of hand.

Keep the dependencies between different parts of the code low. Especially when dealing with 3rd party libraries, you’d better write a wrapper around it. This helps once you want to replace it.

Using a debugger frequently is a strong sign you lost control of the code. Normally, automated tests should cover all the bugs and the debugger remains unused.

YAGNI: You Aren’t Going Need It. Plan ahead the structure of your code but don’t implement anything you don’t need yet. Chances are, you will never need it. Only architects have to speculate what will be used in the future. Developers implement only things that will certainly be used.

The solution representing the natural logic of the problem is usually the best. It has the lowest complexity. The complexity of the code is equal to the complexity of the actual problem to be implemented. The sales team can explain the domain logic and you have to bake it into code. Don’t come up with your own logic on a problem you don’t understand too well. 

Use the simplest features of your programming language as possible. Only use more complex features if you really benefit from it. Don’t use features of your programming language that resemble black magic.

Do not nest if loops. Apparently, this violates the SRP and is highly prone to bugs. Avoid nested try catch blocks as well. Preferably avoid nested loops completely.

Avoid Boolean values and logic as much as you can. Due to human deficiencies these are the lines of code which harbor the most errors. Try to avoid them as far as reasonably possible. Make sure every branch of an if statement is covered with tests.

Don’t pass Booleans as function arguments. They are a strong sign of violated SRP. Resolve the consequences immediately.

Don’t do string comparisons, use enums instead. Convert the string into an enum as soon as you have the string object available.

Make the code self-commenting. Only use comments for things the code can’t explain by itself.

Functions asking for more information than they need. They ask for a complicated structured object, even though they need only a small fraction of the information. "You wanted a banana but what you got was a gorilla holding the banana and the entire jungle." - Joe Armstrong

# 37. 3rd party software

“Prefer visa over power shell” – some youtube video 

// where to write about integration?
// In the google book they write a whole chapter about the proplems on how to deal with 3rd party libraries. This really seems to be an issue.

There are thousands, if not millions of companies selling parts for your software. For many problems there are also open source solutions available. This is great, but as always there is a price to pay.

No airplane engineer would start developing his own jet engine and no programmer would write his own database software. Even if they don’t like the current solution for whatever reason, they get something from the market. Everything else simply crazy. Others are developing databases and you are not going to compete with them. You want to do other things instead. You found your niche elsewhere and you’re going to stay there unless there is a reason to. You outsource everything you don’t really have to do yourself.

Possibly you somehow have a bad feeling about this approach. You want to do everything by yourself. You don’t want to pay other companies for some small libraries. I can assure you that your feeling is natural. But you have to get over it. It’s just not worth it. You didn’t write your own operating system. You get a good amount of money every year. And if you can save some time by outsourcing parts of the code this is great. You also save the maintenance.

Using 3rd party libraries or software is great. Most of the times. Sometimes it also has its issues. There are some companies who didn’t write their code up to the standards and now they are in trouble. Most famously all the customers of Oracle who wrote their code in such a way that it’s nearly impossible to migrate their software to another database vendor. These companies now pay gigantic licensing fees and don’t get away.

Another problem are libraries with comparably few contributors. At some point there might be no one left to maintain the code. In most areas you can still use such a library for a while but you should look out for a different solution. A lot of problems can pop up when using not anymore supported software.

Everything explained here is also true for IT services and infrastructure (Jira, Amazon Web Services (AWS), github, google maps, …).

To put it brief: Third party software is generally great as it saves you a lot of work. But you have to make sure you don’t get stuck with it. You have to stay flexible. Decouple the 3rd party library from your code. Write a thin interface between your code and the library. As always, if you can test something you are fine. When you mock the database, you need an interface that you can possibly use to support other databases as well.

The very big question is always when you really need such an interface. Most of the time I’m too lazy as well for writing one. But you certainly need one when dealing with databases. Call all the database specific queries only within this thin layer. The whole rest of the code is database syntax free zone. This makes it very simple to change the database. You only have to add or replace the wrapper. You might have to change some of the implementation as well as the functionality between databases differs slightly. But this is a small price to pay compared to the millions Oracle got so far.

You should rethink using a 3rd party library if it has only few developers. If there is a reasonable alternative, you’d maybe better refrain from it. On the other hand, this code could be absolutely essential for your own software, then it would be a good idea to join the project and become a developer there as well. In fact, pretty much all major software companies support the software projects they are relying on. Some projects got that much additional man power that they run out of work to do. And even the unthinkable happened: Microsoft became one of the biggest contributors to the Linux kernel!

// add here the supplier-client dependency level? Or mention them in the dependencies?

# 38. Dependencies

In the early days, people wrote code in a single file. This has several drawbacks. It’s very easy to lose the overview of the code and it is hard if you have to replace a part of it. For example, if you found a faster library. Even worse, the library is only available as a binary. Then you can’t use it at all.

These are some of the considerations that made programmers split up their code into many files. But how do you tell the computer how to build up the complete code from these files? Apparently, there are some solutions, but this is an ongoing discussion.

In C++ the whole problem becomes even worse due to the compiler requiring the header files. It is possible to compile a C++ program with the command line for a single file but it becomes unbearable for bigger projects. If you use C++, it is inevitable for you to learn a build tool, for example cmake or meson.

What all programming languages have in common are the import or include statements at the beginning of the files. Even with the build tools of C++ you still need those. They might bother you but at times they are quite handy. They are an indicator for some very bad patterns in your code.

If you draw a plot with all the files as circles and how they import each other as arrows you get a directed acyclic graph. The trunk of this graph is the main function, the highest level of abstraction. As you go up in the graph, the level of abstraction becomes lower.

Now the first thing to look out for in this abstraction graph are two arrows pointing in opposite directions. This means that two files import each other. Depending on the language this may cause anything from normal behavior, undefined behavior, or errors. But even if it works, it is very bad design. Apparently, there is no clear distinction between the levels of abstraction. It’s just a mess.

The simplest solution is fusing these files. However, this is only a superficial fix. You really have to find out the relationships between the function and classes in the files. Maybe you can reorder them, maybe you have to rewrite the corresponding code from scratch.

Circular imports are not common as they are easy to spot and experienced programmers don’t have such issues anyway. The much more common problem are too many dependencies. This makes the code become very sticky. It is very hard to give some numbers to quantify the problem, as it depends on a lot of factors. Breaking up a file is usually a good thing to do, but at the same time it increases the number of dependencies. As a rule of thumb, breaking a file into two is a good thing if the number of dependencies increases only a little and it should be reconsidered if it almost doubles. The later means that most code needs all of the code from this file, so it makes sense to have it all bundled together. 

How you break up a file is the even harder question. Sometimes you can easily bunch the code into groups, other times it is very hard to tell what belongs together. You can certainly split some of the code into a new file if you refactored a class into two classes.

The most important step towards lower dependencies is working on your code and maybe also the whole structure of it. Having database access spread all over the code is usually a very bad sign. The logic of your code should be concentrated at a few spots. Make all the database requests at once, as far as possible, and store the results in a data class. Afterwards you can pass around this data object and there is no need to think about the database anymore. And just like that you get rid of many dependencies by improving your code.

The hardest part is reducing the dependencies by improving the general structure of the code. Good code has simple logic, which in turn has few dependencies. This, however is quite tricky and even if I could, explaining here would be barely possible.

Summary: Write your code to have few dependencies. This is generally a good sign. You may never have circular dependencies.

## Circular dependencies

Circular dependencies are easily created. But with the right technique, one can get rid of them again. In some cases, one has to merge both classes into one. But this should be the exception as it’s more of a hack than a proper solution.

Usually, circular dependencies occur as two classes exchange data between each other. Class A needs data from class B which needs some data from class A in return. You should be able to tell whether class A or class B corresponds to the higher level of abstraction. Let’s assume class A is the higher-level class calling class B at some point. Now class B should never ever have to call class A. B is low level and knows nothing of the high-level class A. This leads to only one solution: class A has to call class B exactly once and hand over all the data class B needs to return the final result. 

Long story short: The high-level object calls the low-level object and hands over all the data required at once. The low-level object returns the final result at the end of the calculation. This resolves the problem of circular dependencies and sorts out the levels of abstraction.

### Example

This example here is deliberately made simple. No one would write code like this. It's just to make a point. Here we have a circular dependency between the functions `a` and `b`. Apparently this makes the code much more convoluted than it had to be.

```py
def a(counter):
    if counter > 0:
        b(counter -1)

def b(counter):
    print(counter)
    a(counter)

a(5)
```
We could simplify it by inserting the definition of b into the function call,
```py
def a(counter):
	if counter > 0:
		print(counter-1)
		a(counter-1)

a(5)
```
This is already much simpler. Of course it could be simplified even further by removing the recursion all together.
```py
def a(counter):
	for i in range(counter-1, 0):
		print(i)
```
As a summary one can say that circular dependencies should be avoided all together. This is usually not too hard and it improves the readability of the code significantly. Even a single recursive call can often be refactored away and make the code even more readable.


# 39. Working in teams

// https://github.com/97-things/97-things-every-programmer-should-know/tree/master/en/thing_85

// see chapter 2 in google: 
people are insecure and don't want to be critisized.
Great things are hardly ever achieved by a single person
Most work doesn't need a genius. But all work requires a minimal amount of social skills.
Talk to people, don't hide your work.
Fail early, fail fast, fail often. get feedback as early as possible
How well is the knowledge distributed? It is better to be one part of a successful project than a critical part of a failed project.
When working in teams you learn much more than when working alone.
Constructive critisism vs. flat out assault
psychological safety is the most important part of an effective team
Social interactions need humility, respect and trust
keep asking questions. there is always something to learn
You always have something to teach
Don't just say, "this is bad". Come up with some reasons.
Bus factor: The number of people that need to get hit by a bus before your project is completely doomed.
A good manager considers how things are done. A great manager considers what is to be done and leaves the rest to his employees. He has faith in them. This is much more motivating than someone yelling around.

Humans are mostly a collection of intermittent bugs. - Brian Fitzpatrick, google

You will probably spend most of your career working in teams. The story of the lone programmer in the basement is a myth. Modern programming is done in teams. Not only do programmers work with other programmers, but you'll also have to work with people from marketing and sales as well as customers.

Cooporating with other programmers has its advantages and drawbacks at the same time. Comparing programming in teams with a lone programmer is like comparing a parlament with a dictator. A parlament requires more time to come to some conclusion, yet the solution is generally better than the decision made by a dictator.

At the same time scaling up software projects only works with teams where all programmers are cooporating together. It is not possible for a dictator to work on his own project. He has to adapt and become part of the parlament.

## Team structure

In most projects a team consists of roughly 4-12 software engineers, one project owner and one project manager. The software engineers are working their ass off writing awesome code while everyone else is just slacking off. The project owner is the only one who has an idea how to implement the tickets and wonders why everyone else is so stupid. And the product manager starts wondering why he has to scratch every bit of information how the software is used out of the nose of the customers. While at the same time his team of highly paid developers needs weeks to finish a tiny ticket. Yes, this will be your somewhat exaggerated future in a software development team.

There are different ways to organize a software team. There is usually a product manager. As you can guess he’s a manager and not an engineer. He talks to customers about their needs. He knows what they are doing. He has to know his product and figure out what feature should be developed next.

The product owner is, you could guess, responsible for the code. He is the link between the product manager and the software developers. He works together with the product manager to write the tickets.

You always have a few software developers. Each one draws a ticket and starts implementing. They implement until all requirements are met.

It is important that everybody in the team talks to each other. Software engineers talk a lot about their code. But quite frequently they have questions about the ticket that the PM has to answer. Vice versa the PM wants to know the state of each feature for estimating the progress of the software.

### The bus factor

https://en.wikipedia.org/wiki/Bus_factor

The bus factor says how many team members have to be at least hit by a bus before the project is doomed. The definition of this expression may sound a little absurd. And it is. But it has a point. Fortunately people don't get hit too often by a bus. But there are other risks. People can get sick or they quit their job for whatever reason. And for a low bus factor, this may put the whole project at risk.

Make sure the bus factor in your project is as high as possible. Ensure that there is a good amount of knowledge exchange between the team members. Such that everyone knows something about everything. That the whole project does not stall only because a single person is ill.

## Developers work

The developers are the ones who do the real work. They are the ones who write all the code. For such hard work it is important that they stick together. Only a tight pack of hungry software engineers can do the job.

Software engineers have several tasks. The most obvious one is, of course, talking to each other. You have to go through the tickets, you have to discuss how the fundamental structure of the code should look like and you have to talk during pair programming or code review sessions. The talking during code reviews is not absolutely necessary. Smaller MRs can be done by writing comments, but when in doubt, it’s better to talk to each other. Especially during times like Corona, the human touch got lost and things sometimes got hairy.

You also have to talk during pair programming. One person works at the computer as usual, while the other person knows everything better. Erm no. Seriously. Both participants discuss together how the code should look like. This creates important knowledge transfer, especially if both participants are experts in different areas of the code. Both programmers learn from each other and the code quality improves. Code review in the MR is no longer required. All together pair programming takes some more time than working alone but frequently this time is well worth it.

Another fairly big job is going through merge requests (MRs). Everyone has to do it, no one really likes it. But it has to be done. Nobody likes to wait a day until his code is approved and merged. It has to be done quickly. So, get up, open the browser and select the first MR. And now… doing code review is a tricky business. You can somehow tell that the code is not good but it’s so elusive. It’s your job to bring it to the point without being too picky. Furthermore, you see some code that had been there before and now it’s duplicated. It should be refactored. And a dozen of other things. Time to give the author of this MR a call. This can’t be solved by writing comments.

Once this is all done you may finally write code. Grab yourself a ticket and get started. Dig yourself through the code down to a place that seems appropriate. Neighboring classes have about the same abstraction level and all the required data is around. So, you start… by writing an acceptance test. Then refactor a little the area where the function will be called, write unit tests. Finally, you write the class and all the tests pass. One more small refactoring and you’re ready to create an MR.

## Communication

// This needs some reworking or it can be removed as well.

In a team, the most important language is not Java but English (or German in the projects I worked on). Use this language to communicate with other team members. And if you think communicating with a computer is hard, think twice. For a computer you can just google what to do and most of the time it works. But with other humans it may take significantly more efforts for a good communication.
-	Make sure you know what you are talking about and know how to talk to the specific audience.
-	Keep communicating. Ask questions. Let the other person talk. Once you don’t get replies anymore you have an issue.

There are probably hundreds of other rules, but these two here are the ones I know. Even though I’m not that good at applying them. As a developer you don’t have to know all these things. But if you want to manage people you have to get a feel for how to talk to others. Get some books or seminars about it, this is not the place to go into details.

## Working with humans

Humans are all inherently flawed. They are insecure and try to hide themselves. They don't like to be critisized. They are scared because they are not a genius. But they don't have to be. Hardly anyone is a genius and most work is done by good, but not outstanding programmers. This fear, however, makes things worse. Because it is important to talk to other developers. Your team is much more productive if the team members talk to each other. If they are able to critisize each other in a constructive way.

In order to excel, humans need psycological savety. This requires 3 things: humility, respect and trust. Effective team work is not possible without these things. Discussions only work if all parties involved are treated equally. 


## Working with customers

// https://github.com/97-things/97-things-every-programmer-should-know/tree/master/en/thing_97 

Customers are only humans. Quite frequently they don't say what they mean because they don't know it any better. Keep your vocabulary changing to figure out what certain words actually mean in the view of the customer. At times this reveals some misguided view. For instance if customer and client have some completely different meaning. Do not expect the discussion on requirements to be over after one meeting with the customer. You have to stay in touch in order to get constant feedback to make sure you implement what the customer wants and not what he says.

Also frequently customers don't know what is important. Or at least things are important to customers that are not important to the programmer. For instance a software is only used if the GUI looks exactly the same as in the previous software. As long as the user does not have to learn anything new. Even if the GUI was really badly designed. You really have to come up with some significant improvement that your version will be accepted.


# 40. Code review

// see chapter code review in SEG (software engineering at google)

Code reviews are important to improve the quality of the code. This does not work without some critisism.

A long time ago, in a kingdom far away, software developers started cooperating. They shared their code. They started working on the same code. At the same time. And problems started creeping up. They needed some software to control the different versions of the code.

After some mediocre attempts to fix this issue there was our savior. Linus Thorwalds, the hero of every fanatic Linux developer, saved us by developing git. This solved the problem of version control software once and for all.

Unfortunately, git was not yet the final solution. It was still possible to write crappy code and merge it into the master. There was no other solution than firing this malicious developer.

But now comes the real solution: Merge Requests (MR) and code reviews. No user is able anymore to make changes on master all by himself. Before he can merge his changes into master, he needs to create a public request and wait for someone else to accept it. And thus, allows the changes to be merged into master.

Now there are a few things to consider regarding code reviews. First of all, code reviews are great not only to keep the code quality up to date, but it also helps improving the programming skills of all developers. They are a great opportunity for knowledge exchange. Developers are obliged to look at each-others code and thereby learn a lot.

## Drawbacks

However, there are some downsides as well. They can be severe enough that teams even stopped using MRs altogether. Most importantly, everyone has to stick to the rules. There is no way to prevent foul play by the developers and sabotaging the system will render it useless or even counterproductive.

The first problem is people just accepting merge requests without any comments. Either because they don’t understand it, because they are lazy, or to make the author of the MR a favor. One could also just stop using MRs at all.

The second problem is speed. It is of utmost importance to check MRs as quickly as possible. Too long idle times for MRs lead to a very significant drop in the developers’ output. Additionally, it is highly frustrating waiting for a MR to be looked at and not being able to continue working.

Another very serious problem are too long MRs. It is impossible to judge the quality of a change of a thousand lines of code. You should keep the tickets small. You should keep the commits small. And you should keep the MRs small. Huge MRs are a waste of time as no one understands what’s going on. If a ticket turns out to be too long, split up the code in several MRs and make sure the tickets become smaller in the future.

There is a wide spread and very fundamental misunderstanding regarding MRs. Don’t expect the referee to find bugs. This is in most cases absolutely impossible. The referee doesn’t have time to think through all these details. The author is responsible for writing error free code along with good test coverage to prove it. MRs are more about the general structure of the code. And they are about knowledge exchange. The referee can only check that there is a reasonable amount of test coverage.

Always be polite. An MR is like criticizing someone by email. This is a highly delicate thing to do. Stay professional and make sure you only comment the code and not its author. Once people start YELLING at each other in MRs it is high time to quit the job. Now things certainly deteriorated during the Corona virus pandemic when most developers had to work in home office. It takes some good team spirit in order to deal with written comments on MRs.

One thing I can highly recommend is looking at the code together. In theory, the referee is supposed to understand the code all by himself (at least that’s my understanding of an MR). However, discussing the code with the other author turns out to be a really good alternative. Especially for long or important MRs. Additionally, it keeps up the human touch. It is much harder to insult someone orally than written. This is a highly important feat.

In case you do pair programming, you may skip the code review phase all together as there were already two developers in agreement that the code is fine. This is one of the reasons why pair programming does not take twice the amount of time. The code review may take a considerable amount of time that will be saved with pair programming.

# 41. Working with existing projects

Up to this point everything was great. We had no restrictions what so ever. I could tell you whatever I wanted. “One beer please! Just before I am forced to tell you how to wiggle around in an existing project.” Yes, working on existing projects can be hard. Sometimes the developers made some very obvious mistakes. But at the same time, it is really hard to keep everything in shape. In every software development there will be this point where you ask yourself “Gosh, how did I screw up this code so badly?” Even if you follow all the advice this book gives. It will happen to everyone. So, if you start with your first job and the code looks nothing like what I explained so far, don’t be disappointed. Don’t be too harsh with your boss. Yes, it is not really motivating to work with bad code. But there is still a lot you can learn. And unless some extremely fundamental flaws were made it is very well possible to make improvements.

You might be motivated to suggest a complete rewrite of the code. You may do that, though I do not recommend it. A complete rewrite is hardly ever an option. It takes years, costs millions and very often the final code is not that much better. Generally, it is better to improve the existing code. You spot something you want to improve. You write tests and start refactoring. This may seem tedious to you but you always have to consider that the code was written by many programmers over many years. It’s worth millions. You are not going to fix it in a few months.

// move text to refactoring?

There are some different stages of how bad the code can be. I’m trying to give you a short overview.

No Interfaces. This is probably the worst case. Without interfaces it is impossible to write tests. Without tests it is impossible to refactor and add interfaces. It’s really bad, but it’s not a lost cause. You can still try to refactor slowly. Though it will be painful and you constantly have to look out for bugs. A sales person will have to check your work frequently. The whole refactoring will probably take years. Maybe a complete rewrite is indeed the better option. I hope you never end in this kind of position.

No Tests. Code without tests is one thing. One can still write them later on, even though it takes much more efforts. The real issue is probably the low quality of the code. It has some interfaces but the classes are way too big and the objects are hard to create. This is one of the few cases where you are officially allowed to cheat. You may make parts of a class public in order to test it. Once the refactoring is done, you should make it private again. In a year or two. Once you have some test coverage, you can break the classes into pieces.

Extremely long functions. Let’s be honest. A function, or even worse a class function, of about a thousand lines is an absolute nightmare. No one will ever understand it with all its corner cases. It is absolutely impossible. No one is ever going to touch it. You might be able to make some small changes, but you are not changing it fundamentally. The only way to really change it is a complete rewrite. The hardest part about it is getting the specification what the function actually did so far. If bugs are absolutely not allowed, you’d better just leave the function as is.

// move where?

If you work on an existing project, there might be no or only an insufficient number of tests. This is a serious issue. Not only from a technical point of view, but also a political one. Due to the bad test coverage, one might introduce bugs when refactoring. And as the last person to touch the code is responsible, it becomes yours to fix. However, this is not what you wanted. You only wanted to improve it, not own it. Ultimately, people are afraid of refactoring the code because they’ll become responsible for it and not so much, because it would be hard. Therefore, the developers stop refactoring and the code decays even faster than it did before.

# 42. Planning

TODO: read through again. Is there duplication with the agile section?

“We take the most experienced engineer. He spends 2 days making various attempts to estimate the amount of work required. In the end he takes the highest estimate and multiplies it by two.” – unknown

Planning major projects is extremely hard, not only in software engineering. Architects and civil engineers plan houses and streets all the time so they’ve become fairly good at it. But as soon as there is something much bigger they never did before, they start struggling. Frequently they are quite good but there are always cases where things go haywire. Not only at the Berlin airport.

With software development it is even worse. There are no small houses and streets that we can get some practice with. Unless you do very basic web or app development. Most software is simply way too complex and fairly unique. It’s impossible to understand all the details. Even the fundamental logic of the problem is not always apparent. Somehow plans on writing software are always too optimistic and failed deadlines are standard.

This sound very logical. We are all motivated and want to get things done. But our working speed is limited. It’s slower than we want it to be. We need more time to understand problems and code, we have to change more code than intended and we also spend a lot of time with MRs and meetings. If your boss asks you when the software is going to be ready try hard not to be too optimistic. It is very hard but making too optimistic guesses won’t help anyone. You put yourself under pressure and ultimately you still miss the deadline.

Planning code in detail is a similar topic. But at least there is now a solution that seems to work in most cases.

For a very long-time software projects were developed using the waterfall approach. There is a team of developers who try to understand the topic and develop a model on the white board how the structure of the code should look like. Another team, possibly the same one, takes these ideas and implements them. Do I have to tell you how this ended? Let me give you some hints. People tend to underestimate complexity; people miss features and furthermore there are changing requirements. The result is a team of software engineers trying hard to implement what they were supposed to. At the same time, it doesn’t work as the planning team missed important details and over the time new requirements showed up. I heard of cases where this approach worked. A few. As well as a lot of disaster.

Now let’s go back to the civil engineer and his houses. It makes sense that the civil engineer plans and the construction workers build the house. That’s what they do. That’s their job. Over the time a construction worker gets an idea how the structure of a house has to look like. But still he is never going to plan one. He wouldn’t know how. Vice versa, the civil engineer could maybe build a house, but it’s financially not interesting. It makes sense to have two different groups taking care of planning and building. And even here the civil engineer has to check the progress of the construction frequently and improvise in case of unexpected events.

In software engineering the planning and the building team both have the same education. The planning team might have a little more experience, but that’s negligible. Then why on earth do you separate the two tasks? This creates only overhead and frustration. If the planning team is smart enough to plan the whole software on their head, they should also have enough experience to write the whole thing down in code. There’s barely and overhead. Like this they will be able to see if everything really works out. In then end the planning team can make the whole job on their own.

This doesn’t mean that there is no planning needed at all. It’s just different. Smaller and faster. 

We need more feedback and to be able to adapt. In one word: Agile. You still need a quite good idea how the general structure of the code should look like. And then you start implementing one feature after another. At the same time, you have to make sure that everything is well covered with tests. It will be inevitable to do refactoring once in a while. But even here the old waterfall approach wasn’t any better. The tests were not there and the refactoring got ignored. But I have to warn you. Agile is not going to solve all your problems. You can have terrible code in Agile and be stuck or you can have great code in a waterfall project and be highly productive.

As a conclusion I would say that Agile is generally the better approach than waterfall. But it only works if you first build a solid basement for your code, you write well tested code and you refactor frequently.

In an Agile project it is important to cut the tickets as small as possible. This clarifies the task and minimizes the risk of a ticket to fail within a sprint. Small tickets are much easier to estimate. Figuring out the number of small tickets up to a certain point in development is the really tricky part.

## Planning code # move elsewhere? Rename section?

A widely used tool to display interactions between objects or classes are UML diagrams. To put it up front, I don’t like them. They are a waste of time. You can also just briefly write the empty classes and connect them in code. It’s the same. Just in a different representation. UML is the worse one. It would be easy to create the UML programming language. But no one has done it. Because graphical programming sucks, it is harder to understand than code. Small UML diagrams are ok, but one can quickly get lost if they get bigger. Ask scientists about their experience with Labview. I prefer writing the code framework right away and save the effort for creating UML diagrams. However, feel free to try UML diagrams. If they are a great help for you or your team it doesn’t matter what I think.

One also has to consider the limitations of UML diagrams. The only represent classes and their relationships. This covers only a tiny fraction of a program. Quite frequently you have to understand the logic behind a problem where UMLs don’t help you. You need something different. Try out whatever you feel like. Some different sketch, a plot, a coffee break, a walk in the forest, … As long as it helps you understanding the problem it’s good. 

I also had such a moment during my master thesis when I was calculating the expected value of the experiment but I was stuck for a long time. One late afternoon a PhD student came by and wanted to talk a little. He just casually mentioned every step of my calculation and within a minute I found my mistake. Talking to other people is usually the best way to solve a problem. 

#where to add a chapter with errors?

# 43. Agile

“Intelligence is the ability to adapt to change.” – Stephen Hawking, among others

All architectures become iterative because of unknown unknowns. Agile just recognizes this and does it sooner. - Fundamentals of Software Architecture

// How much of this chapter is explained in Working in teams

// citation Clean agile, Agile manifesto

// add the INVENT points from clean agile

Until the year 2001, most software development teams were working according to the so-called waterfall scheme. For every project, there was an analysis, a design and an implementation phase. This sounds like a good thing to do, as other engineers work the same way. However, planning software top-down never really worked out and changing requirements made things even worse. Brief, in many cases waterfall projects turned out to be a disaster.

The first problem of waterfall was missing feedback. The whole project was just one big pile of work and it was impossible to get a reasonable estimate on the time it takes to get all the work is done. Many projects failed spectacularly as at the deadline there was still a significant fraction of this pile left but no one informed the management beforehand.

The main issue however was, that people had the wrong mindset. They assumed one can plan software like building a house. One makes a plan in the beginning and gets a team of developers to execute it. This does not work out. And worse, since the team was working in waterfall mode, they were not in the right mind set to adapt to changing requirements or problems encountered during the implementation.

## Agile values

In 2001, a group of software engineers met for two days in the Rocky Mountains in order to improve the planning of software projects. The result was the Agile Manifesto, a brief guide line how software development should be done.
-	Individuals and interactions over processes and tools.
-	Working software over comprehensive documentation.
-	Customer collaboration over contract negotiation.
-	Responding to change over following a plan.

// write something about these values?

Bill of rights

The bill of rights states what kind of rights each individual in an agile process has.

// add them here or should we leave it away?

## Work planning

The product owner has a set of requirements that the code should fulfill. This pile of work is broken down into small tickets. Where I’d like to emphasize the word small. Each ticket should be doable by one person during one sprint. Preferably it’s smaller than that.

Every ticket is estimated for how much work it will take. The ticket size is quantified by the number of story points it gets. This is an artificial number to give the tickets a measurable size. Yet at the same time, the story points are vague enough to indicate that this value is only a vague estimation. In most projects, a story point is between one half and one day of work.

The ticket size is estimated at the sprint planning. For each ticket, the number of story points is estimated by the team. Usually every developer makes a hidden estimation and the average is the actual number of story points. If there is a large discrepancy in the estimations, the team needs to discuss why this is the case. Probably some difficulty was missed, but it could also be that most developers overestimated the task.

Tickets all have business value. They have a direct effect on the user. This means, that every ticket is a vertical slice through the software stack. From the database through the backend code and to the GUI. Everything has to be worked on. So, either you know already how to work on each layer of the software stack, or you team up with someone else and do pair programming in order to fill the knowledge gap.

At the same time, one can write acceptance tests for every ticket. “… if the user clicks x, then the window closes.” This is also the acceptance criterion of the ticket: does the acceptance test pass?

## QA

In waterfall projects, the Quality Assurance (QA) was manually trying to find bugs in the existing software. This certainly does not fit anymore with agile. Instead, the QA should write the acceptance tests of every ticket. These tests should preferably be written before the developers finished working on the same ticket. This is quite similar to TDD and is called Behavior Driven Development (BDD).

Finishing the acceptance tests before the developers finish the actual ticket is a hard task. One way to mitigate this issue is working ahead. The QA team can always try to be half a sprint ahead. This is not so easy as the sprint planning was not yet done. On the other hand, the PM should know quite well one sprint ahead what is going to follow next.

## The Iron Cross

// make a graph of the iron cross

As in most other domains, there is frequent problem of projects not being done in time. There is of course always the solution of reducing quality far enough to make it in time. 

In Software engineering, we have the rule of the Iron Cross: Good, fast, cheap, done. Choose three.

Here are some options how the management can deal with these issues.

### Good

Reducing the quality of the code is the first option. Albeit, it is probably the worst one. This will lead to bugs and the overall productivity of the team will plummet quite quickly. Quick and Dirty just doesn’t work. Especially not on the long term.

### Fast

Reducing scope of a project is usually the best option. In Agile, the important tickets were done at the beginning of the project. Furthermore, the work was cut vertically. Meaning that all the important stuff is already working. This allows the management to remove some of the less important tickets from the scope of the project.

### Cheap

If a software project goes wrong it’s usually not that cheap anymore, no matter what’s being done. 

One thing the management tends to do is throwing more developers at the problem. This, however, is not working out as planned. It takes time and effort to introduce the new developers into the project, leading to a short-term dip in the overall productivity, before ramping up.

### Done

Changing the schedule helps a lot and is frequently the only option. As it was already the case in waterfall times. On the other hand, there are also plenty of projects where the scope of work is tuned in order to get the work done. It is quite amazing how often the core requirements of a project were overestimated.

## Sprints

In Agile, the whole project is split up into sprints of one- or two-weeks length, called sprints. This results in regular feedback how the project is progressing. It allows the project manager to extrapolate the current progress and make rough estimates on how long it will take up to the next mile stone. This biweekly progress can also be used as a monitoring tool how well the development team is doing.

The first meeting of a spring is the sprint planning. It takes the whole team to discuss the tickets and which ones to scope into the sprint. The sprint planning for a two-week sprint may take a whole afternoon.

Part of the meeting is the planning game, where the story points for each ticket are estimated. This is required to plan the scope of the next sprint.

Next is the daily meeting. This one is not mandatory and it’s very short. It is kind of replacing the coffee machine gossip. Everyone very briefly says what he’s doing at the moment and if there are any blockers. There are no discussions in this meeting. Discussions are held afterwards.

Toward the end of the sprint, the software developers present their work done in the sprint presentation meeting. The idea of this meeting is for the stake holders to get an idea what the status of the software is. And hopefully, the developers are proud to present their work done.

The last meeting is the retro perspective. Here the team meets to discuss anything that could improve the productivity of the development. Issues why the ticket size was estimated wrongly, blockers that were not resolved for too long, unresolved MRs, etc.

## The end of the project

The project is apparently done, when all the work is done. Meaning when there are no more tickets around worth doing.

However, it’s not that simple. Frequently all tickets are done but the development team still finds work to do. Some missing test coverage or an obvious refactoring. This is to be praised. Yet at the same time one should not do too much work on a program that’s theoretically over. Go and have a beer instead. Enjoy the end of the project.

## Becoming agile

What I tried to explain in this chapter was supposed to be something like a manual how to become Agile. The real effort, however, lies before you. There is no Agile a manual. It is more like a schema. And you can stretch this schema in many possible directions, whether it makes sense or not.

The most important point from Agile is that you should figure out by yourself what works best. And be honest with yourself. It may be more convenient to work all by yourself for several weeks and hand in a pile of work in the end, than spending some time in meetings every two weeks. But you lack knowledge how you are progressing. And not only you, also your project manager would like to know how things are going. This is a pretty important aspect of Agile: you gain a lot of information about the progress of the project that will help you to further plan the rest of the work.

Furthermore, there are some things that are absolutely mandatory, when working agile. You are not planning the whole software anymore at once in the beginning. Instead, you have to be able to adapt. Your code has to be flexible. Your code would have to be flexible also in Waterfall, but that’s another story.

In order to be flexible, you have to be able to adapt your code. You have to change its structure. You have to refactor. This is a hard task as you’re probably afraid that you may break something. But it’s inevitable. You have to be able to change your code. That’s your job. Instead, you have to mitigate your fear of breaking the code. And the only way to do so are automated tests. Loads of it. Pretty much every single line of your code should be covered by a test. This is the only way how Agile can ever work out.

One quite controversial topic is the role of Agile coaches. Along with the advent of Agile, there was a demand from the industry for people with Agile experience or even Agile consulting, as no one knew how Agile really works out. But as always, there are many courses offering a certificate on Agile development after a two-day course. This is not really helpful.

On the other hand, there are also serious courses, including some project management. The idea that the development team is organizing itself independently may be too optimistic and some external help may be useful. In politics, independent organization frequently led to anarchy. Even though I hope that a team of software developers should do better.

## Agile = Courage + Feedback + Simplicity + Communication

// write also something about the other topics or leave this section away
### Courage

It takes a little bit of courage to work as a software engineer. If you are always afraid that your work could introduce bugs, that you could make mistakes. It is hard to keep up that courage. This has severe consequences. You’ll only make the changes you are absolutely sure they don’t introduce bugs. You’ll only add features and fix bugs that are absolutely necessary. You won’t touch a single line of code you don’t have to. This is absolutely dreadful! You will not refactor code because you are afraid you might break something. No one in the whole team will. No one will refactor your code. It will just keep rotting. Your project is doomed.

Instead you need something to keep your courage up. Something that takes you the fear of breaking stuff. That allows you to refactor code even though you are not exactly sure whether your refactoring really works or not. You need good test coverage. Good test coverage is the only thing that allows you to keep your courage and refactor code as you go. It is the only thing that can prevent your code from rotting. It is the only thing that can keep your productivity up.

You also need courage to be honest. The very first thing is you have to be able to say “No.” Your manager will ask you many questions throughout your career and he hopes you to say yes. But if the real answer is no, you have to tell him so. Lying to him and saying that you will be able to do something that you are not will not do you any good, nor will it to you manager. He’ll be making plans based on wrong assumptions that will not work out.

For the very same reason you have to be honest when estimating the time required for a certain problem. There is no worth giving your boss an estimate that is way too optimistic. This just won’t cut it. Try to be realistic. Multiply your estimate by 2 to make it even more realistic. Or give him the most honest answer there is: tell him that you don’t know how long it will take. 

# 44. Continuous integration

Software teams used to release a new version of their software every few months, sometimes even years, as I explained in the chapter on testing. The reason was the tremendous overhead required to make a release. All the sub projects had to be built, linked and packaged. Even worse, all the code had to be tested before every release. It was simply not possible to release more often with this amount of overhead every time.

Now the idea of Continuous Integration (CI) is to automate this whole process, allowing you to publish a nightly build if needed. You automate the whole build process. You write automated tests, both unit and acceptance tests. You automate absolutely everything you need in order to be sure you have a stable release.

CI is of paramount importance. Not only because of the daily release. It also creates a very short feedback loop. You get to your desk in the morning and you know right away whether all the code works fine or if the busy employee added a hack late at night and introduced a bug that his local unit tests did not catch. You might not be completely convinced, but I cannot overstate how important CI is for bigger projects.

It might have come apparent to you that automating things means using scripts everywhere. This is indeed the case. It might be a pain to you. It sounds like a lot of work. It would be much simpler to build everything with a few clicks instead and let everyone run their own tests. 

This is a perfectly fine argument, but it is missing the point. On the long term, this manual working style is eating up so much time. Spending a few days on a properly set up CI with build process, automated tests, etc. outweighs the initial costs by a lot. Explaining the setup to a new employee becomes straight forward. A build is just a single command away, same for testing, etc. The overhead for a new employee to get started becomes negligible.

As a rule of thumb: if your CI, build, testing, etc. is hard, you just didn’t get it right so far. Keep working on it until you get it right. Then it will feel super smooth. And you learned a great deal along the way.

The most commonly used tool at the time of writing for CI is Jenkins. It is web based ...?

# 45. Hiring and getting hired

// most of the recommendations here are from the book The Software Craftsman (by Sandro Mancuso)

That’s the moment you’ve all been looking for your whole life. Your first real job. The first position as a software engineer. But how do you get there? What is the process behind getting hired? Or rather, what should the process behind getting hired look like?

## Hiring

Let's say it frankly. Unfortunately, quite some job application processes suck. There’s no other way to put it. And the problem behind it is very simple. The application process is being led by a manager who likes numbers. He thinks that 5 years of professional Java development is a reasonable qualification. Even though there are developers with more than 10 years of experience who don’t manage to write reasonable code. They just never made the effort to learn anything by themselves. They keep writing the same old crap code they did 10 years ago. Meanwhile someone working for 3 different companies 1 year each probably has improved his programming skill significantly in the meantime.

Instead of the bulleted point lists of requirements, a company should rather describe in whole sentences what they are doing and who they are looking for.

Similar for the interviews. It’s about getting to know each other personally. This is a very hard task, but there’s no way around it. This is why many companies hire psychologists to support the HR processes. So, ask personal questions. What did you do at your previous job? What were the challenges? How did you get along with the previous work colleagues? There are hundreds such questions and to none of them you will find an answer on the CV. Make sure you don’t waste your time asking the standard Java questions. How can I create a memory leak? Etc. And if you do, make sure the Java version used for the questions is at least up to date.

Instead do some pair programming during the interview. Let the applicant bring his own laptop and give him internet access. He should be working on his laptop the way he’s used to. It’s not about testing his knowledge on the latest IDE or testing framework. It’s about finding out whether he’s smart and sharing the same coding values as you do. About having fruitful discussions on the code, you are just writing. It’s about simulating some real pair programming, as you will also do together if the applicant gets the job.

Search for applicants with that something extra. Developers who are working on some open source project in their free time. There’s hardly any better sign that someone is a very motivated and possibly also skilled programmer. Join one of these software development groups, possibly sponsor an even. This is a great opportunity to get to know other software developers and hire them without the tedious application process.

Keep recruiting all the time. This is a difficult task as the number of proficient programmers is too small to cover all the open positions. Thus, you can’t be too picky about when you are hiring your new team mate. If you have to hire someone under pressure, you’ll end up hiring someone who is not quite up to the task.

## Getting hired

Getting hired does not take quite as much knowhow as hiring someone. For the simple reason that you are getting invited and mostly follow the process. Yet at the same time you should always stay aware that you are an equal partner during the application procedure. If you don’t agree with something you may very well just leave the recruiting process.

As already written above, it’s about getting to know each other. Thus, you may also ask questions. In fact, you are expected to ask questions. If you don’t know what else to ask, ask the developer what he’s exactly working at and what kind of problems they are facing. This is something to get started with.

You shouldn’t take the application process too serious. Just stay yourself. They ask for 3 years of experience? Well, that’s what they wish for. But in reality, 2 years are usually enough if your application is otherwise convincing. Or if you’re living in an area with too few programmers around, which is basically all around the globe.

Make yourself seen with your application. Mention all kind of open source projects, blog posts and conferences you attended. This also makes a good start for the interview.

# 46. Work ethics

// see Clean Craftsmanship

Software engineers have a lot of responsibility. In the best case a bug is merely a nuisance, in the worst-case people may die. This responsibility is comparable to the one of doctors or accountants. Two highly regulated jobs, exactly for this reason. There are only few areas where software development is regulated. I know of aviation, cars, military and healthcare where very strict rules to the development of software apply. In other areas, the developer is free to do what his employer deems ok. Sometimes with fatal, or at least very costly consequences.

// list with software bugs that were expensive or fatal -> clean … ?

// we shall do no harm, etc.

// Working hours

//keep learning

# 47. Examples
So far, there was very little code in this book. Now I’d like to make one example, just to show you an application of some of the things we learned. Once again, I want to have a simple real-world project. Assume we have a robot and we are going to give it some instructions. It’s a smart robot that understands a lot of things, but the general planning we have to do ourselves.

## Apple pie

###  User story

Your father comes for dinner next Sunday and you want to make him happy. Creamy apple pie makes him happy, for example.
Acceptance criteria: your father is happy

Now let’s first write the acceptance test. If we invite our dad, he has to be happy.

In acceptance_tests/test_dinner.py

```
python dinner.py
// how to get the printed value?
Assert(expression.contains(“I’m so happy.”))
```
That’s it. We won’t have to touch the acceptance test anymore until the ticket is done. Note that I used the function contains to make the test a little more flexible. Your dad might say other things as well that we don’t care about.

The very first thing we do is running the test.

Pytest acceptance_tests

And we see that it fails. That was to be expected, we didn’t implement anything so far. But it was still worth the few milliseconds we spent here. There are better places where you can save time.

### Implementation

Let’s start with the implementation. It’s a fairly artificial example, so I can just make some assumptions. In the main function we create the apple pie and have our dad eat it. The big part of the work will be implementing the dad and the function to create the apple pie.
```
Apple_pie = create(“apple_pie”)
Dad Dad
Dad.eat(apple_pie)
```
Next we implement dad and then the create function.
```
Class Dad:
    Def Eat(food):
       If food.name == “apple_pie” and food.flavour == very_creamy
          Print(“I’m so happy”)
```

## Paint

Evans p.259

Idea: We want to define paint of certain color that we can mix with each other and change its color accordingly. I would like to make some comments to the implementation in the book mentioned above.
The code starts with a simple class paint and its variables.
```
class Paint:
	V: float
	R: int
	Y: int
	B: int
```
These member variables don’t have expressive names at all. They are renamed to
```
class Paint:
	Volume: float
	Red: int
	Yellow: int
	Blue: int
```

This can be further improved. The red, yellow and blue values all represent a color. They are all the same, while the volume has a clearly different meaning. Thus we can refactor the RYB colors into a dedicated object to fulfill the single responsibility principle.
```
class Paint:
	volume
	color
class Color:
	Red
	Yellow
	Blue
```
So far so good. We made some smaller refactoring and the basic data structure looks good to go. Now comes the very tricky question: how should the syntax of mixing two colors look like?
```
Paint a, b, c
C = add(a,b)
c.add(a)
```
The first is the procedural #? Way, the second is the object-oriented approach. Besides this fundamental question, we also have to figure out what kind of values a and b should have after this operation. Additionally, we also might want to find another name than add.

First, I would like to answer the conceptual question. What happens with a and b? This is a somewhat philosophical question and without knowing the actual problem we’d like to solve there is no clear answer. We can only reason about it.
```
Def add(paint1, paint2):
	Paint paint3
	volume = paint1.volume + paint2.volume
	Paint3.volume = volume
	Paint3.color.red = (Paint1.color.red* paint1.volume + Paint2.color.red* paint2.volume) / volume
Paint3.color.yellow = (Paint1.color. yellow * paint1.volume + Paint2.color. yellow * paint2.volume) /volume
Paint3.color.blue = (Paint1.color. blue * paint1.volume + Paint2.color. blue * paint2.volume) / volume
Return paint3
```
Now I see 3 different possibilities:
1.	We leave paint1 and paint2 as is. We used a copy of the actual paints and didn’t change the original paints.
1.	We set the volume of both paints to 0. This is the equivalent of mixing the two paints and being left with two empty canisters containing no paint at all.
1.	We set both paints to None. This would be somehow equivalent to throwing the canisters away.

As I said, all of them are perfectly reasonable choices. It is up to us to choose one of them, depending on what seems to be the most appropriate choice for each case. This also has consequences how we should call the add function and what the best way of implementing is.

For the first option, we don’t change neither paint1 nor paint2. Here it makes sense to call the function add or even define the + operator if possible, in your programming language of choice. This is a legitimate choice as we don’t expect add to change any of its function arguments.

Let’s assume that we choose option 2 and we’re left with 2 empty canisters of paint. Calling this function add is no longer an option. Instead we could call it mix or mix_in. Additionally, we have to deal with the question if we want to be more or less object oriented. We do have the following options:
```
Paint3 = mix(paint1, paint2)
Paint1.mix_in(paint2)
```
Now this is a matter of choice. A whole generation of programmers grew up hearing that the later option is the better one. It would be more natural. But honestly, I don’t see why this is supposed to be so super natural. As already seen, for case number 1 I clearly prefer the non-OO solution, simply because we are used to the add function not changing any function arguments while with the mix function, we have to take a look at the definition in order to be sure. Even here, I still opt for the first option. It just feels more natural to me as the function is symmetric, while the OO solution is asymmetric for no apparent reason.

The solution
`
Paint3 = mix(paint1, paint2)
`
Has one drawback. It creates a new object and it changes both function arguments. Now this is a very unfortunate solution. Changing one function argument is already bad enough and changing two is even worse. Now one solution would be passing a list of paints, `Paint3 = mix([paint1, paint2])`

Reasonable programming dictates that all list elements are treated equally and thus they are either all altered together or none at all. Furthermore, we can implement a mix function for any number of paints.

Still, in the end I’m preferring option 1 (not changing paint1 and paint2) and implementing a simple add function. This follows the general conventions and minimizes confusion. It follows the Single Responsibility Principle as it only adds the two paints and doesn’t alter anything else. Changing the volume of the function arguments can be done in a separate step, if needed.

And sorry folks, my preferred solution is not object-oriented, other than defining the pure data classes.

# More Copilot

The examples on Copilot shown throughout the code were all very short. This was done deliberately. Not only for the sake of keeping the problems easy to understand, but also in order to keep the suggestions from Copilot under control. Just as for a human developer, Copilot works best for incremental changes. It is not able to read your mind (even though sometimes it feels like it) and for complex changes it won't be able to make a correct suggestion. If there is a more difficult problem, Copilot frequently makes some undesired suggestions. The solution is to break down the problem into some smaller parts and maybe guide Copilot by writing the beginning of the code, i.e. the definition of a function.

Here is an example with a list of books. In the function `parse_line`, Copilot suggested `author, title = book.spilt(',')` which is wrong. It correctly anticipated that this list contains authors and titles of book. But interestingly enough, it didn't understand that the first and last names of the authors were split by a comma. Only after typing `last_name`, Copilot understood how the line should be parsed.

```py
books =["Rowling,J.K.,Harry Potter and the Philosopher's Stone",
        "Tolkien,JRR.,The Lord of the Rings",
        "Tolkien,JRR.,The Hobbit",
        "Martin,George R.R.,A Game of Thrones",
        "Martin,Robert C.,Clean Code",]

def parse_line(book):
    last_name, first_name, title = book.split(',')
    return f"{first_name} {last_name}: {title}"

print(parse_line(books[0]))
```

# 48. Further reading

I learned quite some things reading books, even though not as much as I did when thinking about and discussing code at work. Here are the books that I read so far:

Clean code (Robert C Martin) The best seller. Uncle Bob explains how good code should look like. I followed many of his rules, quite some of them are in a similar way in this book.

Clean architecture (Robert C Martin) ?

Clean Agile (Robert C Martin) It’s a fairly brief explanation how agile software development is supposed to work.

Software Engineering at Google (Winters et al.) They write extensively about testing at google. What else?

97 things every programmer should know (Kevlin Henney et al.)

Design patterns (Gamma et. Al) Probably one of the most influential software engineering books ever. It explains how classes can be combined to create some whole new functionality. Alternatively, you can also watch some youtube videos about the topic.

Domain-Dirven Design (Eric Evans) Certainly worth a read. But a tough one. Trying to understand what Evans wanted to explain made me understand a big deal and I learned a lot about the fundamentals of programming. Even if some parts of the book are clearly outdated.

Effective C++ (Scott Meyers) If you want to work with C++ this book is certainly worth a read. You learn quite something about the background and how to use the language. However, some parts are outdated and it’s not a book for beginners.

Effective modern C++ (Scott Meyers) Scott explains the ideas behind C++11 and 14. This is at the time of writing probably the more useful book. But only for advanced C++ programmers.

Working with legacy code (Michael Feathers) This book is about working with code that doesn’t have any tests and probably needs some refactoring.

The Pragmatic Programmer 2nd edition (Thomas, Hunt) This book is one of the inspirations to write my book here. It contains a lot of general advice on software development, tough ultimately only quite little of their recommendations made it into this book here.

Refactoring 2nd edition (Martin Fowler) Simply a great book on refactoring. The introductory example is simply amazing. Martin takes an innocent looking function and applies some of his refactoring steps. In the end there is some code that is super smooth. It has barely any indentations!

Software Engineering at google (Winters et al.)

Cheat sheet bbv, https://en.bbv.ch/publikationen-category/cheat-sheet-en/

google style guide, https://google.github.io/styleguide/

# 49. Outlook

"Programming is learned by writing programs." ― Brian Kernighan

Maybe you were surprised sometimes that there were so few code examples. But I hope you understood that they are not required. I wanted to explain fundamental concepts of software engineering. I wanted to give you an overview of the most important things to look out for. This should be a book that tells you the very basic rules that make your code better. There are not so many. But they are really important.

You might have realized that in software engineering for every problem there are a million of possible solutions. Even when writing these very simple examples in this book I have to reconsider how to do it best. For you it must be even worse. I remember how I was lost when I started programming. This book wants to help you. It explains a lot of things you shouldn’t do or use. It’s restricting you. I don’t want you to get lost.

Soon comes the next big step. The real world. Writing code. Finally, you are there. And I have to let you go. I could write another book with code examples and explain why some code is better than the other. But there are plenty such books and I doubt I know better examples than the other authors do.

Your next step will be to apply all the things you learned on your journey so far. Write code. As much as you can. And always try to improve it. How can you make it easier to understand? How should you break that class into pieces? How is the test coverage doing? There are so many things to look out for. There are so many obstacles along the way. Find a good programmer to help you overcome them. Or even better, do an internship. (But make sure they write tests before accepting the job.) Talking with other programmers is important to understand how you can change your code to make it better.
I hope you learned a lot of things that will help you in your life as a software engineer. Good luck!
Marco



# Abbreviations
API	Application Programmable Interface 
BDD	Behavior Driven Development
DB	Database
DI	Dependency injection
GUI	Graphical User Interface 
MR	Merge Request
OO	Object Oriented 
QA	Quality Assurance 
TDD	Test Driven Development 
YAGNI	You Aren’t Going Need It









