# 00aaeff0

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00aaeff0",
  "name": "thunk_FUN_00b341e4",
  "size": 4,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "0d63fd4257e256c3775dc4e7d04a9b25488c761f74d4280497c8839479344e94",
  "source_text_sha256": "0d63fd4257e256c3775dc4e7d04a9b25488c761f74d4280497c8839479344e94"
}
~~~

## 呼び出し元

- [005b9f44](../005b9/005b9f44.md)
- [00796a68](../00796/00796a68.md)
- [007aac3c](../007aa/007aac3c.md)
- [007ab138](../007ab/007ab138.md)
- [00854c7c](../00854/00854c7c.md)

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 2793 bytes

~~~c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

void thunk_FUN_00b341e4(undefined8 param_1,undefined8 param_2)

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
  uVar3 = FUN_005891cc();
  uVar4 = FUN_005894bc();
  uStack_77 = 0;
  bStack_88 = 0x20;
  uStack_7f = (undefined7)s_adjustTrackEvent_002a4cf0._8_8_;
  cStack_78 = SUB81(s_adjustTrackEvent_002a4cf0._8_8_,7);
  acStack_87[0] = s_adjustTrackEvent_002a4cf0[0];
  acStack_87[1] = s_adjustTrackEvent_002a4cf0[1];
  acStack_87[2] = s_adjustTrackEvent_002a4cf0[2];
  acStack_87[3] = s_adjustTrackEvent_002a4cf0[3];
  acStack_87[4] = s_adjustTrackEvent_002a4cf0[4];
  acStack_87[5] = s_adjustTrackEvent_002a4cf0[5];
  acStack_87[6] = s_adjustTrackEvent_002a4cf0[6];
  acStack_87[7] = s_adjustTrackEvent_002a4cf0[7];
  pcStack_b0 = (char *)_Znwm(0x28);
  uVar2 = s__Ljava_lang_String_Ljava_lang_St_002bc7b7._16_8_;
  uVar8 = s__Ljava_lang_String_Ljava_lang_St_002bc7b7._0_8_;
  uVar6 = CONCAT17(s__Ljava_lang_String_Ljava_lang_St_002bc7b7[0x1f],
                   s__Ljava_lang_String_Ljava_lang_St_002bc7b7._24_7_);
  uVar7 = CONCAT71(s__Ljava_lang_String_Ljava_lang_St_002bc7b7._32_7_,
                   s__Ljava_lang_String_Ljava_lang_St_002bc7b7[0x1f]);
  uStack_b8 = _UNK_002c23f8;
  uStack_c0 = _DAT_002c23f0;
  *(undefined8 *)(pcStack_b0 + 8) = s__Ljava_lang_String_Ljava_lang_St_002bc7b7._8_8_;
  *(undefined8 *)pcStack_b0 = uVar8;
  *(undefined8 *)(pcStack_b0 + 0x18) = uVar6;
  *(undefined8 *)(pcStack_b0 + 0x10) = uVar2;
  *(undefined8 *)(pcStack_b0 + 0x1f) = uVar7;
  pcStack_b0[0x27] = '\0';
  lStack_50 = FUN_00589680(uVar4,&bStack_88,&uStack_c0,uVar3);
  if ((uStack_c0 & 1) != 0) {
    _ZdlPv(pcStack_b0);
  }
  if ((bStack_88 & 1) != 0) {
    _ZdlPv((void *)CONCAT62(uStack_76,CONCAT11(uStack_77,cStack_78)));
  }
  uVar5 = FUN_005894a4(&lStack_50);
  if ((uVar5 & 1) != 0) {
    FUN_00589c30(&bStack_88,uVar3,param_1);
    FUN_00589c30(&uStack_c0,uVar3,param_2);
    FUN_005894bc();
    uVar6 = FUN_00589bb0();
    uVar7 = FUN_00589bb8(&bStack_88);
    uVar8 = FUN_00589bb8(&uStack_c0);
    if (lStack_50 != 0) {
      FUN_0057504c(uVar3,uVar6,lStack_50,uVar7,uVar8);
    }
    FUN_0058ac1c(&uStack_c0);
    FUN_0058ac1c(&bStack_88);
  }
  if (*(long *)(lVar1 + 0x28) == lStack_48) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
