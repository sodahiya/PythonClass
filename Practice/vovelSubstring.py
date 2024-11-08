
s = "eazuodeasjhevmfcheleeldmgomahlxnhuuuaqfcxgzkdwkwtbmkanlcccvczyaovocymcmxmzqnwmyghfefdlxyhzqhzevckzdhuuilrcemkkwenzgushpuncfpgpfwncnhevwpygekelwiqofrkladrfkmamzrbiswymroojjzxzygfkvydyxmkibnxzddculxabokiqvdfvbkxxgblcthakypmzhtkxtqnvafsgcxatezsqjkrefihwymurodbbwjtwqxwtbqepqtwwtdrtecvhphdcnhqpjakimxbtuymqdnltmhslyklzvhgroeeqrvnsbwkrvpvvbywjlqtecuaonkrpntacwyzxvahcmsorygalsgccnkgokkstjxwxsqwnyuiunelcxbvarodcztuwwukvgnwvvqfgvfcfybworgpiptizoofpimgrrunduykvvfueknonsxztptlbzlrfcocerpjgemrxmsaxyllqhdkynlsnqagewykfokjqwvsswqwqykaattqghtzuwksdnyvmoqokulxkcabbygvzeqahwxrmqkexmgghipmpszmajlamlsywqrcvhpzhxabkuzzhnbjbfiglfflbfcfnjhyrsztscolzlhwdvxqubafbxdkxhkoiabhgvzphurlwrnshkmzcfdhhvrgkuppdclqsnyceamkxkyctbmtwnslzxljbimnotlmhxojvgjacdilitttdveqvgpwnttutkiksnvcuesrblpacmuapltsohnyycqjnxidkrwbndubambieqovrtpyvqrrgokragwuteupxxixycvwvmjxibhhitmdkvqafnzdzpvyydcoroomndmrseslvhkbppcqkmhxlgsjvqucvfqtwjrtheisvboaxtgtrjoamphlhqtsfdaxdyslvebypukeopxuvtkqydamcpdjydrwpfqqxekkmfgdppcqpwiwndjqkxllqplbqxgecsbnvlkeedfqcjpledqymbccmzyvwqbk"
v = {"a", "e", "i", "o", "u"}
k =5
max = 0
maxcount = 0
for i in range(len(s)):
    for j in range(i+1, len(s)+1):
        str = s[i:j]
        count =0
        if len(str)==k:
            print(str)
            for c in str:
                if c in v:
                    count +=1
            print(count)
            if count > maxcount:
                maxcount = count
                max = str
print(max)
