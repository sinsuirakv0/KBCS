# 00bfc1ac

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00bfc1ac",
  "name": "_ZNSt6__ndk18ios_base5iwordEi",
  "size": 276,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "33f2d0f183873c5a5deaa58d13deb82383a36ad6c632f98e4105f1b526678d31",
  "source_text_sha256": "33f2d0f183873c5a5deaa58d13deb82383a36ad6c632f98e4105f1b526678d31"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bfc5d4](../00bfc/00bfc5d4.md)
- [00c59130](../00c59/00c59130.md)
- [00c5b140](../00c5b/00c5b140.md)

## 関連文字列（未確認候補）

~~~text
"ios_base::clear"
~~~

## 疑似コード / UTF-8 1570 bytes

~~~c

undefined8 * _ZNSt6__ndk18ios_base5iwordEi(long param_1,int param_2)

{
  ulong uVar1;
  void *pvVar2;
  void *pvVar3;
  void *__s;
  uint uVar4;
  void *pvVar5;
  ulong uVar6;
  ulong uVar7;
  
  uVar1 = (long)param_2 + 1;
  if (*(ulong *)(param_1 + 0x68) < uVar1) {
    uVar6 = *(ulong *)(param_1 + 0x68) * 2;
    if (uVar6 < uVar1 || uVar6 - uVar1 == 0) {
      uVar6 = uVar1;
    }
    if (0xffffffffffffffe < uVar1) {
      uVar6 = 0x1fffffffffffffff;
    }
    pvVar5 = realloc(*(void **)(param_1 + 0x58),uVar6 * 8);
    if (pvVar5 == (void *)0x0) {
      uVar4 = *(uint *)(param_1 + 0x20) | 1;
      *(uint *)(param_1 + 0x20) = uVar4;
      if ((*(uint *)(param_1 + 0x24) & uVar4) == 0) {
        DAT_01128460 = 0;
        return &DAT_01128460;
      }
                    /* WARNING: Subroutine does not return */
      FUN_00bfc5d4("ios_base::clear");
    }
    uVar7 = *(ulong *)(param_1 + 0x60);
    *(void **)(param_1 + 0x58) = pvVar5;
    if ((long)uVar7 < (long)uVar6) {
      pvVar3 = (void *)(uVar6 * 8 + (long)pvVar5);
      __s = (void *)((long)pvVar5 + uVar7 * 8);
      pvVar2 = (void *)((long)__s + 8);
      if (pvVar2 <= pvVar3) {
        pvVar2 = pvVar3;
      }
      memset(__s,0,((long)pvVar2 + uVar7 * -8 + ~(ulong)pvVar5 & 0xfffffffffffffff8) + 8);
    }
    *(ulong *)(param_1 + 0x68) = uVar6;
  }
  else {
    pvVar5 = *(void **)(param_1 + 0x58);
    uVar7 = *(ulong *)(param_1 + 0x60);
  }
  if (uVar7 <= uVar1) {
    uVar7 = uVar1;
  }
  *(ulong *)(param_1 + 0x60) = uVar7;
  return (undefined8 *)((long)pvVar5 + (long)param_2 * 8);
}

~~~
