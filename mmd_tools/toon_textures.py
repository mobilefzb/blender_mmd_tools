# -*- coding: utf-8 -*-
import bpy
import re

SIZE = [32, 32]

data = [
    [
        [32, 255, 255, 255],
    ],
    [
        [16, 205, 205, 205],
        [16, 255, 255, 255],
    ],
    [
        [16, 245, 225, 225],
        [16, 255, 255, 255],
    ],
    [
        [16, 154, 154, 154],
        [16, 255, 255, 255],
    ],
    [
        [16, 248, 239, 235],
        [16, 255, 255, 255],
    ],
    [
        [1, 254, 232, 223],
        [1, 255, 231, 222],
        [4, 255, 231, 221],
        [1, 255, 231, 222],
        [1, 255, 233, 224],
        [1, 255, 236, 229],
        [1, 255, 240, 234],
        [1, 255, 246, 242],
        [1, 255, 250, 248],
        [1, 255, 254, 254],
        [19, 255, 255, 255],
    ],
    [
        [6, 195, 172, 3],
        [1, 197, 174, 6],
        [1, 209, 187, 24],
        [1, 238, 218, 69],
        [1, 254, 235, 94],
        [10, 255, 237, 97],
        [1, 255, 242, 138],
        [1, 255, 254, 242],
        [1, 255, 246, 175],
        [1, 255, 238, 106],
        [8, 255, 237, 97],
    ],
    [
        [32, 255, 255, 255],
    ],
    [
        [32, 255, 255, 255],
    ],
    [
        [32, 255, 255, 255],
    ],
    [
        [32, 255, 255, 255],
    ],
]


def makeToonTextureName(toon_index):
    if 0 <= toon_index < 10:
        return 'toon%02d' % (toon_index + 1)
    else:
        return 'toon0'

def isToonTexture(texture):
    if texture.type != 'IMAGE':
        return False

    return (re.search('\\.bmp$', texture.image.name, flags=re.I) is not None
            and list(texture.image.size) == SIZE)

def isSharedToonTexture(texture):
    if texture.type != 'IMAGE':
        return False

    m = re.match('toon(0[0-9]?|10)$', texture.name)
    return (m is not None
            and texture.image.name == m.group(0) + '.bmp'
            and list(texture.image.size) == SIZE
            and texture.image.source == 'GENERATED')

def getSharedToonTexture(toon_index):
    idx = toon_index + 1 if 0 <= toon_index < 10 else 0
    name = makeToonTextureName(toon_index)

    texture = bpy.data.textures.get(name)
    if texture and isSharedToonTexture(texture):
        return texture

    width = SIZE[0]
    height = sum(r[0] for r in data[idx])

    tex = bpy.data.textures.new(name=name, type='IMAGE')
    tex.image = bpy.data.images.new(name=name+'.bmp', width=width, height=height, alpha=True)
    tex.image.pixels = [j / 255.0 for i in data[idx] for j in (i[1:] + [255]) * (i[0] * width)]

    return tex
