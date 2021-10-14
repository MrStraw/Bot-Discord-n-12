from contents.douziens import douziens


def nick_mc_to(pseudo: str):
    nick = douziens.get(pseudo, None)
    if nick is None:
        return pseudo
    else:
        return nick[1]
