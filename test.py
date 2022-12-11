from f1 import even_odd as eo


def test1(word):
    x = eo(word)
    test_x = True
    if len(word) % 2 == 0:
        test_x = True
    else:
        test_x = False
    print (test_x == x)

test1('fsd')
test1(324234)