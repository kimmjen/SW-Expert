#!/bin/bash

# 사용자로부터 폴더 이름 입력받기
read -p "생성할 폴더의 이름을 입력하세요: " FOLDER_NAME

# 폴더 생성
mkdir -p "$FOLDER_NAME"

# Python 파일 생성
touch "$FOLDER_NAME/$FOLDER_NAME.py"

# Markdown 파일 생성 및 템플릿 작성
MD_FILE="$FOLDER_NAME/$FOLDER_NAME.md"

echo "### ${FOLDER_NAME//_/ }" > "$MD_FILE"
echo "" >> "$MD_FILE"
echo "#### 설명" >> "$MD_FILE"
echo "" >> "$MD_FILE"
echo "#### [제약사항]" >> "$MD_FILE"
echo "" >> "$MD_FILE"
echo "#### [입력]" >> "$MD_FILE"
echo "" >> "$MD_FILE"
echo "#### [출력]" >> "$MD_FILE"
echo "" >> "$MD_FILE"


# 스크립트 완료 메시지
echo "폴더 및 파일이 생성되었습니다: $FOLDER_NAME"