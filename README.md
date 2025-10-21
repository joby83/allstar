# Allstar

고급 자료구조 구현 프로젝트 (Advanced Data Structures Implementation)

## 개요 (Overview)

이 프로젝트는 두 가지 중요한 자료구조를 Python으로 구현합니다:
- **Red-Black Tree (레드-블랙 트리)**: 자가 균형 이진 탐색 트리
- **B+ Tree (B+ 트리)**: 데이터베이스와 파일 시스템에서 사용되는 다원 탐색 트리

## 구조 (Structure)

```
allstar/
├── red_black_tree.py        # Red-Black Tree 구현
├── bplus_tree.py            # B+ Tree 구현
├── test_red_black_tree.py   # Red-Black Tree 테스트
├── test_bplus_tree.py       # B+ Tree 테스트
├── examples.py              # 사용 예제
└── README.md                # 문서
```

## Red-Black Tree (레드-블랙 트리)

### 특징
- 자가 균형 이진 탐색 트리
- O(log n) 시간 복잡도로 삽입, 삭제, 검색 수행
- 각 노드는 빨강 또는 검정 색상을 가짐
- 균형을 유지하기 위해 회전과 색상 변경 사용

### 주요 메서드

```python
from red_black_tree import RedBlackTree

rbt = RedBlackTree()

# 삽입
rbt.insert(key, value)

# 검색
value = rbt.search(key)

# 삭제
rbt.delete(key)

# 순회
items = rbt.inorder_traversal()  # 정렬된 순서로 반환

# 트리 정보
size = len(rbt)
height = rbt.get_height()
is_empty = rbt.is_empty()
```

### Red-Black Tree 속성

1. 모든 노드는 빨강 또는 검정
2. 루트는 검정
3. 모든 리프(NIL)는 검정
4. 빨강 노드의 자식은 모두 검정
5. 모든 경로는 같은 수의 검정 노드를 포함

## B+ Tree (B+ 트리)

### 특징
- 다원 탐색 트리 (여러 자식을 가질 수 있음)
- 데이터베이스 인덱스에 최적화
- 모든 값은 리프 노드에 저장
- 리프 노드는 연결되어 있어 범위 검색에 효율적
- O(log n) 시간 복잡도로 삽입, 삭제, 검색 수행

### 주요 메서드

```python
from bplus_tree import BPlusTree

bpt = BPlusTree(order=4)  # order는 최대 자식 수

# 삽입
bpt.insert(key, value)

# 검색
value = bpt.search(key)

# 삭제
bpt.delete(key)

# 범위 검색 (B+ Tree의 강점!)
results = bpt.range_query(start_key, end_key)

# 모든 데이터 가져오기 (정렬된 순서)
all_data = bpt.get_all()

# 트리 정보
size = len(bpt)
height = bpt.get_height()
is_empty = bpt.is_empty()

# 트리 구조 출력
bpt.print_tree()
```

### B+ Tree 속성

1. 모든 값은 리프 노드에만 저장
2. 내부 노드는 탐색을 위한 키만 저장
3. 리프 노드는 연결 리스트로 연결
4. 모든 리프 노드는 같은 레벨
5. 각 노드는 ceil(order/2) ~ order 개의 자식을 가짐

## 사용 예제 (Usage Examples)

### Red-Black Tree 예제

```python
from red_black_tree import RedBlackTree

# 학생 데이터 관리
rbt = RedBlackTree()

# 데이터 삽입
rbt.insert(101, "Alice")
rbt.insert(105, "Bob")
rbt.insert(103, "Charlie")

# 검색
name = rbt.search(103)  # "Charlie"

# 정렬된 순서로 모든 데이터 가져오기
for student_id, name in rbt.inorder_traversal():
    print(f"ID: {student_id}, Name: {name}")

# 삭제
rbt.delete(105)
```

### B+ Tree 예제

```python
from bplus_tree import BPlusTree

# 제품 재고 관리
bpt = BPlusTree(order=4)

# 데이터 삽입
bpt.insert(150, "Laptop")
bpt.insert(200, "Mouse")
bpt.insert(100, "Keyboard")

# 검색
product = bpt.search(150)  # "Laptop"

# 범위 검색 (100~200 사이의 제품 ID)
products = bpt.range_query(100, 200)
for product_id, name in products:
    print(f"ID: {product_id}, Name: {name}")

# 모든 데이터 가져오기 (정렬된 순서)
all_products = bpt.get_all()
```

## 테스트 실행 (Running Tests)

```bash
# Red-Black Tree 테스트
python test_red_black_tree.py

# B+ Tree 테스트
python test_bplus_tree.py

# 사용 예제 실행
python examples.py
```

## 성능 비교 (Performance Comparison)

| 연산 | Red-Black Tree | B+ Tree |
|------|---------------|---------|
| 삽입 | O(log n) | O(log n) |
| 검색 | O(log n) | O(log n) |
| 삭제 | O(log n) | O(log n) |
| 범위 검색 | O(k + log n) | O(k + log n) - 더 효율적! |
| 순차 접근 | O(n) | O(n) - 더 효율적! |

### 사용 시나리오

**Red-Black Tree가 적합한 경우:**
- 메모리 기반 데이터 구조가 필요할 때
- 빠른 삽입/삭제가 중요할 때
- 범위 검색이 드물 때
- 간단한 키-값 저장소가 필요할 때

**B+ Tree가 적합한 경우:**
- 데이터베이스 인덱스 구현
- 파일 시스템 구현
- 범위 검색이 빈번할 때
- 순차 접근이 중요할 때
- 디스크 기반 저장이 필요할 때

## 구현 세부사항 (Implementation Details)

### Red-Black Tree
- 완전한 삽입/삭제 재균형 알고리즘 구현
- NIL 노드를 사용한 표준 구현
- 좌회전/우회전 연산 지원
- 색상 기반 균형 유지

### B+ Tree
- 가변 차수(order) 지원
- 리프 노드 연결 구현
- 노드 분할 및 병합 알고리즘
- 언더플로우/오버플로우 처리
- 효율적인 범위 검색

## 요구사항 (Requirements)

- Python 3.6 이상
- 추가 외부 라이브러리 불필요

## 라이센스 (License)

MIT License

## 기여자 (Contributors)

Superjam Team
