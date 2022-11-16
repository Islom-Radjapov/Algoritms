# from datetime import datetime as date
# import numpy as np
#
# def test():
#
#     # test 1
#     start = date.now().time()
#     for x in range(99999999):
#         x + 5
#     end = date.now().time()
#     print( f"Search completed in {end.second - start.second} seconds {end.microsecond - start.microsecond} microseconds" )
#
#     # test 2
#     start = date.now().time()
#     [x + 5 for x in range(99999999)].count()
#
#     end = date.now().time()
#     print(f"Search completed in {end.second - start.second} seconds {end.microsecond - start.microsecond} microseconds")
#
#
# # test()
#
# def my_strlen(param_1):
#     x = 0
#     try:
#         while param_1[x] != 0:
#             x += 1
#         return x
#     except:
#         return x
#
# # print( my_strlen("RaInB0w d4Sh!") )
#
#
#
# def my_strrchr(param_1, param_2):
#     x = len(param_1) - 1
#     while x > 0:
#         if param_1[x] == param_2:
#             return param_1[x:]
#         x -= 1
#
#
# # print( my_strrchr("abcabc", "b") )
# #
# # print( my_strrchr( "121212", "2") )
# #
# # print( my_strrchr("abc", "d" ) )
# def test_null():
#     res = 0
#     for string in p1:
#         for char in string:
#             for rand in p1:
#                 if string == rand:
#                     continue
#                 elif char in rand:
#                     continue
#                 else:
#                     return False
#     return True
#
#
# param8 = ["xoxAoxo", "xoxAox", "oxAox", "oxo", "A", "ooxAoxx", "oxooxo", "Axo"]
# param4 = ["bonjour", "salut", "bonjour", "bonjour"]
# def str_maxlenoc(p1, p2):
#     def test_null():
#         res = 0
#         for string in p1:
#             for char in string:
#                 for rand in p1:
#                     if string == rand:
#                         continue
#                     elif char in rand:
#                         continue
#                     else:
#                         break
#                         # return False
#                 res +=1
#         return True
#     test_null()
#     def test_string():
#         param = p1[0]
#         start = 0
#         end = len(param)
#         res1 = []
#         for p in range( int( len(param) / 2 ) ):
#             for rand in p1[1:]:
#                 if param[start:end] in rand:
#                     res1.append(param[start:end])
#                     continue
#                 else:
#                     res1 = []
#                     break
#             if len(res1) == p2 - 1:
#                 return res1
#             start += 1
#             end -= 1
#         return False
#
#     # if test_null():
#     #     # print("bit")
#     #     if test_string():
#     #         # print("bir")
#     #         return test_string()
#     #     else:
#     #         # print("222")
#     #         for x in p1[1:]:
#     #             for y in range(len(p1[0])):
#     #                 if p1[0][y] in x:
#     #                     if p1[0][y:] in x:
#     #                         return p1[0][y:]
#     #                     return p1[0][y]
#
#
#
# # print( str_maxlenoc(["xoxAoxo", "xoxAox", "oxAox"],  3) )
# # #
# # print( str_maxlenoc(param8, 8) )
# #
# #
# # print( str_maxlenoc( param4, 4 ) )
#
#
#
#
#
#
# def isPerfectSquare(num):
#     a = num ** 0.5
#     print( a )
#     print(a % 1 )
#     print( np.sqrt(num) )
#     return (num ** 0.5) % 1 == 0
#
# # print( "return=>", isPerfectSquare(14) )
#
#

def transform_to_chessboard(board):
    n = len(board)
    if any(board[0][0] ^ board[i][0] ^ board[0][j] ^ board[i][j] for i in range(n) for j in range(n)):
      return -1

    rowSum = sum(board[0])
    colSum = sum(board[i][0] for i in range(n))

    if rowSum != n // 2 and rowSum != (n + 1) // 2:
      return -1
    if colSum != n // 2 and colSum != (n + 1) // 2:
      return -1

    rowSwaps = sum(board[i][0] == (i & 1) for i in range(n))
    colSwaps = sum(board[0][i] == (i & 1) for i in range(n))

    if n & 1:
      if rowSwaps & 1:
        rowSwaps = n - rowSwaps
      if colSwaps & 1:
        colSwaps = n - colSwaps
    else:
      rowSwaps = min(rowSwaps, n - rowSwaps)
      colSwaps = min(colSwaps, n - colSwaps)

    return (rowSwaps + colSwaps) // 2


print( transform_to_chessboard( [ [0,1,1,0],
                                  [0,1,1,0],
                                  [1,0,0,1],
                                  [1,0,0,1] ] ) )

print( transform_to_chessboard(  [ [0, 1],
                                   [1, 0] ] ) )

print( transform_to_chessboard( [  [1, 0],
                                   [1, 0] ] ) )



def my_average_mark(inList):
    total = 0.0
    if not inList:
        return total
    for i in range( len(inList) ):
        total += float( inList[i]['integer']  )

    return (total / float( len(inList) ) )