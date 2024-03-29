from enum import Enum

MAX_WIDTH = "900px"
IMAGE_HEIGHT = "200px"

class EmSize(Enum):
    DEFAULT = "1em" # 16px/1em
    MEDIUM = "2em"
    BIG = "4em"

class Size(Enum):
    ZERO = "0"
    SMALL = "2"
    DEFAULT = "4" # 16px/1em
    MEDIUM = "6"
    BIG = "8"