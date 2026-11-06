# 00aca2ac

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

ページ 1/1。[入口](00aca2ac.md)

## 関数情報

~~~json
{
  "address": "00aca2ac",
  "name": "FUN_00aca2ac",
  "size": 404,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "8f9e8d6884709900551428ed8f2f4f18bf0da64125df18bf99a90a84a912e2b0",
  "source_text_sha256": "8f9e8d6884709900551428ed8f2f4f18bf0da64125df18bf99a90a84a912e2b0"
}
~~~
## 呼び出し元

- [00ab3444](../00ab3/00ab3444.md)

## 呼び出し先

- [0041e380](../0041e/0041e380.md)
- [00aca440](../00aca/00aca440.md)
- [00bdb040](../00bdb/00bdb040.md)
- [00bdb060](../00bdb/00bdb060.md)
- [00bdb1b0](../00bdb/00bdb1b0.md)
- [00bdb240](../00bdb/00bdb240.md)

## 疑似コード 1/1 / UTF-8 1626 bytes

~~~c

void FUN_00aca2ac(undefined8 *param_1,ulong param_2)

{
  ulong uVar1;
  long lVar2;
  ulong uVar3;
  void *__src;
  size_t sVar4;
  void *pvVar5;
  size_t __n;
  
  pvVar5 = (void *)param_1[1];
  if ((ulong)((param_1[2] - (long)pvVar5 >> 7) * -0x5555555555555555) < param_2) {
    __src = (void *)*param_1;
    sVar4 = (long)pvVar5 - (long)__src;
    uVar1 = ((long)sVar4 >> 7) * -0x5555555555555555 + param_2;
    if (0xaaaaaaaaaaaaaa < uVar1) {
      FUN_00aca440(param_1);
LAB_00aca43c:
                    /* WARNING: Subroutine does not return */
      FUN_0041e380();
    }
    lVar2 = param_1[2] - (long)__src >> 7;
    uVar3 = lVar2 * 0x5555555555555556;
    if (uVar3 < uVar1 || uVar3 - uVar1 == 0) {
      uVar3 = uVar1;
    }
    if (0x55555555555554 < (ulong)(lVar2 * -0x5555555555555555)) {
      uVar3 = 0xaaaaaaaaaaaaaa;
    }
    if (uVar3 == 0) {
      lVar2 = 0;
    }
    else {
      if (0xaaaaaaaaaaaaaa < uVar3) goto LAB_00aca43c;
      lVar2 = _Znwm(uVar3 * 0x180);
    }
    pvVar5 = (void *)(lVar2 + ((long)sVar4 >> 7) * 0x80);
    __n = ((param_2 * 0x180 - 0x180) / 0x180) * 0x180 + 0x180;
    memset(pvVar5,0,__n);
    memcpy((void *)((long)pvVar5 - sVar4),__src,sVar4);
    *param_1 = (void *)((long)pvVar5 - sVar4);
    param_1[1] = (long)pvVar5 + __n;
    param_1[2] = lVar2 + uVar3 * 0x180;
    if (__src != (void *)0x0) {
      _ZdlPv(__src);
      return;
    }
  }
  else {
    if (param_2 != 0) {
      sVar4 = ((param_2 * 0x180 - 0x180) / 0x180) * 0x180 + 0x180;
      memset(pvVar5,0,sVar4);
      pvVar5 = (void *)((long)pvVar5 + sVar4);
    }
    param_1[1] = pvVar5;
  }
  return;
}

~~~
