cmake_minimum_required(VERSION 4.1)
project(DieBasicsDerInformatik C)

set(CMAKE_C_STANDARD 11)

include_directories(Aufgabe04)

add_executable(DieBasicsDerInformatik
        Aufgabe01/solution.c
        Aufgabe02/solution.c
        Aufgabe03/solution.c
        Aufgabe04/input.c
        Aufgabe04/input.h
        Aufgabe04/solution.c
        Aufgabe05/solution.c)
