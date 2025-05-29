# Git 협업 최초 설정 가이드 🛠️

처음 레포지토리를 클론하고 작업을 시작하기 위한 Git 기본 세팅 절차입니다.



## 1️⃣ Git 사용자 정보 설정 (최초 1회만 필요)

git config --global user.name "당신의 이름"
git config --global user.email "당신의 GitHub 이메일"

2️⃣ 레포지토리 클론 받기

git clone https://github.com/KSCH2582/lion_mid_data07.git
cd lion_mid_data07

3️⃣ 자신의 작업 브랜치 만들기 (선택)

기본 브랜치는 main입니다.
새로운 기능이나 수정을 할 때는 개별 브랜치를 만들어 작업하세요.

git checkout main               # 메인 브랜치 전환
git pull origin main            # 최신 상태로 갱신
git checkout -b feature/작업내용  # 새 브랜치 생성 및 전환

4️⃣ 커밋 & 푸시 기본 명령어

git add .
git commit -m "feat: 이름 - 데이터 전처리 완료"
git push origin 브랜치명

5️⃣ GitHub에 올라온 변경사항 반영하기 (푸시 전에 꼭!)
푸시하기 전에 다른 사람의 작업이 반영되었는지 확인하고, 최신 상태로 업데이트해야 충돌을 줄일 수 있어요.

git pull origin main --rebase
git add 충돌_해결_파일
git rebase --continue

✅ 협업 체크리스트

 커밋 전 git pull origin main --rebase 했나요?

 커밋 메시지는 팀 규칙에 맞게 작성했나요?

 작업이 끝난 뒤엔 git push origin 브랜치명 하셨나요?

 PR(Pull Request)을 통해 코드 리뷰 요청했나요?






 
