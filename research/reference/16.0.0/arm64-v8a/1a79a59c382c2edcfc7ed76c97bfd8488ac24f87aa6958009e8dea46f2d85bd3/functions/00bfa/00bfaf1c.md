# 00bfaf1c

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00bfaf1c",
  "name": "_ZNSt6__ndk18ios_base17register_callbackEPFvNS0_5eventERS0_iEi",
  "size": 224,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "0d97e7813080c2b530a8c5308607e3e3aaf563ead907a5794d1b5560e0f55648",
  "source_text_sha256": "0d97e7813080c2b530a8c5308607e3e3aaf563ead907a5794d1b5560e0f55648"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bfb11c](../00bfb/00bfb11c.md)
- [00c59ca0](../00c59/00c59ca0.md)

## 関連文字列（未確認候補）

~~~text
"ios_base::clear"
~~~

## 疑似コード / UTF-8 1511 bytes

~~~c

void _ZNSt6__ndk18ios_base17register_callbackEPFvNS0_5eventERS0_iEi
               (long param_1,undefined8 param_2,undefined4 param_3)

{
  uint uVar1;
  void *pvVar2;
  ulong uVar3;
  ulong uVar4;
  long lVar5;
  
  lVar5 = *(long *)(param_1 + 0x48);
  uVar3 = lVar5 + 1;
  if (*(ulong *)(param_1 + 0x50) < uVar3) {
    uVar4 = *(ulong *)(param_1 + 0x50) * 2;
    if (uVar4 < uVar3 || uVar4 - uVar3 == 0) {
      uVar4 = uVar3;
    }
    if (0xffffffffffffffe < uVar3) {
      uVar4 = 0x1fffffffffffffff;
    }
    pvVar2 = realloc(*(void **)(param_1 + 0x38),uVar4 << 3);
    if (pvVar2 == (void *)0x0) {
      uVar1 = *(uint *)(param_1 + 0x20) | 1;
      *(uint *)(param_1 + 0x20) = uVar1;
      if ((*(uint *)(param_1 + 0x24) & uVar1) != 0) goto LAB_00bfaff0;
    }
    *(void **)(param_1 + 0x38) = pvVar2;
    pvVar2 = realloc(*(void **)(param_1 + 0x40),uVar4 << 2);
    if (pvVar2 == (void *)0x0) {
      uVar1 = *(uint *)(param_1 + 0x20) | 1;
      *(uint *)(param_1 + 0x20) = uVar1;
      if ((*(uint *)(param_1 + 0x24) & uVar1) != 0) {
LAB_00bfaff0:
                    /* WARNING: Subroutine does not return */
        FUN_00bfb11c("ios_base::clear");
      }
    }
    lVar5 = *(long *)(param_1 + 0x48);
    *(void **)(param_1 + 0x40) = pvVar2;
    *(ulong *)(param_1 + 0x50) = uVar4;
    uVar3 = lVar5 + 1;
  }
  *(undefined8 *)(*(long *)(param_1 + 0x38) + lVar5 * 8) = param_2;
  *(undefined4 *)(*(long *)(param_1 + 0x40) + lVar5 * 4) = param_3;
  *(ulong *)(param_1 + 0x48) = uVar3;
  return;
}

~~~
