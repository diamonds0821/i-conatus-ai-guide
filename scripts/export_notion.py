#!/usr/bin/env python3
"""Notion 가이드를 AI용 단일 Markdown으로 발행한다."""

from __future__ import annotations

import json
import re
import shutil
import subprocess
import tempfile
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
OUTPUT_PATH = PROJECT_ROOT / "docs" / "i-conatus-ai-guide.md"
CLI_PATH = shutil.which("ntn") or str(Path.home() / ".local" / "bin" / "ntn")

PAGES = [
    ("00 시작 안내", "3c167fab-50dd-8111-ade7-d2e7237bd9b8", 2),
    ("01 시작 준비편", "3c167fab-50dd-8125-ba35-e6afbaff043b", 2),
    ("0-A Claude 채팅과 설치하기", "3c167fab-50dd-81c6-936f-ed47a1875391", 3),
    ("0-B Claude Code로 인계하기", "3c167fab-50dd-8132-b7a2-f1360a7fc527", 3),
    ("준비 완료 체크리스트", "3c167fab-50dd-8170-be29-ffaf8b9096f1", 3),
    ("02 시리즈 1 — Claude Code와 일하는 법", "3c167fab-50dd-8183-8779-f5c96f6ad614", 2),
    ("1장. Claude Code에 일을 맡기기 전에", "3c167fab-50dd-8116-aded-cd800e840431", 3),
    ("2장. 좋은 질문에 필요한 네 가지", "3c167fab-50dd-8185-8eff-c75363639d72", 3),
    ("3장. AI가 먼저 질문하게 만들기", "3c167fab-50dd-8120-9b6d-e98c08ccba9b", 3),
    ("4장. 계획과 실행을 분리하기", "3c167fab-50dd-813f-9552-cd2420bfa193", 3),
    ("5장. 가장 작은 작업부터 검증하기", "3c167fab-50dd-81f2-be92-cd4e69af646e", 3),
    ("6장. AI의 결과를 확인하고 수정시키기", "3c167fab-50dd-8111-8431-ee4a7ab91d90", 3),
    ("7장. 승인해야 할 것과 맡겨도 되는 것", "3c167fab-50dd-816d-abbf-fdec111542ef", 3),
    ("8장. 다음 대화와 다음 기기로 이어가기", "3c167fab-50dd-8197-8259-e5a0cdcbfa08", 3),
    ("최종 실습. 내 업무 자동화 질문서 만들기", "3c167fab-50dd-81d8-bb12-eadc1d901427", 3),
    ("03 시리즈 2 — 내 업무를 자동화하는 법", "3c167fab-50dd-81d9-a26f-c4de33e8e7de", 2),
    ("1장 — 자동화할 업무 하나 선택하기", "3c667fab-50dd-81d8-9177-f7c2cc20ce51", 3),
    ("2장 — 사람이 하는 과정을 기록하기", "3c667fab-50dd-81a2-84fd-e53788c17013", 3),
    ("3장 — 입력·처리·결과로 나누기", "3c667fab-50dd-817b-a00d-d733b856536f", 3),
    ("4장 — 규칙과 암묵적인 판단 분리하기", "3c667fab-50dd-819c-8b44-f616827ae1fb", 3),
    ("5장 — 가장 먼저 자동화할 단계 고르기", "3c667fab-50dd-818e-bd89-f757efd3c283", 3),
    ("6장 — 자동화 방법 선택하기", "3c667fab-50dd-818e-86f5-c4faf5b56220", 3),
    ("7장 — 업무 규칙을 AI 스킬로 만들기", "3c667fab-50dd-81d1-bc94-c39ddabba3ad", 3),
    ("8장 — 예시 자료로 첫 자동화 검증하기", "3c667fab-50dd-813b-b611-d4e425378684", 3),
    ("9장 — 검증된 단계 연결하기", "3c667fab-50dd-8173-98b3-f8ce8b582b19", 3),
    ("최종 실습 — 내 업무 자동화 설계서", "3c667fab-50dd-8186-a004-c801eee44d0a", 3),
    ("04 시리즈 3 — 안전한 자동화", "3c167fab-50dd-813e-82f0-e97f33e87916", 2),
    ("1장 — 자동화 위험 등급 정하기", "3c667fab-50dd-81d9-a5f8-d8758a60c45e", 3),
    ("2장 — 개인정보와 회사 기밀 보호하기", "3c667fab-50dd-8104-ab57-c447dee2454e", 3),
    ("3장 — 계정·권한·비밀정보 다루기", "3c667fab-50dd-81ad-b031-de32ef638f1d", 3),
    ("4장 — 이메일·메시지·게시물 외부 전송하기", "3c667fab-50dd-81c5-a4a7-f74a838d530f", 3),
    ("5장 — 결제·계약·법률·세무 판단 다루기", "3c667fab-50dd-81cb-a441-d576fe7266f5", 3),
    ("6장 — 파일 삭제·덮어쓰기·복구 준비하기", "3c667fab-50dd-816d-920e-d343cee25bc4", 3),
    ("7장 — 무인 실행·비용·오류 감시하기", "3c667fab-50dd-810d-a06f-e5ef9ea645ba", 3),
    ("8장 — 사고가 발생했을 때 중단하고 기록하기", "3c667fab-50dd-8109-bbeb-cdfea48f82b3", 3),
    ("9장 — 검증된 범위만 단계적으로 확대하기", "3c667fab-50dd-81d7-b90c-ec3e5ed6a796", 3),
    ("최종 실습 — 안전한 자동화 운영서 만들기", "3c667fab-50dd-81e0-b46e-fd1b2a076347", 3),
    ("05 AI가 확인할 참고자료", "3c167fab-50dd-81d6-83e1-e48b9692856a", 2),
    ("Windows 환경 확인", "3c167fab-50dd-819e-b750-f73f009512cd", 3),
    ("VS Code 설치", "3c167fab-50dd-81ac-a201-f43f44170260", 3),
    ("Git for Windows 설치", "3c167fab-50dd-81ea-8ae9-d677b0aae084", 3),
    ("Claude Code 설치", "3c167fab-50dd-818a-b461-d0ab2194561f", 3),
    ("VS Code에서 Claude Code 사용", "3c167fab-50dd-81a3-bcb2-d5f08edb7854", 3),
    ("모바일 Remote Control", "3c167fab-50dd-814a-915f-fc22ae1eb96e", 3),
    ("오류가 발생했을 때", "3c167fab-50dd-8171-b717-d183f2ffdaca", 3),
    ("06 기존 공개 가이드", "3c167fab-50dd-814b-86b1-e4e620e37bbd", 2),
]

