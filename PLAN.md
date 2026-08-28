# 발행 계획

## 목표

공개 Notion 가이드를 한 개의 Markdown 문서로 통합해 AI에게 주소 또는 파일 하나로 전달할 수 있게 한다.

## 선택한 방식

- 공개 GitHub 저장소에 통합 Markdown을 발행한다.
- Notion의 페이지 순서를 명시적으로 관리한다.
- 공식 Notion Markdown API를 이용해 갱신한다.
- 최초 검증은 현재 연결된 Notion 접근 권한으로 생성한다.

## 진행 상태

- [x] 공개 Notion 첫 화면에 사용방법 안내 추가
- [x] `07 AI에게 전달할 자료` 페이지 생성
- [x] 통합 Markdown 초안 생성
- [x] 통합 문서 구조·안전 문구 검수
- [x] 공식 Notion CLI 설치 및 로그인
- [x] 한 번에 갱신하는 발행 스크립트 검증
- [x] GitHub 공개 저장소 생성
- [x] 사용자 승인 후 커밋·푸시
- [x] 07 페이지에 원문·다운로드 주소 연결
- [x] Claude 데스크톱 앱 Cowork + Claude in Chrome에서 공개 노션 접근 확인
- [x] 웹 Cowork의 일반 페이지 가져오기 실패와 통합 Markdown 대체 경로 확인
- [x] 공개 첫 화면·00 시작 안내·07 전달 페이지에 사용 경로 반영
- [x] Windows용 VS Code 공식 다운로드·설치 절차 보강
- [x] macOS 기준 Claude Code 시작·추가 설정 영상을 참고자료로 연결 (2026-08-26 05/Claude Code 설치 페이지로 복원)
- [x] 공개 첫 화면을 "시작 전 확인 → 처음 시작하는 순서(1~5단계, AI 지시서 형식) → 무엇을 배우나요 → AI와 함께 시작하기 → 선택 실습" 구조로 개편
- [x] 06을 "선택 실습 — 화면 녹화와 HAR로 웹 업무 자동화하기"로 이름 변경
- [x] 99 제작·발행 관리를 개인 허브 페이지 하위로 이동해 공개 목록에서 제외
- [x] 00을 "AI 행동 원칙"만 남기고 설치 흐름 설명(사용법·진행순서·페이지바로가기)은 정리
- [x] 01 시작 준비편(0-A/0-B/체크리스트)을 개인 허브 페이지 하위로 이동 — 05 참고자료와 새 루트 흐름으로 대체됨
- [x] export_notion.py PAGES에서 01 관련 4개 항목 제거 (통합 Markdown에서도 제외)
- [x] 통합 Markdown 하나를 설치 가이드 / 작업 가이드 두 개로 분리 (export_notion.py, 루트 페이지, 07 페이지 반영)
- [ ] Windows 환경의 Claude 데스크톱 앱 Cowork에서 최종 접근 테스트
- [ ] 두 Markdown 재생성 후 새 루트 구조와의 정합성 확인
- [x] VS Code 설치→확장 검색·설치→로그인 연결 실행 영상 편집 완료 후 게시 — `docs/assets/videos/vscode-claude-code-getting-started-macos.mp4`로 이미 완성·05/Claude Code 설치 페이지에 연결 확인 완료 (2026-08-28 재확인)
- [x] 루트 페이지를 "2단계로 시작하는 AI 자동화" 부제 + 1단계/2단계 구조로 재구성 (기존 "이렇게 진행됩니다"·"(참고) AI가 진행하는 순서" 중복 섹션 삭제, 나머지는 "더 알고 싶다면"으로 하단 이동) (2026-08-28)
- [x] GitHub blob 뷰어 동영상 미리보기 실패("we can't show files that are this big") 해결 — GitHub Pages 활성화(`https://diamonds0821.github.io/i-conatus-ai-guide/`)로 영상 링크 전환, 브라우저에서 바로 재생 확인 (2026-08-28)
- [x] 07 페이지가 루트 1단계와 겹쳐 "방법 1/2/3 + 루트 프롬프트 = 4개"로 헷갈리던 문제 해결 — 07을 "루트 1단계가 막혔을 때만 보는 예외 대응"으로 재정의, 중복되던 방법2(통합 Markdown 주소) 삭제 (2026-08-28)
- [x] 예외 대응을 별도 페이지 대신 1단계 프롬프트에 인라인으로 내장 ("링크를 못 읽으면 멈추고 물어봐") — 07은 Cowork라는 별개 경로 설명만 남기고 "마지막 수단"/"순서대로 시도" 섹션 삭제 (2026-08-28)

## 산출물 위치

- Notion 루트: https://solid-gerbil-a05.notion.site/i-conatus-AI-3c167fab50dd80ffb19fe3111d89630c
- Notion 07: https://solid-gerbil-a05.notion.site/07-AI-3c667fab50dd81ff8385ec999d4679af
- 설치 가이드: `docs/i-conatus-setup-guide.md`
- 작업 가이드: `docs/i-conatus-work-guide.md`
- Claude Code 시작 참고 영상: `docs/assets/videos/vscode-claude-code-getting-started-macos.mp4`
- Claude Code 추가 설정 영상: `docs/assets/videos/claude-code-additional-settings-macos.mp4`
- GitHub 저장소: https://github.com/diamonds0821/i-conatus-ai-guide
- 설치 가이드 URL: https://raw.githubusercontent.com/diamonds0821/i-conatus-ai-guide/main/docs/i-conatus-setup-guide.md
- 작업 가이드 URL: https://raw.githubusercontent.com/diamonds0821/i-conatus-ai-guide/main/docs/i-conatus-work-guide.md
