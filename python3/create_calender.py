SUNDAY=0
MONDAY=1
TUESDAY=2
WEDNESDAY=3
THURSDAY=4
FRIDAY=5
SATURDAY=6
WEEKS = [SUNDAY, MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY]

COLOR_RED="#FF0000"
COLOR_BLUE="#0066FF"

FONT_TAG="<font color='%s'>%s</font>"
DIV_TAG="<div style='text-align:center;height:80px;width:80px;'>%s<br>[+](%s)</div>"
README_FILE_NAME="%s%s%s\\README.md"

PRINT_WEEKS="|%s|%s|%s|%s|%s|%s|%s|"
SEPARATOR="--"
NONE_DAY="-"

FILE_TITLE="# %s年%s月"

def week_print():
    START_DIV = "<div style='text-align:center;width:80px;'>"
    END_DIV   = "</div>"

    sunday    = START_DIV + (FONT_TAG % (COLOR_RED, "sun")) + END_DIV
    monday    = "%s%s%s" % (START_DIV, "mon", END_DIV)
    tuesday   = "%s%s%s" % (START_DIV, "tue", END_DIV)
    wednesday = "%s%s%s" % (START_DIV, "wed", END_DIV)
    thursday  = "%s%s%s" % (START_DIV, "thu", END_DIV)
    friday    = "%s%s%s" % (START_DIV, "fri", END_DIV)
    saturday  = START_DIV + (FONT_TAG % (COLOR_BLUE, "sat")) + END_DIV
    print(PRINT_WEEKS % (sunday, monday, tuesday, wednesday, thursday, friday, saturday))
    print(PRINT_WEEKS % (SEPARATOR, SEPARATOR, SEPARATOR, SEPARATOR, SEPARATOR, SEPARATOR, SEPARATOR))

def write_line(str_year, str_month, holidays_list, week, date, line):
    
    # 日付をDD文字列に変換する
    str_day = "0" + str(date) if date < 10 else str(date)
    day = ""

    if date in holidays_list:
        day = FONT_TAG % (COLOR_RED, str_day)
    elif week == SUNDAY:
        day = FONT_TAG % (COLOR_RED, str_day)
    elif week == SATURDAY:
        day = FONT_TAG % (COLOR_BLUE, str_day)
    else:
        day = str_day
    
    # README.mdのファイル名を作成する
    file_name = README_FILE_NAME % (str_year, str_month, str_day)

    # divタグを作成する
    div_tag = DIV_TAG % (day, file_name)
    
    # ラインに加算する
    line = "%s|%s" % (line, div_tag)

    # 日付を更新する
    date += 1

    return date, line

def the_first_week_print(str_year, str_month, holidays_list, first_day_of_the_week):
    line = ""
    date = 1

    # 先月の日付はすべて[-]にする
    none_div_tag = DIV_TAG % (NONE_DAY, NONE_DAY)

    for week in WEEKS:
        if week < first_day_of_the_week:
            line = "%s|%s" % (line, none_div_tag)
        else:
            date, line = write_line(str_year, str_month, holidays_list, week, date, line)
    
    print("%s|" % line)
    return date

def the_week_print(str_year, str_month, holidays_list, date, end_day):
    line = ""

    for week in WEEKS:
        date, line = write_line(str_year, str_month, holidays_list, week, date, line)
        if date > end_day:
            break
    print("%s|" % line)
    return date

def get_end_day(str_year, str_month):
    n_month = int(str_month)
    day_31 = [1, 3, 5, 7, 8, 10, 12]
    day_30 = [4, 6, 9, 11]
    end_day = 31
    if n_month in day_31:
        pass
    elif n_month in day_30:
        end_day = 30
    else:
        n_year = int(str_year)
        if n_year % 4 == 0:
            end_day = 29
        else:
            end_day = 28
    return end_day

if __name__ == '__main__':
    str_year = input("作成するカレンダーの年を入力してください(例:2021):")
    str_month = input("作成するカレンダーの月を入力してください(例:05):")

    # 1日の曜日を取得する(pythonは月曜日が0なため、日曜日を0に変換する)
    import calendar
    n_week = calendar.weekday(int(str_year), int(str_month), 1)
    n_week += 1
    if n_week > 6:
        n_week = 0

    # 休日を取得する
    str_holidays = input('祝日(休日)をカンマ区切りで入力してください(例:1, 2, 3, 5):')
    holidays_list = []
    if len(str_holidays) > 0:
        for day in str_holidays.split(","):
            holidays_list.append(int(day))
    
    print(FILE_TITLE % (str_year, str_month))
    print("")
    print("## カレンダー")
    
    # 最終日を取得する
    end_day = get_end_day(str_year, str_month)

    # 表のヘッダーを表示する
    week_print()

    # 第一週を表示する
    next_date = the_first_week_print(str_year, str_month, holidays_list, n_week)

    # 最終日まで表示する
    while(next_date < end_day):
        next_date = the_week_print(str_year, str_month, holidays_list, next_date, end_day)