HEADER = """---
카테고리: AI WORK AUTOMATION GUIDE
부제: Windows 비개발자가 AI와 함께 시작하는 업무 자동화
저자: i.conatus
꼬리말: i.conatus | AI 업무 자동화 가이드
---

# i.conatus | AI 업무 자동화 가이드

> **이 문서는 사람과 AI가 함께 사용하는 통합 가이드입니다.**

## 이 문서를 읽는 AI에게

이 문서를 받은 즉시 설치하거나 실행하지 마세요.

1. 문서 전체의 목적과 진행 순서를 먼저 파악합니다.
2. 사용자가 Windows를 사용하는 비개발자라고 가정하고 전문 용어를 쉽게 설명합니다.
3. 사용자의 현재 상태와 하려는 업무를 먼저 질문합니다.
4. 한 번에 한 단계만 안내하고 완료 기준을 확인한 뒤 다음 단계로 이동합니다.
5. 명령어를 제시할 때 입력 위치·목적·예상되는 변화를 함께 설명합니다.
6. 삭제·덮어쓰기·개인정보 업로드·외부 전송·결제·계정·권한 변경은 사용자의 명시적인 승인을 기다립니다.
7. 비밀번호·API 키·인증번호를 채팅에 입력하도록 요청하지 않습니다.
8. 확인하지 못한 내용은 추측하지 않고 ‘확인 필요’라고 표시합니다.
9. 공식 문서와 이 가이드가 다르면 공식 문서를 우선하고 차이를 설명합니다.
10. 같은 오류가 세 번 반복되면 멈추고 원인을 다시 확인합니다.

## 처음 보고할 내용

사용자에게 다음 다섯 가지만 먼저 보고합니다.

1. 사용자가 거쳐야 할 전체 단계
2. 현재 상태를 확인하기 위한 질문
3. 설치나 설정 변경이 필요한 항목
4. 사람의 승인이 필요한 항목
5. 지금 시작해야 할 첫 번째 단계

---

"""


