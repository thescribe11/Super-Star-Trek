from SST import Enterprise


def test_enterprise() -> None:
    ent = Enterprise()

    ent.svert = 5
    ent.shoriz = 5
    ent.gvert = 5
    ent.ghoriz = 5

    ent.sector = [['.' for i in range(10)] for i in range(10)]
    ent.sector_current = True
    ent.sector[ent.svert][ent.shoriz] = '@'

    for i in ent.sector:
        print(i)

    ent.impulse_move(0.5, 2, 1)
    assert ent.svert == 7
    assert ent.shoriz == 6

    for i in ent.sector:
        print(i)

    ent.svert = 5
    ent.shoriz = 5

    ent.impulse_move(-0.5, 2, -1)
    assert ent.svert == 7
    assert ent.shoriz == 4
    print(f"{ent.svert=}")
    print(f"{ent.shoriz=}")

    ent.svert = 5
    ent.shoriz = 5
    ent.impulse_move(2, 2, 4)
    assert ent.svert == 7
    assert ent.shoriz == 9
    print(f"{ent.svert=}")
    print(f"{ent.shoriz=}")
    for i in ent.sector:
        print(i)

    ent.svert = 5
    ent.shoriz = 5
    ent.impulse_move(2, -2, -4)
    print(f"{ent.svert=}, {ent.shoriz=}")
    assert ent.svert == 3, f"{ent.svert=}"
    assert ent.shoriz == 1, f"{ent.shoriz=}"

    for i in ent.sector:
        print(i)

    ent.svert = 5
    ent.shoriz = 5
    ent.sector = [['.' for i in range(10)] for i in range(10)]
    ent.sector_current = True
    ent.sector[ent.svert][ent.shoriz] = 'E'
    print("\n***** Inter-quadrant movement *****")
    print(f"{ent.gvert=}, {ent.ghoriz=}")

    print("** Begin movement")
    ent.impulse_move(1, 10, 10)
    assert ent.gvert == 6, "Gvert test #1 has failed!"
    assert ent.ghoriz == 6, "Ghoriz test #1 has failed!"



if __name__ == '__main__':
    test_enterprise()
