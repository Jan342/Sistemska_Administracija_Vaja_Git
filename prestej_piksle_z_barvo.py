def prestej_piksle_z_barvo(slika: np.ndarray,
                           spodnja_meja: tuple[float, float, float],
                           zgornja_meja: tuple[float, float, float]) -> int:

    spodnja = np.array(spodnja_meja)
    zgornja = np.array(zgornja_meja)

    maska = np.all((slika >= spodnja) & (slika <= zgornja), axis=-1)

    return int(np.sum(maska))
