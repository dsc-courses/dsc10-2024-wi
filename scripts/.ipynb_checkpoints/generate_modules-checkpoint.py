# generate_modules.py
# Use this to convert from the course calendar spreadsheet to modules that work with the course website template.
# Only run it on the weeks that haven't occurred yet, otherwise it'll erase any manual work.
# Run from the scripts folder.

import pandas as pd
import os
import sys
import numpy as np

# Edit these variables before running script
CSV_PATH = "Lecture Schedule – DSC 10, Winter 2024 - wi24.csv"
DATE_FORMAT = "DATE MONTH/DAY"
YEAR = 2024
START_FROM_WEEK = 1 #only future weeks!


def fill_missing_vals(df):
    df["Week"] = df["Week"].fillna(method="ffill").astype(int)
    df["LectureNum"] = df["LectureNum"].fillna(0).astype(int)
    df["Lecture"] = df["Lecture"].fillna("").astype(str)
    df["Lab"] = df["Lab"].fillna("").astype(str)
    df["Homework"] = df["Homework"].fillna("").astype(str)
    df["Readings"] = df["Readings"].fillna("").astype(str)
    df["Links"] = df["Links"].fillna("").astype(str)
    df["Discussion"] = df["Discussion"].fillna("").astype(str)
    df["Quiz"] = df["Quiz"].fillna("").astype(str)
    return df


df = pd.read_csv(CSV_PATH).rename(columns={"#": "LectureNum"}).pipe(fill_missing_vals)
df


month_map = {
    "Jan": 1,
    "Feb": 2,
    "Mar": 3,
    "Apr": 4,
    "May": 5,
    "Jun": 6,
    "Jul": 7,
    "Aug": 8,
    "Sept": 9,
    "Oct": 10,
    "Nov": 11,
    "Dec": 12,
}


def round_format(i):
    return "0" + str(i) if int(i) <= 9 else str(i)


def date_conv(date):
    if DATE_FORMAT == "DATE. MONTH. DAY":
        try:
            _, month, day = date.split(" ")
        except TypeError:
            print(date)

        month = month_map[month]
        month = round_format(month)
        day = round_format(day)

    elif DATE_FORMAT == "MONTH/DAY":
        try:
            month, day = date.split("/")
        except TypeError:
            print(date)

    elif DATE_FORMAT == "DATE MONTH/DAY":
        date = date.split(" ")[1]
        try:
            month, day = date.split("/")
        except TypeError:
            print(date)

    elif DATE_FORMAT == "MONTH/DAY/YEAR":
        try:
            [month, day, _] = date.split("/")
        except TypeError:
            print(date)

    return f"{YEAR}-{month}-{day}"


def has_content(row):
    return row.loc[["Lecture", "Homework", "Readings", "Lab", "Discussion"]].any()


week = df.query("Week == 1")
week.apply(has_content, axis=1)


# for a single week
def write_week(i, dest="../_modules", write=True):
    week = df.query("Week == @i")
    #week = week[week.apply(has_content, axis=1)] 
    # I deleted this because it wouldn't run when included. 
    # Don't really understand what it's meant to do and how to do it correctly.

    outstr = f"""---
    title: Week {i}
    weekNumber: {i}
    days:"""

    for day in week.itertuples(index=False):
        date = day.Date
        lec_num = day.LectureNum
        lecture = day.Lecture
        homework = day.Homework
        lab = day.Lab
        readings = day.Readings
        links = day.Links
        discussion = day.Discussion
        quiz = day.Quiz

        date_formatted = date_conv(date)

        outstr += f"""
      - date: {date_formatted}
        events:
          """

        # Lecture number
        if lec_num != 0:
            outstr += f""""**LEC {lec_num}**{{: .label .label-lecture }} {lecture}":"""

            combined = ""
            if readings:
                readings_list = readings.split(", ")
                links_list = links.split(", ")
                num_readings = len(readings_list)
                for j in range(num_readings):
                    combined += "["+readings_list[j]+"]("+links_list[j]+")"
                    if j < num_readings - 1:
                        combined += ", "
                outstr += f"""
            "{combined}"
                """
        else:
            if lab:
                lab_num, lab_name = lab.split(". ")
                outstr += f"""
          "**LAB {lab_num}**{{: .label .label-lab }} **{lab_name.strip()}**":"""

            elif "Exam" in lecture:
                outstr += f"""
          "**EXAM**{{: .label .label-exam }} **{lecture.strip()}**":"""
            elif lecture:  # we reach this when we have holidays, like July 4
                outstr += f"""
          "{lecture}":"""

        if homework:
            if "Project" in homework:
                outstr += f"""
          "**PROJ**{{: .label .label-proj }} **{homework.strip()}**":"""
            else:
                hw_num, hw_name = homework.split(". ", 1)
                outstr += f"""
          "**HW {hw_num}**{{: .label .label-hw }} **{hw_name.strip()}**":"""

        if discussion:
            outstr += f"""
          "**DISC**{{: .label .label-disc }} {discussion.strip()}":"""
            
        if quiz:
            quiz_num, quiz_description = quiz.split(". ", 1)
            outstr += f"""
          "**QUIZ {quiz_num}**{{: .label .label-quiz }} **{quiz_description.strip()}**":"""

    outstr += "\n---"

    if write:
        # if not dest in os.listdir():
        #     os.system(f'mkdir {dest}')

        # print(dest + '/week-' + round_format(i) + '.md')

        f = open(dest + "/week-" + round_format(i) + ".md", "w")
        f.write(outstr)
        f.close()
    else:
        return outstr


for i in range(START_FROM_WEEK, 11):
    write_week(i)