def fetch_page(page_id: str) -> str:
    completed = subprocess.run(
        [CLI_PATH, "pages", "get", page_id, "--json"],
        check=True,
        capture_output=True,
        text=True,
    )
    payload = json.loads(completed.stdout)
    markdown_payload = payload.get("markdown")
    if isinstance(markdown_payload, dict):
        page_markdown = markdown_payload
    else:
        page_markdown = payload

    if page_markdown.get("truncated") or page_markdown.get("unknown_block_ids"):
        raise RuntimeError(f"페이지를 전부 읽지 못했습니다: {page_id}")

    markdown = page_markdown.get("markdown")
    if not isinstance(markdown, str):
        raise RuntimeError(f"Markdown 본문 형식을 확인할 수 없습니다: {page_id}")
    return markdown


def normalize_title(value: str) -> str:
    value = re.sub(r"^\d{2}\s+", "", value)
    value = re.sub(r"[.—–-]", " ", value)
    return re.sub(r"\s+", " ", value).strip()


def clean_page(markdown: str, title: str, level: int) -> str:
    lines = markdown.replace("\r\n", "\n").split("\n")
    lines = [
        line
        for line in lines
        if not re.match(r'^<page url="[^"]+">.*</page>$', line.strip())
        and line.strip() != "<empty-block/>"
        and not re.match(r"^\[(이전|다음):", line.strip())
        and not line.strip().startswith("> 제작 원본:")
    ]
    lines = [
        re.sub(
            r"\[([^\]]+)\]\(https://app\.notion\.com/p/[^)]+\)",
            r"\1",
            line,
        )
        for line in lines
    ]

    first_content = next(
        (index for index, line in enumerate(lines) if line.strip()),
        None,
    )
    if first_content is not None and re.match(r"^#\s+", lines[first_content]):
        first_title = re.sub(r"^#\s+", "", lines[first_content]).strip()
        if normalize_title(first_title) == normalize_title(title):
            lines.pop(first_content)

    shifted = []
    for line in lines:
        match = re.match(r"^(#{1,6})\s+(.*)$", line)
        if match:
            depth = min(6, len(match.group(1)) + level)
            line = f'{"#" * depth} {match.group(2)}'
        shifted.append(line)

    body = "\n".join(shifted).strip()
    return f'{"#" * level} {title}\n\n{body}'


def build_guide() -> str:
    sections = []
    for index, (title, page_id, level) in enumerate(PAGES, start=1):
        print(f"[{index}/{len(PAGES)}] {title}")
        sections.append(clean_page(fetch_page(page_id), title, level))
    return HEADER + "\n\n---\n\n".join(sections) + "\n"


def main() -> None:
    if not Path(CLI_PATH).is_file():
        raise SystemExit(
            "Notion 공식 CLI가 설치되어 있지 않습니다. "
            "설치와 로그인을 완료한 뒤 다시 실행하세요."
        )

    guide = build_guide()
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)

    with tempfile.NamedTemporaryFile(
        mode="w",
        encoding="utf-8",
        dir=OUTPUT_PATH.parent,
        delete=False,
    ) as temporary:
        temporary.write(guide)
        temporary_path = Path(temporary.name)

    temporary_path.replace(OUTPUT_PATH)
    print(f"완료: {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
