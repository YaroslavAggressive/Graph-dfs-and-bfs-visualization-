import networkx as nwx
import matplotlib.pyplot as plt
from dataclasses import dataclass
import imageio
import os
from random import *

import datetime
from MyGraph import Graph


TEMP_GRAPH_IMAGE_PREFIX = "test_graph_"  # for creating unique names of pictures in directory
STEP_NAME_PREFIX = "step_"
TEST_PREFIX = "test_"

GIF_OPTIONS = {'duration': 2}  # constantly set duration of result gif
DEFAULT_NODE_COLOR = 'b'
VISITED_NODE_COLOR = 'r'  # painting over node visited in algorithm in current color (red, default - blue)

INDEX_LEFT_BOUND = 0  # randomly chosen borders of result images and gifs indexes, can be chosen later
INDEX_RIGHT_BOUND = 50


@dataclass
class GraphDrawer:

    dir_name: str = ""  # directory name, where user wants to save his visualization result
    result_idx: int = 0  # index, randomly generated for each function "build_visual" call

    def build_visual(self, graph: Graph, search_path: list, show_in_ide: bool):
        # check, that there is no test with such number

        # validating input directory name, if it is incorrect, raising a mistake
        if not os.path.isdir(self.dir_name):
            raise FileExistsError("Error: can't find entered directory")

        now = datetime.datetime.now()
        seed(now.second)
        self.result_idx = randint(INDEX_LEFT_BOUND, INDEX_RIGHT_BOUND)
        tmp_path = self.dir_name + "//" + TEMP_GRAPH_IMAGE_PREFIX + str(self.result_idx)
        while os.path.isdir(tmp_path):
            self.result_idx = randint(INDEX_LEFT_BOUND, INDEX_RIGHT_BOUND)
            tmp_path = self.dir_name + "//" + TEMP_GRAPH_IMAGE_PREFIX + str(self.result_idx)
        os.mkdir(tmp_path)

        list_edges = graph.edges(data=False)
        node_names = [node for node in graph.nodes]
        color_list = [DEFAULT_NODE_COLOR for i in range(len(graph.nodes))]
        iter_num = 1

        filenames = []
        pos = nwx.circular_layout(graph)
        nwx.draw(graph, pos,
                 node_size=1000,
                 node_color=color_list,
                 with_labels=True,
                 arrowstyle="<|-", style="dashed")
        nwx.draw_networkx_edges(graph, pos, edgelist=list_edges,
                                node_size=1000,
                                arrowstyle="<|-", style="dashed")
        if show_in_ide:
            plt.draw()
            plt.pause(0.5)  # delay in rendering

        for node in search_path:  # drawing dfs and bfs
            idx = node_names.index(node)
            color_list[idx] = VISITED_NODE_COLOR
            plt.clf()

            nwx.draw(graph, pos,
                     node_size=1000,
                     node_color=color_list,
                     with_labels=True,
                     arrowstyle="<|-", style="dashed")
            nwx.draw_networkx_edges(graph, pos, edgelist=list_edges,
                                    node_size=1000,
                                    arrowstyle="<|-", style="dashed")

            if show_in_ide:
                plt.draw()
                plt.pause(0.5)  # delay in rendering

            # generate path to file
            filename = self.dir_name + "//" + TEMP_GRAPH_IMAGE_PREFIX + str(self.result_idx) + "//" +\
                       STEP_NAME_PREFIX + str(iter_num) + ".jpg"
            filenames.append(filename)  # save all the names of the pictures from which we create the gif

            plt.savefig(filename)
            iter_num += 1

        gif = self.create_gif_result(filenames, self.result_idx)

        return gif

    def create_gif_result(self, filenames: list, test_number: int):
        images = []
        for filename in filenames:
            images.append(imageio.imread(filename))
        # check, that there is no test with such number
        test_path = self.dir_name + "//" + TEMP_GRAPH_IMAGE_PREFIX + str(test_number) + "//" + TEST_PREFIX + str(test_number)
        if not os.path.isdir(test_path):
            # save it to the working directory and send it back to the program
            result_gif = imageio.mimsave(test_path + '.gif', images,
                                         'GIF', **GIF_OPTIONS)
        else:
            raise NameError("such gif-file named <" + TEST_PREFIX + str(test_number) + "> already exists")

        return result_gif
