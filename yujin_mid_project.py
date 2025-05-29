# Alcohol analysis project
# 아침에 적발되는 알코올 측정 농도 확인
# 2020년 ~ 2023년 측정 시간대별로 알코올 농도량 추이 분석

# 자동으로 파일 목록 수집
# %% 데이터 불러오기
import glob

all_csv_files = glob.glob("lion_mid_data07/data/*.csv")

# %% 연도 필터링
filtered_files = [file for file in all_csv_files if any(year in file for year in ["2020", "2021", "2022", "2023"])]

# %% 확인
for file in filtered_files:
    print(file)

