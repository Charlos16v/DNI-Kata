from src.dni import Dni
from src.tabla_asignacion import TablaAsignacion
import pytest

#casosTest = [    "78484464T","72376173A","01817200Q","95882054E","63587725Q",
#				 "26861694V","21616083Q","26868974Y","40135330P","89044648X",
#				 "80117501Z","34168723S","76857238R","66714505S","66499420A"]


def test_getLetra():
	assert TablaAsignacion.getLetra(self, 0) == "T"
