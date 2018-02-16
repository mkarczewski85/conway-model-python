import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


class ConwaySimulation:

    def __init__(self, size=100):
        self.ALIVE = 1  # wartość dla żywej komórki
        self.DEAD = 0  # wartość dla martwej komórki
        self.size = size
        values = [self.ALIVE, self.DEAD]
        self.world = np.random.choice(values, size * size, p=[0.2, 0.8]).reshape(size, size)

    def compute(self):
        updated_world = self.world.copy()
        s = self.size
        for i in range(s):
            for j in range(s):
                neighbors = (self.world[(i - 1) % s, j] +  # sąsiedztwo N
                             self.world[(i + 1) % s, j] +  # sąsiedztwo S
                             self.world[i, (j - 1) % s] +  # sąsiedztwo W
                             self.world[i, (j + 1) % s] +  # sąsiedztwo E
                             self.world[(i - 1) % s, (j - 1) % s] +  # sąsiedztwo NW
                             self.world[(i - 1) % s, (j + 1) % s] +  # sąsiedztwo NE
                             self.world[(i + 1) % s, (j - 1) % s] +  # sąsiedztwo SW
                             self.world[(i + 1) % s, (j + 1) % s])  # sąsiedztwo SE
                if self.world[i, j] == self.ALIVE:
                    if (neighbors < 2) or (neighbors > 3):  # warunek śmierci żywej komórki
                        updated_world[i, j] = self.DEAD
                else:
                    if neighbors == 3:  # warunek wskrzeszenia martwej komórki
                        updated_world[i, j] = self.ALIVE

        self.world = updated_world
        return self.world


##############################################################################################


plt.rcParams['animation.ffmpeg_path'] = 'D:\\ffmpeg-20180202-caaa40d-win64-static\\bin\\ffmpeg.exe'
simulation = ConwaySimulation()
fig, ax = plt.subplots()
mat = ax.matshow(simulation.world, cmap="Greys")


def update(frame):
    grid = simulation.compute()
    mat.set_data(grid)
    return [mat]


def main():
    ani = animation.FuncAnimation(fig, update, interval=50, save_count=50, frames=1000)
    ani.save('conway.mp4', writer=animation.FFMpegFileWriter(), dpi=150)
    # plt.show()


if __name__ == '__main__':
    main()
