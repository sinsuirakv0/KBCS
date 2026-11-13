# 00bf1aec

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "00bf1aec",
  "name": "_ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6assignEmc",
  "size": 324,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "e68af0ce8082cbba452f8bf0e8131ae8829714faf584dfca52abdb6b01bfef0d",
  "source_text_sha256": "e68af0ce8082cbba452f8bf0e8131ae8829714faf584dfca52abdb6b01bfef0d"
}
~~~

## 呼び出し元

- [00c5a7b0](../00c5a/00c5a7b0.md)

## 呼び出し先

- [0043b7a4](../0043b/0043b7a4.md)
- [00c57f60](../00c57/00c57f60.md)
- [00c57f80](../00c57/00c57f80.md)
- [00c58160](../00c58/00c58160.md)

## 疑似コード / UTF-8 1668 bytes

~~~c

ulong * _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6assignEmc
                  (ulong *param_1,ulong param_2,int param_3)

{
  ulong uVar1;
  byte *__s;
  ulong uVar2;
  byte *__ptr;
  ulong uVar3;
  
  uVar2 = *param_1;
  uVar1 = *param_1;
  uVar3 = 0x16;
  if ((uVar1 & 1) != 0) {
    uVar3 = (uVar2 & 0xfffffffffffffffe) - 1;
  }
  if (uVar3 < param_2) {
    if (-uVar3 - 9 < param_2 - uVar3) {
                    /* WARNING: Subroutine does not return */
      FUN_0043b7a4(param_1);
    }
    __ptr = (byte *)param_1[2];
    if ((uVar2 & 1) == 0) {
      __ptr = (byte *)((long)param_1 + 1);
    }
    if (uVar3 < 0x7ffffffffffffff3) {
      uVar2 = param_2;
      if (param_2 <= uVar3 * 2) {
        uVar2 = uVar3 * 2;
      }
      if (uVar2 < 0x17) {
        uVar3 = 0x17;
      }
      else {
        uVar3 = (uVar2 & 0xfffffffffffffff8) + 8;
        if ((uVar2 | 7) != 0x17) {
          uVar3 = uVar2 | 7;
        }
        uVar3 = uVar3 + 1;
      }
    }
    else {
      uVar3 = 0xfffffffffffffff7;
    }
    __s = (byte *)_Znwm(uVar3);
    if ((uVar1 & 1) != 0) {
      _ZdlPv(__ptr);
    }
    param_1[1] = 0;
    param_1[2] = (ulong)__s;
    *param_1 = uVar3 | 1;
LAB_00bf1be8:
    memset(__s,param_3,param_2);
    if ((*param_1 & 1) == 0) {
LAB_00bf1b98:
      *(byte *)param_1 = (byte)((int)param_2 << 1);
      goto LAB_00bf1c04;
    }
  }
  else {
    __s = (byte *)param_1[2];
    if ((uVar2 & 1) == 0) {
      __s = (byte *)((long)param_1 + 1);
    }
    if (param_2 != 0) goto LAB_00bf1be8;
    if ((uVar2 & 1) == 0) goto LAB_00bf1b98;
  }
  param_1[1] = param_2;
LAB_00bf1c04:
  __s[param_2] = 0;
  return param_1;
}

~~~
