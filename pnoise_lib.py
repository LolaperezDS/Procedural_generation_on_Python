from perlin_noise import PerlinNoise
import pygame


da = 128


def noise():
    output = []

    noise1 = PerlinNoise(octaves=4)
    noise2 = PerlinNoise(octaves=8)
    noise3 = PerlinNoise(octaves=16)
    noise4 = PerlinNoise(octaves=32)

    xpix, ypix = da, da

    for i in range(xpix):
        row = []
        for j in range(ypix):
            noise_val = noise1([i / xpix, j / ypix])
            noise_val += 0.5 * noise2([i / xpix, j / ypix])
            noise_val += 0.25 * noise3([i / xpix, j / ypix])
            noise_val += 0.125 * noise4([i / xpix, j / ypix])

            row.append(noise_val)
        output.append(row)
    min = 0

    for c in range(len(output)):
        for c1 in range(len(output[c])):
            output[c][c1] = (output[c][c1] + 0.875) ** 4

    return output   # -0.7419619625810207


class Slider:
    def __init__(self, pos, xp=0.5):
        self.pos = pos
        self.crossed = False
        self.width_rect = 400
        self.height_rect = 10
        self.xp = int(xp * 400)
        self.pressed = False

    def render(self, sc):
        pygame.draw.rect(sc, (255, 255, 255), (self.pos[0], self.pos[1] + 20, self.width_rect, self.height_rect))
        if self.crossed:
            pygame.draw.circle(sc, (0, 0, 0), (self.pos[0] + self.xp, self.pos[1] + 25), 15)
            pygame.draw.circle(sc, (255, 255, 255), (self.pos[0] + self.xp, self.pos[1] + 25), 12)
        else:
            pygame.draw.circle(sc, (255, 255, 255), (self.pos[0] + self.xp, self.pos[1] + 25), 15)
            pygame.draw.circle(sc, (0, 0, 0), (self.pos[0] + self.xp, self.pos[1] + 25), 12)

    def get_pos(self):
        return self.xp / 400

    def crossing(self, mousepos):
        x1, y1 = mousepos
        x2, y2, w2, h2 = self.pos[0] + self.xp - 15, self.pos[1] + 10, self.pos[0] + self.xp + 15, self.pos[1] + 40
        if x2 <= x1 <= x2 + w2 and y2 <= y1 <= y2 + h2:
            self.crossed = True
            return True
        self.crossed = False
        return False

    def press(self):
        self.pressed = True

    def unpress(self):
        self.pressed = False


if __name__ == '__main__':
    print(noise())
