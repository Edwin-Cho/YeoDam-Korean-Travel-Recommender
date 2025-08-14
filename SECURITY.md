# 보안 체크리스트 (Security Checklist)

## Git 업로드 전 필수 확인사항

### ✅ 완료된 보안 조치
- [x] `.gitignore` 파일 생성 - 민감한 파일들 제외
- [x] `.env.example` 파일 생성 - API 키 템플릿 제공
- [x] 코드에서 API 키 하드코딩 제거 확인
- [x] 환경 변수 사용 확인

### 🔒 보안 파일 목록 (.gitignore에 포함됨)
- `.env` - 실제 API 키가 포함된 환경 변수 파일
- `*.pkl` - 동적 매핑 캐시 파일 (개인 검색 기록 포함 가능)
- `*.key`, `*.pem` - 인증서 및 키 파일
- `__pycache__/` - Python 캐시 파일
- `.vscode/`, `.idea/` - IDE 설정 파일 (개인 설정 포함)

### 📋 업로드 전 최종 점검
1. **API 키 확인**:
   - [ ] 코드에 실제 API 키가 하드코딩되어 있지 않은지 확인
   - [ ] 모든 API 키가 환경 변수로 처리되는지 확인
   - [ ] `.env` 파일이 `.gitignore`에 포함되어 있는지 확인

2. **개인 정보 확인**:
   - [ ] 로그 파일에 개인 정보가 없는지 확인
   - [ ] 캐시 파일이 제외되어 있는지 확인
   - [ ] 테스트 데이터에 실제 개인 정보가 없는지 확인

3. **Git 상태 확인**:
   ```bash
   git status
   git add .
   git status  # 추가된 파일 목록 재확인
   ```

### 🚨 절대 업로드하면 안 되는 것들
- 실제 API 키
- 개인 검색 기록
- 로그인 정보
- 데이터베이스 연결 문자열
- 개인 설정 파일

### 💡 추가 보안 권장사항
1. **Repository 설정**:
   - Private repository 사용 권장 (민감한 프로젝트의 경우)
   - Branch protection rules 설정

2. **API 키 관리**:
   - Google Cloud Console에서 API 키 제한 설정
   - 정기적인 API 키 로테이션
   - 사용량 모니터링 및 알림 설정

3. **코드 리뷰**:
   - 커밋 전 코드 리뷰
   - 자동화된 보안 스캔 도구 사용 고려

## 응급 상황 대응
만약 실수로 API 키를 업로드했다면:
1. 즉시 해당 API 키를 비활성화
2. 새로운 API 키 생성
3. Git 히스토리에서 민감한 정보 제거 (git filter-branch 또는 BFG Repo-Cleaner 사용)
4. Force push로 히스토리 업데이트
