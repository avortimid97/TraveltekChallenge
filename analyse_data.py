import pandas as pd
from collections import Counter


class Process:

    @staticmethod
    def load_data():
        df = pd.read_csv('data/flighdata_B.csv', na_values=['NA'])

        return df

    @staticmethod
    def avg_time_lhr_dxb(df):

        df[['outdeparttime', 'outarrivaltime', 'indeparttime', 'inarrivaltime', 'outdepartdate', 'outarrivaldate',
            'indepartdate', 'inarrivaldate']] = df[['outdeparttime', 'outarrivaltime', 'indeparttime', 'inarrivaltime',
                                                    'outdepartdate', 'outarrivaldate', 'indepartdate', 'inarrivaldate']] \
            .applymap(lambda x: pd.to_datetime(x))

        df['outduration'] = 0
        df['outduration'] = abs(df['outarrivaltime'] - df['outdeparttime'])

        df['induration'] = 0
        df['induration'] = abs(df['inarrivaltime'] - df['indeparttime'])

        df = df.loc[(df['depair'] == 'LHR') & (df['destair'] == "DXB")]

        avg_timedelta = df['outduration'].mean()

        result = "The average journey time between London and Dubai is: {}".format(avg_timedelta)
        return result

    @staticmethod
    def max_departs_man(df):
        df = df.loc[df['depair'] == 'MAN']

        dates_list = []
        result = ' '
        week = {0: "Monday", 1: "Tuesday", 2: "Wednesday", 3: "Thursday", 4: "Friday", 5: "Saturday", 6: "Sunday"}

        for (columnName, columnData) in df.iteritems():
            if columnName == 'outdepartdate':
                dates_list.append(columnData.values)

        for i in dates_list:
            d = Counter(i)

            max_day = max(d)
            occurrences = max(d.values())
            formatted = pd.to_datetime(max_day)

            weekday = formatted.weekday()

            for key, val in week.items():
                if weekday == key:
                    result = 'Max departures from Manchester occur on {}, a total of {} times.'.format(val, occurrences)
        return result

    @staticmethod
    def business_proportion(df, bound):

        flight_class = []
        total = df.shape[0]
        proportion = 0

        for (columnName, columnData) in df.iteritems():
            if columnName == f'{bound}flightclass':
                flight_class.append(columnData.values)

        for i in flight_class:
            flight_class_dict = Counter(i)
            times = flight_class_dict['Business']
            proportion = round(times / total * 100, 2)

        return proportion

    @staticmethod
    def combined_business_proportion(df):
        inbound = Process.business_proportion(df, "in")
        outbound = Process.business_proportion(df, "out")
        combined = 'The proportion of Business class for inbound flights: {}% and outbound flights: {}%.'\
            .format(inbound, outbound)

        return combined

    @staticmethod
    def flights_to_sweden(df):
        swiss_airports = ['ARN', 'GOT', 'NYO', 'BMA', 'MMX', 'LLA', 'UME']
        flights_list = []
        swiss_flights_list = []
        counter_dict = {}

        total = df.shape[0]

        for (columnName, columnData) in df.iteritems():
            if columnName == 'destair':
                flights_list.append(columnData.values)

        for i in flights_list:
            counter_dict = Counter(i)

        for p in swiss_airports:
            number_of_occ = counter_dict[p]
            swiss_flights_list.append(number_of_occ)

        total_swiss_flights = sum(swiss_flights_list)
        proportion = round(total_swiss_flights / total * 100, 2)
        result = "The proportion of flights arriving in Sweden: {}%".format(proportion)

        return result

    @staticmethod
    def most_common_carrier(df):
        flights_list = []
        counter_dict = {}

        for (columnName, columnData) in df.iteritems():
            if columnName == 'carrier':
                flights_list.append(columnData.values)

        for i in flights_list:
            counter_dict = Counter(i)

        first_5_dict = dict(counter_dict.most_common(5))

        return first_5_dict

    @staticmethod
    def main():
        df = Process.load_data()
        Process.avg_time_lhr_dxb(df)
        Process.max_departs_man(df)
        Process.combined_business_proportion(df)
        Process.flights_to_sweden(df)
        Process.most_common_carrier(df)


if __name__ == '__main__':
    Process.main()
