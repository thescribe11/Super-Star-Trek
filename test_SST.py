from SST import Enterprise
import math


def test_check_movement_collision():
    pass


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
    print('\n***** Inter-quadrant movement *****\n')
    print(f'{ent.gvert=}, {ent.ghoriz=}')

    print('\n** Begin movement check #1 (direction: +):')
    ent.impulse_move(1, 10, 10)
    assert ent.gvert == 6, '[**ERROR**]: Gvert test #1 has failed!'
    assert ent.ghoriz == 6, '[**ERROR**]: Ghoriz test #1 has failed!'

    ##  CLEANUP  ##
    ent.gvert = 5
    ent.ghoriz = 5
    ent.svert = 5
    ent.shoriz = 5
    ##  END CLEANUP  ##

    print('\n** Begin movement check #2 (direction: -):')
    ent.impulse_move(1, -10, -10)
    assert ent.gvert == 4, '[**ERROR**]: Gvert test #2 has failed!'
    assert ent.ghoriz == 4, '[**ERROR**]: Ghoriz test #2 has failed!'

    ##  CLEANUP  ##
    ent.gvert = 5
    ent.ghoriz = 5
    ent.svert = 5
    ent.shoriz = 5
    ##  END CLEANUP  ##

    print('\n** Begin movement check #3 (direction: v-):')
    ent.impulse_move(0, -10, 0)
    assert ent.gvert == 4, '[**ERROR**]: Gvert test #3 has failed!'
    assert ent.ghoriz == 5, '[**ERROR**]: Ghoriz test #3 has failed!'

    ##  CLEANUP  ##
    ent.gvert = 5
    ent.ghoriz = 5
    ent.svert = 5
    ent.shoriz = 5
    ##  END CLEANUP  ##

    print('\n** Begin movement check #4 (direction: v+):')
    ent.impulse_move(0, 10, 0)
    assert ent.gvert == 6, '[**ERROR**]: Gvert test #4 has failed!'
    assert ent.ghoriz == 5, '[**ERROR**]: Ghoriz test #4 has failed!'

    ##  CLEANUP  ##
    ent.gvert = 5
    ent.ghoriz = 5
    ent.svert = 5
    ent.shoriz = 5
    ##  END CLEANUP  ##

    print('\n** Begin movement check #5 (horizontal +):')
    ent.impulse_move(math.inf, 0, 2)
    assert ent.shoriz == 7, f'[**ERROR**]: Horizontal Shoriz test #1 failed! {ent.shoriz=}'
    assert ent.svert == 5, '[**ERROR**]: Horizontal Svert test #1 failed!'

    for i in ent.sector:
        print(i)

    ##  CLEANUP  ##
    ent.gvert = 5
    ent.ghoriz = 5
    ent.svert = 5
    ent.shoriz = 5
    ##  END CLEANUP  ##

    print('\n** Begin movement check #6 (horizontal -):')
    ent.impulse_move(math.inf, 0, -4)
    assert ent.shoriz == 1, '[**ERROR**]: Horizontal Shoriz test #2 failed!'

    ##  CLEANUP  ##
    ent.gvert = 5
    ent.ghoriz = 5
    ent.svert = 5
    ent.shoriz = 5
    ##  END CLEANUP  ##

    print('\n** Begin movement check #7 (horizontal ++):')
    ent.impulse_move(math.inf, 0, 20)
    print(f'{ent.ghoriz=}')
    assert ent.ghoriz == 7, '[**ERROR**]: Horizontal Ghoriz test #3 failed!'
    # Well, I fixed the in-quadrant movement, but now inter-quadrant movement is having problems.

    ##  CLEANUP  ##
    ent.gvert = 5
    ent.ghoriz = 5
    ent.svert = 5
    ent.shoriz = 5
    ##  END CLEANUP  ##

    print('\n** Begin movement check #8 (horizontal --):')
    ent.impulse_move(math.inf, 0, -20)
    print(f'{ent.ghoriz=}')
    assert ent.ghoriz == 3, '[**ERROR**]: Horizontal Ghoriz test #4 failed!'


if __name__ == '__main__':
    test_enterprise()
