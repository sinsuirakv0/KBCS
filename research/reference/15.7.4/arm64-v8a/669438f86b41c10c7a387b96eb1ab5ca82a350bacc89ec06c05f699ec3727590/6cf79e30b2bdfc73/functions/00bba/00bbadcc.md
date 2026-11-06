# 00bbadcc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

ページ 1/1。[入口](00bbadcc.md)

## 関数情報

~~~json
{
  "address": "00bbadcc",
  "name": "_ZNSt9bad_allocD0Ev",
  "size": 44,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "eb9a665288e7dedbd6548ffd2f05cce38a2a487ec2013fb800908f569585e707",
  "source_text_sha256": "eb9a665288e7dedbd6548ffd2f05cce38a2a487ec2013fb800908f569585e707"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdb060](../00bdb/00bdb060.md)
- [00bdbc00](../00bdb/00bdbc00.md)

## 疑似コード 1/1 / UTF-8 983 bytes

~~~c

void _ZNSt9bad_allocD0Ev(void *param_1)

{
                    /* catch() { ... } // from try @ 00bb6f54 with catch @ 00bbadd0 */
                    /* catch() { ... } // from try @ 00bb6ba0 with catch @ 00bbadd4 */
                    /* catch() { ... } // from try @ 00bb6b88 with catch @ 00bbadd8 */
                    /* catch() { ... } // from try @ 00bb67d4 with catch @ 00bbaddc */
                    /* catch() { ... } // from try @ 00bb67ec with catch @ 00bbade0 */
  _ZNSt20bad_array_new_lengthD1Ev();
                    /* catch() { ... } // from try @ 00bb6420 with catch @ 00bbade4 */
                    /* catch() { ... } // from try @ 00bb6438 with catch @ 00bbade8 */
                    /* catch() { ... } // from try @ 00bb6084 with catch @ 00bbadec */
                    /* catch() { ... } // from try @ 00bb606c with catch @ 00bbadf0 */
                    /* catch() { ... } // from try @ 00bb5cc4 with catch @ 00bbadf4 */
  _ZdlPv(param_1);
  return;
}

~~~
