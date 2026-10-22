# 00bbabf8

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00bbabf8.md)

## 関数情報

~~~json
{
  "address": "00bbabf8",
  "name": "__cxa_pure_virtual",
  "size": 24,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "cfdefc1d1845d6abecdf10031d0ef0e4e790e6f0ff43657e10e3d0beb2a9b223",
  "source_text_sha256": "cfdefc1d1845d6abecdf10031d0ef0e4e790e6f0ff43657e10e3d0beb2a9b223"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bbb090](../00bbb/00bbb090.md)

## 関連文字列（未確認候補）

~~~text
"Pure virtual function called!"
~~~
## 疑似コード 1/1 / UTF-8 766 bytes

~~~c

void __cxa_pure_virtual(void)

{
                    /* catch() { ... } // from try @ 00bb4e28 with catch @ 00bbabfc */
                    /* catch() { ... } // from try @ 00bb4a48 with catch @ 00bbac00 */
                    /* catch() { ... } // from try @ 00bb4688 with catch @ 00bbac04 */
                    /* catch() { ... } // from try @ 00bba368 with catch @ 00bbac08
                       catch() { ... } // from try @ 00bba3b0 with catch @ 00bbac08 */
                    /* WARNING: Subroutine does not return */
                    /* catch() { ... } // from try @ 00bba350 with catch @ 00bbac0c
                       catch() { ... } // from try @ 00bba398 with catch @ 00bbac0c */
  FUN_00bbb090("Pure virtual function called!");
}

~~~
