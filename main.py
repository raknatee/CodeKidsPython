
def main():
    hr_in:int = int(input(f"Parking time (start) hr: "))
    if hr_in < 8 or hr_in >= 21:
        print("can not enter in this time")
        return
    min_in:int = int(input(f"Parking time (start) min: "))
    if hr_in <= 8 and min_in == 0:
        print("can not enter in this time")
        return
    hr_out:int = int(input(f"Parking time (take-off) hr: "))
    min_out:int = int(input(f"Parking time (take-off) min: "))

    if hr_out < hr_in:
        hr_out+=24

    time_interval:int = (hr_out - hr_in)*60 + (min_out - min_in) - 120

    if time_interval%60 != 0:
        time_interval = time_interval//60 + 1

    if time_interval%60 == 0:
        time_interval = time_interval//60

    cost = time_interval * 20
    if hr_out >= 22:
        cost += 500

    print(f"cost {cost}")

if __name__ == "__main__":
    main()
    print("-"*30)
