import sys
import networkx as nx
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

class GraphDisplay(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Graph Display")
        self.setGeometry(1000, 1000, 800, 800)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout(central_widget)
        self.canvas = GraphCanvas()
        layout.addWidget(self.canvas)

class GraphCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        self.fig, self.ax = plt.subplots(figsize=(width, height), dpi=dpi)
        super().__init__(self.fig)
        self.setParent(parent)
        self.graph = nx.Graph()
        self.draw_graph()

    def draw_graph(self):
        self.graph.clear()
        self.graph.add_node(1)
        self.graph.add_node(2)
        self.graph.add_edge(1, 2)
        self.graph.add_node(3)
        self.graph.add_edge(2, 3)
        self.graph.add_node(4)
        self.graph.add_edge(3, 5)
        self.graph.add_node(5)
        self.graph.add_edge(3, 5)
        self.graph.add_edge(4, 5)
        self.graph.add_edge(1, 4)
        self.graph.add_edge(4, 2)
        self.graph.add_node(6)
        self.graph.add_edge(6, 7)
        self.graph.add_node(7)
        self.graph.add_edge(7, 8)
        self.graph.add_node(8)
        self.graph.add_edge(8, 9)
        self.graph.add_node(9)
        self.graph.add_node(10)

        pos = nx.spring_layout(self.graph)
        nx.draw(self.graph, pos, ax=self.ax, with_labels=True, font_weight='bold', node_size=700, node_color='skyblue', edge_color='gray')
        self.ax.set_title('Graph Display')
        self.ax.autoscale(enable=True, axis='both', tight=True)
        self.ax.set_aspect('equal')
        self.ax.axis('off')
        self.draw()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GraphDisplay()
    window.show()
    sys.exit(app.exec_())
