#백준 9005번 실버3 - 난이도 규칙만 알면 쉬움.
how_ex = int(input()) #몇 번 반복할지 입력
input_lst = [] 
lst = [1, 2, 4] #11미만의 반복되는 숫자들의 값이 저장될 리스트 
 # 규칙 : 4이상의 숫자부터 1, 2, 3에 해당하는 숫자들의 횟수의 합과 같음
 # 즉, i[5] = i[4] + i[3] + i[2] 임
for j in range(2, 9): 
    lst.insert(j+1, lst[j-2] + lst[j-1] + lst[j] )
#앞에서 입력한 인풋만큼 작성 가능하도록한 입력기
for i in range(how_ex):
    x = int(input())
    input_lst.append(x)
for k in input_lst: #결과 출력기
    print(lst[k-1])