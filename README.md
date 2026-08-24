# i.conatus | AI 업무 자동화 가이드

Windows를 사용하는 비개발자가 AI와 함께 업무 자동화를 시작하도록 돕는 무료 가이드입니다.

Claude 데스크톱 앱의 Cowork에서는 공개 Notion 가이드를 직접 전달합니다. 노션을 읽지 못하는 AI에는 통합 Markdown 한 개를 전달합니다.

## 권장 사용 방법

1. Claude 데스크톱 앱에서 `Cowork`를 선택합니다.
2. 입력창의 `+ → 커넥터 → Claude in Chrome`을 켭니다.
3. 공개 Notion 가이드 주소와 아래 시작 문장을 전달합니다.
4. 작업 과정에 `Chrome에서 Claude 사용함`이 표시되는지 확인합니다.

웹 Cowork와 데스크톱 앱 Cowork는 화면이 비슷해도 작동 방식이 다를 수 있습니다. 웹 Cowork나 일반 Claude 채팅이 노션 본문을 읽지 못하면 통합 Markdown을 사용합니다.

## 자료 주소

- [사람이 읽는 공개 Notion 가이드](https://solid-gerbil-a05.notion.site/i-conatus-AI-3c167fab50dd80ffb19fe3111d89630c)
- [AI에게 전달할 통합 Markdown 원문](https://raw.githubusercontent.com/diamonds0821/i-conatus-ai-guide/main/docs/i-conatus-ai-guide.md)
- [통합 Markdown 파일 페이지](https://github.com/diamonds0821/i-conatus-ai-guide/blob/main/docs/i-conatus-ai-guide.md)

Cowork에서 노션을 직접 읽을 때는 다음 문장을 사용합니다.

```plain text
아래 공개 노션 가이드를 읽어줘.

https://solid-gerbil-a05.notion.site/i-conatus-AI-3c167fab50dd80ffb19fe3111d89630c

현재 대화에 연결된 Claude in Chrome으로 실제 페이지를 열어 확인해줘.
웹 검색이나 일반적인 페이지 가져오기로 본문을 읽지 못하면
읽었다고 가정하지 말고 '접근할 수 없음'이라고 알려줘.

아직 설치하거나 실행하지 마.
먼저 자료의 전체 순서와 내 현재 상태를 확인할 질문만 알려줘.
나는 Windows를 사용하는 비개발자야.
전문 용어는 쉽게 설명하고 한 번에 한 단계씩 진행해줘.
읽기 이외의 입력·다운로드·로그인·설정 변경은 하지 마.
```

노션을 읽지 못하면 통합 Markdown 원문 주소를 전달합니다. 주소도 읽지 못하면 파일 페이지에서 Markdown을 내려받아 대화창에 첨부합니다.

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
