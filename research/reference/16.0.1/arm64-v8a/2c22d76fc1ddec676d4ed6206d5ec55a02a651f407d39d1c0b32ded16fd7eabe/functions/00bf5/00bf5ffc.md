# 00bf5ffc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "00bf5ffc",
  "name": "_ZNSt6__ndk15stoldERKNS_12basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEEEPm",
  "size": 360,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "236138efbfa73b35b89d5cc98d19fc07db3e37a469369ad5ac92670090c6f90d",
  "source_text_sha256": "236138efbfa73b35b89d5cc98d19fc07db3e37a469369ad5ac92670090c6f90d"
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
- [00c5e0f0](../00c5e/00c5e0f0.md)

## 関連文字列（未確認候補）

~~~text
": no conversion"
": out of range"
~~~

## 疑似コード / UTF-8 2811 bytes

~~~c

undefined1  [16]
_ZNSt6__ndk15stoldERKNS_12basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEEEPm
          (byte *param_1,long *param_2)

{
  wchar_t *__nptr;
  int iVar1;
  int iVar2;
  undefined1 auVar3 [16];
  int *piVar4;
  undefined8 uVar5;
  undefined4 *puVar6;
  double dVar7;
  undefined8 extraout_var;
  undefined1 local_68;
  undefined4 local_67;
  undefined2 local_63;
  wchar_t *local_50;
  undefined1 local_48;
  undefined4 local_47;
  undefined1 local_43;
  undefined6 local_42;
  char cStack_3c;
  char cStack_3b;
  undefined2 uStack_3a;
  undefined4 local_38;
  uint uStack_34;
  
  local_68 = 10;
  local_50 = (wchar_t *)0x0;
  local_67 = 0x6c6f7473;
  local_63 = 100;
  __nptr = (wchar_t *)(param_1 + 4);
  if ((*param_1 & 1) != 0) {
    __nptr = *(wchar_t **)(param_1 + 0x10);
  }
  piVar4 = (int *)__errno();
  iVar1 = *piVar4;
  *piVar4 = 0;
  dVar7 = wcstold(__nptr,&local_50);
  iVar2 = *piVar4;
  *piVar4 = iVar1;
  puVar6 = (undefined4 *)((ulong)&local_68 | 1);
  if (iVar2 != 0x22) {
    if ((long)local_50 - (long)__nptr != 0) {
      if (param_2 != (long *)0x0) {
        *param_2 = (long)local_50 - (long)__nptr >> 2;
      }
      _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEED1Ev(&local_68);
      auVar3._8_8_ = extraout_var;
      auVar3._0_8_ = dVar7;
      return auVar3;
    }
    local_47 = *puVar6;
    local_43 = *(undefined1 *)(puVar6 + 1);
    local_48 = 0x28;
    local_42 = (undefined6)s___no_conversion_002a750a._0_7_;
    cStack_3c = SUB71(s___no_conversion_002a750a._0_7_,6);
    cStack_3b = s___no_conversion_002a750a[7];
    uStack_3a = (undefined2)s___no_conversion_002a750a._8_7_;
    local_38 = SUB74(s___no_conversion_002a750a._8_7_,2);
    uStack_34 = (uint)SUB71(s___no_conversion_002a750a._8_7_,6);
    uVar5 = FUN_00bf81cc((ulong)&local_48 | 1);
    _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEED1Ev(&local_48);
    _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEED1Ev(&local_68);
                    /* WARNING: Subroutine does not return */
    FUN_00c53f5c(uVar5);
  }
  local_47 = *puVar6;
  local_43 = *(undefined1 *)(puVar6 + 1);
  local_48 = 0x26;
  uStack_34 = 0;
  local_42._0_1_ = s___out_of_range_002b9dc6[0];
  local_42._1_1_ = s___out_of_range_002b9dc6[1];
  local_42._2_1_ = s___out_of_range_002b9dc6[2];
  local_42._3_1_ = s___out_of_range_002b9dc6[3];
  local_42._4_1_ = s___out_of_range_002b9dc6[4];
  local_42._5_1_ = s___out_of_range_002b9dc6[5];
  cStack_3c = (char)s___out_of_range_002b9dc6._6_2_;
  cStack_3b = SUB21(s___out_of_range_002b9dc6._6_2_,1);
  uStack_3a = (undefined2)s___out_of_range_002b9dc6._8_6_;
  local_38 = SUB64(s___out_of_range_002b9dc6._8_6_,2);
                    /* WARNING: Subroutine does not return */
  FUN_00442930((ulong)&local_48 | 1);
}

~~~
