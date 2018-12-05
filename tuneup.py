#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tuneup assignment"""

__author__ = "???"

import cProfile
import pstats
import timeit


def profile(func):
    """A function that can be used as a decorator to meausre performance"""

    def profile_function(*args, **kwargs):

        pr = cProfile.Profile()
        pr.enable()

        result = func(*args, **kwargs)

        pr.disable()

        sortby = 'cumulative'
        ps = pstats.Stats(pr).sort_stats(sortby)
        ps.print_stats()

        return result
    return profile_function


def read_movies(src):
    """Read a list of movie titles"""
    print('Reading file: {}'.format(src))
    with open(src, 'r') as f:
        return f.read().splitlines()


def is_duplicate(title, movies):
    """Case insensitive search within a list"""
    for movie in movies:
        if movie.lower() == title.lower():
            return True
    return False


@profile
def find_duplicate_movies(src):
    """Returns a list of duplicate movies from a src list"""
    movies = read_movies(src)
    duplicates = []
    while movies:
        movie = movies.pop()
        if is_duplicate(movie, movies):
            duplicates.append(movie)
    return duplicates


@profile
def find_duplicate_movies_improved(src):
    """Returns a list of duplicate movies from a src list"""
    movies = read_movies(src)
    duplicates = []
    movie_dict = {}
    for movie in movies:
        if movie in movie_dict:
            duplicates.append(movie)
        else:
            movie_dict[movie] = None
    return duplicates


def timeit_helper():
    """Part A:  Obtain some profiling measurements using timeit"""
    # YOUR CODE GOES HERE
    t = timeit.Timer("find_duplicate_movies('movies.txt')",
                     setup='from __main__ import find_duplicate_movies')
    repeat = 2
    number = 2
    result = min(t.repeat(repeat=repeat, number=number))/number
    print('Best time across {} repeats of {} runs per repeat: {} sec'.format(
        repeat, number, result))


def main():
    """Computes a list of duplicate movie entries"""
    result = find_duplicate_movies('movies.txt')
    find_duplicate_movies_improved('movies.txt')
    print('Found {} duplicate movies:'.format(len(result)))
    print('\n'.join(result))
    # timeit_helper()


if __name__ == '__main__':
    main()
