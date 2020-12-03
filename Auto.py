# --- entries --- #
year = "2020"
month = "8"
day = "8"

class_num = "303"
teacher = "洪于晟"

should_attend = "30"
school_leave = "0"
personal_leave = "0"
sick_leave = "0"
sick_leave_of_fever_id = "0"
leave_for_no_reason = "0"
leave_for_no_reason_id = "0"
real_attend  = "30"

filler = "李杰穎"
# --------------- # 

url = "https://docs.google.com/forms/d/e/1FAIpQLSduotkz5L48QN_vXksFCerIfHF4ihDQyxlARbL4BneSeqzNWg/viewform"

entries = "?entry.1527565392_year={}&entry.1527565392_month={}&entry.1527565392_day={}&entry.156395716={}&entry.279055274={}&entry.1737682478={}&entry.2088338585={}&entry.2043141570={}&entry.28387397={}&entry.1133344552={}&entry.954949304={}&entry.1394632443={}&entry.1018631455={}&entry.1992551612={}".format(
    year,
    month,
    day,
    class_num,
    teacher,
    should_attend, 
    school_leave,
    personal_leave,
    sick_leave,
    sick_leave_of_fever_id,
    leave_for_no_reason,
    leave_for_no_reason_id,
    real_attend,
    filler,
)

print(url+entries)