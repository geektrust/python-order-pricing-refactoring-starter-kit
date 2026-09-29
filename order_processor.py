CAT_NAMES = ["Electronics", "Books", "Clothing"]
CAT_SHIP = [10, 0, 5]

PROMO_CODES = ["SAVE10", "TECH15", "READ25", "WINTER20"]
PROMO_DISCOUNT = [10, 15, 25, 20]
PROMO_ELIGIBLE_CATS = [
    "Electronics,Books,Clothing",
    "Electronics",
    "Books",
    "Clothing",
]


def process_order(s):
    a = s.split(" ")
    c = a[0]
    t = 0
    sh = 0
    seen = ""
    n = 0
    codes = []

    if c != "Regular" and c != "Member" and c != "VIP":
        print("INVALID CUSTOMER TYPE")
        return

    for i in range(1, len(a)):
        if a[i][0] == "+":
            codes.append(a[i][1:])
            continue

        b = a[i].split(":")
        cat = b[0]
        p = int(b[1])
        q = int(b[2])

        idx = -1

        for j in range(len(CAT_NAMES)):
            if CAT_NAMES[j] == cat:
                idx = j

        if idx < 0:
            print("INVALID CATEGORY")
            return

        if ("," + seen).find("," + cat + ",") < 0:
            n = n + 1

        seen = seen + cat + ","

        sh = sh + CAT_SHIP[idx] * q
        t = t + p * q

    d = 0

    if c == "Member":
        d = 10

    if c == "VIP":
        d = 20

    for i in range(len(codes)):
        pi = -1

        for j in range(len(PROMO_CODES)):
            if PROMO_CODES[j] == codes[i]:
                pi = j

        if pi < 0:
            print("INVALID PROMO CODE")
            return

        ok = True
        sl = seen.split(",")

        for k in range(len(sl)):
            if sl[k] == "":
                continue

            if ("," + PROMO_ELIGIBLE_CATS[pi] + ",").find("," + sl[k] + ",") < 0:
                ok = False

        if ok and PROMO_DISCOUNT[pi] > d:
            d = PROMO_DISCOUNT[pi]

    total = t - (t * d) / 100

    if c != "VIP" and n < 3:
        total = total + sh

    print("Order Total: " + format(total, ".2f"))
