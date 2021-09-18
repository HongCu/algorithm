def selledbook(selled):
  selled_dic = dict()
  # 개수별로 사전으로 나눈다
  for book in selled:
    if book in selled_dic:
      selled_dic[book] += 1
    else:
      selled_dic[book] = 1

  # 사전순을 고려하여 밸류값으로 정렬
  selled_dic = sorted(selled_dic.items(), key = lambda x : (-x[1], x[0]))
  return selled_dic[0][0]


def main():
  N = int(input())
  selled = [input() for _ in range(N)]

  print(selledbook(selled))

if __name__ == '__main__':
    main()