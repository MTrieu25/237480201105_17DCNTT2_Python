sinhvien = []

def themSV(ma, ten):
    for sv in sinhvien:
        if sv["ma"] == ma:
            return False
    sinhvien.append({"ma": ma, "ten": ten})
    return True


def xoaSV(ma):
    for sv in sinhvien:
        if sv["ma"] == ma:
            sinhvien.remove(sv)
            return True
    return False


def suaSV(ma, ten_moi):
    for sv in sinhvien:
        if sv["ma"] == ma:
            sv["ten"] = ten_moi
            return True
    return False


def xemDS():
    return sinhvien
