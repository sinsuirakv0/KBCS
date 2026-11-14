# 00afb0ec

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00afb0ec",
  "name": "FUN_00afb0ec",
  "size": 144,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "20cbb5288e72b57972e76ce5b7596d73d4a6882171f09bde1446b4ae6bce53d8",
  "source_text_sha256": "20cbb5288e72b57972e76ce5b7596d73d4a6882171f09bde1446b4ae6bce53d8"
}
~~~

## 呼び出し元

- [00a50418](../00a50/00a50418.md)

## 呼び出し先

- [005e7810](../005e7/005e7810.md)
- [008524fc](../00852/008524fc.md)

## 疑似コード / UTF-8 694 bytes

~~~c

void FUN_00afb0ec(int param_1,int param_2,undefined4 param_3,undefined4 param_4)

{
  long lVar1;
  ulong uVar2;
  
  lVar1 = FUN_008524fc();
  uVar2 = FUN_005e7810(lVar1 + (long)param_1 * 0x1f0 + 0x2768);
  if ((uVar2 & 1) != 0) {
    lVar1 = FUN_008524fc();
                    /* try { // try from 00afb138 to 00bfb15b has its CatchHandler @ 00afb9d0 */
    *(undefined4 *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84c5c) = param_3;
    lVar1 = FUN_008524fc();
                    /* try { // try from 00afb164 to 00bfb16b has its CatchHandler @ 00afbab0 */
    *(undefined4 *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84c60) = param_4;
  }
  return;
}

~~~
