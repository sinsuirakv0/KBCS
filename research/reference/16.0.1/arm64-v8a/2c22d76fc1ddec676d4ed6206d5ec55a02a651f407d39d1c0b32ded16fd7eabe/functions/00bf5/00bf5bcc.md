# 00bf5bcc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "00bf5bcc",
  "name": "_ZNSt6__ndk16stoullERKNS_12basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEEEPmi",
  "size": 380,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "a2ad63f5763b390af7cc7d12b7c5b68010a4dabf627d4d1ec3c16f28892aece8",
  "source_text_sha256": "a2ad63f5763b390af7cc7d12b7c5b68010a4dabf627d4d1ec3c16f28892aece8"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00442930](../00442/00442930.md)
- [00bf81cc](../00bf8/00bf81cc.md)
- [00c53f5c](../00c53/00c53f5c.md)
- [00c580c0](../00c58/00c580c0.md)
- [00c5e050](../00c5e/00c5e050.md)
- [00c5e0c0](../00c5e/00c5e0c0.md)

## 関連文字列（未確認候補）

~~~text
": no conversion"
": out of range"
~~~

## 疑似コード / UTF-8 2802 bytes

~~~c

ulonglong _ZNSt6__ndk16stoullERKNS_12basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEEEPmi
                    (byte *param_1,long *param_2,int param_3)

{
  wchar_t *__nptr;
  int iVar1;
  int iVar2;
  int *piVar3;
  ulonglong uVar4;
  undefined8 uVar5;
  undefined4 *puVar6;
  undefined1 local_70;
  undefined4 local_6f;
  undefined2 local_6b;
  undefined1 local_69;
  undefined1 local_58;
  undefined4 local_57;
  undefined2 local_53;
  undefined6 local_51;
  char cStack_4b;
  char cStack_4a;
  char cStack_49;
  undefined5 local_48;
  char cStack_43;
  undefined2 uStack_42;
  wchar_t *local_28;
  
  local_70 = 0xc;
  local_6f = 0x756f7473;
  local_6b = 0x6c6c;
  local_69 = 0;
  local_28 = (wchar_t *)0x0;
  __nptr = (wchar_t *)(param_1 + 4);
  if ((*param_1 & 1) != 0) {
    __nptr = *(wchar_t **)(param_1 + 0x10);
  }
  piVar3 = (int *)__errno();
  iVar1 = *piVar3;
  *piVar3 = 0;
  uVar4 = wcstoull(__nptr,&local_28,param_3);
  iVar2 = *piVar3;
  *piVar3 = iVar1;
  puVar6 = (undefined4 *)((ulong)&local_70 | 1);
  if (iVar2 != 0x22) {
    if ((long)local_28 - (long)__nptr != 0) {
      if (param_2 != (long *)0x0) {
        *param_2 = (long)local_28 - (long)__nptr >> 2;
      }
      _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEED1Ev(&local_70);
      return uVar4;
    }
    local_57 = *puVar6;
    local_53 = *(undefined2 *)(puVar6 + 1);
    local_58 = 0x2a;
    uStack_42 = 0;
    local_51 = (undefined6)s___no_conversion_002a750a._0_7_;
    cStack_4b = SUB71(s___no_conversion_002a750a._0_7_,6);
    cStack_4a = s___no_conversion_002a750a[7];
    cStack_49 = (char)s___no_conversion_002a750a._8_7_;
    local_48 = SUB75(s___no_conversion_002a750a._8_7_,1);
    cStack_43 = SUB71(s___no_conversion_002a750a._8_7_,6);
    uVar5 = FUN_00bf81cc((ulong)&local_58 | 1);
    _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEED1Ev(&local_58);
    _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEED1Ev(&local_70);
                    /* WARNING: Subroutine does not return */
    FUN_00c53f5c(uVar5);
  }
  local_57 = *puVar6;
  local_53 = *(undefined2 *)(puVar6 + 1);
  local_58 = 0x28;
  cStack_43 = 0;
  uStack_42 = 0;
  local_51._0_1_ = s___out_of_range_002b9dc6[0];
  local_51._1_1_ = s___out_of_range_002b9dc6[1];
  local_51._2_1_ = s___out_of_range_002b9dc6[2];
  local_51._3_1_ = s___out_of_range_002b9dc6[3];
  local_51._4_1_ = s___out_of_range_002b9dc6[4];
  local_51._5_1_ = s___out_of_range_002b9dc6[5];
  cStack_4b = (char)s___out_of_range_002b9dc6._6_2_;
  cStack_4a = SUB21(s___out_of_range_002b9dc6._6_2_,1);
  cStack_49 = (char)s___out_of_range_002b9dc6._8_6_;
  local_48 = SUB65(s___out_of_range_002b9dc6._8_6_,1);
                    /* WARNING: Subroutine does not return */
  FUN_00442930((ulong)&local_58 | 1);
}

~~~
