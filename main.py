parcels_amount = int(input("Podaj ilość paczek: "))
maximum_weight = 20
kilograms_sent = 0
parcel_weight = 0
stop_program = False
parcels_sent = 0
parcel_number = 1
biggest_gap_in_weight = maximum_weight
parcel_with_biggest_gap = 1

while not stop_program:
    element = input("Podaj wagę (lub 'q' aby zakończyć): ")
    if element.lower() == 'q':
        stop_program = True
    else:
        element = float(element)
        if element < 1 or element > 10:
            stop_program = True
        else:
            if parcel_weight + element > maximum_weight:
                if parcel_weight > 0:
                    if maximum_weight - parcel_weight > biggest_gap_in_weight:
                        biggest_gap_in_weight = maximum_weight - parcel_weight
                        parcel_with_biggest_gap = parcel_number
                    parcels_sent += 1
                    kilograms_sent += parcel_weight
                if parcels_sent == parcels_amount:
                    stop_program = True
                parcel_weight = 0
                parcel_number += 1
            parcel_weight += element
            '''biggest_gap_in_weight = maximum_weight - parcel_weight
            parcel_with_biggest_gap = parcel_number  
            wygląda na to że porównanie dla pustych paczek należy dodać po
            dodaniu elementu do paczki - ten kod liczy dobrze, ale za każdym razem bierze puste kg ostatniej paczki nie 
            porównując przez co if sprawdzający jest nadpisywany'''

if parcels_sent > 0 or stop_program:
    parcels_sent += 1
    kilograms_sent += parcel_weight
    print(f"Wysłano kilogramów: {kilograms_sent}")
    print(f"Ilość wysłanych paczek: {parcels_sent}")
    print(f"Suma pustych kilogramów: {parcels_sent * maximum_weight - kilograms_sent}")
    print(f"Paczka z najwieksza iloscia pustych kg: {parcel_with_biggest_gap}")
    if parcel_with_biggest_gap != 0:
        print(f"Najwięcej pustych kilogramów ma paczka {parcel_with_biggest_gap} ({biggest_gap_in_weight}kg)")
else:
    if parcels_sent == 0 and parcel_with_biggest_gap != 0:
        print(f"Najwięcej pustych kilogramów ma paczka {parcel_with_biggest_gap} ({biggest_gap_in_weight}kg)")
    else:
        print("Nie zostały wysłane żadne paczki.")