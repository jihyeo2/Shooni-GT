from .uhmidtown import UHMidtown
from .standard import Standard
from .modera import Modera
from .bowerwestside import BowerWestside

Individual = [
    UHMidtown(),
    Standard(),
    Modera(),
    BowerWestside(),
]

AllApartments = Individual