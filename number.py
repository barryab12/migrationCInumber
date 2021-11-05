MTN = [
    "04", "05", "06", "44", "45", "46", "54", "55", "56", "64", "65", "66",
    "74", "75", "76", "84", "85", "86", "94", "95", "96"
]
ORANGE = [
    "07", "08", "09", "47", "48", "49", "57", "58", "59", "67", "68", "69",
    "77", "78", "79", "87", "88", "89", "97", "98"
]
MOOV = [
    "01", "02", "03", "40", "41", "42", "43", "50", "51", "52", "53", "70",
    "71", "72", "73"
]


def migrate_number(number):
    network_name = ''
    number_length = len(number)
    if number_length < 8 or number_length > 13:
        print("Le numéro saisi est incorrect")
    else:
        if number_length >= 11:
            simple_number = number[-8::]
        else:
            simple_number = number
        number_prefix = simple_number[0:2]
        try:
            if number_prefix in MTN:
                network_name = 'MTN'
                new_number = "05{}".format(simple_number)
            elif number_prefix in MOOV:
                network_name = 'MOOV'
                new_number = "01{}".format(simple_number)
            elif number_prefix in ORANGE:
                network_name = 'ORANGE'
                new_number = "07{}".format(simple_number)
            else:
                print("Ce numéro de téléphone n'est pas encore repertorié")
        except:
            print('Erreur dans la donnees saisie')

        if len(network_name) > 0:
            print(
                "C'est un numéro du réseau {} de préfixe {}. Le nouveau numéro est : {}"
                .format(network_name, number_prefix, new_number))
        else:
            print("Cette numérotation n'appartient a aucun réseau en CI.")


if __name__ == "__main__":
    yes = ['o', 'O']
    rep = 'o'
    while (rep in yes):
        number = input('Saisissez le numéro de téléphone : \n')
        migrate_number(number)
        rep = input('Voulez-vous convertir un numéro ? (o/n) ')