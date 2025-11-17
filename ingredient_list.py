from ingredient import *
from enum import Enum


keta_letco = API("ketamine", "Letco", 500)
keta_pharmasource = API("ketamine", "Pharmasource", 500)
lido_fagron = API("lidocaine", "Fagron", 1000)
lido_medisca = API("lidocaine", "Medisca", 500)
gaba_medisca = API("gabapentin", "Medisca", 500)
gaba_kalchem = API("gabapentin", "Kalchem", 500)
keto_letco = API("ketoprofen", "Letco", 1000)
prog_letco = API("progesterone", "Letco", 1000)
prog_pharmasource = API("progesterone", "Pharmasource", 1000)
test_letco = API("testosterone", "Letco", 1000)
test_pharmasource = API("testosterone", "Pharmasource", 1000)
e2_pharmasource = API("estradiol", "Pharmasource", 100)
e3_pharmasource = API("estriol", "Pharmasource", 100)


phytobase = CreamBase("phytobase", "Fagron", 4500, Type.HORMONE)
hrt_heavy = CreamBase("HRT Heavy", "Fagron", 4500, Type.HORMONE)
lipopen = CreamBase("lipopen", "Fagron", 2000, Type.PAIN)
lipoderm = CreamBase("Lipoderm", "PCCA", 1000, Type.PAIN)
emollient = CreamBase("emollient", "Letco", 500, Type.DERM)
Vanishing = CreamBase("versitile vanishing cream", "Fagron", 500, Type.DERM)
