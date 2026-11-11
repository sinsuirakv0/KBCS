# 00af9bfc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "00af9bfc",
  "name": "FUN_00af9bfc",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b3928f8ce84dd4dba6d4c72cd209fc8702a868d688e63c5f16c05b24f38c4b3e",
  "source_text_sha256": "b3928f8ce84dd4dba6d4c72cd209fc8702a868d688e63c5f16c05b24f38c4b3e"
}
~~~

## 呼び出し元

- [0070ea5c](../0070e/0070ea5c.md)

## 呼び出し先

- [005e7420](../005e7/005e7420.md)
- [008514f8](../00851/008514f8.md)

## 疑似コード / UTF-8 1095 bytes

~~~c

bool FUN_00af9bfc(int param_1,int param_2)

{
  bool bVar1;
  long lVar2;
  ulong uVar3;
  
  lVar2 = FUN_008514f8();
                    /* try { // try from 00af9c14 to 00bf9c1b has its CatchHandler @ 00af9c48 */
                    /* catch() { ... } // from try @ 00af9b58 with catch @ 00af9c1c
                       try { // try from 00af9c1c to 00bf9d0f has its CatchHandler @ 00af981c */
  uVar3 = FUN_005e7420(lVar2 + (long)param_1 * 0x1f0 + 0x2768);
  if ((uVar3 & 1) == 0) {
    bVar1 = false;
  }
  else {
                    /* catch() { ... } // from try @ 00af9944 with catch @ 00af9c34 */
    lVar2 = FUN_008514f8();
                    /* catch() { ... } // from try @ 00af98b4 with catch @ 00af9c48
                       catch() { ... } // from try @ 00af9c14 with catch @ 00af9c48 */
    bVar1 = *(int *)(lVar2 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84a78) != 0;
  }
                    /* catch() { ... } // from try @ 00af9868 with catch @ 00af9c60 */
                    /* catch() { ... } // from try @ 00af9854 with catch @ 00af9c68 */
  return bVar1;
}

~~~
