# 00bbfe8c

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

## 関数情報

~~~json
{
  "address": "00bbfe8c",
  "name": "FUN_00bbfe8c",
  "size": 160,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "3d9bed1bf4dbe16b31b1b13184227038108b62e7a638929fdb61d331080f7186",
  "source_text_sha256": "3d9bed1bf4dbe16b31b1b13184227038108b62e7a638929fdb61d331080f7186"
}
~~~

## 呼び出し元

- [00bbd2c4](../00bbd/00bbd2c4.md)

## 呼び出し先

- [00bdb180](../00bdb/00bdb180.md)
- [00bdd180](../00bdd/00bdd180.md)

## 疑似コード / UTF-8 1393 bytes

~~~c

void FUN_00bbfe8c(long param_1,undefined8 *param_2)

{
  undefined8 *puVar1;
  long lVar2;
  void *pvVar3;
  undefined8 uVar4;
  undefined8 uVar5;
  
  pvVar3 = *(void **)(param_1 + 0x1330);
                    /* try { // try from 00bbfea8 to 00cbfeb3 has its CatchHandler @ 00bc83b0 */
  lVar2 = *(long *)((long)pvVar3 + 8);
                    /* try { // try from 00bbfeb4 to 00cbfebf has its CatchHandler @ 00bc83a0 */
  puVar1 = pvVar3;
  if (lVar2 - 0xfd0U < 0xfffffffffffff010) {
                    /* try { // try from 00bbfec0 to 00cbfecb has its CatchHandler @ 00bc8390 */
    puVar1 = malloc(0x1000);
    if (puVar1 == (void *)0x0) {
                    /* WARNING: Subroutine does not return */
      _ZSt9terminatev();
    }
    lVar2 = 0;
                    /* try { // try from 00bbfecc to 00cbff33 has its CatchHandler @ 00bbf52c */
    *puVar1 = pvVar3;
    puVar1[1] = 0;
    *(undefined8 **)(param_1 + 0x1330) = puVar1;
  }
  *(long *)((long)puVar1 + 8) = lVar2 + 0x20;
  *(undefined ***)((long)puVar1 + lVar2 + 0x10) = &PTR_FUN_00c19898;
  *(undefined1 *)((long)puVar1 + lVar2 + 0x18) = 10;
  uVar5 = param_2[1];
  uVar4 = *param_2;
  *(ushort *)((long)puVar1 + lVar2 + 0x19) =
       *(ushort *)((long)puVar1 + lVar2 + 0x19) & 0xf000 | 0x540;
  *(undefined8 *)((long)puVar1 + lVar2 + 0x28) = uVar5;
  *(undefined8 *)((long)puVar1 + lVar2 + 0x20) = uVar4;
  return;
}

~~~
