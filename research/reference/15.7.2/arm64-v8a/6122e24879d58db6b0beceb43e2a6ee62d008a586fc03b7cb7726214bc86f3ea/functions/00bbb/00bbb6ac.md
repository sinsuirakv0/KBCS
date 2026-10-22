# 00bbb6ac

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00bbb6ac.md)

## 関数情報

~~~json
{
  "address": "00bbb6ac",
  "name": "FUN_00bbb6ac",
  "size": 136,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "2bbc2bda922cfa303a67b9f9392af09186862d672368c24d5fb5ba747c270e55",
  "source_text_sha256": "2bbc2bda922cfa303a67b9f9392af09186862d672368c24d5fb5ba747c270e55"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード 1/1 / UTF-8 1570 bytes

~~~c

void FUN_00bbb6ac(long param_1,long param_2,long param_3,undefined4 param_4)

{
                    /* catch() { ... } // from try @ 00bbb514 with catch @ 00bbb6b4 */
  if (*(long *)(param_1 + 8) == *(long *)(*(long *)(param_2 + 0x10) + 8)) {
                    /* catch() { ... } // from try @ 00bbb504 with catch @ 00bbb6cc */
    if (*(int *)(param_2 + 0x3c) == 0) {
                    /* catch() { ... } // from try @ 00bbb3cc with catch @ 00bbb710 */
      *(undefined4 *)(param_2 + 0x30) = param_4;
                    /* catch() { ... } // from try @ 00bbb288 with catch @ 00bbb714 */
      *(undefined4 *)(param_2 + 0x3c) = 1;
      *(long *)(param_2 + 0x20) = param_3;
      *(undefined8 *)(param_2 + 0x28) = *(undefined8 *)(param_2 + 0x50);
      return;
    }
                    /* catch() { ... } // from try @ 00bbb4f8 with catch @ 00bbb6e0 */
                    /* catch() { ... } // from try @ 00bbb3e8 with catch @ 00bbb6e4 */
    if ((*(long *)(param_2 + 0x28) != *(long *)(param_2 + 0x50)) ||
       (*(long *)(param_2 + 0x20) != param_3)) {
      *(int *)(param_2 + 0x3c) = *(int *)(param_2 + 0x3c) + 1;
                    /* catch() { ... } // from try @ 00bbb3d8 with catch @ 00bbb6fc */
      *(undefined4 *)(param_2 + 0x30) = 2;
      *(undefined1 *)(param_2 + 0x4e) = 1;
      return;
    }
    if (*(int *)(param_2 + 0x30) == 2) {
                    /* catch() { ... } // from try @ 00bbb278 with catch @ 00bbb72c */
      *(undefined4 *)(param_2 + 0x30) = param_4;
      return;
    }
  }
  return;
}

~~~
