# 005dbfbc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `005dbf7c`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005db/005dbf7c.md) · 移動量 `+0x40`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/2-3/priority-0025.md#compare-39d1152376ab588a2163f091625180e3)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 対応先詳細の検証待ち
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/1-2/priority-0026.md#compare-6297a0f6dca707c94fa521ec1c0d4637)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "005dbfbc",
  "name": "FUN_005dbfbc",
  "size": 232,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "5fb3e7f2a8a6cd6cdcd1c46311dd8d16d1701f32f6099973c26c37719d2ee92c",
  "source_text_sha256": "5fb3e7f2a8a6cd6cdcd1c46311dd8d16d1701f32f6099973c26c37719d2ee92c"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [0047ad34](../0047a/0047ad34.md)
- [0047ce14](../0047c/0047ce14.md)
- [00687ee4](../00687/00687ee4.md)
- [00689994](../00689/00689994.md)
- [00851550](../00851/00851550.md)
- [008b91d0](../008b9/008b91d0.md)
- [00a1a6f8](../00a1a/00a1a6f8.md)
- [00b3bfbc](../00b3b/00b3bfbc.md)

## 疑似コード / UTF-8 938 bytes

~~~c

void FUN_005dbfbc(long param_1,undefined8 *param_2,int *param_3,int *param_4)

{
  long lVar1;
  undefined8 uVar2;
  undefined8 uVar3;
  long lVar4;
  
  uVar3 = *param_2;
  if ((*param_3 == 2) && (*param_4 == 0)) {
    lVar4 = *(long *)(param_1 + 8);
    lVar1 = FUN_00851550();
    FUN_00b3bfbc(lVar1 + 0xc578,*(undefined4 *)(param_1 + 0x10));
    lVar1 = FUN_00851550();
    FUN_00687ee4(lVar1 + 0x1648,*(undefined4 *)(param_1 + 0x14),
                 *(undefined4 *)(*(long *)(lVar4 + 8) + (long)*(int *)(lVar4 + 0x330) * 0x68 + 100),
                 0xffffffff);
    lVar1 = FUN_00851550();
    FUN_00689994(lVar1 + 0x1648,*(undefined4 *)(param_1 + 0x18),1);
    FUN_00851550();
    FUN_00a1a6f8();
    lVar1 = FUN_00851550();
    BYTE_ARRAY_0042ebdd[lVar1 + 0x23] = 1;
  }
  else if ((*param_3 != 2) || (*param_4 != 1)) {
    return;
  }
  uVar2 = FUN_0047ad34();
  FUN_0047ce14(uVar2,0xb,0);
  FUN_008b91d0(uVar3);
  return;
}

~~~
