# 00aadf8c

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00aadd90`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aad/00aadd90.md) · 移動量 `+0x1fc`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/2-3/machine_only_observed-0020.md#compare-b0219e7fa70e342e395a8b202b8a8b16)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 対応先詳細の検証待ち
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/0-1/machine_only_observed-0020.md#compare-f25e88bfab1a9d4da506e099cac70525)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aadf8c",
  "name": "thunk_FUN_00b33154",
  "size": 4,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "e13ac9c697bacaedc840925ffc666ab7ecdc744ff356eff26128dc47afa81ce7",
  "source_text_sha256": "e13ac9c697bacaedc840925ffc666ab7ecdc744ff356eff26128dc47afa81ce7"
}
~~~

## 呼び出し元

- [005b9b54](../005b9/005b9b54.md)
- [00796634](../00796/00796634.md)
- [007aa808](../007aa/007aa808.md)
- [007aad04](../007aa/007aad04.md)
- [00853c78](../00853/00853c78.md)

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 2793 bytes

~~~c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

void thunk_FUN_00b33154(undefined8 param_1,undefined8 param_2)

{
  long lVar1;
  undefined8 uVar2;
  undefined8 uVar3;
  undefined8 uVar4;
  ulong uVar5;
  undefined8 uVar6;
  undefined8 uVar7;
  undefined8 uVar8;
  ulong uStack_c0;
  undefined8 uStack_b8;
  char *pcStack_b0;
  byte bStack_88;
  char acStack_87 [8];
  undefined7 uStack_7f;
  char cStack_78;
  undefined1 uStack_77;
  undefined6 uStack_76;
  long lStack_50;
  long lStack_48;
  
  lVar1 = tpidr_el0;
  lStack_48 = *(long *)(lVar1 + 0x28);
  uVar3 = FUN_00588e6c();
  uVar4 = FUN_0058915c();
  uStack_77 = 0;
  bStack_88 = 0x20;
  uStack_7f = (undefined7)s_adjustTrackEvent_002a4c81._8_8_;
  cStack_78 = SUB81(s_adjustTrackEvent_002a4c81._8_8_,7);
  acStack_87[0] = s_adjustTrackEvent_002a4c81[0];
  acStack_87[1] = s_adjustTrackEvent_002a4c81[1];
  acStack_87[2] = s_adjustTrackEvent_002a4c81[2];
  acStack_87[3] = s_adjustTrackEvent_002a4c81[3];
  acStack_87[4] = s_adjustTrackEvent_002a4c81[4];
  acStack_87[5] = s_adjustTrackEvent_002a4c81[5];
  acStack_87[6] = s_adjustTrackEvent_002a4c81[6];
  acStack_87[7] = s_adjustTrackEvent_002a4c81[7];
  pcStack_b0 = (char *)_Znwm(0x28);
  uVar2 = s__Ljava_lang_String_Ljava_lang_St_002bc72d._16_8_;
  uVar8 = s__Ljava_lang_String_Ljava_lang_St_002bc72d._0_8_;
  uVar6 = CONCAT17(s__Ljava_lang_String_Ljava_lang_St_002bc72d[0x1f],
                   s__Ljava_lang_String_Ljava_lang_St_002bc72d._24_7_);
  uVar7 = CONCAT71(s__Ljava_lang_String_Ljava_lang_St_002bc72d._32_7_,
                   s__Ljava_lang_String_Ljava_lang_St_002bc72d[0x1f]);
  uStack_b8 = _UNK_002c2368;
  uStack_c0 = _DAT_002c2360;
  *(undefined8 *)(pcStack_b0 + 8) = s__Ljava_lang_String_Ljava_lang_St_002bc72d._8_8_;
  *(undefined8 *)pcStack_b0 = uVar8;
  *(undefined8 *)(pcStack_b0 + 0x18) = uVar6;
  *(undefined8 *)(pcStack_b0 + 0x10) = uVar2;
  *(undefined8 *)(pcStack_b0 + 0x1f) = uVar7;
  pcStack_b0[0x27] = '\0';
  lStack_50 = FUN_00589320(uVar4,&bStack_88,&uStack_c0,uVar3);
  if ((uStack_c0 & 1) != 0) {
    _ZdlPv(pcStack_b0);
  }
  if ((bStack_88 & 1) != 0) {
    _ZdlPv((void *)CONCAT62(uStack_76,CONCAT11(uStack_77,cStack_78)));
  }
  uVar5 = FUN_00589144(&lStack_50);
  if ((uVar5 & 1) != 0) {
    FUN_005898d0(&bStack_88,uVar3,param_1);
    FUN_005898d0(&uStack_c0,uVar3,param_2);
    FUN_0058915c();
    uVar6 = FUN_00589850();
    uVar7 = FUN_00589858(&bStack_88);
    uVar8 = FUN_00589858(&uStack_c0);
    if (lStack_50 != 0) {
      FUN_00574cec(uVar3,uVar6,lStack_50,uVar7,uVar8);
    }
    FUN_0058a8bc(&uStack_c0);
    FUN_0058a8bc(&bStack_88);
  }
  if (*(long *)(lVar1 + 0x28) == lStack_48) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
