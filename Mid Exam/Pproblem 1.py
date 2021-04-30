size = float(input()) # size of the size of the box
n = int(input())    # sheets of paper
total_sheet_area = 0
box_area = (size * size) * 6

for el in range(1, n+1):

    length_paper = float(input())
    width_paper = float(input())
    if el % 3 == 0:
        sheet_area = (length_paper * width_paper)
        a = sheet_area * 0.25
        sheet_area -= a
        total_sheet_area += sheet_area
        continue
    if not el % 5 == 0:
        sheet_area = (length_paper * width_paper)
        total_sheet_area += sheet_area

if total_sheet_area >= box_area:
    paper_left = total_sheet_area - box_area
    percent_paper_left = (paper_left / total_sheet_area) * 100
    print("You've covered the gift box!")
    print(f"{percent_paper_left:.2f}% wrap paper left. ")
else:
    need_to_cover = box_area - total_sheet_area    # %
    needed_paper = need_to_cover / box_area * 100   # %
    print("You are out of paper!")
    print(f"{needed_paper:.2f}% of the box is not covered.")

