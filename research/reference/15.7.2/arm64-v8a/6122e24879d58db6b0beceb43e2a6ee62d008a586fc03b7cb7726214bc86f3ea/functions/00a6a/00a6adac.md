# 00a6adac

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00a6adac.md)

## 関数情報

~~~json
{
  "address": "00a6adac",
  "name": "FUN_00a6adac",
  "size": 316,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "01c2a57918160e390231e83078dbc2069a8a5f8ec66c08b593bab9b1ef422cc0",
  "source_text_sha256": "01c2a57918160e390231e83078dbc2069a8a5f8ec66c08b593bab9b1ef422cc0"
}
~~~
## 呼び出し元

- [00a6ac88](../00a6a/00a6ac88.md)
- [00a6af0c](../00a6a/00a6af0c.md)

## 呼び出し先

- [0081f580](../0081f/0081f580.md)
- [00827b94](../00827/00827b94.md)
- [008292fc](../00829/008292fc.md)
- [00829304](../00829/00829304.md)
- [0082931c](../00829/0082931c.md)
- [00829328](../00829/00829328.md)

## 疑似コード 1/1 / UTF-8 1894 bytes

~~~c

undefined8 FUN_00a6adac(long param_1)

{
  int iVar1;
  ulong uVar2;
  long lVar3;
  float fVar4;
  
  FUN_0081f580();
  uVar2 = FUN_00827b94();
  if ((uVar2 & 1) == 0) {
    FUN_0081f580();
    uVar2 = FUN_0082931c();
    if ((uVar2 & 1) == 0) {
      FUN_0081f580();
      uVar2 = FUN_00829328();
                    /* try { // try from 00a6addc to 00b6ae0b has its CatchHandler @ 00a6b6a4 */
      if (((uVar2 & 1) == 0) && (lVar3 = FUN_0081f580(), *(char *)(lVar3 + 0x347d) == '\0')) {
        return 0;
      }
    }
  }
  if (*(int *)(param_1 + 0x284) == 1) {
    FUN_0081f580();
    iVar1 = FUN_008292fc();
    if ((float)iVar1 < *(float *)(param_1 + 0x1e4)) {
      return 0;
    }
    FUN_0081f580();
    iVar1 = FUN_008292fc();
    if (*(float *)(param_1 + 0x1e4) + *(float *)(param_1 + 0x1ec) < (float)iVar1) {
      return 0;
    }
    FUN_0081f580();
    iVar1 = FUN_00829304();
    if ((float)iVar1 < *(float *)(param_1 + 0x1e8)) {
      return 0;
    }
    FUN_0081f580();
    iVar1 = FUN_00829304();
    fVar4 = *(float *)(param_1 + 0x1e8);
  }
  else {
    if (*(int *)(param_1 + 0x284) != 0) {
      return 0;
    }
    FUN_0081f580();
    iVar1 = FUN_00829304();
    if ((float)iVar1 < *(float *)(param_1 + 0x1e8)) {
      return 0;
    }
    FUN_0081f580();
    iVar1 = FUN_00829304();
    if (*(float *)(param_1 + 0x1e8) + *(float *)(param_1 + 0x1ec) < (float)iVar1) {
      return 0;
    }
    FUN_0081f580();
    iVar1 = FUN_008292fc();
                    /* try { // try from 00a6ae40 to 00b6b077 has its CatchHandler @ 00a6b6c0 */
    if ((float)iVar1 < *(float *)(param_1 + 0x1e4)) {
      return 0;
    }
    FUN_0081f580();
    iVar1 = FUN_008292fc();
    fVar4 = *(float *)(param_1 + 0x1e4);
  }
  if (fVar4 + *(float *)(param_1 + 0x1d8) < (float)iVar1) {
    return 0;
  }
  return 1;
}

~~~
