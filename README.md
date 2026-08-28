# i.conatus | AI 업무 자동화 가이드

**2단계로 시작하는 AI 자동화** — Windows를 사용하는 비개발자가 AI와 함께 업무 자동화를 시작하도록 돕는 무료 가이드입니다.

이 가이드는 **설치 가이드**와 **작업 가이드**, 두 개의 Markdown 파일로 나뉘어 있습니다. 설치를 돕는 AI는 시리즈 1·2·3 내용을 몰라도 되고, 이미 설치가 끝난 VS Code의 Claude Code는 설치 절차를 다시 읽을 필요가 없기 때문입니다. 처음 시작할 때는 항상 설치 가이드부터 전달합니다 — 작업 가이드는 설치 가이드가 끝에서 사용자에게 직접 전달합니다.

## 권장 사용 방법

1. 지금 쓰고 있는 AI 채팅(어떤 AI든 상관없습니다)에 아래 **설치 가이드용 시작 문장**을 그대로 붙여넣습니다.
2. AI가 계정 확인 → VS Code 설치 → Claude Code 확장 프로그램 설치 → 로그인·연결까지 안내합니다.
3. 연결이 끝나면 설치 가이드가 다음 문장(작업 가이드용)을 알려줍니다. 그 문장을 그대로 복사해 **VS Code 안의 Claude Code 채팅창**에 붙여넣습니다.
4. 이제부터는 Claude Code가 작업 폴더 만들기 → 시리즈 1 → 2 → 3 순서로 이어서 안내합니다.

Claude 데스크톱 앱의 Cowork를 쓸 수 있으면 공개 Notion 가이드를 직접 전달해도 됩니다. 노션을 읽지 못하는 AI에는 아래 Markdown 원문을 전달합니다.

## 자료 주소

- [사람이 읽는 공개 Notion 가이드](https://solid-gerbil-a05.notion.site/i-conatus-AI-3c167fab50dd80ffb19fe3111d89630c)
- [설치 가이드 원문](https://raw.githubusercontent.com/diamonds0821/i-conatus-ai-guide/main/docs/i-conatus-setup-guide.md)
- [작업 가이드 원문](https://raw.githubusercontent.com/diamonds0821/i-conatus-ai-guide/main/docs/i-conatus-work-guide.md) (설치 가이드가 끝에서 직접 전달하므로 보통은 여기를 직접 열 일이 없습니다)

### 설치 가이드용 시작 문장

```plain text
아래 가이드를 전체적으로 읽어줘.

https://raw.githubusercontent.com/diamonds0821/i-conatus-ai-guide/main/docs/i-conatus-setup-guide.md

아직 프로그램을 설치하거나 설정을 변경하지 마.
먼저 내 현재 상태와 하려는 업무를 질문해줘.

나는 Windows를 사용하는 비개발자야.
전문 용어는 쉽게 설명하고 한 번에 한 단계씩 진행해줘.
삭제, 덮어쓰기, 개인정보 업로드, 외부 전송,
결제 및 계정 변경은 반드시 내 승인을 받아줘.
```

## 관리 원칙

- Notion은 편집·관리 원본입니다.
- `docs/i-conatus-setup-guide.md`와 `docs/i-conatus-work-guide.md`는 AI에게 전달하는 배포본입니다. 의도적으로 두 파일로 나눕니다.
- `docs/assets/videos/`에는 배포본과 Notion에서 연결하는 공개 추가 영상이 있습니다.
- PDF는 각 Markdown에서 다시 만들 수 있는 선택 산출물입니다.

## Markdown 갱신

Notion 공식 CLI에 로그인한 환경에서 다음 명령을 실행합니다.

```text
python3 scripts/export_notion.py
```

설치 가이드와 작업 가이드가 함께 재생성됩니다.

검수:

```text
python3 -m unittest tests/test_export_notion.py
```

저자: **i.conatus**
