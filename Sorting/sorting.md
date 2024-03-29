# 정렬 알고리즘

## 선택 정렬 (Selection Sort)

- 선택 정렬의 시간복잡도는 `O(N^2)` 이라고 할 수 있습니다.
- 그렇기에 데이터가 늘어나는 경우 정렬 속도가 급격히 늘어날 수 있습니다.
- 하지만 코딩테스트에서는 **특정한 리스트에서 가장 작은 데이터를 찾는 일**이 매우 자주 등장하므로 아래의 소스코드 형태에 익숙해질 필요가 있습니다.

### 📟 소스코드
```python
array = [ 데이터가 들어가 있다고 생각해주세요. ] # 정렬이 되어야 할 배열이라고 가정.

for i in range(len(array)):
    min_index = i # 가장 작은 원소의 인덱스

    for j in range(i + 1, len(array)): # 정렬된 것을 제외한 나머지 원소
        if array[min_index] > array[j]:
            min_index = j

    array[i], array[min_index] = array[min_index], array[i] # 상호 교환 
    # 상호 교환(Swap)은 파이썬에서는 위와 같이 간단하게 구현할 수 있지만, 대부분 프로그래밍 언어에서는 명시적으로 임시 저장용 변수를 만들어 두 원소의 값을 변경해야 합니다.

print(array)

```

## 삽입 정렬 (Insertion Sort)

삽입 정렬의 가장 큰 개념은 `'데이터를 하나씩 확인하며, 각 데이터를 적절한 위치에 삽입하면 어떨까?'` 라는 전제를 깔고 있다는 것을 알아두어야 합니다.

삽입 정렬은 아래의 과정을 바탕으로 진행된다고 할 수 있습니다.
- 특정한 데이터가 적절한 위치에 들어가기 이전에, 그 앞까지의 데이터는 이미 정렬되어 있다고 가정합니다.
- 정렬되어 있는 **데이터 리스트에서 적절한 위치를 찾은 뒤에, 그 위치에 삽입되는 과정**을 거칩니다.
- 삽입 정렬의 시간 복잡도는 `O(N^2)` 이라고 할 수 있습니다. 
- 이는 선택 정렬과 유사한 시간이 걸린다고 볼 수 있지만, **현재 리스트의 데이터가 거의 정렬되어 있는 상태일 경우**에 큰 메리트가 있다고 할 수 있습니다.

### 📟 소스코드
```python
array = [ 데이터가 들어있다고 가정. ]

for i in range(1, len(array)):
    for j in range(i, 0, -1): # 인덱스 i부터 1까지 감소하며 반복.
        if array[j] < array[j - 1]: # 한 칸씩 왼쪽으로 이동.
            array[j], array[j - 1] = array[j - 1], array[j]
        else: # 자신보다 작은 데이터를 만나면 그 위치에서 정지.
            break

print(array)

```


## 퀵 정렬 (Quick Sort)

이름에서처럼 이 정렬 알고리즘은 **'빠른 정렬'** 알고리즘이다. 이러한 퀵 정렬의 가장 큰 개념은 `'**기준** 데이터를 설정하고 그 기준보다 큰 데이터와 작은 데이터의 위치를 바꾼다.'`는 것에서 유래했습니다.

퀵 정렬은 아래의 과정을 통해서 진행된다고 할 수 있습니다.
- 이 때, 사용되는 기준을 `피벗(Pivot)` 이라고 합니다.
- 피벗을 맨 앞 데이터로 잡는다고 해봅시다.
- 왼쪽 $\rightarrow$ 오른쪽 이동 : 피벗보다 작은 값 탐색하고, 없으면 계속 오른쪽으로 이동.
- 오른쪽 $\rightarrow$ 왼쪽 이동 : 피벗보다 큰 값 탐색하고, 없으면 계속 왼쪽으로 이동.
- 원하는 값을 찾았다면, 두 값 스위치 진행.
- 해당 값들 이후로 과정 반복 
- 더이상 과정을 반복할 수 없고, 경로가 전환될 경우 해당 위치의 값 두 개 중 작은 값과 피벗 데이터 스위치 진행.
- 피벗 좌우 데이터 리스트에 대하여 반복.

이러한 퀵 정렬의 평균 시간 복잡도는 `O(NlogN)` 입니다. 이는 앞선 두 정렬 알고리즘에 비해 매우 빠른 편이라고 할 수 있습니다.

### 📟 소스코드
```python
array = [ 데이터가 있다고 가정함. ]

def quick_sort(array, start, end);
    if start >= end: # 원소가 1개인 경우 종료
        return
    pivot = start # 피벗(기준점)은 첫 번째 원소라고 지정.
    left = start + 1
    right = end
    while left <= right:
        # 피벗보다 큰 데이터를 찾을 때까지 반복.
        while left <= end and array[left] <= array[pivot]:
            left += 1
        # 피벗보다 작은 데이터를 찾을 때까지 반복.
        while right > start and array[right] >= array[pivot]:
            right -= 1

        if left > right: # 엇갈렸다면 작은 데이터와 피벗을 교체.
            array[right], array[pivot] = array[pivot], array[right]
        else: # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체.
            array[left], array[right] = array[right], array[left]
        # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행.
        quick_sort(array, start, right - 1)
        quick_sort(array, right + 1, end)

quicK_sort(array, 0, len(array) - 1)
print(array)

```


## 계수 정렬 (Count Sort)

해당 정렬 알고리즘은 **`특정한 조건이 부합할 떄만 사용할 수 있지만 매우 빠른 정렬 알고리즘`** 이라고 할 수 있다.

