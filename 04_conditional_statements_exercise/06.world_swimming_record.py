record_second = float(input())
distance_meters = float(input())
swim_time = float(input())

delay_time = (distance_meters // 15) * 12.5
swim_record = (distance_meters * swim_time) + delay_time

if record_second > swim_record:
    print(f" Yes, he succeeded! The new world record is {swim_record:.2f} seconds.")
else:
    print(f"No, he failed! He was {abs(record_second - swim_record):.2f} seconds slower.")
