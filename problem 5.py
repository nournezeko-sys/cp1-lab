
def transfer_air(source, target, amount):

    old_pressure = source.get_bar()

    source.release(amount)

    new_pressure = source.get_bar()

    if old_pressure - new_pressure == amount:
        target.fill(amount)


