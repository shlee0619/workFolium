import folium
import os
import webbrowser
import pandas as pd

# 1. 데이터 로드
df = pd.read_csv("./data/소상공인시장진흥공단_상가(상권)정보_서울_202109.csv")
print(df.head())      # 데이터의 처음 몇 행을 출력하여 확인
print(df.info())      # 데이터프레임의 구조 정보를 출력

# 2. '요거프레소'가 포함된 상호명 필터링
yogepresso_df = df[df['상호명'].str.contains('요거프레소', na=False)].copy()

# 3. '상호명'과 '지점명' 결합 (필요한 경우)
yogepresso_df['상호명'] = yogepresso_df.apply(
    lambda row: f"{row['상호명']} {row['지점명']}" if row['상호명'] == '요거프레소' and pd.notnull(row['지점명']) else row['상호명'],
    axis=1
)

# 4. 지도 객체 생성
m = folium.Map(location=[37.5564234, 126.9240735], zoom_start=11)

# 5. 마커 추가
for _, row in yogepresso_df.iterrows():
    try:
        location = [float(row['위도']), float(row['경도'])]
        name = row['상호명']
        address = row['도로명주소']
        
        popup_content = f"{name}\n{address}"
        
        folium.Marker(
            location=location,
            popup=folium.Popup(popup_content, min_width=50, max_width=200),
            tooltip=name,
            icon=folium.Icon(icon='mug-hot', color='black', prefix='fa')
        ).add_to(m)
    except (ValueError, KeyError) as e:
        print(f"데이터 처리 중 오류 발생: {e}")

# 6. 지도 저장 및 열기
output_path = './data/01map.html'
os.makedirs(os.path.dirname(output_path), exist_ok=True)
m.save(output_path)
webbrowser.open(os.path.realpath(output_path))
print(f"{output_path} 파일 저장 및 열기 완료")
