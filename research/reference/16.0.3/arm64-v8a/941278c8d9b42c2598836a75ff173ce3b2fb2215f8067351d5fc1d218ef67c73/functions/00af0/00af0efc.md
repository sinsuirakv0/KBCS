# 00af0efc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00af0efc",
  "name": "FUN_00af0efc",
  "size": 232,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "f5319cc6c270a77c9e9c40b4222d8d3789a4042d322c3f7f284dbd8d9709e5db",
  "source_text_sha256": "f5319cc6c270a77c9e9c40b4222d8d3789a4042d322c3f7f284dbd8d9709e5db"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [0047b054](../0047b/0047b054.md)
- [0047d134](../0047d/0047d134.md)
- [008b7ea8](../008b7/008b7ea8.md)
- [008ba7a4](../008ba/008ba7a4.md)
- [00a47938](../00a47/00a47938.md)
- [00a47c00](../00a47/00a47c00.md)
- [00aeb3e4](../00aeb/00aeb3e4.md)
- [00aeb640](../00aeb/00aeb640.md)

## 疑似コード / UTF-8 1160 bytes

~~~c

void FUN_00af0efc(long param_1,undefined8 *param_2,int *param_3)

{
  uint uVar1;
  undefined8 uVar2;
  undefined4 uVar3;
  undefined8 uVar4;
  long lVar5;
  
  if (*param_3 == 3) {
    uVar4 = *param_2;
    lVar5 = *(long *)(param_1 + 8);
    uVar2 = FUN_0047b054();
    FUN_0047d134(uVar2,0xb,0);
    *(byte *)(lVar5 + 0x9ec) = *(byte *)(lVar5 + 0x9ec) ^ 1;
    uVar2 = FUN_008b7ea8(uVar4);
    uVar2 = FUN_00a47938(uVar2,0);
    uVar3 = 0x90;
    if (*(char *)(lVar5 + 0x9ec) == '\0') {
      uVar3 = 0x91;
    }
    FUN_00a47c00(uVar2,uVar3);
    uVar2 = *(undefined8 *)(param_1 + 0x10);
    uVar1 = FUN_00aeb3e4(lVar5,*(undefined1 *)(lVar5 + 0x9ec));
                    /* try { // try from 00af0f98 to 00bf0f9b has its CatchHandler @ 00af14d0 */
                    /* try { // try from 00af0f9c to 00bf10c7 has its CatchHandler @ 00af0de8 */
    FUN_008ba7a4(uVar2,0,uVar1 & 1);
    uVar2 = *(undefined8 *)(param_1 + 0x10);
    uVar1 = FUN_00aeb640(lVar5,*(undefined1 *)(lVar5 + 0x9ec));
    FUN_008ba7a4(uVar2,1,uVar1 & 1);
    return;
  }
  if (*param_3 == 0) {
    uVar2 = FUN_0047b054();
    FUN_0047d134(uVar2,10,0);
    return;
  }
  return;
}

~~~
