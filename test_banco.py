import pytest
from banco import transferir
def test_transferencia_valida():
    cuentas = {"A": 10000, "B": 5000}
    assert transferir(cuentas, "A", "B", 3000) is True
    assert cuentas == {"A": 7000, "B": 8000}
def test_saldo_insuficiente():
    cuentas = {"A": 10000, "B": 5000}
    with pytest.raises(ValueError, match="Saldo insuficiente"):
        transferir(cuentas, "A", "B", 12000)
    assert cuentas == {"A": 10000, "B": 5000}
@pytest.mark.parametrize(
    ("origen", "destino"),
    [("INEXISTENTE", "B"), ("A", "INEXISTENTE")],
)
def test_cuenta_inexistente(origen, destino):
    cuentas = {"A": 10000, "B": 5000}
    with pytest.raises(ValueError, match="La cuenta no existe"):
        transferir(cuentas, origen, destino, 1000)
    assert cuentas == {"A": 10000, "B": 5000}
def test_transferencia_a_la_misma_cuenta():
    cuentas = {"A": 10000, "B": 5000}
    with pytest.raises(ValueError, match="deben ser diferentes"):
        transferir(cuentas, "A", "A", 1000)
    assert cuentas == {"A": 10000, "B": 5000}
@pytest.mark.parametrize("monto", [0, -100])
def test_monto_no_positivo(monto):
    cuentas = {"A": 10000, "B": 5000}

    with pytest.raises(ValueError, match="mayor que cero"):
        transferir(cuentas, "A", "B", monto)

    assert cuentas == {"A": 10000, "B": 5000}
    
    
    