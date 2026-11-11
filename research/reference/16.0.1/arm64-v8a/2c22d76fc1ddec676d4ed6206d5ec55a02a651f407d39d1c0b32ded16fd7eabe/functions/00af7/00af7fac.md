# 00af7fac

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "00af7fac",
  "name": "FUN_00af7fac",
  "size": 76,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "68e4d63d9f10efefe2b2fda09f7b57868324aa2458a9abe0e4b99f329c5010fc",
  "source_text_sha256": "68e4d63d9f10efefe2b2fda09f7b57868324aa2458a9abe0e4b99f329c5010fc"
}
~~~

## 呼び出し元

- [00a4f3b4](../00a4f/00a4f3b4.md)

## 呼び出し先

- [008514f8](../00851/008514f8.md)

## 疑似コード / UTF-8 411 bytes

~~~c

void FUN_00af7fac(int param_1,int param_2,undefined4 param_3)

{
  long lVar1;
  
  lVar1 = FUN_008514f8();
                    /* try { // try from 00af7fe0 to 00bf7feb has its CatchHandler @ 00af8554 */
  *(undefined4 *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84af0) = param_3;
                    /* try { // try from 00af7fec to 00bf802f has its CatchHandler @ 00af7de0 */
  return;
}

~~~
