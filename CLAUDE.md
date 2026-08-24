# i.conatus AI 업무 자동화 가이드

## 프로젝트 목적

Notion에서 관리하는 업무 자동화 가이드를 AI가 안정적으로 읽을 수 있는 단일 Markdown 문서로 발행한다.

## 핵심 원칙

- 저자는 모든 문서에서 `i.conatus`로 표기한다.
- 독자는 Windows를 사용하는 비개발자다.
- Notion은 편집·관리 원본이고, `docs/i-conatus-ai-guide.md`는 AI가 노션을 읽지 못할 때 사용하는 통합 배포본이다.
- 노션을 AI에게 직접 전달할 때는 Claude 데스크톱 앱의 Cowork와 Claude in Chrome을 기본 경로로 안내한다.
- 웹 Cowork와 데스크톱 앱 Cowork가 같은 방식으로 노션을 읽는다고 가정하지 않는다.
- 배포본에는 `99 제작·발행 관리`를 포함하지 않는다.
- 고정된 최종 확인일을 넣지 않는다.
- 삭제·덮어쓰기·개인정보 업로드·외부 전송·결제·계정 변경은 사람의 승인을 요구한다.
- 비밀값은 저장소와 채팅에 넣지 않는다.

## 파일 구조

- `docs/i-conatus-ai-guide.md`: AI에게 전달하는 통합 Markdown
- `scripts/export_notion.py`: Notion 원본을 정해진 순서로 결합하는 발행 스크립트
- `PLAN.md`: 구현 진행과 산출물 위치

## 변경할 때

1. Notion 원본을 먼저 수정한다.
2. 발행 스크립트로 통합 Markdown을 다시 만든다.
3. 문서 구조와 안전 문구를 검수한다.
4. 사용자 승인 후 커밋·푸시한다.
