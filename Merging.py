import pandas as pd

# 'resources' 폴더 안의 CSV 파일 경로 목록
csv_paths = [
    'resources/JC-202301-citibike-tripdata.csv',
    'resources/JC-202302-citibike-tripdata.csv',
    'resources/JC-202303-citibike-tripdata.csv',
    'resources/JC-202304-citibike-tripdata.csv',
    'resources/JC-202305-citibike-tripdata.csv',
    'resources/JC-202306-citibike-tripdata.csv',
    'resources/JC-202307-citibike-tripdata.csv',
    'resources/JC-202308-citibike-tripdata.csv',
    'resources/JC-202309-citibike-tripdata.csv',
    'resources/JC-202310-citibike-tripdata.csv',
    'resources/JC-202311-citibike-tripdata.csv',
    'resources/JC-202312-citibike-tripdata.csv'
]

# 모든 CSV 파일을 읽고 하나의 DataFrame으로 병합
def merge_csv_files(file_paths):
    # 빈 DataFrame 초기화
    merged_df = pd.DataFrame()

    # 각 파일을 순차적으로 불러와 병합
    for file in file_paths:
        temp_df = pd.read_csv(file)
        merged_df = pd.concat([merged_df, temp_df], ignore_index=True)
    
    return merged_df

# 병합 함수 호출
merged_df = merge_csv_files(csv_paths)

# 병합된 데이터를 새로운 CSV 파일로 저장
merged_df.to_csv('resources/merged_citibike_tripdata.csv', index=False)

# 파일 저장 확인 메시지
print("The data has been successfully merged and saved as 'resources/merged_citibike_tripdata.csv'.")
