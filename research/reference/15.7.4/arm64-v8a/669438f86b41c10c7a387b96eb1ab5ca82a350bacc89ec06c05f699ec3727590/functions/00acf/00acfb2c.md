# 00acfb2c

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

## 関数情報

~~~json
{
  "address": "00acfb2c",
  "name": "FUN_00acfb2c",
  "size": 592,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "7dd1421386eb8ffe72dd1039e9923b846c24ce73818e20f858537e3790eec801",
  "source_text_sha256": "7dd1421386eb8ffe72dd1039e9923b846c24ce73818e20f858537e3790eec801"
}
~~~

## 呼び出し元

- [00453c78](../00453/00453c78.md)

## 呼び出し先

- [0044abe4](../0044a/0044abe4.md)
- [00574f30](../00574/00574f30.md)
- [00574f70](../00574/00574f70.md)
- [00728090](../00728/00728090.md)
- [0073a038](../0073a/0073a038.md)
- [0073e08c](../0073e/0073e08c.md)
- [0081f580](../0081f/0081f580.md)
- [008a0c80](../008a0/008a0c80.md)
- [00acfe60](../00acf/00acfe60.md)
- [00acff98](../00acf/00acff98.md)
- [00bdb040](../00bdb/00bdb040.md)
- [00bdb060](../00bdb/00bdb060.md)
- [00bdb090](../00bdb/00bdb090.md)
- [00bdb110](../00bdb/00bdb110.md)
- [00bdb130](../00bdb/00bdb130.md)

## 関連文字列（未確認候補）

~~~text
"&accountCode="
"&clientInfo="
"&countryCode=%s&timeDifference=%d&clubId=%d"
~~~

## 疑似コード / UTF-8 4271 bytes

~~~c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

void FUN_00acfb2c(undefined2 *param_1)

{
  long lVar1;
  void *pvVar2;
  undefined1 *puVar3;
  undefined8 uVar4;
  undefined8 uVar5;
  undefined4 uVar6;
  ulong uVar7;
  ulong *puVar8;
  long lVar9;
  long lVar10;
  undefined8 uVar11;
  undefined8 local_d0;
  ulong uStack_c8;
  void *local_c0;
  byte local_88 [16];
  void *local_78;
  ulong local_70;
  undefined8 uStack_68;
  char *local_60;
  byte local_50;
  undefined1 auStack_4f [7];
  ulong local_48;
  undefined1 *local_40;
  long local_38;
  
  lVar1 = tpidr_el0;
  local_38 = *(long *)(lVar1 + 0x28);
  *param_1 = 0;
  FUN_0081f580();
  uVar7 = FUN_0073e08c();
  if ((uVar7 & 1) != 0) {
    FUN_0081f580();
    FUN_0073a038(&local_50);
    puVar8 = (ulong *)_ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6insertEmPKc
                                (&local_50,0,"&accountCode=");
    local_c0 = (void *)puVar8[2];
    uStack_c8 = puVar8[1];
    local_d0 = *puVar8;
    puVar8[1] = 0;
    puVar8[2] = 0;
    *puVar8 = 0;
    uVar7 = uStack_c8;
    pvVar2 = local_c0;
    if ((local_d0 & 1) == 0) {
      uVar7 = local_d0 >> 1 & 0x7f;
      pvVar2 = (void *)((long)&local_d0 + 1);
    }
    _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6appendEPKcm
              (param_1,pvVar2,uVar7);
    if ((local_d0 & 1) != 0) {
      _ZdlPv(local_c0);
    }
    if ((local_50 & 1) != 0) {
      _ZdlPv(local_40);
    }
  }
  local_60 = (char *)_Znwm(0x30);
  uVar5 = s__countryCode__s_timeDifference___0029ff21._16_8_;
  uVar4 = s__countryCode__s_timeDifference___0029ff21._0_8_;
  uVar11 = CONCAT53(s__countryCode__s_timeDifference___0029ff21._27_5_,
                    s__countryCode__s_timeDifference___0029ff21._24_3_);
  uStack_68 = _UNK_002b18b8;
  local_70 = _DAT_002b18b0;
  *(undefined8 *)(local_60 + 8) = s__countryCode__s_timeDifference___0029ff21._8_8_;
  *(undefined8 *)local_60 = uVar4;
  *(undefined8 *)(local_60 + 0x18) = uVar11;
  *(undefined8 *)(local_60 + 0x10) = uVar5;
  uVar4 = s__countryCode__s_timeDifference___0029ff21._35_8_;
  uVar11 = CONCAT35(s__countryCode__s_timeDifference___0029ff21._32_3_,
                    s__countryCode__s_timeDifference___0029ff21._27_5_);
  local_60[0x2b] = '\0';
  *(undefined8 *)(local_60 + 0x23) = uVar4;
  *(undefined8 *)(local_60 + 0x1b) = uVar11;
  FUN_00728090(local_88);
  FUN_00574f70(&local_d0);
  lVar9 = FUN_00574f30(&local_d0);
  lVar10 = FUN_0081f580();
  uVar11 = FUN_008a0c80(lVar10 + 0x1f90);
  uVar6 = FUN_0044abe4(uVar11,0);
  lVar9 = SUB168(SEXT816(lVar9) * SEXT816(-0x48d159e26af37c05),8);
  FUN_00acfe60(&local_50,&local_70,local_88,(lVar9 >> 10) - (lVar9 >> 0x3f),uVar6);
  puVar3 = local_40;
  if ((local_50 & 1) == 0) {
    local_48 = (ulong)(local_50 >> 1);
    puVar3 = auStack_4f;
  }
  _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6appendEPKcm
            (param_1,puVar3,local_48);
  if ((local_50 & 1) != 0) {
    _ZdlPv(local_40);
                    /* try { // try from 00acfd5c to 00bd02ef has its CatchHandler @ 00ace214 */
  }
  if ((local_88[0] & 1) != 0) {
    _ZdlPv(local_78);
  }
  if ((local_70 & 1) != 0) {
    _ZdlPv(local_60);
  }
  FUN_00acff98(&local_50);
  puVar8 = (ulong *)_ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6insertEmPKc
                              (&local_50,0,"&clientInfo=");
  local_c0 = (void *)puVar8[2];
  uStack_c8 = puVar8[1];
  local_d0 = *puVar8;
  puVar8[1] = 0;
  puVar8[2] = 0;
  *puVar8 = 0;
  uVar7 = uStack_c8;
  pvVar2 = local_c0;
  if ((local_d0 & 1) == 0) {
    uVar7 = local_d0 >> 1 & 0x7f;
    pvVar2 = (void *)((long)&local_d0 + 1);
  }
  _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6appendEPKcm
            (param_1,pvVar2,uVar7);
  if ((local_d0 & 1) != 0) {
    _ZdlPv(local_c0);
  }
  if ((local_50 & 1) != 0) {
    _ZdlPv(local_40);
  }
                    /* try { // try from 00acfd3c to 00bcfd43 has its CatchHandler @ 00ad09c8 */
  if (*(long *)(lVar1 + 0x28) != local_38) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
                    /* try { // try from 00acfd44 to 00bcfd5b has its CatchHandler @ 00ad09f0 */
  return;
}

~~~
