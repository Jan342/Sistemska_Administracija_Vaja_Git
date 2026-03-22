def razrezi_sliko(slika: np.ndarray, sirina_ps: int, visina_ps: int) -> list[np.ndarray]:

    visina, sirina = slika.shape[:2]
    podslike = []

  #  if sirina % sirina_ps != 0:
        #slika = slika[:, 1:]
        #sirina -= 1

    for y in range(0, visina, visina_ps):
        for x in range(0, sirina, sirina_ps):

            konec_y = min(y + visina_ps, visina)
            konec_x = min(x + sirina_ps, sirina)

            podslika = slika[y:konec_y, x:konec_x]
            podslike.append(podslika)

    return podslike

