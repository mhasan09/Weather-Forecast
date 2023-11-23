from datetime import datetime

def parse_forecasted_data(forecasted_data):
    """
    This lower block of codes is the naive version for
    generating index_of_2pm_temp and average_temp_dict_at_2pm.
    I'm using a dictionary comprehension mitigate the calculating time

    ////////////////////////////////////////////////////////////////////////////////
    index_of_2pm_temp = {}
    for i in forecasted_data:
        index_arr = []
        for j in range(len(forecasted_data[i]["date"])):
            if forecast_data[i]["date"].time[j].hour == 14:
                index_arr.append(j)
        index_of_2pm_temp[i] = index_arr

    average_temp_dict_at_2pm = {}
    for i in index_of_2pm_temp:
        sum_of_temperature = 0
        current_index = index_of_2pm_temp[i]
        for j in current_index:
            sum_of_temperature += forecast_data[i]["temperature_2m"][j]
    ////////////////////////////////////////////////////////////////////////////////

    """
    index_of_2pm_temp = {key: [j for j, date in enumerate(value["date"]) if date.time().hour == 14] for key, value in forecasted_data.items()}

    average_temp_dict_at_2pm = {key: sum(forecasted_data[key]["temperature_2m"][j] for j in index_of_2pm_temp[key]) /
                                     len(index_of_2pm_temp[key]) for key in index_of_2pm_temp}

    coolest_districts = dict(sorted(average_temp_dict_at_2pm.items(), key=lambda item: item[1]))
    return dict(list(coolest_districts.items())[:10])


def parse_forecasted_dates(forecasted_data):
    date_data = [date.date() for date in forecasted_data["Dhaka"]["date"]]
    return list(set(date_data))


def parse_2pm_weather(forecasted_data, location, date):
    temperature_index = -1
    formatted_date = datetime.strptime(date, "%Y-%m-%d").date()
    for index, data in enumerate(forecasted_data[location]["date"]):
        if data.day == formatted_date.day and data.hour == 14:
            temperature_index = index
    return forecasted_data[location]["temperature_2m"][temperature_index]


def parse_travel_decision_data(**kwargs):
    forecasted_data = kwargs["forecasted_data"]
    current_location = kwargs["requested_data"]["current_location"].title()
    destination = kwargs["requested_data"]["destination"].title()
    date_of_travel = kwargs["requested_data"]["date_of_travel"]

    current_location_2pm_weather = parse_2pm_weather(forecasted_data=forecasted_data,
                                                     location=current_location,
                                                     date=date_of_travel)

    destination_2pm_weather = parse_2pm_weather(forecasted_data=forecasted_data,
                                                location=destination,
                                                date=date_of_travel)

    if current_location_2pm_weather > destination_2pm_weather:
        return "It will be cool there, you can travel"
    return "Do not travel, better stay home"
