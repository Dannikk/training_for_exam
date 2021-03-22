import os
from numpy import *


class DirReader:
    def __init__(self, file_path):
        self.file_path = file_path

    def generator(self):
        for root, dirs, files in os.walk(self.file_path):
            if files:
                for file in files:
                    if len(file) > 11:
                        yield root + "\\" + file

    def __enter__(self):
        return self.generator()


    def __exit__(self, exc_type, exc_val, exc_tb):
        print("exiting")
        return 0

    # def __iter__(self):
    #     return self.generator()


def graph_builder(files: str):
    G = {}
    for file_path in files:
        print(file_path)
        with open(file_path, "r") as file:
            file.readline()
            for row in file:
                names = list(set(get_names(row)))
                G = graph_append(G, names)


def graph_append(graph: dict, names: list):
    for name in names:
        if name not in graph:
            # как было
            graph[name] = names
            # как буд делать
            # graph[name] = names
        else:
            # костыль, которым решалась проблема
            # a = graph[name].copy()
            # a.extend(names)
            # graph[name] = a
            print(type(graph[name]))
            graph[name].extend(names) # а чо не работает?
    return graph


def graph_iterator():
    ...

def get_names(research):
    names = research.split('\t')[:-1]
    return names


path_name = "../data"
with DirReader(path_name) as files:
    print(type(files))
    # for file in files:
    #     print(file)
    graph_builder(files)
