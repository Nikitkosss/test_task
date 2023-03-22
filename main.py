from dadata import Dadata

address_location_dict = {}
address = ""
location = ""
token = ""
dadata = Dadata(token)


def coordinations(dict):
    geo_lat = ""
    geo_lon = ""
    for key, value in dict.items():
        if key == "geo_lat":
            geo_lat = value
            # print(value)
        if key == "geo_lon":
            geo_lon = value
    return f"Широта: {geo_lat}, Долгота: {geo_lon}"


def address_location(result):
    for dict in result:
        for key, value in dict.items():
            if key == "value":
                address = value
                print(address)
            if key == 'data':
                location = coordinations(value)
                address_location_dict[address] = location


def f_exact_address(exact_address):
    if exact_address in address_location_dict.keys():
        return address_location_dict[exact_address]
    else:
        return "Такого адреса нет среди предложенных"


def main():
    while True:
        input_address = input("Введите адрес или exit для завершения работы: ")
        if input_address == "exit":
            break
        else:
            result = dadata.suggest(
                name="address",
                query=input_address,
                language="ru",
            )
            address_location(result)
            exact_address = input("Уточните пожалуйста адрес: ")
            result_func = f_exact_address(exact_address)
            print(result_func)


main()
