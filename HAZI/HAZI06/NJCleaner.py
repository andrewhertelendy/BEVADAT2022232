import pandas as pd
import datetime

class NJCleaner:
    def __init__(self, csv_path):
        self.data = pd.read_csv(csv_path)

    def order_by_scheduled_time(self):
        print(self.data)
        order = self.data.sort_values(by = ["scheduled_time"])
        return order
    
    def drop_columns_and_nan(self):
        self.data = self.data.drop(columns=["from", "to"]).dropna()
        return self.data
        

    def convert_date_to_day(self):
        self.data["day"] = self.data["date"].apply(lambda x: datetime.datetime.strptime(x, "%Y-%m-%d").strftime("%A"))
        self.data = self.data.drop(columns=["date"])
        return self.data

    def convert_scheduled_time_to_part_of_the_day(self):
        def part_of_day(time_str):
            time = datetime.datetime.strptime(time_str, "%Y-%m-%d %H:%M:%S")
            hour = time.hour

            if 0 <= hour < 4:
                return "late_night"
            elif 4 <= hour < 8:
                return "early_morning"
            elif 8 <= hour < 12:
                return "morning"
            elif 12 <= hour < 16:
                return "afternoon"
            elif 16 <= hour < 20:
                return "evening"
            else:
                return "night"

        self.data["part_of_the_day"] = self.data["scheduled_time"].apply(part_of_day)
        self.data.drop(columns=["scheduled_time"], inplace=True)
        return self.data
    
    def convert_delay(self):
        self.data["delay"] = self.data["delay_minutes"].apply(lambda x: 0 if 0 <= x < 5 else 1)
        return self.data

    def drop_unnecessary_columns(self):
        self.data = self.data.drop(columns=["train_id", "actual_time", "delay_minutes"])
        return self.data

    def save_first_60k(self, save_path):
        self.data.head(60000).to_csv(save_path, index=False)

    def prep_df(self, save_path):
        self.data = self.order_by_scheduled_time()
        self.drop_columns_and_nan()
        self.convert_date_to_day()
        self.convert_scheduled_time_to_part_of_the_day()
        self.convert_delay()
        self.drop_unnecessary_columns()
        self.save_first_60k(save_path)