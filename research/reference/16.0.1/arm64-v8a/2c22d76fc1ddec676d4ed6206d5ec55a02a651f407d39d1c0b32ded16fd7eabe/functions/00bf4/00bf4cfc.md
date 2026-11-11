# 00bf4cfc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "00bf4cfc",
  "name": "_ZNSt6__ndk14stolERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPmi",
  "size": 276,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "292961000c1938a2a7a84656a25de287bee7b38d7be3979a23619850113c5705",
  "source_text_sha256": "292961000c1938a2a7a84656a25de287bee7b38d7be3979a23619850113c5705"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00442930](../00442/00442930.md)
- [00481e80](../00481/00481e80.md)
- [00bf817c](../00bf8/00bf817c.md)
- [00c53f5c](../00c53/00c53f5c.md)
- [00c580c0](../00c58/00c580c0.md)
- [00c58590](../00c58/00c58590.md)
- [00c5e050](../00c5e/00c5e050.md)

## 関連文字列（未確認候補）

~~~text
": out of range"
~~~

## 疑似コード / UTF-8 1519 bytes

~~~c

long _ZNSt6__ndk14stolERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPmi
               (byte *param_1,long *param_2,int param_3)

{
  int iVar1;
  int iVar2;
  int *piVar3;
  long lVar4;
  undefined8 uVar5;
  byte *__nptr;
  undefined1 local_70;
  undefined4 local_6f;
  undefined1 local_6b;
  byte local_58;
  undefined1 auStack_57 [15];
  undefined1 *local_48;
  char *local_28;
  
  local_70 = 8;
  local_6b = 0;
  local_6f = 0x6c6f7473;
  __nptr = *(byte **)(param_1 + 0x10);
  local_28 = (char *)0x0;
  if ((*param_1 & 1) == 0) {
    __nptr = param_1 + 1;
  }
  piVar3 = (int *)__errno();
  iVar1 = *piVar3;
  *piVar3 = 0;
  lVar4 = strtol((char *)__nptr,&local_28,param_3);
  iVar2 = *piVar3;
  *piVar3 = iVar1;
  if (iVar2 != 0x22) {
    if ((long)local_28 - (long)__nptr != 0) {
      if (param_2 != (long *)0x0) {
        *param_2 = (long)local_28 - (long)__nptr;
      }
      _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEED1Ev(&local_70);
      return lVar4;
    }
    uVar5 = FUN_00bf817c(&local_70);
    _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEED1Ev(&local_58);
    _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEED1Ev(&local_70);
                    /* WARNING: Subroutine does not return */
    FUN_00c53f5c(uVar5);
  }
  FUN_00481e80(&local_58,&local_70,": out of range");
  if ((local_58 & 1) == 0) {
    local_48 = auStack_57;
  }
                    /* WARNING: Subroutine does not return */
  FUN_00442930(local_48);
}

~~~
