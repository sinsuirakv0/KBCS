# 00ac9ddc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

## 関数情報

~~~json
{
  "address": "00ac9ddc",
  "name": "FUN_00ac9ddc",
  "size": 404,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d7855ba7d8070d250650f55e7d6b82d0ec8a2a604b174b6217bdf6133d2a22cf",
  "source_text_sha256": "d7855ba7d8070d250650f55e7d6b82d0ec8a2a604b174b6217bdf6133d2a22cf"
}
~~~

## 呼び出し元

- [00ab3400](../00ab3/00ab3400.md)

## 呼び出し先

- [0041e380](../0041e/0041e380.md)
- [00ac9f70](../00ac9/00ac9f70.md)
- [00bdaff0](../00bda/00bdaff0.md)
- [00bdb010](../00bdb/00bdb010.md)
- [00bdb160](../00bdb/00bdb160.md)
- [00bdb1f0](../00bdb/00bdb1f0.md)

## 疑似コード / UTF-8 1617 bytes

~~~c

void FUN_00ac9ddc(undefined8 *param_1,ulong param_2)

{
  ulong uVar1;
  long lVar2;
  ulong uVar3;
  void *__src;
  size_t sVar4;
  void *pvVar5;
  size_t __n;
  
  pvVar5 = (void *)param_1[1];
  if ((ulong)((param_1[2] - (long)pvVar5 >> 6) * -0x5555555555555555) < param_2) {
    __src = (void *)*param_1;
    sVar4 = (long)pvVar5 - (long)__src;
    uVar1 = ((long)sVar4 >> 6) * -0x5555555555555555 + param_2;
    if (0x155555555555555 < uVar1) {
      FUN_00ac9f70(param_1);
LAB_00ac9f6c:
                    /* WARNING: Subroutine does not return */
      FUN_0041e380();
    }
    lVar2 = param_1[2] - (long)__src >> 6;
    uVar3 = lVar2 * 0x5555555555555556;
    if (uVar3 < uVar1 || uVar3 - uVar1 == 0) {
      uVar3 = uVar1;
    }
    if (0xaaaaaaaaaaaaa9 < (ulong)(lVar2 * -0x5555555555555555)) {
      uVar3 = 0x155555555555555;
    }
    if (uVar3 == 0) {
      lVar2 = 0;
    }
    else {
      if (0x155555555555555 < uVar3) goto LAB_00ac9f6c;
      lVar2 = _Znwm(uVar3 * 0xc0);
    }
    pvVar5 = (void *)(lVar2 + ((long)sVar4 >> 6) * 0x40);
    __n = ((param_2 * 0xc0 - 0xc0) / 0xc0) * 0xc0 + 0xc0;
    memset(pvVar5,0,__n);
    memcpy((void *)((long)pvVar5 - sVar4),__src,sVar4);
    *param_1 = (void *)((long)pvVar5 - sVar4);
    param_1[1] = (long)pvVar5 + __n;
    param_1[2] = lVar2 + uVar3 * 0xc0;
    if (__src != (void *)0x0) {
      _ZdlPv(__src);
      return;
    }
  }
  else {
    if (param_2 != 0) {
      sVar4 = ((param_2 * 0xc0 - 0xc0) / 0xc0) * 0xc0 + 0xc0;
      memset(pvVar5,0,sVar4);
      pvVar5 = (void *)((long)pvVar5 + sVar4);
    }
    param_1[1] = pvVar5;
  }
  return;
}

~~~
