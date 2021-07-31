def type_analysis(year):
    """
    Takes a valid year and outputs its type (Leap, later, middle, previous ou anomalous).
    :param year: the year to analyze.
    :return: binary list with the year type (string) and its list index (0-4).
    """
    types = ['Leap', 'Later', 'Middle', 'Previous', 'Anomalous']

    test1 = year % 4
    test2 = year % 100
    test3 = year % 400

    if test2 == 0 and test3 != 0:
        year_type = types[4]
        index = 4
    else:
        year_type = types[test1]
        index = test1

    return year_type, index


def anomaly_identifier(i, f):
    """
    Takes a year range and tests if it contains anomalous year (as 1700, 1800, 1900, 2100, etc.) or not.
    :param i: first element of the year range.
    :param f: final year.
    :return: two elements set, the answer (boolean: it contains anomalies or not) and the list of anomalies (if True).
    """
    assert i < f

    i_type = type_analysis(i)
    f_type = type_analysis(f)
    preffix_i = int(i / 100)
    preffix_f = int(f / 100)
    anomalies = []

    dif = f - i
    pref_dif = preffix_f - preffix_i

    if 'Anomalous' in (i_type[0], f_type[0]):
        answer = True
        if i_type[0] == 'Anomalous':
            anomalies.append(i)
        if f_type[0] == 'Anomalous':
            anomalies.append(f)
    if pref_dif == 1:
        if dif < 100 and preffix_i % 4 == 0 or preffix_f % 4 == 0 and not anomalies:  # "empty lists are False"
            answer = False
        elif dif > 100 and preffix_f % 4 == 0 and not anomalies:
            answer = False
        else:
            answer = True
            if preffix_f*100 not in anomalies and preffix_f % 4 != 0:
                anomalies.append(preffix_f*100)
    elif pref_dif > 1:
        answer = True
        for c in range(1, pref_dif+1):
            if (preffix_i+c) % 4 != 0 and ((preffix_i+c)*100) not in anomalies:
                anomalies.append((preffix_i+c)*100)
    else:
        if 'Anomalous' not in (i_type[0], f_type[0]):
            answer = False

    return answer, sorted(anomalies)


def what_years_contemporary(pre_list, month, final_year):
    """
    Takes a list of years, the month of the event and a final year. It outputs the later list appended with the years
    whose the event date falls on in the same weekday, but only if the period doesn't contain an anomalous year.
    :param pre_list: a previous list with valid years.
    :param month: month of the event (1-12).
    :param final_year: the limit of the calculation.
    :return: the updated list.
    """
    if not type(pre_list) == list:
        raise TypeError('The first argument should be a list, not int, float, string or any other array type.')
    base_list = pre_list.copy()
    year = base_list[len(base_list) - 1]

    # if anomaly_identifier(year, final_year)[0] is True and (type_analysis(year)[1] != 4 or type_analysis(final_year)[1] != 4):
    #     raise ValueError('The time span shouldn\'t pass through any anomalous years.')

    while year < final_year:
        year_type = type_analysis(year)
        if month in (1, 2):
            if year_type[1] == 0:  # Leap
                r = 5
            elif year_type[1] in (1, 2):  # Later or Middle
                r = 6
            elif year_type[1] == 3:  # Previous
                r = 11
            year += r
            base_list.append(year)
        else:
            if year_type[1] in (0, 1):  # Leap or Later
                r = 6
            elif year_type[1] == 2:  # Middle
                r = 11
            elif year_type[1] == 3:  # Previous
                r = 5
            year += r
            base_list.append(year)
    if base_list[len(base_list) - 1] > final_year:
        base_list.pop(len(base_list) - 1)
    return base_list


def what_years_complete(initial_year, month, final_year):
    """
    Takes valid values of an initial year, a month and a final year. It outputs a set of years whose the event date
    falls on in the same weekday even if the period contains an anomalous year.
    :param initial_year: The year of the event to analyze.
    :param month: month of the event.
    :param final_year: range limit.
    :return: set with years (the list is translated to set to avoid duplicates).
    """
    year = initial_year
    years_list = [year]
    anomaly_test = anomaly_identifier(initial_year, final_year)[0]
    if anomaly_test is True:
        anomalies = anomaly_identifier(initial_year, final_year)[1]

        if month not in (1, 2):  # March to December
            a = 0
            while year < final_year:
                while a < len(anomalies):
                    if anomalies[a] == year:
                        year += 6
                        years_list.append(year)
                    else:
                        years_list.extend(what_years_contemporary(years_list, month, anomalies[a]))
                        years_list = sorted(set(years_list))
                        time_span = anomalies[a] - years_list[len(years_list) - 1]  # Last list's year.
                        if time_span in (1, 2, 5):
                            year += 6
                            years_list.append(year)
                            a += 1
                        elif time_span in (3, 10):
                            year += 12
                            years_list.append(year)
                            a += 1
                        elif time_span == 4:
                            year += 7
                            years_list.append(year)
                            a += 1
                        elif time_span == 6:
                            year += 6
                            years_list.append(year)
                            year += 6
                            years_list.append(year)
                            a += 1
                        if a == len(anomalies)-1:
                            years_list.extend(what_years_contemporary(years_list, month, anomalies[a]))
                            years_list = sorted(set(years_list))
                            if years_list[len(years_list) - 1] > anomalies[a]:
                                years_list.pop(len(years_list) - 1)
                        else:
                            years_list.extend(what_years_contemporary(years_list, month, final_year))
                            years_list = sorted(set(years_list))
                years_list.extend(what_years_contemporary(years_list, month, final_year))
                years_list = sorted(set(years_list))
                if years_list[len(years_list) - 1] > final_year:
                    years_list.pop(len(years_list) - 1)
                break
            return years_list

        else:  # January or February
            return ['Junior dev at work...']

    else:
        years_list.extend(what_years_contemporary(years_list, month, final_year))
        years_list = sorted(set(years_list))
        if years_list[len(years_list)-1] > final_year:
            print(years_list[len(years_list) - 1])
            years_list.pop(len(years_list)-1)
        return years_list


def interface():
    from gld_method_library.interface import cab, cor, lins
    cab('Same weekday calculator')  # Translate
    try:
        event_year = int(input('Enter the event year: '))
        month = int(input('Enter the month of the event (1-12): '))
        limit_year = int(input('Enter a limit year to the calculation (as yyyy format): '))
    except (TypeError or ValueError):
        event_year = int(input('Enter the event year: '))
        month = int(input('Enter the month of the event (1-12): '))
        limit_year = int(input('Enter a limit year to the calculation (as yyyy format): '))
    else:
        years_list = what_years_complete(event_year, month, limit_year)
        print(lins())
        cor(f'The event that took place in {event_year} will have its date falling on the same weekday of that year'
            f'in the following years: ', 'VD', False)
        for index, value in enumerate(years_list):
            print(f'{value}', end='')
            if index == (len(years_list) - 1):
                print('.')
            elif index == (len(years_list) - 2):
                print(' e ', end='')
            else:
                print(', ', end='')


print(what_years_complete(1895, 3, 1920))
# interface()

# Quando há anômalos, soma 6 sempre, pq?