# 00bfdabc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00bfdabc",
  "name": "_ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE6ignoreEli",
  "size": 360,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "df79b1c749842e650ed15e3574e94853553cac4159344cff4acc14aac3673391",
  "source_text_sha256": "df79b1c749842e650ed15e3574e94853553cac4159344cff4acc14aac3673391"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c57ea0](../00c57/00c57ea0.md)
- [00c599d0](../00c59/00c599d0.md)

## 疑似コード / UTF-8 1832 bytes

~~~c

long * _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE6ignoreEli
                 (long *param_1,long param_2,uint param_3)

{
  byte *pbVar1;
  uint uVar2;
  long *plVar3;
  long lVar4;
  char local_24 [4];
  
  param_1[1] = 0;
  _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE6sentryC1ERS3_b(local_24,param_1,1);
  if (local_24[0] == '\0') {
    return param_1;
  }
  if (param_2 == 0x7fffffffffffffff) {
    do {
      plVar3 = *(long **)((long)param_1 + *(long *)(*param_1 + -0x18) + 0x28);
      pbVar1 = (byte *)plVar3[3];
      if (pbVar1 == (byte *)plVar3[4]) {
        uVar2 = (**(code **)(*plVar3 + 0x50))();
        if (uVar2 == 0xffffffff) goto LAB_00bfdbec;
      }
      else {
        plVar3[3] = (long)(pbVar1 + 1);
        uVar2 = (uint)*pbVar1;
      }
      if (param_1[1] != 0x7fffffffffffffff) {
        param_1[1] = param_1[1] + 1;
      }
    } while (uVar2 != param_3);
  }
  else {
    lVar4 = param_1[1];
    if (lVar4 < param_2) {
      do {
        plVar3 = *(long **)((long)param_1 + *(long *)(*param_1 + -0x18) + 0x28);
        pbVar1 = (byte *)plVar3[3];
        if (pbVar1 == (byte *)plVar3[4]) {
          uVar2 = (**(code **)(*plVar3 + 0x50))();
          if (uVar2 == 0xffffffff) goto LAB_00bfdbec;
          lVar4 = param_1[1];
          if (lVar4 != 0x7fffffffffffffff) goto LAB_00bfdb90;
          lVar4 = param_1[1];
        }
        else {
          plVar3[3] = (long)(pbVar1 + 1);
          uVar2 = (uint)*pbVar1;
LAB_00bfdb90:
          lVar4 = lVar4 + 1;
          param_1[1] = lVar4;
        }
      } while (uVar2 != param_3 && lVar4 < param_2);
    }
  }
  uVar2 = 0;
LAB_00bfdbf0:
  lVar4 = (long)param_1 + *(long *)(*param_1 + -0x18);
  _ZNSt6__ndk18ios_base5clearEj(lVar4,*(uint *)(lVar4 + 0x20) | uVar2);
  return param_1;
LAB_00bfdbec:
  uVar2 = 2;
  goto LAB_00bfdbf0;
}

~~~
