[2018-09-29]
Linux Script 작성, git bash 에서 "./g" 로 실행
+-------------------------------------------+[Start]
#! /bin/bash
git pull
git add --all .
if [ "$1" = "" ]
then 
	git commit -m "Commit at $(date +%Y%m%d)-$(date +%H%M)"
else
	git commit -m "$*"
fi
git push
+-------------------------------------------+[End]



[2018-09-11] all.bat 설명
아톰실행 후 자동으로 CLI 창 열기
===============================
atom
cmd /k ".\tf36\Scripts\activate & prompt = $N/처음코딩$G$G"
===============================

[깃커밋 요약]
>> git add --all .
>> git commit -m "Commit Memo"
>> git push

커밋 메시지 작성법
타입: 제목

타입 - feat(기능), fix(버그), dosc(문서), style(포맷변경,세미콜론 수정등), refa(ctor), test, chore(패키지매니저)
제목은 동사원형 시작, 대문자 작성. 총 50자, 마침표X

예) fix: Fix Person Database

1. 다운로드  git-scm.com
설치시 Run Git and associated Unix tools from the Windows command-line 선택

2. 초기화
>> git init
>> git config --global user.name "eventia"
>> git config --global user.email eventia@gmail.com

3.  무시(저장하지 않음) 목록 : .gitignore
.gitignore 내용
*.pyc
*~
__pycache__
myvenv
db.sqlite3
/static
.DS_Store


4. 기본명령
>> git status
>> git add --all .
>> git commit -m "My Project Commit"


5. github 에 저장
>> git remote add origin https://github.com/eventia/my-first-blog.git

[수정시]>> git remote set-url origin https://github.com/eventia/my-first-blog.git

>> git push -u origin master
>> git push

6. pythonanywhere / github to other cloud
>> git clone https://github.com/<your-github-username>/my-first-blog.git
>> git pull

7. 요약
[처음]
>> git init
>> git config --global user.name "eventia"
>> git config --global user.email eventia@gmail.com
>> git add --all .
>> git commit -m "Commit Memo"
>> git remote add origin https://github.com/myid/myrepository.git
>> git push -u origin master

[매번]
>> git add --all .
>> git commit -m "Commit Memo"
>> git push

[참고링크]
https://sujinlee.me/professional-github/