import os


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
        # print("exiting")
        return 0


def graph_builder(files: str):
    G = {}
    for file_path in files:
        # print(file_path)
        with open(file_path, "r") as file:
            _ = file.readline()
            for row in file:
                names = list(set(get_names(row)))
                G = graph_append(G, names)
    return G


def graph_append(graph: dict, names: list):
    for name in names:
        if name not in graph:
            graph[name] = names.copy()
        else:
            graph[name].extend(names)  # а чо не работает?
    return graph


def iter_decorator(g_iter=None, *, output="res_1.txt"):
    print("iter_decorator:")
    if g_iter is None:
        print("g_iter is None:")
        return lambda g_iter: iter_decorator(g_iter, output=output)
    print("g_iter is not None:")
    def wrapper(graph):
        print("wrapper:")
        out_fl = open(output, "w")
        for i, j in g_iter(graph):
            print(i, j, file=out_fl)
            yield i, j
        out_fl.close()
    return wrapper


@iter_decorator(output="resss_2.txt")
class GraphIterator:
    def __init__(self, g: dict):
        self.graph = g
        self.weights = [(scientists.count(name), name) for name, scientists in self.graph.items()]

    def __iter__(self):
        return self.generator()

    def generator(self):
        self.weights.sort(reverse=True)
        for name, count in self.weights:
            yield name, count


def get_names(research):
    names = research.split('\t')[:-1]
    return names


path_name = "../data"
with DirReader(path_name) as files:
    # for file in files:
    #     print(file)
    graph = graph_builder(files)
    # output = open("result.txt", "w")
    file = "results.txt"
    git = GraphIterator(graph)
    for i, j in git:
        print("Result: ", i, j)
    # output.close()

# def decor(func):
#     def wrapper(g_iter):
#         print("wrapper")
#         f = func(g_iter)
#         print(f)
#         return f
#     return wrapper
#
#
# class Tmp:
#     def __init__(self, x, y):
#         self.x, self.y = x, y
#
#     @decor
#     def function(self):
#         print("func")
#         return self.x*self.y + self.x + self.y
#
# tmp = Tmp(1, 2)
# print(tmp.function())


# def decor(g_iter):
#     def wrapper(*args):
#         print("wrapper:")
#         for i in args:
#             print(type(i))
#         # f = func(g_iter)
#         # print(f)
#         return args[0]
#
#     return wrapper
#
#
# @decor
# class Tmp:
#     def __init__(self, x, y):
#         self.x, self.y = x, y
#
#     def function(self):
#         print("func:")
#         return self.x * self.y + self.x + self.y
#
#
# tmp = Tmp(1, 2)
# print("print:", type(tmp))


