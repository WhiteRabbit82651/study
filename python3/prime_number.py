#encode:utf-8

# 素数を計算する
# 冗長な気もするけどコンテストに出るわけでもないので吉とする
cnt = 0
for n in range(99999):
    if n > 1:
        for x in range(n+1):
            if x > 1:
                ans = n % x
                if ans == 0:
                    break
        if n == x:
            cnt += 1
            print("%dth is %d" % (cnt, n))
