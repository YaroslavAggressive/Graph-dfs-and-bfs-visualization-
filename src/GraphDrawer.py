import networkx as nwx
import matplotlib.pyplot as plt
from dataclasses import dataclass
import imageio
import os
from MyGraph import MyGraph

TEMP_GRAPH_IMAGE_PREFIX = "test_graph_"  # for creating unique names of pictures in directory
STEP_NAME_PREFIX = "step_"
TEST_PREFIX = "test_"


@dataclass
class GraphDrawer:

    dir_name: str = ""
    tests_counter: int = 1

    def build_visual(self, graph: MyGraph, search_path: list, show_in_ide: bool):
        # check, that there is no test with such number
        test_path = self.dir_name + "//" + TEMP_GRAPH_IMAGE_PREFIX + str(GraphDrawer.tests_counter)
        os.mkdir(test_path)

        list_edges = graph.edges(data=False)
        node_names = [node for node in graph.nodes]
        color_list = ['b' for i in range(len(graph.nodes))]
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
            color_list[idx] = 'r'
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
            filename = self.dir_name + "//" + TEMP_GRAPH_IMAGE_PREFIX + str(GraphDrawer.tests_counter) + "//" +\
                       STEP_NAME_PREFIX + str(iter_num) + ".jpg"
            filenames.append(filename)  # save all the names of the pictures from which we create the gif

            plt.savefig(filename)
            iter_num += 1

        gif = self.create_gif_result(filenames, GraphDrawer.tests_counter)
        GraphDrawer.tests_counter += 1

        return gif

    def create_gif_result(self, filenames: list, test_number: int):
        images = []
        for filename in filenames:
            images.append(imageio.imread(filename))
        options = {'duration': 2}
        # check, that there is no test with such number
        test_path = self.dir_name + "//" + TEMP_GRAPH_IMAGE_PREFIX + str(test_number) + "//" + TEST_PREFIX + str(test_number)
        if not os.path.isdir(test_path):
            # save it to the working directory and send it back to the program
            result_gif = imageio.mimsave(test_path + '.gif', images,
                                         'GIF', **options)
        else:
            raise NameError("such gif-file named <" + TEST_PREFIX + str(test_number) + "> already exists")

        return result_gif
