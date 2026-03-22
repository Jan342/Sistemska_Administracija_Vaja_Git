def zmanjsaj_za_faktor_2(slika: np.ndarray) -> np.ndarray:

    visina, sirina = slika.shape[:2]

    if visina % 2 != 0:
        slika = slika[1:, :]
        visina -= 1

    if sirina % 2 != 0:
        slika = slika[:, 1:]
        sirina -= 1

    if slika.ndim == 2:

        nova = np.zeros((visina // 2, sirina // 2), dtype=slika.dtype)

        for y in range(0, visina, 2):
            for x in range(0, sirina, 2):

                blok = slika[y:y+2, x:x+2]
                nova[y//2, x//2] = np.mean(blok)

    else:

        kanali = slika.shape[2]
        nova = np.zeros((visina // 2, sirina // 2, kanali), dtype=slika.dtype)

        for y in range(0, visina, 2):
            for x in range(0, sirina, 2):

                blok = slika[y:y+2, x:x+2]
                nova[y//2, x//2] = np.mean(blok, axis=(0, 1))

    return nova
