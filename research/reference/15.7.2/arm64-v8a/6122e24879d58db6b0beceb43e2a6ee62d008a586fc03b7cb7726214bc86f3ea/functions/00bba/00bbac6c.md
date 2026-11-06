# 00bbac6c

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

## 関数情報

~~~json
{
  "address": "00bbac6c",
  "name": "_ZNSt13bad_exceptionD0Ev",
  "size": 44,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "420a010908402ca3732f70cc043d67b5c48fff5af707aeb7b4c2bc02a3e98bab",
  "source_text_sha256": "420a010908402ca3732f70cc043d67b5c48fff5af707aeb7b4c2bc02a3e98bab"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdaf60](../00bda/00bdaf60.md)
- [00be1d50](../00be1/00be1d50.md)

## 疑似コード / UTF-8 1240 bytes

~~~c

void _ZNSt13bad_exceptionD0Ev(void *param_1)

{
                    /* catch() { ... } // from try @ 00bba0c8 with catch @ 00bbac70
                       catch() { ... } // from try @ 00bba218 with catch @ 00bbac70 */
                    /* catch() { ... } // from try @ 00bba0b0 with catch @ 00bbac74
                       catch() { ... } // from try @ 00bba200 with catch @ 00bbac74 */
                    /* catch() { ... } // from try @ 00bba094 with catch @ 00bbac78
                       catch() { ... } // from try @ 00bba1e8 with catch @ 00bbac78 */
                    /* catch() { ... } // from try @ 00bb7698 with catch @ 00bbac7c */
                    /* catch() { ... } // from try @ 00bb72e8 with catch @ 00bbac80 */
  _ZNSt20bad_array_new_lengthD1Ev();
                    /* catch() { ... } // from try @ 00bb6f34 with catch @ 00bbac84 */
                    /* catch() { ... } // from try @ 00bb6b80 with catch @ 00bbac88 */
                    /* catch() { ... } // from try @ 00bb67cc with catch @ 00bbac8c */
                    /* catch() { ... } // from try @ 00bb6418 with catch @ 00bbac90 */
                    /* catch() { ... } // from try @ 00bb6064 with catch @ 00bbac94 */
  _ZdlPv(param_1);
  return;
}

~~~
