def transferir(cuentas, origen, destino, monto):
    if origen not in cuentas or destino not in cuentas:
        raise ValueError("La cuenta no existe")
    if origen == destino:
        raise ValueError("Las cuentas de origen y destino deben ser diferentes")
    if monto <= 0:
        raise ValueError("El monto debe ser mayor que cero")
    if cuentas[origen] < monto:
        raise ValueError("Saldo insuficiente")

    cuentas[origen] -= monto
    cuentas[destino] -= monto
    return True

