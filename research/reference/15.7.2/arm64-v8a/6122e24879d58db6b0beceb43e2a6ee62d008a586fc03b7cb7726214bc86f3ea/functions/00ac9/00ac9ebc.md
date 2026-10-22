# 00ac9ebc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00ac9ebc.md)

## 関数情報

~~~json
{
  "address": "00ac9ebc",
  "name": "FUN_00ac9ebc",
  "size": 400,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "fb15df68fb6564ac9cf6612a67b4dce158b46449dceddbcd2715981ebc8cd5dc",
  "source_text_sha256": "fb15df68fb6564ac9cf6612a67b4dce158b46449dceddbcd2715981ebc8cd5dc"
}
~~~
## 呼び出し元

- [00ab3338](../00ab3/00ab3338.md)

## 呼び出し先

- [0041e380](../0041e/0041e380.md)
- [00aca04c](../00aca/00aca04c.md)
- [00bdaf40](../00bda/00bdaf40.md)
- [00bdaf60](../00bda/00bdaf60.md)
- [00bdb0b0](../00bdb/00bdb0b0.md)
- [00bdb140](../00bdb/00bdb140.md)

## 疑似コード 1/1 / UTF-8 1730 bytes

~~~c

void FUN_00ac9ebc(undefined8 *param_1,ulong param_2)

{
  ulong uVar1;
  void *pvVar2;
  long lVar3;
  ulong uVar4;
  void *__src;
  size_t sVar5;
  void *__s;
  size_t __n;
  
  pvVar2 = (void *)param_1[1];
  if ((ulong)((param_1[2] - (long)pvVar2 >> 4) * -0x1111111111111111) < param_2) {
    __src = (void *)*param_1;
    sVar5 = (long)pvVar2 - (long)__src;
    uVar1 = ((long)sVar5 >> 4) * -0x1111111111111111 + param_2;
    if (0x111111111111111 < uVar1) {
      FUN_00aca04c(param_1);
LAB_00aca048:
                    /* WARNING: Subroutine does not return */
      FUN_0041e380();
    }
    lVar3 = param_1[2] - (long)__src >> 4;
    uVar4 = lVar3 * -0x2222222222222222;
    if (uVar4 < uVar1 || uVar4 - uVar1 == 0) {
      uVar4 = uVar1;
    }
    if (0x88888888888887 < (ulong)(lVar3 * -0x1111111111111111)) {
      uVar4 = 0x111111111111111;
    }
    if (uVar4 == 0) {
      pvVar2 = (void *)0x0;
    }
    else {
      if (0x111111111111111 < uVar4) goto LAB_00aca048;
      pvVar2 = operator_new(uVar4 * 0xf0);
    }
    __s = (void *)((long)pvVar2 + ((long)sVar5 >> 4) * 0x10);
    __n = ((param_2 * 0xf0 - 0xf0) / 0xf0) * 0xf0 + 0xf0;
    memset(__s,0,__n);
    memcpy((void *)((long)__s - sVar5),__src,sVar5);
    *param_1 = (void *)((long)__s - sVar5);
    param_1[1] = (long)__s + __n;
    param_1[2] = (void *)((long)pvVar2 + uVar4 * 0xf0);
    if (__src != (void *)0x0) {
      operator_delete(__src);
      return;
    }
  }
  else {
    if (param_2 != 0) {
      sVar5 = ((param_2 * 0xf0 - 0xf0) / 0xf0) * 0xf0 + 0xf0;
      memset(pvVar2,0,sVar5);
      pvVar2 = (void *)((long)pvVar2 + sVar5);
    }
    param_1[1] = pvVar2;
  }
  return;
}

~~~
