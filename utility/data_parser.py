def parse_forecasted_data(forecast_data):
    index_of_2pm_temp = {key: [j for j, date in enumerate(value["date"]) if date.time().hour == 14] for key, value in forecast_data.items()}
    average_temp_dict_at_2pm = {key: sum(forecast_data[key]["temperature_2m"][j] for j in index_of_2pm_temp[key]) / len(index_of_2pm_temp[key]) for key in index_of_2pm_temp}
    coolest_districts = dict(sorted(average_temp_dict_at_2pm.items(), key=lambda item: item[1]))
    return dict(list(coolest_districts.items())[:10])
