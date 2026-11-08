# 00bd1dbc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

## 関数情報

~~~json
{
  "address": "00bd1dbc",
  "name": "FUN_00bd1dbc",
  "size": 160,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ceafba58556e4f706d6a21530029f589e8b52ba3f4b604312dc94541169f7183",
  "source_text_sha256": "ceafba58556e4f706d6a21530029f589e8b52ba3f4b604312dc94541169f7183"
}
~~~

## 呼び出し元

- [00bbde18](../00bbd/00bbde18.md)

## 呼び出し先

- [00bdb180](../00bdb/00bdb180.md)
- [00bdd180](../00bdd/00bdd180.md)

## 疑似コード / UTF-8 1200 bytes

~~~c

void FUN_00bd1dbc(long param_1,undefined8 *param_2)

{
  undefined8 *puVar1;
  long lVar2;
  undefined8 uVar3;
  void *pvVar4;
  
  pvVar4 = *(void **)(param_1 + 0x1330);
  lVar2 = *(long *)((long)pvVar4 + 8);
  puVar1 = pvVar4;
  if (lVar2 - 0xfd0U < 0xfffffffffffff010) {
    puVar1 = malloc(0x1000);
    if (puVar1 == (void *)0x0) {
                    /* WARNING: Subroutine does not return */
                    /* try { // try from 00bd1e58 to 00cd1e63 has its CatchHandler @ 00bd2904 */
      _ZSt9terminatev();
    }
    lVar2 = 0;
    *puVar1 = pvVar4;
    puVar1[1] = 0;
                    /* try { // try from 00bd1e04 to 00cd1e13 has its CatchHandler @ 00bd291c */
    *(undefined8 **)(param_1 + 0x1330) = puVar1;
  }
                    /* try { // try from 00bd1e14 to 00cd1e23 has its CatchHandler @ 00bd290c */
  *(long *)((long)puVar1 + 8) = lVar2 + 0x20;
  *(undefined ***)((long)puVar1 + lVar2 + 0x10) = &PTR_FUN_00c19d68;
  *(undefined1 *)((long)puVar1 + lVar2 + 0x18) = 0x1f;
  uVar3 = *param_2;
  *(ushort *)((long)puVar1 + lVar2 + 0x19) =
       *(ushort *)((long)puVar1 + lVar2 + 0x19) & 0xf000 | 0x540;
  *(undefined8 *)((long)puVar1 + lVar2 + 0x20) = uVar3;
  return;
}

~~~
