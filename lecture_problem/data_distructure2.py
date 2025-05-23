# 사용자 입력을 통해 리스트의 요소를 추가, 조회, 수정, 삭제하는 기능을 구현한다

# 빈 리스트
items = []

while True:
    print("작업을 선택하세요: ")
    print("""
1: 추가 (Create)
2: 조회 (Read)
3: 수정 (Update)
4: 삭제 (Delete)
5: 종료 (Exit)
""")
    choice = int(input("입력: "))
# 요소 추가(Create)
    if choice == 1:
        add_items = int(input("추가할 값을 입력하세요: "))
        items.append(add_items)
        print("추가 완료")
# 요소 조회 (Read)
    elif choice == 2:
        print("[현재 리스트 내용]")
        for i in range(len(items)):
            print(f"{i}: {items[i]}")
# 요소 수정 (Update)
    elif choice == 3:
        items_idx = int(input("수정할 인덱스를 입력하세요: "))
        
        if 0 <= items_idx < len(items):
            update_items = int(input("새로운 값을 입력하세요: "))
            items[items_idx] = update_items
            print("수정 완료")
        else:
            print("유효하지 않은 인덱스입니다.")
# 요소 삭제 (Delete)
    elif choice == 4:
        items_idx = int(input("삭제할 인덱스를 입력하세요: "))
        
        if 0 <= items_idx < len(items):
            items.pop(items_idx)
            print("삭제 완료")
        else:
            print("유효하지 않은 인덱스입니다.")
# 종료 (Exit)
    elif choice == 5:
        print("프로그램을 종료합니다.")
        break
    else:
        print("올바른 번호를 입력하세요.")