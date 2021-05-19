import networkx as nwx
import matplotlib.pyplot as plt
from dataclasses import dataclass
import imageio
import os
from random import *

import datetime
from MyGraph import Graph


RES_GRAPH_IMAGE_PREFIX = "test_graph_"  # for creating unique names of pictures in directory
STEP_NAME_PREFIX = "step_"
RES_PREFIX = "test_"
DEFAULT_DIRECTORY = "C:/"

GIF_OPTIONS = {'duration': 2}  # constantly set duration of result gif
DEFAULT_NODE_COLOR = 'b'
VISITED_NODE_COLOR = 'r'  # painting over node visited in algorithm in current color (red, default - blue)

NODES_SIZE = 1000  # size of circle nodes in result gif and pictures
ARROW_STYLE = "<|-"  # type of arrow in graph showing to user on result pictures and gif
TEXT_STYLE = "dashed"  # style of text in labels on nodes and edges of result visualization of graph

DELAY = 0.5  # delay of changing the rendering of the graph visualization
VARIABLES_NAME_DELIMETER = '_'  # const for parsing string name and creating test names for pytest


@dataclass
class GraphDrawer:

    @staticmethod
    def build_visual(graph: Graph, search_path: list, dir_name: str, show_in_ide: bool):
        # validating input directory name, if it is incorrect, raising a mistake
        if not os.path.isdir(dir_name):
            raise FileExistsError("Error: can't find entered directory")

        result_idx = GraphDrawer.create_result_dir_and_idx(dir_name)

        list_edges = graph.edges(data=False)
        node_names = [node for node in graph.nodes]
        color_list = [DEFAULT_NODE_COLOR for i in range(len(graph.nodes))]

        filenames = []
        pos = nwx.circular_layout(graph)

        GraphDrawer.redraw_graph_visual(graph, pos, color_list, list_edges, show_in_ide)

        for iter_num, node in enumerate(search_path):  # drawing dfs and bfs
            idx = node_names.index(node)
            color_list[idx] = VISITED_NODE_COLOR
            plt.clf()

            GraphDrawer.redraw_graph_visual(graph, pos, color_list, list_edges, show_in_ide)

            # generate path to file
            filename = GraphDrawer.create_res_path(dir_name, result_idx) + "//" +\
                       STEP_NAME_PREFIX + str(iter_num) + ".jpg"
            filenames.append(filename)  # save all the names of the pictures from which we create the gif

            plt.savefig(filename)

        gif = GraphDrawer.create_gif_result(filenames, dir_name, result_idx)

        return gif

    @staticmethod
    def create_result_dir_and_idx(dir_name: str):  # function for creating graph result directory and its index
        tmp_path = DEFAULT_DIRECTORY
        result_idx = 0
        while os.path.isdir(tmp_path):
            result_idx = int(datetime.datetime.now().timestamp())
            tmp_path = dir_name + "//" + RES_GRAPH_IMAGE_PREFIX + str(result_idx)
        os.mkdir(tmp_path)
        return result_idx

    @staticmethod
    def redraw_graph_visual(graph: Graph, pos: dict, color_list: list, list_edges: list, show_in_ide: bool):
        nwx.draw(graph, pos,
                 node_size=NODES_SIZE,
                 node_color=color_list,
                 with_labels=True,
                 arrowstyle=ARROW_STYLE, style=TEXT_STYLE)
        nwx.draw_networkx_edges(graph, pos, edgelist=list_edges,
                                node_size=NODES_SIZE,
                                arrowstyle=ARROW_STYLE, style=TEXT_STYLE)

        if show_in_ide:
            plt.draw()
            plt.pause(DELAY)  # delay in rendering

    @staticmethod
    def create_gif_result(filenames: list, dir_name: str, test_number: int):
        images = []
        for filename in filenames:
            images.append(imageio.imread(filename))
        # check, that there is no test with such number
        result_path = GraphDrawer.create_res_path(dir_name, test_number) + "//" + RES_PREFIX + str(test_number)
        if not os.path.isdir(result_path):
            # save it to the working directory and send it back to the program
            result_gif = imageio.mimsave(result_path + '.gif', images,
                                         'GIF', **GIF_OPTIONS)
        else:
            raise NameError("such gif-file named <" + RES_PREFIX + str(test_number) + "> already exists")

        return result_gif

    @staticmethod
    def create_res_path(dir_name: str, test_num: int):  # auxilary function for getting directory for result as str obj
        return dir_name + "//" + RES_GRAPH_IMAGE_PREFIX + str(test_num)

