# 00afbfb8

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00afbfb8",
  "name": "FUN_00afbfb8",
  "size": 76,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d137a61fb6c4e013b4c4c6bc21b9ec03b295347b077674a50b720fd6903e4a99",
  "source_text_sha256": "d137a61fb6c4e013b4c4c6bc21b9ec03b295347b077674a50b720fd6903e4a99"
}
~~~

## 呼び出し元

- [00700ab8](../00700/00700ab8.md)
- [00710298](../00710/00710298.md)
- [00a4f1bc](../00a4f/00a4f1bc.md)

## 呼び出し先

- [008514b8](../00851/008514b8.md)

## 疑似コード / UTF-8 314 bytes

~~~c

void FUN_00afbfb8(int param_1,int param_2,undefined4 param_3)

{
  long lVar1;
  
                    /* try { // try from 00afbfc0 to 00bfc097 has its CatchHandler @ 00afb2b0 */
  lVar1 = FUN_008514b8();
  *(undefined4 *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84af4) = param_3;
  return;
}

~~~
