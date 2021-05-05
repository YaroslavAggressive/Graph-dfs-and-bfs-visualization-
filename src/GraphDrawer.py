import networkx as nwx
import matplotlib.pyplot as plt
import imageio
import os

TEMP_GRAPH_IMAGE_PREFIX = "test_graph_"  # for creating unique names of pictures in directory
STEP_NAME_PREFIX = "step_"
TEST_PREFIX = "test_"


class GraphDrawer:

    def __init__(self, dir_name: str):
        self.dir_name = dir_name

    def build_visual(self, graph: nwx.MultiDiGraph, search_path: list, test_num: int, show_in_ide: bool):
        # test_id - number of current test

        # check, that there is no test with such number
        if not os.path.isdir(self.dir_name + "//" + TEMP_GRAPH_IMAGE_PREFIX + str(test_num)):
            os.mkdir(self.dir_name + "//" + TEMP_GRAPH_IMAGE_PREFIX + str(test_num))
        else:
            # print("Error: such directory already exists, rename test number")
            # return None  # returns nothing yet, it is necessary to show user, that there is an mistake here
            raise NameError("such directory named <" + TEST_PREFIX + str(test_num) + "> already exists")

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
            plt.pause(0.5)  # задержка в отрисовке

        for node in search_path:  # рисование dfs и bfs на графике
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
                plt.pause(0.5)  # задержка в отрисовке

            # generate path to file
            filename = self.dir_name + "//" + TEMP_GRAPH_IMAGE_PREFIX + str(test_num) + "//" + STEP_NAME_PREFIX + str(iter_num) + ".jpg"
            filenames.append(filename)  # save all the names of the pictures from which we create the gif

            plt.savefig(filename)
            iter_num += 1

        gif = self.create_gif_result(filenames, test_num)

        return gif

    def create_gif_result(self, filenames: list, test_number: int):
        images = []
        for filename in filenames:
            images.append(imageio.imread(filename))
        options = {'duration': 2}
        # check, that there is no test with such number
        if not os.path.isdir(self.dir_name + "//" + TEMP_GRAPH_IMAGE_PREFIX + str(test_number) + "//" + TEST_PREFIX + str(test_number)):
            # save it to the working directory and send it back to the program
            result_gif = imageio.mimsave(self.dir_name + '//' + TEMP_GRAPH_IMAGE_PREFIX + str(test_number) + "//" + TEST_PREFIX + str(test_number) + '.gif', images,
                                         'GIF', **options)
        else:
            # print("Error: such directory already exists, rename test number")
            # return None  # returns nothing yet, it is necessary to show user, that there is an mistake here
            raise NameError("such gif-file named <" + TEST_PREFIX + str(test_number) + "> already exists")

        return result_gif
