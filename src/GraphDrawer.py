import networkx as nwx
import matplotlib.pyplot as plt
import imageio
import os


class GraphDrawer:

    def __init__(self, graph: dict, search_path: list):
        self.graph = nwx.DiGraph(graph)
        self.search_path = search_path

    def build_visual(self, test_num: int, show_in_ide: bool):  # test_id - номер теста, чтобы не путаться

        if not os.path.isdir("test_images//test_graph_" + str(test_num)):  # проверка, не был ли уже создан тест с таким номером
            os.mkdir("test_images//test_graph_" + str(test_num))
        else:
            print("Error: such directory already exists, rename test number")
            return None  # пока ничего не возвращаем, не был начат процесс визуализации

        node_names = [node for node in self.graph.nodes]
        color_list = ['b' for i in range(len(self.graph.nodes))]
        iter_num = 1

        filenames = []

        nwx.draw_circular(self.graph,
                          node_color='b',
                          node_size=1000,
                          with_labels=True)
        if show_in_ide:
            plt.draw()
            plt.pause(0.5)  # задержка в отрисовке
        tmp_num = 0
        for node in self.search_path:  # рисование dfs и bfs на графике
            idx = node_names.index(node)
            color_list[idx]='r'
            plt.clf()

            nwx.draw_circular(self.graph,
                              node_size=1000,
                              with_labels=True,
                              node_color=color_list)

            if show_in_ide:
                plt.draw()
                plt.pause(0.5)  # задержка в отрисовке

            filename = "test_images//test_graph_" + str(test_num) + "//step_" + str(iter_num) + ".jpg"  # генерируем путь до файла
            filenames.append(filename)  # сохраним все имена картинок, из которых лепим гифку

            plt.savefig(filename)
            iter_num += 1

        gif = self.create_gif_result(filenames, test_num=test_num)

        return gif

    @staticmethod
    def create_gif_result(filenames: list, test_num: int):
        images = []
        for filename in filenames:
            images.append(imageio.imread(filename))
        options = {'duration': 2}
        if not os.path.isdir("test_images//test_graph_" + str(test_num) + "//test_" + str(test_num) + ".gif"):  # проверка, не был ли уже создан тест с таким номером
            result_gif = imageio.mimsave('test_images//test_graph_''' + str(test_num) + '//test_' + str(test_num) + '.gif', images,
                                         'GIF', **options)  # сохраняем в рабочую директорию и отдаем обратно в программу
        else:
            print("Error: such directory already exists, rename test number")
            return None  # пока ничего не возвращаем, не был начат процесс визуализации

        return result_gif
