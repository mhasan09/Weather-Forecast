def parse_forecasted_data(forecast_data):
    index_of_2pm_temp = {}

    for i in forecast_data:
        index_arr = []
        for j in range(len(forecast_data[i]["date"])):
            if forecast_data[i]["date"].time[j].hour == 14:
                index_arr.append(j)
        index_of_2pm_temp[i] = index_arr

    average_temp_dict_at_2pm = {}
    for i in index_of_2pm_temp:
        sum_of_temperature = 0
        current_index = index_of_2pm_temp[i]
        for j in current_index:
            sum_of_temperature += forecast_data[i]["temperature_2m"][j]
        average_temp_dict_at_2pm[i] = sum_of_temperature / 7

    coolest_districts = dict(sorted(average_temp_dict_at_2pm.items(), key=lambda item: item[1]))
    return dict(list(coolest_districts.items())[:10])
