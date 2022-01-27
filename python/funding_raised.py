import csv


class FundingRaised:
    def _import_csv(filepath="../startup_funding.csv"):
        with open(filepath, "rt") as csvfile:
            data = csv.reader(csvfile, delimiter=",", quotechar='"')
            # skip header
            next(data)
            csv_data = []
            for row in data:
                csv_data.append(row)

    return csv_data

    @staticmethod
    def where(options={}):
        # Import
        csv_data = FundingRaised._import_csv()

        # Checking
        columns_dict = {1: "company_name", 4: "city", 5: "state", 9: "round"}
        for key, column in columns_dict.items():
            if column in options:
                result = []
                for row in csv_data:
                    if row[key] == options[column]:
                        result.append(row)
                csv_data = result

        # Mapping
        output = []
        for row in csv_data:
            mapped = {}
            mapped["permalink"] = row[0]
            mapped["company_name"] = row[1]
            mapped["number_employees"] = row[2]
            mapped["category"] = row[3]
            mapped["city"] = row[4]
            mapped["state"] = row[5]
            mapped["funded_date"] = row[6]
            mapped["raised_amount"] = row[7]
            mapped["raised_currency"] = row[8]
            mapped["round"] = row[9]
            output.append(mapped)

        return output

    @staticmethod
    def find_by(options):
        # Import
        csv_data = FundingRaised._import_csv()

        # Checking
        columns_dict = {1: "company_name", 4: "city", 5: "state", 9: "round"}
        for key, column in columns_dict.items():
            if column in options:
                for row in csv_data:
                    if row[key] == options[column]:
                        mapped = {}
                        mapped["permalink"] = row[0]
                        mapped["company_name"] = row[1]
                        mapped["number_employees"] = row[2]
                        mapped["category"] = row[3]
                        mapped["city"] = row[4]
                        mapped["state"] = row[5]
                        mapped["funded_date"] = row[6]
                        mapped["raised_amount"] = row[7]
                        mapped["raised_currency"] = row[8]
                        mapped["round"] = row[9]
                        return mapped

        raise RecordNotFound


class RecordNotFound(Exception):
    pass
