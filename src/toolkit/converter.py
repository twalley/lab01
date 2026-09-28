# словари коэффициентов перевода в базовые единицы (в метры и в граммы)
length_coefs = {
    "mm": 0.001,
    "cm": 0.01,
    "m": 1.0,
    "km": 1000.0
}

mass_coefs = {
    "g": 1.0,
    "kg": 1000.0
}

# отдельная функция для перевода температур
def convert_temp(value, from_unit, to_unit):
    # сначала переводим всё в Кельвины
    if from_unit == "c":
        k = value + 273.15
    elif from_unit == "f":
        k = (value - 32) * 5 / 9 + 273.15
    else:
        k = value

    # задаем погрешность, в одну тысячную градуса
    if k < -0.001:
        raise RuntimeError("Ошибка: температура ниже абсолютного нуля")


    # Из Кельвинов переводим в нужную единицу
    if to_unit == "c":
        return k - 273.15
    elif to_unit == "f":
        return (k - 273.15) * 9 / 5 + 32
    else:
        return k


def convert(value, from_unit, to_unit):
    # убираем пробелы по краям и переводим в нижний регистр
    u_from = from_unit.strip().lower()
    u_to = to_unit.strip().lower()

    temp_units = {"c", "f", "k"}

    # Если это температурная группа
    if u_from in temp_units or u_to in temp_units:
        # Проверяем, что обе единицы температурные
        if not (u_from in temp_units and u_to in temp_units):
            raise RuntimeError(f"Несовместимые единицы: {from_unit} и {to_unit}")
        return float(convert_temp(value, u_from, u_to))

    # Если это группа длины
    if u_from in length_coefs and u_to in length_coefs:
        # Переводим исходное значение в метры, а потом делим на коэффициент целевой единицы
        value_in_meters = value * length_coefs[u_from]
        result = value_in_meters / length_coefs[u_to]
        return float(result)

    # Если это группа массы
    if u_from in mass_coefs and u_to in mass_coefs:
        # Переводим исходное значение в граммы, а потом делим на коэффициент целевой единицы
        value_in_grams = value * mass_coefs[u_from]
        result = value_in_grams / mass_coefs[u_to]
        return float(result)

    # Если мы дошли сюда, значит либо единицы неизвестны, либо они из разных групп (например, kg и m)
    # Сначала проверяем, существуют ли вообще такие единицы
    all_known_units = set(length_coefs.keys()) | set(mass_coefs.keys()) | temp_units
    if u_from not in all_known_units or u_to not in all_known_units:
        raise RuntimeError(f"Неизвестная единица: {from_unit} или {to_unit}")
        
    # Если они существуют, но не попали в `if` выше — значит они из разных групп
    raise RuntimeError(f"Несовместимые единицы: {from_unit} и {to_unit}")