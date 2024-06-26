# EBS FM 편성표 크롤러

https://www.ebs.co.kr/schedule?channelCd=RADIO&onor=RADIO
에서 편성표 정보를 긁어와 DataFrame으로 반환합니다.


## 1. 설치

```bash
pip install ebsfm-schedule
```

## 2. 사용법

### 2.0. 기본형식

```python
schedule(<채널명>, [기준일])
```

- 채널명: 'RADIO'(EBS FM) 또는 'IRADIO'(반디 외국어 전문 채널)
- 기준일: 'YYYYMMDD' 형식의 문자열(생략가능)


### 2.1. 당일 기준
```python
from ebsfm import schedule

# EBS FM 편성표
df = schedule('RADIO')
print(df)

# 반디 외국어 전문 채널 편성표
df = schedule('IRADIO')
print(df)
```

### 2.2. 특정 날짜 기준
```python
from ebsfm import schedule

# EBS FM 편성표
df = schedule('RADIO', '20240624')
print(df)

# 반디 외국어 전문 채널 편성표
df = schedule('IRADIO', '20240624')
print(df)
```