# 00bf5aec

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "00bf5aec",
  "name": "_ZNSt6__ndk15stollERKNS_12basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEEEPmi",
  "size": 376,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "9d17a3ab785391b8d5067f2980ee5aaf51c889a7badc7464ea01a8cae55e6d2b",
  "source_text_sha256": "9d17a3ab785391b8d5067f2980ee5aaf51c889a7badc7464ea01a8cae55e6d2b"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00442970](../00442/00442970.md)
- [00bf8268](../00bf8/00bf8268.md)
- [00c53ffc](../00c53/00c53ffc.md)
- [00c58190](../00c58/00c58190.md)
- [00c5e120](../00c5e/00c5e120.md)
- [00c5e180](../00c5e/00c5e180.md)

## 関連文字列（未確認候補）

~~~text
": no conversion"
": out of range"
~~~

## 疑似コード / UTF-8 2719 bytes

~~~c

longlong _ZNSt6__ndk15stollERKNS_12basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEEEPmi
                   (byte *param_1,long *param_2,int param_3)

{
  wchar_t *__nptr;
  int iVar1;
  int iVar2;
  int *piVar3;
  longlong lVar4;
  undefined8 uVar5;
  undefined4 *puVar6;
  undefined1 local_70;
  undefined4 local_6f;
  undefined2 local_6b;
  undefined1 local_58;
  undefined4 local_57;
  undefined1 local_53;
  undefined6 local_52;
  char cStack_4c;
  char cStack_4b;
  undefined2 uStack_4a;
  undefined4 local_48;
  uint uStack_44;
  wchar_t *local_28;
  
  local_70 = 10;
  local_6f = 0x6c6f7473;
  local_6b = 0x6c;
  local_28 = (wchar_t *)0x0;
  __nptr = (wchar_t *)(param_1 + 4);
  if ((*param_1 & 1) != 0) {
    __nptr = *(wchar_t **)(param_1 + 0x10);
  }
  piVar3 = (int *)__errno();
  iVar1 = *piVar3;
  *piVar3 = 0;
  lVar4 = wcstoll(__nptr,&local_28,param_3);
  iVar2 = *piVar3;
  *piVar3 = iVar1;
  puVar6 = (undefined4 *)((ulong)&local_70 | 1);
  if (iVar2 != 0x22) {
    if ((long)local_28 - (long)__nptr != 0) {
      if (param_2 != (long *)0x0) {
        *param_2 = (long)local_28 - (long)__nptr >> 2;
      }
      _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEED1Ev(&local_70);
      return lVar4;
    }
    local_57 = *puVar6;
    local_53 = *(undefined1 *)(puVar6 + 1);
    local_58 = 0x28;
    local_52 = (undefined6)s___no_conversion_002a74ae._0_7_;
    cStack_4c = SUB71(s___no_conversion_002a74ae._0_7_,6);
    cStack_4b = s___no_conversion_002a74ae[7];
    uStack_4a = (undefined2)s___no_conversion_002a74ae._8_7_;
    local_48 = SUB74(s___no_conversion_002a74ae._8_7_,2);
    uStack_44 = (uint)SUB71(s___no_conversion_002a74ae._8_7_,6);
    uVar5 = FUN_00bf8268((ulong)&local_58 | 1);
    _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEED1Ev(&local_58);
    _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEED1Ev(&local_70);
                    /* WARNING: Subroutine does not return */
    FUN_00c53ffc(uVar5);
  }
  local_57 = *puVar6;
  local_53 = *(undefined1 *)(puVar6 + 1);
  local_58 = 0x26;
  uStack_44 = 0;
  local_52._0_1_ = s___out_of_range_002b9d72[0];
  local_52._1_1_ = s___out_of_range_002b9d72[1];
  local_52._2_1_ = s___out_of_range_002b9d72[2];
  local_52._3_1_ = s___out_of_range_002b9d72[3];
  local_52._4_1_ = s___out_of_range_002b9d72[4];
  local_52._5_1_ = s___out_of_range_002b9d72[5];
  cStack_4c = (char)s___out_of_range_002b9d72._6_2_;
  cStack_4b = SUB21(s___out_of_range_002b9d72._6_2_,1);
  uStack_4a = (undefined2)s___out_of_range_002b9d72._8_6_;
  local_48 = SUB64(s___out_of_range_002b9d72._8_6_,2);
                    /* WARNING: Subroutine does not return */
  FUN_00442970((ulong)&local_58 | 1);
}

~~~
