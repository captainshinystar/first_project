from formula import Formula
from ingredient import *
from ingredient_list import *

pain_cream1 = Formula(
    "Pain Cream",
     [keta_letco, lido_fagron, gaba_kalchem, lipopen],
     [10, 10, 10, 100]
)

prog_cream1 = Formula(
    "Progesterone Cream",
    [prog_letco, hrt_heavy],
    [10, 100]
)

test_cream1 = Formula(
    "Testosterone Cream",
    [test_pharmasource, hrt_heavy],
    [10, 100]
)


formula_list = [
    pain_cream1,
    prog_cream1,
    test_cream1,
]