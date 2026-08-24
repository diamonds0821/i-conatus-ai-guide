# i.conatus | AI 업무 자동화 가이드

Windows를 사용하는 비개발자가 AI와 함께 업무 자동화를 시작하도록 돕는 무료 가이드입니다.

사람은 Notion에서 내용을 확인하고, AI에게는 통합 Markdown 한 개를 전달합니다.

## 자료 사용하기

- [사람이 읽는 공개 Notion 가이드](https://solid-gerbil-a05.notion.site/i-conatus-AI-3c167fab50dd80ffb19fe3111d89630c)
- [AI에게 전달할 통합 Markdown 원문](https://raw.githubusercontent.com/diamonds0821/i-conatus-ai-guide/main/docs/i-conatus-ai-guide.md)
- [통합 Markdown 파일 페이지](https://github.com/diamonds0821/i-conatus-ai-guide/blob/main/docs/i-conatus-ai-guide.md)

AI에게 원문 주소를 전달합니다. AI가 주소를 읽지 못하면 파일 페이지에서 Markdown을 내려받아 대화창에 첨부합니다.

```plain text
아래 가이드를 전체적으로 읽어줘.

https://raw.githubusercontent.com/diamonds0821/i-conatus-ai-guide/main/docs/i-conatus-ai-guide.md

아직 프로그램을 설치하거나 설정을 변경하지 마.
먼저 내 현재 상태와 하려는 업무를 질문해줘.

나는 Windows를 사용하는 비개발자야.
전문 용어는 쉽게 설명하고 한 번에 한 단계씩 진행해줘.
중요한 변경은 반드시 내 승인을 받아줘.
```

## 관리 원칙

- Notion은 편집·관리 원본입니다.
- `docs/i-conatus-ai-guide.md`는 AI에게 전달하는 배포본입니다.
- 배포본은 여러 파일로 나누지 않습니다.
- PDF는 통합 Markdown에서 다시 만들 수 있는 선택 산출물입니다.

## 통합 Markdown 갱신

Notion 공식 CLI에 로그인한 환경에서 다음 명령을 실행합니다.

```text
python3 scripts/export_notion.py
```

검수:

```text
python3 -m unittest tests/test_export_notion.py
```

저자: **i.conatus**

