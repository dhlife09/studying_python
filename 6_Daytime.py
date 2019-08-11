
from datetime import datetime
hour = datetime.now().hour

# 오전일 경우 if문 내용 실행

if hour < 12:
 print('오전입니다!')
