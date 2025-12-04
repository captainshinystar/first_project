from ingredient import *


keta_letco = API("ketamine", "Letco", 50)
keta_pharmasource = API("ketamine", "Pharmasource", 50)
lido_fagron = API("lidocaine", "Fagron", 50)
lido_medisca = API("lidocaine", "Medisca", 50)
gaba_medisca = API("gabapentin", "Medisca", 50)
gaba_kalchem = API("gabapentin", "Kalchem", 50)
prog_letco = API("progesterone", "Letco", 50)
prog_pharmasource = API("progesterone", "Pharmasource", 50)
test_letco = API("testosterone", "Letco", 50)
test_pharmasource = API("testosterone", "Pharmasource", 50)

phytobase = CreamBase("phytobase", "Fagron", 500, Type.HORMONE)
hrt_heavy = CreamBase("HRT Heavy", "Fagron", 500, Type.HORMONE)
lipopen = CreamBase("lipopen", "Fagron", 500, Type.PAIN)
lipoderm = CreamBase("lipoderm", "PCCA", 500, Type.PAIN)

ing_list = [
    keta_letco,
    keta_pharmasource,
    lido_fagron,
    lido_medisca,
    gaba_medisca,
    gaba_kalchem,
    prog_letco,
    prog_pharmasource,
    test_letco,
    test_pharmasource,
    phytobase,
    hrt_heavy,
    lipopen,
    lipoderm
]