# 00bfdbfc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bfd7d4`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfd/00bfd7d4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/2-3/priority-0086.md#compare-82819b04d7b72f42f48a524212f61790)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 対応先詳細の検証待ち
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/0-1/priority-0096.md#compare-95c990e922c8b87a0911922bd8648247)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bfdbfc",
  "name": "_ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE7getlineEPcl",
  "size": 144,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "3f57dc6c5697719541ae289046a2e30ef9ef39c4647f81513be31e499328c20d",
  "source_text_sha256": "3f57dc6c5697719541ae289046a2e30ef9ef39c4647f81513be31e499328c20d"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c58270](../00c58/00c58270.md)
- [00c58280](../00c58/00c58280.md)
- [00c58290](../00c58/00c58290.md)
- [00c5e390](../00c5e/00c5e390.md)

## 疑似コード / UTF-8 644 bytes

~~~c

void _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE7getlineEPcl
               (long *param_1,undefined8 param_2,undefined8 param_3)

{
  undefined4 uVar1;
  long *plVar2;
  undefined1 auStack_38 [8];
  
  _ZNKSt6__ndk18ios_base6getlocEv(auStack_38,(long)param_1 + *(long *)(*param_1 + -0x18));
  plVar2 = (long *)_ZNKSt6__ndk16locale9use_facetERNS0_2idE
                             (auStack_38,PTR__ZNSt6__ndk15ctypeIcE2idE_00c9ac30);
  uVar1 = (**(code **)(*plVar2 + 0x38))(plVar2,10);
  _ZNSt6__ndk16localeD1Ev(auStack_38);
  _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE7getlineEPclc(param_1,param_2,param_3,uVar1);
  return;
}

~~~
