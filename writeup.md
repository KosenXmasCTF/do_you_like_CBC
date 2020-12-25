純粋なXOR CBC問題。また、CBCとは何かはWikipediaを見れば確認できる。

https://ja.wikipedia.org/wiki/%E6%9A%97%E5%8F%B7%E5%88%A9%E7%94%A8%E3%83%A2%E3%83%BC%E3%83%89#Electronic_Codebook_(ECB)

鍵が与えられているので、 writeup.py のように1バイトずつ切り出してxorを行えばフラグ `xm4s{I_like_CBC_encryption!}` を入手できる。
