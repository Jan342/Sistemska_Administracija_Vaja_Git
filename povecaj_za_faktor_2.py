def povecaj_za_faktor_2(slika: np.ndarray) -> np.ndarray:

    if slika.ndim == 2:
        visina, sirina = slika.shape
        nova = np.zeros((visina * 2, sirina * 2), dtype=slika.dtype)

        for y in range(visina):
            for x in range(sirina):
                nova[2*y:2*y+2, 2*x:2*x+2] = slika[y, x]

    else:
        visina, sirina, kanali = slika.shape
        nova = np.zeros((visina * 2, sirina * 2, kanali), dtype=slika.dtype)

        for y in range(visina):
            for x in range(sirina):
                nova[2*y:2*y+2, 2*x:2*x+2, :] = slika[y, x]

    return nova
