# 00bbff2c

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

## 関数情報

~~~json
{
  "address": "00bbff2c",
  "name": "FUN_00bbff2c",
  "size": 348,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d932ff9ccbba6e0c3a52a714174705e52694548abbfd5f71d81a98f3681a81fb",
  "source_text_sha256": "d932ff9ccbba6e0c3a52a714174705e52694548abbfd5f71d81a98f3681a81fb"
}
~~~

## 呼び出し元

- [00bbd2c4](../00bbd/00bbd2c4.md)
- [00bbfa8c](../00bbf/00bbfa8c.md)
- [00bc1710](../00bc1/00bc1710.md)
- [00bc245c](../00bc2/00bc245c.md)
- [00bc2ec8](../00bc2/00bc2ec8.md)
- [00bc5b0c](../00bc5/00bc5b0c.md)
- [00bc5fdc](../00bc5/00bc5fdc.md)
- [00bc966c](../00bc9/00bc966c.md)
- [00bca980](../00bca/00bca980.md)
- [00bd118c](../00bd1/00bd118c.md)

## 呼び出し先

- [00bbb158](../00bbb/00bbb158.md)
- [00bdb0a0](../00bdb/00bdb0a0.md)
- [00bdb180](../00bdb/00bdb180.md)
- [00bdd180](../00bdd/00bdd180.md)

## 関連文字列（未確認候補）

~~~text
"%s:%d: %s"
"out/llvm-project/libcxxabi/src/demangle/ItaniumDemangle.h"
"shrinkToSize() can't expand!"
~~~

## 疑似コード / UTF-8 2275 bytes

~~~c

undefined1  [16] FUN_00bbff2c(long param_1,ulong param_2)

{
  void *__src;
  void *pvVar1;
  undefined8 *puVar2;
  long lVar3;
  size_t __n;
  undefined8 *puVar4;
  long lVar5;
  ulong uVar6;
  ulong uVar7;
  undefined1 auVar8 [16];
  
                    /* try { // try from 00bbff34 to 00cbff3f has its CatchHandler @ 00bc838c */
  lVar5 = *(long *)(param_1 + 0x10);
  pvVar1 = *(void **)(param_1 + 0x18);
  uVar6 = (long)pvVar1 - lVar5 >> 3;
  if (uVar6 < param_2) {
                    /* WARNING: Subroutine does not return */
    FUN_00bbb158("%s:%d: %s","out/llvm-project/libcxxabi/src/demangle/ItaniumDemangle.h",0xaa0,
                 &DAT_00296866);
  }
  __src = (void *)(lVar5 + param_2 * 8);
  puVar4 = *(undefined8 **)(param_1 + 0x1330);
  __n = (long)pvVar1 - (long)__src;
  lVar3 = puVar4[1];
  uVar7 = (ulong)((int)__n + 0xf) & 0xfffffff0;
  puVar2 = puVar4;
  if (0xfef < lVar3 + uVar7) {
    if (0xff0 < uVar7) {
      puVar2 = malloc(uVar7 + 0x10);
      if (puVar2 == (undefined8 *)0x0) {
LAB_00bc0084:
                    /* WARNING: Subroutine does not return */
        _ZSt9terminatev();
      }
      *puVar2 = *puVar4;
      puVar2[1] = 0;
      *puVar4 = puVar2;
      puVar2 = puVar2 + 2;
      goto joined_r0x00bbffec;
    }
    puVar2 = malloc(0x1000);
    if (puVar2 == (undefined8 *)0x0) goto LAB_00bc0084;
    lVar3 = 0;
    *puVar2 = puVar4;
    puVar2[1] = 0;
    *(undefined8 **)(param_1 + 0x1330) = puVar2;
  }
                    /* try { // try from 00bbffd8 to 00cbffdf has its CatchHandler @ 00bc8be8 */
  puVar2[1] = lVar3 + uVar7;
  puVar2 = (undefined8 *)((long)puVar2 + lVar3 + 0x10);
joined_r0x00bbffec:
  if (pvVar1 != __src) {
    memmove(puVar2,__src,__n);
    lVar5 = *(long *)(param_1 + 0x10);
    uVar6 = *(long *)(param_1 + 0x18) - lVar5 >> 3;
  }
  if (param_2 <= uVar6) {
                    /* try { // try from 00bc0018 to 00cc0023 has its CatchHandler @ 00bc8910 */
    auVar8._8_8_ = (long)__n >> 3;
    *(ulong *)(param_1 + 0x18) = lVar5 + param_2 * 8;
    auVar8._0_8_ = puVar2;
    return auVar8;
  }
                    /* WARNING: Subroutine does not return */
  FUN_00bbb158("%s:%d: %s","out/llvm-project/libcxxabi/src/demangle/ItaniumDemangle.h",0x87,
               "shrinkToSize() can\'t expand!");
}

~~~
